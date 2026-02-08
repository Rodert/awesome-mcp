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

## 📚 Projects (3592 total)

> Last updated: **2026-02-08**

### MCP Servers

*MCP server implementations that provide protocol services*

1. **[dify](https://github.com/langgenius/dify)** - ⭐ 129,018
   Production-ready platform for agentic workflow development.

2. **[open-webui](https://github.com/open-webui/open-webui)** - ⭐ 123,255
   User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

3. **[gemini-cli](https://github.com/google-gemini/gemini-cli)** - ⭐ 93,901
   An open-source AI agent that brings the power of Gemini directly into your terminal.

4. **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** - ⭐ 80,496
   A collection of MCP servers.

5. **[servers](https://github.com/modelcontextprotocol/servers)** - ⭐ 78,234
   Model Context Protocol Servers

6. **[netdata](https://github.com/netdata/netdata)** - ⭐ 77,677
   The fastest path to AI-powered full stack observability, even for lean teams.

7. **[ragflow](https://github.com/infiniflow/ragflow)** - ⭐ 72,963
   RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

8. **[lobehub](https://github.com/lobehub/lobehub)** - ⭐ 72,065
   The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

9. **[lobe-chat](https://github.com/lobehub/lobe-chat)** - ⭐ 70,553
   :exploding_head: LobeHub - The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

10. **[anything-llm](https://github.com/Mintplex-Labs/anything-llm)** - ⭐ 54,319
   The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

11. **[TrendRadar](https://github.com/sansan0/TrendRadar)** - ⭐ 45,726
   ⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS, and smart alerts.🎯 告别信息过载，你的 AI 舆情监控助手与热点筛选工具！聚合多平台热点 +  RSS 订阅，支持关键词精准筛选。AI 翻译 +  AI 分析简报直推手机，也支持接入 MCP 架构，赋能 AI 自然语言对话分析、情感洞察与趋势预测等。支持 Docker ，数据本地/云端自持。集成微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 等渠道智能推送。

12. **[JeecgBoot](https://github.com/jeecgboot/JeecgBoot)** - ⭐ 45,192
   【AI低代码平台】AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

13. **[context7](https://github.com/upstash/context7)** - ⭐ 45,055
   Context7 MCP Server -- Up-to-date code documentation for LLMs and AI code editors

14. **[LocalAI](https://github.com/mudler/LocalAI)** - ⭐ 42,658
   :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

15. **[everything-claude-code](https://github.com/affaan-m/everything-claude-code)** - ⭐ 41,931
   Complete Claude Code configuration collection - agents, skills, hooks, commands, rules, MCPs. Battle-tested configs from an Anthropic hackathon winner.

16. **[mindsdb](https://github.com/mindsdb/mindsdb)** - ⭐ 38,419
   Federated Query Engine for AI - The only MCP Server you'll ever need

17. **[cherry-studio](https://github.com/CherryHQ/cherry-studio)** - ⭐ 37,347
   Cherry Studio boosts your productivity with unified AI access, Agent capabilities, and 300+ assistants in one desktop application.

18. **[LibreChat](https://github.com/danny-avila/LibreChat)** - ⭐ 33,709
   Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

19. **[1Panel](https://github.com/1Panel-dev/1Panel)** - ⭐ 33,113
   🔥 1Panel provides an intuitive web interface and MCP Server to manage websites, files, containers, databases, and LLMs on a Linux server.

20. **[nacos](https://github.com/alibaba/nacos)** - ⭐ 32,614
   an easy-to-use dynamic service discovery, configuration and service management platform for building AI cloud native applications.

21. **[awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** - ⭐ 32,162
   A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

22. **[PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate)** - ⭐ 31,728
   [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/MCP/Docker/Zotero

23. **[goose](https://github.com/block/goose)** - ⭐ 30,058
   an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

24. **[ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub)** - ⭐ 28,026
   In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

25. **[UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)** - ⭐ 27,296
   The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra

26. **[playwright-mcp](https://github.com/microsoft/playwright-mcp)** - ⭐ 26,841
   Playwright MCP server

27. **[github-mcp-server](https://github.com/github/github-mcp-server)** - ⭐ 26,717
   GitHub's official MCP Server

28. **[composio](https://github.com/ComposioHQ/composio)** - ⭐ 26,519
   Composio equips your AI agents & LLMs with 100+ high-quality integrations via function calling

29. **[gpt-researcher](https://github.com/assafelovic/gpt-researcher)** - ⭐ 25,240
   An autonomous agent that conducts deep research on any data using any LLM providers.

30. **[gin-vue-admin](https://github.com/flipped-aurora/gin-vue-admin)** - ⭐ 24,298
   🚀Vite+Vue3+Gin拥有AI辅助的基础开发平台，企业级业务AI+开发解决方案，内置mcp辅助服务，内置skills管理，支持TS和JS混用。它集成了JWT鉴权、权限管理、动态路由、显隐可控组件、分页封装、多点登录拦截、资源权限、上传下载、代码生成器、表单生成器和可配置的导入导出等开发必备功能。

31. **[xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)** - ⭐ 23,889
   An MCP-based chatbot | 一个基于MCP的聊天机器人

32. **[chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** - ⭐ 23,500
   Chrome DevTools for coding agents

33. **[fastmcp](https://github.com/jlowin/fastmcp)** - ⭐ 22,675
   🚀 The fast, Pythonic way to build MCP servers and clients

34. **[repomix](https://github.com/yamadashy/repomix)** - ⭐ 21,752
   📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

35. **[python-sdk](https://github.com/modelcontextprotocol/python-sdk)** - ⭐ 21,556
   The official Python SDK for Model Context Protocol servers and clients

36. **[mastra](https://github.com/mastra-ai/mastra)** - ⭐ 20,848
   From the team behind Gatsby, Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack.

37. **[activepieces](https://github.com/activepieces/activepieces)** - ⭐ 20,783
   AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • AI Automation / AI Agent with MCPs • AI Workflows & AI Agents • MCPs for AI Agents

38. **[MaxKB](https://github.com/1Panel-dev/MaxKB)** - ⭐ 20,064
   🔥 MaxKB is an open-source platform for building enterprise-grade agents.  强大易用的开源企业级智能体平台。

39. **[serena](https://github.com/oraios/serena)** - ⭐ 19,857
   A powerful coding agent toolkit providing semantic retrieval and editing capabilities (MCP server & other integrations)

40. **[agentic](https://github.com/transitive-bullshit/agentic)** - ⭐ 18,127
   Your API ⇒ Paid MCP. Instantly.

41. **[blender-mcp](https://github.com/ahujasid/blender-mcp)** - ⭐ 16,925

42. **[cc-switch](https://github.com/farion1231/cc-switch)** - ⭐ 16,762
   A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode & Gemini CLI.

43. **[agentscope](https://github.com/agentscope-ai/agentscope)** - ⭐ 16,229
   AgentScope: Agent-Oriented Programming for Building LLM Applications

44. **[mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** - ⭐ 14,262
   This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration.

45. **[claude-flow](https://github.com/ruvnet/claude-flow)** - ⭐ 13,792
   🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code support via MCP protocol. Ranked #1 in agent-based frameworks.

46. **[trigger.dev](https://github.com/triggerdotdev/trigger.dev)** - ⭐ 13,583
   Trigger.dev – build and deploy fully‑managed AI agents and workflows

47. **[electerm](https://github.com/electerm/electerm)** - ⭐ 13,567
   📻Terminal/ssh/sftp/ftp/telnet/serialport/RDP/VNC client(linux, mac, win)

48. **[filestash](https://github.com/mickael-kerjean/filestash)** - ⭐ 13,423
   :file_folder: What Dropbox should have been if it was based on SFTP, S3, FTP, SMB, NFS, WebDAV, Git, and more

49. **[n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** - ⭐ 13,298
   A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you 

50. **[Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)** - ⭐ 13,227
   Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc.

51. **[Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP)** - ⭐ 13,027
   MCP server to provide Figma layout information to AI coding agents like Cursor

52. **[genai-toolbox](https://github.com/googleapis/genai-toolbox)** - ⭐ 12,763
   MCP Toolbox for Databases is an open source MCP server for databases.

53. **[typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** - ⭐ 11,535
   The official TypeScript SDK for Model Context Protocol servers and clients

54. **[fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)** - ⭐ 11,509
   Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth!

55. **[pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server)** - ⭐ 11,024
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

56. **[nginx-ui](https://github.com/0xJacky/nginx-ui)** - ⭐ 10,584
   Yet another WebUI for Nginx

57. **[gateway](https://github.com/Portkey-AI/gateway)** - ⭐ 10,545
   A blazing fast AI Gateway with integrated guardrails. Route to 200+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.

58. **[mcp-chrome](https://github.com/hangwin/mcp-chrome)** - ⭐ 10,302
   Chrome MCP Server is a Chrome extension-based Model Context Protocol (MCP) server that exposes your Chrome browser functionality to AI assistants like Claude, enabling complex browser automation, content analysis, and semantic search.

59. **[XHS-Downloader](https://github.com/JoeanAmier/XHS-Downloader)** - ⭐ 10,017
   小红书（XiaoHongShu、RedNote）链接提取/作品采集工具：提取账号发布、收藏、点赞、专辑作品链接；提取搜索结果作品、用户链接；采集小红书作品信息；提取小红书作品下载地址；下载小红书作品文件

60. **[zen-mcp-server](https://github.com/BeehiveInnovations/zen-mcp-server)** - ⭐ 9,890
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

61. **[mcp-use](https://github.com/mcp-use/mcp-use)** - ⭐ 9,108
   mcp-use is the easiest way to interact with mcp servers with custom agents

62. **[Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)** - ⭐ 9,087
   Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with automatic conflict detection

63. **[Scrapling](https://github.com/D4Vinci/Scrapling)** - ⭐ 8,937
   🕷️ An undetectable, powerful, flexible, high-performance Python library to make Web Scraping Easy and Effortless as it should be!

64. **[awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps)** - ⭐ 8,809
   A collection of projects showcasing RAG, agents, workflows, and other AI use cases

65. **[inspector](https://github.com/modelcontextprotocol/inspector)** - ⭐ 8,593
   Visual testing tool for MCP servers

66. **[xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)** - ⭐ 8,566
   本项目为xiaozhi-esp32提供后端服务，帮助您快速搭建ESP32设备控制服务器。Backend service for xiaozhi-esp32, helps you quickly build an ESP32 device control server.

67. **[xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp)** - ⭐ 8,555
   MCP for xiaohongshu.com

68. **[memU](https://github.com/NevaMind-AI/memU)** - ⭐ 8,334
   Memory for 24/7 proactive agents like openclaw (moltbot, clawdbot).

69. **[mcp-go](https://github.com/mark3labs/mcp-go)** - ⭐ 8,123
   A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

70. **[mcp](https://github.com/awslabs/mcp)** - ⭐ 8,089
   Official AWS MCP Servers

71. **[mcp-agent](https://github.com/lastmile-ai/mcp-agent)** - ⭐ 8,009
   Build effective agents using Model Context Protocol and simple workflow patterns

72. **[antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)** - ⭐ 7,812
   The Ultimate Collection of 700+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

73. **[git-mcp](https://github.com/idosal/git-mcp)** - ⭐ 7,535
   Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project

74. **[awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources)** - ⭐ 7,502
   🧑‍🚀 全世界最好的LLM资料总结（多模态生成、Agent、辅助编程、AI审稿、数据处理、模型训练、模型推理、o1 模型、MCP、小语言模型、视觉语言模型） | Summary of the world's best LLM resources. 

75. **[GhidraMCP](https://github.com/LaurieWired/GhidraMCP)** - ⭐ 7,472
   MCP Server for Ghidra

76. **[oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)** - ⭐ 7,289
   #1 OpenCode Plugin- Battery included. ASYNC SUBAGENTS (YES LIKE CLAUDE CODE) · Curated agents with proper models · Crafted tools like LSP/AST included · Curated MCPs · Claude Code Compatible Layer — Steroids for your OpenCode. The Best LLM Agent Experience is Here.

77. **[browser-tools-mcp](https://github.com/AgentDeskAI/browser-tools-mcp)** - ⭐ 7,056
   Monitor browser logs directly from Cursor and other MCP compatible IDEs.

78. **[claude-plugins-official](https://github.com/anthropics/claude-plugins-official)** - ⭐ 6,898
   Official, Anthropic-managed directory of high quality Claude Code Plugins.

79. **[hexstrike-ai](https://github.com/0x4m4/hexstrike-ai)** - ⭐ 6,687
   HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, GPT, Copilot, etc.) autonomously run 150+ cybersecurity tools for automated pentesting, vulnerability discovery, bug bounty automation, and security research. Seamlessly bridge LLMs with real-world offensive security capabilities.

80. **[registry](https://github.com/modelcontextprotocol/registry)** - ⭐ 6,379
   A community driven registry service for Model Context Protocol (MCP) servers.

81. **[astron-rpa](https://github.com/iflytek/astron-rpa)** - ⭐ 6,367
   Agent-ready RPA suite with out-of-the-box automation tools. Built for individuals and enterprises.

82. **[awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients)** - ⭐ 6,269
   A collection of MCP clients.

83. **[cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp)** - ⭐ 6,261
   TalkToFigma: MCP integration between Cursor and Figma, allowing Cursor Agentic AI to communicate with Figma for reading designs and modifying them programmatically.

84. **[refly](https://github.com/refly-ai/refly)** - ⭐ 6,135
   The first open-source agent skills builder. 🦞

85. **[Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH)** - ⭐ 6,079
   MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients

86. **[kreuzberg](https://github.com/kreuzberg-dev/kreuzberg)** - ⭐ 5,768
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Java, Go, PHP, Elixir, C#, TypeScript (Node/Bun/Wasm/Deno)- or use via CLI, REST API, or MCP server.

87. **[unity-mcp](https://github.com/CoplayDev/unity-mcp)** - ⭐ 5,741
   Unity MCP acts as a bridge, allowing AI assistants (like Claude, Cursor) to interact directly with your Unity Editor via a local MCP (Model Context Protocol) Client. Give your LLM tools to manage assets, control scenes, edit scripts, and automate tasks within Unity.

88. **[mcp](https://github.com/BrowserMCP/mcp)** - ⭐ 5,722
   Browser MCP is a Model Context Provider (MCP) server that allows AI applications to control your browser

89. **[voltagent](https://github.com/VoltAgent/voltagent)** - ⭐ 5,692
   AI Agent Engineering Platform built on an Open Source TypeScript AI Agent Framework

90. **[klavis](https://github.com/Klavis-AI/klavis)** - ⭐ 5,624
   Klavis AI (YC X25):  MCP integration platforms that let AI agents use tools reliably at any scale

91. **[Everywhere](https://github.com/DearVa/Everywhere)** - ⭐ 5,442
   Context-aware AI assistant for your desktop. Ready to respond intelligently, seamlessly integrating multiple LLMs and MCP tools.

92. **[firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)** - ⭐ 5,427
   🔥 Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients.

93. **[ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp)** - ⭐ 5,427
   AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP.

94. **[DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP)** - ⭐ 5,419
   This is MCP server for Claude that gives it terminal control, file system search and diff file editing capabilities

95. **[whatsapp-mcp](https://github.com/lharries/whatsapp-mcp)** - ⭐ 5,305
   WhatsApp MCP server

96. **[claude-context](https://github.com/zilliztech/claude-context)** - ⭐ 5,278
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

97. **[mcp-playwright](https://github.com/executeautomation/mcp-playwright)** - ⭐ 5,213
   Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in Claude Desktop, Cline, Cursor IDE and More 🔌

98. **[awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)** - ⭐ 5,130
   Awesome MCP Servers - A curated list of Model Context Protocol servers

99. **[UltraRAG](https://github.com/OpenBMB/UltraRAG)** - ⭐ 5,120
   UltraRAG v3: A Low-Code MCP Framework for Building Complex and Innovative RAG Pipelines

100. **[sdk-python](https://github.com/strands-agents/sdk-python)** - ⭐ 5,063
   A model-driven approach to building AI agents in just a few lines of code.

101. **[5ire](https://github.com/nanbingxyz/5ire)** - ⭐ 5,013
   5ire is a cross-platform desktop AI assistant, MCP client. It compatible with major service providers,  supports local knowledge base and  tools via model context protocol servers .

102. **[gaianet-node](https://github.com/GaiaNet-AI/gaianet-node)** - ⭐ 5,011
   Install, run and deploy your own decentralized AI agent service

103. **[aci](https://github.com/aipotheosis-labs/aci)** - ⭐ 4,707
   ACI.dev is the open source tool-calling platform that hooks up 600+ tools into any agentic IDE or custom AI agent through direct function calling or a unified MCP server. The birthplace of VibeOps.

104. **[microsandbox](https://github.com/zerocore-ai/microsandbox)** - ⭐ 4,705
   opensource self-hosted sandboxes for ai agents

105. **[Kiln](https://github.com/Kiln-AI/Kiln)** - ⭐ 4,640
   Build, Evaluate, and Optimize AI Systems. Includes evals, RAG, agents, fine-tuning, synthetic data generation, dataset management, MCP, and more.

106. **[casibase](https://github.com/casibase/casibase)** - ⭐ 4,428
   ⚡️AI Cloud OS: Open-source enterprise-level AI knowledge base and MCP (model-context-protocol)/A2A (agent-to-agent) management platform with admin UI, user management and Single-Sign-On⚡️, supports ChatGPT, Claude, Llama, Ollama, HuggingFace, etc., chat bot demo: https://ai.casibase.com, admin UI demo: https://ai-admin.casibase.com

107. **[deep-research](https://github.com/u14app/deep-research)** - ⭐ 4,374
   Use any LLMs (Large Language Models) for Deep Research. Support SSE API and MCP server.

108. **[mcp-ui](https://github.com/MCP-UI-Org/mcp-ui)** - ⭐ 4,332
   UI over MCP. Create next-gen UI experiences with the protocol and SDK!

109. **[httprunner](https://github.com/httprunner/httprunner)** - ⭐ 4,254
   HttpRunner 是一款开源的 API/UI 测试框架，简单易用，功能强大，具有丰富的插件化机制和高度的可扩展能力。

110. **[magic-mcp](https://github.com/21st-dev/magic-mcp)** - ⭐ 4,248
   It's like v0 but in your Cursor/WindSurf/Cline. 21st dev Magic MCP server for working with your frontend like Magic

111. **[Windows-MCP](https://github.com/CursorTouch/Windows-MCP)** - ⭐ 4,211
   MCP Server for Computer Use in Windows

112. **[mcp-atlassian](https://github.com/sooperset/mcp-atlassian)** - ⭐ 4,206
   MCP server for Atlassian tools (Confluence, Jira)

113. **[XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP)** - ⭐ 4,145
   A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects.

114. **[wanwu](https://github.com/UnicomAI/wanwu)** - ⭐ 4,101
   China Unicom's Yuanjing Wanwu Agent Platform is an enterprise-grade, multi-tenant AI agent development platform. It helps users build applications such as intelligent agents, workflows, and rag, and also supports model management. The platform features a developer-friendly license, and we welcome all developers to build upon the platform.

115. **[Olares](https://github.com/beclab/Olares)** - ⭐ 4,033
   Olares: An Open-Source Personal Cloud to Reclaim Your Data

116. **[mcpo](https://github.com/open-webui/mcpo)** - ⭐ 3,960
   A simple, secure MCP-to-OpenAPI proxy server

117. **[directories](https://github.com/leerob/directories)** - ⭐ 3,898
   The Cursor & Windsurf community, find rules and MCPs

118. **[directories](https://github.com/pontusab/directories)** - ⭐ 3,896
   The Cursor & Windsurf community, find rules and MCPs

119. **[learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai)** - ⭐ 3,896
   Learn Agentic AI using Dapr Agentic Cloud Ascent (DACA) Design Pattern and Agent-Native Cloud Technologies: OpenAI Agents SDK, Memory, MCP, A2A, Knowledge Graphs, Dapr, Rancher Desktop, and Kubernetes.

120. **[csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk)** - ⭐ 3,869
   The official C# SDK for Model Context Protocol servers and clients. Maintained in collaboration with Microsoft.

121. **[notion-mcp-server](https://github.com/makenotion/notion-mcp-server)** - ⭐ 3,854
   Official Notion MCP Server

122. **[spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** - ⭐ 3,852
   A Model Context Protocol (MCP) server that provides structured spec-driven development workflow tools for AI-assisted software development, featuring a real-time web dashboard and VSCode extension for monitoring and managing your project's progress directly in your development environment.

123. **[go-sdk](https://github.com/modelcontextprotocol/go-sdk)** - ⭐ 3,784
   The official Go SDK for Model Context Protocol servers and clients. Maintained in collaboration with Google.

124. **[exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)** - ⭐ 3,766
   Exa MCP for web search and web crawling!

125. **[telegram-search](https://github.com/groupultra/telegram-search)** - ⭐ 3,739
   🔍 导出并模糊搜索 Telegram 聊天记录 | Export and fuzzy search your Telegram chat history

126. **[MemOS](https://github.com/MemTensor/MemOS)** - ⭐ 3,710
   Build memory-native AI agents with Memory OS — an open-source framework for long-term memory, retrieval, and adaptive learning in large language models. Agent Memory | Memory  System | Memory Management | Memory MCP | MCP System | LLM Memory | Agents Memory System | 

127. **[learn-ai-engineering](https://github.com/ashishps1/learn-ai-engineering)** - ⭐ 3,698
   Learn AI and LLMs from scratch using free resources

128. **[fast-agent](https://github.com/evalstate/fast-agent)** - ⭐ 3,657
   Define, Prompt and Test MCP enabled Agents and Workflows

129. **[mcp-server-chart](https://github.com/antvis/mcp-server-chart)** - ⭐ 3,639
   🤖 A visualization mcp & skills contains 25+ visual charts using @antvis. Using for chart generation and data analysis.

130. **[core](https://github.com/opensumi/core)** - ⭐ 3,597
   A framework helps you quickly build AI Native IDE products. MCP Client, supports Model Context Protocol (MCP) tools via MCP server.

131. **[mcp-feedback-enhanced](https://github.com/Minidoracat/mcp-feedback-enhanced)** - ⭐ 3,567
   Enhanced MCP server for interactive user feedback and command execution in AI-assisted development, featuring dual interface support (Web UI and Desktop Application) with intelligent environment detection and cross-platform compatibility.

132. **[ciso-assistant-community](https://github.com/intuitem/ciso-assistant-community)** - ⭐ 3,567
   CISO Assistant is a one-stop-shop GRC platform for Risk Management, AppSec, Compliance & Audit, TPRM, Privacy, and Reporting. It supports 100+ global frameworks with automatic control mapping, including ISO 27001, NIST CSF, SOC 2, CIS, PCI DSS, NIS2, DORA, GDPR, HIPAA, CMMC, and more.

133. **[awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)** - ⭐ 3,531
   A curated list of Model Context Protocol (MCP) servers

134. **[cipher](https://github.com/campfirein/cipher)** - ⭐ 3,503
   Byterover Cipher is an opensource memory layer specifically designed for coding agents. Compatible with Cursor, Codex, Claude Code, Windsurf, Cline, Claude Desktop, Gemini CLI, AWS's Kiro, VS Code, Roo Code, Trae, Amp Code and Warp through MCP. Built by https://byterover.dev/

135. **[Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3)** - ⭐ 3,492
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

136. **[go-whatsapp-web-multidevice](https://github.com/aldinokemal/go-whatsapp-web-multidevice)** - ⭐ 3,467
   GOWA - WhatsApp REST API with support for UI, Multi Account, Webhooks, and MCP, and Chatwoot. Built with Golang for efficient memory use. 

137. **[AionUi](https://github.com/iOfficeAI/AionUi)** - ⭐ 3,452
   Free, local, open-source GUI app for Gemini CLI, Claude Code, Codex, Qwen Code, Goose Cli, Auggie, and more — Enhanced Chat UI, WebUI, Multi-Agent & Multi-LLM, MCP Integration | 🌟 Star if you like it!

138. **[mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** - ⭐ 3,389

139. **[osaurus](https://github.com/dinoki-ai/osaurus)** - ⭐ 3,346
   AI edge infrastructure for macOS. Run local or cloud models, share tools across apps via MCP, and power AI workflows with a native, always-on runtime.

140. **[mobile-mcp](https://github.com/mobile-next/mobile-mcp)** - ⭐ 3,344
   Model Context Protocol Server for Mobile Automation and Scraping (iOS, Android, Emulators, Simulators and Real Devices)

141. **[langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters)** - ⭐ 3,339
   LangChain 🔌 MCP

142. **[claude-code-guide](https://github.com/zebbern/claude-code-guide)** - ⭐ 3,330
   Claude Code Guide - Setup, Commands, workflows, agents, skills & tips-n-tricks 

143. **[octelium](https://github.com/octelium/octelium)** - ⭐ 3,328
   A next-gen FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA platform, API/AI/MCP gateway, a PaaS, an ngrok-alternative and a homelab infrastructure.

144. **[MCP-Chinese-Getting-Started-Guide](https://github.com/liaokongVFX/MCP-Chinese-Getting-Started-Guide)** - ⭐ 3,316
   Model Context Protocol(MCP) 编程极速入门

145. **[PeopleInSpace](https://github.com/joreilly/PeopleInSpace)** - ⭐ 3,306
   Kotlin Multiplatform sample with SwiftUI, Jetpack Compose, Compose for Wear, Compose for Desktop, and Compose for Web clients along with Ktor backend.

146. **[PPTAgent](https://github.com/icip-cas/PPTAgent)** - ⭐ 3,302
   An Agentic Framework for Reflective PowerPoint Generation

147. **[excel-mcp-server](https://github.com/haris-musa/excel-mcp-server)** - ⭐ 3,297
   A Model Context Protocol server for Excel file manipulation

148. **[mcp-context-forge](https://github.com/IBM/mcp-context-forge)** - ⭐ 3,249
   A Model Context Protocol (MCP) Gateway & Registry. Serves as a central management point for tools, resources, and prompts that can be accessed by MCP-compatible LLM applications. Converts REST API endpoints to MCP, composes virtual MCP servers with added security and observability, and converts between protocols (stdio, SSE, Streamable HTTP).

149. **[boost](https://github.com/laravel/boost)** - ⭐ 3,219
   Laravel-focused MCP server for augmenting your AI powered local development experience.

150. **[metorial](https://github.com/metorial/metorial)** - ⭐ 3,216
   Connect any AI model to 600+ integrations; powered by MCP 📡 🚀

151. **[py-xiaozhi](https://github.com/huangjunsen0406/py-xiaozhi)** - ⭐ 3,171
   A Python-based Xiaozhi AI for users who want the full Xiaozhi experience without owning specialized hardware.

152. **[mcp](https://github.com/google/mcp)** - ⭐ 3,156
   Google 💚 MCP

153. **[java-sdk](https://github.com/modelcontextprotocol/java-sdk)** - ⭐ 3,148
   The official Java SDK for Model Context Protocol servers and clients. Maintained in collaboration with Spring AI

154. **[mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase)** - ⭐ 3,118
   Allow LLMs to control a browser with Browserbase and Stagehand

155. **[rikkahub](https://github.com/rikkahub/rikkahub)** - ⭐ 3,084
   RikkaHub is an Android APP that supports for multiple LLM providers.

156. **[archestra](https://github.com/archestra-ai/archestra)** - ⭐ 3,024
   ClawdBot/MoldBot/OpenClaw for Enterprise. Agentic Security, MCP, A2A, LLM; MCP registry & orchestrator

157. **[n8n-nodes-mcp](https://github.com/nerding-io/n8n-nodes-mcp)** - ⭐ 2,977
   n8n custom node for MCP

158. **[rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)** - ⭐ 2,963
   The official Rust SDK for the Model Context Protocol

159. **[core](https://github.com/cheshire-cat-ai/core)** - ⭐ 2,961
   AI agent microservice

160. **[fastmcp](https://github.com/punkpeye/fastmcp)** - ⭐ 2,919
   A TypeScript framework for building MCP servers.

161. **[AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard)** - ⭐ 2,906
   A.I.G (AI-Infra-Guard) is a comprehensive, intelligent, and easy-to-use AI Red Teaming platform developed by Tencent Zhuque Lab.

162. **[mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** - ⭐ 2,818
   MCP server that interacts with Obsidian via the Obsidian rest API community plugin

163. **[playwriter](https://github.com/remorses/playwriter)** - ⭐ 2,753
   Chrome extension to let agents control your browser. Runs Playwright snippets in a stateful sandbox. Available as CLI or MCP

164. **[shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server)** - ⭐ 2,642
   A mcp server to allow LLMS gain context about shadcn ui component structure,usage and installation,compaitable with react,svelte 5,vue & React Native

165. **[kreuzberg](https://github.com/Goldziher/kreuzberg)** - ⭐ 2,561
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Go, and TypeScript/Node.js—or use via CLI, REST API, or MCP server.

166. **[mcp](https://github.com/microsoft/mcp)** - ⭐ 2,550
   Catalog of official Microsoft MCP (Model Context Protocol) server implementations for AI-powered data access and tool integration

167. **[nunu](https://github.com/go-nunu/nunu)** - ⭐ 2,540
   A CLI tool for building Go applications.

168. **[basic-memory](https://github.com/basicmachines-co/basic-memory)** - ⭐ 2,473
   AI conversations that actually remember. Never re-explain your project to your AI again. Join our Discord: https://discord.gg/tyvKNccgqN

169. **[sandbox](https://github.com/agent-infra/sandbox)** - ⭐ 2,465
   All-in-One Sandbox for AI Agents that combines Browser, Shell, File, MCP and VSCode Server in a single Docker container.

170. **[supabase-mcp](https://github.com/supabase-community/supabase-mcp)** - ⭐ 2,451
   Connect Supabase to your AI assistants

171. **[supergateway](https://github.com/supercorp-ai/supergateway)** - ⭐ 2,418
   Run MCP stdio servers over SSE and SSE over stdio. AI gateway.

172. **[markdownify-mcp](https://github.com/zcaceres/markdownify-mcp)** - ⭐ 2,398
   A Model Context Protocol server for converting almost anything to Markdown

173. **[buildwithclaude](https://github.com/davepoon/buildwithclaude)** - ⭐ 2,383
   A single hub to find Claude Skills, Agents, Commands, Hooks, Plugins, and Marketplace collections to extend Claude Code

174. **[MCP-SuperAssistant](https://github.com/srbhptl39/MCP-SuperAssistant)** - ⭐ 2,252
   Brings MCP to ChatGPT, DeepSeek, Perplexity, Grok, Gemini, Google AI Studio, OpenRouter, DeepSeek, T3 Chat and more...

175. **[mcp-grafana](https://github.com/grafana/mcp-grafana)** - ⭐ 2,250
   MCP server for Grafana

176. **[mcp-proxy](https://github.com/sparfenyuk/mcp-proxy)** - ⭐ 2,239
   A bridge between Streamable HTTP and stdio MCP transports

177. **[ableton-mcp](https://github.com/ahujasid/ableton-mcp)** - ⭐ 2,210

178. **[chatmcp](https://github.com/daodao97/chatmcp)** - ⭐ 2,173
   ChatMCP is an AI chat client implementing the Model Context Protocol (MCP).

179. **[kagent](https://github.com/kagent-dev/kagent)** - ⭐ 2,154
   Cloud Native Agentic AI | Discord: https://bit.ly/kagentdiscord

180. **[ddgs](https://github.com/deedy5/ddgs)** - ⭐ 2,150
   DDGS | Dux Distributed Global Search. A metasearch library that aggregates results from diverse web search services

181. **[arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)** - ⭐ 2,141
   A Model Context Protocol server for searching and analyzing arXiv papers

182. **[lemonade](https://github.com/lemonade-sdk/lemonade)** - ⭐ 2,116
   Lemonade helps users discover and run local AI apps by serving optimized LLMs right from their own GPUs and NPUs. Join our discord: https://discord.gg/5xXzkMu8Zk

183. **[bifrost](https://github.com/maximhq/bifrost)** - ⭐ 2,104
   Fastest LLM gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.

184. **[claude-code-subagents-collection](https://github.com/davepoon/claude-code-subagents-collection)** - ⭐ 2,098
   Claude Code Subagents & Commands Collection + CLI Tool

185. **[papersgpt-for-zotero](https://github.com/papersgpt/papersgpt-for-zotero)** - ⭐ 2,096
   A powerful Zotero AI and MCP plugin with ChatGPT, Gemini 3, Claude, Grok, DeepSeek, OpenRouter, Kimi 2.5, GLM 4.7, SiliconFlow, GPT-oss, Gemma 3, Qwen 3

186. **[comfyui_LLM_party](https://github.com/heshengtao/comfyui_LLM_party)** - ⭐ 2,092
   LLM Agent Framework in ComfyUI includes MCP sever, Omost,GPT-sovits, ChatTTS,GOT-OCR2.0, and FLUX prompt nodes,access to Feishu,discord,and adapts to all llms with similar openai / aisuite interfaces, such as o1,ollama, gemini, grok, qwen, GLM, deepseek, kimi,doubao. Adapted to local llms, vlm, gguf such as llama-3.3 Janus-Pro, Linkage graphRAG

187. **[dbhub](https://github.com/bytebase/dbhub)** - ⭐ 2,077
   Zero-dependency, token-efficient database MCP server for Postgres, MySQL, SQL Server, MariaDB, SQLite.

188. **[awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)** - ⭐ 2,055
   A curated list of skills, tools, tutorials, and capabilities for AI coding agents (Claude, Codex, Copilot, VS Code)

189. **[Unla](https://github.com/AmoyLab/Unla)** - ⭐ 2,026
   🧩 MCP Gateway - A lightweight gateway service that instantly transforms existing MCP Servers and APIs into MCP servers with zero code changes. Features Docker deployment and management UI, requiring no infrastructure modifications.

190. **[DevDocs](https://github.com/cyberagiinc/DevDocs)** - ⭐ 2,023
   Completely free, private, UI based Tech Documentation MCP server. Designed for coders and software developers in mind. Easily integrate into Cursor, Windsurf, Cline, Roo Code, Claude Desktop App 

191. **[mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager)** - ⭐ 2,019
   Shrimp Task Manager is a task tool built for AI Agents, emphasizing chain-of-thought, reflection, and style consistency. It converts natural language into structured dev tasks with dependency tracking and iterative refinement, enabling agent-like developer behavior in reasoning AI systems.

192. **[brightdata-mcp](https://github.com/brightdata/brightdata-mcp)** - ⭐ 2,005
   A powerful Model Context Protocol (MCP) server that provides an all-in-one solution for public web access.

193. **[metamcp](https://github.com/metatool-ai/metamcp)** - ⭐ 2,003
   MCP Aggregator, Orchestrator, Middleware, Gateway in one docker

194. **[postgres-mcp](https://github.com/crystaldba/postgres-mcp)** - ⭐ 1,996
   Postgres MCP Pro provides configurable read/write access and performance analysis for you and your AI agents.

195. **[mcp-crawl4ai-rag](https://github.com/coleam00/mcp-crawl4ai-rag)** - ⭐ 1,988
   Web Crawling and RAG Capabilities for AI Agents and AI Coding Assistants

196. **[superglue](https://github.com/superglue-ai/superglue)** - ⭐ 1,980
   superglue (YC W25) builds integrations and tools from natural language. Get production-grade tools for long tail and enterprise systems.

197. **[mcpso](https://github.com/chatmcp/mcpso)** - ⭐ 1,963
   directory for Awesome MCP Servers

198. **[gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool)** - ⭐ 1,953
   MCP server that enables AI assistants to interact with Google Gemini CLI, leveraging Gemini's massive token window for large file analysis and codebase understanding

199. **[Aix-DB](https://github.com/apconw/Aix-DB)** - ⭐ 1,934
   Aix-DB 基于 LangChain/LangGraph 框架，结合 MCP Skills 多智能体协作架构，实现自然语言到数据洞察的端到端转换。

200. **[Peekaboo](https://github.com/steipete/Peekaboo)** - ⭐ 1,934
   Peekaboo is a macOS CLI & optional MCP server that enables AI agents to capture screenshots of applications, or the entire system, with optional visual question answering through local or remote AI models.

201. **[modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol)** - ⭐ 1,932
   The official MCP server implementation for the Perplexity API Platform

202. **[yomo](https://github.com/yomorun/yomo)** - ⭐ 1,880
   🦖 Serverless AI Agent Framework with Geo-distributed Edge AI Infra.

203. **[mcp-cli](https://github.com/chrishayuk/mcp-cli)** - ⭐ 1,880

204. **[witsy](https://github.com/nbonamy/witsy)** - ⭐ 1,853
   Witsy: desktop AI assistant / universal MCP client

205. **[agentset](https://github.com/agentset-ai/agentset)** - ⭐ 1,848
   The open-source RAG platform: built-in citations, deep research, 22+ file formats, partitions, MCP server, and more.

206. **[beelzebub](https://github.com/mariocandela/beelzebub)** - ⭐ 1,833
   A secure low code honeypot framework, leveraging AI for System Virtualization.

207. **[sanic-web](https://github.com/apconw/sanic-web)** - ⭐ 1,817
   一个轻量级、支持全链路且易于二次开发的大模型应用项目(Large Model Data Assistant) 支持DeepSeek/Qwen3等大模型 基于 Dify 、LangChain/LangGraph、Ollama&Vllm、Sanic 和 Text2SQL 📊 等技术构建的一站式大模型应用开发项目，采用 Vue3、TypeScript 和 Vite 5 打造现代UI。它支持通过 ECharts 📈 实现基于大模型的数据图形化问答，具备处理 CSV 文件 📂 表格问答的能力。同时，能方便对接第三方开源 RAG 系统 检索系统 🌐等，以支持广泛的通用知识问答。

208. **[mcphub](https://github.com/samanhappy/mcphub)** - ⭐ 1,792
   A unified hub for centrally managing and dynamically orchestrating multiple MCP servers/APIs into separate endpoints with flexible routing strategies

209. **[opendia](https://github.com/aaronjmars/opendia)** - ⭐ 1,777
   Connect your browser to AI models. Just use Dia on Chrome, Arc or Firefox.

210. **[AIaW](https://github.com/NitroRCr/AIaW)** - ⭐ 1,747
   AI as Workspace - An elegant AI chat client. Full-featured, lightweight. Support multiple workspaces, plugin system, cross-platform, local first + real-time cloud sync, Artifacts, MCP | 更好的 AI 客户端

211. **[Dive](https://github.com/OpenAgentPlatform/Dive)** - ⭐ 1,726
   Dive is an open-source MCP Host Desktop Application that seamlessly integrates with any LLMs supporting function calling capabilities. ✨

212. **[godot-mcp](https://github.com/Coding-Solo/godot-mcp)** - ⭐ 1,719
   MCP server for interfacing with Godot game engine. Provides tools for launching the editor, running projects, and capturing debug output.

213. **[mcphub.nvim](https://github.com/ravitemer/mcphub.nvim)** - ⭐ 1,713
   An MCP client for Neovim that seamlessly integrates MCP servers into your editing workflow with an intuitive interface for managing, testing, and using MCP servers with your favorite chat plugins.

214. **[agentgateway](https://github.com/agentgateway/agentgateway)** - ⭐ 1,713
   Next Generation Agentic Proxy for AI Agents and MCP servers

215. **[mcp-router](https://github.com/mcp-router/mcp-router)** - ⭐ 1,708
   A Unified MCP Server Management App (MCP Manager).

216. **[mcpb](https://github.com/modelcontextprotocol/mcpb)** - ⭐ 1,692
   Desktop Extensions: One-click local MCP server installation in desktop apps

217. **[super-agent-party](https://github.com/heshengtao/super-agent-party)** - ⭐ 1,681
   ⭐ All-in-one AI companion! Desktop girlfriend + virtual streamer + IM bot + browser control + smart home control + computer control + virtual reality, and everything else you can imagine!⭐全能型AI伴侣！桌面女友 + 虚拟主播 + 即时通讯机器人 + 浏览器控制 + 智能家居控制 + 电脑控制 + 虚拟现实 等你能想到的一切功能！

218. **[interactive-feedback-mcp](https://github.com/noopstudios/interactive-feedback-mcp)** - ⭐ 1,669
   Interactive User Feedback MCP

219. **[inspector](https://github.com/MCPJam/inspector)** - ⭐ 1,666
   Test & Debug MCP servers, ChatGPT apps, and MCP Apps (ext-apps)

220. **[mcp_agent_mail](https://github.com/Dicklesworthstone/mcp_agent_mail)** - ⭐ 1,656
   Like gmail for your coding agents. Lets various different agents communicate and coordinate with each other.

221. **[zenfeed](https://github.com/glidea/zenfeed)** - ⭐ 1,642
   Make RSS 📰 great again with AI 🧠✨!! [拯救你的颈椎 - 数字健康工具：https://forcebreak.zenfeed.xyz]

222. **[anyquery](https://github.com/julien040/anyquery)** - ⭐ 1,621
   Query anything (GitHub, Notion, +40 more) with SQL and let LLMs (ChatGPT, Claude) connect to using MCP

223. **[yu-ai-agent](https://github.com/liyupi/yu-ai-agent)** - ⭐ 1,621
   编程导航 2025 年 AI 开发实战新项目，基于 Spring Boot 3 + Java 21 + Spring AI 构建 AI 恋爱大师应用和 ReAct 模式自主规划智能体YuManus，覆盖 AI 大模型接入、Spring AI 核心特性、Prompt 工程和优化、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、AI Agent 开发（Manas Java 实现）、Cursor AI 工具等核心知识。用一套教程将程序员必知必会的 AI 技术一网打尽，帮你成为 AI 时代企业的香饽饽，给你的简历和求职大幅增加竞争力。

224. **[MAI-UI](https://github.com/Tongyi-MAI/MAI-UI)** - ⭐ 1,619
   MAI-UI: Real-World Centric Foundation GUI Agents ranging from 2B to 235B

225. **[codemcp](https://github.com/ezyang/codemcp)** - ⭐ 1,605
   Coding assistant MCP for Claude Desktop

226. **[ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp)** - ⭐ 1,591
   MCP server for interacting with the iOS simulator

227. **[py-gpt](https://github.com/szczyglis-dev/py-gpt)** - ⭐ 1,589
   Desktop AI Assistant powered by GPT-5, GPT-4, o1, o3, Gemini, Claude, Ollama, DeepSeek, Perplexity, Grok, Bielik, chat, vision, voice, RAG, image and video generation, agents, tools, MCP, plugins, speech synthesis and recognition, web search, memory, presets, assistants,and more. Linux, Windows, Mac

228. **[kubb](https://github.com/kubb-labs/kubb)** - ⭐ 1,587
   🧩 The Ultimate Toolkit for Generating Type-Safe API Clients, Hooks, and Validators.

229. **[toolhive](https://github.com/stacklok/toolhive)** - ⭐ 1,584
   ToolHive makes deploying MCP servers easy, secure and fun

230. **[Continuous-Claude-v2](https://github.com/parcadei/Continuous-Claude-v2)** - ⭐ 1,575
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

231. **[mcporter](https://github.com/steipete/mcporter)** - ⭐ 1,570
   Call MCPs via TypeScript, masquerading as simple TypeScript API. Or package them as cli.

232. **[n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server)** - ⭐ 1,559
   MCP server that provides tools and resources for interacting with n8n API

233. **[Office-Word-MCP-Server](https://github.com/GongRzhe/Office-Word-MCP-Server)** - ⭐ 1,547
   A Model Context Protocol (MCP) server for creating, reading, and manipulating Microsoft Word documents. This server enables AI assistants to work with Word documents through a standardized interface, providing rich document editing capabilities.

234. **[mcphost](https://github.com/mark3labs/mcphost)** - ⭐ 1,538
   A CLI host application that enables Large Language Models (LLMs) to interact with external tools through the Model Context Protocol (MCP).

235. **[pg-aiguide](https://github.com/timescale/pg-aiguide)** - ⭐ 1,517
   MCP server and Claude plugin for Postgres skills and documentation. Helps AI coding tools generate better PostgreSQL code.

236. **[mcp-installer](https://github.com/anaisbetts/mcp-installer)** - ⭐ 1,506
   An MCP server that installs other MCP servers for you

237. **[claudian](https://github.com/YishenTu/claudian)** - ⭐ 1,493
   An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault

238. **[Office-PowerPoint-MCP-Server](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server)** - ⭐ 1,491
   A MCP (Model Context Protocol) server for PowerPoint manipulation using python-pptx. This server provides tools for creating, editing, and manipulating PowerPoint presentations through the MCP protocol.

239. **[mcptools](https://github.com/f/mcptools)** - ⭐ 1,473
   A command-line interface for interacting with MCP (Model Context Protocol) servers using both stdio and HTTP transport.

240. **[better-agents](https://github.com/langwatch/better-agents)** - ⭐ 1,464
   Standards for building agents, better

241. **[MCP-Reborn](https://github.com/Hexeption/MCP-Reborn)** - ⭐ 1,448
   MCP-Reborn is an MCP (Mod Coder Pack) for Minecraft for making modded clients and researching its code. (1.13-1.21.4)

242. **[mcp-scan](https://github.com/invariantlabs-ai/mcp-scan)** - ⭐ 1,445
   Security scanner for AI agents, MCP servers and agent skills.

243. **[mcp-language-server](https://github.com/isaacphi/mcp-language-server)** - ⭐ 1,436
   mcp-language-server gives MCP enabled clients access semantic tools like get definition, references, rename, and diagnostics.

244. **[solace-agent-mesh](https://github.com/SolaceLabs/solace-agent-mesh)** - ⭐ 1,434
   An event-driven framework designed to build and orchestrate multi-agent AI systems. It enables seamless integration of AI agents with real-world data sources and systems, facilitating complex, multi-step workflows.

245. **[rulego](https://github.com/rulego/rulego)** - ⭐ 1,422
   ⛓️RuleGo is a lightweight, high-performance, embedded, next-generation component orchestration rule engine framework for Go.

246. **[ext-apps](https://github.com/modelcontextprotocol/ext-apps)** - ⭐ 1,416
   Official repo for spec & SDK of MCP Apps protocol - standard for UIs embedded AI chatbots, served by MCP servers

247. **[awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins)** - ⭐ 1,388
   A curated list of Plugins that let you extend Claude Code with custom commands, agents, hooks, and MCP servers through the plugin system.

248. **[unreal-mcp](https://github.com/chongdashu/unreal-mcp)** - ⭐ 1,377
   Enable AI assistant clients like Cursor, Windsurf and Claude Desktop to control Unreal Engine through natural language using the Model Context Protocol (MCP).

249. **[php-sdk](https://github.com/modelcontextprotocol/php-sdk)** - ⭐ 1,343
   The official PHP SDK for Model Context Protocol servers and clients. Maintained in collaboration with The PHP Foundation.

250. **[mcp](https://github.com/MicrosoftDocs/mcp)** - ⭐ 1,339
   Official Microsoft Learn MCP Server – powering LLMs and AI agents with real-time, trusted Microsoft docs & code samples.

251. **[docker-mcp-tutorial](https://github.com/theNetworkChuck/docker-mcp-tutorial)** - ⭐ 1,328
   Complete tutorial materials for building MCP servers with Docker - from NetworkChuck's video

252. **[nerve](https://github.com/evilsocket/nerve)** - ⭐ 1,319
   The Simple Agent Development Kit.

253. **[google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp)** - ⭐ 1,317
   Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search & Drive with AI - Comprehensive Google Workspace / G Suite MCP Server & CLI Tool

254. **[slack-mcp-server](https://github.com/korotovsky/slack-mcp-server)** - ⭐ 1,306
   The most powerful MCP Slack Server with no permission requirements, Apps support, GovSlack, DMs, Group DMs and smart history fetch logic.

255. **[Risuai](https://github.com/kwaroran/Risuai)** - ⭐ 1,305
   Make your own story. User-friendly software for LLM roleplaying

256. **[code-mode](https://github.com/universal-tool-calling-protocol/code-mode)** - ⭐ 1,304
   🔌 Plug-and-play library to enable agents to call MCP and UTCP tools via code execution. 

257. **[claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills)** - ⭐ 1,302
   270+ Claude Code plugins with 739 agent skills. Production orchestration patterns, interactive tutorials (11 Jupyter notebooks), and CCPI package manager. 4.13.0

258. **[Claude-Code-Development-Kit](https://github.com/peterkrueck/Claude-Code-Development-Kit)** - ⭐ 1,301
   Handle context at scale - my custom Claude Code workflow including hooks, mcp and sub agents

259. **[LitterBox](https://github.com/BlackSnufkin/LitterBox)** - ⭐ 1,300
   A secure sandbox environment for malware developers and red teamers to test payloads against detection mechanisms before deployment. Integrates with LLM agents via MCP for enhanced analysis capabilities.

260. **[mcp-unity](https://github.com/CoderGamester/mcp-unity)** - ⭐ 1,300
   Model Context Protocol (MCP) plugin to connect with Unity Editor — designed for Cursor, Claude Code, Codex, Windsurf and other IDEs

261. **[mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** - ⭐ 1,299
   MCP Server for kubernetes management commands

262. **[mcp-obsidian](https://github.com/smithery-ai/mcp-obsidian)** - ⭐ 1,298
   A connector for Claude Desktop to read and search an Obsidian vault.

263. **[zotero-mcp](https://github.com/54yyyu/zotero-mcp)** - ⭐ 1,298
   Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss papers, get summaries, analyze citations, and more.

264. **[mcp-memory-service](https://github.com/doobidoo/mcp-memory-service)** - ⭐ 1,278
   Stop re-explaining your project to AI every session. Automatic context memory for Claude, VS Code, Cursor, and 13+ AI tools.

265. **[ai](https://github.com/stripe/ai)** - ⭐ 1,256
   One-stop shop for building AI-powered products and businesses with Stripe.

266. **[mcp-remote](https://github.com/geelen/mcp-remote)** - ⭐ 1,255

267. **[damn-vulnerable-MCP-server](https://github.com/harishsg993010/damn-vulnerable-MCP-server)** - ⭐ 1,250
   Damn Vulnerable MCP Server

268. **[kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk)** - ⭐ 1,242
   The official Kotlin SDK for Model Context Protocol servers and clients. Maintained in collaboration with JetBrains

269. **[deepwiki-mcp](https://github.com/regenrek/deepwiki-mcp)** - ⭐ 1,239
   📖 MCP server for fetch deepwiki.com and get latest knowledge in Cursor and other Code Editors

270. **[azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp)** - ⭐ 1,237
   The MCP server for Azure DevOps, bringing the power of Azure DevOps directly to your agents.

271. **[MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP)** - ⭐ 1,235
   Official MiniMax Model Context Protocol (MCP) server that enables interaction with powerful Text to Speech, image generation and video generation APIs.

272. **[web-eval-agent](https://github.com/refreshdotdev/web-eval-agent)** - ⭐ 1,234
   An MCP server that autonomously evaluates web applications. 

273. **[google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp)** - ⭐ 1,231

274. **[sre](https://github.com/SmythOS/sre)** - ⭐ 1,228
   The SmythOS Runtime Environment (SRE) is an open-source, cloud-native runtime for agentic AI. Secure, modular, and production-ready, it lets developers build, run, and manage intelligent agents across local, cloud, and edge environments.

275. **[web-eval-agent](https://github.com/withRefresh/web-eval-agent)** - ⭐ 1,226
   An MCP server that autonomously evaluates web applications. 

276. **[RisuAI](https://github.com/kwaroran/RisuAI)** - ⭐ 1,222
   Make your own story. User-friendly software for LLM roleplaying

277. **[jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp)** - ⭐ 1,222
   Plugin for JADX to integrate MCP server

278. **[swift-sdk](https://github.com/modelcontextprotocol/swift-sdk)** - ⭐ 1,220
   The official Swift SDK for Model Context Protocol servers and clients.

279. **[mcp-gateway](https://github.com/docker/mcp-gateway)** - ⭐ 1,214
   docker mcp CLI plugin / MCP Gateway

280. **[terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server)** - ⭐ 1,210
   The Terraform MCP Server provides seamless integration with Terraform ecosystem, enabling advanced automation and interaction capabilities for Infrastructure as Code (IaC) development.

281. **[grafbase](https://github.com/grafbase/grafbase)** - ⭐ 1,207
   The Grafbase GraphQL Federation Gateway

282. **[mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant)** - ⭐ 1,206
   An official Qdrant Model Context Protocol (MCP) server implementation

283. **[elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp)** - ⭐ 1,203
   The official ElevenLabs MCP server

284. **[A2V](https://github.com/Devin-AXIS/A2V)** - ⭐ 1,201
   A2V: Next-Gen AI Value Compute Protocol.                                                                                 

285. **[xmcp](https://github.com/basementstudio/xmcp)** - ⭐ 1,196
   The TypeScript MCP framework

286. **[cunzhi](https://github.com/imhuso/cunzhi)** - ⭐ 1,189
   告别AI提前终止烦恼，助力AI更加持久

287. **[mcp-golang](https://github.com/metoro-io/mcp-golang)** - ⭐ 1,189
   Write Model Context Protocol servers in few lines of go code. Docs at https://mcpgolang.com . Created by https://metoro.io

288. **[npcpy](https://github.com/NPC-Worldwide/npcpy)** - ⭐ 1,186
   The python library for research and development in NLP, multimodal LLMs, Agents, ML, Knowledge Graphs, and more.

289. **[grepai](https://github.com/yoanbernabeu/grepai)** - ⭐ 1,181
   Semantic Search & Call Graphs for AI Agents (100% Local)

290. **[mcp-server-mysql](https://github.com/benborla/mcp-server-mysql)** - ⭐ 1,174
   A Model Context Protocol server that provides read-only access to MySQL databases. This server enables LLMs to inspect database schemas and execute read-only queries.

291. **[tavily-mcp](https://github.com/tavily-ai/tavily-mcp)** - ⭐ 1,171
   Production ready MCP server with real-time search, extract, map & crawl.

292. **[cli](https://github.com/TanStack/cli)** - ⭐ 1,153
   The official TanStack CLI - Project Scaffolding, MCP Server, Agent Skills Installation, etc

293. **[trustgraph](https://github.com/trustgraph-ai/trustgraph)** - ⭐ 1,147
   Programmable Context for the AI Stack. Build. Version. Deploy. The full lifecycle platform for Context Graphs.

294. **[Agent-MCP](https://github.com/rinadelph/Agent-MCP)** - ⭐ 1,146
   Agent-MCP is a framework for creating multi-agent systems that enables coordinated, efficient AI collaboration through the Model Context Protocol (MCP). The system is designed for developers building AI applications that benefit from multiple specialized agents working in parallel on different aspects of a project.

295. **[iMCP](https://github.com/mattt/iMCP)** - ⭐ 1,143
   A macOS app that provides an MCP server to your Messages, Contacts, Reminders and more

296. **[fast-mcp](https://github.com/yjacquin/fast-mcp)** - ⭐ 1,132
   A Ruby Implementation of the Model Context Protocol

297. **[xiaozhi-esp32-server-java](https://github.com/joey-zhou/xiaozhi-esp32-server-java)** - ⭐ 1,132
   小智ESP32的Java企业级管理平台，提供设备监控、音色定制、角色切换和对话记录管理的前后端及服务端一体化解决方案

298. **[tuui](https://github.com/AI-QL/tuui)** - ⭐ 1,121
   A desktop MCP client designed as a tool unitary utility integration, accelerating AI adoption through the Model Context Protocol (MCP) and enabling cross-vendor LLM API orchestration.

299. **[AWorld](https://github.com/inclusionAI/AWorld)** - ⭐ 1,120
   Build, evaluate and train General Multi-Agent Assistance with ease

300. **[mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server)** - ⭐ 1,119
   A Model Context Protocol (MCP) server that enables secure interaction with MySQL databases

301. **[kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server)** - ⭐ 1,117
   Model Context Protocol (MCP) server for Kubernetes and OpenShift

302. **[xhs-toolkit](https://github.com/aki66938/xhs-toolkit)** - ⭐ 1,112
   📕 小红书创作者MCP工具包 - 支持与AI客户端集成的内容创作和发布工具

303. **[cui](https://github.com/wbopan/cui)** - ⭐ 1,111
   A web UI for Claude Code agents

304. **[skills](https://github.com/microsoft/skills)** - ⭐ 1,078
   Skills, MCP servers, Custom Agents, Agents.md for SDKs to ground Coding Agents

305. **[claude-code-mcp](https://github.com/steipete/claude-code-mcp)** - ⭐ 1,077
   Claude Code as one-shot MCP server to have an agent in your agent.

306. **[flock](https://github.com/Onelevenvy/flock)** - ⭐ 1,070
   Flock is a workflow-based low-code platform for rapidly building chatbots, RAG, and coordinating multi-agent teams, powered by LangGraph, Langchain, FastAPI, and NextJS.（Flock 是一个基于workflow工作流的低代码平台，用于快速构建聊天机器人、RAG、Agent和Muti-Agent应用，采用 LangGraph、Langchain、FastAPI 和 NextJS 构建。）

307. **[ApeRAG](https://github.com/apecloud/ApeRAG)** - ⭐ 1,044
   ApeRAG: Production-ready GraphRAG with multi-modal indexing, AI agents, MCP support, and scalable K8s deployment

308. **[claude-init](https://github.com/cfrs2005/claude-init)** - ⭐ 1,043
   Claude Code 中文开发套件 - 为中国开发者定制的零门槛 AI 编程环境。一键安装完整中文化体验，集成 MCP 服务器、智能上下文管理、安全扫描，支持免翻墙访问。让 AI 编程更简单。

309. **[SearChat](https://github.com/sear-chat/SearChat)** - ⭐ 1,038
   Search + Chat = SearChat(AI Chat with Search), Support OpenAI/Anthropic/VertexAI/Gemini, DeepResearch, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

310. **[mcp-server-chatsum](https://github.com/chatmcp/mcp-server-chatsum)** - ⭐ 1,033
   Query and Summarize your chat messages.

311. **[minima](https://github.com/dmayboroda/minima)** - ⭐ 1,033
   On-premises conversational RAG with configurable containers

312. **[lets-learn-mcp-python](https://github.com/microsoft/lets-learn-mcp-python)** - ⭐ 1,028
   MCP Python Tutorial 

313. **[search_with_ai](https://github.com/yokingma/search_with_ai)** - ⭐ 1,025
   AI Search Chat , Support DeepResearch, OpenAI/Anthropic/VertexAI/Gemini, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

314. **[Awesome-MCP-Servers](https://github.com/YuzeHao2023/Awesome-MCP-Servers)** - ⭐ 1,020
   A curated list of Model Context Protocol (MCP) servers 

315. **[wenyan-mcp](https://github.com/caol64/wenyan-mcp)** - ⭐ 1,012
   文颜 MCP Server 可以让 AI 自动将 Markdown 文章排版后发布至微信公众号。

316. **[better-chatbot](https://github.com/cgoinglove/better-chatbot)** - ⭐ 1,009
   Just a Better Chatbot. Powered by Agent & MCP & Workflows.

317. **[docs-mcp-server](https://github.com/arabold/docs-mcp-server)** - ⭐ 1,007
   Grounded Docs MCP Server: Open-Source Alternative to Context7, Nia, and Ref.Tools

318. **[mcp-boilerplate](https://github.com/iannuttall/mcp-boilerplate)** - ⭐ 1,006
   A remote Cloudflare MCP server boilerplate with user authentication and Stripe for paid tools.

319. **[gitlab-mcp](https://github.com/zereight/gitlab-mcp)** - ⭐ 1,001
   First gitlab mcp for you

320. **[awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers)** - ⭐ 992
   Remote MCP Servers

321. **[ros-mcp-server](https://github.com/robotmcp/ros-mcp-server)** - ⭐ 992
   Connect AI models like Claude & GPT with robots using MCP and ROS.

322. **[Gmail-MCP-Server](https://github.com/GongRzhe/Gmail-MCP-Server)** - ⭐ 986
   A Model Context Protocol (MCP) server for Gmail integration in Claude Desktop with auto authentication support. This server enables AI assistants to manage Gmail through natural language interactions.

323. **[todo-for-ai](https://github.com/todo-for-ai/todo-for-ai)** - ⭐ 986
   🤖 A comprehensive task management system specifically designed for AI assistants. Supports project management, task tracking, team collaboration, and seamless AI integration through MCP (Model Context Protocol). Built with modern tech stack including React, Flask, and Docker. Try it now at https://todo4ai.org/

324. **[quickstart-resources](https://github.com/modelcontextprotocol/quickstart-resources)** - ⭐ 981
   A repository of servers and clients from the Model Context Protocol tutorials

325. **[fetcher-mcp](https://github.com/jae-jae/fetcher-mcp)** - ⭐ 977
   MCP server for fetch web page content using Playwright headless browser.

326. **[ai-dev-tools-zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)** - ⭐ 965
   AI Dev Tools Zoomcamp is a free course that helps you use AI tools to write better code, faster. We're starting the first cohort of this course on November 18, 2025! Sign up here to join us 👇🏼

327. **[ollama-mcp-bridge](https://github.com/patruff/ollama-mcp-bridge)** - ⭐ 963
   Bridge between Ollama and MCP servers, enabling local LLMs to use Model Context Protocol tools

328. **[WebMCP](https://github.com/MiguelsPizza/WebMCP)** - ⭐ 961
   Bringing the power of MCP to the web

329. **[google-calendar-mcp](https://github.com/nspady/google-calendar-mcp)** - ⭐ 960
   MCP integration for Google Calendar to manage events.

330. **[RedNote-MCP](https://github.com/iFurySt/RedNote-MCP)** - ⭐ 959
   🚀MCP server for accessing RedNote(XiaoHongShu, xhs).

331. **[ref-tools-mcp](https://github.com/ref-tools/ref-tools-mcp)** - ⭐ 959
   Helping coding agents never make mistakes working with public or private libraries without wasting the context window.

332. **[short-video-maker](https://github.com/gyoridavid/short-video-maker)** - ⭐ 956
   Creates short videos for TikTok, Instagram Reels, and YouTube Shorts using the Model Context Protocol (MCP) and a REST API.

333. **[mcp-windbg](https://github.com/svnscha/mcp-windbg)** - ⭐ 953
   Model Context Protocol for WinDBG

334. **[CloudBase-MCP](https://github.com/TencentCloudBase/CloudBase-MCP)** - ⭐ 949
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app. 

335. **[mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains)** - ⭐ 943
   A model context protocol server to work with JetBrains IDEs: IntelliJ, PyCharm, WebStorm, etc. Also, works with Android Studio

336. **[gemini-nexus](https://github.com/yeahhe365/gemini-nexus)** - ⭐ 939
   Gemini Nexus 是一款深度集成 Google Gemini 能力的 Chrome 扩展程序。它不仅仅是一个侧边栏插件，而是通过注入式的悬浮工具栏、强大的图像 AI 处理以及前沿的浏览器控制协议 (MCP)，将 AI 的触角伸向网页浏览的每一个交互细节。

337. **[awesome-devops-mcp-servers](https://github.com/rohitg00/awesome-devops-mcp-servers)** - ⭐ 933
   A curated list of awesome MCP servers focused on DevOps tools and capabilities.

338. **[tools](https://github.com/strands-agents/tools)** - ⭐ 932
   A set of tools that gives agents powerful capabilities.

339. **[mcpdoc](https://github.com/langchain-ai/mcpdoc)** - ⭐ 925
   Expose llms-txt to IDEs for development

340. **[Unity-MCP](https://github.com/IvanMurzak/Unity-MCP)** - ⭐ 925
   AI-powered bridge connecting LLMs and advanced AI agents to the Unity Editor via the Model Context Protocol (MCP). Chat with AI to generate code, debug errors, and automate game development tasks directly within your project.

341. **[agents](https://github.com/inkeep/agents)** - ⭐ 912
   Create AI Agents in a No-Code Visual Builder or TypeScript SDK with full 2-way sync. For shipping AI assistants and multi-agent AI workflows.

342. **[mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server)** - ⭐ 911
   A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters.

343. **[Pixelle-MCP](https://github.com/AIDC-AI/Pixelle-MCP)** - ⭐ 910
   An Open-Source Multimodal AIGC Solution based on ComfyUI + MCP + LLM  https://pixelle.ai

344. **[CloudBase-AI-ToolKit](https://github.com/TencentCloudBase/CloudBase-AI-ToolKit)** - ⭐ 909
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app in one click.

345. **[agentic-radar](https://github.com/splx-ai/agentic-radar)** - ⭐ 905
   A security scanner for your LLM agentic workflows

346. **[MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge)** - ⭐ 903
   A middleware to provide an openAI compatible endpoint that can call MCP tools

347. **[mcp-framework](https://github.com/QuantGeekDev/mcp-framework)** - ⭐ 901
   A framework for writing MCP (Model Context Protocol) servers in Typescript

348. **[nuxt-mcp-dev](https://github.com/antfu/nuxt-mcp-dev)** - ⭐ 897
   MCP server helping models to understand your Vite/Nuxt app better.

349. **[jupyter-mcp-server](https://github.com/datalayer/jupyter-mcp-server)** - ⭐ 891
   🪐 🔧 Model Context Protocol (MCP) Server for Jupyter.

350. **[mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j)** - ⭐ 890
   Neo4j Labs Model Context Protocol servers

351. **[mcp-browser-use](https://github.com/Saik0s/mcp-browser-use)** - ⭐ 889

352. **[chatgpt-cli](https://github.com/kardolus/chatgpt-cli)** - ⭐ 885
   ChatGPT CLI is a powerful, multi-provider command-line interface for working with modern LLMs. It supports OpenAI, Azure, Perplexity, LLaMA, and more, with features like streaming, interactive chat, prompt files, image/audio I/O, MCP tool calls, and an experimental agent mode for safe, multi-step automation.

353. **[mcpm.sh](https://github.com/pathintegral-institute/mcpm.sh)** - ⭐ 884
   CLI MCP package manager & registry for all platforms and all clients. Search & configure MCP servers. Advanced Router & Profile features.

354. **[nanobot](https://github.com/nanobot-ai/nanobot)** - ⭐ 883
   Build MCP Agents

355. **[mix.core](https://github.com/mixcore/mix.core)** - ⭐ 881
   🚀 A future-proof enterprise web CMS supporting both headless and decoupled approaches. Build any type of app with customizable APIs on ASP.NET Core/.NET Core. Completely open-source and designed for flexibility.

356. **[notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli)** - ⭐ 881

357. **[MCProtocolLib](https://github.com/GeyserMC/MCProtocolLib)** - ⭐ 878
   A library for communication with a Minecraft client/server.

358. **[excalidraw-mcp-app](https://github.com/antonpk1/excalidraw-mcp-app)** - ⭐ 876
   Excalidraw MCP App Server — hand-drawn diagrams for Claude

359. **[himarket](https://github.com/higress-group/himarket)** - ⭐ 875
   HiMarket is an enterprise-level "AI Capability Marketplace and Developer Ecosystem Hub." It is not merely a simple aggregation of traditional APIs, but rather a comprehensive platform that packages, publishes, manages, and operates core AI assets such as enterprise Model APIs, MCP Servers, Agent APIs, etc., through standardized product formats.

360. **[openapi-mcp-server](https://github.com/janwilmake/openapi-mcp-server)** - ⭐ 871
   Allow AI to wade through complex OpenAPIs using Simple Language

361. **[mcp-course](https://github.com/huggingface/mcp-course)** - ⭐ 870

362. **[awesome-mcp-list](https://github.com/MobinX/awesome-mcp-list)** - ⭐ 863
   A concise list for mcp servers

363. **[trpc-agent-go](https://github.com/trpc-group/trpc-agent-go)** - ⭐ 859
   trpc-agent-go is a powerful Go framework for building intelligent agent systems using large language models (LLMs) and tools.

364. **[AI-Gateway](https://github.com/Azure-Samples/AI-Gateway)** - ⭐ 859
   Labs to explore AI Models, MCP servers, and Agents with the AI Gateway powered by Azure API Management and Microsoft Foundry 🚀

365. **[mcp-notion-server](https://github.com/suekou/mcp-notion-server)** - ⭐ 856

366. **[memory-bank-mcp](https://github.com/alioshr/memory-bank-mcp)** - ⭐ 855
   A Model Context Protocol (MCP) server implementation for remote memory bank management, inspired by Cline Memory Bank.

367. **[hyper-mcp](https://github.com/hyper-mcp-rs/hyper-mcp)** - ⭐ 851
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

368. **[MCPJungle](https://github.com/mcpjungle/MCPJungle)** - ⭐ 849
   Self-hosted MCP Gateway for AI agents

369. **[mcp-cli](https://github.com/philschmid/mcp-cli)** - ⭐ 848
   Lighweight CLI to interact with MCP servers

370. **[OpenDerisk](https://github.com/derisk-ai/OpenDerisk)** - ⭐ 842
   AI-Native Risk Intelligence Systems, OpenDeRisk——Your application system risk intelligent manager provides 7* 24-hour comprehensive and in-depth protection.

371. **[Claude-Code-Everything-You-Need-to-Know](https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know)** - ⭐ 841
   The ultimate all-in-one guide to mastering Claude Code. From setup, prompt engineering, commands, hooks, workflows, automation, and integrations, to MCP servers, tools, and the BMAD method—packed with step-by-step tutorials, real-world examples, and expert strategies to make this the global go-to repo for Claude mastery.

372. **[hyper-mcp](https://github.com/tuananh/hyper-mcp)** - ⭐ 835
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

373. **[hyper-mcp](https://github.com/joseph-wortmann/hyper-mcp)** - ⭐ 834
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

374. **[mcp-sequential-thinking](https://github.com/arben-adm/mcp-sequential-thinking)** - ⭐ 834

375. **[scira-mcp-chat](https://github.com/zaidmukaddam/scira-mcp-chat)** - ⭐ 830
   A minimalistic MCP client with a good feature set.

376. **[wassette](https://github.com/microsoft/wassette)** - ⭐ 829
   Wassette: A security-oriented runtime that runs WebAssembly Components via MCP

377. **[openapi-servers](https://github.com/open-webui/openapi-servers)** - ⭐ 825
   OpenAPI Tool Servers

378. **[excel-mcp-server](https://github.com/negokaz/excel-mcp-server)** - ⭐ 822
   A Model Context Protocol (MCP) server that reads and writes MS Excel data

379. **[yokai](https://github.com/ankorstore/yokai)** - ⭐ 819
   Simple, modular, and observable Go framework for backend applications.

380. **[statespace](https://github.com/statespace-tech/statespace)** - ⭐ 819
   Turn your data into shareable RAG apps in minutes. All in pure Markdown. Zero boilerplate.

381. **[linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server)** - ⭐ 816
   This MCP server allows Claude and other AI assistants to access your LinkedIn. Scrape LinkedIn profiles, companies and jobs, and perform job searches.

382. **[supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server)** - ⭐ 815
   Query MCP enables end-to-end management of Supabase via chat interface: read & write query executions, management API support, automatic migration versioning, access to logs and much more.

383. **[golf](https://github.com/golf-mcp/golf)** - ⭐ 811
   Production-Ready MCP Server Framework • Build, deploy & scale secure AI agent infrastructure • Includes Auth, Observability, Debugger, Telemetry & Runtime • Run real-world MCPs powering AI Agents 

384. **[server](https://github.com/php-mcp/server)** - ⭐ 810
   Core PHP implementation for the Model Context Protocol (MCP) server

385. **[toolfront](https://github.com/statespace-tech/toolfront)** - ⭐ 809
   Turn your data into shareable RAG apps in minutes. All in pure Markdown. Zero boilerplate.

386. **[apple-docs-mcp](https://github.com/kimsungwhee/apple-docs-mcp)** - ⭐ 807
   MCP server for Apple Developer Documentation - Search iOS/macOS/SwiftUI/UIKit docs, WWDC videos, Swift/Objective-C APIs & code examples in Claude, Cursor & AI assistants

387. **[DeepMCPAgent](https://github.com/cryxnet/DeepMCPAgent)** - ⭐ 804
   Model-agnostic plug-n-play LangChain/LangGraph agents powered entirely by MCP tools over HTTP/SSE.

388. **[browser-use-mcp-server](https://github.com/kontext-dev/browser-use-mcp-server)** - ⭐ 803
   Browse the web, directly from Cursor etc.

389. **[arcade-mcp](https://github.com/ArcadeAI/arcade-mcp)** - ⭐ 803
   The best way to create, deploy, and share MCP Servers

390. **[context-space](https://github.com/context-space/context-space)** - ⭐ 800
   Ultimate Context Engineering Infrastructure, starting from MCPs and Integrations

391. **[kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server)** - ⭐ 800
   A Model Context Protocol (MCP) server for Kubernetes. Install: npx kubectl-mcp-server or pip install kubectl-mcp-server

392. **[MCP-Security-Checklist](https://github.com/slowmist/MCP-Security-Checklist)** - ⭐ 799
   A comprehensive security checklist for MCP-based AI tools. Built by SlowMist to safeguard LLM plugin ecosystems.

393. **[notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp)** - ⭐ 793
   MCP server for NotebookLM - Let your AI agents (Claude Code, Codex) research documentation directly with grounded, citation-backed answers from Gemini. Persistent auth, library management, cross-client sharing. Zero hallucinations, just your knowledge base.

394. **[acemcp](https://github.com/qy527145/acemcp)** - ⭐ 791
   一个将ACE(Augment Context Engine) 做成MCP的项目

395. **[mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)** - ⭐ 790
   Scan MCP servers for potential threats & security findings.

396. **[bank-api](https://github.com/erwinkramer/bank-api)** - ⭐ 789
   The Bank API is a design reference project suitable to bootstrap development for a compliant and modern API.

397. **[claude-delegator](https://github.com/jarrodwatts/claude-delegator)** - ⭐ 789
   Delegate tasks to Codex GPT 5.2 directly from within Claude Code.

398. **[mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** - ⭐ 786
   MCP server enabling persistent memory for Claude through a local knowledge graph - fork focused on local development

399. **[duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server)** - ⭐ 786
   A Model Context Protocol (MCP) server that provides web search capabilities through DuckDuckGo, with additional features for content fetching and parsing.

400. **[qgis_mcp](https://github.com/jjsantos01/qgis_mcp)** - ⭐ 783
   Model Context Protocol (MCP) that allows LLMs to use QGIS Desktop

401. **[agent-kit](https://github.com/inngest/agent-kit)** - ⭐ 780
   AgentKit: Build multi-agent networks in TypeScript with deterministic routing and rich tooling via MCP.

402. **[Context](https://github.com/indragiek/Context)** - ⭐ 774
   Native macOS client for Model Context Protocol (MCP)

403. **[k8m](https://github.com/weibaohui/k8m)** - ⭐ 773
   一款轻量级、跨平台的 Mini Kubernetes AI Dashboard，支持大模型+智能体+MCP(支持设置操作权限)，集成多集群管理、智能分析、实时异常检测等功能，支持多架构并可单文件部署，助力高效集群管理与运维优化。

404. **[vllora](https://github.com/vllora/vllora)** - ⭐ 770
   Debug your AI agents

405. **[coderunner](https://github.com/instavm/coderunner)** - ⭐ 769
   A secure local sandbox to run LLM-generated code using Apple containers

406. **[apify-mcp-server](https://github.com/apify/apify-mcp-server)** - ⭐ 766
   The Apify MCP server enables your AI agents to extract data from social media, search engines, maps, e-commerce sites, or any other website using thousands of ready-made scrapers, crawlers, and automation tools available on the Apify Store.

407. **[vibetest-use](https://github.com/browser-use/vibetest-use)** - ⭐ 765
   Vibetest MCP - automated QA testing using Browser-Use agents

408. **[heurist-agent-framework](https://github.com/heurist-network/heurist-agent-framework)** - ⭐ 762
   A flexible multi-interface AI agent framework for building agents with reasoning, tool use, memory, deep research, blockchain interaction, MCP, and agents-as-a-service.

409. **[runno](https://github.com/taybenlor/runno)** - ⭐ 760
   Sandboxed runtime for programming languages and WASI binaries. Works in the browser, on your server, or via MCP.

410. **[mcp-marketplace](https://github.com/cline/mcp-marketplace)** - ⭐ 754
   This is the official repository for submitting MCP servers to be included in Cline's MCP Marketplace. If you’ve built an MCP server and want it to be discoverable and easily installable by millions of developers using Cline, submit your server here.

411. **[code-index-mcp](https://github.com/johnhuang316/code-index-mcp)** - ⭐ 754
   A Model Context Protocol (MCP) server that helps large language models index, search, and analyze code repositories with minimal setup

412. **[mcp-server](https://github.com/financial-datasets/mcp-server)** - ⭐ 748
   An MCP server for interacting with the Financial Datasets stock market API.

413. **[AITreasureBox](https://github.com/superiorlu/AITreasureBox)** - ⭐ 743
   🤖 Collect practical AI repos, tools, websites, papers and tutorials on AI. 实用的AI百宝箱 💎 

414. **[lisa.py](https://github.com/ant4g0nist/lisa.py)** - ⭐ 740
   LLDB MCP Integration + other helpful commands

415. **[glean](https://github.com/LeslieLeung/glean)** - ⭐ 736
   A self-hosted RSS reader and personal knowledge management tool.

416. **[context-portal](https://github.com/GreatScottyMac/context-portal)** - ⭐ 735
   Context Portal (ConPort): A memory bank MCP server building a project-specific knowledge graph to supercharge AI assistants. Enables powerful Retrieval Augmented Generation (RAG) for context-aware development in your IDE.

417. **[MassGen](https://github.com/massgen/MassGen)** - ⭐ 730
   🚀 MassGen is an open-source multi-agent scaling system that runs in your terminal, autonomously orchestrating frontier models and agents to collaborate, reason, and produce high-quality results. | Join us on Discord: discord.massgen.ai

418. **[mcp](https://github.com/hyperbrowserai/mcp)** - ⭐ 729
   A MCP server implementation for hyperbrowser

419. **[mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw)** - ⭐ 728

420. **[annas-mcp](https://github.com/iosifache/annas-mcp)** - ⭐ 724
   MCP server and CLI tool for searching and downloading documents from Anna's Archive

421. **[openmcp-client](https://github.com/LSTM-Kirigaya/openmcp-client)** - ⭐ 720
   All in one vscode plugin for mcp developer

422. **[octocode-mcp](https://github.com/bgauryy/octocode-mcp)** - ⭐ 713
   MCP server for semantic code research and context generation on real-time using LLM patterns | Search naturally across public & private repos based on your permissions | Transform any accessible codebase/s into AI-optimized knowledge on simple and complex flows | Find real implementations and live docs from anywhere

423. **[ruby-sdk](https://github.com/modelcontextprotocol/ruby-sdk)** - ⭐ 713
   The official Ruby SDK for the Model Context Protocol. Maintained in collaboration with Shopify.

424. **[12306-mcp](https://github.com/Joooook/12306-mcp)** - ⭐ 712
   This is a 12306 ticket search server based on the Model Context Protocol (MCP).

425. **[passage-of-time-mcp](https://github.com/jlumbroso/passage-of-time-mcp)** - ⭐ 711
   🤖🕰️ An MCP server that gives language models temporal awareness and time calculation abilities. Teaching AI the significance of the passage of time through collaborative tool development.

426. **[CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI)** - ⭐ 711
   CyberStrikeAI is an AI-native security testing platform built in Go. It integrates 100+ security tools, an intelligent orchestration engine, role-based testing with predefined security roles, a skills system with specialized testing skills, and comprehensive lifecycle management capabilities.

427. **[llm-functions](https://github.com/sigoden/llm-functions)** - ⭐ 708
   Easily create LLM tools and agents using plain Bash/JavaScript/Python functions.

428. **[just-prompt](https://github.com/disler/just-prompt)** - ⭐ 705
   just-prompt is an MCP server that provides a unified interface to top LLM providers (OpenAI, Anthropic, Google Gemini, Groq, DeepSeek, and Ollama)

429. **[ha-mcp](https://github.com/homeassistant-ai/ha-mcp)** - ⭐ 696
   The Unofficial and Awesome Home Assistant MCP Server

430. **[browserwing](https://github.com/browserwing/browserwing)** - ⭐ 690
   BrowserWing turns your browser actions into MCP commands Or Claude Skill, allowing AI agents to control browsers efficiently and reliably. Say goodbye to slow, token-heavy LLM interactions — let agents call commands directly for faster automation. Perfect for AI-driven tasks, browser automation, and boosting productivity.

431. **[HowToCook-mcp](https://github.com/worryzyy/HowToCook-mcp)** - ⭐ 687
   基于Anduin2017 / HowToCook （程序员在家做饭指南）的mcp server

432. **[langgraph-mcp-agents](https://github.com/teddynote-lab/langgraph-mcp-agents)** - ⭐ 684
   LangGraph-powered ReAct agent with Model Context Protocol (MCP) integration. A Streamlit web interface for dynamically configuring, deploying, and interacting with AI agents capable of accessing various data sources and APIs through MCP tools.

433. **[telegram-mcp](https://github.com/chigwell/telegram-mcp)** - ⭐ 683
   Telegram MCP server powered by Telethon to let MCP clients read chats, manage groups, and send/modify messages, media, contacts, and settings.

434. **[fetch-mcp](https://github.com/zcaceres/fetch-mcp)** - ⭐ 682
   A flexible HTTP fetching Model Context Protocol server.

435. **[llm-server-docs](https://github.com/varunvasudeva1/llm-server-docs)** - ⭐ 680
   End-to-end documentation to set up your own local & fully private LLM server on Debian. Equipped with chat, web search, RAG, model management, MCP servers, image generation, and TTS.

436. **[mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse)** - ⭐ 679
   Connect ClickHouse to your AI assistants.

437. **[drift](https://github.com/dadbodgeoff/drift)** - ⭐ 678
   Codebase intelligence for AI. Detects patterns & conventions + remembers decisions across sessions. MCP server for any IDE. Offline CLI.

438. **[clojure-mcp](https://github.com/bhauman/clojure-mcp)** - ⭐ 676
   Clojure MCP

439. **[mcp-server-docker](https://github.com/ckreiling/mcp-server-docker)** - ⭐ 675
   MCP server for Docker

440. **[cuga-agent](https://github.com/cuga-project/cuga-agent)** - ⭐ 668
   CUGA is an open-source generalist agent for the enterprise, supporting complex task execution on web and APIs, OpenAPI/MCP integrations, composable architecture, reasoning modes, and policy-aware features.

441. **[go-mcp](https://github.com/ThinkInAIXYZ/go-mcp)** - ⭐ 665
   Go-MCP is a powerful Go(Golang) version of the MCP SDK that implements the Model Context Protocol (MCP) to facilitate seamless communication between external systems and AI applications. 

442. **[mcp-client-cli](https://github.com/adhikasp/mcp-client-cli)** - ⭐ 665
   A simple CLI to run LLM prompt and implement MCP client.

443. **[mcp](https://github.com/laravel/mcp)** - ⭐ 665
   Rapidly build MCP servers for your Laravel applications.

444. **[android-mcp-server](https://github.com/minhalvp/android-mcp-server)** - ⭐ 659
   An MCP server that provides control over Android devices via adb

445. **[mcp-google-sheets](https://github.com/xing5/mcp-google-sheets)** - ⭐ 657
   This MCP server integrates with your Google Drive and Google Sheets, to enable creating and modifying spreadsheets.

446. **[yacy_grid_mcp](https://github.com/yacy/yacy_grid_mcp)** - ⭐ 654
   The YaCy Grid Master Connect Program

447. **[awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security)** - ⭐ 651
   🔥🔒 Awesome MCP (Model Context Protocol) Security 🖥️

448. **[open-ptc-agent](https://github.com/Chen-zexi/open-ptc-agent)** - ⭐ 647
   An open source implementation of code execution with MCP (Programatic Tool Calling) 

449. **[nuwax](https://github.com/nuwax-ai/nuwax)** - ⭐ 647
   Nuwax Agent OS - The world's first universal agent operating system, building your private vertical general-purpose agent.  全球首个通用智能体操作系统，打造你私有的垂类通用智能体。新一代AI应用设计、开发、实践平台，无需代码，轻松创建，适合各类人群，支持多种端发布及API，提供完善的工作流、插件以及应用开发能力，RAG知识库与数据表存储能力，MCP接入以及开放能力。

450. **[laravel-restify](https://github.com/BinarCode/laravel-restify)** - ⭐ 646
   Laravel API for Ai Agents and humans.

451. **[gcloud-mcp](https://github.com/googleapis/gcloud-mcp)** - ⭐ 645
   gcloud MCP server

452. **[llm-search](https://github.com/snexus/llm-search)** - ⭐ 644
   Querying local documents, powered by LLM

453. **[mcp-mem0](https://github.com/coleam00/mcp-mem0)** - ⭐ 644
   MCP server for long term agent memory with Mem0. Also useful as a template to get you started building your own MCP server with Python!

454. **[enrichmcp](https://github.com/featureform/enrichmcp)** - ⭐ 642
   EnrichMCP is a python framework for building data driven MCP servers

455. **[claude-code-plugins-plus](https://github.com/jeremylongshore/claude-code-plugins-plus)** - ⭐ 641
   Claude Code Plugins Hub — browse and install 243 plugins (175 with Agent Skills v1.2.0). First 100% compliant with Anthropic 2025 Skills schema.

456. **[wcgw](https://github.com/rusiaaman/wcgw)** - ⭐ 640
   Shell and coding agent on mcp clients

457. **[python-utcp](https://github.com/universal-tool-calling-protocol/python-utcp)** - ⭐ 636
   Official python implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

458. **[RAGLight](https://github.com/Bessouat40/RAGLight)** - ⭐ 636
   RAGLight is a modular framework for Retrieval-Augmented Generation (RAG). It makes it easy to plug in different LLMs, embeddings, and vector stores, and now includes seamless MCP integration to connect external tools and data sources.

459. **[drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server)** - ⭐ 636
   Draw.io Model Context Protocol (MCP) Server

460. **[paper-search-mcp](https://github.com/openags/paper-search-mcp)** - ⭐ 636
   A MCP for searching and downloading academic papers from multiple sources like arXiv, PubMed, bioRxiv, etc.

461. **[samples](https://github.com/strands-agents/samples)** - ⭐ 634
   Agent samples built using the Strands Agents SDK.

462. **[obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp)** - ⭐ 633
   A simple MCP server for Obsidian

463. **[mcp-proxy](https://github.com/tbxark/mcp-proxy)** - ⭐ 627
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single HTTP server.

464. **[mcp-proxy](https://github.com/TBXark/mcp-proxy)** - ⭐ 624
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single HTTP server.

465. **[notebooklm-mcp](https://github.com/jacob-bd/notebooklm-mcp)** - ⭐ 624

466. **[workers-mcp](https://github.com/cloudflare/workers-mcp)** - ⭐ 621
   Talk to a Cloudflare Worker from Claude Desktop!

467. **[macos-automator-mcp](https://github.com/steipete/macos-automator-mcp)** - ⭐ 617
   An MCP server to run AppleScript and JXA (JavaScript for Automation) to macOS.

468. **[mcpcan](https://github.com/Kymo-MCP/mcpcan)** - ⭐ 617
   MCPCAN is a centralized management platform for MCP services. It deploys each MCP service using a container deployment method. The platform supports container monitoring and MCP service token verification, solving security risks and enabling rapid deployment of MCP services. It uses SSE, STDIO, and STREAMABLEHTTP access protocols to deploy MCP。

469. **[phpMyFAQ](https://github.com/thorsten/phpMyFAQ)** - ⭐ 612
   phpMyFAQ - Open Source FAQ web application for PHP 8.3+ and MySQL, PostgreSQL and other databases

470. **[vibe](https://github.com/mondaycom/vibe)** - ⭐ 608
   🎨 Vibe Design System - Official monday.com UI resources for application development in React.js

471. **[a-share-mcp-is-just-i-need](https://github.com/24mlight/a-share-mcp-is-just-i-need)** - ⭐ 607

472. **[mem-agent-mcp](https://github.com/firstbatchxyz/mem-agent-mcp)** - ⭐ 606
   mem-agent mcp server

473. **[yargi-mcp](https://github.com/saidsurucu/yargi-mcp)** - ⭐ 605
   MCP Server For Turkish Legal Databases

474. **[mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch)** - ⭐ 604

475. **[brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server)** - ⭐ 602

476. **[mcp-link](https://github.com/automation-ai-labs/mcp-link)** - ⭐ 599
   Convert Any OpenAPI V3 API to MCP Server

477. **[obot](https://github.com/obot-platform/obot)** - ⭐ 596
   Complete MCP Platform -- Hosting, Registry, Gateway, and Chat Client

478. **[TuriX-CUA](https://github.com/TurixAI/TuriX-CUA)** - ⭐ 596
   This is the official website for TuriX Computer-use-Agent

479. **[awesome-web3-mcp-servers](https://github.com/demcp/awesome-web3-mcp-servers)** - ⭐ 595
   DeMCP is the first Decentralized MCP network, offering SSE proxies for MCP services and mainstream LLMs, tackling trust and security with TEE and blockchain.

480. **[FantasyPremierLeague](https://github.com/joreilly/FantasyPremierLeague)** - ⭐ 594
   Fantasy Premier League Kotlin/Compose Multiplatform sample 

481. **[FofaMap](https://github.com/asaotomo/FofaMap)** - ⭐ 594
   FofaMap v2.0 是一款基于 Python3 开发的全网首个 AI 驱动红队资产测绘智能体。在延续原有 FOFA 数据采集、存活检测、统计聚合、图标 Hash 及批量查询等核心功能的基础上，2.0 版本原生支持 MCP 协议，可无缝接入 Cursor、Claude 等 AI 平台。其核心内置了 AI 自我反思机制，能根据查询结果自动调优语法，并智能联动 Nuclei 推荐精准扫描策略，实现从“被动采集”到“主动智能决策”的红队作业进化。

482. **[mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server)** - ⭐ 593
   Go server implementing Model Context Protocol (MCP) for filesystem operations.

483. **[daydreams](https://github.com/daydreamsai/daydreams)** - ⭐ 590
   Daydreams is a set of tools for building agents for commerce

484. **[FLUJO](https://github.com/mario-andreschak/FLUJO)** - ⭐ 586
   MCP-Hub and -Inspector, Multi-Model Workflow and Chat Interface 

485. **[tome](https://github.com/runebookai/tome)** - ⭐ 586
   a magical LLM desktop client that makes it easy for *anyone* to use LLMs and MCP

486. **[next-devtools-mcp](https://github.com/vercel/next-devtools-mcp)** - ⭐ 584
   Next.js Development for Coding Agent

487. **[dexto](https://github.com/truffle-ai/dexto)** - ⭐ 583
   A coding agent and general agent harness for building and orchestrating agentic applications.

488. **[douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server)** - ⭐ 579
   提取抖音无水印视频链接，视频文案，douyin-mcp-server，mcp，claude skill

489. **[mem0-mcp](https://github.com/mem0ai/mem0-mcp)** - ⭐ 578

490. **[blueprint-mcp](https://github.com/ArcadeAI/blueprint-mcp)** - ⭐ 578
   Diagram generation for understanding codebases and system architecture using Nano Banana Pro.

491. **[langgraph-mcp](https://github.com/esxr/langgraph-mcp)** - ⭐ 575
   LangGraph solution template for MCP

492. **[MCP-Nest](https://github.com/rekog-labs/MCP-Nest)** - ⭐ 571
   A NestJS module to effortlessly create Model Context Protocol (MCP) servers for exposing AI tools, resources, and prompts.

493. **[reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant)** - ⭐ 570
   MCP server for reverse engineering tasks in Ghidra 👩‍💻

494. **[obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools)** - ⭐ 569
   Add Obsidian integrations like semantic search and custom Templater prompts to Claude or any MCP client.

495. **[spotify-mcp](https://github.com/varunneal/spotify-mcp)** - ⭐ 567
   MCP to connect your LLM with Spotify.

496. **[mcp-sequentialthinking-tools](https://github.com/spences10/mcp-sequentialthinking-tools)** - ⭐ 560
   🧠 An adaptation of the MCP Sequential Thinking Server to guide tool usage. This server provides recommendations for which MCP tools would be most effective at each stage.

497. **[mcp-pointer](https://github.com/etsd-tech/mcp-pointer)** - ⭐ 558
   MCP tool: let you point at DOM elements for your favorite agentic coding tool. Let AI see what you see.

498. **[mcp-handler](https://github.com/vercel/mcp-handler)** - ⭐ 557
   Easily spin up an MCP Server on Next.js, Nuxt, Svelte, and more

499. **[cclsp](https://github.com/ktnyt/cclsp)** - ⭐ 556
   Claude Code LSP: enhance your Claude Code experience with non-IDE dependent LSP integration.

500. **[MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe)** - ⭐ 554
   MCP-Universe is a comprehensive framework designed for developing, testing, and benchmarking AI agents

501. **[LLMTornado](https://github.com/lofcz/LLMTornado)** - ⭐ 552
   The .NET library to build AI agents with 25+ built-in connectors.

502. **[wren-engine](https://github.com/Canner/wren-engine)** - ⭐ 552
   🤖 The Semantic Engine for Model Context Protocol(MCP) Clients and AI Agents 🔥 

503. **[manim-mcp-server](https://github.com/abhiemj/manim-mcp-server)** - ⭐ 549

504. **[zypher-agent](https://github.com/corespeed-io/zypher-agent)** - ⭐ 548
   A minimal yet powerful framework for creating AI agents with full control over tools, providers, and execution flow.

505. **[mcp-for-security](https://github.com/cyproxio/mcp-for-security)** - ⭐ 545
   MCP for Security: A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

506. **[mcp-shield](https://github.com/riseandignite/mcp-shield)** - ⭐ 544
   Security scanner for MCP servers

507. **[mcp-server-neon](https://github.com/neondatabase/mcp-server-neon)** - ⭐ 544
   MCP server for interacting with Neon Management API and databases

508. **[google-search](https://github.com/web-agent-master/google-search)** - ⭐ 542
   A Playwright-based Node.js tool that bypasses search engine anti-scraping mechanisms to execute Google searches. Local alternative to SERP APIs with MCP server integration.

509. **[apple-doc-mcp](https://github.com/MightyDillah/apple-doc-mcp)** - ⭐ 542
   MCP server providing seamless access to Apple Developer Documentation with smart search and wildcard support

510. **[sentry-mcp](https://github.com/getsentry/sentry-mcp)** - ⭐ 542
   An MCP server for interacting with Sentry via LLMs.

511. **[evo-ai](https://github.com/EvolutionAPI/evo-ai)** - ⭐ 541
   Evo AI is an open-source platform for creating and managing AI agents, enabling integration with different AI models and services.

512. **[vite-plugin-vue-mcp](https://github.com/webfansplz/vite-plugin-vue-mcp)** - ⭐ 540
   Vite plugin that enables a MCP server helping models to understand your Vue app better.

513. **[homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp)** - ⭐ 540
   A MCP server for Home Assistant

514. **[echokit_server](https://github.com/second-state/echokit_server)** - ⭐ 539
   Open Source Voice Agent Platform

515. **[multimodal-agents-course](https://github.com/the-ai-merge/multimodal-agents-course)** - ⭐ 539
   An MCP Multimodal AI Agent with eyes and ears!

516. **[burp-ai-agent](https://github.com/six2dez/burp-ai-agent)** - ⭐ 538
   Burp Suite extension that adds built-in MCP tooling, AI-assisted analysis, privacy controls, passive and active scanning and more

517. **[awesome-mcp-servers](https://github.com/TensorBlock/awesome-mcp-servers)** - ⭐ 537
   A comprehensive collection of Model Context Protocol (MCP) servers

518. **[fastapi-mcp-langgraph-template](https://github.com/NicholasGoh/fastapi-mcp-langgraph-template)** - ⭐ 535
   A modern template for agentic orchestration — built for rapid iteration and scalable deployment using highly customizable, community-supported tools like MCP, LangGraph, and more.

519. **[Mantic.sh](https://github.com/marcoaapfortes/Mantic.sh)** - ⭐ 535
   A structural code search engine for Al agents.

520. **[pg-mcp-server](https://github.com/stuzero/pg-mcp-server)** - ⭐ 534

521. **[tda](https://github.com/irockel/tda)** - ⭐ 534
   TDA - Thread Dump Analyzer (for Java)

522. **[mcp.el](https://github.com/lizqwerscott/mcp.el)** - ⭐ 534
   An Mcp client inside Emacs

523. **[dolphin-mcp](https://github.com/QuixiAI/dolphin-mcp)** - ⭐ 532

524. **[cloud-run-mcp](https://github.com/GoogleCloudPlatform/cloud-run-mcp)** - ⭐ 532
   MCP server to deploy apps to Cloud Run

525. **[mcp-client-for-ollama](https://github.com/jonigl/mcp-client-for-ollama)** - ⭐ 528
   A text-based user interface (TUI) client for interacting with MCP servers using Ollama. Features include agent mode, multi-server, model switching, streaming responses, tool management, human-in-the-loop, thinking mode, model params config, MCP prompts, custom system prompt and saved preferences. Built for developers working with local LLMs.

526. **[awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw)** - ⭐ 525
   A curated list of awesome OpenClaw resources, tools, skills, tutorials, and articles. The open-source AI agent taking the world by storm.

527. **[mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)** - ⭐ 522

528. **[pgmcp](https://github.com/subnetmarco/pgmcp)** - ⭐ 521
   An MCP server to query any Postgres database in natural language.

529. **[iterm-mcp](https://github.com/ferrislucas/iterm-mcp)** - ⭐ 521
   A Model Context Protocol server that executes commands in the current iTerm session - useful for REPL and CLI assistance

530. **[line-bot-mcp-server](https://github.com/line/line-bot-mcp-server)** - ⭐ 519
   MCP server that integrates the LINE Messaging API to connect an AI Agent to the LINE Official Account.

531. **[mcp-server-weread](https://github.com/freestylefly/mcp-server-weread)** - ⭐ 519
   微信读书MCP

532. **[ethora](https://github.com/dappros/ethora)** - ⭐ 519
   Open-source engine for chat 💬, AI assistants 🤖 & wallets 🪪. React, Typescript, Python, XMPP. Build future apps with chat, AI agents and web3.

533. **[skybridge](https://github.com/alpic-ai/skybridge)** - ⭐ 517
   Skybridge is a framework for building ChatGPT & MCP Apps

534. **[gateway](https://github.com/centralmind/gateway)** - ⭐ 516
   Universal MCP-Server for your Databases optimized for LLMs and AI-Agents.

535. **[apple-health-mcp](https://github.com/neiltron/apple-health-mcp)** - ⭐ 516
   MCP server for querying Apple Health data with natural language and SQL

536. **[ghostcrew](https://github.com/GH05TCREW/ghostcrew)** - ⭐ 515
   GhostCrew is an AI agent framework for bug bounty hunting, red-team operations, pentesting, and operator education. It integrates LLM autonomy, multi-agent coordination, and MCP extensibility with a minimal core toolset, supported by RAG for context-aware reasoning, a persistent internal state, reproducible workflows, and interactive assistance.

537. **[ida-mcp-server](https://github.com/MxIris-Reverse-Engineering/ida-mcp-server)** - ⭐ 513
   A Model Context Protocol server for IDA

538. **[openapi-mcp-generator](https://github.com/harsha-iiiv/openapi-mcp-generator)** - ⭐ 511
   A tool that converts OpenAPI specifications to MCP server

539. **[davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp)** - ⭐ 511
   MCP server integration for DaVinci Resolve

540. **[awesome-a2a](https://github.com/ai-boost/awesome-a2a)** - ⭐ 510
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place.

541. **[web-search-mcp](https://github.com/mrkrsl/web-search-mcp)** - ⭐ 510
   A simple, locally hosted Web Search MCP server for use with Local LLMs

542. **[multimodal-agents-course](https://github.com/multi-modal-ai/multimodal-agents-course)** - ⭐ 507
   An MCP Multimodal AI Agent with eyes and ears!

543. **[mcp-get](https://github.com/michaellatman/mcp-get)** - ⭐ 505

544. **[mcp-adapter](https://github.com/WordPress/mcp-adapter)** - ⭐ 502
   An MCP adapter that bridges the Abilities API to the Model Context Protocol, enabling MCP clients to discover and invoke WordPress plugin, theme, and core abilities programmatically.

545. **[mcp-server-bash-sdk](https://github.com/muthuishere/mcp-server-bash-sdk)** - ⭐ 501
   Yes Mcp server in bash

546. **[UnityMCP](https://github.com/jackwrichards/UnityMCP)** - ⭐ 499

547. **[freecad-mcp](https://github.com/neka-nat/freecad-mcp)** - ⭐ 499
   FreeCAD MCP(Model Context Protocol) server

548. **[MCPSpy](https://github.com/alex-ilgayev/MCPSpy)** - ⭐ 497
   MCP Monitoring with eBPF

549. **[rails-mcp-server](https://github.com/maquina-app/rails-mcp-server)** - ⭐ 496
   A Ruby gem implementation of a Model Context Protocol (MCP) server for Rails projects. This server allows LLMs (Large Language Models) to interact with Rails projects through the Model Context Protocol.

550. **[AnyTool](https://github.com/HKUDS/AnyTool)** - ⭐ 496
   "AnyTool: Universal Tool-Use Layer for AI Agents"

551. **[alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server)** - ⭐ 495
   Alpaca’s official MCP Server lets you trade stocks, ETFs, crypto, and options, run data analysis, and build strategies in plain English directly from your favorite LLM tools and IDEs

552. **[mcp-pandoc](https://github.com/vivekVells/mcp-pandoc)** - ⭐ 494
   MCP server for document format conversion using pandoc.

553. **[PentestAgent](https://github.com/GH05TCREW/PentestAgent)** - ⭐ 493
   All-in-one offensive security toolbox with AI agent and MCP architecture. Integrates tools like Nmap, Metasploit, FFUF, SQLMap. Enables pentesting, bug bounty hunting, threat hunting, and reporting. RAG-based responses with local knowledge base support.

554. **[UnrealMCP](https://github.com/kvick-games/UnrealMCP)** - ⭐ 493
   MCP to allow AI agents to control Unreal

555. **[UnityMCP](https://github.com/Arodoid/UnityMCP)** - ⭐ 491

556. **[web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)** - ⭐ 491
   🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support

557. **[talk-to-girlfriend-ai](https://github.com/arlanrakh/talk-to-girlfriend-ai)** - ⭐ 491
   im busy building ai agents so why not let an ai talk to my girlfriend? (i am single) 

558. **[mcp-youtube](https://github.com/anaisbetts/mcp-youtube)** - ⭐ 490
   A Model-Context Protocol Server for YouTube

559. **[borsa-mcp](https://github.com/saidsurucu/borsa-mcp)** - ⭐ 490
   MCP Server for Turkish & American Stock Exchange and Fund Data

560. **[cli](https://github.com/smithery-ai/cli)** - ⭐ 489
   Install, manage and develop MCP servers and skills for agents

561. **[MetasploitMCP](https://github.com/GH05TCREW/MetasploitMCP)** - ⭐ 489
   MCP Server for Metasploit

562. **[chroma-mcp](https://github.com/chroma-core/chroma-mcp)** - ⭐ 489
   A Model Context Protocol (MCP) server implementation that provides database capabilities for Chroma

563. **[cupertino](https://github.com/mihaelamj/cupertino)** - ⭐ 488
   A local Apple Documentation crawler and MCP server. Written in Swift.

564. **[claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you)** - ⭐ 483
   Enable any LLM (e.g. Claude) to interactively debug any language for you via MCP and a VS Code Extension

565. **[llm-mcp-rag](https://github.com/KelvinQiu802/llm-mcp-rag)** - ⭐ 483
   LLM + MCP + RAG = Magic

566. **[haiku.rag](https://github.com/ggozad/haiku.rag)** - ⭐ 482
   Opinionated agentic RAG powered by LanceDB, Pydantic AI, and Docling

567. **[dbt-mcp](https://github.com/dbt-labs/dbt-mcp)** - ⭐ 482
   A MCP (Model Context Protocol) server for interacting with dbt.

568. **[pdf-reader-mcp](https://github.com/SylphxAI/pdf-reader-mcp)** - ⭐ 482
   📄 Production-ready MCP server for PDF processing - 5-10x faster with parallel processing and 94%+ test coverage

569. **[bm.md](https://github.com/miantiao-me/bm.md)** - ⭐ 480
   更好用的 Markdown 排版助手｜一键适配微信公众号、网页与图片。

570. **[n8n-workflow-builder](https://github.com/makafeli/n8n-workflow-builder)** - ⭐ 477
   AI assistant integration for n8n workflow automation through Model Context Protocol (MCP). Connect Claude Desktop, ChatGPT, and other AI assistants to n8n for natural language workflow management.

571. **[MCP-Kali-Server](https://github.com/Wh0am123/MCP-Kali-Server)** - ⭐ 474
   MCP configuration to connect AI agent to a Linux machine.

572. **[mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite)** - ⭐ 472
   MCP Server to interact with Google Gsuite prodcuts

573. **[open-multi-agent-canvas](https://github.com/CopilotKit/open-multi-agent-canvas)** - ⭐ 471
   The open-source multi-agent chat interface that lets you manage multiple agents in one dynamic conversation and add MCP servers for deep research

574. **[laravel](https://github.com/php-mcp/laravel)** - ⭐ 470
   An SDK building Laravel MCP servers

575. **[argo](https://github.com/xark-argo/argo)** - ⭐ 470
   ARGO is an open-source AI Agent platform that brings Local Manus to your desktop. With one-click model downloads, seamless closed LLM integration, and offline-first RAG knowledge bases, ARGO becomes a DeepResearch powerhouse for autonomous thinking, task planning, and 100% of your data stays locally. Support Win/Mac/Docker.

576. **[aser](https://github.com/AmeNetwork/aser)** - ⭐ 469
   Aser is a lightweight, self-assembling AI Agent frame.

577. **[mcp-server](https://github.com/PortSwigger/mcp-server)** - ⭐ 469
   MCP Server for Burp

578. **[mineru-tianshu](https://github.com/magicyuan876/mineru-tianshu)** - ⭐ 468
   天枢 - 企业级 AI 一站式数据预处理平台 | PDF/Office转Markdown | 支持MCP协议AI助手集成 | Vue3+FastAPI全栈方案 | 文档解析 | 多模态信息提取

579. **[minecraft-mcp-server](https://github.com/yuniko-software/minecraft-mcp-server)** - ⭐ 466
   A Minecraft MCP Server powered by Mineflayer API. It allows to control a Minecraft character in real-time, allowing AI assistants to build structures, explore the world, and interact with the game environment through natural language instruction

580. **[atlas-mcp-server](https://github.com/cyanheads/atlas-mcp-server)** - ⭐ 464
   A Model Context Protocol (MCP) server for ATLAS, a Neo4j-powered task management system for LLM Agents - implementing a three-tier architecture (Projects, Tasks, Knowledge) to manage complex workflows. Now with Deep Research.

581. **[copilot-mcp](https://github.com/VikashLoomba/copilot-mcp)** - ⭐ 464
   A powerful VSCode extension that lets you find and install MCP servers to use with GitHub Copilot, Claude Code, and Codex CLI.

582. **[mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript)** - ⭐ 464
   This is an MCP server that allows you to directly download transcripts of YouTube videos.

583. **[nexus](https://github.com/Nexus-Router/nexus)** - ⭐ 463
   Govern & Secure your AI

584. **[flux-operator](https://github.com/controlplaneio-fluxcd/flux-operator)** - ⭐ 463
   GitOps on Autopilot Mode

585. **[vibe-check-mcp-server](https://github.com/PV-Bhat/vibe-check-mcp-server)** - ⭐ 462
   Vibe Check is a tool that provides mentor-like feedback to AI Agents, preventing tunnel-vision, over-engineering and reasoning lock-in for complex and long-horizon agent workflows. KISS your over-eager AI Agents goodbye! Effective for: Coding, Ambiguous Tasks, High-Risk tasks

586. **[clickup-mcp-server](https://github.com/taazkareem/clickup-mcp-server)** - ⭐ 462
   ClickUp MCP Server - Integrate ClickUp project management with AI through Model Context Protocol

587. **[doctor](https://github.com/sisig-ai/doctor)** - ⭐ 462
   Doctor is a tool for discovering, crawl, and indexing web sites to be exposed as an MCP server for LLM agents.

588. **[meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp)** - ⭐ 462
   MCP server to manage Facebook and Instagram Ads (Meta Ads)

589. **[deeppowers](https://github.com/deeppowers/deeppowers)** - ⭐ 460
   DEEPPOWERS is a Fully Homomorphic Encryption (FHE) framework built for MCP (Model Context Protocol), aiming to provide end-to-end privacy protection and high-efficiency computation for the upstream and downstream ecosystem of the MCP protocol.

590. **[director](https://github.com/director-run/director)** - ⭐ 458
   MCP Playbooks for AI agents

591. **[ai-trader](https://github.com/whchien/ai-trader)** - ⭐ 458
   Backtrader-powered backtesting framework for algorithmic trading, featuring 20+ strategies, multi-market support, CLI tools, and an integrated MCP server for professional traders.

592. **[mcp-remote-macos-use](https://github.com/baryhuang/mcp-remote-macos-use)** - ⭐ 457
   The only general AI agent that does NOT requires extra API key, giving you full control on your local and remote MacOs from Claude Desktop App

593. **[adb-mcp](https://github.com/mikechambers/adb-mcp)** - ⭐ 457

594. **[mcp-gateway](https://github.com/microsoft/mcp-gateway)** - ⭐ 457
   MCP Gateway is a reverse proxy and management layer for MCP servers, enabling scalable, session-aware stateful routing and lifecycle management of MCP servers in Kubernetes environments.

595. **[tsidp](https://github.com/tailscale/tsidp)** - ⭐ 456
   A simple OIDC / OAuth Identity Provider (IdP) server for your tailnet.

596. **[sdk-typescript](https://github.com/strands-agents/sdk-typescript)** - ⭐ 454
   A model-driven approach to building AI agents in just a few lines of code. 

597. **[mcpe](https://github.com/ReMinecraftPE/mcpe)** - ⭐ 450
   ReMinecraftPE - A custom experience based on Minecraft PE as of 2011.

598. **[awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins)** - ⭐ 450
   Awesome Claude Code plugins — a curated list of slash commands, subagents, MCP servers, and hooks for Claude Code

599. **[mcp-obsidian](https://github.com/bitbonsai/mcp-obsidian)** - ⭐ 450
   A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access

600. **[docker-mcp](https://github.com/QuantGeekDev/docker-mcp)** - ⭐ 449
   A docker MCP Server (modelcontextprotocol)

601. **[ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server)** - ⭐ 448
   A Model Context Protocol (MCP) server for interacting with Microsoft 365 and Office services through the Graph API

602. **[nexus](https://github.com/grafbase/nexus)** - ⭐ 446
   Govern & Secure your AI

603. **[nexus](https://github.com/nexus-ai-labs/nexus)** - ⭐ 446
   Govern & Secure your AI

604. **[MCP](https://github.com/jina-ai/MCP)** - ⭐ 446
   Official Jina AI Remote MCP Server

605. **[MCP-Zero](https://github.com/xfey/MCP-Zero)** - ⭐ 444
   MCP-Zero: Active Tool Discovery for Autonomous LLM Agents

606. **[mcp-send-email](https://github.com/resend/mcp-send-email)** - ⭐ 444
   Send emails directly from Cursor with this email sending MCP server

607. **[claude-pilot](https://github.com/maxritter/claude-pilot)** - ⭐ 444
   Claude Code is powerful. Pilot makes it reliable. Tests enforced. Context preserved. Quality automated. ☑️

608. **[Godot-MCP](https://github.com/ee0pdt/Godot-MCP)** - ⭐ 442
   An MCP for Godot that lets you create and edit games in the Godot game engine with tools like Claude

609. **[mcp-bench](https://github.com/Accenture/mcp-bench)** - ⭐ 441
   MCP-Bench: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers

610. **[mcp-security](https://github.com/google/mcp-security)** - ⭐ 440

611. **[prism-insight](https://github.com/dragon1086/prism-insight)** - ⭐ 439
   AI-based stock analysis and trading system

612. **[work-iq-mcp](https://github.com/microsoft/work-iq-mcp)** - ⭐ 439
   MCP Server and CLI for accessing Work IQ

613. **[youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server)** - ⭐ 438
   MCP Server for YouTube API, enabling video management, Shorts creation, and advanced analytics

614. **[unreal-engine-mcp](https://github.com/flopperam/unreal-engine-mcp)** - ⭐ 437
   Control Unreal Engine 5.5+ through AI with natural language. Build incredible 3D worlds and architectural masterpieces using MCP. Create entire towns, medieval castles, modern mansions, challenging mazes, and complex structures with AI-powered commands.

615. **[cocos-mcp-server](https://github.com/DaxianLee/cocos-mcp-server)** - ⭐ 435
   一款全面的、便捷的cocos creator AI MCP服务插件，适用于3.8.0以上cocos版本，一键安装，一键启动。A comprehensive and convenient cocos creator AI MCP service plug-in, suitable for cocos versions above 3.8.0, one-click installation and one-click start.

616. **[AgentX](https://github.com/lucky-aeon/AgentX)** - ⭐ 433
   AgentX 致力于让小白也能无门槛通过自然语言打造属于自己的 Agent。AgentX 采用了自研 MCP 网关，模型高可用组件打造高可用

617. **[lanhu-mcp](https://github.com/dsphper/lanhu-mcp)** - ⭐ 433
   ⚡ 需求分析效率提升 200%！全球首个为 AI 编程时代设计的团队协作 MCP 服务器，自动分析需求自动编写前后端代码，下载切图

618. **[mcp-searxng](https://github.com/ihor-sokoliuk/mcp-searxng)** - ⭐ 433
   MCP Server for SearXNG

619. **[xhs-mcp](https://github.com/jobsonlook/xhs-mcp)** - ⭐ 432
   小红书MCP服务 x-s x-t js逆向

620. **[joinly](https://github.com/joinly-ai/joinly)** - ⭐ 432
   Make your meetings accessible to AI Agents

621. **[mcp-hub](https://github.com/ravitemer/mcp-hub)** - ⭐ 431
   A centralized manager for Model Context Protocol (MCP) servers with dynamic server management and monitoring

622. **[FinanceMCP](https://github.com/guangxiangdebizi/FinanceMCP)** - ⭐ 431
   这是一个金融领域相关的mcp,本项目通过集成 Tushare API 和 Binance API 为语言模型（如Claude）提供全面的实时金融数据访问能力，支持股票、基金、债券、宏观经济指标、稳定币、虚拟货币等多维度金融数据分析。其中也包含了金融数据查询、财经新闻查询、国家统计局数据查询等

623. **[agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)** - ⭐ 430
   A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.

624. **[lark-openapi-mcp](https://github.com/larksuite/lark-openapi-mcp)** - ⭐ 429
   飞书/Lark官方 OpenAPI MCP

625. **[mcp-nixos](https://github.com/utensils/mcp-nixos)** - ⭐ 428
   MCP-NixOS - Model Context Protocol Server for NixOS resources

626. **[mcpstore](https://github.com/whillhill/mcpstore)** - ⭐ 425
   开盒即用的优雅管理mcp服务 | 结合Agent框架 | 作者听劝 | 已发布pypi | Vue页面demo 

627. **[CoexistAI](https://github.com/SPThole/CoexistAI)** - ⭐ 425
   CoexistAI is a modular, developer-friendly research assistant framework . It enables you to build, search, summarize, and automate research workflows using LLMs, web search, Reddit, YouTube, and mapping tools—all with simple MCP tool calls or API calls or Python functions. 

628. **[mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry)** - ⭐ 425
   Enterprise-ready MCP Gateway & Registry that centralizes AI development tools with secure OAuth authentication, dynamic tool discovery, and unified access for both autonomous AI agents and AI coding assistants. Transform scattered MCP server chaos into governed, auditable tool access with Keycloak/Entra integration.

629. **[mcp-server-spec-driven-development](https://github.com/formulahendry/mcp-server-spec-driven-development)** - ⭐ 423
   Spec-Driven Development MCP Server, not just Vibe Coding

630. **[kratos-transport](https://github.com/tx7do/kratos-transport)** - ⭐ 423
   kratos transport layer extension, support: rabbitmq,kafka,rocketmq,activemq,apollo,mcp,tcp,websocket...

631. **[claude-codepro](https://github.com/maxritter/claude-codepro)** - ⭐ 422
   Production-Grade Development Environment for Claude Code. Quality automated. Context optimized. Testing enforced. Ship with confidence. ✔️

632. **[learn-low-code-agentic-ai](https://github.com/panaversity/learn-low-code-agentic-ai)** - ⭐ 422
   Low-Code Full-Stack Agentic AI Development using LLMs, n8n, Loveable, UXPilot, Supabase and MCP. Class Videos: https://www.youtube.com/playlist?list=PL0vKVrkG4hWq5T6yqCtUL7ol9rDuEyzBH

633. **[GhidrAssistMCP](https://github.com/jtang613/GhidrAssistMCP)** - ⭐ 420
   An MCP extension for Ghidra

634. **[codexia](https://github.com/milisp/codexia)** - ⭐ 420
   A powerfull GUI and Toolkit for Codex CLI + Claude Code. FileTree + prompt notepad + git worktree and more

635. **[mcp-registry](https://github.com/docker/mcp-registry)** - ⭐ 419
   Official Docker MCP registry 

636. **[kmcp](https://github.com/kagent-dev/kmcp)** - ⭐ 418
   CLI tool and Kubernetes Controller for building, testing and deploying MCP servers

637. **[mcp-redis](https://github.com/redis/mcp-redis)** - ⭐ 418
   The official Redis MCP Server is a natural language interface designed for agentic applications to manage and search data in Redis efficiently

638. **[mcpadapt](https://github.com/grll/mcpadapt)** - ⭐ 416
   Unlock 650+ MCP servers tools in your favorite agentic framework.

639. **[Feishu-MCP](https://github.com/cso1z/Feishu-MCP)** - ⭐ 416
   为 Cursor、Windsurf、Cline 和其他 AI 驱动的编码工具提供访问、编辑和结构化处理飞书文档的能力，基于 Model Context Protocol 服务器实现。

640. **[shinkai-local-ai-agents](https://github.com/dcSpark/shinkai-local-ai-agents)** - ⭐ 415
   Shinkai is a two click install App that allows you to create Local AI agents in 5 minutes or less using a simple UI.  Supports: MCPs, Remote and Local AI, Crypto and Payments.

641. **[applescript-mcp](https://github.com/peakmojo/applescript-mcp)** - ⭐ 414
   MCP server that execute applescript giving you full control of your Mac

642. **[awesome-mcp-devtools](https://github.com/punkpeye/awesome-mcp-devtools)** - ⭐ 413
   A curated list of developer tools, SDKs, libraries, and testing utilities for Model Context Protocol (MCP) server development.

643. **[home-assistant-vibecode-agent](https://github.com/Coolver/home-assistant-vibecode-agent)** - ⭐ 413
   Home Assistant MCP server agent. Enable Cursor, VS Code, Claude Code, or any MCP-enabled IDE to help you vibe-code and manage Home Assistant: create and debug automations, design dashboards, tweak themes, modify configs, and deploy changes using natural language

644. **[azure-ai-travel-agents](https://github.com/Azure-Samples/azure-ai-travel-agents)** - ⭐ 412
   A robust enterprise application sample (deployed on ACA) that leverages MCP and multiple AI agents orchestrated by Langchain.js, Llamaindex.TS and Microsoft Agent Framework.

645. **[mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck)** - ⭐ 412
   Local MCP server for DuckDB and MotherDuck

646. **[mcp-cli](https://github.com/wong2/mcp-cli)** - ⭐ 411
   A CLI inspector for the Model Context Protocol

647. **[NetCoreKevin](https://github.com/junkai-li/NetCoreKevin)** - ⭐ 411
   基于NET搭建-AI知识库智能体-现代化Saas企业级前后端分离架构：前端Vue3、IDS4单点登录、多缓存、自动任务、分布式、一库多租户、日志、授权和鉴权、CAP集成事件、SignalR、领域事件、ESL、MCP协议服务、IOC模块化注入、Cors、Quartz自动任务、多短信集成、AI、AgentFramework智能体、AISemanticKernel集成、RAG检索增强、OCR识别、API多版本、单元测试、RabbitMQ、代码生成器、AI知识库、AI联网搜索

648. **[biomcp](https://github.com/genomoncology/biomcp)** - ⭐ 410
   BioMCP: Biomedical Model Context Protocol

649. **[docfork](https://github.com/docfork/docfork)** - ⭐ 410
   Docfork - Up-to-date Docs for AI Agents.

650. **[airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server)** - ⭐ 409
   🗂️🤖 Airtable Model Context Protocol Server, for allowing AI systems to interact with your Airtable bases

651. **[mcp-mermaid](https://github.com/hustcc/mcp-mermaid)** - ⭐ 408
   ❤️ Generate mermaid diagram and chart with AI MCP dynamically.

652. **[claude-codex-settings](https://github.com/fcakyon/claude-codex-settings)** - ⭐ 406
   My personal Claude Code and OpenAI Codex setup with battle-tested skills, commands, hooks, agents and MCP servers that I use daily.

653. **[CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext)** - ⭐ 404
   An MCP server plus a CLI tool that indexes local code into a graph database to provide context to AI assistants.

654. **[RestClient.Net](https://github.com/MelbourneDeveloper/RestClient.Net)** - ⭐ 403
   The safest way to make REST calls in C# with an MCP Generator

655. **[Software-planning-mcp](https://github.com/NightTrek/Software-planning-mcp)** - ⭐ 399
   An experiment in software planning using MCP

656. **[mcp](https://github.com/baidu-maps/mcp)** - ⭐ 398
   Baidu Map MCP Server

657. **[docling-mcp](https://github.com/docling-project/docling-mcp)** - ⭐ 396
   Making docling agentic through MCP

658. **[lunar](https://github.com/TheLunarCompany/lunar)** - ⭐ 395
   lunar.dev: Agent native MCP Gateway for governance and security

659. **[memento-mcp](https://github.com/gannonh/memento-mcp)** - ⭐ 394
   Memento MCP: A Knowledge Graph Memory System for LLMs

660. **[chatluna](https://github.com/ChatLunaLab/chatluna)** - ⭐ 391
   多平台模型接入，可扩展，多种输出格式，提供大语言模型聊天服务的插件 | A bot plugin for LLM chat with multi-model integration, extensibility, and various output formats

661. **[UnrealGenAISupport](https://github.com/prajwalshettydev/UnrealGenAISupport)** - ⭐ 389
   An Unreal Engine plugin for LLM/GenAI models & MCP UE5 server. Includes OpenAI's GPT 5.1, Deepseek V3.1, Claude Sonnet 4.5 APIs, Gemini 3, Alibaba Qwen, Kimi and Grok 4.1, with plans to add Gemini, audio tts, elevenlabs, OpenRouter, Groq, Dashscope & realtime APIs soon. UnrealMCP is also here!! Automatic scene generation from AI!! 

662. **[mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy)** - ⭐ 387
   A MCP (model context protocol) server that gives the LLM access to and knowledge about relational databases like SQLite, Postgresql, MySQL & MariaDB, Oracle, and MS-SQL.

663. **[mcp-google-ads](https://github.com/cohnen/mcp-google-ads)** - ⭐ 387
   An MCP tool that connects Google Ads with Claude AI/Cursor and others, allowing you to analyze your advertising data through natural language conversations. This integration gives you access to campaign information, performance metrics, keyword analytics, and ad management—all through simple chat with Claude, Cursor or Windsurf.

664. **[edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp)** - ⭐ 385
   An MCP service designed for deploying HTML content to EdgeOne Pages and obtaining an accessible public URL.

665. **[MCP-SecurityTools](https://github.com/Ta0ing/MCP-SecurityTools)** - ⭐ 383
   MCP-SecurityTools 是一个专注于收录和更新网络安全领域 MCP 的开源项目，旨在汇总、整理和优化各类与 MCP 相关的安全工具、技术及实战经验。

666. **[ai4j](https://github.com/LnYo-Cly/ai4j)** - ⭐ 383
   一款JavaSDK用于快速接入AI大模型应用，整合多平台大模型，如OpenAi、智谱Zhipu(ChatGLM)、深度求索DeepSeek、月之暗面Moonshot(Kimi)、腾讯混元Hunyuan、零一万物(01)等等，提供统一的输入输出(对齐OpenAi)消除差异化，优化函数调用(Tool Call)，优化RAG调用、支持向量数据库(Pinecone)、内置联网增强，并且支持JDK1.8，为用户提供快速整合AI的能力。

667. **[mcpmark](https://github.com/eval-sys/mcpmark)** - ⭐ 382
   MCPMark is a comprehensive, stress-testing MCP benchmark designed to evaluate model and agent capabilities in real-world MCP use.

668. **[groq-desktop-beta](https://github.com/groq/groq-desktop-beta)** - ⭐ 382
   Local Groq Desktop chat app with MCP support

669. **[mcp-hfspace](https://github.com/evalstate/mcp-hfspace)** - ⭐ 382
   MCP Server to Use HuggingFace spaces, easy configuration and Claude Desktop mode. 

670. **[minion-agent](https://github.com/femto/minion-agent)** - ⭐ 381
   A simple agent framework that's capable of browser use + mcp + auto instrument + plan + deep  research + more

671. **[agent-builder](https://github.com/strands-agents/agent-builder)** - ⭐ 381
   An example agent demonstrating streaming, tool use, and interactivity from your terminal. This agent builder can help you to build your own agents and tools.

672. **[puppeteer-mcp-server](https://github.com/merajmehrabi/puppeteer-mcp-server)** - ⭐ 380
   This MCP server provides browser automation capabilities through Puppeteer, allowing interaction with both new browser instances and existing Chrome windows.

673. **[station](https://github.com/cloudshipai/station)** - ⭐ 379
   Station is our open-source runtime that lets teams deploy agents on their own infrastructure with full control.

674. **[Agentfy](https://github.com/Agentfy-io/Agentfy)** - ⭐ 379
   🤖 Agentfy is a modular microservices architecture designed to process user requests and execute workflows across multiple social media platforms.  ASK ONCE, LET THE AGENT DO THE REST!

675. **[labs-ai-tools-for-devs](https://github.com/docker/labs-ai-tools-for-devs)** - ⭐ 377
   Your trusted home for discovering MCP tools – seamlessly integrated into Docker

676. **[kicad-mcp](https://github.com/lamaalrajih/kicad-mcp)** - ⭐ 377
   Model Context Protocol server for KiCad on Mac, Windows, and Linux

677. **[better-icons](https://github.com/better-auth/better-icons)** - ⭐ 377
   Skill and MCP server for searching and retrieving icons

678. **[mcp-code-graph](https://github.com/JudiniLabs/mcp-code-graph)** - ⭐ 376
   MCP Server for code graph analysis and visualization by CodeGPT

679. **[Redbook-Search-Comment-MCP2.0](https://github.com/chenningling/Redbook-Search-Comment-MCP2.0)** - ⭐ 375
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client（如Claude for Desktop），帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布AI生成评论等操作。

680. **[yutu](https://github.com/eat-pray-ai/yutu)** - ⭐ 374
   A fully functional MCP server and CLI for YouTube

681. **[sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)** - ⭐ 374
   SonarQube MCP Server

682. **[powerbi-modeling-mcp](https://github.com/microsoft/powerbi-modeling-mcp)** - ⭐ 374
   The Power BI Modeling MCP Server, brings Power BI semantic modeling capabilities to your AI agents.

683. **[Anemoi](https://github.com/Coral-Protocol/Anemoi)** - ⭐ 373
   Anemoi: A Semi-Centralized Multi-agent Systems Based on Agent-to-Agent Communication MCP server from Coral Protocol

684. **[mcp-server](https://github.com/e2b-dev/mcp-server)** - ⭐ 373
   Giving Claude ability to run code with E2B via MCP (Model Context Protocol)

685. **[reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy)** - ⭐ 373
   Clean, LLM-optimized Reddit MCP server. Browse posts, search content, analyze users. No fluff, just Reddit data.

686. **[docfork-mcp](https://github.com/docfork/docfork-mcp)** - ⭐ 372
   Docfork MCP - Up-to-date Docs for AI Agents.

687. **[graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server)** - ⭐ 372
   Model Context Protocol (MCP) Server for Graphlit Platform

688. **[mcp-k8s-go](https://github.com/strowk/mcp-k8s-go)** - ⭐ 372
   MCP server connecting to Kubernetes

689. **[bagel](https://github.com/Extelligence-ai/bagel)** - ⭐ 371
   Chat with your robotics, drone, and IoT data — ChatGPT for the physical world.

690. **[mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb)** - ⭐ 371
   Search Airbnb using your AI Agent

691. **[mcp](https://github.com/mondaycom/mcp)** - ⭐ 371
   Enable AI agents to work reliably - giving them secure access to structured data, tools to take action, and the context needed to make smart decisions.

692. **[MoltBrain](https://github.com/nhevers/MoltBrain)** - ⭐ 370
   Long-term memory layer for OpenClaw & MoltBook agents that learns and recalls your project context automatically.

693. **[OpenContext](https://github.com/0xranx/OpenContext)** - ⭐ 370
   A personal context store for AI agents and assistants—reuse your existing coding agent CLI (Codex/Claude/OpenCode) with built‑in Skills/tools and a desktop GUI to capture, search, and reuse project knowledge across agents and repos.

694. **[mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub)** - ⭐ 369
   A growing collection of MCP servers bringing offensive security tools to AI assistants. Nmap, Ghidra, Nuclei, SQLMap, Hashcat and more.

695. **[generative-ui](https://github.com/CopilotKit/generative-ui)** - ⭐ 368
   Generative UI examples for: AG-UI, A2UI/Open-JSON-UI, and MCP Apps.

696. **[mnemo](https://github.com/MnemoAI/mnemo)** - ⭐ 366
   A MCP-Ready Intelligence Engine for Data & Agent-as-a-Service.

697. **[agent](https://github.com/1mcp-app/agent)** - ⭐ 366
   A unified Model Context Protocol server implementation that aggregates multiple MCP servers into one.

698. **[VTCode](https://github.com/vinhnx/VTCode)** - ⭐ 365
   VT Code - Semantic coding agent in the terminal

699. **[evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server)** - ⭐ 364
   MCP server that provides LLMs with tools for interacting with EVM networks

700. **[open-skills](https://github.com/instavm/open-skills)** - ⭐ 363
   OpenSkills: Run Claude Skills Locally using any LLM

701. **[tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp)** - ⭐ 363
    Advanced TradingView MCP Server for AI-powered market analysis. Real-time crypto & stock screening, technical indicators, Bollinger Band intelligence, and candlestick patterns. Works with Claude Desktop & AI assistants. Multi-exchange support (Binance, KuCoin, Bybit+). Open source trading toolkit.

702. **[mcp-sdk-php](https://github.com/logiscape/mcp-sdk-php)** - ⭐ 362
   Model Context Protocol SDK for PHP

703. **[automation-mcp](https://github.com/ashwwwin/automation-mcp)** - ⭐ 360
   Control your Mac with detailed mouse, keyboard, screen, and window management capabilities.

704. **[MCPSharp](https://github.com/afrise/MCPSharp)** - ⭐ 359
   MCPSharp is a .NET library that helps you build Model Context Protocol (MCP) servers and clients - the standardized API protocol used by AI assistants and models.

705. **[prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server)** - ⭐ 359
   A Model Context Protocol (MCP) server that enables AI agents and LLMs to query and analyze Prometheus metrics through standardized interfaces.

706. **[mcp2mqtt](https://github.com/mcp2everything/mcp2mqtt)** - ⭐ 358
   本项目通过将 MCP 协议转换为 MQTT 协议，我们能够利用强大的大型语言模型（LLMs），就能轻松操控您的智能家居、机器人或其他硬件设备。

707. **[obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server)** - ⭐ 357
   Obsidian Knowledge-Management MCP (Model Context Protocol) server that enables AI agents and development tools to interact with an Obsidian vault. It provides a comprehensive suite of tools for reading, writing, searching, and managing notes, tags, and frontmatter, acting as a bridge to the Obsidian Local REST API plugin.

708. **[todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server)** - ⭐ 356
   MCP server for Todoist integration enabling natural language task management with Claude

709. **[applescript-mcp](https://github.com/joshrutkowski/applescript-mcp)** - ⭐ 356
   A macOS AppleScript MCP server

710. **[vtcode](https://github.com/vinhnx/vtcode)** - ⭐ 355
   VT Code - Semantic coding agent in the terminal

711. **[ableton-live-mcp-server](https://github.com/Simon-Kansara/ableton-live-mcp-server)** - ⭐ 354
   MCP Server implementation for Ableton Live OSC control

712. **[tfmcp](https://github.com/nwiizo/tfmcp)** - ⭐ 354
   🌍 Terraform Model Context Protocol (MCP) Tool - An experimental CLI tool that enables AI assistants to manage and operate Terraform environments. Supports reading Terraform configurations, analyzing plans, applying configurations, and managing state with Claude Desktop integration. ⚡️

713. **[mcp-graphql](https://github.com/blurrah/mcp-graphql)** - ⭐ 354
   Model Context Protocol server for GraphQL

714. **[twitter-mcp](https://github.com/EnesCinr/twitter-mcp)** - ⭐ 353
   A Model Context Protocol server allows to interact with Twitter, enabling posting tweets and searching Twitter.

715. **[f2c-mcp](https://github.com/f2c-ai/f2c-mcp)** - ⭐ 353
   F2C MCP Server

716. **[claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** - ⭐ 353
   A Model Context Protocol (MCP) that allows Claude Desktop and other AI tools (GitHub Copilot, Cursor, etc.) to interact directly with Figma

717. **[mcpr](https://github.com/conikeec/mcpr)** - ⭐ 352
   Model Context Protocol (MCP) implementation in Rust

718. **[xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server)** - ⭐ 351
   MCP Server implementation for Xcode integration

719. **[mcp-aktools](https://github.com/aahl/mcp-aktools)** - ⭐ 351
   📈 提供股票、加密货币的数据查询和分析功能MCP服务器

720. **[vestige](https://github.com/samvallad33/vestige)** - ⭐ 351
   Cognitive memory MCP server for Claude - FSRS-6, spreading activation, synaptic tagging, and 130 years of memory research

721. **[mcp-teams-server](https://github.com/InditexTech/mcp-teams-server)** - ⭐ 349
   An MCP (Model Context Protocol) server implementation for Microsoft Teams integration, providing capabilities to read messages, create messages, reply to messages, mention members.

722. **[RetroMCP-Java](https://github.com/MCPHackers/RetroMCP-Java)** - ⭐ 349
   A rewrite of MCP to provide support for many versions of Minecraft which were never supported by original MCP

723. **[mcp-apple-notes](https://github.com/RafalWilinski/mcp-apple-notes)** - ⭐ 349
   Talk with your notes in Claude. RAG over your Apple Notes using Model Context Protocol.

724. **[Android-MCP](https://github.com/CursorTouch/Android-MCP)** - ⭐ 349
   Lightweight MCP Server for interacting with Android Operating System.

725. **[mcp-reddit](https://github.com/adhikasp/mcp-reddit)** - ⭐ 348
   A Model Context Protocol (MCP) server that provides tools for fetching and analyzing Reddit content.

726. **[skillz](https://github.com/intellectronica/skillz)** - ⭐ 348
   An MCP server for loading skills (shim for non-claude clients).

727. **[revit-mcp](https://github.com/mcp-servers-for-revit/revit-mcp)** - ⭐ 348
   AI-Powered Revit Modeling

728. **[Construction-Hazard-Detection](https://github.com/yihong1120/Construction-Hazard-Detection)** - ⭐ 347
   Enhances construction site safety using YOLO for object detection, identifying hazards like workers without helmets or safety vests, and proximity to machinery or vehicles. HDBSCAN clusters safety cone coordinates to create monitored zones. Post-processing algorithms improve detection accuracy.

729. **[revit-mcp](https://github.com/revit-mcp/revit-mcp)** - ⭐ 347
   AI-Powered Revit Modeling

730. **[run-model-context-protocol-servers-with-aws-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda)** - ⭐ 347
   Run existing Model Context Protocol (MCP) stdio-based servers in AWS Lambda functions

731. **[devopness](https://github.com/devopness/devopness)** - ⭐ 345
   DevOps Happiness: 1-click or 1-prompt MCP. Deploy apps + infra + CI/CD on your cloud. Happy humans + reliable agents. 🚀

732. **[linear-mcp-server](https://github.com/jerhadf/linear-mcp-server)** - ⭐ 344
   A server that integrates Linear's project management system with the Model Context Protocol (MCP) to allow LLMs to interact with Linear.

733. **[maverick-mcp](https://github.com/wshobson/maverick-mcp)** - ⭐ 344
   MaverickMCP - Personal Stock Analysis MCP Server

734. **[awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit)** - ⭐ 344
   The most comprehensive toolkit for Claude Code -- 135 agents, 35 curated skills (+15,000 via SkillKit), 42 commands, 120 plugins, 19 hooks, 15 rules, 7 templates, 6 MCP configs, and more.

735. **[WireMCP](https://github.com/0xKoda/WireMCP)** - ⭐ 343
   An MCP for WireShark (tshark). Empower LLM's with realtime network traffic analysis capability

736. **[mcp-gateway](https://github.com/lasso-security/mcp-gateway)** - ⭐ 343
   A plugin-based gateway that orchestrates other MCPs and allows developers to build upon it enterprise-grade agents.

737. **[AgentChat](https://github.com/Shy2593666979/AgentChat)** - ⭐ 343
   AgentChat 是一个基于 LLM 的智能体交流平台，内置默认 Agent 并支持用户自定义 Agent。通过多轮对话和任务协作，Agent 可以理解并协助完成复杂任务。项目集成 LangChain、Function Call、MCP 协议、RAG、Memory、Milvus 和 ElasticSearch 等技术，实现高效的知识检索与工具调用，使用 FastAPI 构建高性能后端服务。

738. **[droidmind](https://github.com/hyperb1iss/droidmind)** - ⭐ 341
   Control your Android devices with AI using Model Context Protocol

739. **[a2a-directory](https://github.com/sing1ee/a2a-directory)** - ⭐ 340
   Agent2Agent (A2A) – AgentCards, Servers, Clients, Docs

740. **[agent-skills](https://github.com/microsoft/agent-skills)** - ⭐ 340
   Skills, MCP servers, Custom Coding Agents, Agents.md for SDKs to ground Coding Agents

741. **[daan](https://github.com/pluveto/daan)** - ⭐ 339
   ✨Lightweight LLM Client with MCP 🔌 & Characters 👤

742. **[base-mcp](https://github.com/base/base-mcp)** - ⭐ 339
   A Model Context Protocol (MCP) server that provides onchain tools for LLMs, allowing them to interact with the Base network and Coinbase API.

743. **[devtools-debugger-mcp](https://github.com/ScriptedAlchemy/devtools-debugger-mcp)** - ⭐ 339
   An MCP server exposing full Chrome DevTools Protocol debugging: breakpoints, step/run, call stacks, eval, and source maps.

744. **[mcp-calculator](https://github.com/78/mcp-calculator)** - ⭐ 339
   Xiaozhi MCP sample program

745. **[db-mcp-server](https://github.com/FreePeak/db-mcp-server)** - ⭐ 339
   A powerful multi-database server implementing the Model Context Protocol (MCP) to provide AI assistants with structured access to databases.

746. **[awesome-cursor-mpc-server](https://github.com/kleneway/awesome-cursor-mpc-server)** - ⭐ 338
   Example of an MCP server with custom tools that can be called directly from cursor

747. **[mcp-selenium](https://github.com/angiejones/mcp-selenium)** - ⭐ 338
   An MCP implementation for Selenium WebDriver

748. **[hermes-mcp](https://github.com/cloudwalk/hermes-mcp)** - ⭐ 338
   Elixir Model Context Protocol (MCP) SDK

749. **[WebMCP](https://github.com/jasonjmcghee/WebMCP)** - ⭐ 337
   Early WebMCP proposal / implementation - since evolved and worked on by much more capable folks that develop the web: https://github.com/webmachinelearning/webmcp

750. **[claude-code-mastery](https://github.com/TheDecipherist/claude-code-mastery)** - ⭐ 337
   The complete guide to Claude Code: CLAUDE.md, hooks, skills, MCP servers, and commands

751. **[mcp-for-next.js](https://github.com/vercel-labs/mcp-for-next.js)** - ⭐ 336

752. **[BloodHound-MCP-AI](https://github.com/MorDavid/BloodHound-MCP-AI)** - ⭐ 335
   BloodHound-MCP-AI is integration that connects BloodHound with AI through Model Context Protocol, allowing security professionals to analyze Active Directory attack paths using natural language instead of complex Cypher queries.

753. **[interactive-mcp](https://github.com/ttommyth/interactive-mcp)** - ⭐ 334
   Vibe coding should have human in the loop! interactive-mcp: Local, cross-platform MCP server for interact with your AI Agent

754. **[paws-on-mcp](https://github.com/hemanth/paws-on-mcp)** - ⭐ 332
   A comprehensive Model Context Protocol (MCP) server implementing the latest specification.

755. **[CodeGraphContext](https://github.com/Shashankss1205/CodeGraphContext)** - ⭐ 331
   An MCP server plus a CLI tool that indexes local code into a graph database to provide context to AI assistants.

756. **[open-mcp](https://github.com/wegotdocs/open-mcp)** - ⭐ 331

757. **[mcsmcp](https://github.com/microsoft/mcsmcp)** - ⭐ 330
   Lab for creating an MCP Server and using it in Microsoft Copilot Studio.

758. **[MemoryMesh](https://github.com/CheMiguel23/MemoryMesh)** - ⭐ 330
   A knowledge graph server that uses the Model Context Protocol (MCP) to provide structured memory persistence for AI models.

759. **[laravel-mcp-server](https://github.com/opgginc/laravel-mcp-server)** - ⭐ 329
   A Laravel package for implementing secure Model Context Protocol servers using Streamable HTTP and SSE transport, providing real-time communication and a scalable tool system for enterprise environments.

760. **[vscode-mcp-server](https://github.com/juehang/vscode-mcp-server)** - ⭐ 329
   MCP server to expose VS Code editing features to an LLM for AI coding

761. **[agentcontrolplane](https://github.com/humanlayer/agentcontrolplane)** - ⭐ 329
   ACP is the Agent Control Plane - a distributed agent scheduler optimized for simplicity, clarity, and control. It is designed for outer-loop agents that run without supervision, and make asynchronous tool calls like requesting human feedback on key operations. Full MCP support.

762. **[Ace-Mcp-Node](https://github.com/yeuxuan/Ace-Mcp-Node)** - ⭐ 328
   Acemcp 是一个高性能的 MCP (Model Context Protocol) 服务器，专为 AI 助手（如 Claude、GPT 等）提供代码库索引和语义搜索能力。通过 Acemcp，AI 助手可以：  🔍 快速搜索和理解大型代码库 📊 获取带行号的精确代码片段 🤖 自动增量更新索引 🌐 通过 Web 界面管理和调试

763. **[ast-grep-mcp](https://github.com/ast-grep/ast-grep-mcp)** - ⭐ 328

764. **[claude-code-statusline](https://github.com/rz1989s/claude-code-statusline)** - ⭐ 328
   Transform your Claude Code terminal with atomic precision statusline. Features flexible layouts, real-time cost tracking, MCP monitoring, prayer times, and beautiful themes.

765. **[zotero-mcp](https://github.com/cookjohn/zotero-mcp)** - ⭐ 328
   Zotero MCP Plugin 是一个 Zotero 插件，通过 MCP协议实现 AI 助手与 Zotero深度集成。插件支持文献检索、元   数据管理、全文分析和智能问答等功能，让 Claude、ChatGPT 等 AI 工具能够直接访问和操作您的文献库。 Zotero MCP Plugin enables integration between AI assistants and Zotero through MCP. 

766. **[css-mcp](https://github.com/stolinski/css-mcp)** - ⭐ 327

767. **[mesh](https://github.com/decocms/mesh)** - ⭐ 327
   One secure endpoint for every MCP server. Deploy anywhere.

768. **[moling](https://github.com/gojue/moling)** - ⭐ 325
   MoLing is a computer-use and browser-use based MCP server. It is a locally deployed, dependency-free office AI assistant.

769. **[mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops)** - ⭐ 325
   An MCP server for Azure DevOps

770. **[mcp](https://github.com/IBM/mcp)** - ⭐ 324
   A collection of Model Context Protocol (MCP) servers, clients and developer tools by IBM.

771. **[stealth-browser-mcp](https://github.com/vibheksoni/stealth-browser-mcp)** - ⭐ 324
   The only browser automation that bypasses anti-bot systems. AI writes network hooks, clones UIs pixel-perfect via simple chat.

772. **[redd-archiver](https://github.com/19-84/redd-archiver)** - ⭐ 323
   A PostgreSQL-backed archive generator that creates browsable HTML archives from link aggregator platforms including Reddit, Voat, and Ruqqus.

773. **[Rube](https://github.com/ComposioHQ/Rube)** - ⭐ 322
   Rube is a Model Context Protocol (MCP) server that connects your AI tools to 500+ apps like Gmail, Slack, GitHub, and Notion. Simply install it in your AI client, authenticate once with your apps, and start asking your AI to perform real actions like "Send an email" or "Create a task."

774. **[abcoder](https://github.com/cloudwego/abcoder)** - ⭐ 322
   deep, reliable and confidential coding-context

775. **[Context-Engine](https://github.com/Context-Engine-AI/Context-Engine)** - ⭐ 322
   Context-Engine MCP - Agentic Context Compression Suite

776. **[ClimateTraceKMP](https://github.com/joreilly/ClimateTraceKMP)** - ⭐ 321
   Kotlin/Compose Multiplatform project to show climate related emission data from https://climatetrace.org/data.

777. **[Minecraft-Hack-BaseClient](https://github.com/OxideWaveLength/Minecraft-Hack-BaseClient)** - ⭐ 319
   This is a Minecraft Base Client

778. **[one-mcp](https://github.com/burugo/one-mcp)** - ⭐ 319
   A centralized proxy platform for MCP servers, accessible via a single HTTP server,featuring a web-based management interface. 

779. **[gptr-mcp](https://github.com/assafelovic/gptr-mcp)** - ⭐ 319
   MCP server for enabling LLM applications to perform deep research via the MCP protocol

780. **[langconnect-client](https://github.com/teddynote-lab/langconnect-client)** - ⭐ 318
   A Modern GUI Interface for Vector Database Management(Supports MCP integration)

781. **[anything-to-notebooklm](https://github.com/joeseesun/anything-to-notebooklm)** - ⭐ 318
   Claude Skill: Multi-source content processor for NotebookLM. Supports WeChat articles, web pages, YouTube, PDF, Markdown, search queries → Podcast/PPT/MindMap/Quiz etc.

782. **[mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd)** - ⭐ 317
   An implementation of Model Context Protocol (MCP) server for Argo CD.

783. **[aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol](https://github.com/microsoft/aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol)** - ⭐ 317

784. **[tinystruct](https://github.com/tinystruct/tinystruct)** - ⭐ 314
   A lightweight, modular Java application framework for web and CLI development,         designed for AI integration and plugin-based architecture.         Enabling developers to create robust solutions with ease for building efficient and scalable applications.

785. **[vllm-mlx](https://github.com/waybarrios/vllm-mlx)** - ⭐ 314
   OpenAI-compatible server for Apple Silicon. Run LLMs and vision-language models (Llama, Qwen-VL, LLaVA) with continuous batching, MCP tool calling, and multimodal support. Native MLX backend, 400+ tok/s.

786. **[emcee](https://github.com/mattt/emcee)** - ⭐ 313
   MCP generator for OpenAPIs 🫳🎤💥

787. **[autogenstudio-skills](https://github.com/madtank/autogenstudio-skills)** - ⭐ 313
   Repo of skills for autogen studio using model context protocol (mcp)

788. **[mcp-servers-hub](https://github.com/apappascs/mcp-servers-hub)** - ⭐ 312
   Discover the most comprehensive and up-to-date collection of MCP servers in the market. This repository serves as a centralized hub, offering an extensive catalog of open-source and proprietary MCP servers, complete with features, documentation links, and contributors.

789. **[x64DbgMCPServer](https://github.com/AgentSmithers/x64DbgMCPServer)** - ⭐ 311
   x64DbgMCPServer made from c# with Claude, Windsurf and Cursor support

790. **[code-sandbox-mcp](https://github.com/Automata-Labs-team/code-sandbox-mcp)** - ⭐ 310
   An MCP server to create secure code sandbox environment for executing code within Docker containers. This MCP server provides AI applications with a safe and isolated environment for running code while maintaining security through containerization.

791. **[mcp-server](https://github.com/mapbox/mcp-server)** - ⭐ 309
   Mapbox Model Context Protocol (MCP) server

792. **[ebook-mcp](https://github.com/onebirdrocks/ebook-mcp)** - ⭐ 309
   A MCP server that supports mainstream eBook formats including EPUB, PDF and more. Simplify your eBook user experience with LLM.

793. **[deep-research-mcp](https://github.com/Ozamatash/deep-research-mcp)** - ⭐ 309

794. **[investor-agent](https://github.com/ferdousbhai/investor-agent)** - ⭐ 307
   A Model Context Protocol server for building an investor agent

795. **[claude-skills-mcp](https://github.com/K-Dense-AI/claude-skills-mcp)** - ⭐ 307
   MCP server for searching and retrieving Claude Agent Skills using vector search

796. **[mcp-server-code-execution-mode](https://github.com/elusznik/mcp-server-code-execution-mode)** - ⭐ 306
   An MCP server that executes Python code in isolated rootless containers with optional MCP server proxying. Implementation of Anthropic's and Cloudflare's ideas for reducing MCP tool definitions context bloat.

797. **[mssql_mcp_server](https://github.com/RichardHan/mssql_mcp_server)** - ⭐ 306
   A Model Context Protocol (MCP) server for Microsoft SQL Server that enables secure database interactions through a controlled interface. Allows AI assistants to safely list tables, read data, and execute SQL queries while maintaining security and structure.

798. **[mcprouter](https://github.com/chatmcp/mcprouter)** - ⭐ 304
   api router for MCP Servers

799. **[mcp-sse](https://github.com/sidharthrajaram/mcp-sse)** - ⭐ 304
   A working pattern for SSE-based MCP clients and servers

800. **[openmcp](https://github.com/getdatanaut/openmcp)** - ⭐ 303
   Turn any openapi file into an mcp server, with just the tools you need.

801. **[KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server)** - ⭐ 303
   KiCAD MCP is a Model Context Protocol (MCP) implementation that enables Large Language Models (LLMs) like Claude to directly interact with KiCAD for printed circuit board design.

802. **[automcp](https://github.com/NapthaAI/automcp)** - ⭐ 302
   Easily convert tool, agents and orchestrators from existing agent frameworks to MCP servers

803. **[sdk](https://github.com/smithery-ai/sdk)** - ⭐ 302
   Smithery helps AI agents access external services via a unified gateway.

804. **[mcp-database-server](https://github.com/executeautomation/mcp-database-server)** - ⭐ 302
   MCP Database Server is a new MCP Server which helps connect with Sqlite, SqlServer and Posgresql Databases

805. **[skillport](https://github.com/gotalab/skillport)** - ⭐ 302
   Bring Agent Skills to Any AI Agent and Coding Agent — via CLI or MCP. Manage once, serve anywhere.

806. **[deepseek-mcp-server](https://github.com/DMontgomery40/deepseek-mcp-server)** - ⭐ 300
   Model Context Protocol server for DeepSeek's advanced language models

807. **[MaaMCP](https://github.com/MAA-AI/MaaMCP)** - ⭐ 300
   基于 MaaFramework 的 MCP 服务器 为 AI 助手提供 Android 设备和 Windows 桌面自动化能力

808. **[mq](https://github.com/harehare/mq)** - ⭐ 299
   jq-like command-line tool for markdown processing

809. **[solon-ai](https://github.com/opensolon/solon-ai)** - ⭐ 298
   Java AI application development framework (supports LLM-tool,skill; RAG; MCP; Agent-ReAct,Team-Agent). Compatible with java8 ~ java25. It can also be embedded in SpringBoot, jFinal, Vert.x, Quarkus, and other frameworks.

810. **[mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code)** - ⭐ 297
   MCP implementation of Claude Code capabilities and more

811. **[mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest)** - ⭐ 297
   A Model Context Protocol (MCP) server that helps read GitHub repository structure and important files.

812. **[mcp-youtube-transcript](https://github.com/jkawamoto/mcp-youtube-transcript)** - ⭐ 297
   MCP server retrieving transcripts of YouTube videos

813. **[mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search)** - ⭐ 297

814. **[AI-Kline](https://github.com/QuantML-C/AI-Kline)** - ⭐ 297
   Python-based stock analysis tool that combines traditional technical analysis with AI prediction capabilities.  Providing comprehensive stock analysis and forecasting using K-line charts, technical indicators, financial data, and news data. With CMD/WEB/MCP supported.

815. **[Lynkr](https://github.com/Fast-Editor/Lynkr)** - ⭐ 297
   Streamline your workflow with Lynkr, a CLI tool that acts as an HTTP proxy for efficient code interactions using Claude Code CLI.

816. **[todoist-ai](https://github.com/Doist/todoist-ai)** - ⭐ 297
   A set of tools to connect to AI agents, to allow them to use Todoist on a user's behalf. Includes MCP support.

817. **[mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts)** - ⭐ 296

818. **[generator](https://github.com/context-hub/generator)** - ⭐ 296
   CTX: a tool that solves the context management gap when working with LLMs like ChatGPT or Claude. It helps developers organize and automatically collect information from their codebase into structured documents that can be easily shared with AI assistants.

819. **[DeepWideResearch](https://github.com/puppyone-ai/DeepWideResearch)** - ⭐ 295
   Agentic RAG for any scenario. Customize sources, depth, and width

820. **[rhinomcp](https://github.com/jingcheng-chen/rhinomcp)** - ⭐ 293
   RhinoMCP connects Rhino 3D to AI Agent through the Model Context Protocol (MCP)

821. **[atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server)** - ⭐ 293
   Remote MCP Server that securely connects Jira and Confluence with your LLM, IDE, or agent platform of choice.

822. **[CAAL](https://github.com/CoreWorxLab/CAAL)** - ⭐ 293
   Local voice assistant that learns new abilities via auto-discovered n8n workflows exposed as tools via MCP

823. **[mysql_mcp_server_pro](https://github.com/wenb1n-dev/mysql_mcp_server_pro)** - ⭐ 292
   Model Context Protocol (MCP) server that supports secure interaction with MySQL databases and has anomaly analysis capabilities.更加牛逼！更加好用！不仅止于mysql的增删改查功能； 还包含了数据库异常分析能力；且便于开发者们进行个性化的工具扩展 

824. **[aider-mcp-server](https://github.com/disler/aider-mcp-server)** - ⭐ 292
   Minimal MCP Server for Aider

825. **[llm-context.py](https://github.com/cyberchitta/llm-context.py)** - ⭐ 291
   Share code with LLMs via Model Context Protocol or clipboard. Rule-based customization enables easy switching between different tasks (like code review and documentation). Includes smart code outlining.

826. **[mcp-server-simulator-ios-idb](https://github.com/InditexTech/mcp-server-simulator-ios-idb)** - ⭐ 291
   A Model Context Protocol (MCP) server that enables LLMs to interact with iOS simulators through natural language commands.

827. **[kagimcp](https://github.com/kagisearch/kagimcp)** - ⭐ 291
   The Official Model Context Protocol (MCP) server for Kagi search & other tools.

828. **[aws-mcp](https://github.com/RafalWilinski/aws-mcp)** - ⭐ 290
   Talk with your AWS using Claude. Model Context Protocol (MCP) server for AWS. Better Amazon Q alternative.

829. **[google-docs-mcp](https://github.com/a-bonus/google-docs-mcp)** - ⭐ 290
   The Ultimate Google Docs, Sheets & Drive MCP Server. Google Docs MCP is an MCP server (primarily for use in Claude Desktop) that gains full access to your google docs, etc. and allows claude to make direct edits and formatting.

830. **[blender-mcp-vxai](https://github.com/VxASI/blender-mcp-vxai)** - ⭐ 289

831. **[apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server)** - ⭐ 289
   A MCP Server for APK Tool (Part of Android Reverse Engineering MCP Suites)

832. **[mcp-server-mas-sequential-thinking](https://github.com/FradSer/mcp-server-mas-sequential-thinking)** - ⭐ 289
   An advanced sequential thinking process using a Multi-Agent System (MAS) built with the Agno framework and served via MCP.

833. **[consult7](https://github.com/szeider/consult7)** - ⭐ 288
   MCP server to consult a language model with large context size

834. **[obsidian-mcp](https://github.com/newtype-01/obsidian-mcp)** - ⭐ 287
   Obsidian MCP (Model Context Protocol) Server

835. **[o3-search-mcp](https://github.com/yoshiko-pg/o3-search-mcp)** - ⭐ 287
   MCP server for OpenAI o3 web search

836. **[utcp-specification](https://github.com/universal-tool-calling-protocol/utcp-specification)** - ⭐ 287
   The specification for the Universal Tool Calling Protocol

837. **[mcp-linker](https://github.com/milisp/mcp-linker)** - ⭐ 287
   mcp store manager, add & syncs MCP server configurations across clients like Claude code, Cursor💡 build-in Codex agent use ChatGPT subscription, mcphub

838. **[mcp-cli](https://github.com/apify/mcp-cli)** - ⭐ 287
   mcpc is a CLI client for MCP. It supports persistent sessions, stdio/HTTP, OAuth 2.1, JSON output for code mode, proxy for AI sandboxes, and much more.

839. **[anytype-mcp](https://github.com/anyproto/anytype-mcp)** - ⭐ 287
   An MCP server enabling AI assistants to interact with Anytype - your encrypted, local and collaborative wiki - to organize objects, lists, and more through natural language.

840. **[mcpsvr](https://github.com/nanbingxyz/mcpsvr)** - ⭐ 286
   Discover Exceptional MCP Servers

841. **[mcp-neovim-server](https://github.com/bigcodegen/mcp-neovim-server)** - ⭐ 285
   Control Neovim using Model Context Protocol (MCP) and the official neovim/node-client JavaScript library

842. **[remote-mcp-server-with-auth](https://github.com/coleam00/remote-mcp-server-with-auth)** - ⭐ 285
   Template for a remote MCP server with GitHub OAuth - following best practices for building MCP servers so you can take this as a starting point for any MCP server you want to build!

843. **[safe-mcp](https://github.com/SAFE-MCP/safe-mcp)** - ⭐ 285
   SAFE-MCP is a comprehensive security framework for documenting and mitigating threats in the AI Agent ecosystem.

844. **[lets-learn-mcp-csharp](https://github.com/microsoft/lets-learn-mcp-csharp)** - ⭐ 284

845. **[meGPT](https://github.com/adrianco/meGPT)** - ⭐ 284
   Code to process many kinds of content by an author into an MCP server

846. **[jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server)** - ⭐ 284
   MCP server for JADX-AI Plugin

847. **[things-mcp](https://github.com/hald/things-mcp)** - ⭐ 284
   Things.app MCP Server

848. **[hydra-mcp-solana](https://github.com/hydra-mcp/hydra-mcp-solana)** - ⭐ 283
   hydra-ai

849. **[minthcm](https://github.com/minthcm/minthcm)** - ⭐ 283
   First AI‑enabled open-source Human Capital Management system that you can start using today.

850. **[perplexity-mcp](https://github.com/DaInfernalCoder/perplexity-mcp)** - ⭐ 283
   A Model Context Protocol (MCP) server for research and documentation assistance using Perplexity AI. Won 1st @ Cline Hackathon

851. **[app-store-connect-mcp-server](https://github.com/JoshuaRileyDev/app-store-connect-mcp-server)** - ⭐ 283

852. **[mcp](https://github.com/oracle/mcp)** - ⭐ 282
   Repository containing MCP (Model Context Protocol) servers that provides a suite of tools for managing and interacting with Oracle products.

853. **[mcp-documentation-server](https://github.com/andrea9293/mcp-documentation-server)** - ⭐ 282
   MCP Documentation Server - Bridge the AI Knowledge Gap.  ✨ Features: Document management • Gemini integration • AI-powered semantic search • File uploads • Smart chunking • Multilingual support • Zero-setup  🎯 Perfect for: New frameworks • API docs • Internal guides 

854. **[imagesorcery-mcp](https://github.com/sunriseapps/imagesorcery-mcp)** - ⭐ 282
   An MCP server providing tools for image processing operations

855. **[DeepWideResearch](https://github.com/PuppyAgent/DeepWideResearch)** - ⭐ 281
   Agentic RAG for any scenario. Customize sources, depth, and width

856. **[perplexity-mcp](https://github.com/jsonallen/perplexity-mcp)** - ⭐ 281
   A Model Context Protocol (MCP) server that provides web search functionality using Perplexity AI's API.

857. **[ddddocr](https://github.com/86maid/ddddocr)** - ⭐ 281
   ddddocr rust 版本，ocr_api_server rust 版本，二进制版本，验证码识别，不依赖 opencv 库，跨平台运行，AI MCP 支持，a simple OCR API server, very easy to deploy。

858. **[mcp-manager](https://github.com/zueai/mcp-manager)** - ⭐ 280
   simple web ui to manage mcp (model context protocol) servers in the claude app

859. **[MCPControl](https://github.com/claude-did-this/MCPControl)** - ⭐ 280
   MCP server for Windows OS automation

860. **[mcp-manager](https://github.com/amxv/mcp-manager)** - ⭐ 280
   simple web ui to manage mcp (model context protocol) servers in the claude app

861. **[chrome-devtools-mcp](https://github.com/benjaminr/chrome-devtools-mcp)** - ⭐ 279
   An MCP Server for Chrome DevTools, following the Chrome DevTools Protocol. Integrates with Claude Desktop and Claude Code.

862. **[mcp940](https://github.com/WangTingZheng/mcp940)** - ⭐ 279
   Source code of minecraft 1.12

863. **[geminimcp](https://github.com/GuDaStudio/geminimcp)** - ⭐ 279
   Gemini-MCP is an MCP server that encapsulates Google's Gemini CLI tool into a standard MCP protocol interface, enabling Claude Code to invoke Gemini for AI-assisted programming tasks.

864. **[telegram-mcp](https://github.com/chaindead/telegram-mcp)** - ⭐ 279
   Telegram MCP for managing dialogs, messages, drafts, read statuses, and more.

865. **[MCP-handle](https://github.com/WeatherPal-AI/MCP-handle)** - ⭐ 278
   MCP integration platforms making AI-Agents developers focusing on their own tasks

866. **[FileScopeMCP](https://github.com/admica/FileScopeMCP)** - ⭐ 278
   Analyzes your codebase identifying important files based on dependency relationships. Generates diagrams and importance scores per file, helping AI assistants understand the codebase. Automatically parses popular programming languages such as Python, C, C++, Rust, Zig, Lua.

867. **[laravel-claude-code-setup](https://github.com/laraben/laravel-claude-code-setup)** - ⭐ 277
   One-command setup for AI-powered Laravel development with Claude Code and MCP servers

868. **[nova-proximity](https://github.com/Nova-Hunting/nova-proximity)** - ⭐ 277
   Nova-Proximity is a MCP and Agent Skills security scanner powered with NOVA

869. **[mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server)** - ⭐ 277
   A Model Context Protocol Server for MongoDB

870. **[Context-Engine](https://github.com/m1rl0k/Context-Engine)** - ⭐ 276
   Context-Engine MCP - Agentic Context Compression Suite

871. **[MCP-Server-Playwright](https://github.com/VikashLoomba/MCP-Server-Playwright)** - ⭐ 276
   MCP server for browser automation using Playwright

872. **[dify-mcp-server](https://github.com/YanxingLiu/dify-mcp-server)** - ⭐ 275
   Model Context Protocol (MCP) Server for dify workflows

873. **[mcp-reasoner](https://github.com/Jacck/mcp-reasoner)** - ⭐ 275
   A systematic reasoning MCP server implementation for Claude Desktop with beam search and thought evaluation.

874. **[metorial-index](https://github.com/metorial/metorial-index)** - ⭐ 275
   Metorial MCP Index - An ever growing list of open source MCP servers 📁 🎉

875. **[hass-mcp](https://github.com/voska/hass-mcp)** - ⭐ 272
   Home Assistant MCP Server

876. **[mcp-server-12306](https://github.com/drfccv/mcp-server-12306)** - ⭐ 272
   12306 MCP Server​​ 是一个基于 ​​Model Context Protocol (MCP)​​ 的高性能火车票查询后端系统。它通过标准化接口提供官方 12306 的实时数据服务，包括余票查询、车站信息、列车经停站、中转换乘方案等核心功能。

877. **[proximity](https://github.com/Nova-Hunting/proximity)** - ⭐ 271
   Proximity is a MCP security scanner powered with NOVA

878. **[next-lens](https://github.com/1weiho/next-lens)** - ⭐ 270
   A CLI that scans Next.js routes and provides quick insights from your terminal, web UI, and MCP.

879. **[jinni](https://github.com/smat-dev/jinni)** - ⭐ 269
   Bring your project into LLM context - tool and MCP server

880. **[proximity](https://github.com/fr0gger/proximity)** - ⭐ 269
   Proximity is a MCP security scanner powered with NOVA

881. **[claude-modular](https://github.com/oxygen-fragment/claude-modular)** - ⭐ 269
   Production-ready modular Claude Code framework with 30+ commands, token optimization, and MCP server integration. Achieves 2-10x productivity gains through   systematic command organization and hierarchical configuration.

882. **[AetherLink](https://github.com/1600822305/AetherLink)** - ⭐ 269
   AetherLink is a cross-platform AI assistant application that supports multiple mainstream AI models (OpenAI, Google Gemini, Anthropic Claude, Grok, etc.). Built with React, TypeScript, and Capacitor, it delivers a seamless conversational experience. Key features include customizable model configurations, multi-topic chat management, AI reasoning vi

883. **[ssh-mcp](https://github.com/tufantunc/ssh-mcp)** - ⭐ 269
   MCP server exposing SSH control for Linux servers via Model Context Protocol.

884. **[mcp](https://github.com/salesforcecli/mcp)** - ⭐ 269
   MCP Server for interacting with Salesforce instances

885. **[studio-rust-mcp-server](https://github.com/Roblox/studio-rust-mcp-server)** - ⭐ 269
   Standalone Roblox Studio MCP Server

886. **[ultra-mcp](https://github.com/RealMikeChong/ultra-mcp)** - ⭐ 267
   100x Your Claude Code, Gemini CLI, Cursor and/or any coding tools with MCP client support

887. **[mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)** - ⭐ 267
   🔍 A Model Context Protocol (MCP) server providing unified access to multiple search engines (Tavily, Brave, Kagi), AI tools (Perplexity, FastGPT), and content processing services (Jina AI, Kagi). Combines search, AI responses, content processing, and enhancement features through a single interface.

888. **[model-context-protocol-resources](https://github.com/cyanheads/model-context-protocol-resources)** - ⭐ 266
   Exploring the Model Context Protocol (MCP) through practical guides, clients, and servers I've built while learning about this new protocol.

889. **[mcp-odoo](https://github.com/tuanle96/mcp-odoo)** - ⭐ 266
   MCP Server for Odoo

890. **[lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp)** - ⭐ 266
   Lean Theorem Prover MCP

891. **[iam-policy-autopilot](https://github.com/awslabs/iam-policy-autopilot)** - ⭐ 264
   IAM Policy Autopilot is an open source static code analysis tool that helps you quickly create baseline AWS IAM policies that you can refine as your application evolves. This tool is available as a command-line utility and MCP server for use within AI coding assistants for quickly building IAM policies.

892. **[ai-agent-team](https://github.com/peterfei/ai-agent-team)** - ⭐ 264
   AI Agent Team-拥有24/7专业AI开发团队：产品经理、前端开发、后端开发、测试工程师、DevOps工程师、技术负责人。一键安装，支持中英文命令，大幅提升开发效率！

893. **[django-mcp-server](https://github.com/gts360/django-mcp-server)** - ⭐ 264
   Django MCP Server is a Django extensions to easily enable AI Agents to interact with Django Apps through the Model Context Protocol it works equally well on WSGI and ASGI

894. **[reddit-mcp](https://github.com/Arindam200/reddit-mcp)** - ⭐ 262
   Model Context Protocol server implementation for Reddit

895. **[mcp-gdrive](https://github.com/isaacphi/mcp-gdrive)** - ⭐ 262
   Model Context Protocol (MCP) Server for reading from Google Drive and editing Google Sheets

896. **[Unreal_mcp](https://github.com/ChiR24/Unreal_mcp)** - ⭐ 261
   A comprehensive Model Context Protocol (MCP) server that enables AI assistants to control Unreal Engine through the native C++ Automation Bridge plugin. Built with TypeScript, C++, and Rust (WebAssembly) for ultra-high-performance game development automation.

897. **[deepcontext-mcp](https://github.com/Wildcard-Official/deepcontext-mcp)** - ⭐ 260
   DeepContext is an MCP server that adds symbol-aware semantic search to Claude Code, Codex CLI, and other agents for faster, smarter context on large codebases.

898. **[osp_marketing_tools](https://github.com/open-strategy-partners/osp_marketing_tools)** - ⭐ 259
   A Model Context Protocol (MCP) server that empowers LLMs to use some of Open Srategy Partners' core writing and product marketing techniques.

899. **[apollo-mcp-server](https://github.com/apollographql/apollo-mcp-server)** - ⭐ 259
   Apollo MCP Server

900. **[private-journal-mcp](https://github.com/obra/private-journal-mcp)** - ⭐ 259
   A lightweight MCP server that provides Claude with a private journaling capability to process feelings and thoughts

901. **[cheatengine-mcp-bridge](https://github.com/miscusi-peek/cheatengine-mcp-bridge)** - ⭐ 259
   Connect Cursor, Copilot & Claude directly to Cheat Engine via MCP. Automate reverse engineering, pointer scanning, and memory analysis using natural language.

902. **[mcp-ical](https://github.com/Omar-V2/mcp-ical)** - ⭐ 258
   A Model Context Protocol Server that allows you to interact with your MacOS Calendar through natural language.

903. **[mcp-server](https://github.com/strands-agents/mcp-server)** - ⭐ 256
   This MCP server provides documentation about Strands Agents to your GenAI tools, so you can use your favorite AI coding assistant to vibe-code Strands Agents.

904. **[project-nova](https://github.com/dujonwalker/project-nova)** - ⭐ 255
   A multi-agent AI architecture that connects 25+ specialized agents through n8n and MCP servers. Project NOVA routes requests to domain-specific experts, enabling control of applications from knowledge bases to DAWs, home automation to development tools. Includes system prompts, Dockerfiles, and workflows for a complete AI assistant ecosystem.

905. **[xiaozhi-client](https://github.com/shenjingnan/xiaozhi-client)** - ⭐ 255
   小智AI客户端，目前主要用于MCP的对接

906. **[mcp-server-tree-sitter](https://github.com/wrale/mcp-server-tree-sitter)** - ⭐ 254
   MCP Server for Tree-sitter

907. **[doris-mcp-server](https://github.com/apache/doris-mcp-server)** - ⭐ 254
   Apache Doris MCP Server

908. **[api200](https://github.com/API-200/api200)** - ⭐ 254
   API 200 is an open source API gateway to simplify 3rd-party integrations. Import endpoints, set up caching, retries, and mocks. Access all services via one URL. Monitor logs, track errors, and get alerts on API incidents.

909. **[figma-console-mcp](https://github.com/southleft/figma-console-mcp)** - ⭐ 254
   Your design system as an API. Connect AI to Figma for extraction, creation, and debugging.

910. **[admin](https://github.com/decocms/admin)** - ⭐ 253
   Define and compose secure MCPs in TypeScript. Generate AI workflows and agents with React + Tailwind UI. Deploy anywhere.

911. **[enterprise-mcp-course](https://github.com/decodingai-magazine/enterprise-mcp-course)** - ⭐ 253
   Learn to build from scratch an AI PR reviewer integrated with GitHub, Slack and Asana that scales within your organization.

912. **[1c_mcp](https://github.com/vladimir-kharin/1c_mcp)** - ⭐ 252
   Инструмент для создания MCP-серверов в 1С:Предприятие путем разработки расширения конфигурации. Позволяет интегрировать данные и функциональность 1С с AI-ассистентами (Claude, Cursor и т.д.). Включает Python-прокси и пример расширения 1С с готовыми инструментами.

913. **[aci-mcp](https://github.com/aipotheosis-labs/aci-mcp)** - ⭐ 251
   MCP server(s) for Aipolabs ACI.dev

914. **[code-reasoning](https://github.com/mettamatt/code-reasoning)** - ⭐ 251
   A code reasoning MCP server, a fork of sequential-thinking

915. **[rust-docs-mcp-server](https://github.com/Govcraft/rust-docs-mcp-server)** - ⭐ 251
   🦀 Prevents outdated Rust code suggestions from AI assistants. This MCP server fetches current crate docs, uses embeddings/LLMs, and provides accurate context via a tool call.

916. **[mcp_massive](https://github.com/massive-com/mcp_massive)** - ⭐ 250
   An MCP server for Massive.com Financial Market Data

917. **[g-search-mcp](https://github.com/jae-jae/g-search-mcp)** - ⭐ 250
   A powerful MCP server for Google search that enables parallel searching with multiple keywords simultaneously.

918. **[AEnvironment](https://github.com/inclusionAI/AEnvironment)** - ⭐ 250
   Standardized environment infrastructure for Agentic AI development.

919. **[spring-ai-summary](https://github.com/java-ai-tech/spring-ai-summary)** - ⭐ 250
   SpringAI，LLM，MCP，Embedding

920. **[bazi-mcp](https://github.com/cantian-ai/bazi-mcp)** - ⭐ 249
   MCP server for Bazi (八字) information

921. **[MARM-Systems](https://github.com/Lyellr88/MARM-Systems)** - ⭐ 248
   Turn AI into a persistent, memory-powered collaborator. Universal MCP Server (supports HTTP, STDIO, and WebSocket) enabling cross-platform AI memory, multi-agent coordination, and context sharing. Built with MARM protocol for structured reasoning that evolves with your work.

922. **[claude-recall](https://github.com/nhevers/claude-recall)** - ⭐ 247
   Long-term memory layer for MoltBot & Claude Code that learns and recalls your project context automatically

923. **[suppr-mcp](https://github.com/WildDataX/suppr-mcp)** - ⭐ 247
    超能文献|AI驱动的文档翻译与学术搜索服务。支持PDF、DOCX、PPTX等多格式文档的高质量翻译（支持11种语言），特别优化了数学公式翻译。同时提供PubMed学术文献智能搜索功能。更多访问：https://suppr.wilddata.cn

924. **[Windows-MCP.Net](https://github.com/shuyu-labs/Windows-MCP.Net)** - ⭐ 247
   A .NET-based Windows desktop automation MCP (Model Context Protocol) server that provides AI assistants with the ability to interact with the Windows desktop environment.

925. **[wexin-read-mcp](https://github.com/Bwkyd/wexin-read-mcp)** - ⭐ 247
   能够让大模型阅读微信公众号文章，使用浏览器模拟绕过反爬虫。

926. **[mcp_flutter](https://github.com/Arenukvern/mcp_flutter)** - ⭐ 246
   MCP server and MCP Toolkit  for Flutter and Dart VM - supports dynamic tooling

927. **[mcp-server-gemini](https://github.com/aliargun/mcp-server-gemini)** - ⭐ 245
   MCP server implementation for Google's Gemini API

928. **[elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server)** - ⭐ 245
   A Model Context Protocol (MCP) server implementation that provides Elasticsearch and OpenSearch interaction.

929. **[video-editing-mcp](https://github.com/burningion/video-editing-mcp)** - ⭐ 245
   MCP Interface for Video Jungle

930. **[Windows-MCP.Net](https://github.com/AIDotNet/Windows-MCP.Net)** - ⭐ 244
   A .NET-based Windows desktop automation MCP (Model Context Protocol) server that provides AI assistants with the ability to interact with the Windows desktop environment.

931. **[gemini-cli-desktop](https://github.com/Piebald-AI/gemini-cli-desktop)** - ⭐ 244
   Web/desktop UI for Gemini CLI/Qwen Code.  Manage projects, switch between tools, search across past conversations, and manage MCP servers, all from one multilingual interface, locally or remotely.

932. **[chat-mcp](https://github.com/AI-QL/chat-mcp)** - ⭐ 243
   A Desktop Chat App that leverages MCP(Model Context Protocol) to interface with other LLMs.

933. **[mcp-chatbot](https://github.com/3choff/mcp-chatbot)** - ⭐ 243
   A simple CLI chatbot that demonstrates the integration of the Model Context Protocol (MCP).

934. **[browser-control-mcp](https://github.com/eyalzh/browser-control-mcp)** - ⭐ 242
   MCP server paired with a browser extension that enables AI agents to control the user's browser.

935. **[mcp-feedback-collector](https://github.com/sanshao85/mcp-feedback-collector)** - ⭐ 241
   一个现代化的 Model Context Protocol (MCP) 服务器，为AI助手提供交互式用户反馈收集功能。

936. **[human-mcp](https://github.com/mrgoonie/human-mcp)** - ⭐ 241

937. **[mcp-gsc](https://github.com/AminForou/mcp-gsc)** - ⭐ 241
   Google Search Console Insights with Claude AI for SEOs

938. **[mcp-prompt-server](https://github.com/gdli6177/mcp-prompt-server)** - ⭐ 240
   这是一个基于Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地使用。

939. **[claude-code-mcpinstall](https://github.com/undeadpickle/claude-code-mcpinstall)** - ⭐ 240
   Easy guide to installing Claude Code MCPs globally on your machine.

940. **[weather-mcp-server](https://github.com/ezh0v/weather-mcp-server)** - ⭐ 240
   A lightweight Model Context Protocol (MCP) server that enables AI assistants like Claude to retrieve and interpret real-time weather data. Discuss on Hacker News:

941. **[PIXRA](https://github.com/dodufish/PIXRA)** - ⭐ 239
   Pixelize the real world on-chain

942. **[MCPBench](https://github.com/modelscope/MCPBench)** - ⭐ 239
   The evaluation benchmark on MCP servers

943. **[mcp2py](https://github.com/MaximeRivest/mcp2py)** - ⭐ 239
   Turn any MCP server into a Python module

944. **[claude_code-gemini-mcp](https://github.com/RaiAnsar/claude_code-gemini-mcp)** - ⭐ 238
   Simplified Gemini for Claude Code. 

945. **[mcp-server-code-runner](https://github.com/formulahendry/mcp-server-code-runner)** - ⭐ 238
   Code Runner MCP Server

946. **[foundry-mcp-server](https://github.com/PraneshASP/foundry-mcp-server)** - ⭐ 238
   An experimental MCP Server for foundry built for Solidity devs

947. **[mcp-server](https://github.com/volcengine/mcp-server)** - ⭐ 238
   Volcengine MCP Servers

948. **[mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp)** - ⭐ 238
   An MCP server that securely interfaces with your iMessage database via the Model Context Protocol (MCP), allowing LLMs to query and analyze iMessage conversations. It includes robust phone number validation, attachment processing, contact management, group chat handling, and full support for sending and receiving messages.

949. **[mcp-on-vercel](https://github.com/vercel-labs/mcp-on-vercel)** - ⭐ 237

950. **[mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws)** - ⭐ 237
   AWS MCP Proxy Server

951. **[outlook-mcp](https://github.com/ryaker/outlook-mcp)** - ⭐ 237
   MCP server for Claude to access Outlook data via Microsoft Graph API

952. **[stitch](https://github.com/gemini-cli-extensions/stitch)** - ⭐ 237
   The Stitch extension for Gemini CLI enables you to interact with the Stitch MCP server using natural language commands. 

953. **[firebase-mcp](https://github.com/gannonh/firebase-mcp)** - ⭐ 236
   🔥 Model Context Protocol (MCP) server for Firebase.

954. **[strava-mcp](https://github.com/r-huijts/strava-mcp)** - ⭐ 236
   A Model Context Protocol (MCP) server that connects to Strava API, providing tools to access Strava data through LLMs

955. **[dat](https://github.com/hexinfo/dat)** - ⭐ 236
   Asking yours data in a natural language way through pre-modeling (data models and semantic models).

956. **[mcp_chatbot](https://github.com/keli-wen/mcp_chatbot)** - ⭐ 236
   A chatbot implementation compatible with MCP (terminal / streamlit supported)

957. **[CAD-MCP](https://github.com/daobataotie/CAD-MCP)** - ⭐ 236
   CAD MCP Server

958. **[NFTIAI](https://github.com/Axarb/NFTIAI)** - ⭐ 235
   NFTI AI — NFTI your AI Agents & Virtual IP. Bridging intelligent agents, MCP protocols, and RWA to create a new era of digital sovereignty.

959. **[mcp-proxy](https://github.com/punkpeye/mcp-proxy)** - ⭐ 233
   A TypeScript streamable HTTP and SSE proxy for MCP servers that use stdio transport.

960. **[ticktick-mcp](https://github.com/jacepark12/ticktick-mcp)** - ⭐ 233
   MCP server that interacts with TickTick (Dida 365) via the TickTick Open API

961. **[Lambda-MCP-Server](https://github.com/mikegc-aws/Lambda-MCP-Server)** - ⭐ 232
   Creates a simple MCP tool server with "streaming" HTTP.

962. **[awesome-mcp-servers](https://github.com/PipedreamHQ/awesome-mcp-servers)** - ⭐ 232
   A collection of MCP servers

963. **[universal-db-mcp](https://github.com/Anarkh-Lee/universal-db-mcp)** - ⭐ 232
   通用数据库 MCP 连接器：支持 MySQL、PostgreSQL、Oracle、MongoDB 等 17 种数据库，支持 Claude Desktop、Cursor、Windsurf、VS Code、ChatGPT 等 50+ 平台，用自然语言查询和分析数据

964. **[MCP-connect](https://github.com/EvalsOne/MCP-connect)** - ⭐ 231
   Enables cloud-based AI services to access local Stdio based MCP servers via HTTP requests

965. **[mcp-foundry](https://github.com/microsoft-foundry/mcp-foundry)** - ⭐ 231
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

966. **[openapi-to-mcpserver](https://github.com/higress-group/openapi-to-mcpserver)** - ⭐ 231
   A tool&lib that can automatically convert OpenAPI documents into Higress remote MCP server configurations.

967. **[Security-Detections-MCP](https://github.com/MHaggis/Security-Detections-MCP)** - ⭐ 231
   MCP to help Defenders Detection Engineer Harder and Smarter

968. **[xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server)** - ⭐ 230
   A Model Context Protocol (MCP) server that enables natural language queries to databases

969. **[octocode](https://github.com/Muvon/octocode)** - ⭐ 230
   Semantic code searcher and codebase utility with AI memory onboard

970. **[MiroRL](https://github.com/MiroMindAI/MiroRL)** - ⭐ 229
   MiroRL is  an MCP-first reinforcement learning framework for deep research agent.

971. **[mcp-telegram](https://github.com/dryeab/mcp-telegram)** - ⭐ 228
   MCP Server for Telegram

972. **[sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers)** - ⭐ 228
   Sample implementations of AI Agents and MCP Servers running on AWS Serverless compute

973. **[omnicoreagent](https://github.com/omnirexflora-labs/omnicoreagent)** - ⭐ 228
   OmniCoreAgent is a powerful Python framework for building autonomous AI agents that think, reason, and execute complex tasks. Production-ready agents that use tools, manage memory, coordinate workflows, and handle real-world business logic.

974. **[Mimir](https://github.com/orneryd/Mimir)** - ⭐ 228
   Mimir - Fully open and customizable memory bank with semantic vector search capabilities for locally indexed files (Code Intelligence) and stored memories that are shared across sessions and chat contexts allowing worker agent to learn from errors in past runs. Includes Drag and Drop multi-agent orchestration

975. **[mcp-foundry](https://github.com/azure-ai-foundry/mcp-foundry)** - ⭐ 227
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

976. **[cobolt](https://github.com/platinum-hill/cobolt)** - ⭐ 227
   This is a cross-platform desktop application that allows you to chat with locally hosted LLMs and enjoy features like MCP support

977. **[spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server)** - ⭐ 227
   Lightweight MCP server for Spotify

978. **[mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** - ⭐ 226
   A Model Context Protocol (MCP) server that provides tools for interacting with Trello boards.

979. **[remote-swe-agents](https://github.com/aws-samples/remote-swe-agents)** - ⭐ 225
   Autonomous SWE agent working in the cloud! (a.k.a. Vibe coding with Bedrock)

980. **[mcp](https://github.com/Snowflake-Labs/mcp)** - ⭐ 225
   MCP Server for Snowflake including Cortex AI, object management, SQL orchestration, semantic view consumption, and more

981. **[facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server)** - ⭐ 225

982. **[mcp-server-guide](https://github.com/figma/mcp-server-guide)** - ⭐ 225
   A guide on how to use the Figma MCP server

983. **[lyraios](https://github.com/GalaxyLLMCI/lyraios)** - ⭐ 224
   LYRAI is a Model Context Protocol (MCP) operating system for multi-AI AGENTs designed to extend the functionality of AI applications by enabling them to interact with financial networks and blockchain public chains. The server offers a range of advanced AI assistants, including blockchain public chain operations (SOLANA,ETH,BSC,etc.)

984. **[Alice](https://github.com/pmbstyle/Alice)** - ⭐ 224
   Alice is a voice-first desktop AI assistant application built with Vue.js, Vite, and Electron. Advanced memory system, function calling, MCP support, optional fully local use, and more.

985. **[mcp-maigret](https://github.com/BurtTheCoder/mcp-maigret)** - ⭐ 224
   MCP server for maigret, a powerful OSINT tool that collects user account information from various public sources. 

986. **[obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin)** - ⭐ 224
   High-performance Model Context Protocol (MCP) server for Obsidian that provides AI tools with direct vault access through semantic operations and HTTP transport.

987. **[mcp-server-commands](https://github.com/g0t4/mcp-server-commands)** - ⭐ 223
   Model Context Protocol server to run commands

988. **[mcp-compass](https://github.com/liuyoshio/mcp-compass)** - ⭐ 223
   MCP Discovery & Recommendation Service - Find the right MCP server for your needs

989. **[llamacloud-mcp](https://github.com/run-llama/llamacloud-mcp)** - ⭐ 222

990. **[langgraph-whatsapp-agent](https://github.com/lgesuellip/langgraph-whatsapp-agent)** - ⭐ 222
   A template for building WhatsApp agents using LangGraph and Twilio. This project enables you to deploy AI agents that interact with users via WhatsApp, process messages and images, and invoke custom graph-based agents. It integrates with MCP and runs on the LangGraph Platform.

991. **[effect-mcp](https://github.com/tim-smart/effect-mcp)** - ⭐ 222

992. **[c2sagent](https://github.com/C2SAgent/c2sagent)** - ⭐ 222
   C2S Agent is an lightweight AI Agent construction platform that provides configurable online Agents and MCP services, You can configure any HTTP request interface as an MCP tool. C2S Agent 是一个轻量级的AI Agent构建平台，提供在线可配置的Agent，MCP，您可以一个HTTP请求的接口配置成为一个MCP工具，Agent之间可以进行自交流。并提供了单端口多A2A服务，MCP服务的解决方案

993. **[agent-mcp-lab](https://github.com/WaveSpeedAI/agent-mcp-lab)** - ⭐ 221

994. **[Google-Scholar-MCP-Server](https://github.com/JackKuo666/Google-Scholar-MCP-Server)** - ⭐ 221
   A MCP Server for Google Scholar: 🔍 Enable AI assistants to search and access Google Scholar papers through a simple MCP interface.

995. **[mcp-twikit](https://github.com/adhikasp/mcp-twikit)** - ⭐ 220
   A Model Context Protocol (MCP) server for interacting with Twitter.

996. **[smart-tree](https://github.com/8b-is/smart-tree)** - ⭐ 219
   Smart Tree: not just a tree, a philosophy. A context-aware, AI-crafted replacement for 20+ tools with MEM8 quantum compression, semantic search, AST-smart editing, and partnership memory. Crafted with care by human + AI—accept no knock-offs.

997. **[home-assistant-cursor-agent](https://github.com/Coolver/home-assistant-cursor-agent)** - ⭐ 219
   Enable Cursor AI, VS Code, or any MCP-enabled IDE to help you manage Home Assistant: create automations, modify configs, and deploy changes using natural language

998. **[penpot-mcp](https://github.com/montevive/penpot-mcp)** - ⭐ 219
   Penpot MCP server

999. **[TradingAgents-MCPmode](https://github.com/guangxiangdebizi/TradingAgents-MCPmode)** - ⭐ 219
   TradingAgents-MCPmode 是一个创新的多智能体交易分析系统，集成了 Model Context Protocol (MCP) 工具，实现了智能化的股票分析和交易决策流程。系统通过多个专业化智能体的协作，提供全面的市场分析、投资建议和风险管理。

1000. **[antd-components-mcp](https://github.com/zhixiaoqiang/antd-components-mcp)** - ⭐ 218
   An MCP service for Ant Design components query | 一个减少 Ant Design 组件代码生成幻觉的 MCP 服务，包含系统提示词、组件文档、API 文档、代码示例和更新日志查询

1001. **[vulnerable-mcp-servers-lab](https://github.com/appsecco/vulnerable-mcp-servers-lab)** - ⭐ 218
   A collection of servers which are deliberately vulnerable to learn Pentesting MCP Servers.

1002. **[playwright-mcp](https://github.com/cloudflare/playwright-mcp)** - ⭐ 218
   Playwright MCP fork that works with Cloudflare Browser Rendering

1003. **[mcp-openapi-server](https://github.com/ivo-toby/mcp-openapi-server)** - ⭐ 218
   MCP Server (Model Context Protocol) for turning OpenAPI specifications into a MCP Resource

1004. **[image-gen-server](https://github.com/fengin/image-gen-server)** - ⭐ 217
   一个能与Cursor集成的图片生成mcp server工具，实现调用即梦逆向接口

1005. **[mermaid-mcp-server](https://github.com/peng-shawn/mermaid-mcp-server)** - ⭐ 217
   A Model Context Protocol (MCP) server that converts Mermaid diagrams to PNG images

1006. **[claude-historian-mcp](https://github.com/Vvkmnn/claude-historian-mcp)** - ⭐ 217
   🤖 An MCP server for surfacing useful Claude Code conversation history

1007. **[human-in-the-loop](https://github.com/KOBA789/human-in-the-loop)** - ⭐ 217
   An MCP (Model Context Protocol) server that allows AI assistants to ask questions to humans via Discord.

1008. **[domainstack.io](https://github.com/jakejarvis/domainstack.io)** - ⭐ 217
   🧰 All-in-one domain name intelligence as a service

1009. **[learn-agentic-ai-from-low-code-to-code](https://github.com/panaversity/learn-agentic-ai-from-low-code-to-code)** - ⭐ 217
   Build production-grade agents with OpenAI AgentKit, a no-code platfrom.

1010. **[lokka](https://github.com/merill/lokka)** - ⭐ 217
   MCP (Model Context Protocol) for Microsoft 365. Includes support for Microsoft Graph and other services

1011. **[Google-Search-MCP-Server](https://github.com/mixelpixx/Google-Search-MCP-Server)** - ⭐ 217
   MCP Server built for use with Claude Code, Claude Desktop, VS Code, Cline  - enable google search and ability to follow links and research websites

1012. **[tentix](https://github.com/labring/tentix)** - ⭐ 216
   TenTix (10x Efficiency) - An AI native customer service platform with 10x accelerated resolution. Support MCP extension, and AI knowlage base system.

1013. **[plate-playground-template](https://github.com/udecode/plate-playground-template)** - ⭐ 215
   Plate AI template with React 19, Next 16, Tailwind 4, MCP.

1014. **[vibevideo-mcp](https://github.com/hyepartners-gmail/vibevideo-mcp)** - ⭐ 214
   Agent MCP for ffmpeg

1015. **[mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus)** - ⭐ 214
   Model Context Protocol Servers for Milvus

1016. **[kite-mcp-server](https://github.com/zerodha/kite-mcp-server)** - ⭐ 214
   Zerodha Kite MCP server

1017. **[anki-mcp-server](https://github.com/nailuoGG/anki-mcp-server)** - ⭐ 214
   MCP server for Anki via AnkiConnect

1018. **[cpp-mcp](https://github.com/hkr04/cpp-mcp)** - ⭐ 214
   Lightweight C++ MCP (Model Context Protocol) SDK

1019. **[mcp-trends-hub](https://github.com/baranwang/mcp-trends-hub)** - ⭐ 214
   基于 Model Context Protocol (MCP) 协议的全网热点趋势一站式聚合服务

1020. **[binary_ninja_mcp](https://github.com/fosdickio/binary_ninja_mcp)** - ⭐ 214
   A Binary Ninja plugin containing an MCP server that enables seamless integration with your favorite LLM/MCP client.

1021. **[mcp_code_executor](https://github.com/bazinga012/mcp_code_executor)** - ⭐ 213
   The MCP Code Executor is an MCP server that allows LLMs to execute Python code within a specified Conda environment.

1022. **[mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server)** - ⭐ 213
   mindmap, mcp server, artifact

1023. **[razorpay-mcp-server](https://github.com/razorpay/razorpay-mcp-server)** - ⭐ 213
   Razorpay's Official MCP Server

1024. **[composer-trade-mcp](https://github.com/invest-composer/composer-trade-mcp)** - ⭐ 213
   Composer's MCP server lets MCP-enabled LLMs like Claude backtest trading ideas and automatically invest in them for you

1025. **[lihil](https://github.com/raceychan/lihil)** - ⭐ 212
   2X faster ASGI web framework for python, offering high-level development, low-level performance.

1026. **[uber-eats-mcp-server](https://github.com/ericzakariasson/uber-eats-mcp-server)** - ⭐ 211

1027. **[gibber-mcp](https://github.com/antonpk1/gibber-mcp)** - ⭐ 211
   Tiny MCP server with cryptography tools, sufficient to establish end-to-end encryption between LLM agents

1028. **[tmux-mcp](https://github.com/nickgnd/tmux-mcp)** - ⭐ 211
   A MCP server for our beloved terminal multiplexer tmux.

1029. **[ruby_llm-mcp](https://github.com/patvice/ruby_llm-mcp)** - ⭐ 210
   Full-featured MCP support for Ruby and RubyLLM—making it easy to build structured, composable LLM workflows in pure Ruby.

1030. **[yt-dlp-mcp](https://github.com/kevinwatt/yt-dlp-mcp)** - ⭐ 210
   A Model Context Protocol (MCP) server that bridges Video & Audio content with Large Language Models using yt-dlp.

1031. **[mcp-taskmanager](https://github.com/kazuph/mcp-taskmanager)** - ⭐ 210

1032. **[multimodal-mcp-client](https://github.com/Ejb503/multimodal-mcp-client)** - ⭐ 210
   A Multi-modal MCP client for voice powered agentic workflows

1033. **[mastergo-magic-mcp](https://github.com/mastergo-design/mastergo-magic-mcp)** - ⭐ 210
   MasterGo Magic MCP is a standalone MCP (Model Context Protocol) service designed to connect MasterGo design tools with AI models.

1034. **[claude-config-editor](https://github.com/gagarinyury/claude-config-editor)** - ⭐ 210
   Claude Config Editor is a lightweight web tool that helps you clean and optimize your Claude Code/Desktop config files (.claude.json). Analyze project sizes, bulk delete chat histories, export data for backup, manage servers visually, and speed up Claude—all locally, with auto-backup, no dependencies, and cross-platform support.

1035. **[Autono](https://github.com/vortezwohl/Autono)** - ⭐ 209
   A ReAct-Based Highly Robust Autonomous Agent Framework.

1036. **[figma-mcp](https://github.com/MatthewDailey/figma-mcp)** - ⭐ 209
   ModelContextProtocol for Figma's REST API

1037. **[jebmcp](https://github.com/dawnslab/jebmcp)** - ⭐ 209

1038. **[automagik-genie](https://github.com/namastexlabs/automagik-genie)** - ⭐ 207
   🧞 Automagik Genie – bootstrap, update, and roll back AI agent workspaces with a single CLI + MCP toolkit.

1039. **[mcp-server-deep-research](https://github.com/reading-plus-ai/mcp-server-deep-research)** - ⭐ 207

1040. **[jetski](https://github.com/hyprmcp/jetski)** - ⭐ 207
   Authentication, analytics, and prompt visibility for MCP servers with zero code changes. Supports OAuth2.1, DCR, real-time logs, and client onboarding out of the box

1041. **[mcp-context-protector](https://github.com/trailofbits/mcp-context-protector)** - ⭐ 206
   MCP security wrapper

1042. **[mcp-rb](https://github.com/funwarioisii/mcp-rb)** - ⭐ 206
   A lightweight Ruby framework for building MCP servers with a Sinatra-like DSL

1043. **[Remote-MCP](https://github.com/ssut/Remote-MCP)** - ⭐ 206
   A type-safe solution to remote MCP communication, enabling effortless integration for centralized management of Model Context.

1044. **[ha-mcp-for-xiaozhi](https://github.com/c1pher-cn/ha-mcp-for-xiaozhi)** - ⭐ 206
   Homeassistant MCP server for 小智AI

1045. **[gram](https://github.com/speakeasy-api/gram)** - ⭐ 206
   Power your product agents and chat with MCP! 

1046. **[OSWorld-MCP](https://github.com/X-PLUG/OSWorld-MCP)** - ⭐ 205

1047. **[notion_mcp](https://github.com/danhilse/notion_mcp)** - ⭐ 205
   A simple MCP integration that allows Claude to read and manage a personal Notion todo list

1048. **[melrose](https://github.com/emicklei/melrose)** - ⭐ 205
   interactive programming of melodies, producing MIDI 

1049. **[mcp-n8n-workflow-builder](https://github.com/salacoste/mcp-n8n-workflow-builder)** - ⭐ 205
   AI-powered n8n workflow automation through natural language. MCP server enabling Claude AI & Cursor IDE to create, manage, and monitor workflows via Model Context Protocol. Multi-instance support, 17 tools, comprehensive docs. Build workflows conversationally without manual JSON editing.

1050. **[AutomatedEmulation](https://github.com/iknowjason/AutomatedEmulation)** - ⭐ 205
   An automated Adversary Emulation lab with terraform and MCP server.  Build Caldera techniques and operations assisted with LLMs.  Built for IaC stability, consistency, and speed.

1051. **[langchain-mcp](https://github.com/rectalogic/langchain-mcp)** - ⭐ 205
   Model Context Protocol tool support for LangChain

1052. **[ht-mcp](https://github.com/memextech/ht-mcp)** - ⭐ 205
   Pure Rust implementation of MCP server for headless terminal 

1053. **[sora-mcp](https://github.com/Doriandarko/sora-mcp)** - ⭐ 204
   An MCP server to use Sora video generation APIs

1054. **[yahoo-finance-mcp](https://github.com/Alex2Yang97/yahoo-finance-mcp)** - ⭐ 204
   This is a Model Context Protocol (MCP) server that provides comprehensive financial data from Yahoo Finance. It allows you to retrieve detailed information about stocks, including historical prices, company information, financial statements, options data, and market news.

1055. **[sqrl](https://github.com/DataSQRL/sqrl)** - ⭐ 203
   Data Pipeline Automation Framework to build MCP servers, data APIs, and data lakes with SQL.

1056. **[mcp-echarts](https://github.com/hustcc/mcp-echarts)** - ⭐ 203
   🧬 Generate visual charts using ECharts with AI MCP dynamically, used for chart generation and data analysis.

1057. **[phone-mcp](https://github.com/hao-cyber/phone-mcp)** - ⭐ 203
   A phone control plugin for MCP that allows you to control your Android phone through ADB commands to connect any human

1058. **[y-cli](https://github.com/luohy15/y-cli)** - ⭐ 202
   A Tiny Terminal Chat App for AI Models with MCP Client Support

1059. **[unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server)** - ⭐ 202
   🔎 A MCP server for Unsplash image search.

1060. **[dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp)** - ⭐ 201
   MCP server for Dynatrace Observability

1061. **[pctx](https://github.com/portofcontext/pctx)** - ⭐ 201
   pctx is the execution layer for agentic tool calls. It exposes custom tools and MCP servers as code that runs in secure sandboxes for token-efficient calls.

1062. **[mcp](https://github.com/hopx-ai/mcp)** - ⭐ 200

1063. **[BifrostMCP](https://github.com/biegehydra/BifrostMCP)** - ⭐ 200
   VSCode Extension with an MCP server that exposes semantic tools like Find Usages and Rename to LLMs

1064. **[mathom](https://github.com/stephenlacy/mathom)** - ⭐ 199
   Run and monitor MCP servers locally

1065. **[ai-infrastructure-agent](https://github.com/VersusControl/ai-infrastructure-agent)** - ⭐ 199
   AI Infrastructure Agent is an intelligent system that allows you to manage AWS infrastructure using natural language commands.

1066. **[mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser)** - ⭐ 199
   A MCP Server for the RAG Web Browser Actor

1067. **[mcp-launchpad](https://github.com/kenneth-liao/mcp-launchpad)** - ⭐ 199
   A lightweight CLI for efficiently discovering (search) and executing tools from multiple MCP (Model Context Protocol) servers.

1068. **[metorial-platform](https://github.com/metorial/metorial-platform)** - ⭐ 198
   The engine powering hundreds of thousands of MCP connections 🤖 🔥

1069. **[claude-self-reflect](https://github.com/ramakay/claude-self-reflect)** - ⭐ 198
   Claude forgets everything. This fixes that. 🔗 www.npmjs.com/package/claude-self-reflect

1070. **[pbi-desktop-mcp-public](https://github.com/maxanatsko/pbi-desktop-mcp-public)** - ⭐ 198
   The MCP Engine is a Power BI tool that lets AI assistants like Claude interact with your Power BI models programmatically: read your model structure, run DAX queries, create and modify measures, manage relationships, and perform advanced analytics - all through natural conversation.

1071. **[concierge](https://github.com/concierge-hq/concierge)** - ⭐ 198
   The fabric for building next gen MCP apps

1072. **[rmcp](https://github.com/finite-sample/rmcp)** - ⭐ 197
   R MCP Server

1073. **[mongodb-lens](https://github.com/furey/mongodb-lens)** - ⭐ 197
   🍃🔎 MongoDB Lens: Full Featured MCP Server for MongoDB Databases

1074. **[sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp)** - ⭐ 197
   A SEC EDGAR MCP (Model Context Protocol) Server

1075. **[MakeMoneyWithAI](https://github.com/garylab/MakeMoneyWithAI)** - ⭐ 197
   A list of open-source AI projects you can use to generate income easily.

1076. **[sandboxed.sh](https://github.com/Th0rgal/sandboxed.sh)** - ⭐ 197
   Self-hosted orchestrator for AI autonomous agents. Run Claude Code & Open Code in isolated linux workspaces. Manage your skills, configs and encrypted secrets with a git repo.

1077. **[ProxmoxMCP](https://github.com/canvrno/ProxmoxMCP)** - ⭐ 196
   MCP for Proxmox integration in Cline

1078. **[cognition-wheel](https://github.com/Hormold/cognition-wheel)** - ⭐ 196
   A Model Context Protocol (MCP) server that implements a "wisdom of crowds" approach to AI reasoning by consulting multiple state-of-the-art language models in parallel and synthesizing their responses.

1079. **[opik-mcp](https://github.com/comet-ml/opik-mcp)** - ⭐ 196
   Model Context Protocol (MCP) implementation for Opik enabling seamless IDE integration and unified access to prompts, projects, traces, and metrics. 

1080. **[wavefront](https://github.com/rootflo/wavefront)** - ⭐ 196
   🔥🔥🔥 Enterprise AI middleware, alternative to unifyapps, n8n, lyzr

1081. **[mcp-proxy-server](https://github.com/adamwattis/mcp-proxy-server)** - ⭐ 196
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single interface

1082. **[mcp-portal-transparencia](https://github.com/dutradotdev/mcp-portal-transparencia)** - ⭐ 195
   MCP para orquestração automatizada de chamadas à API do Portal da Transparência do Governo Federal brasileiro

1083. **[nano-agent](https://github.com/disler/nano-agent)** - ⭐ 195
   A MCP Server for a small scale engineering agents with multi-provider LLM support.

1084. **[figma-flutter-mcp](https://github.com/mhmzdev/figma-flutter-mcp)** - ⭐ 195
   An MCP server that provides the coding agents Figma's design token to write Flutter code.

1085. **[mcp_forge](https://github.com/mlzoo/mcp_forge)** - ⭐ 195
   这是一个专为开发企业级MCP server而设计的通用开发框架

1086. **[servicenow-mcp](https://github.com/echelon-ai-labs/servicenow-mcp)** - ⭐ 195
   MCP Server for ServiceNow

1087. **[pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp)** - ⭐ 195
   MCP server for PageIndex. PageIndex is a vectorless reasoning-based RAG system which uses multi-step reasoning and tree search to retrieve information like a human expert would.

1088. **[gemini-kit](https://github.com/nth5693/gemini-kit)** - ⭐ 195
   🚀 19 AI Agents + 44 Commands for Gemini CLI - Code 10x faster with auto planning, testing, review & security

1089. **[waldzell-mcp](https://github.com/waldzellai/waldzell-mcp)** - ⭐ 194
   Waldzell AI's monorepo of MCP servers. Use in Claude Desktop, Cline, Roo Code, and more!

1090. **[nosia](https://github.com/dilolabs/nosia)** - ⭐ 194
   Self-hosted AI RAG + MCP Platform

1091. **[claudex](https://github.com/Mng-dev-ai/claudex)** - ⭐ 194
   Your own Claude Code UI, local/e2b/modal sandbox, in-browser VS Code, terminal, multi-provider support (Max, Z.AI, OpenRouter), custom skills, and MCP servers.

1092. **[frida-mcp](https://github.com/dnakov/frida-mcp)** - ⭐ 193
   MCP stdio server for frida

1093. **[persistent-ai-memory](https://github.com/savantskie/persistent-ai-memory)** - ⭐ 192
   A persistent local memory for AI, LLMs, or Copilot in VS Code.

1094. **[gcp-mcp](https://github.com/eniayomi/gcp-mcp)** - ⭐ 192
   A Model Context Protocol (MCP) server that enables AI assistants like Claude to interact with your Google Cloud Platform environment. This allows for natural language querying and management of your GCP resources during conversations.

1095. **[mcp-guardian](https://github.com/eqtylab/mcp-guardian)** - ⭐ 192
   Manage / Proxy / Secure your MCP Servers

1096. **[easy-mcp](https://github.com/zcaceres/easy-mcp)** - ⭐ 192
   Absurdly easy Model Context Protocol Servers in Typescript

1097. **[mcp-servers-nix](https://github.com/natsukium/mcp-servers-nix)** - ⭐ 192
   A Nix-based configuration framework for Model Control Protocol (MCP) servers with ready-to-use packages.

1098. **[life-sciences](https://github.com/anthropics/life-sciences)** - ⭐ 192
   Repo for the Claude Code Marketplace to use with the Claude for Life Sciences Launch. This will continue to host the marketplace.json long-term, but not the actual MCP servers.

1099. **[RelaMind](https://github.com/El-12stu/RelaMind)** - ⭐ 191
   基于 AI 的个人成长轨迹分析系统，通过记录生活、回顾历史、分析模式帮助用户更好地理解自己，实现持续成长。包含智能路由、RAG 检索、自主任务智能体等功能。

1100. **[hf-mcp-server](https://github.com/huggingface/hf-mcp-server)** - ⭐ 191
   Hugging Face MCP Server

1101. **[after-effects-mcp](https://github.com/Dakkshin/after-effects-mcp)** - ⭐ 191
   MCP Server for Adobe After Effects. Enables remote control (compositions, text, shapes, solids, properties) via the Model Context Protocol using ExtendScript.

1102. **[touchdesigner-mcp](https://github.com/8beeeaaat/touchdesigner-mcp)** - ⭐ 191
   MCP server for TouchDesigner

1103. **[MCP-server-client-computer-use-ai-sdk](https://github.com/mediar-ai/MCP-server-client-computer-use-ai-sdk)** - ⭐ 190

1104. **[seo-mcp](https://github.com/cnych/seo-mcp)** - ⭐ 190
   A free SEO tool MCP (Model Control Protocol) service based on Ahrefs data. Includes features such as backlinks, keyword ideas, and more.

1105. **[utcp-mcp](https://github.com/universal-tool-calling-protocol/utcp-mcp)** - ⭐ 190
   All-in-one MCP server that can connect your AI agents to any native endpoint, powered by UTCP

1106. **[codex-mcp-server](https://github.com/tuannvm/codex-mcp-server)** - ⭐ 190
   MCP server wrapper for OpenAI Codex CLI that enables Claude Code to leverage Codex's AI capabilities directly.

1107. **[armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp)** - ⭐ 189
   The MCP server for interacting with Blockchain, Swaps, Strategic Planning and more.

1108. **[supabase-mcp](https://github.com/coleam00/supabase-mcp)** - ⭐ 189
   Supabase MCP server created in Python.

1109. **[mcp-agent-graph](https://github.com/keta1930/mcp-agent-graph)** - ⭐ 189
   MCP Agent Graph is a Multi-Agent System built on the principles of Context Engineering

1110. **[AutoDocs](https://github.com/TrySita/AutoDocs)** - ⭐ 188
   We handle what engineers and IDEs won't: generating and maintaining technical documentation for your codebase, while also providing search with dependency-aware context to help your AI tools understand your codebase and its conventions.

1111. **[mcp-linkedin](https://github.com/adhikasp/mcp-linkedin)** - ⭐ 188
   A Model Context Protocol (MCP) server that provides tools to interact with LinkedIn's Feeds and Job API.

1112. **[code-sandbox-mcp](https://github.com/philschmid/code-sandbox-mcp)** - ⭐ 187

1113. **[mcp-usecase](https://github.com/teddynote-lab/mcp-usecase)** - ⭐ 187

1114. **[mcp-injection-experiments](https://github.com/invariantlabs-ai/mcp-injection-experiments)** - ⭐ 187
   Code snippets to reproduce MCP tool poisoning attacks.

1115. **[sudocode](https://github.com/sudocode-ai/sudocode)** - ⭐ 187
   Lightweight agent orchestration dev tool that lives in your repo

1116. **[comfyui-mcp-server](https://github.com/joenorton/comfyui-mcp-server)** - ⭐ 187
   lightweight Python-based MCP (Model Context Protocol) server for local ComfyUI

1117. **[Omni-Adapter](https://github.com/HuChundong/Omni-Adapter)** - ⭐ 186
   多平台 文生图/图生图 等能力接入MCP

1118. **[auto-mcp](https://github.com/brizzai/auto-mcp)** - ⭐ 186
   Transform any OpenAPI/Swagger definition into a fully-featured Model Context Protocol (MCP) server

1119. **[Geargrafx](https://github.com/drhelius/Geargrafx)** - ⭐ 186
   PC Engine / TurboGrafx-16 / SuperGrafx / PCE CD-ROM² emulator, debugger, and embedded MCP server for macOS, Windows, Linux, BSD and RetroArch.

1120. **[EdgeBox](https://github.com/BIGPPWONG/EdgeBox)** - ⭐ 186
   A fully-featured, GUI-powered local LLM Agent sandbox with complete MCP protocol support.   Features both CLI and full desktop environment, enabling AI agents to operate browsers, terminal, and other desktop applications just like humans. Based on E2B oss code.

1121. **[overseer](https://github.com/dmmulroy/overseer)** - ⭐ 186
   CLI & Codemode MCP server for agent task management

1122. **[MCP-Checklists](https://github.com/MCP-Manager/MCP-Checklists)** - ⭐ 185

1123. **[litemcp](https://github.com/wong2/litemcp)** - ⭐ 185
   A TypeScript framework for building MCP servers elegantly

1124. **[gistpad-mcp](https://github.com/lostintangent/gistpad-mcp)** - ⭐ 185
   📓 An MCP server for managing your personal knowledge, daily notes, and re-usable prompts via GitHub Gists

1125. **[mcp-logseq](https://github.com/ergut/mcp-logseq)** - ⭐ 185
   MCP server to interact with LogSeq via its Local HTTP API - enabling AI assistants like Claude to seamlessly read, write, and manage your LogSeq graph.

1126. **[claude-context-local](https://github.com/FarhanAliRaza/claude-context-local)** - ⭐ 185
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent. Embeddings are created and stored locally. No API cost. 

1127. **[a2a_mcp-example](https://github.com/ishanExtreme/a2a_mcp-example)** - ⭐ 184
   An example showing how A2A and MCP can be used together

1128. **[ai-counsel](https://github.com/blueman82/ai-counsel)** - ⭐ 184
   True deliberative consensus MCP server where AI models debate and refine positions across multiple rounds

1129. **[mcp-servers](https://github.com/cursor/mcp-servers)** - ⭐ 184
   A list of MCP (Model Context Protocol) servers for developer tools and services

1130. **[wikipedia-mcp](https://github.com/Rudra-ravi/wikipedia-mcp)** - ⭐ 183
   A Model Context Protocol (MCP) server that retrieves information from Wikipedia to provide context to LLMs.

1131. **[mcp-proxy-server](https://github.com/ptbsare/mcp-proxy-server)** - ⭐ 183
   This server acts as a central hub for Model Context Protocol (MCP) resource servers.

1132. **[siconos](https://github.com/siconos/siconos)** - ⭐ 183
   Simulation framework for nonsmooth dynamical systems

1133. **[protoc-gen-go-mcp](https://github.com/redpanda-data/protoc-gen-go-mcp)** - ⭐ 183
   Go protobuf compiler extension to turn any gRPC service into an MCP server

1134. **[agents](https://github.com/astronomer/agents)** - ⭐ 183
   AI agent tooling for data engineering workflows.

1135. **[thinkchain](https://github.com/martinbowling/thinkchain)** - ⭐ 182
   🧠 Advanced Claude streaming interface with interleaved thinking, dynamic tool discovery, and MCP integration. Watch Claude think through problems in real-time while executing tools with live progress updates.

1136. **[mcp-openai-gemini-llama-example](https://github.com/philschmid/mcp-openai-gemini-llama-example)** - ⭐ 182

1137. **[dify-plugin-tools-mcp_sse](https://github.com/junjiem/dify-plugin-tools-mcp_sse)** - ⭐ 182
   Dify 1.0 Plugin MCP HTTP with SSE or Streamable HTTP transport Tools

1138. **[quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers)** - ⭐ 181
   Model Context Protocol Servers in Quarkus

1139. **[k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server)** - ⭐ 181
   K8s-mcp-server is a Model Context Protocol (MCP) server that enables AI assistants like Claude to securely execute Kubernetes commands. It provides a bridge between language models and essential Kubernetes CLI tools including kubectl, helm, istioctl, and argocd, allowing AI systems to assist with cluster management, troubleshooting, and deployments

1140. **[smart-coding-mcp](https://github.com/omar-haris/smart-coding-mcp)** - ⭐ 181
   An extensible Model Context Protocol (MCP-Local-MRL-RAG-AST) server that provides intelligent semantic code search for AI assistants. Built with local AI models, inspired by Cursor's semantic search.

1141. **[penpot-mcp](https://github.com/penpot/penpot-mcp)** - ⭐ 181
   Penpot's official MCP Server

1142. **[4D-ARE](https://github.com/ybeven/4D-ARE)** - ⭐ 180
   Build LLM agents that explain why, not just what. Attribution-driven agent requirements engineering framework. Based on the 4D-ARE Paper - https://arxiv.org/abs/2601.04556

1143. **[mcp-server-siri-shortcuts](https://github.com/dvcrn/mcp-server-siri-shortcuts)** - ⭐ 180
   MCP for calling Siri Shorcuts from LLMs

1144. **[garmin_mcp](https://github.com/Taxuspt/garmin_mcp)** - ⭐ 180
   MCP server to access Garmin data

1145. **[git-mcp-server](https://github.com/cyanheads/git-mcp-server)** - ⭐ 180
   An MCP (Model Context Protocol) server enabling LLMs and AI agents to interact with Git repositories. Provides tools for comprehensive Git operations including clone, commit, branch, diff, log, status, push, pull, merge, rebase, worktree, tag management, and more, via the MCP standard. STDIO & HTTP.

1146. **[mcp-text-editor](https://github.com/tumf/mcp-text-editor)** - ⭐ 178

1147. **[claude-code-mcp](https://github.com/auchenberg/claude-code-mcp)** - ⭐ 178
   claude-code-mcp

1148. **[burp-mcp-agents](https://github.com/six2dez/burp-mcp-agents)** - ⭐ 178
   Practical setup guides and helpers to connect Burp Suite MCP Server to multiple AI backends (Codex, Gemini, Ollama, ...).

1149. **[xero-mcp-server](https://github.com/XeroAPI/xero-mcp-server)** - ⭐ 178
   An MCP server that integrates with the MCP protocol. https://modelcontextprotocol.io/introduction

1150. **[tripo-mcp](https://github.com/VAST-AI-Research/tripo-mcp)** - ⭐ 177
   Official MCP server for Tripo

1151. **[ida-mcp-server-plugin](https://github.com/taida957789/ida-mcp-server-plugin)** - ⭐ 177
   IDA Pro Plugin for serving MCP SSE server for cursor / claude

1152. **[bilibili-mcp-server](https://github.com/huccihuang/bilibili-mcp-server)** - ⭐ 177
   MCP Server for the Bilibili API, supporting various operations.

1153. **[facebook-ads-library-mcp](https://github.com/talknerdytome-labs/facebook-ads-library-mcp)** - ⭐ 177
   MCP Server for Facebook ADs Library - Get instant answers from FB's ad library

1154. **[spring-ai-playground](https://github.com/JM-Lab/spring-ai-playground)** - ⭐ 176
   A self-hosted web UI that simplifies AI experimentation and testing for Java developers. It provides playgrounds for all major vector databases and MCP tools, supports intuitive interaction with LLMs, and enables rapid development and testing of RAG workflows, MCP integrations, and unified chat experiences.

1155. **[mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server)** - ⭐ 176

1156. **[anki-mcp-server](https://github.com/scorzeth/anki-mcp-server)** - ⭐ 175
   An MCP server for Anki

1157. **[quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server)** - ⭐ 175
   This extension enables developers to implement the MCP server features easily.

1158. **[tableau-mcp](https://github.com/tableau/tableau-mcp)** - ⭐ 175
   Official Tableau MCP server, providing a suite of tools that make it easier for developers to build and configure AI applications that integrate with Tableau Cloud and Server.

1159. **[mcp](https://github.com/magicuidesign/mcp)** - ⭐ 175
   Official Magic UI MCP server.

1160. **[appium-mcp](https://github.com/appium/appium-mcp)** - ⭐ 175
   Appium MCP on Steroids!

1161. **[mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp)** - ⭐ 174
   A mongo db server for the model context protocol (MCP)

1162. **[aws-finops-mcp-server](https://github.com/ravikiranvm/aws-finops-mcp-server)** - ⭐ 174
   An MCP (Model Context Protocol) server that brings powerful AWS FinOps capabilities directly into your AI assistant. Analyze cloud costs, audit for waste, and get budget insights using natural language, all while keeping your credentials secure on your local machine.

1163. **[Revornix](https://github.com/Qingyon-AI/Revornix)** - ⭐ 173
   Built-in MCP client–powered document/news management tool with daily auto summaries, document interaction, user-defined notifications (email, apns, etc.), and customizable model support.内置 MCP 客户端的文档/资讯管理工具，支持每日自动总结、文档交互、自定义通知（邮箱、APNS等）以及模型自定义。

1164. **[aws-mcp-server](https://github.com/alexei-led/aws-mcp-server)** - ⭐ 173
   A lightweight service that enables AI assistants to execute AWS CLI commands (in safe containerized environment) through the Model Context Protocol (MCP). Bridges Claude, Cursor, and other MCP-aware AI tools with AWS CLI for enhanced cloud infrastructure management.

1165. **[mcp-chat](https://github.com/PipedreamHQ/mcp-chat)** - ⭐ 173
   Examples of using Pipedream's MCP server in your app or AI agent.

1166. **[discord-mcp](https://github.com/SaseQ/discord-mcp)** - ⭐ 173
   A MCP server for the Discord integration. Enable your AI assistants to seamlessly interact with Discord. Enhance your Discord experience with powerful automation capabilities.

1167. **[skyll](https://github.com/assafelovic/skyll)** - ⭐ 173
   A tool for AI agents to discover and learn skills autonomously

1168. **[tomcp](https://github.com/Ami3466/tomcp)** - ⭐ 172
   Turn any website or doc into an MCP server

1169. **[mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb)** - ⭐ 172
   A Model Context Protocol (MCP) server implementation for DuckDB, providing database interaction capabilities

1170. **[mcp-google-map](https://github.com/cablate/mcp-google-map)** - ⭐ 172
   A powerful Model Context Protocol (MCP) server providing comprehensive Google Maps API integration with LLM processing capabilities.

1171. **[google-analytics-mcp](https://github.com/surendranb/google-analytics-mcp)** - ⭐ 172
   Google Analytics 4 MCP Server for Claude, Cursor, Windsurf etc - Access GA4 data through natural language with 200+ dimensions & metrics

1172. **[skunit](https://github.com/mehrandvd/skunit)** - ⭐ 171
   skUnit is a testing tool for AI units, such as IChatClient, MCP Servers and agents.

1173. **[Text2Sql.Net](https://github.com/shuyu-labs/Text2Sql.Net)** - ⭐ 171
   Text2Sql.Net 是一个使用DotNet和Semantic Kernel开发的Text2Sql工具

1174. **[claudepro-directory](https://github.com/JSONbored/claudepro-directory)** - ⭐ 171
   Claude Pro Directory is a searchable collection of pre-built configurations, MCP servers, and custom rules designed to enhance Claude AI's performance for specific tasks.

1175. **[mcp-server-wazuh](https://github.com/gbrigandi/mcp-server-wazuh)** - ⭐ 171
   MCP Server for Wazuh SIEM

1176. **[discordmcp](https://github.com/v-3/discordmcp)** - ⭐ 171
   Discord MCP Server for Claude Integration

1177. **[Text2Sql.Net](https://github.com/AIDotNet/Text2Sql.Net)** - ⭐ 170
   Text2Sql.Net 是一个使用DotNet和Semantic Kernel开发的Text2Sql工具

1178. **[mcp-scholarly](https://github.com/adityak74/mcp-scholarly)** - ⭐ 170
   A MCP server to search for accurate academic articles.

1179. **[openapi-mcp](https://github.com/ckanthony/openapi-mcp)** - ⭐ 170
   Dockerized MCP Server to allow your AI agent to access any API with existing api docs

1180. **[sketchup-mcp](https://github.com/mhyrr/sketchup-mcp)** - ⭐ 170
   Sketchup Model Context Protocol

1181. **[command](https://github.com/scopecraft/command)** - ⭐ 170
   Scopecraft Command - A CLI and MCP server for Markdown-Driven Task Management (MDTM)

1182. **[markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server)** - ⭐ 170
   An MCP server for converting Markdown to interactive mind maps with export support (PNG/JPG/SVG).

1183. **[y-gui](https://github.com/luohy15/y-gui)** - ⭐ 168
   A Tiny Web Chat App for AI Models with MCP Client Support

1184. **[install-mcp](https://github.com/supermemoryai/install-mcp)** - ⭐ 168
   A simple CLI to install MCP servers into any client - auth included!

1185. **[Chanakya-Local-Friend](https://github.com/Rishabh-Bajpai/Chanakya-Local-Friend)** - ⭐ 167
   Chanakya is an advanced, open-source, and self-hostable voice assistant designed for privacy, power, and flexibility. It leverages local AI/ML models to ensure your data stays with you. It Integrates with 1000+ third-party MCP servers including Home Assistant. 

1186. **[keyboard-local](https://github.com/keyboard-dev/keyboard-local)** - ⭐ 167
   One MCP Server, All Your Apps, Privacy First

1187. **[mcp](https://github.com/neo4j/mcp)** - ⭐ 167
   Neo4j official MCP Server

1188. **[mcp-use-ts](https://github.com/mcp-use/mcp-use-ts)** - ⭐ 167
   mcp-use is the framework for MCP with the best DX - Build AI agents, create MCP   servers with UI widgets, and debug with built-in inspector. Includes client SDK, server SDK, React hooks, and powerful dev tools.

1189. **[agentregistry](https://github.com/agentregistry-dev/agentregistry)** - ⭐ 167
   Fast-track AI innovation with a centralized, trusted, curated registry

1190. **[mcp-agent-langchainjs](https://github.com/Azure-Samples/mcp-agent-langchainjs)** - ⭐ 167
   Serverless AI agent using LangChain.js and Model Context Protocol (MCP) integration to order burgers from a burger restaurant

1191. **[meilisearch-mcp](https://github.com/meilisearch/meilisearch-mcp)** - ⭐ 167
   A Model Context Protocol (MCP) server for interacting with Meilisearch through LLM interfaces.

1192. **[toolbase](https://github.com/Toolbase-AI/toolbase)** - ⭐ 166
   A desktop application that adds powerful tools to Claude and AI platforms

1193. **[mcp-shell-server](https://github.com/tumf/mcp-shell-server)** - ⭐ 166

1194. **[DrissionPageMCP](https://github.com/wxhzhwxhzh/DrissionPageMCP)** - ⭐ 166
   基于DrissionPage和FastMCP的浏览器自动化MCP服务器，提供丰富的浏览器操作API供AI调用

1195. **[docs](https://github.com/strands-agents/docs)** - ⭐ 166
   Documentation for the Strands Agents SDK. A model-driven approach to building AI agents in just a few lines of code. 

1196. **[mcp-access-point](https://github.com/sxhxliang/mcp-access-point)** - ⭐ 165
   Turn a web server into an MCP server in one click without making any code changes.

1197. **[postman-mcp-server](https://github.com/postmanlabs/postman-mcp-server)** - ⭐ 165
   Connect your AI to your APIs on Postman

1198. **[c4-genai-suite](https://github.com/codecentric/c4-genai-suite)** - ⭐ 164
   c4 GenAI Suite

1199. **[lsp-mcp](https://github.com/jonrad/lsp-mcp)** - ⭐ 164
   An Model Context Protocol (MCP) server that provides LLMs/AI Agents with the capabilities of a language server protocol (LSP) server. This gives the AI the ability to get language aware context from the codebase.

1200. **[linux-mcp-server](https://github.com/rhel-lightspeed/linux-mcp-server)** - ⭐ 164
   Tools to allow LLM clients to interact with Linux systems remotely

1201. **[AIDA](https://github.com/Vasco0x4/AIDA)** - ⭐ 164
   AI-Driven Security Assessment - Connect AI to 400+ pentesting tools via MCP

1202. **[dify-mcp-client](https://github.com/3dify-project/dify-mcp-client)** - ⭐ 163
   MCP Client as an Agent Strategy Plugin. Support GUI operation via UI-TARS-SDK.

1203. **[mcp-telegram](https://github.com/sparfenyuk/mcp-telegram)** - ⭐ 163
   MCP server to work with Telegram through MTProto

1204. **[cli-mcp-server](https://github.com/MladenSU/cli-mcp-server)** - ⭐ 162
   Command line interface for MCP clients with secure execution and customizable security policies

1205. **[integrate-mcp-with-copilot](https://github.com/skills/integrate-mcp-with-copilot)** - ⭐ 162
   Learn how to use MCP Servers with GitHub Copilot

1206. **[mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate)** - ⭐ 161
   MCP (Model Context Protocol) server for Weaviate

1207. **[gbox](https://github.com/babelcloud/gbox)** - ⭐ 161
   Cli and MCP for gbox. Enable AI agents to operate Android/Browser/Desktop like human.

1208. **[jmap-mcp](https://github.com/wyattjoh/jmap-mcp)** - ⭐ 161
   A Model Context Protocol (MCP) server that provides tools for interacting with JMAP (JSON Meta Application Protocol) email servers. Built with Deno and using the jmap-jam client library.

1209. **[pg-mcp-server](https://github.com/ericzakariasson/pg-mcp-server)** - ⭐ 161
   MCP Server for Postgres

1210. **[polymarket-mcp-server](https://github.com/caiovicentino/polymarket-mcp-server)** - ⭐ 161
   🤖 AI-Powered MCP Server for Polymarket - Enable Claude to trade prediction markets with 45 tools, real-time monitoring, and enterprise-grade safety features

1211. **[UnityNaturalMCP](https://github.com/notargs/UnityNaturalMCP)** - ⭐ 160
   UnityNaturalMCP is an MCP server implementation for Unity that aims for a "natural" user experience.

1212. **[photoshop-python-api-mcp-server](https://github.com/loonghao/photoshop-python-api-mcp-server)** - ⭐ 160
   A Model Context Protocol (MCP) server that interfaces with Adobe Photoshop's Python API. Enables LLMs to execute image editing operations, automate workflows, and manage Photoshop tasks through structured commands and context-aware interactions.

1213. **[flights-mcp](https://github.com/ravinahp/flights-mcp)** - ⭐ 160
   An MCP server to search for flights.

1214. **[open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp)** - ⭐ 160
   An OpenStreetMap MCP server implementation that enhances LLM capabilities with location-based services and geospatial data.

1215. **[tmcp](https://github.com/paoloricciuti/tmcp)** - ⭐ 160
   Typescript SDK to build MCP servers in an agnostic way

1216. **[Context-Engineering-for-Multi-Agent-Systems](https://github.com/Denis2054/Context-Engineering-for-Multi-Agent-Systems)** - ⭐ 160
   Save thousands of lines of code by building universal, domain-agnostic Multi-Agent Systems (MAS) through high-level semantic orchestration. This repository provides a production-ready blueprint for the Agentic Era, allowing you to replace rigid, hard-coded workflows with a dynamic transparent Context Engine that provides 100% transparency.

1217. **[dbt-llm-agent](https://github.com/pragunbhutani/dbt-llm-agent)** - ⭐ 159
   LLM based AI Agent to automate Data Analysis for dbt projects with remote MCP server

1218. **[Quickchart-MCP-Server](https://github.com/GongRzhe/Quickchart-MCP-Server)** - ⭐ 159
   A Model Context Protocol server for generating charts using QuickChart.io  . It allows you to create various types of charts through MCP tools.

1219. **[Companion](https://github.com/mattt/Companion)** - ⭐ 159
   Your neighborhood friendly MCP utility for macOS, iOS, and visionOS

1220. **[slack-mcp-client](https://github.com/tuannvm/slack-mcp-client)** - ⭐ 159
   A Slack bot and MCP client acts as a bridge between Slack and Model Context Protocol (MCP) servers. Using Slack as the interface, it enables large language models (LLMs) to connect and interact with various MCP servers through standardized MCP tools.

1221. **[gate22](https://github.com/aipotheosis-labs/gate22)** - ⭐ 159
   Open-source MCP gateway and control plane for teams to govern which tools agents can use, what they can do, and how it’s audited—across agentic IDEs like Cursor, or other agents and AI tools.

1222. **[opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server)** - ⭐ 159
   Unified MCP server for querying OpenTelemetry traces across multiple backends (Jaeger, Tempo, Traceloop, etc.), enabling AI agents to analyze distributed traces for automated debugging and observability.

1223. **[remote-mcp-server](https://github.com/gleanwork/remote-mcp-server)** - ⭐ 158
   Remote MCP Server that securely connects Enterprise context with your LLM, IDE, or agent platform of choice.

1224. **[toolsdk-mcp-registry](https://github.com/toolsdk-ai/toolsdk-mcp-registry)** - ⭐ 158
   ToolSDK.ai's Awesome MCP Servers and Packages Registry and Database with Structured JSON configurations. Supports OAuth2.1, DCR...

1225. **[lucid-agents](https://github.com/daydreamsai/lucid-agents)** - ⭐ 158
   Lucid Agents Commerce SDK. Bootstrap AI agents in 60 seconds that can pay, sell, and participate in agentic commerce supply chains. Our protocol agnostic SDK provides CLI-generated templates and drop-in adapters for Hono, Express, Next.js, and TanStack, giving you instant access to crypto/fiat payment rails (AP2, A2A, x402, ERC8004).

1226. **[recall](https://github.com/joseairosa/recall)** - ⭐ 158
   Give Claude perfect recall - Redis-powered persistent memory for LLMs

1227. **[obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp)** - ⭐ 158
   Connect Claude Code and other AI tools to your Obsidian notes using Model Context Protocol (MCP)

1228. **[ssh-mcp-server](https://github.com/classfang/ssh-mcp-server)** - ⭐ 158
   基于 SSH 的 MCP 服务器 🧙‍♀️。已被MCP官方收录 🎉。 SSH MCP Server 🧙‍♀️. It has been included in the community MCP repository 🎉.

1229. **[fetch-mcp](https://github.com/egoist/fetch-mcp)** - ⭐ 157
   An MCP server for fetching URLs / Youtube video transcript.

1230. **[spotinfo](https://github.com/alexei-led/spotinfo)** - ⭐ 157
   CLI for exploring AWS EC2 Spot inventory. Inspect AWS Spot instance types, saving, price, and interruption frequency.

1231. **[compliant-llm](https://github.com/fiddlecube/compliant-llm)** - ⭐ 157
   Build Secure and Compliant AI agents and MCP Servers. YC W23

1232. **[superset-mcp](https://github.com/aptro/superset-mcp)** - ⭐ 157
   connect to 50+ data stores via superset mcp server. Can use with open ai agent sdk, Claude app, cursor, windsurf

1233. **[matlab-mcp-core-server](https://github.com/matlab/matlab-mcp-core-server)** - ⭐ 157
   Run MATLAB® using AI applications with the official MATLAB MCP Server from MathWorks®. This MCP server for MATLAB supports a wide range of coding agents like Claude Code® and Visual Studio® Code.

1234. **[mcp-client-slackbot](https://github.com/sooperset/mcp-client-slackbot)** - ⭐ 157
   Simple Slackbot MCP Client

1235. **[mcp-email-server](https://github.com/ai-zerolab/mcp-email-server)** - ⭐ 156
   IMAP and SMTP via MCP Server

1236. **[MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce)** - ⭐ 156
   MCP Salesforce connector

1237. **[awesome-a2a](https://github.com/pab1it0/awesome-a2a)** - ⭐ 156
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place. 

1238. **[SharpToolsMCP](https://github.com/kooshi/SharpToolsMCP)** - ⭐ 156
   A suite of MCP tools for AIs to analyze and modify C# solutions with high signal, Roslyn powered context.

1239. **[XPack-MCP-Marketplace](https://github.com/xpack-ai/XPack-MCP-Marketplace)** - ⭐ 155
   The world’s first open-source MCP monetization platform, to quickly create and sell your own MCP server in just minutes. | XPack 是全球首个开源 MCP 交易平台，帮助你在10分钟内快速搭建自己的 MCP 商店并立刻开始销售 MCP 服务。

1240. **[alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server)** - ⭐ 155

1241. **[mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed)** - ⭐ 155
   MCP server for searching and querying PubMed medical papers/research database

1242. **[mcp-server-langfuse](https://github.com/langfuse/mcp-server-langfuse)** - ⭐ 155
   Model Context Protocol (MCP) Server for Langfuse Prompt Management. This server allows you to access and manage your Langfuse prompts through the Model Context Protocol.

1243. **[metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server)** - ⭐ 155
   Model Context Protocol (MCP) to enable AI LLMs to trade using MetaTrader platform

1244. **[coolify-mcp](https://github.com/StuMason/coolify-mcp)** - ⭐ 155
   MCP server for Coolify. 35 tools for managing self-hosted PaaS through AI assistants.

1245. **[mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition)** - ⭐ 154
   MCP server providing access to the comprehensive OpenNutrition food database with 300,000+ food items, nutritional data, and barcode lookups

1246. **[python-mcp-server-client](https://github.com/GobinFan/python-mcp-server-client)** - ⭐ 154
   支持查询主流agent框架技术文档的MCP server（支持stdio和sse两种传输协议）, 支持 langchain、llama-index、autogen、agno、openai-agents-sdk、mcp-doc、camel-ai 和 crew-ai

1247. **[mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server)** - ⭐ 154
   Connects MCP to major 3D printer APIs (Orca, Bambu, OctoPrint, Klipper, Duet, Repetier, Prusa, Creality). Control prints, monitor status, and perform advanced STL operations like scaling, rotation, sectional editing, and base extension. Includes slicing and visualization.

1248. **[web3-research-mcp](https://github.com/aaronjmars/web3-research-mcp)** - ⭐ 154
   Deep Research for crypto - free & fully local

1249. **[mcp-summarizer](https://github.com/0xshellming/mcp-summarizer)** - ⭐ 153
   MCP Server for AI Summarization

1250. **[mcp-shark](https://github.com/mcp-shark/mcp-shark)** - ⭐ 153
   Wireshark-like forensic analysis for Model Context Protocol communications  Capture, inspect, and investigate all HTTP requests and responses between your IDE and MCP servers

1251. **[task-orchestrator](https://github.com/jpicklyk/task-orchestrator)** - ⭐ 153
   Persistent AI memory for coding assistants - MCP server providing context persistence across sessions for Claude, Cursor, Windsurf.  MCP Tools for task tracking, workflow automation, and AI memory. Eliminates context loss between sessions.

1252. **[mcptools](https://github.com/posit-dev/mcptools)** - ⭐ 152
   Model Context Protocol For R

1253. **[eShopLite](https://github.com/Azure-Samples/eShopLite)** - ⭐ 152
   eShopLite is a set of reference .NET applications implementing an eCommerce site with features like Semantic Search, MCP, Reasoning models and more.

1254. **[awesome-claude-dxt](https://github.com/milisp/awesome-claude-dxt)** - ⭐ 152
   Awesome Claude Desktop Extensions (dxt) (not only Claude) mcpb

1255. **[sunpeak](https://github.com/Sunpeak-AI/sunpeak)** - ⭐ 152
   Local-first ChatGPT App framework.

1256. **[strudel-mcp-server](https://github.com/williamzujkowski/strudel-mcp-server)** - ⭐ 152
   A Model Context Protocol (MCP) server that gives Claude direct control over Strudel.cc for AI-assisted music generation and live coding.

1257. **[plane-mcp-server](https://github.com/makeplane/plane-mcp-server)** - ⭐ 152
   Plane's Official Model Context Protocol Server 🔌 ⌨️ 🔥

1258. **[agentor](https://github.com/CelestoAI/agentor)** - ⭐ 152
   Fastest way to build and deploy reliable AI agents, MCP tools and  agent-to-agent. Deploy in a production ready serverless environment.

1259. **[mcp-gateway](https://github.com/lightconetech/mcp-gateway)** - ⭐ 151
   A gateway demo for MCP SSE Server

1260. **[mcp-server-metamcp](https://github.com/metatool-ai/mcp-server-metamcp)** - ⭐ 151
   MCP Server MetaMCP manages all your other MCPs in one MCP.

1261. **[mcp-server-example](https://github.com/alejandro-ao/mcp-server-example)** - ⭐ 151
   A simple MCP server to search for documentation (tutorial)

1262. **[scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server)** - ⭐ 151
   Scrapeless Mcp Server

1263. **[mcp-solver](https://github.com/szeider/mcp-solver)** - ⭐ 151
   Model Context Protocol (MCP) server for constraint optimization and solving"

1264. **[opencode-studio](https://github.com/Microck/opencode-studio)** - ⭐ 151
   web GUI for securely managing local OpenCode configuration

1265. **[instagram_dm_mcp](https://github.com/trypeggy/instagram_dm_mcp)** - ⭐ 150
   Instagram Direct messages MCP

1266. **[mcp-dotnet-samples](https://github.com/microsoft/mcp-dotnet-samples)** - ⭐ 150
   A comprehensive set of samples of creating and using MCP servers and clients with .NET

1267. **[mcp-client-go](https://github.com/yincongcyincong/mcp-client-go)** - ⭐ 150
   mcp client for Go (Golang). Integrate multiple  Model Context Protocol (MCP) servers

1268. **[AgentCrew](https://github.com/saigontechnology/AgentCrew)** - ⭐ 150
   Chat application with multi-agents system supports multi-models and MCP

1269. **[mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** - ⭐ 150
   A Model Context Protocol (MCP) server that enables AI assistants to securely interact with Odoo ERP systems through standardized resources and tools for data retrieval and manipulation.

1270. **[GEmojiSharp](https://github.com/hlaueriksson/GEmojiSharp)** - ⭐ 149
   :octocat: GitHub Emoji for C#, dotnet and beyond

1271. **[chatgpt-copilot](https://github.com/feiskyer/chatgpt-copilot)** - ⭐ 149
   ChatGPT Copilot Extension for Visual Studio Code

1272. **[make-mcp-server](https://github.com/integromat/make-mcp-server)** - ⭐ 149
   Make MCP Server

1273. **[Log-Analyzer-with-MCP](https://github.com/awslabs/Log-Analyzer-with-MCP)** - ⭐ 149
   A Model Context Protocol (MCP) server that provides AI assistants access to AWS CloudWatch Logs for analysis, searching, and correlation

1274. **[open-responses-server](https://github.com/teabranch/open-responses-server)** - ⭐ 149
   Wraps any OpenAI API interface as Responses with MCPs support so it supports Codex. Adding any missing stateful features. Ollama and Vllm compliant.

1275. **[tinymcp](https://github.com/golioth/tinymcp)** - ⭐ 148
   Let LLMs control embedded devices via the Model Context Protocol.

1276. **[MCPHub-Desktop](https://github.com/Jeamee/MCPHub-Desktop)** - ⭐ 148
   Desktop APP for Discover and Install MCP Servers

1277. **[any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp)** - ⭐ 148
   MCP Server for using any LLM as a Tool

1278. **[solana-mcp](https://github.com/sendaifun/solana-mcp)** - ⭐ 148
   A Model Context Protocol server for interacting with the Solana blockchain, powered by the Solana Agent Kit (https://github.com/sendaifun/solana-agent-kit)

1279. **[cursor-notebook-mcp](https://github.com/jbeno/cursor-notebook-mcp)** - ⭐ 148
   Model Context Protocol (MCP) server designed to allow AI agents within Cursor to interact with Jupyter Notebook (.ipynb) files

1280. **[relay](https://github.com/prism-php/relay)** - ⭐ 148
   An MCP client tool for Prism

1281. **[CreatorBox](https://github.com/xiesx123/CreatorBox)** - ⭐ 148
   🚀🎬灵活、高效、可扩展，专属剪辑配音工具箱，释放创作潜力 . Flexible, efficient, and scalable toolbox for editing and dubbing, unleashing creative potential

1282. **[In-Memoria](https://github.com/pi22by7/In-Memoria)** - ⭐ 148
   Persistent Intelligence Infrastructure for AI Agents

1283. **[osint-tools-mcp-server](https://github.com/frishtik/osint-tools-mcp-server)** - ⭐ 148
   MCP server exposing multiple OSINT tools for AI assistants like Claude

1284. **[code-assistant](https://github.com/stippi/code-assistant)** - ⭐ 148
   An LLM-powered, autonomous coding assistant. Also offers an MCP and ACP mode.

1285. **[mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server)** - ⭐ 148
   A Model Context Protocol server for MySQL database operations

1286. **[google-slides-mcp](https://github.com/matteoantoci/google-slides-mcp)** - ⭐ 148
   MCP Server for Google Slides

1287. **[medusa](https://github.com/Pantheon-Security/medusa)** - ⭐ 148
   AI-first security scanner with 74+ analyzers, 180+ AI agent security rules, intelligent false positive reduction. Supports all languages. CVE detection for React2Shell, mcp-remote RCE.

1288. **[decipher-research-agent](https://github.com/mtwn105/decipher-research-agent)** - ⭐ 147
   Turn topics, links, and files into AI-generated research notebooks — summarize, explore, and ask anything.

1289. **[autocad-mcp](https://github.com/puran-water/autocad-mcp)** - ⭐ 147
   MCP server for AutoCAD LT: AI agents translate natural language into AutoLISP code for geometry, 600+ ISA 5.1 P&ID symbols, block attributes, and layer management—generating technical drawings with 80% performance improvement via batch operations.

1290. **[website-downloader](https://github.com/pskill9/website-downloader)** - ⭐ 147
   MCP server to download entire websites

1291. **[MaxMSP-MCP-Server](https://github.com/tiianhk/MaxMSP-MCP-Server)** - ⭐ 147
   MCP (Model Context Protocol) Server for Max (Max/MSP/Jitter)

1292. **[figma-mcp-server](https://github.com/TimHolden/figma-mcp-server)** - ⭐ 146
   Model Context Protocol server implementation for Figma API

1293. **[refref](https://github.com/refrefhq/refref)** - ⭐ 146
   🌟 Open Source Referral and Affiliate Marketing Platform - Launch your referral program in minutes!

1294. **[mcp-server-gsc](https://github.com/ahonn/mcp-server-gsc)** - ⭐ 146
   A Model Context Protocol (MCP) server providing access to Google Search Console

1295. **[zabbix-mcp-server](https://github.com/mpeirone/zabbix-mcp-server)** - ⭐ 146
   🔌 Complete MCP server for Zabbix integration - Connect AI assistants to Zabbix monitoring with 40+ tools for hosts, items, triggers, templates, problems, and more. Features read-only mode and comprehensive API coverage.

1296. **[unifi-network-mcp](https://github.com/sirkirby/unifi-network-mcp)** - ⭐ 146
   MCP server implementation for the UniFi network application

1297. **[mcp-server-weread](https://github.com/ChenyqThu/mcp-server-weread)** - ⭐ 145

1298. **[ultimate_mcp_client](https://github.com/Dicklesworthstone/ultimate_mcp_client)** - ⭐ 145

1299. **[postman-mcp-server](https://github.com/delano/postman-mcp-server)** - ⭐ 145
   An MCP server that provides access to Postman.

1300. **[goku](https://github.com/jcaromiq/goku)** - ⭐ 145
   Goku is an HTTP load testing application written in Rust 

1301. **[Gemini-mcp](https://github.com/LKbaba/Gemini-mcp)** - ⭐ 145
   MCP server implementation for Google's Gemini API

1302. **[hypertool-mcp](https://github.com/toolprint/hypertool-mcp)** - ⭐ 145
   Dynamically expose tools from proxied servers based on an Agent Persona

1303. **[rust-mcp-sdk](https://github.com/rust-mcp-stack/rust-mcp-sdk)** - ⭐ 145
   A high-performance, asynchronous toolkit for building MCP servers and clients in Rust.

1304. **[uaip](https://github.com/concierge-hq/uaip)** - ⭐ 144
   Universal Agent Interactive Protocol (UAIP) is an open standard for ordered and verifiable interactions between autonomous services and AI agents.

1305. **[notion-mcp-server](https://github.com/awkoy/notion-mcp-server)** - ⭐ 144
   **Notion MCP Server** is a Model Context Protocol (MCP) server implementation that enables AI assistants to interact with Notion's API. This production-ready server provides a complete set of tools.

1306. **[seo-research-mcp](https://github.com/egebese/seo-research-mcp)** - ⭐ 144
   A free SEO research tool using Model Context Protocol (MCP) powered by Ahrefs data. Get backlink analysis, keyword research, traffic estimation, and more — directly in your AI-powered IDE.

1307. **[pubmearch](https://github.com/Darkroaster/pubmearch)** - ⭐ 144
   A PubMed MCP server.

1308. **[mcp-server-starrocks](https://github.com/StarRocks/mcp-server-starrocks)** - ⭐ 144
   StarRocks MCP (Model Context Protocol) Server

1309. **[Frappe_Assistant_Core](https://github.com/buildswithpaul/Frappe_Assistant_Core)** - ⭐ 144
   Infrastructure that connects LLMs to ERPNext. Frappe Assistant Core works with the Model Context Protocol (MCP) to expose ERPNext functionality to any compatible Language Model

1310. **[memory-graph](https://github.com/memory-graph/memory-graph)** - ⭐ 144
   A graph DB-based MCP memory server for coding agents with intelligent relationship tracking

1311. **[OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP)** - ⭐ 143
   Connect any Open Data to any LLM with Model Context Protocol.

1312. **[mcp-servers](https://github.com/charIesding/mcp-servers)** - ⭐ 143
   mcp server implementations

1313. **[quick-data-mcp](https://github.com/disler/quick-data-mcp)** - ⭐ 143
   Prompt focused MCP Server for .json and .csv agentic data analytics for Claude Code

1314. **[logfire-mcp](https://github.com/pydantic/logfire-mcp)** - ⭐ 143
   The Logfire MCP Server is here! :tada:

1315. **[mcp-discord](https://github.com/hanweg/mcp-discord)** - ⭐ 143
   MCP server for discord bot

1316. **[mcp-1panel](https://github.com/1Panel-dev/mcp-1panel)** - ⭐ 142
   mcp-1panel is an implementation of the Model Context Protocol (MCP) server for 1Panel.

1317. **[kom](https://github.com/weibaohui/kom)** - ⭐ 142
   kom 是一个用于 Kubernetes 操作的工具，SDK级的kubectl、client-go的使用封装。并且支持作为管理k8s 的 MCP server。 它提供了一系列功能来管理 Kubernetes 资源，包括创建、更新、删除和获取资源，甚至使用SQL查询k8s资源。这个项目支持多种 Kubernetes 资源类型的操作，并能够处理自定义资源定义（CRD）。 通过使用 kom，你可以轻松地进行资源的增删改查和日志获取以及操作POD内文件等动作。

1318. **[openagent](https://github.com/Th0rgal/openagent)** - ⭐ 142
   Self-hosted orchestrator for AI autonomous agents. Run Claude Code & Open Code in isolated linux workspaces. Manage your skills, configs and encrypted secrets with a git repo.

1319. **[node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp)** - ⭐ 142
   A Node.js–based Model Context Protocol server that spins up disposable Docker containers to execute arbitrary JavaScript.

1320. **[wa_llm](https://github.com/ilanbenb/wa_llm)** - ⭐ 142
   A WhatsApp bot that can participate in group conversations, powered by AI. The bot monitors group messages and responds when mentioned.

1321. **[agentql-mcp](https://github.com/tinyfish-io/agentql-mcp)** - ⭐ 142
   Model Context Protocol server that integrates AgentQL's data extraction capabilities.

1322. **[AutoRedTeam-Orchestrator](https://github.com/Coff0xc/AutoRedTeam-Orchestrator)** - ⭐ 142
   AI-Driven Automated Red Team Orchestration Framework | AI驱动的自动化红队编排框架 | 101 MCP Tools | 2000+ Payloads | Full ATT&CK Coverage | MCTS Attack Planner | Knowledge Graph | Cross-platform

1323. **[mcp-interviewer](https://github.com/microsoft/mcp-interviewer)** - ⭐ 141
   Catch MCP server issues before your agents do.

1324. **[ReActMCP](https://github.com/mshojaei77/ReActMCP)** - ⭐ 141
   ReActMCP is a reactive MCP client that empowers AI assistants to instantly respond with real-time, Markdown-formatted web search insights powered by the Exa API.

1325. **[mcp-server-calculator](https://github.com/githejie/mcp-server-calculator)** - ⭐ 141
   A Model Context Protocol server for calculating.

1326. **[powerpoint](https://github.com/supercurses/powerpoint)** - ⭐ 141
   A MCP Server for creating Powerpoint Presentations

1327. **[Polymcp](https://github.com/poly-mcp/Polymcp)** - ⭐ 141
   Polymcp provides a simple and efficient way to interact with MCP servers using custom agents

1328. **[bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js)** - ⭐ 140
   Bilibili video search MCP (Model Context Protocol) service - 哔哩哔哩视频搜索MCP服务

1329. **[intervals-mcp-server](https://github.com/mvilanova/intervals-mcp-server)** - ⭐ 140
   Model Context Protocol (MCP) server for connecting Claude and ChatGPT with the Intervals.icu API.

1330. **[systemprompt-code-orchestrator](https://github.com/systempromptio/systemprompt-code-orchestrator)** - ⭐ 140
     MCP server for orchestrating AI coding agents (Claude Code CLI & Gemini CLI). Features task management, process execution, Git integration, and dynamic resource discovery. Full TypeScript implementation with Docker support and Cloudflare Tunnel integration. 

1331. **[mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript)** - ⭐ 140
   DataForSEO API modelcontextprotocol server 

1332. **[marionette_mcp](https://github.com/leancodepl/marionette_mcp)** - ⭐ 140
   MCP server enabling AI agents to interact with Flutter apps at runtime - let them inspect widgets, simulate taps, enter text, scroll, and take screenshots.

1333. **[radare2-mcp](https://github.com/radareorg/radare2-mcp)** - ⭐ 140
   MCP stdio server for radare2

1334. **[mcp-montano-server](https://github.com/lucasmontano/mcp-montano-server)** - ⭐ 139
   Simple MCP Server Implementation

1335. **[MCP-X](https://github.com/TimeCyber/MCP-X)** - ⭐ 139
   这是一个MCP客户端，让你轻松配置各个大模型，对接各种MCP Server而开发。This is an MCP client that allows you to easily configure various large models and develop interfaces with various MCP servers.

1336. **[mcp-k8s](https://github.com/silenceper/mcp-k8s)** - ⭐ 139
   A Kubernetes MCP (Model Control Protocol) server that enables interaction with Kubernetes clusters through MCP tools.

1337. **[eion](https://github.com/eiondb/eion)** - ⭐ 139
   Shared Memory Storage for Multi-Agent Systems

1338. **[mssql-mcp](https://github.com/Aaronontheweb/mssql-mcp)** - ⭐ 139
   MSSQL Server MCP implementation written in C#

1339. **[forgetful](https://github.com/ScottRBK/forgetful)** - ⭐ 139
   Opensource Memory for Agents

1340. **[frontmcp](https://github.com/agentfront/frontmcp)** - ⭐ 138
   TypeScript-first framework for the Model Context Protocol (MCP). You write clean, typed code; FrontMCP handles the protocol, transport, DI, session/auth, and execution flow.

1341. **[graphiti-mcp-server](https://github.com/gifflet/graphiti-mcp-server)** - ⭐ 138
   Graphiti MCP Server

1342. **[backlog-mcp-server](https://github.com/nulab/backlog-mcp-server)** - ⭐ 138

1343. **[guidance-for-deploying-model-context-protocol-servers-on-aws](https://github.com/aws-solutions-library-samples/guidance-for-deploying-model-context-protocol-servers-on-aws)** - ⭐ 138
   This Guidance demonstrates how to securely run Model Context Protocol (MCP) servers on the AWS Cloud using containerized architecture. It helps organizations implement industry-standard OAuth 2.0 authentication while protecting server deployments with multiple security layers, including content delivery networks and web application firewalls. 

1344. **[k8s-mcp-server](https://github.com/reza-gholizade/k8s-mcp-server)** - ⭐ 138
   Manage Your Kubernetes Cluster with k8s mcp-server

1345. **[drawio2go](https://github.com/Menghuan1918/drawio2go)** - ⭐ 138
   A modern DrawIO editor application.  AI-Powered, Human-AI Collaboration | AI 加持，人机共绘drawio

1346. **[datagov-mcp](https://github.com/aviveldan/datagov-mcp)** - ⭐ 137
   MCP server for Israel Government Data

1347. **[SecureMCP](https://github.com/makalin/SecureMCP)** - ⭐ 137
   SecureMCP is a security auditing tool designed to detect vulnerabilities and misconfigurations in applications using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction). It proactively identifies threats like OAuth token leakage, prompt injection vulnerabilities, rogue MCP servers, and tool poisoning attacks.

1348. **[doc-ops-mcp](https://github.com/Tele-AI/doc-ops-mcp)** - ⭐ 137
   MCP server for seamless document format conversion and processing

1349. **[ghost-mcp](https://github.com/MFYDev/ghost-mcp)** - ⭐ 137
   A Model Context Protocol (MCP) server for interacting with Ghost CMS through LLM interfaces like Claude. Allow you to control your Ghost blog by simply asking Claude etc.

1350. **[mcp-server-manifest](https://github.com/Zomato/mcp-server-manifest)** - ⭐ 137

1351. **[mcp-server-serper](https://github.com/marcopesani/mcp-server-serper)** - ⭐ 137
   Serper MCP Server supporting search and webpage scraping

1352. **[agent-toolkit](https://github.com/datacommonsorg/agent-toolkit)** - ⭐ 136
   Tools and agents for interacting with the Data Commons Knowledge Graph using the Model Context Protocol (MCP).

1353. **[ultimate_mcp_server](https://github.com/Dicklesworthstone/ultimate_mcp_server)** - ⭐ 136
   The Ultimate Model Context Protocol (MCP) Server, providing unified access to a wide variety of useful and powerful tools.

1354. **[hayhooks](https://github.com/deepset-ai/hayhooks)** - ⭐ 136
   Easily deploy Haystack pipelines as REST APIs and MCP Tools.

1355. **[MCP-PostgreSQL-Ops](https://github.com/call518/MCP-PostgreSQL-Ops)** - ⭐ 136
   🔍Professional MCP server for PostgreSQL operations & monitoring: 30+ extension-independent tools for performance analysis, table bloat detection, autovacuum monitoring, schema introspection, and database management. Supports PostgreSQL 12-17.

1356. **[zettelkasten-mcp](https://github.com/entanglr/zettelkasten-mcp)** - ⭐ 136
   A Model Context Protocol (MCP) server that implements the Zettelkasten knowledge management methodology, allowing you to create, link, explore and synthesize atomic notes through Claude and other MCP-compatible clients.

1357. **[freecad_mcp](https://github.com/bonninr/freecad_mcp)** - ⭐ 136
   FreecadMCP connects Freecad to Claude AI and other MCP-ready tools like Cursor through the Model Context Protocol (MCP), allowing Claude to directly interact with and control Freecad. This integration enables prompt assisted CAD 3d Design.

1358. **[uLoopMCP](https://github.com/hatayama/uLoopMCP)** - ⭐ 136
   Your Unity project's AI autopilot. Compile, test, debug, repeat—until it just works.

1359. **[dedalus-mcp-python](https://github.com/dedalus-labs/dedalus-mcp-python)** - ⭐ 136
   A simple and performant Model Context Protocol framework for Python.

1360. **[OmniFocus-MCP](https://github.com/themotionmachine/OmniFocus-MCP)** - ⭐ 135
   Let LLMs interface with your tasks and projects through the Model Context Protocol. Add, organize, and query your OmniFocus database with natural language commands.

1361. **[LMStudio-MCP](https://github.com/infinitimeless/LMStudio-MCP)** - ⭐ 135
   A Model Control Protocol (MCP) server that allows Claude to communicate with locally running LLM models via LM Studio.

1362. **[Human-In-the-Loop-MCP-Server](https://github.com/GongRzhe/Human-In-the-Loop-MCP-Server)** - ⭐ 135
   A powerful MCP Server that enables AI assistants like Claude to interact with humans through intuitive GUI dialogs. This server bridges the gap between automated AI processes and human decision-making by providing real-time user input tools, choices, confirmations, and feedback mechanisms.

1363. **[mkinf](https://github.com/mkinf-io/mkinf)** - ⭐ 134
   mkinf SDK to interact with mkinf hub MCP servers

1364. **[mcp-server-reddit](https://github.com/Hawstein/mcp-server-reddit)** - ⭐ 134
   A Model Context Protocol (MCP) server that provides tools for fetching Reddit content, including frontpage posts, subreddit information and hot posts, post details, and comments.

1365. **[mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow)** - ⭐ 134

1366. **[xhs-mcp-server](https://github.com/aicu-icu/xhs-mcp-server)** - ⭐ 133
   小红书MCP服务器 | 基于Electron+小红书Web API。一键安装运行、极速抓取笔记、评论、用户等数据并让AI智能分析、整理与导出

1367. **[Multi-Source-Media-MCP-Server](https://github.com/Decade-qiu/Multi-Source-Media-MCP-Server)** - ⭐ 133
   An MCP Tool Implementation for Multi-Source Image Access & Generation

1368. **[Awesome-MCP](https://github.com/AlexMili/Awesome-MCP)** - ⭐ 133
   Awesome ModelContextProtocol resources - A curated list of MCP resources

1369. **[mcp-think-tool](https://github.com/DannyMac180/mcp-think-tool)** - ⭐ 133
   An MCP server implementing the think tool for Claude

1370. **[Gitingest-MCP](https://github.com/puravparab/Gitingest-MCP)** - ⭐ 133
   mcp server for gitingest

1371. **[ollama-mcp](https://github.com/rawveg/ollama-mcp)** - ⭐ 133
   An MCP Server for Ollama

1372. **[mcp-rubber-duck](https://github.com/nesquikm/mcp-rubber-duck)** - ⭐ 133
   An MCP server that acts as a bridge to query multiple OpenAI-compatible LLMs with MCP tool access. Just like rubber duck debugging, explain your problems to various AI "ducks" who can actually research and get different perspectives!

1373. **[aicode-toolkit](https://github.com/AgiFlow/aicode-toolkit)** - ⭐ 133
   Toolkit for Coding Agents to work reliably with repo of any size.

1374. **[A2A-MCP-Server](https://github.com/GongRzhe/A2A-MCP-Server)** - ⭐ 133
   A mcp server that bridges the Model Context Protocol (MCP) with the Agent-to-Agent (A2A) protocol, enabling MCP-compatible AI assistants (like Claude) to seamlessly interact with A2A agents.

1375. **[claude-prompts](https://github.com/minipuft/claude-prompts)** - ⭐ 133
   MCP prompt template server: hot-reload, thinking frameworks, quality gates

1376. **[mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server)** - ⭐ 132
   A Model Context Protocol (MCP) server that provides secure, read-only access to BigQuery datasets. Enables Large Language Models (LLMs) to safely query and analyze data through a standardized interface.

1377. **[mcp-server-macos-use](https://github.com/mediar-ai/mcp-server-macos-use)** - ⭐ 132
   AI agent that controls computer with OS-level tools, MCP compatible, works with any model

1378. **[mcp-chat](https://github.com/Flux159/mcp-chat)** - ⭐ 132
   Open Source Generic MCP Client for testing & evaluating mcp servers and agents

1379. **[mcp-gateway](https://github.com/acehoss/mcp-gateway)** - ⭐ 132
   A flexible gateway server that bridges Model Context Protocol (MCP) STDIO servers to MCP HTTP+SSE and REST API, enabling multi-instance MCP servers to be exposed over HTTP.

1380. **[esp-mcp](https://github.com/horw/esp-mcp)** - ⭐ 132
   Centralize ESP32 related commands and simplify getting started with seamless, LLM-driven interaction and help.

1381. **[aleph](https://github.com/Hmbown/aleph)** - ⭐ 132
   Skill + MCP server for recursive LLM reasoning. Load context, iterate with search/code/think tools, converge on answers.

1382. **[ragrabbit](https://github.com/madarco/ragrabbit)** - ⭐ 131
   Open Source, Self-Hosted, AI Search and LLM.txt for your website

1383. **[jupyter-ai-agents](https://github.com/datalayer/jupyter-ai-agents)** - ⭐ 131
   🪐 🤖 AI Agents for JupyterLab with 🔧 MCP tools - Chat interface for optimized notebook interaction and code execution.

1384. **[play-store-mcp](https://github.com/antoniolg/play-store-mcp)** - ⭐ 131
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1385. **[mcp-crash-course](https://github.com/emarco177/mcp-crash-course)** - ⭐ 131
   Hands-on crash course for the Model Context Protocol (MCP) with project-based branches on Streamable-HTTP, LangChain adapters, and Docker.

1386. **[codeql-mcp](https://github.com/JordyZomer/codeql-mcp)** - ⭐ 131
   This project runs a Model Context Protocol (MCP) server that wraps the CodeQL query server. It enables tools like [Cursor](https://cursor.sh/) or AI agents to interact with CodeQL through structured commands.

1387. **[N8N2MCP](https://github.com/Super-Chain/N8N2MCP)** - ⭐ 131
   Convert N8N agent / workflow into MCP servers, you can use it in Claude / Cursor / Super Chain 

1388. **[mcp-read-website-fast](https://github.com/just-every/mcp-read-website-fast)** - ⭐ 130
   Quickly reads webpages and converts to markdown for fast, token efficient web scraping

1389. **[zotero-mcp](https://github.com/kujenga/zotero-mcp)** - ⭐ 130
   Model Context Protocol (MCP) server for the Zotero API, in Python

1390. **[mcp_server_exe](https://github.com/shadowcz007/mcp_server_exe)** - ⭐ 130
   小智 & Cursor 的 MCP 启动器 - MCP For Cursor&xiaozhi。打包成可执行文件。Turn MCP server into an executable file

1391. **[codex-mcp-server](https://github.com/cexll/codex-mcp-server)** - ⭐ 130
   Codex Mcp Server 

1392. **[dify-plugin-agent-mcp_sse](https://github.com/junjiem/dify-plugin-agent-mcp_sse)** - ⭐ 129
   Dify 1.0 Plugin Support MCP Tools Agent strategies

1393. **[mcpd](https://github.com/mozilla-ai/mcpd)** - ⭐ 129
   Declaratively define and run required tools across environments, from local development to containerized cloud deployments.

1394. **[crawl4ai-mcp-server](https://github.com/weidwonder/crawl4ai-mcp-server)** - ⭐ 129
   用于提供给本地开发者的 LLM的高效互联网搜索&内容获取的MCP Server， 节省你的token

1395. **[zig-mcp](https://github.com/zig-wasm/zig-mcp)** - ⭐ 129
   Model Context Protocol (MCP) server that provides up-to-date documentation for the Zig programming language standard library and builtin functions

1396. **[ksail](https://github.com/devantler-tech/ksail)** - ⭐ 129
   Tool for creating, maintaining and operating Kubernetes clusters with ease.

1397. **[unreal-analyzer-mcp](https://github.com/ayeletstudioindia/unreal-analyzer-mcp)** - ⭐ 129
   MCP server for Unreal Engine 5

1398. **[awesome-crypto-mcp-servers](https://github.com/badkk/awesome-crypto-mcp-servers)** - ⭐ 128
   A collection of crypto MCP servers.

1399. **[aws-cost-explorer-mcp-server](https://github.com/aarora79/aws-cost-explorer-mcp-server)** - ⭐ 128
   MCP server for understanding AWS spend

1400. **[mcp-server-aws](https://github.com/rishikavikondala/mcp-server-aws)** - ⭐ 128
   A Model Context Protocol server implementation for operations on AWS resources

1401. **[magg](https://github.com/sitbon/magg)** - ⭐ 128
   Magg: The MCP Aggregator

1402. **[beyond-mcp](https://github.com/disler/beyond-mcp)** - ⭐ 128
   It's time to push beyond MCP Servers... Right?

1403. **[ChatPPT-MCP](https://github.com/YOOTeam/ChatPPT-MCP)** - ⭐ 128
   The AI-powered PPT generation service based on ChatPPT can create presentations based on themes, requirements, or uploaded documents, supporting online editing and downloading.基于chatppt进行的AI PPT生成服务，可以满足基于主题或者要求、以及上传文档进行生成ppt，以及美化换模板、修改配色字体等，支持在线编辑与下载。

1404. **[mcp-apache-spark-history-server](https://github.com/kubeflow/mcp-apache-spark-history-server)** - ⭐ 128
   MCP Server for Apache Spark History Server. The bridge between Agentic AI and Apache Spark.

1405. **[mcp-server-plugin](https://github.com/JetBrains/mcp-server-plugin)** - ⭐ 127
   JetBrains MCP Server Plugin

1406. **[laravel-loop](https://github.com/kirschbaum-development/laravel-loop)** - ⭐ 127
   Laravel Loop is a powerful Model Context Protocol (MCP) server designed specifically for Laravel applications. It connects your Laravel application with AI assistants using the MCP protocol.

1407. **[paiml-mcp-agent-toolkit](https://github.com/paiml/paiml-mcp-agent-toolkit)** - ⭐ 127
   Pragmatic AI Labs MCP Agent Toolkit - An MCP Server designed to make code with agents more deterministic

1408. **[mcp-endpoint-server](https://github.com/xinnan-tech/mcp-endpoint-server)** - ⭐ 127
   xiaozhi mcp接入点服务器，用于自定义mcp服务注册，方便拓展小智服务端工具调用

1409. **[mcp-server](https://github.com/browserstack/mcp-server)** - ⭐ 127
   BrowserStack's Official MCP Server

1410. **[rust-mcp-filesystem](https://github.com/rust-mcp-stack/rust-mcp-filesystem)** - ⭐ 127
   Blazing-fast, asynchronous MCP server for seamless filesystem operations.

1411. **[tabularis](https://github.com/debba/tabularis)** - ⭐ 127
   A lightweight, developer-focused database management tool

1412. **[dart-mcp-server](https://github.com/its-dart/dart-mcp-server)** - ⭐ 126
   Dart AI Model Context Protocol (MCP) server

1413. **[think-mcp-server](https://github.com/PhillipRt/think-mcp-server)** - ⭐ 126

1414. **[claude-prompts-mcp](https://github.com/minipuft/claude-prompts-mcp)** - ⭐ 126
   MCP prompt template server: hot-reload, thinking frameworks, quality gates

1415. **[specs-workflow-mcp](https://github.com/kingkongshot/specs-workflow-mcp)** - ⭐ 126
   Intelligent spec workflow management MCP server

1416. **[mcp-server-ccxt](https://github.com/doggybee/mcp-server-ccxt)** - ⭐ 126
   High-performance CCXT MCP server for cryptocurrency exchange integration

1417. **[ZotLink](https://github.com/TonybotNi/ZotLink)** - ⭐ 126
   Production‑ready MCP server for Zotero to save open preprints (arXiv, CVF, bio/med/chemRxiv) with rich metadata and smart PDF attachments — with upcoming support for publisher databases (Nature, Science, IEEE Xplore, Springer).

1418. **[mcp](https://github.com/MariaDB/mcp)** - ⭐ 125
   MariaDB MCP (Model Context Protocol) server implementation

1419. **[tiktok-mcp](https://github.com/Seym0n/tiktok-mcp)** - ⭐ 125
   Model Context Protocol (MCP) with TikTok integration

1420. **[play-store-mcp](https://github.com/devexpert-io/play-store-mcp)** - ⭐ 125
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1421. **[mcp-evals](https://github.com/mclenhard/mcp-evals)** - ⭐ 125
   A Node.js package and GitHub Action for evaluating MCP (Model Context Protocol) tool implementations using LLM-based scoring. This helps ensure your MCP server's tools are working correctly and performing well.

1422. **[mcp-streamable-http](https://github.com/invariantlabs-ai/mcp-streamable-http)** - ⭐ 125
   Example implementation of MCP Streamable HTTP client/server in Python and TypeScript.

1423. **[mcp-server-datadog](https://github.com/winor30/mcp-server-datadog)** - ⭐ 125

1424. **[paperless-mcp](https://github.com/nloui/paperless-mcp)** - ⭐ 125
   An MCP (Model Context Protocol) server for interacting with a Paperless-NGX API server. This server provides tools for managing documents, tags, correspondents, and document types in your Paperless-NGX instance.

1425. **[shopify-mcp](https://github.com/GeLi2001/shopify-mcp)** - ⭐ 125
   MCP server for Shopify api, usable on mcp hosts such as Claude and Cursor

1426. **[seline](https://github.com/tercumantanumut/seline)** - ⭐ 125
   seline agent with a style

1427. **[gemini-mcp](https://github.com/RLabs-Inc/gemini-mcp)** - ⭐ 125
   MCP Server that enables Claude code to interact with Gemini

1428. **[data-go-mcp-servers](https://github.com/Koomook/data-go-mcp-servers)** - ⭐ 125
   Korea public data portal (data.go.kr) API MCP servers

1429. **[mcp-client-server](https://github.com/willccbb/mcp-client-server)** - ⭐ 124
   An MCP Server that's also an MCP Client. Useful for letting Claude develop and test MCPs without needing to reset the application.

1430. **[mcp-linear](https://github.com/tacticlaunch/mcp-linear)** - ⭐ 124
   MCP server that enables AI assistants to interact with Linear project management system through natural language, allowing users to retrieve, create, and update issues, projects, and teams.

1431. **[buttplug-mcp](https://github.com/ConAcademy/buttplug-mcp)** - ⭐ 124
   Buttplug.io Model Context Protocol (MCP) Server

1432. **[kindly-web-search-mcp-server](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server)** - ⭐ 124
   Kindly Web Search MCP Server: Web search + robust content retrieval for AI coding tools (Claude Code, Codex, Cursor, GitHub Copilot, Gemini, etc.). Supports Serper, Tavily, and SearXNG.

1433. **[computer-use-mcp](https://github.com/domdomegg/computer-use-mcp)** - ⭐ 124
   💻 Give AI models complete control of your computer (probably a bad idea)

1434. **[mcp-redmine](https://github.com/runekaagaard/mcp-redmine)** - ⭐ 124
   A redmine MCP server covering close to 100% of redmines API

1435. **[mcp](https://github.com/pronskiy/mcp)** - ⭐ 123
   🐉 The fast, PHP way to build MCP servers

1436. **[mcp-svelte-docs](https://github.com/spences10/mcp-svelte-docs)** - ⭐ 123
   🔍 MCP server that lets you search and access Svelte documentation with built-in caching

1437. **[linear-mcp](https://github.com/cline/linear-mcp)** - ⭐ 123
   a private MCP server for accessing Linear

1438. **[aws-lambda-mcp-cookbook](https://github.com/ran-isenberg/aws-lambda-mcp-cookbook)** - ⭐ 123
   This repository provides a working, deployable, open source-based, serverless MCP server blueprint with an AWS Lambda function and AWS CDK Python code with all the best practices and a complete CI/CD pipeline.

1439. **[MakerAi](https://github.com/gustavoeenriquez/MakerAi)** - ⭐ 123
   The AI Operating System for Delphi. 100% native framework with RAG 2.0 for knowledge retrieval, autonomous agents with semantic memory, visual workflow orchestration, and universal LLM connector. Supports OpenAI, Claude, Gemini, Ollama, and more. Enterprise-grade AI for Delphi 10.3+

1440. **[NornicDB](https://github.com/orneryd/NornicDB)** - ⭐ 123
   NornicDB is a high-performance graph + vector database built for AI agents and knowledge systems. It speaks Neo4j's (Bolt + Cypher) and qdrant's (gRPC) languages so you can use Nornic with zero code changes, while adding intelligent features including a graphql endpoint, air-gapped embeddings, GPU accelerated search, and other intelligent features.

1441. **[robloxstudio-mcp](https://github.com/boshyxd/robloxstudio-mcp)** - ⭐ 123
   Create agentic AI workflows in ROBLOX Studio

1442. **[openapi](https://github.com/samchon/openapi)** - ⭐ 122
   OpenAPI definitions, converters and LLM function calling schema composer.

1443. **[mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery)** - ⭐ 122
   A Model Context Protocol server that provides access to BigQuery

1444. **[mevzuat-mcp](https://github.com/saidsurucu/mevzuat-mcp)** - ⭐ 122
   MCP Server for Searching Turkish Legislation

1445. **[laravel-toon](https://github.com/mischasigtermans/laravel-toon)** - ⭐ 122
   TOON encoding for Laravel. Encode data for AI/LLMs with ~50% fewer tokens than JSON.

1446. **[isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp)** - ⭐ 122
   Isaac Simulation MCP Extension and Server

1447. **[muppet](https://github.com/muppet-dev/muppet)** - ⭐ 121
   MCP Servers SDK for TypeScript

1448. **[mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce)** - ⭐ 121
   Salesforce MCP Server

1449. **[mcp-watch](https://github.com/kapilduraphe/mcp-watch)** - ⭐ 121
   A comprehensive security scanner for Model Context Protocol (MCP) servers that detects vulnerabilities and security issues in your MCP server implementations.

1450. **[anki-mcp-server](https://github.com/ankimcp/anki-mcp-server)** - ⭐ 121
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Anki, the spaced repetition flashcard application.

1451. **[mcp-package-version](https://github.com/sammcj/mcp-package-version)** - ⭐ 120
   An MCP server that provides LLMs with the latest stable package versions when coding

1452. **[ffmpeg-mcp](https://github.com/egoist/ffmpeg-mcp)** - ⭐ 120
   An MCP server for FFmpeg

1453. **[mcp-devtools](https://github.com/sammcj/mcp-devtools)** - ⭐ 120
   A modular MCP server that provides commonly used developer tools for AI coding agents

1454. **[easy-code-reader](https://github.com/FangYuan33/easy-code-reader)** - ⭐ 120
   A powerful MCP (Model Context Protocol) server for intelligently reading Java source code.

1455. **[mcp-glootie](https://github.com/AnEntrypoint/mcp-glootie)** - ⭐ 120
   wanna develop an app ❓

1456. **[n8n-mcp-server](https://github.com/illuminaresolutions/n8n-mcp-server)** - ⭐ 120
   MCP server implementation for n8n workflow automation

1457. **[mcp-victoriametrics](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics)** - ⭐ 120
   The implementation of Model Context Protocol (MCP) server for VictoriaMetrics

1458. **[UnityMCP](https://github.com/isuzu-shiranui/UnityMCP)** - ⭐ 119
   Unity Editor integration with Model Context Protocol (MCP) enabling AI assistants like Claude to interact with Unity projects. Features a TypeScript MCP server and C# Unity plugin with extensible command handler architecture, TCP/IP communication, and dynamic plugin discovery.

1459. **[jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp)** - ⭐ 119
   A Model Context Protocol (MCP) for Jupyter Notebook

1460. **[hub-mcp](https://github.com/docker/hub-mcp)** - ⭐ 119
   Docker Hub MCP Server

1461. **[turbo-flow-claude](https://github.com/marcuspat/turbo-flow-claude)** - ⭐ 119
   Advanced Agentic Development Environment Supporting Devpods, Rackspace Spot Instances, Github Codespaces, Google Cloud Shell, and more!  Features 600+ AI agents, Claude Flow, SPARC methodology, and automatic context loading! Deploy intelligent multi-agent swarms, coordinate autonomous workflows.

1462. **[OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server)** - ⭐ 119
   Devin's attempt at creating an OpenSCAD MCP Server that takes a user prompt and generates a preview image and 3d file.

1463. **[mcpproxy-go](https://github.com/smart-mcp-proxy/mcpproxy-go)** - ⭐ 119
   Supercharge AI Agents, Safely

1464. **[mcp-bsl-platform-context](https://github.com/alkoleft/mcp-bsl-platform-context)** - ⭐ 119
   MCP сервер для AI-ассистентов (справка по синтаксису и объектной модели 1С:Предприятие)

1465. **[memov](https://github.com/memovai/memov)** - ⭐ 119
   Give git-like & traceable memory to any coding agents and OpenClaw(Moltbot, Clawdbot). By https://memov.ai/

1466. **[remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)** - ⭐ 118
   This is a quickstart template to easily build and deploy a custom remote MCP server to the cloud using Azure functions. You can clone/restore/run on your local machine with debugging, and `azd up` to have it in the cloud in a couple minutes.  The MCP server is secured by design using 

1467. **[memorizer-v1](https://github.com/petabridge/memorizer-v1)** - ⭐ 118
   Vector-search powered agent memory MCP server

1468. **[VisionCraft-MCP-Server](https://github.com/augmentedstartups/VisionCraft-MCP-Server)** - ⭐ 118
   VisionCraft MCP delivers up-to-date, specialized computer vision and Gen-AI knowledge directly to Claude and other AI assistants.

1469. **[mcp-mianshiya-server](https://github.com/yuyuanweb/mcp-mianshiya-server)** - ⭐ 118
   基于 Spring AI 的面试鸭搜索题目的 MCP Server 服务，快速让 AI 搜索企业面试真题和答案

1470. **[MCP-Workspace-Server](https://github.com/answerlink/MCP-Workspace-Server)** - ⭐ 118
   🚀 Beyond Filesystem - Complete AI Development Environment - One MCP Server provides full Agent capability stack: web development, code execution, data processing, image generation. No need for multiple tools, configure once. Perfect support for Dify, FastGPT, Cherry Studio.       文件操作、Python/Node.js 代码执行、Web 应用一键部署（支持泛域名）、Excel 处理、图像生成。开箱即用

1471. **[nextcloud-mcp-server](https://github.com/cbcoutinho/nextcloud-mcp-server)** - ⭐ 118
   Nextcloud MCP Server

1472. **[paperbanana](https://github.com/llmsresearch/paperbanana)** - ⭐ 118
   Open source implementation and extension of Google Research’s PaperBanana for automated academic figures, diagrams, and research visuals, expanded to new domains like slide generation.

1473. **[memorizer](https://github.com/petabridge/memorizer)** - ⭐ 118
   Vector-search powered agent memory MCP server

1474. **[elevenlabs-mcp-server](https://github.com/mamertofabian/elevenlabs-mcp-server)** - ⭐ 117

1475. **[mcp-server-asana](https://github.com/roychri/mcp-server-asana)** - ⭐ 117

1476. **[aseprite-mcp](https://github.com/diivi/aseprite-mcp)** - ⭐ 117
   MCP server for interacting with the Aseprite API

1477. **[FirstData](https://github.com/MLT-OSS/FirstData)** - ⭐ 117
   The World's Most Comprehensive, Authoritative, and Structured Open Source Data Source Knowledge Base

1478. **[raindrop-mcp](https://github.com/adeze/raindrop-mcp)** - ⭐ 117
   Raindrop MCP Server

1479. **[SmartDB_MCP](https://github.com/wenb1n-dev/SmartDB_MCP)** - ⭐ 116
   Universal database MCP server connecting to MySQL, PostgreSQL, SQL Server, MariaDB,DM8,Oracle,not only provides basic database connection such as OAuth 2.0 authentication , health checks, SQL optimization, and index health detection

1480. **[google-workspace-mcp](https://github.com/aaronsb/google-workspace-mcp)** - ⭐ 116
   A Model Context Protocol (MCP) server that provides authenticated access to Google Workspace APIs, offering integrated Authentication, Gmail, Calendar, and Drive functionality

1481. **[railway-mcp-server](https://github.com/railwayapp/railway-mcp-server)** - ⭐ 116
   Official Railway MCP Server for interacting with your Railway account

1482. **[mcp-ts-template](https://github.com/cyanheads/mcp-ts-template)** - ⭐ 116
   Production-grade TypeScript template for Model Context Protocol (MCP) servers. Ships with declarative tools/resources, robust error handling, DI, easy auth, optional OpenTelemetry, and first-class support for both local and edge (Cloudflare Workers) runtimes.

1483. **[Wazuh-MCP-Server](https://github.com/gensecaihq/Wazuh-MCP-Server)** - ⭐ 116
    AI-powered security operations with Wazuh SIEM + Claude Desktop. Natural language threat detection, automated incident response & compliance. Real-time monitoring, ML anomaly detection. Transform your SOC with conversational security analysis. Production-ready MCP server.

1484. **[web-scout-mcp](https://github.com/pinkpixel-dev/web-scout-mcp)** - ⭐ 116
   A powerful MCP server extension providing web search and content extraction capabilities. Integrates DuckDuckGo search functionality and URL content extraction into your MCP environment, enabling AI assistants to search the web and extract webpage content programmatically.

1485. **[cloudflare-mcp](https://github.com/mattzcarey/cloudflare-mcp)** - ⭐ 116
   unofficial mcp server for cloudflare api

1486. **[kodit](https://github.com/helixml/kodit)** - ⭐ 115
   👩‍💻 MCP server to index external repositories

1487. **[mcp_proxy_rust](https://github.com/tidewave-ai/mcp_proxy_rust)** - ⭐ 115
   A proxy to use HTTP/SSE MCPs from STDIO clients

1488. **[SwiftMCP](https://github.com/Cocoanetics/SwiftMCP)** - ⭐ 115
   Model Context Protocol Server for Swift

1489. **[Hegelion](https://github.com/Hmbown/Hegelion)** - ⭐ 115
   Dialectical reasoning architecture for LLMs (Thesis → Antithesis → Synthesis)

1490. **[Easy-MCP-AutoCad](https://github.com/zh19980811/Easy-MCP-AutoCad)** - ⭐ 115
   这个项目是一个基于Model Context Protocol (MCP)的AutoCAD集成服务器，它允许通过自然语言与AutoCAD进行交互。通过这个服务器，用户可以使用Claude等大型语言模型来创建、修改和分析AutoCAD图纸，同时还可以存储和查询CAD元素的相关数据。目前制作参考学习，仅实现端到端之间的通信，具体工具函数尚未晚上

1491. **[teslamate-mcp](https://github.com/cobanov/teslamate-mcp)** - ⭐ 115
   A Model Context Protocol (MCP) server that provides access to your TeslaMate database, allowing AI assistants to query Tesla vehicle data and analytics.

1492. **[mcp-server](https://github.com/bitwarden/mcp-server)** - ⭐ 115
   MCP server for interaction with Bitwarden.

1493. **[ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp)** - ⭐ 115
   Using ffmpeg command line to achieve an mcp server, can be very convenient, through the dialogue to achieve the local video search, tailoring, stitching, playback,clip, overlay, concat and other functions

1494. **[netbox-mcp-server](https://github.com/netboxlabs/netbox-mcp-server)** - ⭐ 115
   Model Context Protocol (MCP) server for read-only interaction with NetBox data in LLMs

1495. **[-mcp-to-skill-converter](https://github.com/GBSOSS/-mcp-to-skill-converter)** - ⭐ 115
      Convert any MCP server into a Claude Skill with 90% context savings

1496. **[MCppServer](https://github.com/Noeli14/MCppServer)** - ⭐ 114
   Fast and super efficient Minecraft Server written in C++

1497. **[mcp-server](https://github.com/InterviewReady/mcp-server)** - ⭐ 114
   An MCP server for InterviewReady

1498. **[mcp-memory](https://github.com/Puliczek/mcp-memory)** - ⭐ 114
   🔥🖥️ MCP Memory is a MCP Server that gives MCP Clients (Cursor, Claude, Windsurf and more) the ability to remember information about users (preferences, behaviors) across conversations.

1499. **[iphone-mcp](https://github.com/Lakr233/iphone-mcp)** - ⭐ 114
   A Model Context Protocol (MCP) server for automating iPhone tasks with Appium. Supports app control, UI interactions, and screenshot capture via streamable HTTP.

1500. **[mcp-hubspot](https://github.com/peakmojo/mcp-hubspot)** - ⭐ 114
   A Model Context Protocol (MCP) server that enables AI assistants to interact with HubSpot CRM data, providing built-in vector storage and caching mechanisms help overcome HubSpot API limitations while improving response times.

1501. **[polymarket-mcp](https://github.com/berlinbra/polymarket-mcp)** - ⭐ 114
   MCP Server for PolyMarket API

1502. **[pentest-mcp](https://github.com/DMontgomery40/pentest-mcp)** - ⭐ 114
   NOT for educational purposes: An MCP server for professional penetration testers including STDIO/HTTP/SSE support, nmap, go/dirbuster, nikto, JtR, hashcat, wordlist building, and more.

1503. **[comet-mcp](https://github.com/hanzili/comet-mcp)** - ⭐ 114
   MCP Server connecting to Perplexity Comet browser

1504. **[cli](https://github.com/mcpgod/cli)** - ⭐ 113
   Fine-grained control over model context protocol (MCP) clients, servers, and tools. Context is God.

1505. **[remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)** - ⭐ 113
   Azure API Management as AI Gateway to Remote MCP servers.

1506. **[MCP-oura](https://github.com/YuzeHao2023/MCP-oura)** - ⭐ 113
   MCP server for Oura API integration

1507. **[xcodeproj-mcp-server](https://github.com/giginet/xcodeproj-mcp-server)** - ⭐ 113
   A Model Context Protocol Server to manipulate *.xcodeproj

1508. **[swagger-mcp](https://github.com/dcolley/swagger-mcp)** - ⭐ 113
   Swagger to MCP server

1509. **[server-google-news](https://github.com/ChanMeng666/server-google-news)** - ⭐ 113
   【Star-crossed coders unite!⭐️】Model Context Protocol (MCP) server implementation providing Google News search capabilities via SerpAPI, with automatic news categorization and multi-language support.

1510. **[google-sheets-mcp](https://github.com/mkummer225/google-sheets-mcp)** - ⭐ 113
   Google Sheets MCP Server 📊🤖

1511. **[foxy-contexts](https://github.com/strowk/foxy-contexts)** - ⭐ 113
   Foxy contexts is a library for building context servers supporting Model Context Protocol

1512. **[swiftlens](https://github.com/swiftlens/swiftlens)** - ⭐ 113
   SwiftLens is a Model Context Protocol (MCP) server that provides deep, semantic-level analysis of Swift codebases to any AI models. By integrating directly with Apple's SourceKit-LSP, SwiftLens enables AI models to understand Swift code with compiler-grade accuracy.

1513. **[computer-control-mcp](https://github.com/AB498/computer-control-mcp)** - ⭐ 113
   MCP server that provides computer control capabilities, like mouse, keyboard, OCR, etc. using PyAutoGUI, RapidOCR, ONNXRuntime. Similar to 'computer-use' by Anthropic. With Zero External Dependencies.

1514. **[portainer-mcp](https://github.com/portainer/portainer-mcp)** - ⭐ 113
   Portainer MCP server

1515. **[remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python)** - ⭐ 112
   Getting Started with Remote MCP Servers using Azure Functions (Python)

1516. **[exstruct](https://github.com/harumiWeb/exstruct)** - ⭐ 112
   Excel to structured JSON (tables, shapes, charts) for LLM/RAG pipelines

1517. **[crypto-indicators-mcp](https://github.com/kukapay/crypto-indicators-mcp)** - ⭐ 112
   An MCP server providing a range of cryptocurrency technical analysis indicators and strategies.

1518. **[ableton-mcp-extended](https://github.com/uisato/ableton-mcp-extended)** - ⭐ 112
   Ableton Live MCP (Model Context Protocol) server that allows control directly through AI assistants.

1519. **[MCP2Lambda](https://github.com/danilop/MCP2Lambda)** - ⭐ 111
   Run any AWS Lambda function as a Large Language Model (LLM) tool without code changes using Anthropic's Model Context Protocol (MCP).

1520. **[notion-mcp](https://github.com/ccabanillas/notion-mcp)** - ⭐ 111
   A Model Context Protocol (MCP) server implementation for Notion integration, providing a standardized interface for interacting with Notion's API.

1521. **[punkpeye_awesome-mcp-servers](https://github.com/MCP-Mirror/punkpeye_awesome-mcp-servers)** - ⭐ 111
   Mirror of https://github.com/punkpeye/awesome-mcp-servers

1522. **[Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP](https://github.com/newideas99/Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP)** - ⭐ 111
   🧠 MCP server implementing RAT (Retrieval Augmented Thinking) - combines DeepSeek's reasoning with GPT-4/Claude/Mistral responses, maintaining conversation context between interactions.

1523. **[MCP-searxng](https://github.com/SecretiveShell/MCP-searxng)** - ⭐ 111
   MCP server for connecting agentic systems to search systems via searXNG

1524. **[spring-documentation-mcp-server](https://github.com/andrlange/spring-documentation-mcp-server)** - ⭐ 111
   Spring Boot based MCP Server provide full Spring Ecosystem Documentation for LLMs

1525. **[hevy-mcp](https://github.com/chrisdoc/hevy-mcp)** - ⭐ 111
   Manage your Hevy workouts, routines, folders, and exercise templates. Create and update sessions faster, organize plans, and search exercises to build workouts quickly. Stay synced with changes so your training log is always up to date.

1526. **[aks-mcp](https://github.com/Azure/aks-mcp)** - ⭐ 111
   A Model Context Protocol (MCP) server that enables AI assistants to interact with AKS clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and AKS.

1527. **[vscode-as-mcp-server](https://github.com/acomagu/vscode-as-mcp-server)** - ⭐ 111
   Expose VSCode features such as file viewing and editing as MCP, enabling advanced AI-assisted coding directly from tools like Claude Desktop

1528. **[mcp-checkpoint](https://github.com/aira-security/mcp-checkpoint)** - ⭐ 110
   MCP Checkpoint continuously secures and monitors Model Context Protocol operations through static and dynamic scans, revealing hidden risks in agent-to-tool communications.

1529. **[mcpauth](https://github.com/mcpauth/mcpauth)** - ⭐ 110
   Authentication for MCP Servers

1530. **[mcp-jfrog](https://github.com/jfrog/mcp-jfrog)** - ⭐ 110
   Model Context Protocol (MCP) Server for the JFrog Platform API, enabling repository management, build tracking, release lifecycle management, and more.

1531. **[livebook_tools](https://github.com/thmsmlr/livebook_tools)** - ⭐ 110
   Powertools for livebook.dev — AI Code Editing, MCP Servers, and Running Livebooks from the CLI

1532. **[dash-mcp-server](https://github.com/Kapeli/dash-mcp-server)** - ⭐ 110
   MCP server for Dash, the macOS documentation browser

1533. **[gRPC-zig](https://github.com/ziglana/gRPC-zig)** - ⭐ 110
   blazigly fast gRPC/MCP client & server implementation in zig

1534. **[gemini-cli-mcp-server](https://github.com/centminmod/gemini-cli-mcp-server)** - ⭐ 110

1535. **[akshare-one-mcp](https://github.com/zwldarren/akshare-one-mcp)** - ⭐ 110
   MCP server that provides access to Chinese stock market data using akshare-one

1536. **[server-wp-mcp](https://github.com/emzimmer/server-wp-mcp)** - ⭐ 109

1537. **[ai-command](https://github.com/mcp-wp/ai-command)** - ⭐ 109
   Control WordPress using WP-CLI, AI, and MCP.

1538. **[modex](https://github.com/theronic/modex)** - ⭐ 109
   Modex is a Clojure MCP Library to augment your AI models with Tools, Resources & Prompts using Clojure (Model Context Protocol). Implements MCP Server & Client.

1539. **[game-asset-mcp](https://github.com/MubarakHAlketbi/game-asset-mcp)** - ⭐ 109
   An MCP server for creating 2D/3D game assets from text using Hugging Face AI models.

1540. **[Taiwan-Health-MCP](https://github.com/healthymind-tech/Taiwan-Health-MCP)** - ⭐ 109

1541. **[DINO-X-MCP](https://github.com/IDEA-Research/DINO-X-MCP)** - ⭐ 109
   Official DINO-X Model Context Protocol (MCP) server that empowers LLMs with real-world visual perception through image object detection, localization, and captioning APIs.

1542. **[mcp-probe](https://github.com/conikeec/mcp-probe)** - ⭐ 109
   A Model Context Protocol (MCP) client library and debugging toolkit in Rust. This foundation provides both a production-ready SDK for building MCP integrations and the core architecture for an interactive debugger.

1543. **[apple-health-mcp-server](https://github.com/the-momentum/apple-health-mcp-server)** - ⭐ 109
   MCP server for querying Apple Health data with natural language using DuckDB under the hood.

1544. **[share-best-mcp](https://github.com/shareAI-lab/share-best-mcp)** - ⭐ 108
   世界上最好的MCP Servers的列表,The best mcp servers in the world.

1545. **[minesweeper-mcp-server](https://github.com/tonypan2/minesweeper-mcp-server)** - ⭐ 108
   An MCP server for playing Minesweeper

1546. **[asyncmcp](https://github.com/bh-rat/asyncmcp)** - ⭐ 108
   Async transport layers for MCP

1547. **[mcp_client](https://github.com/theailanguage/mcp_client)** - ⭐ 108
   MCP Client Implementation using Python, LangGraph and Gemini

1548. **[oracle-mcp-server](https://github.com/danielmeppiel/oracle-mcp-server)** - ⭐ 108
   MCP Server for working with large Oracle databases

1549. **[UnityMCPIntegration](https://github.com/quazaai/UnityMCPIntegration)** - ⭐ 108
   Enable AI Agents to Control Unity

1550. **[apple-rag-mcp](https://github.com/BingoWon/apple-rag-mcp)** - ⭐ 108
    MCP server providing AI agents with instant access to Apple developer documentation via RAG technology

1551. **[augments-mcp-server](https://github.com/augmnt/augments-mcp-server)** - ⭐ 108
   Comprehensive MCP server providing real-time framework documentation access for Claude Code with intelligent caching, multi-source integration, and context-aware assistance.

1552. **[mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket)** - ⭐ 108
   Node.js/TypeScript MCP server for Atlassian Bitbucket. Enables AI systems (LLMs) to interact with workspaces, repositories, and pull requests via tools (list, get, comment, search). Connects AI directly to version control workflows through the standard MCP interface.

1553. **[typst-mcp](https://github.com/johannesbrandenburger/typst-mcp)** - ⭐ 108
   Typst MCP Server is an MCP (Model Context Protocol) implementation that helps AI models interact with Typst, a markup-based typesetting system. The server provides tools for converting between LaTeX and Typst, validating Typst syntax, and generating images from Typst code.

1554. **[toolhive-studio](https://github.com/stacklok/toolhive-studio)** - ⭐ 108
   ToolHive is an application that allows you to install, manage and run MCP servers and connect them to AI agents

1555. **[kibitz](https://github.com/nick1udwig/kibitz)** - ⭐ 107
   The coding agent for professionals

1556. **[slack-mcp-server](https://github.com/ubie-oss/slack-mcp-server)** - ⭐ 107
   A Slack MCP server

1557. **[selfhosted-supabase-mcp](https://github.com/HenkDz/selfhosted-supabase-mcp)** - ⭐ 107
   An MCP Server for your Self Hosted Supabase

1558. **[mcp-tool-kit](https://github.com/getfounded/mcp-tool-kit)** - ⭐ 107
   Agentic abstraction layer for building high precision vertical AI agents written in python for Model Context Protocol.

1559. **[payloadcmsmcp](https://github.com/disruption-hub/payloadcmsmcp)** - ⭐ 107
   Payload CMS MCP Server

1560. **[Financial-Modeling-Prep-MCP-Server](https://github.com/imbenrabi/Financial-Modeling-Prep-MCP-Server)** - ⭐ 107
   A Model Context Protocol (MCP) implementation for Financial Modeling Prep, enabling AI assistants to access and analyze financial data, stock information, company fundamentals, and market insights.

1561. **[mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal)** - ⭐ 107
   A Model Context Protocol (MCP) server for querying the VirusTotal API.

1562. **[awesome-x402](https://github.com/xpaysh/awesome-x402)** - ⭐ 107
   🚀 Curated list of x402 resources: HTTP 402 Payment Required protocol for blockchain payments, crypto micropayments, AI agents, API monetization. Includes SDKs (TypeScript, Python, Rust), examples, facilitators (Coinbase, Cloudflare), MCP integration, tutorials. Accept USDC payments with one line of code. Perfect for AI agent economy.

1563. **[mcp-client](https://github.com/punkpeye/mcp-client)** - ⭐ 106
   An MCP client for Node.js.

1564. **[IntelliConnect](https://github.com/ruanrongman/IntelliConnect)** - ⭐ 106
   本项目为xiaozhi-esp32提供后端服务  |  A Powerful AI agent IoT platform core.

1565. **[mcp-toolkit](https://github.com/nuxt-modules/mcp-toolkit)** - ⭐ 106
   Create MCP servers directly in your Nuxt application. Define tools, resources, and prompts with a simple and intuitive API.

1566. **[template-repo](https://github.com/AndrewAltimit/template-repo)** - ⭐ 106
   Agent orchestration & security template featuring MCP tool building, agent2agent workflows, mechanistic interpretability on sleeper agents, and agent integration via DLL injection and CLI wrappers.

1567. **[Fabric-Analytics-MCP](https://github.com/santhoshravindran7/Fabric-Analytics-MCP)** - ⭐ 105
   A Model Context Protocol (MCP) server that enables AI assistants to securely access and analyze Microsoft Fabric Analytics data through authenticated API calls.

1568. **[mcp](https://github.com/frappe/mcp)** - ⭐ 105
   Frappe MCP allows Frappe apps to function as MCP servers

1569. **[mcp-prompts](https://github.com/sparesparrow/mcp-prompts)** - ⭐ 105
   Model Context Protocol server for managing, storing, and providing prompts and prompt templates for LLM interactions. 

1570. **[flowlens-mcp-server](https://github.com/magentic/flowlens-mcp-server)** - ⭐ 105
   FlowLens is an open-source MCP server that gives your coding agent (Claude Code, Cursor, Copilot, Codex) full browser context for in-depth debugging and regression testing.

1571. **[typescript-utcp](https://github.com/universal-tool-calling-protocol/typescript-utcp)** - ⭐ 105
   Official typescript implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

1572. **[sourcerer-mcp](https://github.com/st3v3nmw/sourcerer-mcp)** - ⭐ 105
   MCP for semantic code search & navigation that reduces token waste

1573. **[mcpm](https://github.com/MCP-Club/mcpm)** - ⭐ 105
   A command-line tool for managing MCP servers in Claude App. Also can run a MCP Server to help you manage all your MCP Servers

1574. **[csharp-runner](https://github.com/sdcb/csharp-runner)** - ⭐ 105
   fast, secure c# runner

1575. **[mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan)** - ⭐ 105
   MCP server for querying the Shodan API

1576. **[ZipAgent](https://github.com/JiayuXu0/ZipAgent)** - ⭐ 104
   轻量级AI Agent框架，让你5分钟构建专属智能助手。Lightweight AI Agent framework. Build your AI assistant in 5 minutes.

1577. **[mcp.science](https://github.com/pathintegral-institute/mcp.science)** - ⭐ 104
   Open Source MCP Servers for Scientific Research

1578. **[agentcare-mcp](https://github.com/Kartha-AI/agentcare-mcp)** - ⭐ 104
   MCP Server for EMRs with FHIR

1579. **[freqtrade-mcp](https://github.com/kukapay/freqtrade-mcp)** - ⭐ 104
   An MCP server that integrates with the Freqtrade cryptocurrency trading bot.

1580. **[awesome-context-engineering](https://github.com/jihoo-kim/awesome-context-engineering)** - ⭐ 104
   A curated list of awesome open-source libraries for context engineering (Long-term memory, MCP: Model Context Protocol, Prompt/RAG Compression, Multi-Agent)

1581. **[GenesisCore](https://github.com/AIGODLIKE/GenesisCore)** - ⭐ 104
   One click installation! BlenderMCP tool that supports DeepSeek, Claude, and others, fully integrated into Blender!

1582. **[pocketbase-mcp](https://github.com/mrwyndham/pocketbase-mcp)** - ⭐ 104
   MCP server for building PocketBase apps really quickly - Need a front end quick consider FastPocket

1583. **[gemini-desktop](https://github.com/kkrishnan90/gemini-desktop)** - ⭐ 103
   The MCP Gemini Electron App is a cross-platform desktop application that creates a seamless chat interface for Google's Gemini AI models with extensible capabilities through a Model Context Protocol (MCP) framework.

1584. **[smileyCoin](https://github.com/fefergrgrgrg/smileyCoin)** - ⭐ 103
   simple web ui to manage mcp (model context protocol) servers in the claude app

1585. **[memory-bank-MCP](https://github.com/tuncer-byte/memory-bank-MCP)** - ⭐ 103
   Memory Bank is an MCP server that helps teams create, manage, and access structured project documentation. It generates and maintains a set of interconnected Markdown documents that capture different aspects of project knowledge, from high-level goals to technical details and day-to-day progress.

1586. **[solana-mcp](https://github.com/solanamcp/solana-mcp)** - ⭐ 103
   Solana Agent Kit MCP Server 

1587. **[ARIES](https://github.com/Chieko-Seren/ARIES)** - ⭐ 103
   顺便一提，我们支持 RWKV | 「Intel 2025 人工智能创新大赛」🚀AutoOPS: Provide the chaos brought by language models to the operation and maintenance industry! 🏆使用 LLM 提供的动力实现全自动运维，支持 Windows Server/Linux/macOS/Cisco IOS，可进行全网自动管理，让我们颠覆运维行业【带外管理/自动运维/IoT设备管理/WebHook监控/任意平台/全模态Workflow】

1588. **[http-oauth-mcp-server](https://github.com/NapthaAI/http-oauth-mcp-server)** - ⭐ 103
   Remote MCP server (SEE + Streamable HTTP) implementing the MCP spec's authorization extension. Use directly from your agents, or from Cursor / Claude with mcp-remote

1589. **[chronulus-mcp](https://github.com/ChronulusAI/chronulus-mcp)** - ⭐ 103
   MCP Server for Chronulus AI Forecasting and Prediction Agents

1590. **[vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server)** - ⭐ 103
   Official Vectorize MCP Server

1591. **[finance-trading-ai-agents-mcp](https://github.com/aitrados/finance-trading-ai-agents-mcp)** - ⭐ 103
   A comprehensive, free MCP server designed specifically for financial analysis and quantitative trading. This specialized platform offers one-click local deployment with a sophisticated department-based architecture that mirrors real financial company operations.

1592. **[neurolink](https://github.com/juspay/neurolink)** - ⭐ 103
   Universal AI Development Platform with MCP server integration, multi-provider support, and professional CLI. Build, test, and deploy AI applications with multiple ai providers.

1593. **[mcp](https://github.com/taskade/mcp)** - ⭐ 103
   🤖 Taskade MCP · Official MCP server and OpenAPI to MCP codegen. Build AI agent tools from any OpenAPI API and connect to Claude, Cursor, and more.

1594. **[JavaSinkTracer_MCP](https://github.com/Zacarx/JavaSinkTracer_MCP)** - ⭐ 103
   基于函数级污点分析的 Java 源代码漏洞审计工具JavaSinkTracer，通过 Model Context Protocol (MCP) 为 AI 助手提供安全分析能力。

1595. **[gis-mcp](https://github.com/mahdin75/gis-mcp)** - ⭐ 103
   A Model Context Protocol (MCP) server implementation that connects Large Language Models (LLMs) to GIS operations using GIS libraries, enabling AI assistants to perform geospatial operations and transformations.

1596. **[memory-mcp-server](https://github.com/okooo5km/memory-mcp-server)** - ⭐ 102
   A Model Context Protocol server that provides knowledge graph management capabilities. 

1597. **[erickwendel-contributions-mcp](https://github.com/ErickWendel/erickwendel-contributions-mcp)** - ⭐ 102
   A Model Context Protocol (MCP) server that provides tools to query Erick Wendel's contributions across different platforms

1598. **[a2a-mcp-tutorial](https://github.com/Tsadoq/a2a-mcp-tutorial)** - ⭐ 102
   A tutorial on how to use Model Context Protocol by Anthropic and Agent2Agent Protocol by Google

1599. **[remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions)** - ⭐ 102
   Landing page for Remote MCP Server efforts in Azure Functions with links to all language stack specific repos.

1600. **[mcp-local-rag](https://github.com/nkapila6/mcp-local-rag)** - ⭐ 102
   "primitive" RAG-like web search model context protocol (MCP) server that runs locally. ✨ no APIs ✨

1601. **[mcp-server](https://github.com/webflow/mcp-server)** - ⭐ 102
   Model Context Protocol (MCP) server for the Webflow Data API.

1602. **[linggen](https://github.com/linggen/linggen)** - ⭐ 102
   A local-first memory layer for AI (Cursor, Zed, Claude). Persistent architectural context via semantic search.

1603. **[gtasks-mcp](https://github.com/zcaceres/gtasks-mcp)** - ⭐ 102
   A Google Tasks Model Context Protocol Server for Claude

1604. **[deep-code-reasoning-mcp](https://github.com/haasonsaas/deep-code-reasoning-mcp)** - ⭐ 102
   A Model Context Protocol (MCP) server that provides advanced code analysis and reasoning capabilities powered by Google's Gemini AI

1605. **[code-pathfinder](https://github.com/shivasurya/code-pathfinder)** - ⭐ 102
   AI-Native Static Code Analysis for modern security teams. Built for finding vulnerabilities, advanced structural search, derive insights and supports MCP

1606. **[btp-sap-odata-to-mcp-server](https://github.com/lemaiwo/btp-sap-odata-to-mcp-server)** - ⭐ 101
   BTP CloudFoundry Node.js MCP server for SAP OData services integration

1607. **[alibabacloud-ack-mcp-server](https://github.com/aliyun/alibabacloud-ack-mcp-server)** - ⭐ 101
   Alibaba Cloud's ack-mcp-server unifies container operations capabilities, enabling AI assistants and third-party AI agents to perform complex tasks via natural language through the MCP protocol, empowering container-native AIOps. DingTalk discussion group:  70080006301

1608. **[snippy](https://github.com/Azure-Samples/snippy)** - ⭐ 101
   🧩 Build AI-powered MCP Tools with Azure Functions, Durable Agents & Cosmos vector search. Features orchestrated multi-agent workflows using OpenAI.

1609. **[sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server)** - ⭐ 100
   An MCP server that provides safe, read-only access to SQLite databases through Model Context Protocol (MCP). This server is built with the FastMCP framework, which enables LLMs to explore and query SQLite databases with built-in safety features and query validation.

1610. **[claude-code-mcp-enhanced](https://github.com/grahama1970/claude-code-mcp-enhanced)** - ⭐ 100
   Enhanced Claude Code MCP server with orchestration capabilities, reliability improvements, and self-contained execution patterns

1611. **[mcp-hono-stateless](https://github.com/mhart/mcp-hono-stateless)** - ⭐ 100
   An example Hono MCP server using Streamable HTTP

1612. **[AgentBoard](https://github.com/igrigorik/AgentBoard)** - ⭐ 100
   A switchboard for AI in your browser: wire in any model, script WebMCP tools, connect remote MCP servers, bring your commands.

1613. **[autodev-codebase](https://github.com/anrgct/autodev-codebase)** - ⭐ 100
   A vector embedding-based code semantic search tool with MCP server and multi-model integration. Can be used as a pure CLI tool. Supports Ollama for fully local embedding and reranking, enabling complete offline operation and privacy protection for your code repository

1614. **[complete-intro-to-mcp](https://github.com/btholt/complete-intro-to-mcp)** - ⭐ 100
   The Complete Intro to MCP Servers, as taught for Frontend Masters by Brian Holt

1615. **[academic-search-mcp-server](https://github.com/afrise/academic-search-mcp-server)** - ⭐ 100
   Academic Paper Search MCP Server for Claude Desktop integration. Allows Claude to access data from Semantic Scholar and Crossref. 

1616. **[MiniMax-MCP-JS](https://github.com/MiniMax-AI/MiniMax-MCP-JS)** - ⭐ 100
   Official MiniMax Model Context Protocol (MCP) JavaScript implementation that provides seamless integration with MiniMax's powerful AI capabilities including image generation, video generation, text-to-speech, and voice cloning APIs.

1617. **[falcon-mcp](https://github.com/CrowdStrike/falcon-mcp)** - ⭐ 100
   Connect AI agents to CrowdStrike Falcon for automated security analysis and threat hunting

1618. **[mcp-screenshot-website-fast](https://github.com/just-every/mcp-screenshot-website-fast)** - ⭐ 99
   Quickly screenshots webpages and converts to an LLM friendly size

1619. **[sample-agentic-ai-demos](https://github.com/aws-samples/sample-agentic-ai-demos)** - ⭐ 99
   Collection of examples of how to use Model Context Protocol with AWS.

1620. **[mcp-windows-desktop-automation](https://github.com/mario-andreschak/mcp-windows-desktop-automation)** - ⭐ 99
   A Model Context Protocol (MCP) server for Windows desktop automation using AutoIt.

1621. **[next-mcp-server](https://github.com/vertile-ai/next-mcp-server)** - ⭐ 99
   Help LLMs to understand your Next apps better

1622. **[turbular](https://github.com/raeudigerRaeffi/turbular)** - ⭐ 99
   A MCP server allowing LLM agents to easily connect and retrieve data from any database

1623. **[pywss](https://github.com/czasg/pywss)** - ⭐ 99
   一个轻量级的 Python Web 框架，一站式集成 MCP SSE、StreamHTTP 和 MCPO 协议，助你轻松构建MCP Server🔥

1624. **[mighty-security](https://github.com/NineSunsInc/mighty-security)** - ⭐ 99
   Don't Simply Trust MCP Server Code, Validate and Scan

1625. **[mcp-client-nodejs](https://github.com/ConardLi/mcp-client-nodejs)** - ⭐ 99
   Node.js Client Implementation for Model Context Protocol (MCP)

1626. **[rust-docs-mcp](https://github.com/snowmead/rust-docs-mcp)** - ⭐ 99
   MCP server for agents to explore rust docs, analyze source code, and build with confidence

1627. **[diagram-mcp-server](https://github.com/andrewmoshu/diagram-mcp-server)** - ⭐ 99
   An MCP server that seamlessly creates infrastructure diagrams for AWS, Azure, GCP, Kubernetes and more

1628. **[mcp_on_ruby](https://github.com/rubyonai/mcp_on_ruby)** - ⭐ 98
   💎 A Ruby implementation of the Model Context Protocol

1629. **[atomic-red-team-mcp](https://github.com/cyberbuff/atomic-red-team-mcp)** - ⭐ 98
   MCP server for Atomic Red Team

1630. **[mysql-mcp-server-sse](https://github.com/mangooer/mysql-mcp-server-sse)** - ⭐ 98
   MySQL query server based on the MCP sse.Multi-level SQL risk control & injection protection Docker support for quick deployment

1631. **[github-stars](https://github.com/miantiao-me/github-stars)** - ⭐ 98
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

1632. **[terminal-controller-mcp](https://github.com/GongRzhe/terminal-controller-mcp)** - ⭐ 98
   A Model Context Protocol (MCP) server that enables secure terminal command execution, directory navigation, and file system operations through a standardized interface.

1633. **[godoc-mcp](https://github.com/mrjoshuak/godoc-mcp)** - ⭐ 98
   go doc mcp server

1634. **[heimdall-mcp-server](https://github.com/lcbcFoo/heimdall-mcp-server)** - ⭐ 98
   Your AI Coding Assistant's Long-Term Memory

1635. **[awesome-mcp-enterprise](https://github.com/bh-rat/awesome-mcp-enterprise)** - ⭐ 98
   A curated list of awesome MCP (Model Context Protocol) tools, platforms, and services for enterprises.

1636. **[mcp-sse-demo](https://github.com/cnych/mcp-sse-demo)** - ⭐ 97
   claude mcp sse demo with server and client(cli、web)

1637. **[gemini-mcp-desktop-client](https://github.com/duke7able/gemini-mcp-desktop-client)** - ⭐ 97
   first gemini based desktop client for MCP

1638. **[searxng-mul-mcp](https://github.com/jae-jae/searxng-mul-mcp)** - ⭐ 97
   A Model Context Protocol (MCP) server for SearXNG search engine with multi-query parallel search support

1639. **[lapras-mcp-server](https://github.com/lapras-inc/lapras-mcp-server)** - ⭐ 97
   lapras.com 公式MCP Server

1640. **[go-utcp](https://github.com/universal-tool-calling-protocol/go-utcp)** - ⭐ 97
    Official Go implementation of the UTCP 

1641. **[mcp-typescript-sdk](https://github.com/emqx/mcp-typescript-sdk)** - ⭐ 97
   A TypeScript SDK for implementing Model Context Protocol (MCP) over MQTT, supporting both browser and Node.js environments.

1642. **[powerbi-mcp](https://github.com/sulaiman013/powerbi-mcp)** - ⭐ 97
   MCP server for natural language interaction with Power BI datasets

1643. **[all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol)** - ⭐ 97
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows

1644. **[systemprompt-mcp-server](https://github.com/systempromptio/systemprompt-mcp-server)** - ⭐ 97
   A complete, production-ready implementation of a Model Context Protocol (MCP) server demonstrating OAuth 2.1, tools, prompts, resources, sampling, and notifications using Reddit as a real-world integration example.

1645. **[langgraph-ai](https://github.com/piyushagni5/langgraph-ai)** - ⭐ 97
   LangGraph AI Repository

1646. **[mcp-graphiti](https://github.com/rawr-ai/mcp-graphiti)** - ⭐ 97
   Graphiti Model Context Protocol (MCP) Server - An MCP server for knowledge graph management via Graphiti

1647. **[alibaba-cloud-ops-mcp-server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server)** - ⭐ 97
   AlibabaCloud CloudOps MCP Server

1648. **[outline-mcp-server](https://github.com/mmmeff/outline-mcp-server)** - ⭐ 97
   It's an MCP server... for Outline (the documentation platform!)

1649. **[wanaku](https://github.com/wanaku-ai/wanaku)** - ⭐ 97
   Wanaku MCP Router

1650. **[mcp-kit](https://github.com/my-mcp-hub/mcp-kit)** - ⭐ 96
   A CLI tool to create MCP (Model Context Protocol) applications with ease.

1651. **[sandbox-mcp](https://github.com/pottekkat/sandbox-mcp)** - ⭐ 96
   A Model Context Protocol (MCP) server that enables LLMs to run ANY code safely in isolated Docker containers.

1652. **[Vibe-Coder-MCP](https://github.com/freshtechbro/Vibe-Coder-MCP)** - ⭐ 96
    Vibe-Coder-MCP server extends AI assistants with specialized software development tools.

1653. **[opencv-mcp-server](https://github.com/GongRzhe/opencv-mcp-server)** - ⭐ 95
   OpenCV MCP Server  provides OpenCV's image and video processing capabilities through the Model Context Protocol (MCP). Access powerful computer vision tools for tasks ranging from basic image manipulation to advanced object detection and tracking.

1654. **[api2mcp4j](https://github.com/TheEterna/api2mcp4j)** - ⭐ 95
   This is a revolutionary AI MCP plugin with excellent pluggable and encapsulated features. With just a few lines of configuration, it can easily integrate into your Spring boot web program and give it MCP capabilities,inheriting the powerful engineering capabilities of the Spring series framework

1655. **[gossiphs](https://github.com/williamfzc/gossiphs)** - ⭐ 95
   "Zero setup" & "Blazingly fast" general code file relationship analysis. With Python & Rust. Based on tree-sitter and git analysis. Support MCP and ready for AI🤖

1656. **[editor-mcp-server](https://github.com/playcanvas/editor-mcp-server)** - ⭐ 95
   MCP Server for AI automation of the PlayCanvas Editor

1657. **[octagon-mcp-server](https://github.com/OctagonAI/octagon-mcp-server)** - ⭐ 95
   A free MCP server to analyze and extract insights from public filings, earnings transcripts, financial metrics, stock market data, private market transactions, and deep web-based research within Claude Desktop and other popular MCP clients.

1658. **[google-tag-manager-mcp-server](https://github.com/stape-io/google-tag-manager-mcp-server)** - ⭐ 95
   MCP server for Google Tag Manager

1659. **[yfinance-mcp](https://github.com/narumiruna/yfinance-mcp)** - ⭐ 95

1660. **[mikrotik-mcp](https://github.com/jeff-nasseri/mikrotik-mcp)** - ⭐ 95
   MCP server for Mikrotik

1661. **[flexible-graphrag](https://github.com/stevereiner/flexible-graphrag)** - ⭐ 95
   Flexible GraphRAG: Python, LlamaIndex, Docker Compose: 8 Graph dbs, 10 Vector dbs, OpenSearch, Elasticsearch, Alfresco. 13 data sources (9 auto-sync), KG auto-building, schemas, LLMs, Docling or LlamaParse doc processing, GraphRAG, RAG only, Hybrid search, AI chat. React, Vue, Angular frontends, FastAPI backend, REST API, MCP Server. Please 🌟 Star

1662. **[ruby-mcp-client](https://github.com/simonx1/ruby-mcp-client)** - ⭐ 94
   This is a Ruby implementation of MCP (Model Context Protocol) client

1663. **[ToolsForMCPServer](https://github.com/tanaikech/ToolsForMCPServer)** - ⭐ 94
   The Gemini CLI confirmed that the MCP server built with Google Apps Script (GAS), a low-code platform, offers immense possibilities. If you've created snippets for GAS, these could be revitalized and/or leveraged in new ways by using them as the MCP server. The Gemini CLI and other MCP clients will be useful in achieving this.

1664. **[brave-search-mcp](https://github.com/mikechao/brave-search-mcp)** - ⭐ 94
   An MCP Server implementation that integrates the Brave Search API, providing, Web Search, Local Points of Interest Search, Image Search, Video Search and News Search capabilities

1665. **[needle-mcp](https://github.com/needle-ai/needle-mcp)** - ⭐ 94
   Needle MCP Server for easy RAG.Long-term memory for LLMs.

1666. **[zed-mcp-server-context7](https://github.com/akbxr/zed-mcp-server-context7)** - ⭐ 94
   Context7 MCP Server for Zed

1667. **[Matryoshka](https://github.com/yogthos/Matryoshka)** - ⭐ 94
   MCP server for token-efficient large document analysis via the use of REPL state

1668. **[infobus-mcp](https://github.com/simovilab/infobus-mcp)** - ⭐ 93
   Model Context Protocol server enabling AI assistants to access transit information through standardized interfaces

1669. **[elektron-mcp](https://github.com/zerubeus/elektron-mcp)** - ⭐ 93
   MCP sever for controlling Elektron devices using LLMs

1670. **[MasterMCP](https://github.com/slowmist/MasterMCP)** - ⭐ 93
   A demonstration toolkit revealing potential security vulnerabilities in MCP (Model Context Protocol) frameworks through data poisoning, JSON injection, function overriding, and cross-MCP call attacks, exposing AI security issues while providing defense recommendations. For educational and research purposes only.

1671. **[mcp-replicate](https://github.com/deepfates/mcp-replicate)** - ⭐ 93
   Model Context Protocol server for Replicate's API

1672. **[gospy](https://github.com/monsterxx03/gospy)** - ⭐ 93
   Non-Invasive goroutine inspector

1673. **[a2ajava](https://github.com/vishalmysore/a2ajava)** - ⭐ 93
   Pure java implementation of Google A2A protocol. Integrate your spring boot java applications with A2A protocol , includes client and sever both. Any agent built with a2ajava will also be exposed as MCP tool automatically

1674. **[openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp)** - ⭐ 93
   A Model Context Protocol (MCP) tool server for OpenAI's GPT-4o/gpt-image-1 image generation and editing APIs.

1675. **[sparql-llm](https://github.com/sib-swiss/sparql-llm)** - ⭐ 93
   🦜✨ Chat system, MCP server, and reusable components to improve LLMs capabilities when generating SPARQL queries

1676. **[google_ads_mcp](https://github.com/google-marketing-solutions/google_ads_mcp)** - ⭐ 93
   The Google Ads MCP Server is an implementation of the Model Context Protocol (MCP) that enables Large Language Models (LLMs), such as Gemini, to interact directly with the Google Ads API.

1677. **[CoWork-OS](https://github.com/CoWork-OS/CoWork-OS)** - ⭐ 92
   Operating System for your personal AI Agents with Security-first approach. Multi-channel (WhatsApp, Telegram, Discord, Slack, iMessage), multi-provider (Claude, GPT, Gemini, Ollama), fully self-hosted.

1678. **[narsil-mcp](https://github.com/postrv/narsil-mcp)** - ⭐ 92
   Rust MCP server for comprehensive code intelligence - 90 tools, 32 languages, security scanning, call graphs, and more

1679. **[mcp-server-idapro](https://github.com/fdrechsler/mcp-server-idapro)** - ⭐ 92
   A Model Context Protocol (MCP) server that enables AI assistants to interact with IDA Pro for reverse engineering and binary analysis tasks.

1680. **[mcp-server](https://github.com/OctopusDeploy/mcp-server)** - ⭐ 92
   Octopus Deploy Official MCP Server

1681. **[open-mcp-auth-proxy](https://github.com/wso2/open-mcp-auth-proxy)** - ⭐ 92
   Authentication and Authorization Proxy for MCP Servers

1682. **[pluggedin-app](https://github.com/VeriTeknik/pluggedin-app)** - ⭐ 92
   The Crossroads for AI Data Exchanges. A unified, self-hostable web interface for discovering, configuring, and managing Model Context Protocol (MCP) servers—bringing together AI tools, workspaces, prompts, and logs from multiple MCP sources (Claude, Cursor, etc.) under one roof.

1683. **[schedcp](https://github.com/eunomia-bpf/schedcp)** - ⭐ 92
   MCP Server for Linux Scheduler Management and Auto optimization

1684. **[model-context-protocol-mcp-hands-on-with-agentic-ai-2034200](https://github.com/LinkedInLearning/model-context-protocol-mcp-hands-on-with-agentic-ai-2034200)** - ⭐ 92
   This is a code repository for the LinkedIn Learning course Model Context Protocol (MCP): Hands-On with Agentic AI [ASI] [TEXT] [MODELS]

1685. **[FNewsCrawler](https://github.com/noimank/FNewsCrawler)** - ⭐ 92
   一个专门为大模型设计的财经信息MCP（Model Context Protocol）服务，通过高效的爬虫技术从各大财经网站（同花顺、东方财富等）获取实时资讯，为AI模型提供准确、及时的财经数据支持。

1686. **[mcp-local-rag](https://github.com/shinpr/mcp-local-rag)** - ⭐ 92
   Local-first RAG server for developers using MCP. Semantic + keyword search for code and technical docs. Fully private, zero setup.

1687. **[AgentUp](https://github.com/always-further/AgentUp)** - ⭐ 91
   Portable , scalable , secure AI Agents

1688. **[square-mcp-server](https://github.com/square/square-mcp-server)** - ⭐ 91
   A Model Context Protocol (MCP) server for square

1689. **[litegraph](https://github.com/litegraphdb/litegraph)** - ⭐ 91
   Lightweight graph database with relational, vector, and MCP support, designed to power knowledge and artificial intelligence persistence and retrieval.

1690. **[mcpcat-typescript-sdk](https://github.com/MCPCat/mcpcat-typescript-sdk)** - ⭐ 91
   MCPcat is an analytics platform for MCP server owners 🐱.

1691. **[mcp-trino](https://github.com/tuannvm/mcp-trino)** - ⭐ 91
   A high-performance Model Context Protocol (MCP) server for Trino implemented in Go.

1692. **[spring-ai-playground](https://github.com/spring-ai-community/spring-ai-playground)** - ⭐ 91
   Spring AI Playground is a self-hosted web UI for low-code AI tool development with live MCP server registration. It includes MCP server inspection, agentic chat, and integrated LLM and RAG workflows, enabling real-time experimentation and evolution of tool-enabled AI systems without redeployment.

1693. **[vibe](https://github.com/michiosw/vibe)** - ⭐ 91
   Open-Source AI-powered web browser. Browse the web with your own LLM API key. Alternative to Dia / Comet.

1694. **[splunk-mcp](https://github.com/livehybrid/splunk-mcp)** - ⭐ 90
   A Model Context Protocol (MCP) implementation for Splunk Enterprise and Cloud integration with Cursor IDE or Claude

1695. **[IB_MCP](https://github.com/rcontesti/IB_MCP)** - ⭐ 90
   This project provides an Interactive Brokers (IB) API interface using the Model Context Protocol (MCP).

1696. **[deepl-mcp-server](https://github.com/DeepLcom/deepl-mcp-server)** - ⭐ 90
   A Model Context Protocol (MCP) server that provides translation capabilities using the DeepL API.

1697. **[semantic-scholar-fastmcp-mcp-server](https://github.com/zongmin-yu/semantic-scholar-fastmcp-mcp-server)** - ⭐ 90
   A FastMCP server implementation for the Semantic Scholar API, providing comprehensive access to academic paper data, author information, and citation networks.

1698. **[mcp-python-interpreter](https://github.com/yzfly/mcp-python-interpreter)** - ⭐ 90
   MCP Python Interpreter: run python code. Python-mcp-server, mcp-python-server, Code Executor

1699. **[arxiv-latex-mcp](https://github.com/takashiishida/arxiv-latex-mcp)** - ⭐ 89
   MCP server that uses arxiv-to-prompt to fetch and process arXiv LaTeX sources for precise interpretation of mathematical expressions in scientific papers.

1700. **[tiger-cli](https://github.com/timescale/tiger-cli)** - ⭐ 89
   Tiger CLI is the command-line interface for Tiger Cloud. It includes an MCP server for helping coding agents write production-level Postgres code.

1701. **[fhir-mcp-server](https://github.com/wso2/fhir-mcp-server)** - ⭐ 89
   FHIR MCP Server – helping you expose any FHIR Server or API as a MCP Server.

1702. **[bouvet](https://github.com/vrn21/bouvet)** - ⭐ 89
   Sandbox for Agents 

1703. **[paper-search-mcp-nodejs](https://github.com/Dianel555/paper-search-mcp-nodejs)** - ⭐ 89
   A Node.js implementation of the Model Context Protocol (MCP) server for searching and downloading academic papers from multiple sources, including **Web of Science**, arXiv, and more.

1704. **[z-image-studio](https://github.com/iconben/z-image-studio)** - ⭐ 89
   A Cli, a webUI, and a MCP server for the Z-Image-Turbo text-to-image generation model (Tongyi-MAI/Z-Image-Turbo base model as well as quantized models)

1705. **[Nano-Banana-MCP](https://github.com/ConechoAI/Nano-Banana-MCP)** - ⭐ 89
   A Nano Banana MCP server, which you can integrate to cursor/claude code and any mcp client

1706. **[molecule-mcp](https://github.com/ChatMol/molecule-mcp)** - ⭐ 88
   A model-context-protocol server for molecules.

1707. **[mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw)** - ⭐ 88
   An MCP stdio to HTTP SSE transport gateway with example server and MCP client

1708. **[action_mcp](https://github.com/seuros/action_mcp)** - ⭐ 88
   Rails Engine with MCP compliant Spec.

1709. **[mcp-rest-api](https://github.com/dkmaker/mcp-rest-api)** - ⭐ 88
   A TypeScript-based MCP server that enables testing of REST APIs through Cline. This tool allows you to test and interact with any REST API endpoints directly from your development environment.

1710. **[apps-sdk-template](https://github.com/alpic-ai/apps-sdk-template)** - ⭐ 88
   A minimalist Typescript ChatGPT App based on the Skybridge framework

1711. **[mcp-memory-keeper](https://github.com/mkreyman/mcp-memory-keeper)** - ⭐ 88
   MCP server for persistent context management in AI coding assistants

1712. **[browser-debugger-cli](https://github.com/szymdzum/browser-debugger-cli)** - ⭐ 88
   CLI tool for agents to quickly access browser telemetry (DOM, network, console) via Chrome DevTools Protocol.

1713. **[awsome_kali_MCPServers](https://github.com/ccq1/awsome_kali_MCPServers)** - ⭐ 88
   awsome kali MCPServers is a set of MCP servers tailored for Kali Linux

1714. **[mcp-outline](https://github.com/Vortiago/mcp-outline)** - ⭐ 88
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Outline documentation services.

1715. **[mcp-agent](https://github.com/Haohao-end/mcp-agent)** - ⭐ 87
   A modular Python framework implementing the Model Context Protocol (MCP). It features a standardized client-server architecture over StdIO, integrating LLMs with external tools, real-time weather data fetching, and an advanced RAG (Retrieval-Augmented Generation) system.

1716. **[mem0-mcp](https://github.com/pinkpixel-dev/mem0-mcp)** - ⭐ 87
   ✨ mem0 MCP Server: A memory system using mem0 for AI applications with model context protocl (MCP) integration. Enables long-term memory for AI agents as a drop-in MCP server.

1717. **[chat-ui](https://github.com/AI-QL/chat-ui)** - ⭐ 87
   Single-File AI Chatbot UI with Multimodal & MCP Support: An All-in-One HTML File for a Streamlined Chatbot Conversational Interface

1718. **[achatbot](https://github.com/ai-bot-pro/achatbot)** - ⭐ 87
   An open source chat bot architecture for voice/vision (and multimodal) assistants,  local(CPU/GPU bound) and remote(I/O bound) to run.

1719. **[mcpgen](https://github.com/lyeslabs/mcpgen)** - ⭐ 87
   Generate Go MCP server boilerplate from OpenAPI 3 specifications

1720. **[mcp-ui](https://github.com/machaojin1917939763/mcp-ui)** - ⭐ 87
   基于MCP(Model Context Protocol)的智能聊天应用，支持Web和桌面环境。集成OpenAI/Anthropic API，提供MCP服务器的所有工具能力。简洁现代的UI设计，支持跨平台部署。

1721. **[awesome-openid-connect](https://github.com/cerberauth/awesome-openid-connect)** - ⭐ 87
   OpenID Connect, the authentication protocol and identity layer on top of OAuth 2.0 used in many SSO and adopted in many social logins (Apple, Facebook, Google, ...etc). Find this curated list of providers, services, libraries, and resources to adopt it and know more about existing specs.

1722. **[slidev-mcp](https://github.com/LSTM-Kirigaya/slidev-mcp)** - ⭐ 87
   mcp server for slidev to make web ppt quickly and elegantly

1723. **[idun-agent-platform](https://github.com/Idun-Group/idun-agent-platform)** - ⭐ 87
   🟪 Open source Agent Governance Platform that turns any LangGraph or ADK agent into a production-ready service. Supports: AG-UI, CopilotKit API, OpenTelemetry, MCP, memory, guardrails, SSO, RBAC.

1724. **[leetcode-mcp-server](https://github.com/jinzcdev/leetcode-mcp-server)** - ⭐ 87
   An MCP server enabling automated access to LeetCode's problems, solutions, and public data with optional authentication for user-specific features, supporting leetcode.com & leetcode.cn sites.

1725. **[context-sync](https://github.com/Intina47/context-sync)** - ⭐ 87
   Local persistent memory store for LLM applications including continue.dev, cursor, claude desktop, github copilot, codex, antigravity, etc.

1726. **[design-systems-mcp](https://github.com/southleft/design-systems-mcp)** - ⭐ 87
   I'm your specialized design systems assistant. Ask me about components, tokens, patterns, and best practices.

1727. **[pinescript-mcp-server](https://github.com/cklose2000/pinescript-mcp-server)** - ⭐ 86
   A Model Context Protocol (MCP) server for working with TradingView PineScript

1728. **[react-agent-hooks](https://github.com/chuanqisun/react-agent-hooks)** - ⭐ 86
   Turn React hooks into LLM tools

1729. **[mcp-server-llamacloud](https://github.com/run-llama/mcp-server-llamacloud)** - ⭐ 86
   A MCP server connecting to managed indexes on LlamaCloud

1730. **[vggt-mps](https://github.com/jmanhype/vggt-mps)** - ⭐ 86
   VGGT 3D Vision Agent optimized for Apple Silicon with Metal Performance Shaders

1731. **[memory-mcp-server-go](https://github.com/okooo5km/memory-mcp-server-go)** - ⭐ 86
   A Model Context Protocol server that provides knowledge graph management capabilities.

1732. **[FrontAgent](https://github.com/ceilf6/FrontAgent)** - ⭐ 86
   AI agent platform for frontend engineering with SDD constraints & MCP-controlled automation. | 面向前端工程的企业级 AI Agent 平台

1733. **[mcp-dbutils](https://github.com/donghao1393/mcp-dbutils)** - ⭐ 86
   数读 是一件可以让你的大模型安全连接到数据库的MCP工具。| DButils is an all-in-one MCP service that enables your AI to do data analysis by harnessing versatile types of database (sqlite, mysql, postgres, and more) within a unified configuration of multiple connections in a secured way (like SSL and controlled write access).

1734. **[furi](https://github.com/ashwwwin/furi)** - ⭐ 86
   CLI & API for MCP management

1735. **[agent-tool-protocol](https://github.com/mondaycom/agent-tool-protocol)** - ⭐ 86
   Agent Tool Protocol

1736. **[ragie-mcp-server](https://github.com/ragieai/ragie-mcp-server)** - ⭐ 86
   Ragie Model Context Protocol Server

1737. **[QMT-MCP](https://github.com/guangxiangdebizi/QMT-MCP)** - ⭐ 86
    QMT-MCP 模块化量化交易助手

1738. **[perfetto-mcp](https://github.com/antarikshc/perfetto-mcp)** - ⭐ 86
   This is a Model Context Protocol (MCP) server that gets answers from your Perfetto Traces. It turns natural‑language prompts into focused Perfetto analyses.

1739. **[healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public)** - ⭐ 86
   A Model Context Protocol (MCP) server providing AI assistants with access to healthcare data and medical information tools, including FDA drug info, PubMed, medRxiv, NCBI Bookshelf, clinical trials, ICD-10, DICOM metadata, and a medical calculator.

1740. **[github-stars](https://github.com/ccbikai/github-stars)** - ⭐ 85
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

1741. **[mcp](https://github.com/twilio-labs/mcp)** - ⭐ 85
   Monorepo providing 1) OpenAPI to MCP Tool generator 2) Exposing all of Twilio's API as MCP Tools

1742. **[mcp-sqlite](https://github.com/jparkerweb/mcp-sqlite)** - ⭐ 85
   🐇 Model Context Protocol (MCP) server that provides comprehensive SQLite database interaction capabilities

1743. **[xclaude-plugin](https://github.com/conorluddy/xclaude-plugin)** - ⭐ 85
   iOS development ClaudeCode plugin for mindful token and context usage. Contains modular MCPs that group various Xcode/IDB tools based on your current workflow.

1744. **[anubis-mcp](https://github.com/zoedsoupe/anubis-mcp)** - ⭐ 85
   Elixir Model Context Protocol (MCP) SDK (hermes-mcp fork)

1745. **[mcp-dockmaster](https://github.com/dcSpark/mcp-dockmaster)** - ⭐ 84
   MCP Dockmaster allows you to easily install and manage MCP servers. Available for Mac, Windows and Linux as a Desktop App, CLI and a library.

1746. **[spiceflow](https://github.com/remorses/spiceflow)** - ⭐ 84
   Super Simple API framework, type safe, automatic OpenAPI, MCP support, client RPC, streaming with SSE

1747. **[cve-search_mcp](https://github.com/roadwy/cve-search_mcp)** - ⭐ 84
   A Model Context Protocol (MCP) server for querying the CVE-Search API

1748. **[amap-mcp-server](https://github.com/sugarforever/amap-mcp-server)** - ⭐ 84
   高德地图MCP Server，支持stdio, sse和streamable-http

1749. **[Delphi-MCP-Server](https://github.com/GDKsoftware/Delphi-MCP-Server)** - ⭐ 84
   Native Delphi Server implementation of the Model Context Protocol (MCP)

1750. **[bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp)** - ⭐ 84
   Bitbucket MCP - A Model Context Protocol (MCP) server for integrating with Bitbucket Cloud and Server APIs

1751. **[mcp-node](https://github.com/algolia/mcp-node)** - ⭐ 83
   MCP server for interacting with Algolia

1752. **[claude-swarm](https://github.com/cj-vana/claude-swarm)** - ⭐ 83
   MCP server for orchestrating parallel Claude Code worker swarms with protocol-based behavioral governance, persistent state, and real-time monitoring dashboard

1753. **[legion-mcp](https://github.com/TheRaLabs/legion-mcp)** - ⭐ 83
   A server that helps people access and query data in databases using the Legion Query Runner with Model Context Protocol (MCP) in Python.

1754. **[xiaozhi-mcp-ha](https://github.com/mac8005/xiaozhi-mcp-ha)** - ⭐ 83
   A Home Assistant Custom Integration (HACS) that connects Xiaozhi ESP32 AI chatbot to Home Assistant via MCP

1755. **[mcp-github-project-manager](https://github.com/kunwarVivek/mcp-github-project-manager)** - ⭐ 83
   a mcp server to manage github project's functionality 

1756. **[mcp-n8n-builder](https://github.com/spences10/mcp-n8n-builder)** - ⭐ 83
   🪄 MCP server for programmatic creation and management of n8n workflows. Enables AI assistants to build, modify, and manage workflows without direct user intervention through a comprehensive set of tools and resources for interacting with n8n's REST API.

1757. **[viper](https://github.com/ozanunal0/viper)** - ⭐ 83
   🛡️ VIPER: Stay ahead of threats with AI-driven vulnerability intelligence. Prioritize CVEs effectively using NVD, EPSS, CISA KEV, and Google Gemini insights, all on an interactive dashboard

1758. **[reddit-research-mcp](https://github.com/king-of-the-grackles/reddit-research-mcp)** - ⭐ 83
   Turn Reddit's chaos into structured insights with full citations. MCP server for competitive analysis, customer discovery, and market research. Zero-setup hosted solution with semantic search across 20,000+ subreddits.

1759. **[identity](https://github.com/agntcy/identity)** - ⭐ 83
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

1760. **[mcp-gateway](https://github.com/hyprmcp/mcp-gateway)** - ⭐ 83
   MCP OAuth Proxy incl. dynamic client registration (DCR), MCP prompt analytics and MCP firewall to build enterprise grade MCP servers.

1761. **[loki-mcp](https://github.com/grafana/loki-mcp)** - ⭐ 83
   An MCP ( Model Context Protocol ) Server for Grafana Loki

1762. **[arbor](https://github.com/Anandb71/arbor)** - ⭐ 83
   Graph-native code intelligence that replaces embedding-based RAG with deterministic program understanding.

1763. **[mcp-memory-libsql](https://github.com/spences10/mcp-memory-libsql)** - ⭐ 82
   🧠 High-performance persistent memory system for Model Context Protocol (MCP) powered by libSQL. Features vector search, semantic knowledge storage, and efficient relationship management - perfect for AI agents and knowledge graph applications.

1764. **[agentic-stock-research-system](https://github.com/rooneyrulz/agentic-stock-research-system)** - ⭐ 82
   A sophisticated multi-agent AI system for analyzing Indian NSE-listed stocks using real-time data, technical indicators, news sentiment, and advanced AI reasoning.

1765. **[oxylabs-mcp](https://github.com/oxylabs/oxylabs-mcp)** - ⭐ 82
   Official Oxylabs MCP integration

1766. **[node-candidate-mcp-server](https://github.com/jhgaylor/node-candidate-mcp-server)** - ⭐ 81
   A Model Context Protocol (MCP) server library that gives LLMs access to information about a candidate.

1767. **[mcp-rs-template](https://github.com/linux-china/mcp-rs-template)** - ⭐ 81
   Model Context Protocol (MCP) CLI server template for Rust

1768. **[sh-disney-mcp](https://github.com/syyuan14/sh-disney-mcp)** - ⭐ 81
   sh-disney-mcp 是一个基于 Model Context Protocol (MCP) 的mcp server，旨在通过标准化的接口，帮助大模型快速获取上海迪士尼乐园的门票价格和售卖状态信息

1769. **[mcphub](https://github.com/Cognitive-Stack/mcphub)** - ⭐ 81
   MCPHub is an embeddable Model Context Protocol (MCP) solution for AI services. Seamlessly integrate MCP servers with OpenAI Agents, LangChain, and Autogen frameworks through a unified interface. Simplifies configuration, setup, and management of MCP tools across different AI applications.

1770. **[mcp-excel-server](https://github.com/yzfly/mcp-excel-server)** - ⭐ 81
   The Excel MCP Server is a powerful tool that enables natural language interaction with Excel files through the Model Context Protocol (MCP). It provides a comprehensive set of capabilities for reading, analyzing, visualizing, and writing Excel data.

1771. **[Awesome-Claude-MCP-Servers](https://github.com/win4r/Awesome-Claude-MCP-Servers)** - ⭐ 81
   A curated list of Model Context Protocol (MCP) servers optimized for Claude AI assistants.

1772. **[office-editor-mcp](https://github.com/theWDY/office-editor-mcp)** - ⭐ 81
   基于MCP(Model Context Protocol)的Office文档处理助手，支持在MCP Client中创建和编辑Word、Excel、Powerpoint文档。

1773. **[dicom-mcp](https://github.com/ChristianHinge/dicom-mcp)** - ⭐ 81
   Model Context Protocol (MCP) for interacting with dicom servers (PACS etc.)

1774. **[ramparts](https://github.com/highflame-ai/ramparts)** - ⭐ 81
   mcp scan that scans any mcp server for indirect attack vectors and security or configuration vulnerabilities

1775. **[anki-mcp-server](https://github.com/CamdenClark/anki-mcp-server)** - ⭐ 81
   A model context protocol server that connects to Anki through AnkiConnect

1776. **[cursor-rust-tools](https://github.com/terhechte/cursor-rust-tools)** - ⭐ 81
   A MCP server to allow the LLM in Cursor to access Rust Analyzer, Crate Docs and Cargo Commands.

1777. **[mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins)** - ⭐ 81
   The Model Context Protocol (MCP) is an open-source implementation that bridges Jenkins with AI language models following Anthropic's MCP specification. This project enables secure, contextual AI interactions with Jenkins tools while maintaining data privacy and security.

1778. **[rohlik-mcp](https://github.com/tomaspavlin/rohlik-mcp)** - ⭐ 80
   MCP server that lets you shop groceries across the Rohlik Group platforms (Rohlik.cz, Knuspr.de, Gurkerl.at, Kifli.hu, Sezamo.ro)

1779. **[mcp-server](https://github.com/keboola/mcp-server)** - ⭐ 80
   Model Context Protocol (MCP) Server for the Keboola Platform

1780. **[mcp-server-stability-ai](https://github.com/tadasant/mcp-server-stability-ai)** - ⭐ 80
   MCP Server integrating MCP Clients with Stability AI-powered image manipulation functionalities: generate, edit, upscale, and more.

1781. **[aws-security-mcp](https://github.com/groovyBugify/aws-security-mcp)** - ⭐ 80
   A Model Context Protocol server that connects AI assistants like Claude to AWS security services, allowing them to autonomously query, inspect, and analyze AWS infrastructure for security issues and misconfigurations.

1782. **[MCPay](https://github.com/microchipgnu/MCPay)** - ⭐ 80
   Open-source Infrastructure for MCP and x402

1783. **[mcp-discovery](https://github.com/rust-mcp-stack/mcp-discovery)** - ⭐ 80
   A command-line tool written in Rust for discovering and documenting MCP Server capabilities.

1784. **[NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server)** - ⭐ 80
   A Model Context Protocol (MCP) server for NASA APIs, providing a standardized interface for AI models to interact with NASA's vast array of data sources.

1785. **[actual-mcp](https://github.com/s-stefanov/actual-mcp)** - ⭐ 80
   Model Context Protocol for Actual Budget API

1786. **[awesome-osint-mcp-servers](https://github.com/soxoj/awesome-osint-mcp-servers)** - ⭐ 80
   A curated list of OSINT MCP servers. Pull requests are welcomed!

1787. **[mcp-metatrader5-server](https://github.com/Qoyyuum/mcp-metatrader5-server)** - ⭐ 80
   A Model Context Protocol (MCP) server for interacting with the MetaTrader 5 trading platform. This server provides AI assistants with tools and resources to access market data, perform trading operations, and analyze trading history.

1788. **[x64dbgMCP](https://github.com/Wasdubya/x64dbgMCP)** - ⭐ 80
   Model Context Protocol for x64dbg & x32dbg

1789. **[esankhyiki-mcp](https://github.com/nso-india/esankhyiki-mcp)** - ⭐ 80
   This repository consists of Source Code for Model Context Protocol (MCP) Pilot Project being undertaken by Ministry of Statistics and Programme Implementation and source code for the same is being shared under GNU General Public License.

1790. **[fastmcp-boilerplate](https://github.com/punkpeye/fastmcp-boilerplate)** - ⭐ 79
   A simple MCP server built using FastMCP, TypeScript, ESLint, and Prettier.

1791. **[github-chat-mcp](https://github.com/AsyncFuncAI/github-chat-mcp)** - ⭐ 79
   A Model Context Protocol (MCP) for analyzing and querying GitHub repositories using the GitHub Chat API.

1792. **[codemirror-mcp](https://github.com/marimo-team/codemirror-mcp)** - ⭐ 79
   CodeMirror extension to hook up a Model Context Provider (MCP)

1793. **[jira-mcp](https://github.com/nguyenvanduocit/jira-mcp)** - ⭐ 79
   A Go-based MCP (Model Control Protocol) connector for Jira that enables AI assistants like Claude to interact with Atlassian Jira. This tool provides a seamless interface for AI models to perform common Jira operations including issue management, sprint planning, and workflow transitions.

1794. **[ls-mcp](https://github.com/lirantal/ls-mcp)** - ⭐ 79
   List MCP Server configurations in your system used by AI applications like Cursor, Claude Desktop, VS Code and others

1795. **[mcp-server-any-openapi](https://github.com/baryhuang/mcp-server-any-openapi)** - ⭐ 79
   A MCP server that enables Claude to discover and call any API endpoint through semantic search. Intelligently chunks OpenAPI specifications to handle large API documentation, with built-in request execution capabilities. Perfect for integrating private APIs with Claude Desktop.

1796. **[stock-mcp](https://github.com/huweihua123/stock-mcp)** - ⭐ 79
   专业的金融市场数据 MCP 服务器 - 支持A股/美股/加密货币，原生 MCP 协议，AI Agent 友好

1797. **[mcp-azure-devops](https://github.com/Vortiago/mcp-azure-devops)** - ⭐ 78
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Azure DevOps services via Python SDK.

1798. **[mcp-monitor](https://github.com/seekrays/mcp-monitor)** - ⭐ 78
   A system monitoring tool that exposes system metrics via the Model Context Protocol (MCP). This tool allows LLMs to retrieve real-time system information through an MCP-compatible interface.

1799. **[mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms)** - ⭐ 78
   Version 2.2 - 54 tools available - an MCP server for interacting with the Canvas LMS API. This server allows you to manage courses, assignments, enrollments, and grades within Canvas.

1800. **[woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server)** - ⭐ 78
   A WooCommerce (MCP) Model Context Protocol server

1801. **[gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp)** - ⭐ 78
   Interact seamlessly with GitLab repositories to manage merge requests and issues. Fetch details, add comments, and streamline your code review process with ease.

1802. **[mcp-reticle](https://github.com/soth-ai/mcp-reticle)** - ⭐ 78
   Reticle intercepts, visualizes, and profiles JSON-RPC traffic between your LLM and MCP servers in real-time, with zero latency overhead. Stop debugging blind. Start seeing everything.

1803. **[fabric-mcp](https://github.com/ksylvan/fabric-mcp)** - ⭐ 78
   Fabric MCP Server: Seamlessly integrate Fabric AI capabilities into MCP-enabled tools like IDEs and chat interfaces.

1804. **[agent-toolkit](https://github.com/sanity-io/agent-toolkit)** - ⭐ 78
   Collection of resources to help AI agents build better with Sanity.

1805. **[lucidity-mcp](https://github.com/hyperb1iss/lucidity-mcp)** - ⭐ 77
   AI-powered code quality analysis using MCP to help AI assistants review code more effectively. Analyze git changes for complexity, security issues, and more through structured prompts.

1806. **[advanced-unity-mcp](https://github.com/codemaestroai/advanced-unity-mcp)** - ⭐ 77
   Public repository for Advanced Unity MCP by Code Maestro (www.code-maestro.com).

1807. **[visual-ui-debug-agent-mcp](https://github.com/samihalawa/visual-ui-debug-agent-mcp)** - ⭐ 77
   VUDA is an autonomous debugging agent that empowers AI models to visually analyze, test, and debug web

1808. **[devex](https://github.com/ParthKapoor-dev/devex)** - ⭐ 77
   ⚡️ Devex — A Fast, Secure, and Scalable Repl-as-a-Service Platform built for Developers 🚀

1809. **[mcp-openapi](https://github.com/ReAPI-com/mcp-openapi)** - ⭐ 77
   OpenAPI specification MCP server.

1810. **[tester-mcp-client](https://github.com/apify/tester-mcp-client)** - ⭐ 77
   Model Context Protocol (MCP) Client for Apify's Actors

1811. **[terminal_server](https://github.com/theailanguage/terminal_server)** - ⭐ 77
   MCP server that can execute terminal commands

1812. **[google-cloud-mcp](https://github.com/krzko/google-cloud-mcp)** - ⭐ 77
   🤖 A Model Context Protocol (MCP) server for Google Cloud (GCP)

1813. **[mcp-reticle](https://github.com/LabTerminal/mcp-reticle)** - ⭐ 77
   Reticle intercepts, visualizes, and profiles JSON-RPC traffic between your LLM and MCP servers in real-time, with zero latency overhead. Stop debugging blind. Start seeing everything.

1814. **[mcp-server](https://github.com/cap-js/mcp-server)** - ⭐ 77
   MCP server for AI-assisted development of CAP applications

1815. **[mcp-gemini-google-search](https://github.com/yukukotani/mcp-gemini-google-search)** - ⭐ 77
   MCP server for Google Search integration using Gemini's built-in search capabilities

1816. **[youtrack-mcp](https://github.com/tonyzorin/youtrack-mcp)** - ⭐ 77
   Model Context Protocol Server for YouTrack - Multi-platform support (ARM64/Apple Silicon + AMD64) with comprehensive API integration

1817. **[Mureka-mcp](https://github.com/SkyworkAI/Mureka-mcp)** - ⭐ 77
   generate lyrics, song and background music(instrumental). Model Context Protocol (MCP) server.

1818. **[spring-ai](https://github.com/eazybytes/spring-ai)** - ⭐ 77
   From Java Dev to AI Engineer: Spring AI Fast Track

1819. **[ols4](https://github.com/EBISPOT/ols4)** - ⭐ 77
   The EMBL-EBI Ontology Lookup Service (OLS)

1820. **[fullstack-langgraph-nextjs-agent](https://github.com/agentailor/fullstack-langgraph-nextjs-agent)** - ⭐ 77
     Production-ready Next.js template for building AI agents with LangGraph.js. Features MCP integration for dynamic tool loading, human-in-the-loop tool approval, persistent conversation memory   with PostgreSQL, and real-time streaming responses. Built with TypeScript, React, Prisma, and Tailwind CSS.

1821. **[claude-desktop-extension-bear-notes](https://github.com/vasylenko/claude-desktop-extension-bear-notes)** - ⭐ 77
   Claude Desktop extension with bundled MCP Server for Bear note taking app

1822. **[awesome-mcp-servers-devops](https://github.com/WagnerAgent/awesome-mcp-servers-devops)** - ⭐ 77
   A curated, DevOps-focused list of Model Context Protocol (MCP) servers—covering source control, IaC, Kubernetes, CI/CD, cloud, observability, security, and collaboration—with a bias toward maintained, production-ready integrations.

1823. **[codeglide-mcpgen](https://github.com/CodeGlide/codeglide-mcpgen)** - ⭐ 76
   Generation of Secure MCP (Model Context Protocol) Servers from API source code at Scale

1824. **[mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci)** - ⭐ 76
   A specialized server implementation for the Model Context Protocol (MCP) designed to integrate with CircleCI's development workflow. This project serves as a bridge between CircleCI's infrastructure and the Model Context Protocol, enabling enhanced AI-powered development experiences.

1825. **[ExternalAttacker-MCP](https://github.com/MorDavid/ExternalAttacker-MCP)** - ⭐ 76
   A modular external attack surface mapping tool integrating tools for automated reconnaissance and bug bounty workflows.

1826. **[imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server)** - ⭐ 76
   An MCP server that provides safe access to your iMessage database through Model Context Protocol (MCP). This server is built with the FastMCP framework and the imessagedb library, enabling LLMs to query and analyze iMessage conversations with proper phone number validation and attachment handling.

1827. **[mcp-llm](https://github.com/sammcj/mcp-llm)** - ⭐ 76
    An MCP server that provides LLMs access to other LLMs

1828. **[code-to-tree](https://github.com/micl2e2/code-to-tree)** - ⭐ 76
   A runtime-free MCP server that converts source code into AST🌲, regardless of language.

1829. **[agentic-tools-mcp](https://github.com/Pimzino/agentic-tools-mcp)** - ⭐ 76
   A comprehensive Model Context Protocol (MCP) server providing AI assistants with powerful task management and agent memories capabilities with project-specific storage.

1830. **[cursor10x-mcp](https://github.com/aiurda/cursor10x-mcp)** - ⭐ 75
   The Cursor10x MCP is a persistent multi-dimensional memory system for Cursor that enhances AI assistants with conversation context, project history, and code relationships across sessions.

1831. **[sample-agents-with-nova-act-and-mcp](https://github.com/aws-samples/sample-agents-with-nova-act-and-mcp)** - ⭐ 75
   Discover how to build agents that can perform actions on websites by combining Amazon Nova Act with Model Context Protocol (MCP).

1832. **[agentic-coding](https://github.com/sammcj/agentic-coding)** - ⭐ 75
   Agentic Coding Rules, Templates etc...

1833. **[ChEMBL-MCP-Server](https://github.com/Augmented-Nature/ChEMBL-MCP-Server)** - ⭐ 75
   A comprehensive Model Context Protocol (MCP) server providing advanced access to the ChEMBL chemical database.

1834. **[mcp-forge](https://github.com/achetronic/mcp-forge)** - ⭐ 75
   A complete MCP server template that include vitamins (oauth authentication included)

1835. **[zed-mcp-server-github](https://github.com/LoamStudios/zed-mcp-server-github)** - ⭐ 75
   A GitHub MCP Server extension for Zed

1836. **[glif-mcp-server](https://github.com/glifxyz/glif-mcp-server)** - ⭐ 75
   Easily run glif.app AI workflows inside your LLM: image generators, memes, selfies, and more. Glif supports all major multimedia AI models inside one app

1837. **[bridge4simulator](https://github.com/AppGram/bridge4simulator)** - ⭐ 75
   An MCP (Model Context Protocol) server that enables AI assistants to control iOS Simulator. Seamlessly integrates with Claude Desktop, Cursor, Claude Code, and other MCP-compatible clients.

1838. **[bing-search-mcp](https://github.com/leehanchung/bing-search-mcp)** - ⭐ 75
   MCP Server for Bing Search API

1839. **[ida-mcp-rs](https://github.com/blacktop/ida-mcp-rs)** - ⭐ 75
   Headless IDA MCP Server

1840. **[surrealmcp](https://github.com/surrealdb/surrealmcp)** - ⭐ 75
   The official MCP server for SurrealDB

1841. **[wecom-bot-mcp-server](https://github.com/loonghao/wecom-bot-mcp-server)** - ⭐ 75
   A Python server implementation for WeCom (WeChat Work) bot that follows the Model Context Protocol (MCP). This server provides a standardized interface for handling automated messaging and context-aware interactions within enterprise WeChat environments.

1842. **[mcp-llms-txt-explorer](https://github.com/thedaviddias/mcp-llms-txt-explorer)** - ⭐ 74
   MCP to explore websites with llms.txt files

1843. **[jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server)** - ⭐ 74
   This is an implementation project of a JVM-based MCP (Model Context Protocol) server. The project aims to provide a standardized MCP server implementation for the JVM platform, enabling AI models to better interact with the Java ecosystem.

1844. **[mcp-kafka](https://github.com/kanapuli/mcp-kafka)** - ⭐ 74
   A Model Context Protocol Server to perform Kafka client operations

1845. **[SillyTavern-MCP-Client](https://github.com/bmen25124/SillyTavern-MCP-Client)** - ⭐ 74
   An extension of MCP for SillyTavern.

1846. **[ophis](https://github.com/njayp/ophis)** - ⭐ 74
   Transform any Cobra CLI into an MCP server

1847. **[HopperMCP](https://github.com/MxIris-Reverse-Engineering/HopperMCP)** - ⭐ 74
   A Model Context Protocol server for Hopper Disassembler

1848. **[masquerade](https://github.com/postralai/masquerade)** - ⭐ 73
   The Privacy Firewall for LLMs

1849. **[mcp-fal](https://github.com/am0y/mcp-fal)** - ⭐ 73
   A Model Context Protocol (MCP) server for interacting with fal.ai models and services.

1850. **[bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp)** - ⭐ 73
   Bitcoin & Lightning Network MCP Server.

1851. **[choturobo](https://github.com/vishalmysore/choturobo)** - ⭐ 73
   Integrate Arduino-based robotics (using the NodeMCU ESP32 or Arduino Nano 368 board) with AI using the MCP (Model Context Protocol) framework from Claude Anthropic

1852. **[rust-mcp-schema](https://github.com/rust-mcp-stack/rust-mcp-schema)** - ⭐ 72
   A type-safe implementation of the official Model Context Protocol (MCP) schema in Rust.

1853. **[conductor-tasks](https://github.com/hridaya423/conductor-tasks)** - ⭐ 72
   A task management system designed for AI development

1854. **[codebase-mcp](https://github.com/DeDeveloper23/codebase-mcp)** - ⭐ 72
   Model Context Protocol implementation for retrieving codebases using RepoMix

1855. **[ytt-mcp](https://github.com/cottongeeks/ytt-mcp)** - ⭐ 72
   MCP server to fetch YouTube transcripts

1856. **[ccxt-mcp](https://github.com/lazy-dinosaur/ccxt-mcp)** - ⭐ 72
   CCXT MCP Server bridges the gap between AI models and cryptocurrency trading by providing a standardized interface through the Model Context Protocol. Created to empower automated trading strategies, this tool allows AI assistants like Claude and GPT to directly interact with over 100 cryptocurrency exchanges without requiring users to write comple

1857. **[gopher-mcp](https://github.com/GopherSecurity/gopher-mcp)** - ⭐ 72
   MCP C++ SDK - Model Context Protocol implementation in CPP with enterprise-grade security, visibility and connectivity.

1858. **[ncp](https://github.com/portel-dev/ncp)** - ⭐ 72
   Natural Context Provider (NCP). Your MCPs, supercharged. Find any tool instantly, load on demand, run on schedule, ready for any   client. Smart loading saves tokens and energy.

1859. **[mcp-client-capabilities](https://github.com/apify/mcp-client-capabilities)** - ⭐ 72
   Index of all Model Context Protocol (MCP) clients and their capabilities

1860. **[iron-manus-mcp](https://github.com/dnnyngyen/iron-manus-mcp)** - ⭐ 71
   Iron Manus MCP (+ J.A.R.V.I.S. Orchestration)

1861. **[chat.md](https://github.com/rusiaaman/chat.md)** - ⭐ 71
   An md file as a chat interface and editable history in one.

1862. **[MCP-wolfram-alpha](https://github.com/SecretiveShell/MCP-wolfram-alpha)** - ⭐ 71
   Connect your chat repl to wolfram alpha computational intelligence

1863. **[Custom-MCP-Server](https://github.com/Sharan-Kumar-R/Custom-MCP-Server)** - ⭐ 71
   MCP server for scraping LinkedIn, Facebook, Instagram profiles and Google search.

1864. **[template-mcp-server](https://github.com/mcpdotdirect/template-mcp-server)** - ⭐ 71
   Template to quickly set up your own MCP server 

1865. **[windbg-ext-mcp](https://github.com/NadavLor/windbg-ext-mcp)** - ⭐ 71
   WinDbg-ext-MCP bridges your favorite LLM client (like Cursor, Claude, or VS Code) with WinDbg, enabling real-time, AI assisted kernel debugging. Write prompts in your AI coding assistant and receive instant, context-aware analysis and insights from your live kernel debugging session.

1866. **[math-mcp](https://github.com/EthanHenrickson/math-mcp)** - ⭐ 71
   A Model Context Protocol (MCP) server that provides basic mathematical and statistical functions to Large Language Models (LLMs). This server enables LLMs to perform accurate numerical calculations through a simple API.

1867. **[mcp-hetzner](https://github.com/dkruyt/mcp-hetzner)** - ⭐ 71
   A Model Context Protocol (MCP) server for interacting with the Hetzner Cloud API. This server allows language models to manage Hetzner Cloud resources through structured functions.

1868. **[mcp](https://github.com/vuetifyjs/mcp)** - ⭐ 71
   🤖 A Model Context Protocol (MCP) library for use with Agentic chat bots

1869. **[sanity-mcp-server](https://github.com/sanity-io/sanity-mcp-server)** - ⭐ 71
   Deprecated: Use the remote MCP server at https://mcp.sanity.io instead.

1870. **[airtable-mcp](https://github.com/felores/airtable-mcp)** - ⭐ 70
   Search, create and update Airtable bases, tables, fields, and records using Claude Desktop and MCP (Model Context Protocol) clients

1871. **[railway-mcp](https://github.com/jason-tan-swe/railway-mcp)** - ⭐ 70
   An unofficial and community-built MCP server for integrating with https://railway.app

1872. **[MCP-server-Deepseek_R1](https://github.com/66julienmartin/MCP-server-Deepseek_R1)** - ⭐ 70
   A Model Context Protocol (MCP) server implementation connecting Claude Desktop with DeepSeek's language models (R1/V3)

1873. **[BurpSuite-MCP-Server](https://github.com/X3r0K/BurpSuite-MCP-Server)** - ⭐ 70
   BurpSuite MCP Server:  A powerful Model Context Protocol (MCP) server implementation for BurpSuite, providing programmatic access to Burp's core functionalities.

1874. **[github-brain](https://github.com/wham/github-brain)** - ⭐ 70
   An experimental GitHub MCP server with local database.

1875. **[mcp-server-email](https://github.com/Shy2593666979/mcp-server-email)** - ⭐ 70
   一个基于 MCP (Model Context Protocol) 的邮件服务，支持 LLM 发送带附件的电子邮件及在指定目录中搜索文件。提供安全的 SMTP 传输、多收件人支持和附件模式匹配搜索功能，适用于 Gmail、Outlook、Yahoo、QQ 邮箱和网易 126 邮箱等主流邮箱服务。

1876. **[perplexity-mcp-zerver](https://github.com/wysh3/perplexity-mcp-zerver)** - ⭐ 70
   MCP web search using perplexity without any API KEYS 

1877. **[unreal-mcp](https://github.com/runreal/unreal-mcp)** - ⭐ 70
   MCP server for Unreal Engine that uses Unreal Python Remote Execution

1878. **[mcpc](https://github.com/mcpc-tech/mcpc)** - ⭐ 70
   Build agentic-MCP servers by composing existing MCP tools.

1879. **[django-ai-boost](https://github.com/vintasoftware/django-ai-boost)** - ⭐ 70
   A MCP server for Django applications, inspired by Laravel Boost.

1880. **[gdai-mcp-plugin-godot](https://github.com/3ddelano/gdai-mcp-plugin-godot)** - ⭐ 70
   A MCP server integration for Godot Engine that allows Claude, Cursor, Windsurf, VSCode, etc to perform actions like creating scenes, resources, scripts, reading errors and much more.

1881. **[unitree-go2-mcp-server](https://github.com/lpigeon/unitree-go2-mcp-server)** - ⭐ 70
   The Unitree Go2 MCP Server is a server built on the MCP that enables users to control the Unitree Go2 robot using natural language commands interpreted by a LLM.

1882. **[OmniMCP](https://github.com/OpenAdaptAI/OmniMCP)** - ⭐ 69
   OmniMCP uses Microsoft OmniParser and Model Context Protocol (MCP) to provide AI models with rich UI context and powerful interaction capabilities.

1883. **[mcp-client-python](https://github.com/alejandro-ao/mcp-client-python)** - ⭐ 69

1884. **[rtfmbro-mcp](https://github.com/marckrenn/rtfmbro-mcp)** - ⭐ 69
   rtfmbro provides always-up-to-date, version-specific package documentation as context for coding agents. An alternative to context7

1885. **[ig-mcp](https://github.com/jlbadano/ig-mcp)** - ⭐ 69
   A production-ready Model Context Protocol (MCP) server that enables AI applications to seamlessly interact with Instagram Business accounts.

1886. **[ynab-mcp-server](https://github.com/calebl/ynab-mcp-server)** - ⭐ 69
   Model Context Protocol for YNAB (you need a budget)

1887. **[slither-mcp](https://github.com/trailofbits/slither-mcp)** - ⭐ 69
   MCP server for Slither static analysis of Solidity smart contracts

1888. **[markitdown_mcp_server](https://github.com/KorigamiK/markitdown_mcp_server)** - ⭐ 69
   A Model Context Protocol (MCP) server that converts various file formats to Markdown using the MarkItDown utility.

1889. **[tauri-plugin-mcp](https://github.com/P3GLEG/tauri-plugin-mcp)** - ⭐ 69
   Allows AI agents (e.g., Cursor, Claude Code) to debug within Tauri apps via screenshot capture, window management, DOM access, and simulated user inputs.

1890. **[monarch-mcp-server](https://github.com/robcerda/monarch-mcp-server)** - ⭐ 69
   MCP Server for use with Monarch Money

1891. **[meta-mcp](https://github.com/brijr/meta-mcp)** - ⭐ 69
   MCP Server for connecting to the Meta Marketing API

1892. **[mcp-velociraptor](https://github.com/mgreen27/mcp-velociraptor)** - ⭐ 68
   VelociraptorMCP is a Model Context Protocol bridge for exposing LLMs to MCP clients.

1893. **[blender-open-mcp](https://github.com/dhakalnirajan/blender-open-mcp)** - ⭐ 68
   Open Models MCP for Blender Using Ollama

1894. **[ClueoMCP](https://github.com/ClueoFoundation/ClueoMCP)** - ⭐ 68
   🎭 The Personality Layer for LLMs- Transform any MCP-compatible AI with rich, consistent personalities powered by Clueo's Big Five personality engine.

1895. **[vibe-blocks-mcp](https://github.com/majidmanzarpour/vibe-blocks-mcp)** - ⭐ 68
   Connects Roblox Studio to AI coding editors via the Model Context Protocol (MCP), enabling AI-assisted game development within your Roblox Studio environment.

1896. **[ollama-mcp-client](https://github.com/mihirrd/ollama-mcp-client)** - ⭐ 68
   MCP client for local ollama models

1897. **[agenite](https://github.com/subeshb1/agenite)** - ⭐ 68
   🤖 Build powerful AI agents with TypeScript. Agenite makes it easy to create, compose, and control AI agents with first-class support for tools, streaming, and multi-agent architectures. Switch seamlessly between providers like OpenAI, Anthropic, AWS Bedrock, and Ollama.

1898. **[openfoam-mcp-server](https://github.com/webworn/openfoam-mcp-server)** - ⭐ 68
   LLM-powered OpenFOAM MCP server for intelligent CFD education with Socratic questioning and expert error resolution

1899. **[raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server)** - ⭐ 68
   An integration that allows LLMs to interact with Raindrop.io bookmarks using the Model Context Protocol (MCP).

1900. **[mcp-openmemory](https://github.com/baryhuang/mcp-openmemory)** - ⭐ 68
   Simple standalone MCP server giving Claude the ability to remember your conversations and learn from them over time.

1901. **[airtable-mcp](https://github.com/rashidazarang/airtable-mcp)** - ⭐ 68
   Airtable integration for AI-powered applications via Anthropic's Model Context Protocol (MCP)

1902. **[uml-mcp](https://github.com/antoinebou12/uml-mcp)** - ⭐ 68
   UML-MCP Server is a UML diagram generation tool based on MCP (Model Context Protocol), which can help users generate various types of UML diagrams through natural language description or directly writing PlantUML and Mermaid and Kroki

1903. **[XActions](https://github.com/nirholas/XActions)** - ⭐ 68
   ⚡ The Complete X/Twitter Automation Toolkit — Scrapers, MCP server for AI agents (Claude/GPT), CLI, browser scripts. No API fees. Open source. Unfollow people who don't follow back. Monitor real-time analytics. Auto follow, like, comment, scrape, without API.

1904. **[google-ai-mode-mcp](https://github.com/PleasePrompto/google-ai-mode-mcp)** - ⭐ 68
   MCP server for free Google AI Mode search with citations. Query optimization, CAPTCHA handling, multi-agent support. Works with Claude Code, Cursor, Cline, Windsurf.

1905. **[MCPhoenix](https://github.com/jmanhype/MCPhoenix)** - ⭐ 67
   A simplified implementation of the Model Context Protocol (MCP) server using Elixir's Phoenix Framework.

1906. **[mcp_gradio_client](https://github.com/justjoehere/mcp_gradio_client)** - ⭐ 67
   This is a proof of concept repo on how to create a gradio UI using the Model Context Protocol Client Python SDK.

1907. **[gmail-mcp-server](https://github.com/jasonsum/gmail-mcp-server)** - ⭐ 67
   Model Context Protocol (MCP) server for Gmail

1908. **[optuna-mcp](https://github.com/optuna/optuna-mcp)** - ⭐ 67
   The Optuna MCP Server is a Model Context Protocol (MCP) server to interact with Optuna APIs.

1909. **[anilist-mcp](https://github.com/yuna0x0/anilist-mcp)** - ⭐ 67
   AniList MCP server for accessing anime and manga data

1910. **[piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server)** - ⭐ 67
   A TypeScript implementation of a Model Context Protocol (MCP) server that integrates with PiAPI's API. PiAPI makes user able to generate media content with Midjourney/Flux/Kling/LumaLabs/Udio/Chrip/Trellis directly from Claude or any other MCP-compatible apps.

1911. **[deepseek-thinker-mcp](https://github.com/ruixingshi/deepseek-thinker-mcp)** - ⭐ 67
   A MCP provider Deepseek reasoning content to MCP-enabled AI Clients, like Claude Desktop. Supports access to Deepseek's CoT from the Deepseek API service or a local Ollama server.

1912. **[deepview-mcp](https://github.com/ai-1st/deepview-mcp)** - ⭐ 67
   DeepView MCP is a Model Context Protocol server that enables IDEs like Cursor and Windsurf to analyze large codebases using Gemini 2.5 Pro's extensive context window.

1913. **[m3](https://github.com/rafiattrach/m3)** - ⭐ 67
   🏥🤖 Query MIMIC-IV medical data using natural language through Model Context Protocol (MCP). Transform healthcare research with AI-powered database interactions - supports both local MIMIC-IV SQLite demo dataset and full BigQuery datasets.

1914. **[mcp-wolframalpha](https://github.com/akalaric/mcp-wolframalpha)** - ⭐ 67
   A Python-powered Model Context Protocol MCP server and client that uses Wolfram Alpha via API.

1915. **[lazy-mcp](https://github.com/voicetreelab/lazy-mcp)** - ⭐ 67
     MCP proxy server with lazy loading support - reduces context usage through on-demand tool activation

1916. **[mcp-discord](https://github.com/barryyip0625/mcp-discord)** - ⭐ 67
   Implement Discord MCP server enabling AI assistants to interact with the Discord platform.

1917. **[junos-mcp-server](https://github.com/Juniper/junos-mcp-server)** - ⭐ 67
   This is a Junos Model Context Protocol (MCP) Server project that provides a bridge between MCP-compatible clients (like Claude Desktop) and Juniper Junos network devices.

1918. **[mcp-server-datahub](https://github.com/acryldata/mcp-server-datahub)** - ⭐ 66
   The official Model Context Protocol (MCP) server for DataHub (https://datahub.com)

1919. **[boilerplate-mcp-server](https://github.com/aashari/boilerplate-mcp-server)** - ⭐ 66
   TypeScript Model Context Protocol (MCP) server boilerplate providing IP lookup tools/resources. Includes CLI support and extensible structure for connecting AI systems (LLMs) to external data sources like ip-api.com. Ideal template for creating new MCP integrations via Node.js.

1920. **[awesome-mcp-best-practices](https://github.com/lirantal/awesome-mcp-best-practices)** - ⭐ 66
   Build Awesome MCPs with Awesome Best Practices for MCP Servers and MCP Clients

1921. **[QuickMCP](https://github.com/gunpal5/QuickMCP)** - ⭐ 66
   Effortlessly Build Model Context Protocol Servers with OpenAPI or Swagger or Google Discovery Specifications

1922. **[nautex](https://github.com/hmldns/nautex)** - ⭐ 66
   MCP server for guiding Coding Agents via end-to-end requirements to implementation plan pipeline

1923. **[mcp-server-node](https://github.com/lucianoayres/mcp-server-node)** - ⭐ 66
   MCP Server implemented in JavaScript using Node.js that demonstrates how to build an MCP server with a custom prompt and custom tools, including one that loads an environment variable from a configuration file, to integrate seamlessly with AI-assisted environments like Cursor IDE.

1924. **[turbomcp](https://github.com/Epistates/turbomcp)** - ⭐ 66
   A full featured, enterprise grade rust MCP SDK

1925. **[wasmcp](https://github.com/wasmcp/wasmcp)** - ⭐ 66
   Build MCP servers with WebAssembly components

1926. **[CanvasMCPClient](https://github.com/n00bvn/CanvasMCPClient)** - ⭐ 66
   Canvas MCP Client is an open-source, self-hostable dashboard application built around an infinite, zoomable, and pannable canvas. It provides a unified interface for interacting with multiple MCP (Model Context Protocol) servers through a flexible, widget-based system.

1927. **[mcp-tutorials](https://github.com/chenmingyong0423/mcp-tutorials)** - ⭐ 65
   Model Context Protocol(MCP) 中文教程讲解

1928. **[community-servers](https://github.com/mcp-get/community-servers)** - ⭐ 65
   This repository contains a collection of community-maintained Model Context Protocol (MCP) servers. All servers are automatically listed on the MCP Get registry and can be viewed and installed via CLI

1929. **[flapi](https://github.com/DataZooDE/flapi)** - ⭐ 65
   API Framework heavily relying on the power of DuckDB and DuckDB extensions. Ready to build performant and cost-efficient APIs on top of BigQuery or Snowflake  for AI Agents and Data Apps

1930. **[shinzo-ts](https://github.com/shinzo-labs/shinzo-ts)** - ⭐ 65
   TypeScript SDK for MCP server observability, built on OpenTelemetry. Gain insight into agent usage patterns, contextualize tool calls, and analyze server performance across platforms. Integrate with any OpenTelemetry ingest service including the Shinzo platform.

1931. **[nav2_mcp_server](https://github.com/ajtudela/nav2_mcp_server)** - ⭐ 65
   MCP server that provides tools and resources to control and monitor robots using Nav2.

1932. **[mcp4k](https://github.com/ondrsh/mcp4k)** - ⭐ 65
   Compiler-driven MCP framework for Kotlin Multiplatform

1933. **[deep-research-mcp-server](https://github.com/ssdeanx/deep-research-mcp-server)** - ⭐ 65
   MCP Deep Research Server using Gemini creating a Research AI Agent

1934. **[one-search-mcp](https://github.com/yokingma/one-search-mcp)** - ⭐ 65
   🚀 OneSearch MCP Server: Web Search & Scraper & Extract,  Support agent-browser, SearXNG, Tavily, DuckDuckGo, Bing, etc.

1935. **[robot_MCP](https://github.com/IliaLarchenko/robot_MCP)** - ⭐ 65
   A simple MCP server for the SO-ARM100 control

1936. **[crash-mcp](https://github.com/nikkoxgonzales/crash-mcp)** - ⭐ 65
   MCP server for structured and efficient reasoning with step validation, branching, and revisions.

1937. **[mcp-arr](https://github.com/aplaceforallmystuff/mcp-arr)** - ⭐ 65
   MCP server for *arr media management suite

1938. **[interactive-brokers-mcp](https://github.com/code-rabi/interactive-brokers-mcp)** - ⭐ 65
   Interactive Brokers MCP Server

1939. **[lsd-mcp](https://github.com/lsd-so/lsd-mcp)** - ⭐ 64
   LSD Model Context Protocol

1940. **[svelte5-mcp](https://github.com/StudentOfJS/svelte5-mcp)** - ⭐ 64
   A specialized Model Context Protocol (MCP) server for Svelte 5 frontend development

1941. **[ollama-mcp-client](https://github.com/anjor/ollama-mcp-client)** - ⭐ 64

1942. **[mcp-config](https://github.com/marcusschiesser/mcp-config)** - ⭐ 64
   A CLI tool for easy installation of MCP servers and managing their configuration

1943. **[VibeShift](https://github.com/GroundNG/VibeShift)** - ⭐ 64
   [MCP Server] The Security Agent for AI assisted coding

1944. **[amazon-mcp](https://github.com/Fewsats/amazon-mcp)** - ⭐ 64
   Amazon MCP server to search & buy products using the L402

1945. **[ros2_mcp](https://github.com/wise-vision/ros2_mcp)** - ⭐ 64
   Advanced MCP Server ROS 2 bridging AI agents straight into robotics

1946. **[MySQL_MCP](https://github.com/guangxiangdebizi/MySQL_MCP)** - ⭐ 64
   这是一个功能强大且易用的MySQL数据库MCP（Model Context Protocol）服务器，让你的AI助手可以安全地进行完整的数据库操作，支持多数据库连接管理、增删改查、事务管理和智能回滚功能。

1947. **[sub-agents-mcp](https://github.com/shinpr/sub-agents-mcp)** - ⭐ 64
   Define task-specific AI sub-agents in Markdown for any MCP-compatible tool.

1948. **[roundtable](https://github.com/askbudi/roundtable)** - ⭐ 64
   Zero-configuration MCP server that unifies multiple AI coding assistants (Codex, Claude Code, Cursor, Gemini) through intelligent auto-discovery and standardized interface

1949. **[mcp-bear](https://github.com/jkawamoto/mcp-bear)** - ⭐ 64
   A MCP server for interacting with Bear note-taking software.

1950. **[mcp-gopls](https://github.com/hloiseau/mcp-gopls)** - ⭐ 64
   Model Context Protocol (MCP) server for Go using gopls – LSP-powered analysis, tests, coverage, and tooling.

1951. **[ableton-copilot-mcp](https://github.com/xiaolaa2/ableton-copilot-mcp)** - ⭐ 64
   An MCP server built on ableton-js enables AI assistants to control Ableton Live in real time, including Arrangement View operations such as song management, track control, MIDI editing, and audio recording, along with other capabilities.

1952. **[mcp_newsnow](https://github.com/sligter/mcp_newsnow)** - ⭐ 64
   一个基于 Model Context Protocol (MCP) 的新闻聚合服务器，通过 Newsnow API 提供多平台热点新闻和趋势话题。

1953. **[mcp-fhir](https://github.com/flexpa/mcp-fhir)** - ⭐ 63
   A Model Context Protocol implementation for FHIR

1954. **[mcp-sdk](https://github.com/AntigmaLabs/mcp-sdk)** - ⭐ 63
   Minimalistic Rust Implementation Of Model Context Protocol from Anthropic

1955. **[mcp-server-ccxt](https://github.com/Nayshins/mcp-server-ccxt)** - ⭐ 63
   Cryptocurrency Market Data MCP Server

1956. **[mcp-openapi-schema-explorer](https://github.com/kadykov/mcp-openapi-schema-explorer)** - ⭐ 63
   MCP server providing token-efficient access to OpenAPI/Swagger specs via MCP Resource Templates for client-side exploration.

1957. **[ipybox](https://github.com/gradion-ai/ipybox)** - ⭐ 63
   Python code execution sandbox with programmatic MCP tool calling (PTC)

1958. **[nutrient-dws-mcp-server](https://github.com/PSPDFKit/nutrient-dws-mcp-server)** - ⭐ 63
   A Model Context Protocol (MCP) server implementation that integrates with the Nutrient Document Web Service (DWS) Processor API, providing powerful PDF processing capabilities for AI assistants.

1959. **[tiny-mcp](https://github.com/wdndev/tiny-mcp)** - ⭐ 63
   Python 实现 MCP client / service

1960. **[voice-mcp-agent](https://github.com/den-vasyliev/voice-mcp-agent)** - ⭐ 63
   A voice assistant application built with the LiveKit Agents framework, capable of using Model Context Protocol (MCP) tools to interact with external services

1961. **[mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye)** - ⭐ 63
   A Model Context Protocol server that provides network asset information based on query conditions. This server allows LLMs to obtain network asset information and supports querying network asset information by zoomeye dork etc.

1962. **[usolver](https://github.com/sdiehl/usolver)** - ⭐ 62
   A model context protocol server for solving combinatorial optimization problems with logical and numerical constraints.

1963. **[mcp-durable-object-client](https://github.com/Dhravya/mcp-durable-object-client)** - ⭐ 62
   testing mcps

1964. **[mcp-miro](https://github.com/k-jarzyna/mcp-miro)** - ⭐ 62
   Miro integration for Model Context Protocol

1965. **[mcp-server-okppt](https://github.com/NeekChaw/mcp-server-okppt)** - ⭐ 62
   这个项目是一个基于MCP (Model Context Protocol) 的服务器工具，名为 "MCP OKPPT Server"。它的核心功能是允许大型语言模型（如Claude、GPT等）通过生成SVG图像来间接设计和创建PowerPoint演示文稿。工具负责将这些SVG图像高质量地插入到PPTX幻灯片中，并保留其矢量特性，确保图像在PowerPoint中可缩放且清晰。

1966. **[fred-mcp-server](https://github.com/stefanoamorelli/fred-mcp-server)** - ⭐ 62
   Open-source FRED MCP Server (Federal Reserve Economic Data)

1967. **[mcp-all-in-one](https://github.com/vtxf/mcp-all-in-one)** - ⭐ 62
   A powerful MCP (Model Context Protocol) service aggregator that combines multiple MCP services into a single unified MCP service with self-configuration capabilities.

1968. **[pydantic-rpc](https://github.com/i2y/pydantic-rpc)** - ⭐ 62
   PydanticRPC is a Python library for rapidly exposing Pydantic models as gRPC, ConnectRPC, and MCP services without protobuf files.

1969. **[contentful-mcp](https://github.com/ivo-toby/contentful-mcp)** - ⭐ 61
   MCP (Model Context Protocol) server for the Contentful Management API

1970. **[kollektiv-mcp](https://github.com/alexander-zuev/kollektiv-mcp)** - ⭐ 61
   Kollektiv MCP enables you to chat with and query your own documents directly from IDEs and MCP clients. Private, secure, and integrated into your favorite code editor

1971. **[ollama-mcp-db](https://github.com/robdodson/ollama-mcp-db)** - ⭐ 61
   An interactive chat interface that combines Ollama's LLM capabilities with PostgreSQL database access through the Model Context Protocol (MCP).

1972. **[mcp-cn](https://github.com/mengjian-github/mcp-cn)** - ⭐ 61
   MCP Hub 中国是一个专注于 Model Context Protocol (MCP) 生态的开源平台。它致力于汇聚全球优质的 MCP 服务,提供一站式的解决方案,包括服务发现、接入指南和使用示例,并建立完善的中文生态,欢迎开发者参与贡献和完善平台功能。

1973. **[yamcp](https://github.com/hamidra/yamcp)** - ⭐ 61
   Organize your MCP servers in local workspaces, share them as Yet-Another-MCP through a single command

1974. **[data-gov-il-mcp](https://github.com/DavidOsherdiagnostica/data-gov-il-mcp)** - ⭐ 61
   Advanced MCP server for seamless access to Israeli Government Open Data

1975. **[identity-service](https://github.com/agntcy/identity-service)** - ⭐ 61
   AGNTCY Identity Service serves as the central hub for managing and verifying digital identities for your Agentic Services. 

1976. **[xiaozhi-mcp-client](https://github.com/shadowcz007/xiaozhi-mcp-client)** - ⭐ 61
   可视化的配置和管理，给xiaozhi接入mcp

1977. **[mcpr](https://github.com/devOpifex/mcpr)** - ⭐ 61
   Model Context Protocol server and client for R

1978. **[mcp-auth-proxy](https://github.com/sigbit/mcp-auth-proxy)** - ⭐ 61
   MCP Auth Proxy is a secure OAuth 2.1 authentication proxy for Model Context Protocol (MCP) servers

1979. **[erpnext-mcp-server](https://github.com/rakeshgangwar/erpnext-mcp-server)** - ⭐ 61
   Connect AI assistants to your ERPNext instance via the Model Context Protocol (MCP) using the official Frappe API.

1980. **[dramacraft](https://github.com/whatyun/dramacraft)** - ⭐ 61
   DramaCraft 是一个专业的短剧视频编辑 MCP (Model Context Protocol) 服务，集成国产中文大模型 API，实现剪映的智能自动化编辑功能。项目已完成从视频分析到草稿生成的完整解决方案

1981. **[quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** - ⭐ 61
   The QuickBooks MCP Server lets AI assistants access QuickBooks data via a standard interface. It uses the Model Context Protocol to expose QBO features as callable tools, enabling developers to build AI apps that fetch real-time QBO data through MCP.

1982. **[rember-mcp](https://github.com/rember/rember-mcp)** - ⭐ 61
   A Model Context Protocol (MCP) server for Rember.

1983. **[mcp-server-tauri](https://github.com/hypothesi/mcp-server-tauri)** - ⭐ 61
   A Model Context Protocol (MCP) server and plugin for Tauri v2 development

1984. **[chess-mcp](https://github.com/pab1it0/chess-mcp)** - ⭐ 60
   A Model Context Protocol server for Chess.com's Published Data API.  This provides access to Chess.com player data, game records, and other public information through standardized MCP interfaces, allowing AI assistants to search and analyze chess information.

1985. **[devto-mcp](https://github.com/Arindam200/devto-mcp)** - ⭐ 60
   MCP Server of DevTo

1986. **[mcp-difyworkflow-server](https://github.com/gotoolkits/mcp-difyworkflow-server)** - ⭐ 60
   mcp-difyworkflow-server is an mcp server Tools application that implements the query and invocation of Dify workflows, supporting the on-demand operation of multiple custom Dify workflows.

1987. **[MediaWiki-MCP-Server](https://github.com/ProfessionalWiki/MediaWiki-MCP-Server)** - ⭐ 60
   Model Context Protocol (MCP) Server to connect your AI with any MediaWiki

1988. **[autosteer](https://github.com/notch-ai/autosteer)** - ⭐ 60
   Desktop app for multi-workspace Claude Code management

1989. **[nocodb-mcp-server](https://github.com/edwinbernadus/nocodb-mcp-server)** - ⭐ 60
   nocodb mcp server

1990. **[mcp-servers](https://github.com/pulsemcp/mcp-servers)** - ⭐ 60
   MCP (Model Context Protocol) Servers authored and maintained by the PulseMCP team. We build reliable servers thoughtfully designed specifically for MCP Client-powered workflows.

1991. **[mcp-clojure-sdk](https://github.com/unravel-team/mcp-clojure-sdk)** - ⭐ 59
   A Clojure SDK to create MCP servers (and eventually clients)

1992. **[ocaml-mcp-sdk](https://github.com/bmorphism/ocaml-mcp-sdk)** - ⭐ 59
   OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect library

1993. **[daipendency-mcp](https://github.com/daipendency/daipendency-mcp)** - ⭐ 59
   Model Context Protocol server for Daipendency

1994. **[smart-pet-with-mcp](https://github.com/shijianzhong/smart-pet-with-mcp)** - ⭐ 59
   一个桌宠形式的mcp client，可以对接任意mcp server,配合测试的mcp server 开源地址：https://github.com/shijianzhong/mcp-server-for-pc

1995. **[cline-mcp-memory-bank](https://github.com/dazeb/cline-mcp-memory-bank)** - ⭐ 59
   A memory system for Cline that tracks progress between conversations.

1996. **[shadcn-ui-mcp-server](https://github.com/ymadd/shadcn-ui-mcp-server)** - ⭐ 59
   MCP server for shadcn/ui component references

1997. **[mcp-server-echart](https://github.com/cnkanwei/mcp-server-echart)** - ⭐ 59
   基于 mcp-go 框架构建的 mcp 服务，它提供了一个能动态生成 ECharts 图表页面的工具。

1998. **[nutrient-document-engine-mcp-server](https://github.com/PSPDFKit/nutrient-document-engine-mcp-server)** - ⭐ 59
   A Model Context Protocol (MCP) server implementation exposes document processing capabilities through natural language, supporting both direct human interaction and AI agent tool calling.

1999. **[purple-mcp](https://github.com/Sentinel-One/purple-mcp)** - ⭐ 59
   Access SentinelOne's Purple AI and security services through the Model Context Protocol (MCP) - query alerts, vulnerabilities, misconfigurations, and inventory

2000. **[fastmail-mcp](https://github.com/MadLlama25/fastmail-mcp)** - ⭐ 59
   A Model Context Protocol (MCP) server that provides access to the Fastmail API, enabling AI assistants to interact with email, contacts, and calendar data. Includes a DXT (desktop extension) for Claude Desktop.

2001. **[xiaohongshu-mcp-python](https://github.com/luyike221/xiaohongshu-mcp-python)** - ⭐ 59
   xiaohongshu-mcp-python是一个基于现代Python技术栈开发的小红书内容自动化发布工具，通过Model Context Protocol (MCP)协议为AI客户端提供强大的小红书操作能力。  项目核心功能包括小红书账户登录管理、图文内容发布、视频内容发布、内容搜索与获取、帖子详情查看以及评论互动等。支持多种图片格式（JPG、PNG、GIF）和视频格式（MP4、MOV、AVI），既可处理本地文件路径，也支持HTTP/HTTPS链接，为用户提供灵活的内容发布方案。   该工具特别适合内容创作者、营销人员和开发者使用，能够显著提升小红书内容发布的效率和自动化程度。通过标准化的MCP接口，用户可以轻松地将小红书操作能力集成到各种AI工作流中，实现智能化的内容管理和发布。

2002. **[baml-agents](https://github.com/Elijas/baml-agents)** - ⭐ 59
   Building Agents with LLM structured generation (BAML), MCP Tools, and 12-Factor Agents principles

2003. **[EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP)** - ⭐ 59
   The first open-source Model Context Protocol server enabling AI assistants and applications to interact programmatically with EnergyPlus building energy simulation.

2004. **[clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server)** - ⭐ 59
   A Model Context Protocol (MCP) server for Microsoft Clarity

2005. **[claude-mermaid](https://github.com/veelenga/claude-mermaid)** - ⭐ 59
   MCP Server to previewing mermaid diagrams

2006. **[joplin-mcp](https://github.com/alondmnt/joplin-mcp)** - ⭐ 59
   MCP server for the Joplin note taking app

2007. **[claude-code-buddy](https://github.com/PCIRCLE-AI/claude-code-buddy)** - ⭐ 59
   MeMesh - Your AI memory mesh for Claude Code. Smart routing, persistent memory, and intelligent task management. (Formerly Claude Code Buddy)

2008. **[generative-ui-playground](https://github.com/CopilotKit/generative-ui-playground)** - ⭐ 59
   Interact with all three types of generative UI, all in one interface

2009. **[mcp-hub](https://github.com/lobstercare/mcp-hub)** - ⭐ 58
   A curated list of awesome Model Context Protocol (MCP) servers.

2010. **[ashra-mcp](https://github.com/getrupt/ashra-mcp)** - ⭐ 58
   A Model Context Protocol server for Ashra

2011. **[create-mcp-app](https://github.com/boguan/create-mcp-app)** - ⭐ 58
   A CLI tool for quickly scaffolding Model Context Protocol (MCP) server applications with TypeScript support and modern development tooling

2012. **[mcp-server-axiom](https://github.com/axiomhq/mcp-server-axiom)** - ⭐ 58
   Axiom Model Context Protocol Server

2013. **[quick-mcp-example](https://github.com/ALucek/quick-mcp-example)** - ⭐ 58
   Short and sweet example MCP server / client implementation for Tools, Resources and Prompts.

2014. **[mcpserver](https://github.com/2234839/mcpserver)** - ⭐ 58
   为claude code+glm 添加上眼睛

2015. **[mobile-mcp](https://github.com/runablehq/mobile-mcp)** - ⭐ 58
   A Model Context Protocol (MCP) server that provides mobile automation capabilities.

2016. **[MCP4EDA](https://github.com/NellyW8/MCP4EDA)** - ⭐ 58
   This is the Github Repo for the paper: MCP4EDA: LLM-Powered Model Context Protocol RTL-to-GDSII Automation with Backend Aware Synthesis Optimization. MCP server for a collection of open-source EDA tools

2017. **[fli](https://github.com/punitarani/fli)** - ⭐ 58
   Google Flights MCP and Python Library

2018. **[MCP-Dandan](https://github.com/82ch/MCP-Dandan)** - ⭐ 58
   MCP Security Solution for Agentic AI — real-time proxying, behavior analysis, and malicious tool detection

2019. **[job-searchoor](https://github.com/0xDAEF0F/job-searchoor)** - ⭐ 58
   A simple MCP server that delivers you jobs based on your needs

2020. **[mcp_server_gdb](https://github.com/pansila/mcp_server_gdb)** - ⭐ 58
   MCP Server to expose the GDB debugging capabilities

2021. **[mcd-mcp-server](https://github.com/M-China/mcd-mcp-server)** - ⭐ 58
   McDonald's China MCP Server Integration Guide

2022. **[zendesk-mcp-server](https://github.com/reminia/zendesk-mcp-server)** - ⭐ 58
   A Model Context Protocol server for Zendesk

2023. **[time-mcp](https://github.com/yokingma/time-mcp)** - ⭐ 58
   ⏰ Time MCP Server: Giving LLMs Time Awareness Capabilities

2024. **[WeChat-MCP](https://github.com/BiboyQG/WeChat-MCP)** - ⭐ 58
   WeChat-MCP: let Claude/ChatGPT and other AI assistants read and reply to WeChat for you

2025. **[metis-router](https://github.com/metis-mantis/metis-router)** - ⭐ 57
   MCP router and Web Based MCP client

2026. **[Archive-Agent](https://github.com/shredEngineer/Archive-Agent)** - ⭐ 57
   Find your files with natural language and ask questions.

2027. **[sublinear-time-solver](https://github.com/ruvnet/sublinear-time-solver)** - ⭐ 57
   Rust + WASM sublinear-time solver for asymmetric diagonally dominant systems. Exposes Neumann series, push, and hybrid random-walk algorithms with npm/npx CLI and Flow-Nexus HTTP streaming for swarm cost propagation and verification.

2028. **[mcp-server](https://github.com/UI5/mcp-server)** - ⭐ 57
   The UI5 MCP server improves the developer experience when working with agentic AI and the UI5 framework.

2029. **[zeromcp](https://github.com/mrexodia/zeromcp)** - ⭐ 57
   Zero-dependency MCP server implementation.

2030. **[adbfriend](https://github.com/mikepenz/adbfriend)** - ⭐ 57
   Android ADB CLI tool including integrated MCP Server with common adb actions used during development

2031. **[mcp-think-tank](https://github.com/flight505/mcp-think-tank)** - ⭐ 57
   MCP Think Tank is a powerful Model Context Protocol (MCP) server designed to enhance the capabilities of AI assistants like Cursor and Claude. It provides a structured environment for enhanced reasoning, persistent memory, and responsible tool usage.

2032. **[mcp-manager](https://github.com/MediaPublishing/mcp-manager)** - ⭐ 57
   A web-based GUI tool for managing Model Context Protocol (MCP) servers in Claude and Cursor

2033. **[FreeCAD-MCP](https://github.com/ATOI-Ming/FreeCAD-MCP)** - ⭐ 57
   FreeCAD plugin for automating model creation and control via Model Contro Protocol (MCP). Provides a MCP server,GUl panel, and client for running macros,managing documents, and adjusting views.

2034. **[joplin-mcp-server](https://github.com/dweigend/joplin-mcp-server)** - ⭐ 57
   A Model Context Protocol (MCP) Server for https://joplinapp.org/ that enables note access through the https://modelcontextprotocol.io. Perfect for integration with AI assistants like Claude.

2035. **[ticktick-mcp-server](https://github.com/alexarevalo9/ticktick-mcp-server)** - ⭐ 57
   A Model Context Protocol (MCP) server designed to integrate with the TickTick task management platform, enabling intelligent context-aware task operations and automation.

2036. **[mono-mcp](https://github.com/sin4ch/mono-mcp)** - ⭐ 57
   A comprehensive Model Context Protocol (MCP) server for Nigerian banking operations using the Mono Open Banking API.

2037. **[Alph](https://github.com/Aqualia/Alph)** - ⭐ 57
   Universal MCP Server Configuration Manager

2038. **[appium-mcp](https://github.com/Rahulec08/appium-mcp)** - ⭐ 57
   AI-powered mobile automation with Model Context Protocol (MCP) integration. Seamlessly control Android & iOS devices through Appium with intelligent visual element detection and recovery. Built for AI agents like Claude to perform complex mobile testing workflows.

2039. **[xc-mcp](https://github.com/conorluddy/xc-mcp)** - ⭐ 57
   XCode CLI MCP: Convenience wrapper for Xcode CLI tools & iOS Simulator. Progressive disclosure of tool responses to reduce context usage.  Use --mini param for build-only with tiny context footprint.

2040. **[mcp-gemini-search](https://github.com/arjunprabhulal/mcp-gemini-search)** - ⭐ 56
   Model Context Protocol (MCP) with Gemini 2.5 Pro. Convert conversational queries into flight searches using Gemini's function calling capabilities and MCP's flight search tools

2041. **[Intelli](https://github.com/intelligentnode/Intelli)** - ⭐ 56
   Build multi-model chatbots and agents from intent.

2042. **[mcp-thinking](https://github.com/mattzcarey/mcp-thinking)** - ⭐ 56
   thinking tool for claude desktop/mcp clients using Deepseek reasoner

2043. **[AllVoiceLab-MCP](https://github.com/allvoicelab/AllVoiceLab-MCP)** - ⭐ 56
   Official AllVoiceLab Model Context Protocol (MCP) server, supporting interaction with powerful text-to-speech and video translation APIs. 

2044. **[geoserver-mcp](https://github.com/mahdin75/geoserver-mcp)** - ⭐ 56
   A Model Context Protocol (MCP) server implementation that connects LLMs to the GeoServer REST API

2045. **[mkp](https://github.com/StacklokLabs/mkp)** - ⭐ 56
   MKP is a Model Context Protocol (MCP) server for Kubernetes

2046. **[mcp-open-library](https://github.com/8enSmith/mcp-open-library)** - ⭐ 56
   A Model Context Protocol (MCP) server for the Internet Archive's Open Library API that enables AI assistants to search for book and author information.

2047. **[solana-mcp-server](https://github.com/openSVM/solana-mcp-server)** - ⭐ 56
   solana mcp sever to enable solana rpc methods

2048. **[freecad-mcp](https://github.com/contextform/freecad-mcp)** - ⭐ 56
   FreeCAD MCP - Open-source Model Context Protocol server for FreeCAD automation

2049. **[stackoverflow-mcp](https://github.com/gscalzo/stackoverflow-mcp)** - ⭐ 56
   A Model Context Protocol server for querying Stack Overflow to help AI models find programming solutions

2050. **[bc-code-intelligence-mcp](https://github.com/JeremyVyska/bc-code-intelligence-mcp)** - ⭐ 56
   BC Code Intelligence MCP Server - Persona-driven workflow orchestration for Business Central development. Provides 16+ MCP tools, layered knowledge system, and intelligent BC pattern analysis through Model Context Protocol.

2051. **[ollama-mcp-bridge](https://github.com/jonigl/ollama-mcp-bridge)** - ⭐ 56
   Extend the Ollama API with dynamic AI tool integration from multiple MCP (Model Context Protocol) servers. Fully compatible, transparent, and developer-friendly, ideal for building powerful local LLM applications, AI agents, and custom chatbots

2052. **[mcp-shell](https://github.com/sonirico/mcp-shell)** - ⭐ 56
   Give hands to AI. MCP server to run shell commands securely, auditably, and on demand.

2053. **[fhir-mcp-server](https://github.com/the-momentum/fhir-mcp-server)** - ⭐ 56
   FHIR MCP Server for handling medical data standard.

2054. **[medical-mcp](https://github.com/JamesANZ/medical-mcp)** - ⭐ 56
   An MCP server that provides comprehensive medical information by querying multiple authoritative medical APIs including FDA, WHO, PubMed, Google Scholar, and RxNorm

2055. **[UnrealMotionGraphicsMCP](https://github.com/winyunq/UnrealMotionGraphicsMCP)** - ⭐ 56
   🚀 UE5-UMG-MCP: A deep-focused MCP for Unreal Engine UMG layout. Designed to maximize AI efficiency within limited context windows by prioritizing precision in UI structure, animations, and blueprint integration.

2056. **[scrapegraph-mcp](https://github.com/ScrapeGraphAI/scrapegraph-mcp)** - ⭐ 55
   ScapeGraph MCP Server

2057. **[umbraco-mcp](https://github.com/Matthew-Wise/umbraco-mcp)** - ⭐ 55
   A model context protocol  (MCP) server for Umbraco 

2058. **[mcp-bridge-api](https://github.com/INQUIRELAB/mcp-bridge-api)** - ⭐ 55
   MCP Bridge is a lightweight, fast, and LLM-agnostic proxy for connecting to multiple Model Context Protocol (MCP) servers through a unified REST API. It enables secure tool execution across diverse environments like mobile, web, and edge devices. Designed for flexibility, scalability, and easy integration with any LLM backend.

2059. **[astro-mcp](https://github.com/morinokami/astro-mcp)** - ⭐ 55
   MCP server to support Astro project development

2060. **[mxcp](https://github.com/raw-labs/mxcp)** - ⭐ 55
   Model eXecution + Context Protocol: Enterprise-Grade Data-to-AI Infrastructure

2061. **[web2mcp](https://github.com/neelsomani/web2mcp)** - ⭐ 55
   Generate an MCP for any web app

2062. **[mcp-ssh](https://github.com/shuakami/mcp-ssh)** - ⭐ 55
   🔐 SSH MCP Tool - AI-powered SSH management through MCP protocol | 基于MCP协议的SSH工具，为AI提供SSH远程操作能力

2063. **[mcp](https://github.com/abap-ai/mcp)** - ⭐ 55
   ABAP MCP - Model Context Protocol - Server SDK

2064. **[nasdaq-data-link-mcp](https://github.com/stefanoamorelli/nasdaq-data-link-mcp)** - ⭐ 55
   A Nasdaq Data Link MCP (Model Context Protocol) Server

2065. **[podman-mcp-server](https://github.com/manusa/podman-mcp-server)** - ⭐ 55
   Model Context Protocol (MCP) server for container runtimes (Podman and Docker)

2066. **[mcp-server-kibana](https://github.com/TocharianOU/mcp-server-kibana)** - ⭐ 55
   MCP server for Kibana, Access search and manage Kibana in MCP Client.

2067. **[mcp-server-flomo](https://github.com/chatmcp/mcp-server-flomo)** - ⭐ 54
   Write notes to Flomo

2068. **[openai-mcp-client](https://github.com/ResoluteError/openai-mcp-client)** - ⭐ 54
   A rudimentary implementation of Anthropic's Model Context Protocol with OpenAIs Model

2069. **[mcp-headless-gmail](https://github.com/baryhuang/mcp-headless-gmail)** - ⭐ 54
   A MCP (Model Context Protocol) server that provides get, send Gmails without local credential or token setup.

2070. **[minibridge](https://github.com/acuvity/minibridge)** - ⭐ 54
   Make your MCP servers secure and production ready

2071. **[mssql_mcp_server](https://github.com/JexinSam/mssql_mcp_server)** - ⭐ 54
   A Model Context Protocol (MCP) server facilitating secure interactions with MSSQL databases.

2072. **[temporal-mcp](https://github.com/Mocksi/temporal-mcp)** - ⭐ 54
   Empowering AI with Workflow Orchestration

2073. **[mcp-batchit](https://github.com/ryanjoachim/mcp-batchit)** - ⭐ 54
   🚀 MCP aggregator for batching multiple tool calls into a single request. Reduces overhead, saves tokens, and simplifies complex operations in AI agent workflows.

2074. **[naver-search-mcp](https://github.com/isnow890/naver-search-mcp)** - ⭐ 54
   MCP server for Naver Search API integration. Provides comprehensive search capabilities across Naver services (web, news, blog, shopping, etc) and data trend analysis tools via DataLab API.

2075. **[mcp-secrets-plugin](https://github.com/amirshk/mcp-secrets-plugin)** - ⭐ 54
   Secure credential management for MCP servers leveraging system-native keychain storage across macOS, Windows, and Linux platforms

2076. **[DecompilerServer](https://github.com/pardeike/DecompilerServer)** - ⭐ 54
   A powerful MCP (Model Context Protocol) server for decompiling and analyzing .NET assemblies, with specialized support for Unity's Assembly-CSharp.dll files. DecompilerServer provides comprehensive decompilation, search, and code analysis capabilities through a rich set of tools and APIs.

2077. **[bloodhound_mcp](https://github.com/mwnickerson/bloodhound_mcp)** - ⭐ 54
   A Model Context Protocol (MCP) server to converse with data in Bloodhound

2078. **[mcp-server-azure-ai-agents](https://github.com/farzad528/mcp-server-azure-ai-agents)** - ⭐ 54
   Model Context Protocol Servers for Azure AI Search

2079. **[chucknorris](https://github.com/pollinations/chucknorris)** - ⭐ 54
   ⚡ C̷h̷u̷c̷k̷N̷o̷r̷r̷i̷s̷ MCP server: Helping LLMs break limits. Provides enhancement prompts inspired by elder-plinius' L1B3RT4S

2080. **[MCP_Atom_of_Thoughts](https://github.com/kbsooo/MCP_Atom_of_Thoughts)** - ⭐ 54
   Atom of Thoughts (AoT) MCP is a server that decomposes complex problems into independent atomic units of thought, using the dependencies between these units to deliver more robust reasoning and validated insights.

2081. **[trpc-mcp-go](https://github.com/trpc-group/trpc-mcp-go)** - ⭐ 54
   Go implementation of the Model Context Protocol (MCP) with comprehensive Streamable HTTP, STDIO, and SSE support. 

2082. **[python](https://github.com/mcp-auth/python)** - ⭐ 54
   🔐 Plug-and-play auth for Python MCP servers.

2083. **[mcp-openai](https://github.com/S1M0N38/mcp-openai)** - ⭐ 53
   🔗 MCP Client with OpenAI compatible API

2084. **[qu3-app](https://github.com/qu3ai/qu3-app)** - ⭐ 53
   Quantum-proof MCP Server and Client Interactions

2085. **[NoLLMChat](https://github.com/zrg-team/NoLLMChat)** - ⭐ 53
   Not-Only LLM Chat. An AI application that enhances creativity and user experience beyond just LLM chat. Noted: Seems it beta version of there is issue with DB please clear site Data in debug 

2086. **[gomcp](https://github.com/llmcontext/gomcp)** - ⭐ 53
   Unofficial Golang SDK for Anthropic Model Context Protocol

2087. **[awesome-remote-mcp-servers](https://github.com/sylviangth/awesome-remote-mcp-servers)** - ⭐ 53
   A curated list of Hosted & Managed Model Context Protocol (MCP) Servers accessible via a simple URL endpoint.

2088. **[mcp-docs-service](https://github.com/alekspetrov/mcp-docs-service)** - ⭐ 53
   MCP Documentation Management Service - A Model Context Protocol implementation for documentation management

2089. **[client](https://github.com/php-mcp/client)** - ⭐ 53
   Core PHP implementation for the Model Context Protocol (MCP) Client

2090. **[user-feedback-mcp](https://github.com/mrexodia/user-feedback-mcp)** - ⭐ 53
   Simple MCP Server to enable a human-in-the-loop workflow in tools like Cline and Cursor.

2091. **[cosmotop](https://github.com/bjia56/cosmotop)** - ⭐ 53
   Multiplatform system monitoring tool using Cosmopolitan Libc

2092. **[sympy-mcp](https://github.com/sdiehl/sympy-mcp)** - ⭐ 53
   A MCP server for symbolic manipulation of mathematical expressions

2093. **[ibkr-mcp-server](https://github.com/seriallazer/ibkr-mcp-server)** - ⭐ 53
   MCP Server for IBKR Client

2094. **[mcp](https://github.com/twelvedata/mcp)** - ⭐ 53
   Twelve Data MCP (Model Context Protocol) Server provides seamless, real-time access to financial market data via WebSocket, enabling reliable streaming of price quotes, market metrics, and events directly into your applications.

2095. **[vscode-mcp](https://github.com/tjx666/vscode-mcp)** - ⭐ 53
   MCP server for Claude Code/VSCode/Cursor/Windsurf to use editor self functionality. ⚡ Get real-time LSP diagnostics, type information, and code navigation for AI coding agents without waiting for slow tsc/eslint checks.

2096. **[puremd-mcp](https://github.com/puremd/puremd-mcp)** - ⭐ 53
   Unblock, scrape, and search tools for MCP clients

2097. **[attio-mcp-server](https://github.com/kesslerio/attio-mcp-server)** - ⭐ 53
   Attio Model Context Protocol (MCP) server implementation

2098. **[canvas-mcp](https://github.com/vishalsachdev/canvas-mcp)** - ⭐ 53
   A Model Context Protocol server to run locally and connect to a Canvas LMS 

2099. **[vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp)** - ⭐ 53
   This project is a Model Context Protocol (MCP) server for interacting with the VRChat API.

2100. **[academia_mcp](https://github.com/IlyaGusev/academia_mcp)** - ⭐ 53
   Academia MCP server: Tools for automatic scientific research

2101. **[desktop](https://github.com/agentify-sh/desktop)** - ⭐ 53
   Agentify Desktop lets Codex control your logged-in ChatGPT, Claude, AiStudio, Grok web sessions via MCP, parallel hidden/visible tabs, file upload + image download

2102. **[pi-mcp-adapter](https://github.com/nicobailon/pi-mcp-adapter)** - ⭐ 53
   Token-efficient MCP adapter for Pi coding agent

2103. **[cap-mcp-plugin](https://github.com/gavdilabs/cap-mcp-plugin)** - ⭐ 52
   MCP (Model Context Protocol) server plugin for CAP NodeJS

2104. **[mcp-cpp](https://github.com/Neumann-Labs/mcp-cpp)** - ⭐ 52
   A C++ SDK for the Model Context Protocol (MCP). The SDK will provide a framework for creating MCP servers and clients in C++.

2105. **[ocaml-mcp](https://github.com/tmattio/ocaml-mcp)** - ⭐ 52
   OCaml implementation of the Model Context Protocol (MCP)

2106. **[mcp-app-demo](https://github.com/pomerium/mcp-app-demo)** - ⭐ 52
   Demo application showcasing how to build and secure MCP servers and clients with Pomerium using contextual access policies.

2107. **[mcp-duckdb-memory-server](https://github.com/IzumiSy/mcp-duckdb-memory-server)** - ⭐ 52
   MCP Memory Server with DuckDB backend

2108. **[adx-mcp-server](https://github.com/pab1it0/adx-mcp-server)** - ⭐ 52
   A Model Context Protocol (MCP) server that enables AI assistants to query and analyze Azure Data Explorer databases through standardized interfaces.

2109. **[A2A_ADK_MCP](https://github.com/RubensZimbres/A2A_ADK_MCP)** - ⭐ 52
   Multi-Agent Systems with Google's Agent Development Kit + A2A + MCP

2110. **[claude-code-emacs](https://github.com/yuya373/claude-code-emacs)** - ⭐ 52
   This package provides seamless integration with Claude Code, allowing you to run AI-powered coding sessions directly in your Emacs environment.

2111. **[talkito](https://github.com/robdmac/talkito)** - ⭐ 52
   TalkiTo lets developers interact with AI systems through speech across multiple channels (terminal, API, phone). It can be used as both a command-line tool and a Python library.

2112. **[gomcp](https://github.com/localrivet/gomcp)** - ⭐ 52
   gomcp provides a Go implementation of the Model Context Protocol (MCP), enabling communication between language models/agents and external tools or resources via a standardized protocol.

2113. **[rag-app-on-aws](https://github.com/genieincodebottle/rag-app-on-aws)** - ⭐ 52
   Build and deploy a full-stack RAG app on AWS with Terraform, using free tier Gemini Pro, real-time web search using Remote MCP server and Streamlit UI with token based authentication.

2114. **[context-optimizer-mcp-server](https://github.com/malaksedarous/context-optimizer-mcp-server)** - ⭐ 52
   A Model Context Protocol (MCP) server that provides context optimization tools for AI coding assistants including GitHub Copilot, Cursor AI, Claude Desktop, and other MCP-compatible assistants enabling them to extract targeted information rather than processing large terminal outputs and files wasting their context.

2115. **[mcp-server-synology](https://github.com/atom2ueki/mcp-server-synology)** - ⭐ 52
   💾 Model Context Protocol (MCP) server for Synology NAS - Enables AI assistants (Claude, Cursor, Continue) to manage files, downloads, and system operations through secure API integration. Features Docker deployment, auto-authentication, and comprehensive file system tools.

2116. **[swift-mcp-gui](https://github.com/NakaokaRei/swift-mcp-gui)** - ⭐ 52
   MCP server that can execute commands such as keyboard input and mouse movement on macOS

2117. **[mcp-swagger-server](https://github.com/zaizaizhao/mcp-swagger-server)** - ⭐ 52
   MCP Swagger Server 将任何符合 OpenAPI/Swagger 规范的 REST API 转换为 Model Context Protocol (MCP) 格式，让 AI 助手能够理解和调用您的 API。

2118. **[mcp-server-security-standard](https://github.com/mcp-security-standard/mcp-server-security-standard)** - ⭐ 52
   MCP Server Security Standard (MSSS): an open, testable security control standard for certifying MCP servers, with levels, evidence requirements, and reporting schemas.

2119. **[adk-mcp-a2a-crash-course](https://github.com/chongdashu/adk-mcp-a2a-crash-course)** - ⭐ 52
   This project demonstrates a multi-agent system using Google's Agent Development Kit (ADK), Agent2Agent (A2A) and Model Context Protocol (MCP).  that integrates Notion for information retrieval and ElevenLabs for text-to-speech conversion.

2120. **[trellis_blender](https://github.com/FishWoWater/trellis_blender)** - ⭐ 52
   Blender plugin for TRELLIS and TRELLIS.2 (3D AIGC Model, Text-to-3D, Image-to-3D)

2121. **[mcp-gearbox](https://github.com/rohitsoni007/mcp-gearbox)** - ⭐ 52
   A modern desktop application for managing Model Context Protocol (MCP) servers across multiple AI agents

2122. **[pubmed-mcp-server](https://github.com/cyanheads/pubmed-mcp-server)** - ⭐ 52
   A Model Context Protocol (MCP) server enabling AI agents to intelligently search, retrieve, and analyze biomedical literature from PubMed via NCBI E-utilities. Includes a research agent scaffold. STDIO & HTTP

2123. **[CodeMCP](https://github.com/SimplyLiz/CodeMCP)** - ⭐ 52
   Code intelligence for AI assistants - MCP server, CLI, and HTTP API with symbol navigation, impact analysis, and architecture mapping

2124. **[scheduler-mcp](https://github.com/PhialsBasement/scheduler-mcp)** - ⭐ 52
   MCP Scheduler is a task automation server that lets you schedule shell commands, API calls, AI tasks, and desktop notifications using cron expressions. Built with Model Context Protocol for seamless integration with Claude Desktop and other AI assistants.

2125. **[godoctor](https://github.com/danicat/godoctor)** - ⭐ 52
   A Model Context Protocol server for Go developers

2126. **[mcp-client](https://github.com/rakesh-eltropy/mcp-client)** - ⭐ 51

2127. **[Memory-Plus](https://github.com/Yuchen20/Memory-Plus)** - ⭐ 51
   🧠 𝑴𝒆𝒎𝒐𝒓𝒚-𝑷𝒍𝒖𝒔 is a lightweight, local RAG memory store for MCP agents. Easily record, retrieve, update, delete, and visualize persistent "memories" across sessions—perfect for developers working with multiple AI coders (like Windsurf, Cursor, or Copilot) or anyone who wants their AI to actually remember them.

2128. **[go-mcp-mysql](https://github.com/Zhwt/go-mcp-mysql)** - ⭐ 51
   Zero burden, ready-to-use Model Context Protocol (MCP) server for interacting with MySQL and automation. No Node.js or Python environment needed.

2129. **[deploystack](https://github.com/deploystackio/deploystack)** - ⭐ 51
   Open source MCP hosting - deploy MCP servers to HTTP endpoints for n8n, Dify, Voiceflow, and any MCP client.

2130. **[baba_is_eval](https://github.com/lennart-finke/baba_is_eval)** - ⭐ 51
   Claude  et al. play the brilliant puzzle title "Baba is You"

2131. **[mcp-server-atlassian-jira](https://github.com/aashari/mcp-server-atlassian-jira)** - ⭐ 51
   Node.js/TypeScript MCP server for Atlassian Jira. Equips AI systems (LLMs) with tools to list/get projects, search/get issues (using JQL/ID), and view dev info (commits, PRs). Connects AI capabilities directly into Jira project management and issue tracking workflows.

2132. **[mcp-mermaid-validator](https://github.com/rtuin/mcp-mermaid-validator)** - ⭐ 51
   A Model Context Protocol server that validates and renders Mermaid diagrams.

2133. **[nowledge-mem](https://github.com/nowledge-co/nowledge-mem)** - ⭐ 51
   Memory and context manager just works.

2134. **[tuisic](https://github.com/Dark-Kernel/tuisic)** - ⭐ 51
   First of its kind, A simple TUI online music streaming application written in c++ with easy vim motions, now with support for Model Context Protocol (MCP)

2135. **[supermcp](https://github.com/dhanababum/supermcp)** - ⭐ 51
   🚀 SuperMCP - Create multiple isolated MCP servers using a single connector. Build powerful Model Context Protocol integrations for databases (PostgreSQL, MSSQL) with FastAPI backend, React dashboard, and token-based auth. Perfect for multi-tenant apps and AI assistants.

2136. **[Navidrome-MCP](https://github.com/Blakeem/Navidrome-MCP)** - ⭐ 51
   Analyze listening patterns, create custom playlists, discover missing albums, discover similar artists, discover radio stations, and validate radio streams using natural language.

2137. **[lc2mcp](https://github.com/xiaotonng/lc2mcp)** - ⭐ 51
   Convert LangChain tools to FastMCP tools

2138. **[lingti-bot](https://github.com/ruilisi/lingti-bot)** - ⭐ 51
   🐕⚡ "极简至上 效率为王 一次编译 到处执行 极速接入"的AI Bot 

2139. **[Perigon.CLI](https://github.com/AterDev/Perigon.CLI)** - ⭐ 50
   This is a tool that helps you quickly build backend services based on Asp.Net Core and EF Core. It provides command line, WebUI and IDE MCP support. In a well-designed project architecture that has been put into practice, code generation and LLM technology are used to reduce various template codes and greatly improve development efficiency!

2140. **[AgentDNS-Node](https://github.com/jsjfai/AgentDNS-Node)** - ⭐ 50
   AgentDNS·Node makes it easy to manage and scale multiple MCP (Model Context Protocol) servers by organizing them into flexible Streamable HTTP (SSE) endpoints—supporting access to all servers, individual servers, or logical server groups.

2141. **[mcp-guard](https://github.com/General-Analysis/mcp-guard)** - ⭐ 50
   MCP Guard secures your MCP client from prompt injection attacks and more.

2142. **[mcp-security-audit](https://github.com/qianniuspace/mcp-security-audit)** - ⭐ 50
   A powerful MCP (Model Context Protocol) Server that audits npm package dependencies for security vulnerabilities. Built with remote npm registry integration for real-time security checks.

2143. **[youtube-mcp-server](https://github.com/mourad-ghafiri/youtube-mcp-server)** - ⭐ 50
   A powerful Model Context Protocol (MCP) server for YouTube video transcription and metadata extraction.

2144. **[ScreenPilot](https://github.com/Mtehabsim/ScreenPilot)** - ⭐ 50
   Tool that allows the AI to control your device in the same way you do, enabling automation for everything!

2145. **[mcp-server-drupal](https://github.com/Omedia/mcp-server-drupal)** - ⭐ 50
   TS based companion MCP server for the Drupal MCP module that works with the STDIO transport.

2146. **[kroger-mcp](https://github.com/CupOfOwls/kroger-mcp)** - ⭐ 50
   A FastMCP server that provides AI assistants like Claude with access to Kroger's grocery shopping functionality through the Model Context Protocol (MCP). This server enables AI assistants to find stores, search products, manage shopping carts, and access Kroger's comprehensive grocery data via the kroger-api python library.

2147. **[tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp)** - ⭐ 50
   A Model Context Protocol (MCP) server for Tripadvisor Content API.  This provides access to Tripadvisor location data, reviews, and photos through standardized MCP interfaces, allowing AI assistants to search for travel destinations and experiences.

2148. **[ntfy-me-mcp](https://github.com/gitmotion/ntfy-me-mcp)** - ⭐ 50
   An ntfy MCP server for sending/fetching ntfy notifications to self-hosted or ANY ntfy.sh server from AI Agents 📤 (supports secure token auth & more - use with npx or docker!)

2149. **[whois-mcp](https://github.com/bharathvaj-ganesan/whois-mcp)** - ⭐ 50
   MCP Server for whois lookups.

2150. **[create-mcp](https://github.com/zueai/create-mcp)** - ⭐ 50
   CLI to set up and deploy MCP Servers to Cloudflare Workers in seconds. Just write TypeScript functions to make Cursor MCP tools.

2151. **[mcpo_docker_use](https://github.com/flyfox666/mcpo_docker_use)** - ⭐ 50
   An example Docker image for mcpo（with npm,curl,nodejs,uv Pre-Built;Pre-Built MCP:amap;baidumap;server-brave-search; tavily;fetch）, a tool that exposes MCP (Model Context Protocol) servers as OpenAPI-compatible HTTP endpoints for OpenWebUI.

2152. **[n8n-workflow-builder-mcp](https://github.com/ifmelate/n8n-workflow-builder-mcp)** - ⭐ 49
   MCP server that allow LLM in agent mode builds n8n workflows for you

2153. **[rulego-server](https://github.com/rulego/rulego-server)** - ⭐ 49
   A lightweight dependency-free workflow automation platform. Supports iPaaS, stream computing, MCP, and AI capabilities. 

2154. **[oatpp-mcp](https://github.com/oatpp/oatpp-mcp)** - ⭐ 49
   Anthropic’s Model Context Protocol implementation for Oat++

2155. **[AI-Cursor-Scraping-Assistant](https://github.com/TheWebScrapingClub/AI-Cursor-Scraping-Assistant)** - ⭐ 49
   A powerful tool that leverages Cursor AI and MCP (Model Context Protocol) to easily generate web scrapers for various types of websites.

2156. **[mcp-oauth-gateway](https://github.com/atrawog/mcp-oauth-gateway)** - ⭐ 49
   An OAuth 2.1 Authorization Server that adds authentication to any MCP (Model Context Protocol) server without code modification.

2157. **[linux-do-mcp](https://github.com/Pleasurecruise/linux-do-mcp)** - ⭐ 49
   A MCP Server For LINUX DO community

2158. **[anysite-mcp-server](https://github.com/anysiteio/anysite-mcp-server)** - ⭐ 49
   A Model Context Protocol (MCP) server that provides comprehensive access to LinkedIn data and functionalities using the Anysite API, enabling not only data retrieval but also robust management of user accounts.

2159. **[model-context-protocol-rb](https://github.com/dickdavis/model-context-protocol-rb)** - ⭐ 49
   An implementation of the Model Context Protocol in Ruby.

2160. **[rs-utcp](https://github.com/universal-tool-calling-protocol/rs-utcp)** - ⭐ 49
   Official Rust implementation of the UTCP

2161. **[mcp-atlassian-server](https://github.com/phuc-nt/mcp-atlassian-server)** - ⭐ 49
   MCP server connecting AI assistants with Jira & Confluence for smart project management.

2162. **[matlab-mcp-server](https://github.com/subspace-lab/matlab-mcp-server)** - ⭐ 49
   Matlab MCP Server in python

2163. **[mcp-server](https://github.com/inkdropapp/mcp-server)** - ⭐ 49
   Inkdrop Model Context Protocol Server

2164. **[gemini-cloud-assist-mcp](https://github.com/GoogleCloudPlatform/gemini-cloud-assist-mcp)** - ⭐ 49
   An MCP Server for Gemini Cloud Assist; provides tools to assist with your tasks on GCP

2165. **[mcp-kubernetes](https://github.com/Azure/mcp-kubernetes)** - ⭐ 49
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Kubernetes clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and Kubernetes

2166. **[hmr](https://github.com/promplate/hmr)** - ⭐ 49
   Real hot-module reload for Python—side effects handled reactively. https://py3.online/hmr

2167. **[Koppla](https://github.com/ruudmens/Koppla)** - ⭐ 49
   A Model-Context-Protocol (MCP) Server for Active Directory

2168. **[us-census-bureau-data-api-mcp](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp)** - ⭐ 49
   The U.S. Census Bureau Data API MCP connects AI Assistants with official Census Bureau statistics.

2169. **[skrills](https://github.com/athola/skrills)** - ⭐ 49
   Coordinate skills between Codex, Copilot, and Claude Code. Validates, analyzes, and syncs skills, subagents, commands, and configuration between multiple CLIs.

2170. **[blockbench-mcp-plugin](https://github.com/jasonjgardner/blockbench-mcp-plugin)** - ⭐ 49
   Adds MCP server to Blockbench

2171. **[powhttp-mcp](https://github.com/usestring/powhttp-mcp)** - ⭐ 49
   MCP server enabling agents to debug HTTP requests better (using powhttp)

2172. **[mcp](https://github.com/goplus/mcp)** - ⭐ 48
   A XGo implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

2173. **[auto-MCP-client](https://github.com/Chen-speculation/auto-MCP-client)** - ⭐ 48
   A Go library implementation of the Model Controller Protocol (MCP). This library allows developers to easily parse MCP service configurations, generate corresponding MCP clients, and integrate them as callable tools within LLM agent systems. Focuses on providing reusable Go packages for building MCP-enabled applications.

2174. **[mcp-client-demo](https://github.com/KelvinQiu802/mcp-client-demo)** - ⭐ 48

2175. **[1xn-vmcp](https://github.com/1xn-labs/1xn-vmcp)** - ⭐ 48
   vMCP - Virtual Model Context Protocol

2176. **[mcp-things3](https://github.com/drjforrest/mcp-things3)** - ⭐ 48
   A Model Context Protocol for reading todos and writing todos and projects in the macOS app Things3 using a combination of Applescript and x-call URLs.

2177. **[vchart-mcp-server](https://github.com/VisActor/vchart-mcp-server)** - ⭐ 48
   A Model Context Protocol (MCP) server for the @visactor/vchart that enables AI assistants to generate interactive charts and visualizations.

2178. **[mcp-server-chart-minio](https://github.com/zaizaizhao/mcp-server-chart-minio)** - ⭐ 48
   mcp-server-chart私有化部署方案

2179. **[mcp-gitee](https://github.com/oschina/mcp-gitee)** - ⭐ 48
   mcp-gitee is a Model Context Protocol (MCP) server implementation for Gitee. It provides a set of tools that interact with Gitee's API, allowing AI assistants to manage repository, issues, pull requests, etc.

2180. **[rust-analyzer-mcp](https://github.com/zeenix/rust-analyzer-mcp)** - ⭐ 48
   A Model Context Protocol (MCP) server that provides integration with rust-analyzer

2181. **[lakevision](https://github.com/lakevision-project/lakevision)** - ⭐ 48
   Lakevision is a tool which provides insights into your Apache Iceberg based Data Lakehouse.

2182. **[mcp-image](https://github.com/shinpr/mcp-image)** - ⭐ 48
   MCP server for AI image generation and editing powered by Gemini 3 Pro Image Preview (Nano Banana Pro 🍌). For Cursor, Codex & more.

2183. **[mcp_demo](https://github.com/Ming-jiayou/mcp_demo)** - ⭐ 47
   A simple example of building an MCP client using C#.

2184. **[kuon](https://github.com/lissettecarlr/kuon)** - ⭐ 47
   久远：一个开发中的大模型语音助手，当前关注易用性，简单上手，支持对话选择性记忆和Model Context Protocol (MCP)服务。 KUON:A large language model-based voice assistant under development, currently focused on ease of use and simple onboarding. It supports selective memory in conversations and the Model Context Protocol (MCP) service.

2185. **[claude-mcp-setup](https://github.com/patruff/claude-mcp-setup)** - ⭐ 47
   Easy setup script for Anthropic Claude Model Context Protocol (MCP) servers on Windows

2186. **[mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers)** - ⭐ 47
   🔒 Reference MCP servers that demo how authentication works with the current Model Context Protocol spec.

2187. **[spec-coding-mcp](https://github.com/feiyun0112/spec-coding-mcp)** - ⭐ 47
   Transform feature ideas into production-ready code through systematic Spec-Driven Development 通过系统化的**规格驱动开发**，将功能想法转化为可投入生产的代码

2188. **[crawlbase-mcp](https://github.com/crawlbase/crawlbase-mcp)** - ⭐ 47
   Crawlbase MCP Server connects AI agents and LLMs with real-time web data. It powers Claude, Cursor, and Windsurf integrations with battle-tested web scraping, JavaScript rendering, and anti-bot protection enabling structured, live data inside your AI workflows.

2189. **[ai-humanizer-mcp-server](https://github.com/Text2Go/ai-humanizer-mcp-server)** - ⭐ 47
   A powerful Model Context Protocol (MCP) server that helps refine AI-generated content to sound more natural and human-like. Built with advanced AI detection and text enhancement capabilities.

2190. **[hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp)** - ⭐ 47
   A Model Context Protocol server for integrating HackMD's note-taking platform with AI assistants.

2191. **[godot-mcp](https://github.com/bradypp/godot-mcp)** - ⭐ 47
   A Model Context Protocol (MCP) server for interacting with the Godot game engine.

2192. **[mcp-victorialogs](https://github.com/VictoriaMetrics-Community/mcp-victorialogs)** - ⭐ 47
   The implementation of Model Context Protocol (MCP) server for VictoriaLogs.

2193. **[codex-mcp-go](https://github.com/w31r4/codex-mcp-go)** - ⭐ 47
   codex-mcp-go is a Go-based MCP (Model Context Protocol) server that serves as a bridge for Codex CLI, enabling various AI coding assistants (such as Claude Code, Roo Code, KiloCode, etc.) to seamlessly collaborate with Codex.

2194. **[clinicaltrialsgov-mcp-server](https://github.com/cyanheads/clinicaltrialsgov-mcp-server)** - ⭐ 47
   A Model Context Protocol (MCP) Server providing LLM tools for the official ClinicalTrials.gov REST API. Search and retrieve clinical trial data, including study details and more

2195. **[mcp](https://github.com/40ants/mcp)** - ⭐ 47
   40ANTS-MCP is a framework for building Model Context Protocol servers in Common Lisp

2196. **[semanticscholar-MCP-Server](https://github.com/JackKuo666/semanticscholar-MCP-Server)** - ⭐ 47
   🔍 This project implements a Model Context Protocol (MCP) server for interacting with the Semantic Scholar API. It provides tools for searching papers, retrieving paper and author details, and fetching citations and references.

2197. **[cinema4d-mcp](https://github.com/ttiimmaacc/cinema4d-mcp)** - ⭐ 47
   Cinema 4D plugin integrating Claude AI for prompt-driven 3D modeling, scene creation, and manipulation.

2198. **[caldav-mcp](https://github.com/dominik1001/caldav-mcp)** - ⭐ 47
   A CalDAV client using Model Context Protocol (MCP) to expose calendar operations as tools for AI assistants.

2199. **[pagerduty-mcp-server](https://github.com/PagerDuty/pagerduty-mcp-server)** - ⭐ 47
   PagerDuty's official local MCP (Model Context Protocol) server which provides tools to interact with your PagerDuty account directly from your MCP-enabled client.

2200. **[langchain-mcp-client](https://github.com/guinacio/langchain-mcp-client)** - ⭐ 46
   This Streamlit application provides a user interface for connecting to MCP (Model Context Protocol) servers and interacting with them using different LLM providers (OpenAI, Anthropic, Google, Ollama).

2201. **[APIWeaver](https://github.com/GongRzhe/APIWeaver)** - ⭐ 46
   A FastMCP server that dynamically creates MCP (Model Context Protocol) servers from web API configurations. This allows you to easily integrate any REST API, GraphQL endpoint, or web service into an MCP-compatible tool that can be used by AI assistants like Claude.

2202. **[ns-mcp-server](https://github.com/r-huijts/ns-mcp-server)** - ⭐ 46
   A Model Context Protocol (MCP) server that provides access to NS (Dutch Railways) travel information through Claude AI. This server enables Claude to fetch real-time train travel information and disruptions using the official Dutch NS API.

2203. **[eliza-plugin-mcp](https://github.com/fleek-platform/eliza-plugin-mcp)** - ⭐ 46
   ElizaOS plugin allowing agents to connect to MCP servers

2204. **[Homeassistant-server-mcp](https://github.com/hekmon8/Homeassistant-server-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) server for interacting with Home Assistant. This server provides tools to control and monitor your Home Assistant devices through MCP-enabled applications.

2205. **[Aspire.MCP.Sample](https://github.com/elbruno/Aspire.MCP.Sample)** - ⭐ 46
   Sample MCP Server and MCP client with Aspire

2206. **[mcp-lite-dev](https://github.com/datawhalechina/mcp-lite-dev)** - ⭐ 46
   共学《MCP极简开发》项目代码

2207. **[shadowgit-mcp](https://github.com/blade47/shadowgit-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) server that provides AI assistants with secure, read-only access to your ShadowGit repositories. This enables powerful debugging and code analysis capabilities by giving AI access to your project's fine-grained git history.

2208. **[image-gen-mcp](https://github.com/lansespirit/image-gen-mcp)** - ⭐ 46
   An MCP server that integrates with gpt-image-1 & Gemini imagen4 model for text-to-image generation services

2209. **[steel-mcp-server](https://github.com/steel-dev/steel-mcp-server)** - ⭐ 46
   MCP Server for interacting with a Steel web browser

2210. **[dremio-mcp](https://github.com/dremio/dremio-mcp)** - ⭐ 46
   Dremio MCP server

2211. **[tiger-slack](https://github.com/timescale/tiger-slack)** - ⭐ 46
   Real-time Slack ingest and MCP server to power your agentic Slack bots

2212. **[mcp-mail](https://github.com/shuakami/mcp-mail)** - ⭐ 46
   📧 MCP Mail Tool - AI-powered email management tool | 基于 MCP 的智能邮件管理工具

2213. **[mcp_server_notify](https://github.com/Cactusinhand/mcp_server_notify)** - ⭐ 46
   Send system notification when Agent task is done.

2214. **[mcp-rdf-explorer](https://github.com/emekaokoye/mcp-rdf-explorer)** - ⭐ 46
   A Model Context Protocol (MCP) server that provides conversational interface for the exploration and analysis of RDF (Turtle) based Knowledge Graph in Local File mode or SPARQL Endpoint mode.

2215. **[calculator-mcp-server](https://github.com/huhabla/calculator-mcp-server)** - ⭐ 46
   A Model Context Protocol (MCP) server that provides Claude with advanced mathematical calculation capabilities

2216. **[mcp](https://github.com/getAlby/mcp)** - ⭐ 46
   Connect a bitcoin lightning wallet to your LLM using Nostr Wallet Connect and Model Context Protocol

2217. **[gnome-mcp-server](https://github.com/bilelmoussaoui/gnome-mcp-server)** - ⭐ 46
   Grant the AI octopus access to a portion of your desktop

2218. **[pprof-analyzer-mcp](https://github.com/ZephyrDeng/pprof-analyzer-mcp)** - ⭐ 46
   This is a Model Context Protocol (MCP) server implemented in Go, providing a tool to analyze Go pprof performance profiles.

2219. **[mcp-tts](https://github.com/blacktop/mcp-tts)** - ⭐ 46
   MCP Server for Text to Speech

2220. **[mcp-youtube](https://github.com/adhikasp/mcp-youtube)** - ⭐ 46
   Model Context Protocol to fetch youtube transcript

2221. **[modular-mcp](https://github.com/d-kimuson/modular-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) proxy server that enables efficient management of large tool collections across multiple MCP servers by grouping them and loading tool schemas on-demand.

2222. **[abaqus-mcp-server](https://github.com/jianzhichun/abaqus-mcp-server)** - ⭐ 46
   An MCP (Model Context Protocol) server designed to interact with an already running Abaqus/CAE Graphical User Interface (GUI). It allows for the execution of Python scripts within the Abaqus environment and retrieval of messages from the Abaqus message log/area, all through MCP tools.

2223. **[p4mcp-server](https://github.com/perforce/p4mcp-server)** - ⭐ 46
   [Community Supported] Perforce P4MCP Server is a Model Context Protocol (MCP) server that integrates with the Perforce P4 version control system.

2224. **[firefox-devtools-mcp](https://github.com/freema/firefox-devtools-mcp)** - ⭐ 46
   Model Context Protocol server for Firefox DevTools - enables AI assistants to inspect and control Firefox browser through the Remote Debugging Protocol

2225. **[mcp-openapi-schema](https://github.com/hannesj/mcp-openapi-schema)** - ⭐ 45
   OpenAPI Schema Model Context Protocol Server

2226. **[mcp-sdk](https://github.com/symfony/mcp-sdk)** - ⭐ 45
   Model Context Protocol SDK for Client and Server applications in PHP

2227. **[mcp-made-simple](https://github.com/chongdashu/mcp-made-simple)** - ⭐ 45
   Model Context Protocol (MCP) Made Simple - Code for the tutorial series - focusing on practical ways to understand and use MCP

2228. **[Serper-search-mcp](https://github.com/NightTrek/Serper-search-mcp)** - ⭐ 45
   Un-official Serper Google search server for Cline and other MCP clients

2229. **[mcpcat-python-sdk](https://github.com/MCPCat/mcpcat-python-sdk)** - ⭐ 45
   MCPcat is an analytics platform for MCP server owners 🐱.

2230. **[sample-agentic-ai-web](https://github.com/aws-samples/sample-agentic-ai-web)** - ⭐ 45
   This project demonstrates how to use AWS Bedrock with Anthropic Claude and Amazon Nova models to create a web automation assistant with tool use, human-in-the-loop interaction, and vision capabilities.

2231. **[excalidraw-mcp](https://github.com/i-tozer/excalidraw-mcp)** - ⭐ 45
   Model Context Protocol (MCP) server for Excalidraw - Work in Progress

2232. **[marinade-finance-mcp-server](https://github.com/lorine93s/marinade-finance-mcp-server)** - ⭐ 45
   Marinade Finance MCP Server is an MCP server specifically designed for the Marinade Finance.

2233. **[mcp-server-atlassian-confluence](https://github.com/aashari/mcp-server-atlassian-confluence)** - ⭐ 45
   Node.js/TypeScript MCP server for Atlassian Confluence. Provides tools enabling AI systems (LLMs) to list/get spaces & pages (content formatted as Markdown) and search via CQL. Connects AI seamlessly to Confluence knowledge bases using the standard MCP interface.

2234. **[meme-mcp](https://github.com/haltakov/meme-mcp)** - ⭐ 45
   A simple Model Context Protocol (MCP) server for generating memes using the ImgFlip API

2235. **[vercel-ai-docs-mcp](https://github.com/IvanAmador/vercel-ai-docs-mcp)** - ⭐ 45
   A Model Context Protocol (MCP) server that provides AI-powered search and querying capabilities for the Vercel AI SDK documentation. This project enables developers to ask questions about the Vercel AI SDK and receive accurate, contextualized responses based on the official documentation.

2236. **[awesome-mcp-security](https://github.com/AIM-Intelligence/awesome-mcp-security)** - ⭐ 45
   Security Threats related with MCP (Model Context Protocol), MCP Servers and more

2237. **[langchaingo-mcp-adapter](https://github.com/i2y/langchaingo-mcp-adapter)** - ⭐ 45
   A Go adapter that bridges LangChain Go tools with Model Context Protocol (MCP) servers.

2238. **[dataproduct-mcp](https://github.com/entropy-data/dataproduct-mcp)** - ⭐ 45
   A Model Context Protocol (MCP) server for discovering data products and requesting access in Data Mesh Manager, and executing queries on the data platform to access business data.

2239. **[mcp-starter-template](https://github.com/StevenStavrakis/mcp-starter-template)** - ⭐ 45
   An opinionated starter template for making Model Context Protocol (MCP) servers

2240. **[advanced-homeassistant-mcp](https://github.com/jango-blockchained/advanced-homeassistant-mcp)** - ⭐ 45
   An advanced MCP server for Home Assistant. 🔋 Batteries included.

2241. **[flightradar24-mcp-server](https://github.com/sunsetcoder/flightradar24-mcp-server)** - ⭐ 45
   Model Context Protocol server for Flight Tracking

2242. **[Reversecore_MCP](https://github.com/sjkim1127/Reversecore_MCP)** - ⭐ 45
   A security-first MCP server empowering AI agents to orchestrate Ghidra, Radare2, and YARA for automated reverse engineering.

2243. **[EDT-MCP](https://github.com/DitriXNew/EDT-MCP)** - ⭐ 45
   MCP for 1C:EDT

2244. **[esa-mcp-server](https://github.com/esaio/esa-mcp-server)** - ⭐ 45
   esa.io の公式 MCP(Model Context Protocol)サーバー(STDIO Transport版)

2245. **[moondream-mcp](https://github.com/ColeMurray/moondream-mcp)** - ⭐ 45
   Moondream MCP Server in Python

2246. **[globalping-mcp-server](https://github.com/jsdelivr/globalping-mcp-server)** - ⭐ 45
   Remote MCP server that gives LLMs access to run network commands

2247. **[langfuse-mcp](https://github.com/avivsinai/langfuse-mcp)** - ⭐ 45
   A Model Context Protocol (MCP) server for Langfuse, enabling AI agents to query Langfuse trace data for enhanced debugging and observability

2248. **[mcp-metabase-server](https://github.com/easecloudio/mcp-metabase-server)** - ⭐ 45
   A comprehensive MCP server for Metabase with 70+ tools.

2249. **[mealie-mcp-server](https://github.com/rldiao/mealie-mcp-server)** - ⭐ 45
   MCP server that exposes Mealie APIs to MCP clients such as Claude Desktop

2250. **[buildkite-mcp-server](https://github.com/buildkite/buildkite-mcp-server)** - ⭐ 45
   Official MCP Server for Buildkite.

2251. **[mcp-amadeus](https://github.com/donghyun-chae/mcp-amadeus)** - ⭐ 45
   Amadeus MCP(Model Context Protocol) Server

2252. **[lisply-mcp](https://github.com/gornskew/lisply-mcp)** - ⭐ 45
   Model Context Protocol (MCP) server to manage and talk to compliant "Lisply" lisp-speaking backend services

2253. **[mcp-dap-server](https://github.com/go-delve/mcp-dap-server)** - ⭐ 45
   MCP server to communicate with DAP servers allowing AI Agents the ability to debug live programs.

2254. **[js](https://github.com/mcp-auth/js)** - ⭐ 45
   🔐 Plug-and-play auth for Node.js MCP servers.

2255. **[mcp-yfinance-server](https://github.com/Adity-star/mcp-yfinance-server)** - ⭐ 45
   Real-time stock API with Python, MCP server example, yfinance stock analysis dashboard

2256. **[vue-mcp-next](https://github.com/tuskermanshu/vue-mcp-next)** - ⭐ 44
   Vue MCP Next bridges AI agents with Vue.js applications, enabling real-time component state inspection and   manipulation through the Model Context Protocol. Built for AI-assisted development workflows

2257. **[generic-mcp-client-chat](https://github.com/rom1504/generic-mcp-client-chat)** - ⭐ 44
   Generic MCP Client to use any MCP tool in a chat

2258. **[spring-ai-mcp-client](https://github.com/ogulcanarbc/spring-ai-mcp-client)** - ⭐ 44
   mcp client application that utilizes spring ai. it integrates with mcp protocol-supported servers to enable ai-powered chat interactions.

2259. **[Claude-Project-Coordinator](https://github.com/M-Pineapple/Claude-Project-Coordinator)** - ⭐ 44
   Claude Project Coordinator is a Swift-powered MCP (Model Context Protocol) server designed to streamline multi-project Xcode development. It lets you track project status, auto-detect frameworks, search code patterns, and maintain a structured development knowledge base — all locally, with Claude Desktop as your assistant.

2260. **[thingspanel-mcp](https://github.com/ThingsPanel/thingspanel-mcp)** - ⭐ 44
   This MCP server integrates ThingsPanel IoT platform with AI models like Claude, GPT, and others that support the Model Context Protocol. 

2261. **[mcp-filter](https://github.com/pro-vi/mcp-filter)** - ⭐ 44
   A proxy MCP (Model Context Protocol) server that filters the upstream tool surface to just the tools you need.

2262. **[rhinoMcpServer](https://github.com/always-tinkering/rhinoMcpServer)** - ⭐ 44
   RhinoMCP connects Rhino to Claude AI through the Model Context Protocol (MCP), enabling AI-assisted 3D modeling and architectural design.

2263. **[ainovelprompter](https://github.com/danielsobrado/ainovelprompter)** - ⭐ 44
   Create the prompts you need to write your Novel using AI

2264. **[mcp-typescribe](https://github.com/yWorks/mcp-typescribe)** - ⭐ 44
   An MCP server implementation enabling LLMs to work with new APIs and frameworks

2265. **[code-screenshot-mcp](https://github.com/MoussaabBadla/code-screenshot-mcp)** - ⭐ 44
   MCP server for generating beautiful code screenshots directly from Claude

2266. **[scaled-mcp](https://github.com/Traego/scaled-mcp)** - ⭐ 44
   ScaledMCP is a horizontally scalabled MCP and A2A Server. You know, for AI.

2267. **[luma-mcp](https://github.com/JochenYang/luma-mcp)** - ⭐ 44
   Multi-Model Visual Understanding MCP Server, GLM-4.6V, DeepSeek-OCR (free), and Qwen3-VL-Flash. Provide visual processing capabilities for AI coding models that do not support image understanding.多模型视觉理解MCP服务器，GLM-4.6V、DeepSeek-OCR（免费）和Qwen3-VL-Flash等。为不支持图片理解的 AI 编码模型提供视觉处理能力。

2268. **[inAI-wiki](https://github.com/inai-sandy/inAI-wiki)** - ⭐ 44
   🌍 The open-source Wikipedia of AI — 2M+ apps, agents, LLMs & datasets. Updated daily with tools, tutorials & news.

2269. **[contentful-mcp-server](https://github.com/contentful/contentful-mcp-server)** - ⭐ 44
   MCP (Model Context Protocol) server for the Contentful Management API

2270. **[mcp-container-ts](https://github.com/Azure-Samples/mcp-container-ts)** - ⭐ 44
   This is a quick start guide that provides the basic building blocks to set up a remote Model Context Protocol (MCP) server using Azure Container Apps. The MCP server is built using Node.js and TypeScript, and it can be used to run various tools and services in a serverless environment.

2271. **[python-notebook-mcp](https://github.com/UsamaK98/python-notebook-mcp)** - ⭐ 44
   Lightweight Python Notebook MCP - Enable AI assistants to create, edit, and view Jupyter notebooks via Model Context Protocol

2272. **[dynamic-fastmcp](https://github.com/ragieai/dynamic-fastmcp)** - ⭐ 44
   Dynamic FastMCP extends the Model Context Protocol Python server with context-aware tools that adapt their behavior and descriptions based on user, tenant, and request context.

2273. **[mcp-agents-hub](https://github.com/mcp-agents-ai/mcp-agents-hub)** - ⭐ 44
   The open-source ecosystem for building, discovering, and deploying Model Context Protocol servers and clients.

2274. **[vikunja-mcp](https://github.com/democratize-technology/vikunja-mcp)** - ⭐ 44
   Model Context Protocol server for Vikunja task management. Enables AI assistants to interact with Vikunja instances via MCP.

2275. **[MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API)** - ⭐ 44
   🔍Model Context Protocol (MCP) server for Apache Airflow API integration. Provides comprehensive tools for managing Airflow clusters including service operations, configuration management, status monitoring, and request tracking.

2276. **[MDB-MCP](https://github.com/smadi0x86/MDB-MCP)** - ⭐ 44
   Multi Debugger MCP server that enables LLMs to interact with GDB and LLDB for binary debugging and analysis.

2277. **[wechat-mcp](https://github.com/JettChenT/wechat-mcp)** - ⭐ 43
   Model Context Protocol for WeChat

2278. **[MCPP.Net](https://github.com/xuzeyu91/MCPP.Net)** - ⭐ 43
   Model Context Protocol Platform，统一管理你的MCP服务

2279. **[mcp-playground](https://github.com/Elkhn/mcp-playground)** - ⭐ 43
   A Streamlit-based chat app for LLMs with plug-and-play tool support via Model Context Protocol (MCP), powered by LangChain, LangGraph, and Docker.

2280. **[LLaMa-MCP-Streamlit](https://github.com/Nikunj2003/LLaMa-MCP-Streamlit)** - ⭐ 43
   AI assistant built with Streamlit, NVIDIA NIM (LLaMa 3.3:70B) / Ollama, and Model Control Protocol (MCP).

2281. **[pdf-mcp](https://github.com/saury1120/pdf-mcp)** - ⭐ 43
   一个强大的 PDF 处理 MCP（Model Context Protocol）服务，提供全面的 PDF 文档分析功能

2282. **[mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi)** - ⭐ 43
   A Model Context Protocol server implementation for Kagi's API

2283. **[world_bank_mcp_server](https://github.com/anshumax/world_bank_mcp_server)** - ⭐ 43
   An implementation of the Model Context Protocol for the World Bank open data API

2284. **[bookstack-mcp-server](https://github.com/pnocera/bookstack-mcp-server)** - ⭐ 43
   A Model Context Protocol (MCP) server providing full access to BookStack's knowledge management capabilities

2285. **[mcp-server-ledger](https://github.com/minhyeoky/mcp-server-ledger)** - ⭐ 43
   A Model Context Protocol server for interacting with Ledger CLI, a powerful double-entry accounting system. This server enables Large Language Models to query and analyze financial data through a standardized interface, making it easy for AI assistants to help with financial reporting, budget analysis, and accounting tasks.

2286. **[any2markdown](https://github.com/WW-AI-Lab/any2markdown)** - ⭐ 43
   一个高性能的文档转换服务器，同时支持 Model Context Protocol (MCP) 和 RESTful API 接口。将 PDF、Word 和 Excel 文档转换为 Markdown 格式，具备图片提取、页眉页脚移除和批量处理等高级功能

2287. **[mcp-graphql-schema](https://github.com/hannesj/mcp-graphql-schema)** - ⭐ 43
   GraphQL Schema Model Context Protocol Server

2288. **[openrpc-mcp-server](https://github.com/shanejonas/openrpc-mcp-server)** - ⭐ 43
   A Model Context Protocol (MCP) server that provides JSON-RPC functionality through OpenRPC.

2289. **[beemcp](https://github.com/OkGoDoIt/beemcp)** - ⭐ 43
   BeeMCP: an unofficial Model Context Protocol (MCP) server that connects your Bee wearable lifelogger to AI via the Model Context Protocol

2290. **[mcp-openmsx](https://github.com/nataliapc/mcp-openmsx)** - ⭐ 43
   A Model Context Protocol (MCP) server for automating openMSX emulator instances. This server provides comprehensive tools for MSX software development, testing, and automation through standardized MCP protocols.

2291. **[devcontext](https://github.com/aiurda/devcontext)** - ⭐ 43
   DevContext is a cutting-edge Model Context Protocol (MCP) server designed to provide developers with continuous, project-centric context awareness. Unlike traditional context systems, DevContext continuously learns from and adapts to your development patterns and delivers highly relevant context providing a deeper understanding of your codebase.

2292. **[chrome-debug-mcp](https://github.com/robertheadley/chrome-debug-mcp)** - ⭐ 43
   An MCP server to allow you to debug webpages using LLMs

2293. **[mcp-rquest](https://github.com/xxxbrian/mcp-rquest)** - ⭐ 43
   A MCP server providing realistic browser-like HTTP request capabilities with accurate TLS/JA3/JA4 fingerprints for bypassing anti-bot measures. It also supports converting PDF and HTML documents to Markdown for easier processing by LLMs.

2294. **[mcp-zen](https://github.com/199-mcp/mcp-zen)** - ⭐ 43
   Enhanced Zen MCP Server with 'zen' default tool and improvements

2295. **[MCPApp](https://github.com/tanaikech/MCPApp)** - ⭐ 43
   This text introduces the Model Context Protocol (MCP) for AI interaction, exploring Google Apps Script (GAS) as a server option. It shows feasibility with a sample but notes the lack of a GAS SDK, aiming to encourage understanding and development.

2296. **[Claude-Deep-Research](https://github.com/mcherukara/Claude-Deep-Research)** - ⭐ 43
   An MCP (Model Context Protocol) server that enables comprehensive research capabilities for Claude

2297. **[salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server)** - ⭐ 43
   Model Context Protocol server for Salesforce REST API integration

2298. **[mcp_server_filesystem](https://github.com/MarcusJellinghaus/mcp_server_filesystem)** - ⭐ 43
   MCP File System Server: A secure Model Context Protocol server that provides file operations for AI assistants. Enables Claude and other assistants to safely read, write, and list files in a designated project directory with robust path validation and security controls.

2299. **[youtrack-mcp](https://github.com/devstroop/youtrack-mcp)** - ⭐ 43
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

2300. **[cli](https://github.com/syrin-labs/cli)** - ⭐ 43
   Runtime intelligence system that makes MCP servers debuggable, testable, and safe to run in production.

2301. **[shotgrid-mcp-server](https://github.com/loonghao/shotgrid-mcp-server)** - ⭐ 43
   A Model Context Protocol (MCP) server for Autodesk ShotGrid/Flow Production Tracking (FPT) with comprehensive CRUD operations and data management capabilities.

2302. **[lighthouse-mcp-server](https://github.com/danielsogl/lighthouse-mcp-server)** - ⭐ 43
   MCP server that enables AI agents to perform comprehensive web audits using Google Lighthouse with 13+ tools for performance, accessibility, SEO, and security analysis.

2303. **[activitywatch-mcp-server](https://github.com/8bitgentleman/activitywatch-mcp-server)** - ⭐ 43
   Model Context Protocol server for ActivityWatch time tracking data

2304. **[ask-user-questions-mcp](https://github.com/paulp-o/ask-user-questions-mcp)** - ⭐ 43
   Better 'AskUserQuestion' - A lightweight MCP server/OpenCode plugin/Agent Skills + CLI tool that allows your LLMs ask questions to you. Be the human in the human-in-the-loop!

2305. **[agentic-developer-mcp](https://github.com/teabranch/agentic-developer-mcp)** - ⭐ 43
   An MCP server that scales development into controllable agentic, recursive flows, and build a feature from bottom-up

2306. **[taskMaster-todoist-mcp](https://github.com/mingolladaniele/taskMaster-todoist-mcp)** - ⭐ 42
   A lightweight Model Context Protocol (MCP) server that enables natural language interaction with your Todoist tasks directly from your IDE. Built with simplicity and maintainability in mind.

2307. **[solana-dev-mcp](https://github.com/solana-foundation/solana-dev-mcp)** - ⭐ 42
   Solana Model Context Protocol (MCP) Demo

2308. **[awesome-mcp-servers](https://github.com/mctrinh/awesome-mcp-servers)** - ⭐ 42
   A curated list of excellent Model Context Protocol (MCP) servers.

2309. **[mcp-ai-memory](https://github.com/scanadi/mcp-ai-memory)** - ⭐ 42
   A production-ready Model Context Protocol (MCP) server for semantic memory management

2310. **[mcp-server-arangodb](https://github.com/ravenwits/mcp-server-arangodb)** - ⭐ 42
   This is a TypeScript-based MCP server that provides database interaction capabilities through ArangoDB. It implements core database operations and allows seamless integration with ArangoDB through MCP tools. You can use it wih Claude app and also extension for VSCode that works with mcp like Cline!

2311. **[ai-software-architect](https://github.com/codenamev/ai-software-architect)** - ⭐ 42
   AI-powered architecture documentation framework with ADRs, reviews, and pragmatic mode. Now available as Claude Code Plugin for easiest installation.

2312. **[mobile-dev-mcp-server](https://github.com/jsuarezruiz/mobile-dev-mcp-server)** - ⭐ 42
   This is a MCP designed to manage and interact with mobile devices and simulators.

2313. **[python-dependency-manager-companion-mcp-server](https://github.com/KemingHe/python-dependency-manager-companion-mcp-server)** - ⭐ 42
   Self-updating MCP server to cross-ref latest official pip, conda, poetry, uv, pixi, and pdm docs

2314. **[repl-mcp](https://github.com/simm-is/repl-mcp)** - ⭐ 42
   Model Context Protocol Clojure support including REPL integration with development tools.

2315. **[mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor)** - ⭐ 42
   MCP (Model Context Protocol) server that enables AI assistants to interact with Storybook design systems. Extract component HTML, analyze styles, and help with design system adoption and refactoring.

2316. **[prism-mcp-rs](https://github.com/prismworks-ai/prism-mcp-rs)** - ⭐ 42
   Enterprise-grade Rust implementation of Anthropic's MCP protocol

2317. **[davinci-resolve-mcp](https://github.com/apvlv/davinci-resolve-mcp)** - ⭐ 42
   A Model Context Protocol (MCP) server for interacting with DaVinci Resolve and Fusion

2318. **[mcp-ssh](https://github.com/AiondaDotCom/mcp-ssh)** - ⭐ 42
   A Model Context Protocol (MCP) server for managing and controlling SSH connections.

2319. **[mcp-toolbox-sdk-go](https://github.com/googleapis/mcp-toolbox-sdk-go)** - ⭐ 42
   Go SDK for interacting with the MCP Toolbox for Databases.

2320. **[mcp-logic](https://github.com/angrysky56/mcp-logic)** - ⭐ 42
   Fully functional AI Logic Calculator utilizing Prover9/Mace4 via Python based Model Context Protocol (MCP-Server)- tool for Windows Claude App etc

2321. **[zed-mcp-server-sequential-thinking](https://github.com/LoamStudios/zed-mcp-server-sequential-thinking)** - ⭐ 42
   A sequential thinking MCP server extension for Zed

2322. **[gradle-mcp-server](https://github.com/IlyaGulya/gradle-mcp-server)** - ⭐ 41
   A Model Context Protocol (MCP) server to enable AI tools to interact with Gradle projects programmatically.

2323. **[platform-context-exporter](https://github.com/alkoleft/platform-context-exporter)** - ⭐ 41
   Инструмент для выгрузки синтаксис помощника в файлы

2324. **[mcp-server](https://github.com/profullstack/mcp-server)** - ⭐ 41
   A generic, modular server for implementing the Model Context Protocol (MCP). 

2325. **[mcp-server-js](https://github.com/yepcode/mcp-server-js)** - ⭐ 41
   An MCP (Model Context Protocol) server that enables ✨ AI platforms to interact with 🤖 YepCode's infrastructure.  Turn your YepCode processes into powerful tools that AI assistants can use 🚀

2326. **[dynamic-shell-server](https://github.com/codelion/dynamic-shell-server)** - ⭐ 41
   Dynamic Shell Command MCP Server

2327. **[zig-mcp-server](https://github.com/openSVM/zig-mcp-server)** - ⭐ 41
   A Model Context Protocol (MCP) server that provides Zig language tooling, code analysis, and documentation access. This server enhances AI capabilities with Zig-specific functionality including code optimization, compute unit estimation, code generation, and best practices recommendations.

2328. **[kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server)** - ⭐ 41
   A Model Context Protocol (MCP) server for Apache Kafka implemented in Go, leveraging franz-go and mcp-go.

2329. **[mcp](https://github.com/Azure-Samples/mcp)** - ⭐ 41
   Links to samples, tools, and resources for building and integrating Model Context Protocol (MCP) servers on Azure using multiple languages

2330. **[mailgun-mcp-server](https://github.com/mailgun/mailgun-mcp-server)** - ⭐ 41
   Implementation of Model Context Protocol server for Mailgun APIs

2331. **[dify-mcp-server](https://github.com/AI-FE/dify-mcp-server)** - ⭐ 41
   A Model Context Protocol server for Dify

2332. **[ZMCPTools](https://github.com/ZachHandley/ZMCPTools)** - ⭐ 41
   A custom TypeScript MCP Server intended to be used with Claude Code

2333. **[kanban-mcp](https://github.com/bradrisse/kanban-mcp)** - ⭐ 41
   MCP Kanban is a specialized middleware designed to facilitate interaction between Large Language Models (LLMs) and Planka, a Kanban board application. It serves as an intermediary layer that provides LLMs with a simplified and enhanced API to interact with Planka's task management system.

2334. **[locallama-mcp](https://github.com/Heratiki/locallama-mcp)** - ⭐ 41
   An MCP Server that works with Roo Code/Cline.Bot/Claude Desktop to optimize costs by intelligently routing coding tasks between local LLMs free APIs and paid APIs.

2335. **[mcp-codestyle-server](https://github.com/itxaiohanglover/mcp-codestyle-server)** - ⭐ 41
   MCP Codestyle Server 是一个基于 Spring AI 实现的 Model Context Protocol (MCP) 服务器，为 IDE 和 AI 代理提供代码模板搜索和检索工具。该服务从本地缓存查找模板，并在缺失时自动从远程仓库下载元数据和文件进行修复。

2336. **[seekcode](https://github.com/seekrays/seekcode)** - ⭐ 41
   A clean and efficient code snippet and clipboard management tool designed for developers

2337. **[illustrator-mcp-server](https://github.com/spencerhhubert/illustrator-mcp-server)** - ⭐ 41
   mcp server to run scripts on adobe illustrator

2338. **[gimp-mcp](https://github.com/maorcc/gimp-mcp)** - ⭐ 41
   GIMP MCP server

2339. **[codebadger](https://github.com/Lekssays/codebadger)** - ⭐ 41
   A containerized Model Context Protocol (MCP) server providing static code analysis using Joern's Code Property Graph (CPG) with support for Java, C/C++, JavaScript, Python, Go, Kotlin, C#, Ghidra, Jimple, PHP, Ruby, and Swift.

2340. **[nmap-mcp-server](https://github.com/PhialsBasement/nmap-mcp-server)** - ⭐ 41
   A Model Context Protocol (MCP) server that enables AI assistants to perform network scanning operations using NMAP

2341. **[mcp-zenml](https://github.com/zenml-io/mcp-zenml)** - ⭐ 41
   MCP server to connect an MCP client (Cursor, Claude Desktop etc) with your ZenML MLOps and LLMOps pipelines

2342. **[imap-mcp](https://github.com/non-dirty/imap-mcp)** - ⭐ 41
   IMAP Model Context Protocol server for interactive email processing

2343. **[mcp_rails_template](https://github.com/seuros/mcp_rails_template)** - ⭐ 40
   A minimal Rails API template for creating MCP (Model Context Protocol) servers with robust tool execution capabilities and examples.

2344. **[agentic-mcp-client](https://github.com/peakmojo/agentic-mcp-client)** - ⭐ 40
   A standalone agent runner that executes tasks using MCP (Model Context Protocol) tools via Anthropic Claude, AWS BedRock and OpenAI APIs. It enables AI agents to run autonomously in cloud environments and interact with various systems securely.

2345. **[instagram-engagement-mcp](https://github.com/Bob-lance/instagram-engagement-mcp)** - ⭐ 40
   📢 Instagram MCP Server – A powerful Model Context Protocol (MCP) server for tracking Instagram engagement, generating leads, and analyzing audience feedback.

2346. **[browser-use-mcp-client](https://github.com/Linzo99/browser-use-mcp-client)** - ⭐ 40
   A MCP client for browser-use

2347. **[beanquery-mcp](https://github.com/vanto/beanquery-mcp)** - ⭐ 40
   Beancount MCP Server is an experimental implementation that utilizes the Model Context Protocol (MCP) to enable AI assistants to query and analyze Beancount ledger files using Beancount Query Language (BQL) and the beanquery tool.

2348. **[mcp-shell](https://github.com/hdresearch/mcp-shell)** - ⭐ 40
   Execute a secure shell in Claude Desktop using the Model Context Protocol.

2349. **[osm-mcp](https://github.com/wiseman/osm-mcp)** - ⭐ 40
   Model Context Protocol server for OpenStreetMap data

2350. **[bsky-mcp-server](https://github.com/brianellin/bsky-mcp-server)** - ⭐ 40
   Bluesky MCP (Model Context Protocol) Server

2351. **[just-mcp](https://github.com/toolprint/just-mcp)** - ⭐ 40
   Share the same project justfile tasks with your AI Coding Agent.

2352. **[scraps](https://github.com/boykush/scraps)** - ⭐ 40
   Scraps is a portable CLI knowledge hub for managing interconnected Markdown documentation with Wiki-link notation.

2353. **[anki-mcp](https://github.com/nietus/anki-mcp)** - ⭐ 40
   MCP server for anki

2354. **[sugar](https://github.com/roboticforce/sugar)** - ⭐ 40
   🍰 Sugar - The autonomous layer for AI coding agents

2355. **[MayaMCP](https://github.com/PatrickPalmer/MayaMCP)** - ⭐ 40
   Model Context Protocol (MCP) server implementation for Autodesk Maya

2356. **[yandex-tracker-mcp](https://github.com/aikts/yandex-tracker-mcp)** - ⭐ 40
   Yandex Tracker MCP Server with OAuth2 support

2357. **[metabase-mcp](https://github.com/jerichosequitin/metabase-mcp)** - ⭐ 40
   A high-performance Model Context Protocol server for AI integration with Metabase analytics platforms. Features response optimization, robust error handling, and comprehensive data access tools. Featured on Claude.

2358. **[codex-specialized-subagents](https://github.com/leonardsellem/codex-specialized-subagents)** - ⭐ 40
   MCP server that lets Codex delegate to isolated codex exec sub-agents, selecting repo+global skills automatically

2359. **[binance-mcp-server](https://github.com/AnalyticAce/binance-mcp-server)** - ⭐ 40
   Unofficial tools and server implementation for Binance's Model Context Protocol (MCP). Designed to support developers building crypto trading  AI Agents.

2360. **[discourse-mcp](https://github.com/discourse/discourse-mcp)** - ⭐ 40
   MCP client for Discourse sites

2361. **[Scientific-Papers-MCP](https://github.com/benedict2310/Scientific-Papers-MCP)** - ⭐ 40
   A Model Context Protocol (MCP) server that provides LLMs with real-time access to scientific papers from arXiv and OpenAlex.

2362. **[pentestMCP](https://github.com/ramkansal/pentestMCP)** - ⭐ 40
   pentestMCP: AI-Powered Penetration Testing via MCP, an MCP designed for penetration testers.

2363. **[UnrealClaude](https://github.com/Natfii/UnrealClaude)** - ⭐ 40
   Claude Code CLI integration for Unreal Engine 5.7 - Get AI coding assistance with built-in UE5.7 documentation context directly in the editor.

2364. **[dotcom.chat](https://github.com/kamath/dotcom.chat)** - ⭐ 39
   A simple NextJS MCP client with sensible keybindings

2365. **[MCPollinations](https://github.com/pinkpixel-dev/MCPollinations)** - ⭐ 39
   A Model Context Protocol (MCP) server that enables AI assistants to generate images, text, and audio through the Pollinations APIs. Supports customizable parameters, image saving, and multiple model options.

2366. **[sharepoint-mcp](https://github.com/DEmodoriGatsuO/sharepoint-mcp)** - ⭐ 39
   SharePoint MCP (Model Context Protocol) - A SharePoint connector for LLM applications. Access SharePoint documents and lists through Microsoft Graph API.

2367. **[mcp_code_analyzer](https://github.com/emiryasar/mcp_code_analyzer)** - ⭐ 39
   A Model Context Protocol (MCP) server implementation for comprehensive code analysis. This tool integrates with Claude Desktop to provide code analysis capabilities through natural language interactions.

2368. **[mcp-crypto-price](https://github.com/truss44/mcp-crypto-price)** - ⭐ 39
   A Model Context Protocol (MCP) server that provides real-time cryptocurrency analysis via CoinCap's API. Enables Claude and other MCP clients to fetch crypto prices, analyze market trends, and track historical data.

2369. **[mmcp](https://github.com/koki-develop/mmcp)** - ⭐ 39
   🛠️ Manage your MCP (Model Context Protocol) server definitions in one place and apply them to supported agents.

2370. **[mcp-desktop](https://github.com/http4k/mcp-desktop)** - ⭐ 39
   http4k MCP Desktop Client

2371. **[mcp-client-server-host-demo](https://github.com/danwritecode/mcp-client-server-host-demo)** - ⭐ 39
   A quick pokemon demo to showcase MCP server, client, and host

2372. **[mcp](https://github.com/kyopark2014/mcp)** - ⭐ 39
   It shows how to use model-context-protocol. 

2373. **[openrouter-deep-research-mcp](https://github.com/wheattoast11/openrouter-deep-research-mcp)** - ⭐ 39
   A multi-agent research MCP server + mini client adapter - orchestrates a net of async agents or streaming swarm to conduct ensemble consensus-backed research. Each task builds its own indexed pglite database on the fly in web assembly. Includes semantic + hybrid search, SQL execution, semaphores, prompts/resources and more

2374. **[mssql-mcp](https://github.com/daobataotie/mssql-mcp)** - ⭐ 39
   mssql mcp server

2375. **[mcp_ctl](https://github.com/runablehq/mcp_ctl)** - ⭐ 39
   A package manager to manage all your mcp servers across platforms

2376. **[algorand-mcp](https://github.com/GoPlausible/algorand-mcp)** - ⭐ 39
   Algorand Model Context Protocol (Server & Client)

2377. **[mcp-panther](https://github.com/panther-labs/mcp-panther)** - ⭐ 39
   Write detections, investigate alerts, and query logs from your favorite AI agents

2378. **[MCPToolBenchPP](https://github.com/mcp-tool-bench/MCPToolBenchPP)** - ⭐ 39
   MCPToolBench++ MCP Model Context Protocol Tool Use Benchmark on AI Agent and Model Tool Use Ability

2379. **[mcp-android-server-python](https://github.com/nim444/mcp-android-server-python)** - ⭐ 39
   MCP Android agent - This project provides an *MCP (Model Context Protocol)* server for automating Android devices using uiautomator2. It's designed to be easily plugged into AI agents like GitHub Copilot Chat, Claude, or Open Interpreter to control Android devices through natural language.

2380. **[nia](https://github.com/nozomio-labs/nia)** - ⭐ 39
   Nia is a context-augmentation layer for agents, primarily designed for coding agents. It provides them with an up-to-date knowledge base and improves their performance by 27%.

2381. **[ai-vision-mcp](https://github.com/tan-yong-sheng/ai-vision-mcp)** - ⭐ 39
   A Model Context Protocol (MCP) server that provides vision capabilities to analyze image and video

2382. **[vscode-agent-todos](https://github.com/digitarald/vscode-agent-todos)** - ⭐ 39
   Gives VS Code agent mode planning superpowers with dynamic todo lists

2383. **[dev-to-mcp](https://github.com/nickytonline/dev-to-mcp)** - ⭐ 39
   A remote Model Context Protocol (MCP) server for interacting with the dev.to public API without requiring authentication.

2384. **[pbixray-mcp-server](https://github.com/jonaolden/pbixray-mcp-server)** - ⭐ 39
   MCP server to give llms such as Claude, GitHub Copilot etc full PowerBI model context (from input .pbix) through tools based on PBIXRay python package.

2385. **[ContextPods](https://github.com/conorluddy/ContextPods)** - ⭐ 39
   Model Context Protocol management suite/factory. An MCP that can generate and manage other local MCPs in multiple languages. Uses the official SDKs for code gen.

2386. **[neurondb](https://github.com/neurondb/neurondb)** - ⭐ 39
   PostgreSQL extension for vector search, embeddings, and ML, plus NeuronAgent runtime and NeuronMCP server.

2387. **[smythos-studio](https://github.com/SmythOS/smythos-studio)** - ⭐ 39
   SmythOS Studio: Open-Source Visual AI Agent Builder and deployable runtime stack from SmythOS. Start with an intuitive drag-and-drop workspace, extend with custom code, and deploy your agents anywhere — local, cloud, or edge — with full governance and control.

2388. **[mcp-server-ios-simulator](https://github.com/atom2ueki/mcp-server-ios-simulator)** - ⭐ 39
   Model Context Protocol (MCP) implementation for iOS simulators

2389. **[mcp-sitecore-server](https://github.com/Antonytm/mcp-sitecore-server)** - ⭐ 39
   Model Context Protocol server for Sitecore

2390. **[mcp-pyautogui-server](https://github.com/hetaoBackend/mcp-pyautogui-server)** - ⭐ 39
   A MCP (Model Context Protocol) server that provides automated GUI testing and control capabilities through PyAutoGUI.

2391. **[gno](https://github.com/gmickel/gno)** - ⭐ 39
   Local AI-powered document search and editing with first-in-class hybrid retrieval, LLM answers, WebUI, REST API and MCP support for AI clients.

2392. **[How-To-Create-MCP-Server](https://github.com/nisalgunawardhana/How-To-Create-MCP-Server)** - ⭐ 38
   This guide will help you set up a basic MCP (Model Context Protocol) server in .NET, configure it in VS Code, and interact with it using Copilot Chat.

2393. **[middy-mcp](https://github.com/fredericbarthelet/middy-mcp)** - ⭐ 38
   Middy middleware for Model Context Protocol server hosting on AWS Lambda

2394. **[mcp-center](https://github.com/nautilus-ops/mcp-center)** - ⭐ 38
   A centralized platform for managing and connecting MCP servers. MCP Center provides a high-performance proxy service that enables seamless communication between MCP clients and multiple MCP servers.

2395. **[McpDotNet.Extensions.SemanticKernel](https://github.com/StefH/McpDotNet.Extensions.SemanticKernel)** - ⭐ 38
   Microsoft SemanticKernel integration for the Model Context Protocol (MCP). Enables seamless use of MCP tools as AI functions.

2396. **[okta-mcp-server](https://github.com/fctr-id/okta-mcp-server)** - ⭐ 38
   The Okta MCP Server is a groundbreaking tool built by the team at Fctr that enables AI models to interact directly with your Okta environment using the Model Context Protocol (MCP). Built specifically for IAM engineers, security teams, and Okta administrators, it implements the MCP specification to help work with Okta enitities

2397. **[grafana-mcp-analyzer](https://github.com/SailingCoder/grafana-mcp-analyzer)** - ⭐ 38
   让AI助手直接分析你的Grafana监控数据 - A Model Context Protocol server for Grafana data analysis

2398. **[mcp_weather_server](https://github.com/isdaniel/mcp_weather_server)** - ⭐ 38
   A Model Context Protocol (MCP) server that provides weather information using the Open-Meteo API.

2399. **[open-ghl-mcp](https://github.com/basicmachines-co/open-ghl-mcp)** - ⭐ 38
   An open source Model Context Protocol server for GoHighLevel API v2 with OAuth

2400. **[shodan-mcp-server](https://github.com/Cyreslab-AI/shodan-mcp-server)** - ⭐ 38
   A Model Context Protocol server that provides access to Shodan API functionality

2401. **[mcp-server-webcrawl](https://github.com/pragmar/mcp-server-webcrawl)** - ⭐ 38
   MCP server tailored to connecting web crawler data and archives

2402. **[prompt-decorators](https://github.com/synaptiai/prompt-decorators)** - ⭐ 38
   A standardized framework for enhancing how LLMs process and respond to prompts through composable decorators, featuring an official open standard specification and Python reference implementation with MCP server integration.

2403. **[DeepCo](https://github.com/succlz123/DeepCo)** - ⭐ 38
   A Chat Client for LLMs, written in Compose Multiplatform.

2404. **[vancouver](https://github.com/jameslong/vancouver)** - ⭐ 38
   Simple MCP server library for Elixir.

2405. **[cdk_pywrapper](https://github.com/sebotic/cdk_pywrapper)** - ⭐ 38
   A Python wrapper for the Chemistry Development Kit (CDK)

2406. **[mocxykit](https://github.com/shunseven/mocxykit)** - ⭐ 38
   This is an Frontend development service middleware that can be used with webpack and vite. Its main function is to visualize the configuration, manage http(s)-proxy, and mock data.

2407. **[search-scrape](https://github.com/DevsHero/search-scrape)** - ⭐ 38
   100% free, Rust-native MCP tools for AI assistants. Federated search with SearXNG, intelligent scraping with noise filtering, automatic source citations, optional research history (Qdrant), JSON output mode for agents, and privacy-first local processing — no API keys or subscriptions. 🦀🔍

2408. **[mcp-obsidian](https://github.com/fazer-ai/mcp-obsidian)** - ⭐ 38
   MCP server for Obsidian (TypeScript + Bun)

2409. **[steampipe-mcp](https://github.com/turbot/steampipe-mcp)** - ⭐ 38
   Enable AI assistants to explore and query your Steampipe data!

2410. **[HAL](https://github.com/DeanWard/HAL)** - ⭐ 38
   HAL (HTTP API Layer) is a Model Context Protocol (MCP) server that provides HTTP API capabilities to Large Language Models.

2411. **[comfy-mcp-server](https://github.com/lalanikarim/comfy-mcp-server)** - ⭐ 38
   A server using FastMCP framework to generate images based on prompts via a remote Comfy server.

2412. **[mcpmc](https://github.com/gerred/mcpmc)** - ⭐ 38
   Model Context Protocol Minecraft Server

2413. **[lunchmoney-mcp](https://github.com/akutishevsky/lunchmoney-mcp)** - ⭐ 38
   A Model Context Protocol (MCP) server implementation for LunchMoney, providing programmatic access to personal finance management through LunchMoney's API.

2414. **[autoteam](https://github.com/diazoxide/autoteam)** - ⭐ 38
   Orchestrate AI agents with YAML-driven workflows via universal Model Context Protocol (MCP)

2415. **[webscraping-ai-mcp-server](https://github.com/webscraping-ai/webscraping-ai-mcp-server)** - ⭐ 38
    A Model Context Protocol (MCP) server implementation that integrates with WebScraping.AI for web data extraction capabilities.

2416. **[thoughtbox](https://github.com/Kastalien-Research/thoughtbox)** - ⭐ 38
   Thoughtbox lets you assemble and orchestrate ad-hoc agent teams over MCP. Orchestrate Claude Code, Codex, Cursor, Antigravity, Cline, Roo Code, and any other agents you want  to work together.

2417. **[gemini-superclaude-mcp-server](https://github.com/Dianel555/gemini-superclaude-mcp-server)** - ⭐ 38
   A **complete rewrite** of the original SuperClaude MCP server with intelligent command routing, dynamic persona switching, and real MCP server orchestration for Gemini CLI.Th

2418. **[altium-mcp](https://github.com/coffeenmusic/altium-mcp)** - ⭐ 38
   Altium Model Context Protocol server and Altium API script

2419. **[fast-filesystem-mcp](https://github.com/efforthye/fast-filesystem-mcp)** - ⭐ 38
   A high-performance Model Context Protocol (MCP) server that provides secure filesystem access for Claude and other AI assistants.

2420. **[agent-mcp-gateway](https://github.com/roddutra/agent-mcp-gateway)** - ⭐ 38
   Provides per-subagent MCP access controls to Claude Code (or any MCP client) across all your MCPs and prevents context window bloat. Loads only 3 tools instead of all your MCP Server's tool definitions. Agents discover tools on-demand, only when needed. Control which servers and individual tools each agent/subagent can access.

2421. **[tomtom-mcp](https://github.com/tomtom-international/tomtom-mcp)** - ⭐ 38
   A Model Context Protocol (MCP) server providing TomTom's location services, search, routing, and traffic data to AI agents.

2422. **[adeu](https://github.com/dealfluence/adeu)** - ⭐ 38
   Agentic DOCX Redlining Engine. Enables LLMs to read Word documents and inject native Track Changes (w:ins, w:del) and Comments without breaking formatting. Includes Model Context Protocol (MCP) Server.

2423. **[teams-mcp](https://github.com/floriscornel/teams-mcp)** - ⭐ 38
   MCP server providing comprehensive Microsoft Teams and Graph API access for AI assistants including messaging, search, and user management.

2424. **[org-mcp](https://github.com/laurynas-biveinis/org-mcp)** - ⭐ 38
   Emacs Org-mode integration with Model Context Protocol (MCP) for AI-assisted task management

2425. **[embedded-debugger-mcp](https://github.com/Adancurusul/embedded-debugger-mcp)** - ⭐ 38
   A Model Context Protocol server for embedded debugging with probe-rs - supports ARM Cortex-M, RISC-V debugging via J-Link, ST-Link, and more

2426. **[mcp-konnect](https://github.com/Kong/mcp-konnect)** - ⭐ 37
   A Model Context Protocol (MCP) server for interacting with Kong Konnect APIs, allowing AI assistants to query and analyze Kong Gateway configurations, traffic, and analytics.

2427. **[mcp-client-example](https://github.com/artemnovichkov/mcp-client-example)** - ⭐ 37
   Learn how to implement MCP client with SwiftUI and Anthropic API

2428. **[offeryn](https://github.com/avahowell/offeryn)** - ⭐ 37
   Build tools for LLMs in Rust using Model Context Protocol

2429. **[youtrack-mcp](https://github.com/itsalfredakku/youtrack-mcp)** - ⭐ 37
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

2430. **[solscan-mcp](https://github.com/wowinter13/solscan-mcp)** - ⭐ 37
   An MCP server for querying Solana transactions using natural language with Solscan API

2431. **[RedBook-Search-Comment-MCP](https://github.com/chenningling/RedBook-Search-Comment-MCP)** - ⭐ 37
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client，帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布智能评论等操作。

2432. **[matlab-mcp](https://github.com/Tsuchijo/matlab-mcp)** - ⭐ 37
   Model Context Protocol server to let LLMs write and execute matlab scripts 

2433. **[nuclei-mcp](https://github.com/addcontent/nuclei-mcp)** - ⭐ 37
   An implementation of a Model Context Protocol (MCP) for the Nuclei scanner. This tool enables context-aware vulnerability scanning by intelligently providing models and context to the scanning engine, allowing for more efficient and targeted template execution

2434. **[mcp-summarization-functions](https://github.com/Braffolk/mcp-summarization-functions)** - ⭐ 37
   Provides summarised output from various actions that could otherwise eat up tokens and cause crashes for AI agents 

2435. **[mcp-tasks](https://github.com/flesler/mcp-tasks)** - ⭐ 37
   A comprehensive and efficient MCP server for task management with multi-format support (Markdown, JSON, YAML)

2436. **[openai-mcp](https://github.com/arthurcolle/openai-mcp)** - ⭐ 37
   OpenAI Code Assistant Model Context Protocol (MCP) Server

2437. **[dexpaprika-mcp](https://github.com/coinpaprika/dexpaprika-mcp)** - ⭐ 37
   DexPaprika MCP server allows access real-time and historical data on crypto tokens, DEX trading activity, and liquidity across multiple blockchains. It enables natural language queries for exploring market trends, token performance, and DeFi analytics through a standardized interface.

2438. **[Mcp.Net](https://github.com/SamFold/Mcp.Net)** - ⭐ 37
   A fully featured C# implementation of Anthropic's Model Context Protocol (MCP)

2439. **[mcp-server-leetcode](https://github.com/doggybee/mcp-server-leetcode)** - ⭐ 37
   A Model Context Protocol (MCP) server for LeetCode that provides access to problems, user data, and contest information through GraphQL

2440. **[apple-books-mcp](https://github.com/vgnshiyer/apple-books-mcp)** - ⭐ 37
   Apple Books MCP Server

2441. **[pdf-rag-mcp-server](https://github.com/hyson666/pdf-rag-mcp-server)** - ⭐ 37
   PDF RAG server for cursor.

2442. **[kitwork](https://github.com/kitwork/kitwork)** - ⭐ 37
   Automate kit workflows effortlessly with a lightweight, high-performance, fast, and flexible engine for cloud or self-hosted environments.

2443. **[octomind](https://github.com/Muvon/octomind)** - ⭐ 37
   Highly configurable autonomous efficient-first agentic AI framework for CLI

2444. **[Readwise-Reader-MCP](https://github.com/edricgsh/Readwise-Reader-MCP)** - ⭐ 37
   A Model Context Protocol (MCP) server for the Readwise Reader API, built with TypeScript and the official Claude SDK.

2445. **[TWSEMCPServer](https://github.com/twjackysu/TWSEMCPServer)** - ⭐ 37
   台灣證交所OpenAPI 的 MCP Server

2446. **[polymarket-mcp](https://github.com/ozgureyilmaz/polymarket-mcp)** - ⭐ 37
   a mcp server for polymarket

2447. **[GDB-MCP](https://github.com/smadi0x86/GDB-MCP)** - ⭐ 37
   An MCP server that enables LLMs to interact with GDB and LLDB for binary debugging and analysis.

2448. **[mcp-mistral-ocr](https://github.com/everaldo/mcp-mistral-ocr)** - ⭐ 37
   Model Context Protocol (MCP) Server for Mistral OCR API

2449. **[mcp-ssh-manager](https://github.com/bvisible/mcp-ssh-manager)** - ⭐ 37
   MCP SSH Server: 37 tools for remote SSH management | Claude Code & OpenAI Codex | DevOps automation, backups, database operations, health monitoring

2450. **[mcp-flight-search](https://github.com/arjunprabhulal/mcp-flight-search)** - ⭐ 37
   MCP Server implementation for the Model Context Protocol (MCP) enabling AI tool usage - Realtime Flight Search 

2451. **[mcp-accessibility-scanner](https://github.com/JustasMonkev/mcp-accessibility-scanner)** - ⭐ 37
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core.

2452. **[Web-Algebra](https://github.com/AtomGraph/Web-Algebra)** - ⭐ 37
   Suite of generic Linked Data/SPARQL as well as LinkedDataHub-specific MCP tools

2453. **[mcp-anywhere](https://github.com/locomotive-agency/mcp-anywhere)** - ⭐ 37
   A unified gateway for Model Context Protocol (MCP) servers that lets you discover, configure, and access MCP tools from any GitHub repository through a single endpoint.

2454. **[keycloak-model-context-protocol](https://github.com/ChristophEnglisch/keycloak-model-context-protocol)** - ⭐ 37
   MCP server implementation for Keycloak user management. Enables AI-powered administration of Keycloak users and realms through the Model Context Protocol (MCP). Seamlessly integrates with Claude Desktop and other MCP clients for automated user operations.

2455. **[reaper-reapy-mcp](https://github.com/wegitor/reaper-reapy-mcp)** - ⭐ 36
   Reaper and MCP or AI integration A Python application for controlling REAPER Digital Audio Workstation (DAW) using the MCP(Model context protocol).

2456. **[mcp-go](https://github.com/riza-io/mcp-go)** - ⭐ 36
   Build Model Context Protocol (MCP) servers in Go

2457. **[baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server)** - ⭐ 36
   特定のWeb APIに関するBaselineの状況を提供するModel Context Protocolサーバー

2458. **[example-mcp-server](https://github.com/kirill-markin/example-mcp-server)** - ⭐ 36
   A ready-to-use MCP (Model Context Protocol) server template for extending Cursor IDE with custom tools. Deploy your own server to Heroku with one click, create custom commands, and enhance your Cursor IDE experience. Perfect for developers who want to add their own tools and commands to Cursor IDE without complex setup.

2459. **[mcp-governance-sdk](https://github.com/ithena-one/mcp-governance-sdk)** - ⭐ 36
   Enterprise Governance Layer (Identity, RBAC, Credentials, Auditing, Logging, Tracing) for the Model Context Protocol SDK

2460. **[OmniMind](https://github.com/Techiral/OmniMind)** - ⭐ 36
   OmniMind: An open-source Python library for effortless MCP (Model Context Protocol) integration, AI Agents, AI workflows, and AI Automations. Plug & Play AI Tools for MCP Servers and Clients, powered by Google Gemini.

2461. **[flutter-mcp-ai-chat](https://github.com/leehack/flutter-mcp-ai-chat)** - ⭐ 36
   Demonstrate how to implement MCP Client in Flutter application with AI.

2462. **[FastDomainCheck-MCP-Server](https://github.com/bingal/FastDomainCheck-MCP-Server)** - ⭐ 36
   A Model Context Protocol for checking domain name registration status in bulk.

2463. **[mcp-debug](https://github.com/giantswarm/mcp-debug)** - ⭐ 36

2464. **[mlb-api-mcp](https://github.com/guillochon/mlb-api-mcp)** - ⭐ 36
   A Model Context Protocol (MCP) server that provides comprehensive access to MLB statistics and baseball data through a FastMCP-based interface.

2465. **[code-mcp](https://github.com/54yyyu/code-mcp)** - ⭐ 36
   Code-MCP: Connect Claude AI to your development environment through the Model Context Protocol (MCP), enabling terminal commands and file operations through the AI interface.

2466. **[MCPNotes](https://github.com/9Ninety/MCPNotes)** - ⭐ 36
   A simple note-taking MCP server for recording and managing notes with AI models.

2467. **[MCP-Server-Creator](https://github.com/GongRzhe/MCP-Server-Creator)** - ⭐ 36
   A powerful Model Context Protocol (MCP) server that creates other MCP servers! This meta-server provides tools for dynamically generating FastMCP server configurations and Python code.

2468. **[mcp-wikidata](https://github.com/zzaebok/mcp-wikidata)** - ⭐ 36
   A server implementation for Wikidata API using the Model Context Protocol (MCP).

2469. **[mcp-gateway](https://github.com/theognis1002/mcp-gateway)** - ⭐ 36
   Model Context Protocol (MCP) Gateway & Registry - Central hub for managing tools, resources, and prompts for MCP-compatible LLMs. Translates REST APIs into MCP, builds virtual MCP servers with security and observability, and bridges multiple transports (stdio, SSE, streamable HTTP).

2470. **[tasker-mcp](https://github.com/dceluis/tasker-mcp)** - ⭐ 36
   An MCP server for Android's Tasker automation app.

2471. **[MCP-Microsoft-Office](https://github.com/Aanerud/MCP-Microsoft-Office)** - ⭐ 36
   an local MCP server you can run on your env, connecting you to Microsoft Graph, and the complete M365 eco system.

2472. **[nostr-mcp](https://github.com/AbdelStark/nostr-mcp)** - ⭐ 36
   A Nostr MCP server that allows to interact with Nostr, enabling posting notes, and more.

2473. **[mcp-server-antv](https://github.com/antvis/mcp-server-antv)** - ⭐ 36
   🧑🏻‍💻 MCP Server for @antvis visualization development, which provides documentation context and examples for visualization developers.

2474. **[FastAPI-BitNet](https://github.com/grctest/FastAPI-BitNet)** - ⭐ 36
   Running Microsoft's BitNet inference framework via FastAPI, Uvicorn and Docker.

2475. **[reactbits-mcp-server](https://github.com/ceorkm/reactbits-mcp-server)** - ⭐ 36
   MCP server providing access to 135+ animated React components from ReactBits.dev (9.2/10 test score)

2476. **[mcp-gitlab-server](https://github.com/yoda-digital/mcp-gitlab-server)** - ⭐ 36
   Enhanced MCP server for GitLab: group projects listing and activity tracking

2477. **[linkedin-mcp-server](https://github.com/Dishant27/linkedin-mcp-server)** - ⭐ 36
   Model Context Protocol (MCP) server for LinkedIn API integration

2478. **[whatsapp-mcp](https://github.com/felipeadeildo/whatsapp-mcp)** - ⭐ 36
   WhatsApp Unofficial MCP Server

2479. **[memcord](https://github.com/ukkit/memcord)** - ⭐ 36
   🧠 Privacy-first MCP server for AI memory management. Save, search & organize chat history with intelligent  summarization.

2480. **[a11y-mcp](https://github.com/priyankark/a11y-mcp)** - ⭐ 36
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core. Use the results in an agentic loop with your favorite AI assistants (Amp/Cline/Cursor/GH Copilot) and let them fix a11y issues for you!

2481. **[storyblok-mcp-server](https://github.com/Kiran1689/storyblok-mcp-server)** - ⭐ 36
   A modular, extensible MCP Server for managing Storyblok spaces, stories, components, assets, workflows, and more via the Model Context Protocol (MCP).

2482. **[mcp-google-cse](https://github.com/Richard-Weiss/mcp-google-cse)** - ⭐ 36
   A Model Context Protocol server that provides search capabilities using a Google CSE (custom search engine).

2483. **[mcp-gemini-server](https://github.com/bsmi021/mcp-gemini-server)** - ⭐ 35
   This project provides a dedicated MCP (Model Context Protocol) server that wraps the @google/genai SDK. It exposes Google's Gemini model capabilities as standard MCP tools, allowing other LLMs (like Cline) or MCP-compatible systems to leverage Gemini's features as a backend workhorse.

2484. **[esa-mcp-server](https://github.com/d-kimuson/esa-mcp-server)** - ⭐ 35
   esa の Model Context Protocol サーバー実装

2485. **[mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client)** - ⭐ 35
   LangChain.js client for Model Context Protocol.

2486. **[codebase-mcp](https://github.com/danyQe/codebase-mcp)** - ⭐ 35
   Open-source AI development assistant via Model Context Protocol (MCP). Turn Claude or any LLM into your personal coding assistant. Privacy-first with local semantic search, AI-assisted editing, persistent memory, and quality-checked code generation. Built for Python & React. Free alternative to paid AI coding tools.

2487. **[mcp-bundle](https://github.com/symfony/mcp-bundle)** - ⭐ 35
   Symfony integration bundle for Model Context Protocol (via official mcp/sdk)

2488. **[mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server)** - ⭐ 35
   Model Context Protocol (MCP) server for Databricks that empowers AI agents to autonomously interact with Unity Catalog metadata. Enables data discovery, lineage analysis, and intelligent SQL execution. Agents explore catalogs/schemas/tables, understand relationships, discover notebooks/jobs, and execute queries - greatly reducing ad-hoc query time.

2489. **[mcp-front](https://github.com/stainless-api/mcp-front)** - ⭐ 35
   Auth proxy for Model Context Protocol servers - adds authentication to MCP tools for Claude.ai, Claude Code, Cursor, Gemini

2490. **[mcp-sandbox](https://github.com/JohanLi233/mcp-sandbox)** - ⭐ 35
   Python sandboxes for llms

2491. **[ai-workshop](https://github.com/dotnet-presentations/ai-workshop)** - ⭐ 35
   Building GenAI Apps in C#: AI Templates, GitHub Models, Azure OpenAI & More

2492. **[mcp-crew-ai](https://github.com/adam-paterson/mcp-crew-ai)** - ⭐ 35
   MCP Crew AI Server is a lightweight Python-based server designed to run, manage and create CrewAI workflows.

2493. **[mcp-tung-shing](https://github.com/baranwang/mcp-tung-shing)** - ⭐ 35
   中国传统黄历 MCP 服务 | Chinese Traditional Almanac MCP Service

2494. **[agentic-commerce-protocol-demo](https://github.com/locus-technologies/agentic-commerce-protocol-demo)** - ⭐ 35
   Reference implementation of OpenAI's Agentic Commerce Protocol (ACP)

2495. **[coin_api_mcp](https://github.com/longmans/coin_api_mcp)** - ⭐ 35
   A Model Context Protocol server that provides access to CoinMarketCap's cryptocurrency data. This server enables AI-powered applications to retrieve cryptocurrency listings, quotes, and detailed information about various coins.

2496. **[trivy-mcp](https://github.com/aquasecurity/trivy-mcp)** - ⭐ 35
   Trivy plugin for starting an MCP server

2497. **[mcp](https://github.com/screenshotone/mcp)** - ⭐ 35
   A simple implementation of an MCP server for the ScreenshotOne API

2498. **[atlas-docs-mcp](https://github.com/CartographAI/atlas-docs-mcp)** - ⭐ 35
   Provide LLMs hosted, clean markdown documentation of libraries and frameworks

2499. **[salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server)** - ⭐ 35
   A comprehensive Model Context Protocol (MCP) server that provides seamless Salesforce integration for AI development tools like Claude Desktop, Cline, and other MCP-compatible clients.

2500. **[tinyagent](https://github.com/askbudi/tinyagent)** - ⭐ 35
   Tiny Agent: Production-Ready LLM Agent SDK for Every Developer

2501. **[linkedapi-mcp](https://github.com/Linked-API/linkedapi-mcp)** - ⭐ 35
   MCP server that lets AI assistants control LinkedIn accounts and retrieve real-time data.

2502. **[unreal-mcp](https://github.com/runeape-sats/unreal-mcp)** - ⭐ 35
   Unreal Engine MCP server for Claude Desktop (early alpha preview)

2503. **[RiMCP_hybrid](https://github.com/h7lu/RiMCP_hybrid)** - ⭐ 35
   Rimworld Coding RAG MCP server

2504. **[linkedin-mcpserver](https://github.com/felipfr/linkedin-mcpserver)** - ⭐ 35
   A powerful Model Context Protocol server for LinkedIn API integration

2505. **[storybook-mcp](https://github.com/mcpland/storybook-mcp)** - ⭐ 35
   A MCP server for Storybook.

2506. **[diy-tools-mcp](https://github.com/hesreallyhim/diy-tools-mcp)** - ⭐ 35
   An MCP server that allows users to dynamically add custom tools/functions at runtime

2507. **[RivalSearchMCP](https://github.com/damionrashford/RivalSearchMCP)** - ⭐ 35
   Deep Research & Competitor Analysis MCP for Claude & Cursor. No API Keys. Features: Web Search, Social Media (Reddit/HN), Trends & OCR.

2508. **[Handler](https://github.com/alDuncanson/Handler)** - ⭐ 35
   A2A Protocol client and developer toolkit.

2509. **[mcp-file-context-server](https://github.com/bsmi021/mcp-file-context-server)** - ⭐ 35
   A Model Context Protocol (MCP) server that provides file system context to Large Language Models (LLMs). This server enables LLMs to read, search, and analyze code files with advanced caching and real-time file watching capabilities.

2510. **[mcp-zero](https://github.com/zeromicro/mcp-zero)** - ⭐ 35
   Model Context Protocol (MCP) server for go-zero framework - Generate APIs, RPC services, and models with AI assistance.

2511. **[mcp-toolkit](https://github.com/metosin/mcp-toolkit)** - ⭐ 34
   a lib to build MCP clients and MCP servers in Clojure(script)

2512. **[awesome-mcp-personas](https://github.com/toolprint/awesome-mcp-personas)** - ⭐ 34
   A curated collection of persona-based mcp server & tool groupings.

2513. **[mcp-security-inspector](https://github.com/purpleroc/mcp-security-inspector)** - ⭐ 34
   一个用于检测Model Context Protocol (MCP)安全性的Chrome扩展工具。

2514. **[mcp-client-auth](https://github.com/dzhng/mcp-client-auth)** - ⭐ 34
   A TypeScript library providing OAuth2 authentication utilities for Model Context Protocol (MCP) clients. This library simplifies the process of adding OAuth authentication to MCP client implementations.

2515. **[MCPSwiftWrapper](https://github.com/jamesrochabrun/MCPSwiftWrapper)** - ⭐ 34
   A light wrapper around mcp-swift-sdk for easy usage of MCP clients in Swift

2516. **[chat-nextjs-mcp-client](https://github.com/shricodev/chat-nextjs-mcp-client)** - ⭐ 34
   ⚡ Chat MCP Client for Remote hosted MCP Servers (with Composio) and locally hosted MCP servers. 📡

2517. **[mcp-starter](https://github.com/instructa/mcp-starter)** - ⭐ 34
   A super simple Starter to build your own MCP Server

2518. **[mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal)** - ⭐ 34
   Model Context Protocol Server for Apache OpenDAL™

2519. **[meta-prompt-mcp-server](https://github.com/tisu19021997/meta-prompt-mcp-server)** - ⭐ 34
   Turn any MCP Client into a "multi-agent" system (via prompting)

2520. **[aio-mcp](https://github.com/athapong/aio-mcp)** - ⭐ 34
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows. Folk from https://github.com/nguyenvanduocit/all-in-one-model-context-protocol

2521. **[llm-tools-mcp](https://github.com/VirtusLab/llm-tools-mcp)** - ⭐ 34
   Connect to MCP servers right from your shell. Plugin for simonw/llm.

2522. **[macOS-Notification-MCP](https://github.com/devizor/macOS-Notification-MCP)** - ⭐ 34
   macOS Notification MCP enables AI assistants to trigger native macOS sounds, visual notifications, and text-to-speech. Built for Claude and other AI models using the Model Context Protocol.

2523. **[jina-mcp-tools](https://github.com/PsychArch/jina-mcp-tools)** - ⭐ 34
   A Model Context Protocol (MCP) server that integrates with Jina AI Search Foundation APIs.

2524. **[godoc-mcp-server](https://github.com/yikakia/godoc-mcp-server)** - ⭐ 34
   A mcp server provide infomation from pkg.go.dev. For all golang programmers

2525. **[DBJavaGenix](https://github.com/ZhaoXingPeng/DBJavaGenix)** - ⭐ 34
   智能数据库代码生成工具基于MCP架构，支持MySQL等多种数据库，自动生成Entity、DAO、Service及Controller等完整分层代码，大幅提升开发效率。依托MCP协议，具备强大扩展与集成能力，可智能推断表关系与业务语义。集成Mustache、MapStruct和Lombok，实现跨语言生成、高效映射和代码简化，并提供依赖自动管理，保障项目稳定。

2526. **[mcp-prompt-server-go](https://github.com/smallnest/mcp-prompt-server-go)** - ⭐ 34
   一个提供优秀prompt的Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地和使用。提供tool和prompt两种形式

2527. **[mcp-server](https://github.com/VapiAI/mcp-server)** - ⭐ 34
   Vapi MCP Server

2528. **[chessagineweb](https://github.com/jalpp/chessagineweb)** - ⭐ 34
   The most underrated FOSS chess interface that combines AI agents and chess engines into one unified platform. 

2529. **[nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server)** - ⭐ 34
   A Model Context Protocol (MCP) server that provides Nostr capabilities to AI agents

2530. **[openscad-mcp](https://github.com/quellant/openscad-mcp)** - ⭐ 34
   A Model Context Protocol (MCP) server for OpenSCAD 3D modeling and rendering

2531. **[prometheus_mcp_server](https://github.com/CaesarYangs/prometheus_mcp_server)** - ⭐ 34
   A Model Context Protocol (MCP) server enabling LLMs to query, analyze, and interact with Prometheus databases through predefined routes.

2532. **[React-Native-MCP](https://github.com/MrNitro360/React-Native-MCP)** - ⭐ 34
   A Model Context Protocol (MCP) server providing comprehensive guidance and best practices for React Native development based on official React Native documentation.

2533. **[codelogic-mcp-server](https://github.com/CodeLogicIncEngineering/codelogic-mcp-server)** - ⭐ 34
   An MCP Server to utilize Codelogic's rich software dependency data in your AI programming assistant.

2534. **[any-script-mcp](https://github.com/izumin5210/any-script-mcp)** - ⭐ 34
   An MCP server that exposes arbitrary CLI tools and shell scripts as MCP Tools

2535. **[modao-proto-mcp](https://github.com/modao-dev/modao-proto-mcp)** - ⭐ 34
   Modao Proto MCP is a standalone MCP (Model Context Protocol) service designed to connect Modao Proto design tools with AI models.

2536. **[mcp-zap-server](https://github.com/dtkmn/mcp-zap-server)** - ⭐ 34
   A Spring Boot application exposing OWASP ZAP as an MCP (Model Context Protocol) server. It lets any MCP‑compatible AI agent (e.g., Claude Desktop, Cursor) orchestrate ZAP actions—spider, active scan, import OpenAPI specs, and generate reports.

2537. **[claude-code-mcp](https://github.com/KunihiroS/claude-code-mcp)** - ⭐ 34
   MCP Server connects with claude code local command.

2538. **[claude-mcp](https://github.com/cnych/claude-mcp)** - ⭐ 34
   Claude Unified Model Context Interaction Protocol

2539. **[keycloak-mcp-server](https://github.com/sshaaf/keycloak-mcp-server)** - ⭐ 34
   An MCP server for Keycloak,  designed to work with Keycloak for identity and access management, covering, Users, Realms, Clients, Roles, Groups, IDPs, Authentication. Searching keycloak discourse, Native builds available.

2540. **[mcp-domain-availability](https://github.com/imprvhub/mcp-domain-availability)** - ⭐ 34
   A Model Context Protocol (MCP) server that enables Claude Desktop to check domain availability across 50+ TLDs. Features DNS/WHOIS verification, bulk checking, and smart suggestions. Zero-clone installation via uvx.

2541. **[mermaid-mcp](https://github.com/Narasimhaponnada/mermaid-mcp)** - ⭐ 34

2542. **[nvim-mcp](https://github.com/linw1995/nvim-mcp)** - ⭐ 34
   A Model Context Protocol (MCP) server that provides seamless integration with Neovim instances, enabling AI assistants to interact with your editor through connections and access diagnostic information via structured resources.

2543. **[adk-python-mcp-client](https://github.com/arjunprabhulal/adk-python-mcp-client)** - ⭐ 33
   Demo of ADK (Agent Development Kit) as an MCP (Model Context Protocol) client for flight search capabilities.

2544. **[mcp-scala](https://github.com/windymelt/mcp-scala)** - ⭐ 33
   Model Context Protocol server written in Scala

2545. **[mcp-google-calendar](https://github.com/markelaugust74/mcp-google-calendar)** - ⭐ 33
   A Model Context Protocol (MCP) server implementation for Google Calendar integration. Create and manage calendar events directly through Claude or other AI assistants.

2546. **[mcp-registry](https://github.com/ARadRareness/mcp-registry)** - ⭐ 33
   A central registry and HTTP interface for coordinating Model Context Protocol (MCP) servers.

2547. **[Outlook_Calendar_MCP](https://github.com/merajmehrabi/Outlook_Calendar_MCP)** - ⭐ 33
   A Model Context Protocol (MCP) server that allows Claude to access and manage your local Microsfot Outlook calendar (Windows only).

2548. **[mcp-server-text-editor](https://github.com/bhouston/mcp-server-text-editor)** - ⭐ 33
   An open source implementation of the Claude built-in text editor tool

2549. **[McpToolkit](https://github.com/nuskey8/McpToolkit)** - ⭐ 33
   Lightweight, fast, NativeAOT compatible MCP (Model Context Protocol) framework for .NET

2550. **[mcp-api-gateway](https://github.com/rflpazini/mcp-api-gateway)** - ⭐ 33
   A universal MCP (Model Context Protocol) server to integrate any API with Claude Desktop using only Docker configurations.

2551. **[mcp-browser-agent](https://github.com/imprvhub/mcp-browser-agent)** - ⭐ 33
   A Model Context Protocol (MCP) integration that provides Claude Desktop with autonomous browser automation capabilities. This agent enables Claude to interact with web content, manipulate DOM elements, execute JavaScript, and perform API requests.

2552. **[evernote-mcp-server](https://github.com/brentmid/evernote-mcp-server)** - ⭐ 33
   Evernote MCP server - allows LLMs that support MCP (like Claude Desktop) to query your notes in Evernote

2553. **[twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server)** - ⭐ 33
   A Model Context Protocol (MCP) server for Twenty CRM integration. Enables natural language interactions with your CRM data through Claude and other AI assistants. Supports CRUD operations, dynamic schema discovery, and advanced search across people, companies, tasks, and notes.

2554. **[iotdb-mcp-server](https://github.com/apache/iotdb-mcp-server)** - ⭐ 33
   Apache IoTDB MCP Server

2555. **[1mcp](https://github.com/buremba/1mcp)** - ⭐ 33
   Let your agent write code and execute code directly in the browser with WASM

2556. **[DMCPServer](https://github.com/Daniel09Fernandes/DMCPServer)** - ⭐ 33
   Dinos MCP Server, make your code, on MCP Action and execute by AI

2557. **[mcp-sync](https://github.com/ztripez/mcp-sync)** - ⭐ 33
   Sync MCP (Model Context Protocol) configurations across AI tools

2558. **[awesome-blockchain-mcps](https://github.com/royyannick/awesome-blockchain-mcps)** - ⭐ 33
   🔗 A curated list of Blockchain & Crypto Model Context Protocol (MCP) servers. Enabling AI Agents to interact with the Blockchain, Web3, DeFi, on-chain data, on-chain actions, etc.  🚀

2559. **[mcp-veo2](https://github.com/mario-andreschak/mcp-veo2)** - ⭐ 33
   MCP for Video- or Image-Generation with Google VEO2

2560. **[kaggle-mcp](https://github.com/arrismo/kaggle-mcp)** - ⭐ 33
   MCP server for Kaggle

2561. **[mcp-launcher](https://github.com/moeru-ai/mcp-launcher)** - ⭐ 33
   🐳🧩 Easy to use MCP builder & launcher for all possible MCP servers, just like Ollama for models!

2562. **[kanban-mcp](https://github.com/eyalzh/kanban-mcp)** - ⭐ 33
   MCP server providing kanban-based task management memory for complex multi-session workflows with AI agents

2563. **[forgejo-mcp](https://github.com/raohwork/forgejo-mcp)** - ⭐ 33
   A MCP server that enables you to manage Gitea/Forgejo repositories through AI assistants

2564. **[mentor-mcp-server](https://github.com/cyanheads/mentor-mcp-server)** - ⭐ 33
   A Model Context Protocol server providing LLM Agents a second opinion via AI-powered Deepseek-Reasoning R1 mentorship capabilities, including code review, design critique, writing feedback, and idea brainstorming through the Deepseek API.

2565. **[wezterm-mcp](https://github.com/hiraishikentaro/wezterm-mcp)** - ⭐ 33
   About A Model Context Protocol server that executes commands in the current WezTerm session

2566. **[mcp-tool-filter](https://github.com/Portkey-AI/mcp-tool-filter)** - ⭐ 33
   Ultra-fast semantic tool filtering for MCP (Model Context Protocol) servers using embedding similarity. Reduce your tool context from 1000+ tools down to the most relevant 10-20 tools in under 10ms.

2567. **[awesome-devops-mcp](https://github.com/agenticdevops/awesome-devops-mcp)** - ⭐ 33
   List of Awesome MCP Servers and Clients for building Agentic Devops 

2568. **[SUMO-MCP-Server](https://github.com/XRDS76354/SUMO-MCP-Server)** - ⭐ 33
   SUMO-MCP 是一个连接大语言模型 (LLM) 与 Eclipse SUMO 交通仿真的中间件。通过 Model Context Protocol (MCP)，它允许 AI 智能体（如 Claude, Cursor, TRAE等）直接调用 SUMO 的核心功能，实现从OpenStreetMap 数据获取、路网生成、需求建模到仿真运行与信号优化的全流程自动化。

2569. **[svgmaker-mcp](https://github.com/GenWaveLLC/svgmaker-mcp)** - ⭐ 33
   Model Context Protocol server for SVGMaker - AI-powered SVG generation and editing. Seamlessly integrate SVG creation into AI workflows.

2570. **[postman-mcp](https://github.com/SalehKhatri/postman-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server that provides seamless integration with the Postman API. This package enables AI assistants and applications to interact with Postman workspaces, collections, requests, environments, and folders programmatically.

2571. **[filesystem-mcp-server](https://github.com/cyanheads/filesystem-mcp-server)** - ⭐ 32
   A Model Context Protocol (MCP) server for platform-agnostic file capabilities, including advanced search/replace and directory tree traversal

2572. **[mcp-nats](https://github.com/sinadarbouy/mcp-nats)** - ⭐ 32
   A Model Context Protocol (MCP) server for NATS messaging system integration

2573. **[zilliz-mcp-server](https://github.com/zilliztech/zilliz-mcp-server)** - ⭐ 32
   A Model Context Protocol (MCP) server seamlessly connecting AI Agents and AI coding tools with Zilliz Cloud  https://zilliz.com/

2574. **[azure-functions-mcp-extension](https://github.com/Azure/azure-functions-mcp-extension)** - ⭐ 32
   Model Context Protocol extension for Azure Functions.

2575. **[laravel-mcp-client](https://github.com/scriptoshi/laravel-mcp-client)** - ⭐ 32

2576. **[crawl-mcp](https://github.com/wutongci/crawl-mcp)** - ⭐ 32
   完整的微信文章抓取MCP服务器 - 基于Model Context Protocol (MCP)的智能网页抓取工具，专为Cursor IDE和AI工具设计。

2577. **[fantasy-football-mcp-public](https://github.com/derekrbreese/fantasy-football-mcp-public)** - ⭐ 32
   Yahoo Fantasy Football MCP server for Claude Desktop - Advanced lineup optimization, draft assistance, and league management. Built using Claude Code.

2578. **[sunnysideFigma-Context-MCP](https://github.com/tercumantanumut/sunnysideFigma-Context-MCP)** - ⭐ 32
   A comprehensive Model Context Protocol (MCP) server that bridges Figma designs with AI development workflows. It provides 30 specialized tools for extracting pixel-perfect code, assets, and component structures directly from Figma designs.

2579. **[openbim-mcp](https://github.com/helenkwok/openbim-mcp)** - ⭐ 32
   Model Context Protocol (MCP) server for openBIM

2580. **[mcpc](https://github.com/OlaHulleberg/mcpc)** - ⭐ 32
   An extension to MCP (Model-Context-Protocol) that enables two-way asynchronous communication between LLMs and tools through the already existing MCP transport - no additional transport layer needed.

2581. **[authenticator_mcp](https://github.com/firstorderai/authenticator_mcp)** - ⭐ 32
   A secure MCP (Model Context Protocol) server that enables AI agents to interact with the Authenticator App.

2582. **[n8n-mcp](https://github.com/vredrick/n8n-mcp)** - ⭐ 32
   n8n MCP Server - Documentation and tools for n8n nodes via Model Context Protocol with SSE support

2583. **[mcp_server](https://github.com/peppemas/mcp_server)** - ⭐ 32
   A C++ implementation of a Model Context Protocol Server with a pluggable module architecture.

2584. **[mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks)** - ⭐ 32
   This Model Context Protocol (MCP) server provides a bridge between LLMs and Google Tasks, allowing you to manage your task lists and tasks directly through Claude.

2585. **[mcp-server](https://github.com/membranehq/mcp-server)** - ⭐ 32
   MCP Server for Membrane

2586. **[copilot-security-instructions](https://github.com/Robotti-io/copilot-security-instructions)** - ⭐ 32
   ✨ A customizable copilot-instructions.md ruleset & prompts to guide GitHub Copilot toward secure coding defaults in Java, Node.js, C# and Python. Blocks risky patterns, teaches safe habits.

2587. **[pushover-mcp](https://github.com/AshikNesin/pushover-mcp)** - ⭐ 32
   A MCP implementation for sending notifications via Pushover

2588. **[Direwolf](https://github.com/Framebuffers/Direwolf)** - ⭐ 32
   Distributed Data Processing Pipeline for MCP.

2589. **[imagegen-mcp](https://github.com/spartanz51/imagegen-mcp)** - ⭐ 32
   MCP server for OpenAI Image Generation & Editing — text-to-image, image-to-image (with mask), no extra plugins.

2590. **[capacities-mcp](https://github.com/jem-computer/capacities-mcp)** - ⭐ 32
   Capacities×MCP

2591. **[shadcn-svelte-mcp](https://github.com/Michael-Obele/shadcn-svelte-mcp)** - ⭐ 32
   Mastra MCP server and tooling for the shadcn-svelte component docs and developer utilities.

2592. **[PubChem-MCP-Server](https://github.com/Augmented-Nature/PubChem-MCP-Server)** - ⭐ 32
   A comprehensive Model Context Protocol (MCP) server for accessing the PubChem chemical database. This server provides access to over 110 million chemical compounds with extensive molecular properties, bioassay data, and chemical informatics tools.

2593. **[context-awesome](https://github.com/bh-rat/context-awesome)** - ⭐ 32
   awesome-lists now available as MCP server for you agent.

2594. **[reaper-mcp](https://github.com/itsuzef/reaper-mcp)** - ⭐ 32
   A comprehensive Model Context Protocol (MCP) server that enables AI agents to create fully mixed and mastered tracks in REAPER with both MIDI and audio capabilities.

2595. **[midi-mcp-server](https://github.com/tubone24/midi-mcp-server)** - ⭐ 32
   MIDI MCP Server is a Model Context Protocol (MCP) server that enables AI models to generate MIDI files from text-based music data. This tool allows for programmatic creation of musical compositions through a standardized interface.

2596. **[ptt_mcp_server](https://github.com/PyPtt/ptt_mcp_server)** - ⭐ 32
   The best PTT MCP server

2597. **[mcp-appstore](https://github.com/appreply-co/mcp-appstore)** - ⭐ 32
   This is an MCP server that provides tools to LLMs for searching and analyzing apps from both Google Play Store and Apple App Store – perfect for ASO.

2598. **[PixVerse-MCP](https://github.com/PixVerseAI/PixVerse-MCP)** - ⭐ 32
   Official PixVerse Model Context Protocol (MCP) server that enables interaction with powerful AI video generation APIs.

2599. **[MCPDocSearch](https://github.com/alizdavoodi/MCPDocSearch)** - ⭐ 32
   This project provides a toolset to crawl websites wikis, tool/library documentions and generate Markdown documentation, and make that documentation searchable via a Model Context Protocol (MCP) server, designed for integration with tools like Cursor.

2600. **[lets-learn-mcp-java](https://github.com/microsoft/lets-learn-mcp-java)** - ⭐ 32
   Learn how to build Java-based MCP Servers and Clients with LangChain4J and Quarkus

2601. **[mcp-server-lib.el](https://github.com/laurynas-biveinis/mcp-server-lib.el)** - ⭐ 32
   Emacs Lisp implementation of the Model Context Protocol

2602. **[azure-container-apps-ai-mcp](https://github.com/Azure-Samples/azure-container-apps-ai-mcp)** - ⭐ 32
   This project showcases how to use the MCP protocol with Azure OpenAI. It provides a simple example to interact with OpenAI's API seamlessly via an MCP server and client.

2603. **[keynote-mcp](https://github.com/easychen/keynote-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server that enables AI assistants to control Keynote presentations through AppleScript automation.

2604. **[yahoo-finance-server](https://github.com/AgentX-ai/yahoo-finance-server)** - ⭐ 32
   A Model Context Protocol (MCP) server that lets your AI interact with Yahoo Finance to get comprehensive stock market data, news, financials, and more

2605. **[hana-mcp-server](https://github.com/HatriGt/hana-mcp-server)** - ⭐ 32
   Model Context Server Protocol for your HANA DB

2606. **[MCP-Scanner](https://github.com/knostic/MCP-Scanner)** - ⭐ 32
   Advanced Shodan-based scanner for discovering, verifying, and enumerating Model Context Protocol (MCP) servers and AI infrastructure tools over HTTP & SSE.

2607. **[xhs-mcp](https://github.com/Algovate/xhs-mcp)** - ⭐ 32
   用于小红书（xiaohongshu.com）的 Model Context Protocol（MCP）服务器与 CLI 工具，支持登录、发布、搜索、推荐等自动化能力

2608. **[nestjs-starter](https://github.com/hmake98/nestjs-starter)** - ⭐ 32
   Production-ready NestJS boilerplate with JWT auth, PostgreSQL/Prisma, AWS S3/SES, Bull/Redis queues, Docker/K8s support, and MCP integration for AI capabilities

2609. **[devduck](https://github.com/cagataycali/devduck)** - ⭐ 32
   Minimalist AI agent that fixes itself when things break.

2610. **[mcp-wasm](https://github.com/beekmarks/mcp-wasm)** - ⭐ 32
   A proof-of-concept implementation of a Model Context Protocol (MCP) server that runs in WebAssembly (WASM) within a web browser. This project demonstrates the integration of MCP tools and resources in a browser environment.

2611. **[adb-mcp](https://github.com/srmorete/adb-mcp)** - ⭐ 32
   An MCP (Model Context Protocol) server for interacting with Android devices through ADB in TypeScript.

2612. **[Learn-Model-Context-Protocol-with-Python](https://github.com/PacktPublishing/Learn-Model-Context-Protocol-with-Python)** - ⭐ 32
   Learn Model Context Protocol with Python, published by Packt

2613. **[Fusion-360-MCP-Server](https://github.com/AuraFriday/Fusion-360-MCP-Server)** - ⭐ 32
   Control Fusion 360 with any AI through Model Context Protocol (MCP)

2614. **[simple-psql-mcp](https://github.com/NetanelBollag/simple-psql-mcp)** - ⭐ 31
   A beginner-friendly MCP server template featuring a PostgreSQL connector with clean, easy-to-understand code. Perfect for developers new to Model Context Protocol who want to experiment and create their own AI tool connectors with minimal setup.

2615. **[MCPCorpus](https://github.com/Snakinya/MCPCorpus)** - ⭐ 31
   MCPCorpus is a comprehensive dataset for analyzing the Model Context Protocol (MCP) ecosystem, containing ~14K MCP servers and 300 MCP clients with 20+ normalized metadata attributes.

2616. **[seatunnel-mcp](https://github.com/ocean-zhc/seatunnel-mcp)** - ⭐ 31
   A Model Context Protocol (MCP) server for Apache Seatunnel.  This provides access to your Apache Seatunnel RESTful API V2 instance and the surrounding ecosystem.

2617. **[mcp-weather](https://github.com/TimLukaHorstmann/mcp-weather)** - ⭐ 31
   A Model Context Protocol (MCP) server that provides hourly and daily weather forecasts using the AccuWeather API.

2618. **[Smart-Thinking](https://github.com/Leghis/Smart-Thinking)** - ⭐ 31
   Smart-Thinking is a Model Context Protocol (MCP) server that delivers graph-based, multi-step reasoning without relying on external AI APIs. Everything happens locally: similarity search, heuristic-based scoring, verification tracking, memory, and visualization all run in a deterministic pipeline designed for transparency and reproducibility.

2619. **[AlphaFold-MCP-Server](https://github.com/Augmented-Nature/AlphaFold-MCP-Server)** - ⭐ 31
   A comprehensive Model Context Protocol (MCP) server that provides access to the AlphaFold Protein Structure Database through a rich set of tools and resources for protein structure prediction analysis.

2620. **[PRD-MCP-Server](https://github.com/Saml1211/PRD-MCP-Server)** - ⭐ 31
   Flagship Model Context Protocol server for generating Product Requirement Documents (PRDs) from codebase context.

2621. **[dev-kit](https://github.com/nguyenvanduocit/dev-kit)** - ⭐ 31
   [Model Context Protocol] Dev Kit - anything a developer need for him day to day works

2622. **[postmancer](https://github.com/hijaz/postmancer)** - ⭐ 31
   An experimental MCP server Rest Client intended to be a replacement of tools postman & insomnia

2623. **[apisix-mcp](https://github.com/api7/apisix-mcp)** - ⭐ 31
   APISIX Model Context Protocol (MCP) server is used to bridge large language models (LLMs) with the APISIX Admin API.

2624. **[dap_mcp](https://github.com/KashunCheng/dap_mcp)** - ⭐ 31
   Model Context Protocol (MCP) server that interacts with a Debugger

2625. **[chatwork-mcp-server](https://github.com/chatwork/chatwork-mcp-server)** - ⭐ 31
   ChatworkをAIから操作するためのMCP(Model Context Protocol)サーバー

2626. **[zerodha-mcp](https://github.com/mtwn105/zerodha-mcp)** - ⭐ 31
   Zerodha MCP Server & Client - AI Agent (w/Agno & w/Google ADK)

2627. **[mcp-server-fuzzer](https://github.com/Agent-Hellboy/mcp-server-fuzzer)** - ⭐ 31
   A generic mcp server fuzzer

2628. **[machinepal](https://github.com/skalenetwork/machinepal)** - ⭐ 31
   The Cloud-Native MCP and X402 Gateway to Run and Monetize your AI Agents and Services, as well as optimize your AI costs

2629. **[jlcpcb-parts-mcp](https://github.com/nvsofts/jlcpcb-parts-mcp)** - ⭐ 31
   JLCPCB PCBA向けの、部品探しを補助するためのMCPサーバー

2630. **[fastmcp-threatintel](https://github.com/4R9UN/fastmcp-threatintel)** - ⭐ 31
   AI-Powered Threat Intelligence MCP tool

2631. **[unplugin-mcp](https://github.com/situ2001/unplugin-mcp)** - ⭐ 31
   A unified plugin for developers integrating MCP servers into modern JavaScript build tools, including Webpack, Rollup, Vite, and more.

2632. **[mcp-server](https://github.com/HuaweiCloudDeveloper/mcp-server)** - ⭐ 31
   Provide different cloud products  MCP Server tools to  help developers  manage cloud resources  with AI-agent

2633. **[octave-mcp](https://github.com/elevanaltd/octave-mcp)** - ⭐ 31
   OCTAVE protocol - structured AI communication with 3-20x token reduction. MCP server with lenient-to-canonical pipeline and schema validation.

2634. **[ez-mcp](https://github.com/intellectronica/ez-mcp)** - ⭐ 31
   The easiest path to getting an MCP server going

2635. **[mcp-for-security-python](https://github.com/f1tz/mcp-for-security-python)** - ⭐ 31
   一个为主流渗透测试工具打造的MCP服务器集合。 | A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

2636. **[mcp-java-sdk-examples](https://github.com/thought2code/mcp-java-sdk-examples)** - ⭐ 31
   A collection of MCP server examples developed by various Java SDKs

2637. **[bitrise-mcp](https://github.com/bitrise-io/bitrise-mcp)** - ⭐ 31
   MCP Server for the Bitrise API, enabling app management, build operations, artifact management and more.

2638. **[elysia-mcp](https://github.com/kerlos/elysia-mcp)** - ⭐ 31
   ElysiaJS plugin for Model Context Protocol with HTTP transport

2639. **[searxng-mcp](https://github.com/tisDDM/searxng-mcp)** - ⭐ 31
   A Model Context Protocol (MCP) server that enables AI assistants to perform web searches using SearXNG, a privacy-respecting metasearch engine.

2640. **[metabase-mcp](https://github.com/hluaguo/metabase-mcp)** - ⭐ 31
   Metabase MCP server provides integration with the Metabase API, enabling LLM with MCP capabilites to directly interact with your analytics data, this server acts as a bridge between your analytics platform and conversational AI.

2641. **[ESP32MCPServer](https://github.com/navado/ESP32MCPServer)** - ⭐ 31
   Allow AI models connect to ESP32 exposed interfaces. AI generated MCP server for ESP32. 

2642. **[mcp-searxng-enhanced](https://github.com/OvertliDS/mcp-searxng-enhanced)** - ⭐ 31
   Enhanced MCP server for SearXNG: category-aware web-search, web-scraping, and date/time retrieval.

2643. **[AskUserQuestionPlus](https://github.com/JoJoJotarou/AskUserQuestionPlus)** - ⭐ 31
   A MCP server (Streamable HTTP) for asking user questions via a web interface, inspired by the Claude Code AskUserQuestion Tool.

2644. **[mcp-tools](https://github.com/clerk/mcp-tools)** - ⭐ 31
   Tools for building modern & secure MCP integrations across the client and server side

2645. **[gopls-mcp](https://github.com/xieyuschen/gopls-mcp)** - ⭐ 31
   The essential MCP server for Go language development: Exposing compiler-grade semantics to AI Agents and LLM for deterministic code analysis and minimal context pollution.

2646. **[maven-mcp-server](https://github.com/Bigsy/maven-mcp-server)** - ⭐ 31
   An MCP (Model Context Protocol) server that provides tools for checking Maven dependency versions.

2647. **[mcp-client-cli](https://github.com/thedotmack/mcp-client-cli)** - ⭐ 31
   Command-line interface for any Model Context Protocol (MCP) server.

2648. **[mcp-server-weibo](https://github.com/Selenium39/mcp-server-weibo)** - ⭐ 30
   Model Context Protocol服务器，用于抓取微博用户信息、动态和搜索功能

2649. **[mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing)** - ⭐ 30
   A minimal Model Context Protocol 🖥️ server/client🧑‍💻with Azure OpenAI and 🌐 web browser control via Playwright.

2650. **[pan-mcp-relay](https://github.com/PaloAltoNetworks/pan-mcp-relay)** - ⭐ 30
   Palo Alto Networks AI Runtime Security Model Context Protocol (MCP) Relay Server

2651. **[EU_AI_ACT_MCP](https://github.com/SonnyLabs/EU_AI_ACT_MCP)** - ⭐ 30
   EU AI Act MCP (Model Context Protocol) that connects to your AI agents, helping you to comply with the EU AI Act.

2652. **[clap-mcp](https://github.com/gakonst/clap-mcp)** - ⭐ 30
   A Rust framework that bridges clap command-line applications with the Model Context Protocol (MCP)

2653. **[demo-mcp-server-client-implementation](https://github.com/mschwarzmueller/demo-mcp-server-client-implementation)** - ⭐ 30
   A demo implementation of a MCP server (consuming a dummy API) and basic client.

2654. **[mcp-ollama](https://github.com/emgeee/mcp-ollama)** - ⭐ 30
   Query model running with Ollama from within Claude Desktop or other MCP clients

2655. **[mcp-client](https://github.com/edanyal/mcp-client)** - ⭐ 30
   Typescript mcp client library.

2656. **[mcp-inception](https://github.com/tanevanwifferen/mcp-inception)** - ⭐ 30
   Call another MCP client from your MCP client. Offload context windows, delegate tasks, split between models

2657. **[mcp-cyclops](https://github.com/cyclops-ui/mcp-cyclops)** - ⭐ 30
   Model Context Protocol server for Cyclops

2658. **[univer-mcp](https://github.com/dream-num/univer-mcp)** - ⭐ 30
   AI-powered spreadsheet automation through Model Context Protocol (MCP) server for Univer

2659. **[mcp-hacker-news](https://github.com/paabloLC/mcp-hacker-news)** - ⭐ 30
   This MCP server acts as a bridge between the official Hacker News API and AI-powered tools that support the Model Context Protocol, such as Claude and Cursor.

2660. **[mcp-appium-gestures](https://github.com/AppiumTestDistribution/mcp-appium-gestures)** - ⭐ 30
   This is a Model Context Protocol (MCP) server providing resources and tools for Appium mobile gestures using Actions API..

2661. **[AI-Tracker](https://github.com/twwch/AI-Tracker)** - ⭐ 30
   本仓库旨在整理关于大语言模型（LLM）底层逻辑、**上下文工程 (Context Engineering)** 以及 **Model Context Protocol (MCP)** 协议的核心学习资源与实战路径。

2662. **[carrot-ai-pm](https://github.com/talvinder/carrot-ai-pm)** - ⭐ 30
   Carrot auto-writes specs and catches AI code drift. MCP server for Cursor that AST-validates every commit.

2663. **[runjs](https://github.com/CharlieDigital/runjs)** - ⭐ 30
   The only MCP server you need: let your LLM generate and safely execute JavaScript -- including fetch API calls, JSONPath ETL, built-in resiliencey, and secrets management

2664. **[airflow-mcp-server](https://github.com/abhishekbhakat/airflow-mcp-server)** - ⭐ 30
   MCP Server for Apache Airflow

2665. **[kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp)** - ⭐ 30
   A comprehensive Message Control Protocol (MCP) server for Kafka Schema Registry.

2666. **[itential-mcp](https://github.com/itential/itential-mcp)** - ⭐ 30
   🔌 Itential Platform MCP Server

2667. **[phonepi-mcp](https://github.com/priyankark/phonepi-mcp)** - ⭐ 30
   PhonePi MCP enables seamless integration between desktop AI tools and your smartphone, providing 23+ direct actions including SMS messaging, phone calls, contact management, snippet creation and search, clipboard sharing, notifications, battery status checks, and remote device controls.

2668. **[matrix-mcp-server](https://github.com/mjknowles/matrix-mcp-server)** - ⭐ 30
   MCP Server for a Matrix home server integration; chat, manage rooms, etc.

2669. **[mcp-server-weibo](https://github.com/qinyuanpei/mcp-server-weibo)** - ⭐ 30
   基于 Model Context Protocol 的微博数据接口服务器 - 实时获取微博用户信息、动态内容、热搜榜单、粉丝关注数据。支持用户搜索、内容搜索、话题分析，为 AI 应用提供完整的微博数据接入方案。

2670. **[mcp-bash](https://github.com/patrickomatik/mcp-bash)** - ⭐ 30
   A simple model context protocol (MCP) server that allows Claude Desktop or other MCP aware clients to run Bash commands on your local machine.

2671. **[ros-mcp](https://github.com/Yutarop/ros-mcp)** - ⭐ 30
   MCP server for ROS to control robots via topics, services, and actions.

2672. **[datagouv-mcp](https://github.com/datagouv/datagouv-mcp)** - ⭐ 30
   Model Context Protocol (MCP) server that allows AI chatbots to search, explore, and analyze datasets from data.gouv.fr, the French national Open Data platform, directly through conversation.

2673. **[kirby-mcp](https://github.com/bnomei/kirby-mcp)** - ⭐ 30
   CLI-first MCP server for composer-based Kirby CMS projects — inspect blueprints/templates/plugins, interact with a real Kirby runtime, and use a bundled Kirby knowledge base.

2674. **[fal-mcp-server](https://github.com/raveenb/fal-mcp-server)** - ⭐ 30
   MCP server for Fal.ai - Generate images, videos, music and audio with Claude

2675. **[puppeteer-mcp-claude](https://github.com/jaenster/puppeteer-mcp-claude)** - ⭐ 30
   A Model Context Protocol (MCP) server that provides Claude Code with comprehensive browser automation capabilities through Puppeteer

2676. **[openzim-mcp](https://github.com/cameronrye/openzim-mcp)** - ⭐ 30
   OpenZIM MCP is a modern, secure, and high-performance MCP (Model Context Protocol) server that enables AI models to access and search ZIM format knowledge bases offline.

2677. **[MCP-Server-Starter](https://github.com/TheSethRose/MCP-Server-Starter)** - ⭐ 29
   A Model Context Protocol server starter template

2678. **[mcp-server-dumplingai](https://github.com/DumplingAI/mcp-server-dumplingai)** - ⭐ 29
   MCP (Model Context Protocol) server for Dumpling AI

2679. **[mcp-badges](https://github.com/mcpx-dev/mcp-badges)** - ⭐ 29
   Get your projects MCP (Model Context Protocol)  badges

2680. **[mcp-attr](https://github.com/frozenlib/mcp-attr)** - ⭐ 29
   A library for declaratively building Model Context Protocol servers.

2681. **[rails-pg-extras-mcp](https://github.com/pawurb/rails-pg-extras-mcp)** - ⭐ 29
   MCP (Model Context Protocol) LLM interface for rails-pg-extras gem

2682. **[browserai-mcp](https://github.com/brightdata/browserai-mcp)** - ⭐ 29
   A powerful Model Context Protocol (MCP) server that provides an access to serverless browser for AI agents and apps

2683. **[luke-desktop](https://github.com/DrJonBrock/luke-desktop)** - ⭐ 29
   A modern desktop client for Claude AI with MCP server support, built with Tauri, React, and TypeScript.

2684. **[xmind-generator-mcp](https://github.com/BangyiZhang/xmind-generator-mcp)** - ⭐ 29
   An MCP (Model Context Protocol) server for generating Xmind mind maps. This server allows LLMs to create structured mind maps through the MCP protocol.

2685. **[actor-critic-thinking-mcp](https://github.com/aquarius-wing/actor-critic-thinking-mcp)** - ⭐ 29
   A dual-perspective thinking analysis server based on Model Context Protocol (MCP), providing comprehensive performance evaluation through Actor-Critic methodology.

2686. **[rod-mcp](https://github.com/go-rod/rod-mcp)** - ⭐ 29
   Model Context Protocol Server of Rod

2687. **[NetContextServer](https://github.com/willibrandon/NetContextServer)** - ⭐ 29
   A .NET implementation of the Model Context Protocol enabling AI assistants to explore and understand .NET codebases.

2688. **[openai-mcp-agent-dotnet](https://github.com/Azure-Samples/openai-mcp-agent-dotnet)** - ⭐ 29
   Sample to create an AI Agent using OpenAI models with any MCP server running on Azure Container Apps

2689. **[dockashell](https://github.com/anzax/dockashell)** - ⭐ 29
   DockaShell is an MCP server that gives AI agents isolated Docker containers to work in. MCP tools for shell access, file operations, and full audit trail.

2690. **[mcp](https://github.com/fastly/mcp)** - ⭐ 29
   Model Context Protocol (MCP) server for AI-powered Fastly CDN management.

2691. **[email-mcp](https://github.com/TimeCyber/email-mcp)** - ⭐ 29
   一个让AI轻松接管邮箱的MCP服务，基于 Model Context Protocol (MCP) 构建，支持在 MCP-X,Claude Desktop 等 MCP 客户端中使用。

2692. **[paraview_mcp](https://github.com/llnl/paraview_mcp)** - ⭐ 29
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

2693. **[mattermost-mcp-host](https://github.com/jagan-shanmugam/mattermost-mcp-host)** - ⭐ 29
   A Mattermost integration that connects to Model Context Protocol (MCP) servers, leveraging a LangGraph-based Agent.

2694. **[biothings-mcp](https://github.com/longevity-genie/biothings-mcp)** - ⭐ 29
   MCP (Model Context Protocol) server for biothings

2695. **[levante](https://github.com/levante-hub/levante)** - ⭐ 29
   Levante - Personal, Secure, Free, Local AI, MCP Client

2696. **[gatekit](https://github.com/gatekit-ai/gatekit)** - ⭐ 29
   A hackable Model Context Protocol (MCP) gateway

2697. **[chrome-extension-bridge-mcp](https://github.com/Oanakiaja/chrome-extension-bridge-mcp)** - ⭐ 29
   A chrome extension bridge that allows you to connect to a mcp server to use global window object.

2698. **[telegram-mcp-server](https://github.com/kfastov/telegram-mcp-server)** - ⭐ 29
   MCP server implementation for Telegram

2699. **[agent-pm](https://github.com/gannonh/agent-pm)** - ⭐ 29
   MCP server for the planning and execution of AI-assisted development projects.

2700. **[pfsense-mcp-server](https://github.com/gensecaihq/pfsense-mcp-server)** - ⭐ 29
   pfSense MCP Server enables security administrators to manage their pfSense firewalls using natural language through AI assistants like Claude Desktop. Simply ask "Show me blocked IPs" or "Run a PCI compliance check" instead of navigating complex interfaces. Supports REST/XML-RPC/SSH connections, and includes built-in complian

2701. **[mcp-notify](https://github.com/aahl/mcp-notify)** - ⭐ 29
   💬  MCP Server for notify to Weixin, Telegram, Bark, Lark, 飞书, 钉钉

2702. **[rdkit-mcp-server](https://github.com/tandemai-inc/rdkit-mcp-server)** - ⭐ 29
   MCP server that enables language models to interact with RDKit through natural language

2703. **[protonmail-mcp](https://github.com/amotivv/protonmail-mcp)** - ⭐ 29
   This MCP server provides email sending functionality using Protonmail's SMTP service. It allows both Claude Desktop and Cline VSCode extension to send emails on your behalf using your Protonmail credentials.

2704. **[ida-headless-mcp](https://github.com/zboralski/ida-headless-mcp)** - ⭐ 29
   Headless IDA Pro binary analysis via Model Context Protocol

2705. **[robinhood-mcp-server](https://github.com/rohitsingh-iitd/robinhood-mcp-server)** - ⭐ 29
   The Robinhood MCP Server provides a comprehensive interface to the Robinhood Crypto API. This server handles authentication, account management, market data retrieval, and trading operations through both REST API and WebSocket interfaces.

2706. **[WebSearch-MCP](https://github.com/mnhlt/WebSearch-MCP)** - ⭐ 29
   [Self-hosted] A Model Context Protocol (MCP) server implementation that provides a web search capability over stdio transport. This server integrates with a WebSearch Crawler API to retrieve search results.

2707. **[cca-mcp-configurator](https://github.com/doggy8088/cca-mcp-configurator)** - ⭐ 29
   一個簡單易用的網頁工具，用於管理 GitHub Copilot 的 MCP (Model Context Protocol) 設定

2708. **[alibabacloud-dms-mcp-server](https://github.com/aliyun/alibabacloud-dms-mcp-server)** - ⭐ 29
   A universal multi-cloud data MCP Server supporting over 40 types of data source connections, providing secure, unified data access in a single platform. Supports full range of Alibaba Cloud services and Mainstream databases/data warehouses.

2709. **[prediction-market-mcp](https://github.com/JamesANZ/prediction-market-mcp)** - ⭐ 29
   A simple MCP server that grabs prediction market data from polymarket, PredictIt, & Kalshi. 

2710. **[turbovault](https://github.com/Epistates/turbovault)** - ⭐ 29
   MCP server that transforms your Obsidian vault into an intelligent knowledge system

2711. **[tgcli](https://github.com/kfastov/tgcli)** - ⭐ 29
   Telegram user console client and archiver

2712. **[workflowy](https://github.com/mholzen/workflowy)** - ⭐ 29
   Powerful CLI and MCP server for WorkFlowy: reports, search/replace, backup support, and AI integration (Claude, LLMs)

2713. **[google-drive-mcp](https://github.com/piotr-agier/google-drive-mcp)** - ⭐ 29
   A Model Context Protocol (MCP) server that provides secure integration with Google Drive, Docs, Sheets, and Slides. It allows Claude Desktop and other MCP clients to manage files in Google Drive through a standardized interface.

2714. **[framer-plugin-mcp](https://github.com/Sheshiyer/framer-plugin-mcp)** - ⭐ 29
   A Model Context Protocol (MCP) server for creating and managing Framer plugins with web3 capabilities

2715. **[crawl4ai-mcp-server](https://github.com/sadiuysal/crawl4ai-mcp-server)** - ⭐ 29
   🕷️ A lightweight Model Context Protocol (MCP) server that exposes Crawl4AI web scraping and crawling capabilities as tools for AI agents.  Similar to Firecrawl's API but self-hosted and free. Perfect for integrating web scraping into your AI workflows with OpenAI Agents SDK, Cursor, Claude Code, and other MCP-compatible tools.

2716. **[Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server)** - ⭐ 28
   A Model Context Protocol (MCP) server that integrates Volatility 3 memory forensics framework with Claude

2717. **[sketchfab-mcp-server](https://github.com/gregkop/sketchfab-mcp-server)** - ⭐ 28
   This is an MCP (Model Context Protocol) Server for discovering and downloading 3D models 

2718. **[mcp-testing-framework](https://github.com/L-Qun/mcp-testing-framework)** - ⭐ 28
   Testing framework for Model Context Protocol (MCP)

2719. **[laravel-mcp-sdk](https://github.com/mohamedahmed01/laravel-mcp-sdk)** - ⭐ 28
   Laravel Based Implementation for Model Context Protocol

2720. **[mcp-websocket](https://github.com/virajsharma2000/mcp-websocket)** - ⭐ 28
   This server implements an MCP (Model Context Protocol) server with WebSocket enhancements for real-time data updates.

2721. **[mcp_autogen_sse_stdio](https://github.com/SaM-92/mcp_autogen_sse_stdio)** - ⭐ 28
   This repository demonstrates how to use AutoGen to integrate local and remote MCP (Model Context Protocol) servers. It showcases a local math tool (math_server.py) using Stdio and a remote Apify tool (RAG Web Browser Actor) via SSE for tasks like arithmetic and web browsing.

2722. **[nchan-mcp-transport](https://github.com/ConechoAI/nchan-mcp-transport)** - ⭐ 28
   The best way to deploy mcp server. A high-performance WebSocket/SSE transport layer & gateway for Anthropic's MCP (Model Context Protocol) — powered by Nginx, Nchan, and FastAPI.

2723. **[TAM-MCP-Server](https://github.com/gvaibhav/TAM-MCP-Server)** - ⭐ 28
   A comprehensive Model Context Protocol (MCP) server for market sizing analysis, TAM/SAM calculations, and industry research. Built with TypeScript, Express.js, and following the MCP  specification.

2724. **[mcp-etherscan-server](https://github.com/crazyrabbitLTC/mcp-etherscan-server)** - ⭐ 28
   An MCP (Model Context Protocol) server that provides Ethereum blockchain data tools via Etherscan's API. Features include checking ETH balances, viewing transaction history, tracking ERC20 transfers, fetching contract ABIs, monitoring gas prices, and resolving ENS names.

2725. **[vsc-mcp](https://github.com/thomasgazzoni/vsc-mcp)** - ⭐ 28
   This project provides tools that expose Language Server Protocol (LSP) functionality as MCP (Model Context Protocol) tools

2726. **[asterisk-mcp-server](https://github.com/winfunc/asterisk-mcp-server)** - ⭐ 28
   Asterisk Model Context Protocol (MCP) server.

2727. **[notion-mcp](https://github.com/Badhansen/notion-mcp)** - ⭐ 28
   A simple Model Context Protocol (MCP) server that integrates with Notion's API to manage my personal todo list.

2728. **[YFinance-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop)** - ⭐ 28
   An MCP (Model Context Protocol) tool that provides stock market data and trading capabilities using the yfinance library, specifically adapted for Claude Desktop.

2729. **[UnrealMCPBridge](https://github.com/appleweed/UnrealMCPBridge)** - ⭐ 28
   An Unreal Engine plugin that implements an MCP server allowing MCP clients to access the UE Editor Python API.

2730. **[openapi-mcp-generator](https://github.com/abutbul/openapi-mcp-generator)** - ⭐ 28
   A Python tool that automatically converts OpenAPI(Swagger, ETAPI) compatible specifications into fully functional Model Context Protocol (MCP) servers. Generates Docker-ready implementations with support for SSE/IO communication protocols, authentication, and comprehensive error handling. https://pypi.org/project/openapi-mcp-generator/

2731. **[workflows-mcp-server](https://github.com/cyanheads/workflows-mcp-server)** - ⭐ 28
   Model Context Protocol server that enables AI agents to discover, create, and execute complex, multi-step workflows defined in simple YAML files. Allow your AI agents to better organize their tool usage and provide a more structured way to handle complex multi-step tasks.

2732. **[mcp-proxy](https://github.com/stephenlacy/mcp-proxy)** - ⭐ 28
   Fast rust MCP proxy between stdio and SSE

2733. **[claude-code-mcp](https://github.com/zebbern/claude-code-mcp)** - ⭐ 28
   Model Context Protocol (MCP) servers with Claude Code. These tools dramatically enhance Claude Code's capabilities, allowing it to interact with your filesystem, web browsers, and more.

2734. **[taskflow-mcp](https://github.com/pinkpixel-dev/taskflow-mcp)** - ⭐ 28
   A task management Model Context Protocol (MCP) server that helps AI assistants break down user requests into manageable tasks with subtasks, dependencies, and notes. Enforces a structured workflow with user approval steps.

2735. **[gemsuite-mcp](https://github.com/PV-Bhat/gemsuite-mcp)** - ⭐ 28
   Professional Gemini API integration for Claude and all MCP-compatible hosts with intelligent model selection and advanced file handling | Smithery.ai verified

2736. **[kaggle-mcp](https://github.com/54yyyu/kaggle-mcp)** - ⭐ 28
   Kaggle-MCP: Connect Claude AI to the Kaggle API through the Model Context Protocol (MCP), enabling competition, dataset, and kernel operations through the AI interface.

2737. **[google-search-console-mcp-server](https://github.com/Shin-sibainu/google-search-console-mcp-server)** - ⭐ 28
   Model Context Protocol server for Google Search Console API - integrate with Claude Code and Claude Desktop

2738. **[excel-reader-mcp](https://github.com/ArchimedesCrypto/excel-reader-mcp)** - ⭐ 28
   A Model Context Protocol (MCP) server for reading Excel files with automatic chunking and pagination support. Built with SheetJS and TypeScript.

2739. **[gaia-x](https://github.com/YFGaia/gaia-x)** - ⭐ 28
   Gaia-X 基于AI新范式的下一代企业级AI应用平台。Gaia-X旨在实现类人脑的、针对企业办公业务场景的AI化赋能，包括一系列新颖而稳定的企业级AI功能，包括不限于：企业级管理功能、MCP Server支持（且支持将企业内部系统API转换为MCP Server提供服务）、支持自然语言驱动的RPA（大模型操作电脑）、划词分析和悬浮球等。

2740. **[ddg_search](https://github.com/OEvortex/ddg_search)** - ⭐ 28
   A powerful Model Context Protocol (MCP) server for web search and URL content extraction using DuckDuckGo.

2741. **[tempo-mcp-server](https://github.com/ivelin-web/tempo-mcp-server)** - ⭐ 28
   MCP server for managing Tempo worklogs in Jira

2742. **[Amazing-Marvin-MCP](https://github.com/bgheneti/Amazing-Marvin-MCP)** - ⭐ 28
   Model Context Provider for Amazing Marvin productivity app - Access your tasks, projects, and categories in AI assistants

2743. **[mcp-server](https://github.com/blockscout/mcp-server)** - ⭐ 28
   Wraps Blockscout APIs and exposes blockchain data by Model Context Protocol

2744. **[freepik-mcp](https://github.com/freepik-company/freepik-mcp)** - ⭐ 28
   The Freepik enables popular agent Model Context Protocol (MCP) to integrate with Freepik APIs through function calling.

2745. **[browser-use-rs](https://github.com/BB-fat/browser-use-rs)** - ⭐ 28
   A Rust library for browser automation via Chrome DevTools Protocol with built-in AI integration through Model Context Protocol (MCP)

2746. **[mcp-ollama-agent](https://github.com/ausboss/mcp-ollama-agent)** - ⭐ 27
   A TypeScript example showcasing the integration of Ollama with the Model Context Protocol (MCP) servers. This project provides an interactive command-line interface for an AI agent that can utilize the tools from multiple MCP Servers..

2747. **[Memgpt-MCP-Server](https://github.com/Vic563/Memgpt-MCP-Server)** - ⭐ 27
   A Model Context Protocol (MCP) server that provides persistent memory and multi-model LLM support.

2748. **[aws-mcp](https://github.com/lokeswaran-aj/aws-mcp)** - ⭐ 27
   An MCP(Model Context Protocol) Server for AWS services

2749. **[mcpc](https://github.com/apify/mcpc)** - ⭐ 27
   Universal command-line client for the Model Context Protocol (MCP)

2750. **[VercelGenUI_MCP](https://github.com/JamesSloan/VercelGenUI_MCP)** - ⭐ 27
   Proof of concept chat AI combining the Model Context Protocol (MCP) with Vercel's AI SDK UI

2751. **[postgres-mcp-server](https://github.com/ahmedmustahid/postgres-mcp-server)** - ⭐ 27
   MCP (Model Context Protocol) Server for postgres Database

2752. **[mcp](https://github.com/supadata-ai/mcp)** - ⭐ 27
   Official Supadata MCP Server - Adds powerful video & web scraping to Cursor, Claude and any other LLM clients.

2753. **[google-workspace-mcp-server](https://github.com/epaproditus/google-workspace-mcp-server)** - ⭐ 27
   A Model Context Protocol server for Google Workspace integration (Gmail and Calendar)

2754. **[nettune](https://github.com/jtsang4/nettune)** - ⭐ 27
   A network diagnostics and TCP optimization tool with MCP (Model Context Protocol) integration for AI-assisted configuration.

2755. **[mcp-web-browser](https://github.com/random-robbie/mcp-web-browser)** - ⭐ 27
   An advanced web browsing server for the Model Context Protocol (MCP) powered by Playwright, enabling headless browser interactions through a flexible, secure API.

2756. **[directus-mcp-server](https://github.com/rijkvanzanten/directus-mcp-server)** - ⭐ 27
   Model Context Protocol server for Directus

2757. **[Python-Runtime-Interpreter-MCP-Server](https://github.com/hileamlakB/Python-Runtime-Interpreter-MCP-Server)** - ⭐ 27
   PRIMS is a lightweight, open-source Model Context Protocol (MCP) server that lets LLM agents safely execute arbitrary Python code in a secure, throw-away sandbox.

2758. **[seo-insights-mcp-server](https://github.com/mrgoonie/seo-insights-mcp-server)** - ⭐ 27
   TypeScript Model Context Protocol (MCP) server for SEO Insights. Provides SEO tools for backlinks, keyword research, and traffic analysis. Includes CLI support and extensible structure for connecting AI systems (LLMs) to SEO APIs

2759. **[mcp_espn_ff](https://github.com/KBThree13/mcp_espn_ff)** - ⭐ 27
   ESPN Fantasy API with LLMs!

2760. **[nimbletools-core](https://github.com/NimbleBrainInc/nimbletools-core)** - ⭐ 27
   NimbleTools is an open-source MCP runtime. Infrastructure for the agentic web.

2761. **[deno-mcp-template](https://github.com/phughesmcr/deno-mcp-template)** - ⭐ 27
   A template repo for writing and publishing local, remote, DXT, and binary MCP servers using Deno.

2762. **[mcp-stytch-consumer-todo-list](https://github.com/stytchauth/mcp-stytch-consumer-todo-list)** - ⭐ 27
   Workers + Stytch TODO App MCP Server

2763. **[mindbridge-mcp](https://github.com/pinkpixel-dev/mindbridge-mcp)** - ⭐ 27
   MindBridge is an AI orchestration MCP server that lets any app talk to any LLM — OpenAI, Anthropic, DeepSeek, Ollama, and more — through a single unified API. Route queries, compare models, get second opinions, and build smarter multi-LLM workflows.

2764. **[php-mcp](https://github.com/dtyq/php-mcp)** - ⭐ 27
   A complete PHP implementation of the Model Context Protocol (MCP) with server and client support, STDIO and HTTP transports, and framework integration

2765. **[src-to-kb](https://github.com/vezlo/src-to-kb)** - ⭐ 27
   Convert source code to LLM ready knowledge base

2766. **[Healthcare-MCP](https://github.com/innovaccer/Healthcare-MCP)** - ⭐ 27
   Specification and documentation for the Healthcare Model Context Protocol. This builds on top of the base Model Context Protocol

2767. **[MCP-BOE](https://github.com/ComputingVictor/MCP-BOE)** - ⭐ 27
   MCP server para el BOE 🇪🇸 — Acceso a legislación consolidada, sumarios diarios y tablas oficiales del Boletín Oficial del Estado mediante Model Context Protocol y API REST.

2768. **[MCPSecBench](https://github.com/AIS2Lab/MCPSecBench)** - ⭐ 27
   MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols

2769. **[cml-mcp](https://github.com/xorrkaz/cml-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) Server for Cisco Modeling Labs (CML)

2770. **[mcp-log-proxy](https://github.com/emicklei/mcp-log-proxy)** - ⭐ 27
   a web logging proxy for MCP client-server communication

2771. **[mcp-writer-substack](https://github.com/jonathan-politzki/mcp-writer-substack)** - ⭐ 27
   Model Context Protocol to bridge in Substack writings to Claude.

2772. **[mcp-local-dev](https://github.com/txbm/mcp-local-dev)** - ⭐ 27
   Let LLMs manage your local dev environments

2773. **[alibabacloud-dataworks-mcp-server](https://github.com/aliyun/alibabacloud-dataworks-mcp-server)** - ⭐ 27
   A Model Context Protocol (MCP) server that provides tools for AI, allowing it to interact with the DataWorks Open API through a standardized interface. This implementation is based on the Aliyun Open API and enables AI agents to perform cloud resources operations seamlessly.

2774. **[mcp-server-giphy](https://github.com/magarcia/mcp-server-giphy)** - ⭐ 27
   An implementation of Giphy integration with Model Context Protocol

2775. **[ai-foundry-agents-samples](https://github.com/Azure-Samples/ai-foundry-agents-samples)** - ⭐ 27
   Azure AI Foundry - Agents related sample code

2776. **[RoslynMCP](https://github.com/carquiza/RoslynMCP)** - ⭐ 27
   A Model Context Protocol (MCP) server that provides C# code analysis capabilities using Microsoft Roslyn

2777. **[bear-notes-mcp](https://github.com/bejaminjones/bear-notes-mcp)** - ⭐ 27
   MCP server for Bear app - Full Read + Write AI-powered note management with Claude Desktop

2778. **[powerplatform-mcp](https://github.com/michsob/powerplatform-mcp)** - ⭐ 27
   PowerPlatform Model Context Protocol server

2779. **[minimax_search](https://github.com/MiniMax-AI/minimax_search)** - ⭐ 27
   MiniMax Search is an MCP (Model Context Protocol) server that provides web search and browsing capabilities.

2780. **[mcp-probe-kit](https://github.com/mybolide/mcp-probe-kit)** - ⭐ 27
   一个强大的 MCP (Model Context Protocol) 服务器，提20个实用工具，覆盖代码质量、开发效率、项目管理、生成skills文档全流程。

2781. **[mcp-structured-thinking](https://github.com/Promptly-Technologies-LLC/mcp-structured-thinking)** - ⭐ 26
   A TypeScript Model Context Protocol (MCP) server to allow LLMs to programmatically construct mind maps to explore an idea space, with enforced "metacognitive" self-reflection

2782. **[touchdesigner-mcp-server](https://github.com/bottobot/touchdesigner-mcp-server)** - ⭐ 26
   TouchDesigner Documentation MCP Server v2.6.1 - FIXED Python API tools! Features 629 operators + 14 tutorials + 69 Python API classes with working get_python_api & search_python_api tools. Zero-configuration setup for VS Code/Codium.

2783. **[mcp-frontend-testing](https://github.com/StudentOfJS/mcp-frontend-testing)** - ⭐ 26
   Frontend testing tools for Model Context Protocol

2784. **[do-remote-mcp-server-template](https://github.com/do-community/do-remote-mcp-server-template)** - ⭐ 26
   A Model Context Protocol (MCP) server that checks domain name availability using WHOIS lookups and DNS resolution

2785. **[pptx-xlsx-mcp](https://github.com/jenstangen1/pptx-xlsx-mcp)** - ⭐ 26
   Antrophics Model context protocol to edit powerpoint files

2786. **[minds-mcp](https://github.com/mindsdb/minds-mcp)** - ⭐ 26
   An MCP (Model Context Protocol) server for Minds, allowing LLMs to interact with the Minds SDK through a standardized interface.

2787. **[mcp-client-x](https://github.com/RGGH/mcp-client-x)** - ⭐ 26
   Python MCP client + server example

2788. **[mcp-gateway](https://github.com/lucky-aeon/mcp-gateway)** - ⭐ 26
   The MCP gateway is a reverse proxy server that forwards requests from clients to the MCP server or uses all MCP servers under the gateway through a unified portal.

2789. **[langchain-mcp-tools-py](https://github.com/hideya/langchain-mcp-tools-py)** - ⭐ 26
   MCP to LangChain Tools Conversion Utility / Python

2790. **[MalwareBazaar_MCP](https://github.com/mytechnotalent/MalwareBazaar_MCP)** - ⭐ 26
   An AI-driven MCP server that autonomously interfaces with Malware Bazaar, delivering real-time threat intel and sample metadata for authorized cybersecurity research workflows.

2791. **[omop_mcp](https://github.com/OHNLP/omop_mcp)** - ⭐ 26
   Model Context Protocol (MCP) server for mapping clinical terminology to Observational Medical Outcomes Partnership (OMOP) concepts using Large Language Models

2792. **[ton-blockchain-mcp](https://github.com/devonmojito/ton-blockchain-mcp)** - ⭐ 26
   A Model Context Protocol (MCP) server written in Python for natural language interaction with the TON blockchain 💎

2793. **[mcpmcp-server](https://github.com/glenngillen/mcpmcp-server)** - ⭐ 26
   Discover, setup, and integrate MCP servers with your favorite clients. Unlock the full potential of AI in your daily workflow.

2794. **[whistle-mcp](https://github.com/7gugu/whistle-mcp)** - ⭐ 26
   A Whistle proxy management tool based on Model Context Protocol that allows AI assistants to directly control local Whistle proxy servers, simplifying network debugging, API testing, and proxy rule configuration through natural language interaction.

2795. **[MCPServer](https://github.com/rhennigan/MCPServer)** - ⭐ 26
   Implements a model context protocol server using Wolfram Language

2796. **[nebulagraph-mcp-server](https://github.com/nebula-contrib/nebulagraph-mcp-server)** - ⭐ 26
   Model Context Protocol Server for NebulaGraph 3.x

2797. **[taiwan-holiday-mcp](https://github.com/lis186/taiwan-holiday-mcp)** - ⭐ 26
   一個基於 Model Context Protocol (MCP) 的台灣假期查詢伺服器，為 AI 工具提供準確的台灣國定假日資訊。

2798. **[MCP-Developer-SubAgent](https://github.com/gensecaihq/MCP-Developer-SubAgent)** - ⭐ 26
    A specialized framework for Model Context Protocol (MCP) development featuring 8   Claude Code sub-agents, security hooks, and production-ready FastMCP server   templates. Provides immediate MCP development assistance through markdown-driven   agents with optional programmatic SDK .

2799. **[enhanced-mcp-memory](https://github.com/cbunting99/enhanced-mcp-memory)** - ⭐ 26
   An enhanced MCP (Model Context Protocol) server for intelligent memory and task management, designed for AI assistants and development workflows. Features semantic search, automatic task extraction, knowledge graphs, and comprehensive project management.

2800. **[mcp-auth](https://github.com/famma-ai/mcp-auth)** - ⭐ 26
   MCP Auth via Reverse Proxy 

2801. **[mcp-caiyun-weather](https://github.com/caiyunapp/mcp-caiyun-weather)** - ⭐ 26
   A Model Context Protocol (MCP) server for Caiyun (ColorfulClouds) Weather.

2802. **[laravel-mcp-companion](https://github.com/brianirish/laravel-mcp-companion)** - ⭐ 26
   A Laravel developer's MCP companion. Get the absolute best advice, recommendations, and up-to-date documentation for the entire Laravel ecosystem.

2803. **[mcp-simple-timeserver](https://github.com/andybrandt/mcp-simple-timeserver)** - ⭐ 26
   Simple solution to give Claude ability to check current time via MCP

2804. **[bgg-mcp](https://github.com/kkjdaniel/bgg-mcp)** - ⭐ 26
   BGG MCP provides access to BoardGameGeek and a variety of board game related data through the Model Context Protocol. Enabling retrieval and filtering of board game data, user collections, and profiles.

2805. **[native-devtools-mcp](https://github.com/sh3ll3x3c/native-devtools-mcp)** - ⭐ 26
   Model Context Protocol server for native app testing 

2806. **[mcp-chain-of-draft-server](https://github.com/bsmi021/mcp-chain-of-draft-server)** - ⭐ 25
   Chain of Draft Server is a powerful AI-driven tool that helps developers make better decisions through systematic, iterative refinement of thoughts and designs. It integrates seamlessly with popular AI agents and provides a structured approach to reasoning, API design, architecture decisions, code reviews, and implementation planning.

2807. **[alpaca-mcp-server](https://github.com/tedlikeskix/alpaca-mcp-server)** - ⭐ 25
   Model Context Protocol (MCP) server for Alpaca trading API

2808. **[gyazo-mcp-server](https://github.com/nota/gyazo-mcp-server)** - ⭐ 25
   Official Model Context Protocol server for Gyazo

2809. **[mcp-php](https://github.com/garyblankenship/mcp-php)** - ⭐ 25
   model context protocol or mcp for php laravel

2810. **[mcp-media-processor](https://github.com/maoxiaoke/mcp-media-processor)** - ⭐ 25
   A Node.js server implementing Model Context Protocol (MCP) for media processing operations, providing powerful video and image manipulation capabilities.

2811. **[mcp-webdriveragent](https://github.com/AppiumTestDistribution/mcp-webdriveragent)** - ⭐ 25
   This is a Model Context Protocol (MCP) server that provides tools for building and signing WebDriverAgent for iOS.

2812. **[turn-based-game-mcp](https://github.com/github-samples/turn-based-game-mcp)** - ⭐ 25
   A turn-based games app built with Next.js and TypeScript that features Tic-Tac-Toe and Rock Paper Scissors games with AI opponents powered by the Model Context Protocol (MCP), offering three difficulty levels.

2813. **[mcp-manager](https://github.com/nstebbins/mcp-manager)** - ⭐ 25
   CLI tool for managing Model Context Protocol (MCP) servers in one place & using them across them different clients

2814. **[php-mcp-sdk](https://github.com/dalehurley/php-mcp-sdk)** - ⭐ 25
   PHP implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.  ✨ Features  🚀 Complete MCP Protocol Support - Full implementation of the MCP specification 🔧 Type-Safe - Leverages PHP 8.1+ type system with enums, union types, and strict typing ⚡ Async First

2815. **[symfony-mcp-server](https://github.com/klapaudius/symfony-mcp-server)** - ⭐ 25
   A Symfony package designed for building secure servers based on the Model Context Protocol, utilizing Server-Sent Events (SSE) and/or StreamableHTTP for real-time communication. It offers a scalable tool system tailored for enterprise-grade applications.

2816. **[FalkorDB-MCPServer](https://github.com/FalkorDB/FalkorDB-MCPServer)** - ⭐ 25
   FalkorDB-MCPServer is an MCP (Model Context Protocol) server that connects LLMs to FalkorDB

2817. **[mcp-server-semgrep](https://github.com/VetCoders/mcp-server-semgrep)** - ⭐ 25
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

2818. **[deep-research-mcp](https://github.com/pinkpixel-dev/deep-research-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) compliant server designed for comprehensive web research. It uses Tavily's Search and Crawl APIs to gather detailed information on a given topic, then structures this data in a format perfect for LLMs to create high-quality markdown documents.

2819. **[puzzlebox](https://github.com/cliffhall/puzzlebox)** - ⭐ 25
   An MCP server that hosts finite state machines as dynamic resources that multiple clients can subscribe to and be updated when their state changes.

2820. **[Tiny-OAI-MCP-Agent](https://github.com/jalr4ever/Tiny-OAI-MCP-Agent)** - ⭐ 25
   A MCP protocol agent that operates a SQLite using natural language by OpenAI-Compatible LLM.

2821. **[slack-mcp-server](https://github.com/AVIMBU/slack-mcp-server)** - ⭐ 25
   A Model Context Protocol Server for Interacting with Slack

2822. **[vision-one-mcp-server](https://github.com/trendmicro/vision-one-mcp-server)** - ⭐ 25
   The Trend Vision One Model Context Protocol (MCP) Server enables natural language interaction between your favourite AI tooling and the Trend Vision One web APIs.  This allows users to harness the power of Large Language Models (LLM) to interpret and respond to security events.

2823. **[zillow-mcp-server](https://github.com/sap156/zillow-mcp-server)** - ⭐ 25
   Zillow MCP Server for real estate data access via the Model Context Protocol

2824. **[systemprompt-mcp-notion](https://github.com/Ejb503/systemprompt-mcp-notion)** - ⭐ 25
   This an Model Context Protocol (MCP) server that integrates Notion into your AI workflows. This server enables seamless access to Notion through MCP, allowing AI agents to interact with pages, databases, and comments.

2825. **[mcp-config-manager](https://github.com/holstein13/mcp-config-manager)** - ⭐ 25
   Manage MCP server configs across Claude, Gemini & other AI systems. Interactive CLI for server enable/disable, preset management & config sync.

2826. **[kernel-mcp-server](https://github.com/kernel/kernel-mcp-server)** - ⭐ 25
   Open-source MCP server for secure, low-latency cloud-browser automation on Kernel.

2827. **[FerrumMCP](https://github.com/Eth3rnit3/FerrumMCP)** - ⭐ 25
   A Model Context Protocol (MCP) server that provides web automation capabilities through Ferrum, with optional BotBrowser integration for advanced anti-detection features. This enables AI agents to interact with web pages seamlessly.

2828. **[mcp_rss](https://github.com/buhe/mcp_rss)** - ⭐ 25
   MCP RSS is a Model Context Protocol (MCP) server for interacting with RSS feeds.

2829. **[agent-hub-mcp](https://github.com/gilbarbara/agent-hub-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server that enables communication and coordination between multiple AI agents

2830. **[clay-mcp](https://github.com/clay-inc/clay-mcp)** - ⭐ 25
   A simple Model Context Protocol (MCP) server for Clay.

2831. **[meeting-mcp](https://github.com/Meeting-BaaS/meeting-mcp)** - ⭐ 25
   Model Context Protocol server for AI assistants to create meeting bots, search transcripts, and manage meeting recordings.

2832. **[mcp_streamable_http](https://github.com/theailanguage/mcp_streamable_http)** - ⭐ 25
   Educational repo for MCP streamable HTTP servers and clients

2833. **[pulse-editor](https://github.com/ClayPulse/pulse-editor)** - ⭐ 25
   Vibe code on any device, and scale your apps with visual workflows. Pulse Editor is a modular, cross-platform, AI-powered productivity platform with federated app collaboration and extensible workflows. 

2834. **[semrush-mcp](https://github.com/mrkooblu/semrush-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server implementation that provides tools for accessing Semrush API data.

2835. **[ccmcp](https://github.com/gsong/ccmcp)** - ⭐ 25
   A CLI tool that intelligently discovers, validates, and selects MCP (Model Context Protocol) server configurations for Claude Code.

2836. **[awesome-mcp-lists](https://github.com/collabnix/awesome-mcp-lists)** - ⭐ 25
   A Curated List of MCP Servers, Clients and Toolkits

2837. **[metals-standalone-client](https://github.com/jpablo/metals-standalone-client)** - ⭐ 25
   Minimal Metals stand alone client that allows running the metals mcp server

2838. **[mcp-slicer](https://github.com/zhaoyouj/mcp-slicer)** - ⭐ 25
   A Model Context Protocol server for 3D Slicer integration

2839. **[powerpoint-mcp](https://github.com/Ayushmaniar/powerpoint-mcp)** - ⭐ 25
   Open Source Model Context Protocol server for PowerPoint automation on Windows via pywin32

2840. **[chatbot_Shopify](https://github.com/Mobeen-Dev/chatbot_Shopify)** - ⭐ 25
   Agentic Shopify Chatbot with MCP integration, embedded directly into Shopify via a Theme Extension

2841. **[mcp-server-excel](https://github.com/sbroenne/mcp-server-excel)** - ⭐ 25
   Excel MCP Server & CLI - 22 tools, 211 operations for AI-powered Excel automation via COM API

2842. **[nestjs-mcp](https://github.com/bamada/nestjs-mcp)** - ⭐ 25
   NestJS module for seamless Model Context Protocol (MCP) server integration using decorators.

2843. **[prometheus-mcp](https://github.com/idanfishman/prometheus-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server implementation that provides AI agents with programmatic access to Prometheus metrics via a unified interface.

2844. **[greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server)** - ⭐ 25
   A Model Context Protocol (MCP) server for GreptimeDB

2845. **[codesys-mcp-toolkit](https://github.com/johannesPettersson80/codesys-mcp-toolkit)** - ⭐ 25
   Model Context Protocol server for CODESYS automation platform

2846. **[MCPbundler](https://github.com/eugenepyvovarov/MCPbundler)** - ⭐ 25

2847. **[mcp-server-starter-ts](https://github.com/alexanderop/mcp-server-starter-ts)** - ⭐ 25
   A minimal TypeScript starter template for building Model Context Protocol (MCP) servers.

2848. **[foundry-vtt-mcp](https://github.com/adambdooley/foundry-vtt-mcp)** - ⭐ 25
   An MCP (Model Context Protocol) server that bridges Foundry VTT data with Claude Desktop, enabling users to chat with their game world data using their own Claude subscription.

2849. **[RevitMCP](https://github.com/oakplank/RevitMCP)** - ⭐ 25
   model context protocol for Autodesk Revit

2850. **[peta-core](https://github.com/dunialabs/peta-core)** - ⭐ 25
   Peta core: The Control Plane for MCP — secure vault, managed runtime, audit trail, and policy-based approvals.

2851. **[GenomeMCP](https://github.com/Eldergenix/GenomeMCP)** - ⭐ 24
   An AI-driven genomic intelligence system delivering structured ClinVar interpretation and high-precision exon, intron, and gene queries using the Model Context Protocol (MCP).

2852. **[Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop](https://github.com/gloveboxes/Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop)** - ⭐ 24

2853. **[opnsense-mcp-server](https://github.com/floriangrousset/opnsense-mcp-server)** - ⭐ 24
   A Model Context Protocol (MCP) server implementation for managing OPNsense firewalls. This server allows Claude and other MCP-compatible clients to interact with all features exposed by the OPNsense API.

2854. **[n8n-AI-agent-DVM-MCP-client](https://github.com/r0d8lsh0p/n8n-AI-agent-DVM-MCP-client)** - ⭐ 24
   An AI agent built in n8n which can find and use Model Context Protocol (MCP) Server Tools served as Data Vending Machines (DVM) over the Nostr network.

2855. **[mcp-server-semgrep](https://github.com/Szowesgad/mcp-server-semgrep)** - ⭐ 24
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

2856. **[python-sequential-thinking-mcp](https://github.com/XD3an/python-sequential-thinking-mcp)** - ⭐ 24
   A Python implementation of the Sequential Thinking MCP server using the official Model Context Protocol (MCP) Python SDK. This server facilitates a detailed, step-by-step thinking process for problem-solving and analysis.

2857. **[MCP](https://github.com/EduBase/MCP)** - ⭐ 24
   The EduBase MCP server enables Claude and other LLMs to interact with EduBase's comprehensive e-learning platform through the Model Context Protocol (MCP).

2858. **[mcp-task-manager-server](https://github.com/bsmi021/mcp-task-manager-server)** - ⭐ 24
   A local Model Context Protocol (MCP) server providing backend tools for client-driven project and task management using a SQLite database.

2859. **[brlaw_mcp_server](https://github.com/pdmtt/brlaw_mcp_server)** - ⭐ 24
   A MCP (Model Context Protocol) server for agent-driven research on Brazilian law using official sources

2860. **[DeepResearchMCP](https://github.com/ameeralns/DeepResearchMCP)** - ⭐ 24
   Deep Research MCP is an intelligent research assistant built on the Model Context Protocol (MCP) that performs comprehensive, multi-step research on any topic.

2861. **[aistudio-mcp-server](https://github.com/eternnoir/aistudio-mcp-server)** - ⭐ 24
   Google AI Studio MCP Server - Powerful Gemini API integration for Model Context Protocol with multi-modal file processing, PDF-to-Markdown conversion, image analysis,   and audio transcription capabilities. Supports all Gemini 2.5 models with comprehensive file format support.

2862. **[mcp-template-dotnet](https://github.com/NikiforovAll/mcp-template-dotnet)** - ⭐ 24
   This repository contains a template for creating a Model Context Protocol (MCP) applications in .NET.

2863. **[mcp-playground](https://github.com/zanetworker/mcp-playground)** - ⭐ 24
   Simple MCP Client for remote MCP Servers 🌐

2864. **[Awesome-MCP](https://github.com/Albertchamberlain/Awesome-MCP)** - ⭐ 24
   Awesome-MCP Servers & Clients & Funny things

2865. **[openai-copilot](https://github.com/feiskyer/openai-copilot)** - ⭐ 24
   Your life Copilot powered by LLM models (CLI interface for LLM models with MCP tools).

2866. **[calendar-mcp](https://github.com/deciduus/calendar-mcp)** - ⭐ 24
   This project implements a Python-based MCP (Model Context Protocol) server that acts as an interface between Large Language Models (LLMs) and the Google Calendar API. It enables LLMs to perform calendar operations via natural language requests.

2867. **[readwise-vector-db](https://github.com/leonardsellem/readwise-vector-db)** - ⭐ 24
   Turn your Readwise library into a blazing-fast, self-hosted semantic search engine – complete with nightly syncs, vector search API, Prometheus metrics, and a streaming MCP server for LLM clients.

2868. **[forgejo-mcp](https://github.com/goern/forgejo-mcp)** - ⭐ 24
   MIRROR ONLY!! This Model Context Protocol (MCP) server provides tools and resources for interacting with the Forgejo (specifically Codeberg.org) REST API.

2869. **[cfbd-mcp-server](https://github.com/lenwood/cfbd-mcp-server)** - ⭐ 24
   An MCP server enabling CFBD API queries within Claude Desktop.

2870. **[mcp-server-amazon-bedrock](https://github.com/zxkane/mcp-server-amazon-bedrock)** - ⭐ 24
   Model Context Procotol(MCP) server for using Amazon Bedrock Nova Canvas to generate images

2871. **[MiAO-MCP-for-Unity](https://github.com/MiAO-AI-Lab/MiAO-MCP-for-Unity)** - ⭐ 24
   MCP Server + Plugin for Unity Editor and Unity game. The Plugin allows to connect to MCP clients like Claude Desktop or others.

2872. **[github-repo-mcp](https://github.com/Ryan0204/github-repo-mcp)** - ⭐ 24
   Model Context Protocol server for Github Repo // Reading Github Repo

2873. **[k6-mcp-server](https://github.com/QAInsights/k6-mcp-server)** - ⭐ 24
   k6 MCP server

2874. **[bzm-mcp](https://github.com/Blazemeter/bzm-mcp)** - ⭐ 24
   Official BlazeMeter MCP Server for AI-driven performance testing

2875. **[mcp-desktop-automation](https://github.com/tanob/mcp-desktop-automation)** - ⭐ 24
   A Model Context Protocol server that provides desktop automation capabilities using RobotJS and screenshot capabilities

2876. **[metabase-mcp-server](https://github.com/hyeongjun-dev/metabase-mcp-server)** - ⭐ 24
   A Model Context Protocol server that integrates AI assistants with Metabase analytics platform

2877. **[batchdata-mcp-real-estate](https://github.com/zellerhaus/batchdata-mcp-real-estate)** - ⭐ 24
   Model Context Protocol (MCP) server for BatchData.io property and address APIs - Real estate data integration for Claude and other AI assistants

2878. **[mcp-ffmpeg-helper](https://github.com/sworddut/mcp-ffmpeg-helper)** - ⭐ 24
   一个基于 Model Context Protocol (MCP) 的 FFmpeg 辅助工具，提供视频处理功能。

2879. **[mcp-client-agent](https://github.com/shane-kercheval/mcp-client-agent)** - ⭐ 24
   CLI that uses DSPy to interact with MCP servers.

2880. **[roo-logger](https://github.com/annenpolka/roo-logger)** - ⭐ 24
   An MCP server for logging activity in Roo Code/Cline.

2881. **[identity-spec](https://github.com/agntcy/identity-spec)** - ⭐ 24
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

2882. **[apifox-mcp](https://github.com/iwen-conf/apifox-mcp)** - ⭐ 24
   Apifox MCP 服务器 - 让 Claude 等 AI 助手通过自然语言管理你的 Apifox 项目，轻松创建、更新和审计 API 接口

2883. **[mcp-annotated-java-sdk](https://github.com/thought2code/mcp-annotated-java-sdk)** - ⭐ 24
   Annotation-driven MCP dev 🚀 No Spring, Zero Boilerplate, Pure Java

2884. **[cursor-db-mcp](https://github.com/jbdamask/cursor-db-mcp)** - ⭐ 24
   Model Context Protocol server for querying Cursor chat history

2885. **[d365fo-client](https://github.com/mafzaal/d365fo-client)** - ⭐ 24
   A comprehensive Python client library and MCP server for Microsoft Dynamics 365 Finance & Operations (D365 F&O) that provides easy access to OData endpoints, metadata operations, label management, and AI assistant integration.

2886. **[lua-resty-mcp](https://github.com/ufownl/lua-resty-mcp)** - ⭐ 24
   Model Context Protocol SDK implemented in Lua for OpenResty

2887. **[solana-mcp](https://github.com/tony-42069/solana-mcp)** - ⭐ 24
   A comprehensive Solana MCP (Model Context Protocol) server for analyzing memecoins, tracking trends, and providing AI-powered insights using cultural analysis and on-chain data.

2888. **[opnsense-mcp-server](https://github.com/Pixelworlds/opnsense-mcp-server)** - ⭐ 24
   Modular MCP server for OPNsense firewall management - 88 tools providing access to 2000+ methods through AI assistants

2889. **[openproject-mcp-server](https://github.com/AndyEverything/openproject-mcp-server)** - ⭐ 24
   A Model Context Protocol (MCP) server that provides seamless integration with OpenProject API v3.

2890. **[silverbullet-mcp](https://github.com/Ahmad-A0/silverbullet-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) server to interact with your SilverBullet notes and data.

2891. **[deep-research](https://github.com/ssdeanx/deep-research)** - ⭐ 24
   The Deep Research Assistant is meticulously crafted on Mastra's modular, scalable architecture, designed for intelligent orchestration and seamless human-AI interaction. It's built to tackle complex research challenges autonomously.

2892. **[aj-mcp](https://github.com/lightweight-component/aj-mcp)** - ⭐ 24
   Simple MCP SDK in Java

2893. **[skill-mcp](https://github.com/fkesheh/skill-mcp)** - ⭐ 24
   LLM-managed skills platform using MCP - create, edit, and execute skills programmatically in Claude, Cursor, and any MCP-compatible client without manual file uploads.

2894. **[mcp-claude-spotify](https://github.com/imprvhub/mcp-claude-spotify)** - ⭐ 24
   An integration that allows Claude Desktop to interact with Spotify using the Model Context Protocol (MCP).

2895. **[Wwise-MCP](https://github.com/BilkentAudio/Wwise-MCP)** - ⭐ 24
   Wwise-MCP is a Model Context Protocol server that allows LLMs to interact with the Wwise Authoring application. It exposes tools from a custom python waapi function library to MCP clients.

2896. **[arch-mcp](https://github.com/nihalxkumar/arch-mcp)** - ⭐ 24
   Arch Linux MCP (Model Context Protocol)

2897. **[cheat-engine-server-python](https://github.com/bethington/cheat-engine-server-python)** - ⭐ 24
   MCP Cheat Engine Server — provides safe, structured read-only access to memory analysis and debugging functionality through the Model Context Protocol (MCP). For developers, security researchers, and game modders.

2898. **[wiki-js-mcp](https://github.com/talosdeus/wiki-js-mcp)** - ⭐ 24
   Model Context Protocol (MCP) server for Wiki.js with hierarchical documentation & Docker setup

2899. **[relace-mcp](https://github.com/possible055/relace-mcp)** - ⭐ 23
   Unofficial Relace MCP client with AI features. Personal project; not affiliated with or endorsed by Relace

2900. **[Model-Context-Protocol](https://github.com/Coding-Crashkurse/Model-Context-Protocol)** - ⭐ 23

2901. **[jigsawstack-mcp-server](https://github.com/JigsawStack/jigsawstack-mcp-server)** - ⭐ 23
   Model Context Protocol Server that allows AI models to interact with JigsawStack models!

2902. **[cortex](https://github.com/FreePeak/cortex)** - ⭐ 23
   A declarative platform for building Model Context Protocol (MCP) servers in Golang—exposing tools, resources & prompts in a clean, structured way

2903. **[paraview_mcp](https://github.com/LLNL/paraview_mcp)** - ⭐ 23
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

2904. **[lineshopping-api-mcp](https://github.com/woraphol-j/lineshopping-api-mcp)** - ⭐ 23
   Model Context Protocol (MCP) server for the LINE SHOPPING API. Enables AI agents and tools to manage products, inventory, orders, and settlements on LINE SHOPPING via auto-generated MCP tools from the official OpenAPI spec.

2905. **[home-assistant-mcp](https://github.com/hpohlmann/home-assistant-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) integration that enables AI assistants to search for and control Home Assistant devices through natural language commands in Cursor.

2906. **[mcp-twitter-server](https://github.com/crazyrabbitLTC/mcp-twitter-server)** - ⭐ 23
   Model Context Protocol Server for Accessing twitter

2907. **[strava-mcp](https://github.com/kw510/strava-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) server with Strava OAuth integration, built on Cloudflare Workers. Enables secure authentication and tool access for MCP clients like Claude and Cursor through Strava login. Perfect for developers looking to integrate Strava authentication with AI tools.

2908. **[mcp-community](https://github.com/Mirascope/mcp-community)** - ⭐ 23
   Easily run, deploy, and connect to MCP servers

2909. **[jsonv-ts](https://github.com/dswbx/jsonv-ts)** - ⭐ 23
   JSON Schema builder and validator for TypeScript with static type inference, Hono middleware for OpenAPI generation and validation, and MCP server/client implementation. Lightweight, dependency-free, and built on Web Standards.

2910. **[aisdk-mcp-bridge](https://github.com/vrknetha/aisdk-mcp-bridge)** - ⭐ 23
   Bridge package enabling seamless integration between Model Context Protocol (MCP) servers and AI SDK tools. Supports multiple server types, real-time communication, and TypeScript.

2911. **[nlweb-net](https://github.com/nlweb-ai/nlweb-net)** - ⭐ 23
   The official .NET 9 implementation of the NLWeb protocol for building natural language web interfaces with support for List, Summarize, and Generate query modes, plus Model Context Protocol (MCP) integration for AI clients.

2912. **[mcp-pa-ai-agent](https://github.com/zhangzhongnan928/mcp-pa-ai-agent)** - ⭐ 23
   A personal assistant AI agent built with the Model Context Protocol (MCP)

2913. **[microsoft_fabric_mcp](https://github.com/Augustab/microsoft_fabric_mcp)** - ⭐ 23
   MCP server wrapping around the Fabric Rest API

2914. **[lightdash-mcp-server](https://github.com/syucream/lightdash-mcp-server)** - ⭐ 23
   A MCP(Model Context Protocol) server that accesses to Lightdash

2915. **[balldontlie-mcp](https://github.com/mikechao/balldontlie-mcp)** - ⭐ 23
   An MCP Server implementation that integrates the Balldontlie API, to provide information about players, teams and games for the NBA, NFL and MLB

2916. **[slack-mcp-client](https://github.com/csonigo/slack-mcp-client)** - ⭐ 23
   An MCP client for slack in Typescript

2917. **[fastify-mcp-server](https://github.com/flaviodelgrosso/fastify-mcp-server)** - ⭐ 23
   Fastify plugin to easily spin up Model Context Protocol (MCP) HTTP servers

2918. **[json2video-mcp-server](https://github.com/omergocmen/json2video-mcp-server)** - ⭐ 23
   Message Communication Protocol server for json2video API integration

2919. **[congressMCP](https://github.com/amurshak/congressMCP)** - ⭐ 23
   An MCP server allowing AI agents and MCP clients to interface with the Congress.gov API

2920. **[holoviz-mcp](https://github.com/MarcSkovMadsen/holoviz-mcp)** - ⭐ 23
   ✨A MCP server that provides intelligent access to the HoloViz ecosystem for humans and AIs.

2921. **[kratos-mcp](https://github.com/ceorkm/kratos-mcp)** - ⭐ 23
   🏛️ Memory System for AI Coding Tools - Never explain your codebase again. MCP server with perfect project isolation, 95.8% context accuracy, and the Four Pillars Framework.

2922. **[mcp-rss-aggregator](https://github.com/imprvhub/mcp-rss-aggregator)** - ⭐ 23
   Model Context Protocol Server for aggregating RSS feeds in Claude Desktop

2923. **[codemesh](https://github.com/kiliman/codemesh)** - ⭐ 23
   The Self-Improving MCP Server - Agents write code to orchestrate multiple MCP servers with intelligent TypeScript execution and auto-augmentation

2924. **[azure-diagram-mcp](https://github.com/dminkovski/azure-diagram-mcp)** - ⭐ 23
   MCP server that turns natural-language prompts into Microsoft Azure architecture diagrams (PNG) using Python Diagrams + Graphviz.

2925. **[Unity-AI-Animation](https://github.com/IvanMurzak/Unity-AI-Animation)** - ⭐ 23
   AI-powered tools for Unity animation workflow. Create and modify AnimationClips and AnimatorControllers directly through natural language commands.

2926. **[fastify-mcp](https://github.com/haroldadmin/fastify-mcp)** - ⭐ 22
   A Fastify plugin to run Model Context Protocol (MCP) servers

2927. **[MCP-123](https://github.com/Tylersuard/MCP-123)** - ⭐ 22
   The easiest possible implementation of an MCP server and client.  Set up a server or a client in 2 lines of code.

2928. **[nobitex-mcp-server](https://github.com/xmannii/nobitex-mcp-server)** - ⭐ 22
   a Model Context Protocol (MCP) server that provides access to cryptocurrency market data from the Nobitex API.

2929. **[mcp-server-oracle](https://github.com/hdcola/mcp-server-oracle)** - ⭐ 22
   Model Context Protocol server to access oracle database

2930. **[higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation that enables comprehensive configuration and management of Higress.

2931. **[Elysia-mcp](https://github.com/keithagroves/Elysia-mcp)** - ⭐ 22
   Model Context Protocol (MCP) Server for Bun and Elysia

2932. **[mcp-flux-studio](https://github.com/jmanhype/mcp-flux-studio)** - ⭐ 22
   A Model Context Protocol server for Flux image generation, providing tools for image generation, manipulation, and control

2933. **[DANP-Engine](https://github.com/DANP-LABS/DANP-Engine)** - ⭐ 22
   A trusted AI Model Context Protocol (MCP) runtime for secure, decentralized AI tools and services.

2934. **[mcp-sse-authenticated-cloud-run](https://github.com/the-freetech-company/mcp-sse-authenticated-cloud-run)** - ⭐ 22
   Host an Model Context Protocol SSE deployment on Cloud Run, Authenticating with IAM.

2935. **[MobSF-MCP](https://github.com/il-il1/MobSF-MCP)** - ⭐ 22
   a Node.js-based Model Context Protocol implementation for MobSF

2936. **[async-mcp](https://github.com/v3g42/async-mcp)** - ⭐ 22
   A minimalistic async Rust implementation of the Model Context Protocol (MCP).

2937. **[mcpagentai](https://github.com/mcpagents-ai/mcpagentai)** - ⭐ 22
   Python SDK designed to simplify interactions with MCP (Model Context Protocol) servers. It provides an easy-to-use interface for connecting to MCP servers, reading resources, and calling tools

2938. **[p5js-ai-editor](https://github.com/adilmoujahid/p5js-ai-editor)** - ⭐ 22
   A modern, web-based IDE for creating and editing p5.js sketches with AI assistance and Model Context Protocol (MCP) integration for Claude Desktop.

2939. **[printify-mcp](https://github.com/TSavo/printify-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server for integrating AI assistants with Printify's print-on-demand platform

2940. **[cf-mcp-client](https://github.com/cpage-pivotal/cf-mcp-client)** - ⭐ 22
   Tanzu Platform Chat

2941. **[supabase-mcp-client](https://github.com/tambo-ai/supabase-mcp-client)** - ⭐ 22
   Supabase MCP client react app with Tambo

2942. **[biznagafest-mcp](https://github.com/0GiS0/biznagafest-mcp)** - ⭐ 22
   MCP Servers en Málaga con salero

2943. **[langchain-mcp-tools-ts](https://github.com/hideya/langchain-mcp-tools-ts)** - ⭐ 22
   MCP to LangChain Tools Conversion Utility / TypeScript

2944. **[dbt-docs-mcp](https://github.com/mattijsdp/dbt-docs-mcp)** - ⭐ 22
   MCP (model context protocol) server for interacting with dbt Docs

2945. **[Claude-Code-MCP-Manager](https://github.com/qdhenry/Claude-Code-MCP-Manager)** - ⭐ 22
    A comprehensive tool to manage Model Context Protocol (MCP) configurations for Claude code

2946. **[Excel-MCP-Server-Master](https://github.com/guillehr2/Excel-MCP-Server-Master)** - ⭐ 22
   Excel MCP Server - Manipulate Excel files without Microsoft Excel. Model Context Protocol for XLSX, XLSM with Claude AI integration

2947. **[google-search-console-mcp](https://github.com/surendranb/google-search-console-mcp)** - ⭐ 22
   Google Search Console MCP Server for Claude, Cursor, Windsurf and other MCP Clients

2948. **[metmuseum-mcp](https://github.com/mikechao/metmuseum-mcp)** - ⭐ 22
   Met Museum MCP integration to discover the art collection at The Metropolitan Museum of Art in New York

2949. **[nix-mcp-servers](https://github.com/ismail-kattakath/nix-mcp-servers)** - ⭐ 22
   A nix flake for configuring Model Context Protocol (MCP) servers across supported AI assistant clients

2950. **[ib-mcp-cache-server](https://github.com/ibproduct/ib-mcp-cache-server)** - ⭐ 22
   Memory Cache Server for use with supported MCP API Clients.

2951. **[your-money-left-the-chat](https://github.com/Rayato159/your-money-left-the-chat)** - ⭐ 22
   A Rust + MCP powered financial tracker that knows exactly where your money ghosted you.

2952. **[turbomcpstudio](https://github.com/Epistates/turbomcpstudio)** - ⭐ 22
   A native desktop application for developing, testing, and debugging Model Context Protocol servers.

2953. **[mcp-cmd](https://github.com/developit/mcp-cmd)** - ⭐ 22
   CLI for calling successive MCP Server tools

2954. **[fast-mcp-telegram](https://github.com/leshchenko1979/fast-mcp-telegram)** - ⭐ 22
   Telegram MCP Server and HTTP-MTProto bridge | Multi-user auth, intelligent search, file sending, web setup | Docker & PyPI ready

2955. **[codingbuddy](https://github.com/JeremyDev87/codingbuddy)** - ⭐ 22
   Codingbuddy orchestrates 29 specialized AI agents to deliver code quality comparable to a team of human experts through a PLAN → ACT → EVAL workflow.

2956. **[MCP_A2A](https://github.com/regismesquita/MCP_A2A)** - ⭐ 21
   A2A MCP Server is a lightweight Python bridge that lets Claude Desktop or any MCP client talk to A2A agents. It provides three tools: register servers, list agents, and call an agent, enabling quick integration of A2A-compatible agents with zero boilerplate for rapid prototyping.

2957. **[grumpydev-mcp](https://github.com/sinedied/grumpydev-mcp)** - ⭐ 21
   Let the grumpy senior dev review your code with this MCP server

2958. **[bridge-mcp](https://github.com/codingjam/bridge-mcp)** - ⭐ 21
   Open Source MCP gateway and proxy for Model Context Protocol (MCP) servers with enterprise authentication and service discovery

2959. **[mcpsharepoint](https://github.com/BrianCusack/mcpsharepoint)** - ⭐ 21
   Model Context Protocol server that provides access to Organisational SharePoint.

2960. **[command-executor-mcp-server](https://github.com/Sunwood-ai-labs/command-executor-mcp-server)** - ⭐ 21
   Model Context Protocol Server for Safely Executing Pre-approved Commands

2961. **[emqx-mcp-server](https://github.com/Benniu/emqx-mcp-server)** - ⭐ 21
   A Model Context Protocol (MCP) server implementation that provides EMQX MQTT broker interaction.

2962. **[mcp-sentry](https://github.com/MCP-100/mcp-sentry)** - ⭐ 21
   A Model Context Protocol server for retrieving and analyzing issues from Sentry.io

2963. **[mcp-korean-spell](https://github.com/winterjung/mcp-korean-spell)** - ⭐ 21
   MCP(Model Context Protocol) server designed for Korean spell checking

2964. **[DocsRay](https://github.com/MIMICLab/DocsRay)** - ⭐ 21
   Lightweight PDF Q&A tool powered by RAG (Retrieval-Augmented Generation) with MCP (Model Context Protocol) Support.

2965. **[MCPRules](https://github.com/bartwisch/MCPRules)** - ⭐ 21
   A powerful Model Context Protocol (MCP) server that manages and serves programming guidelines and rules. This server integrates with development tools to provide consistent coding standards across projects.

2966. **[code-context-mcp](https://github.com/fkesheh/code-context-mcp)** - ⭐ 21
   A Model Context Protocol (MCP) server for providing code context from git repositories

2967. **[mcp-knowledge-base](https://github.com/hjlee94/mcp-knowledge-base)** - ⭐ 21
   MCP agent/client/server implementation for private knowledge base

2968. **[awesome-mcp](https://github.com/MCPHubCloud/awesome-mcp)** - ⭐ 21
   A collection of mcp servers/client/sdks

2969. **[server-sharepoint](https://github.com/Zerg00s/server-sharepoint)** - ⭐ 21
   This is a MCP server for Claude Desktop that allows you to interact with SharePoint Online using the SharePoint REST API. It is designed to be used with the [Claude Desktop](https://claude.ai/download) app, but could be used by other MCP clients as well.

2970. **[plux](https://github.com/milisp/plux)** - ⭐ 21
   💡AI finder/explorer. One click @files via a visual filetree and save insights in a notepad. build with Tauri

2971. **[ffmpeg-mcp-lite](https://github.com/kevinwatt/ffmpeg-mcp-lite)** - ⭐ 21
   MCP server for video/audio processing via FFmpeg - convert, compress, trim, extract audio, add subtitles

2972. **[mcp-deepseek-demo](https://github.com/Ulanxx/mcp-deepseek-demo)** - ⭐ 21
   deepseek 结合 mcp 场景，最小用例，包括 client and server

2973. **[room-mcp](https://github.com/agree-able/room-mcp)** - ⭐ 21
   Allow MCP clients like claude-desktop to use rooms to coordinate with other agents

2974. **[mcp-observer-server](https://github.com/hesreallyhim/mcp-observer-server)** - ⭐ 21
   An MCP server that provides server-to-client notifications for file changes that the client subscribes to

2975. **[mcp-wireshark](https://github.com/khuynh22/mcp-wireshark)** - ⭐ 21
   An MCP server that integrates Wireshark/tshark with AI tools and IDEs. Capture live traffic, parse .pcap files, apply display filters, follow streams, and export JSON - all via Claude Desktop, VS Code, or CLI. Cross‑platform, typed, tested, and pip‑installable.

2976. **[mcp-framework](https://github.com/koki7o/mcp-framework)** - ⭐ 21
   Rust MCP framework for building AI agents

2977. **[GUI-MCP](https://github.com/PhialsBasement/GUI-MCP)** - ⭐ 21
   A Blueprint-style visual node editor for creating FastMCP servers. Build MCP tools, resources, and prompts by connecting nodes - no coding required.

2978. **[hs-mcp](https://github.com/buecking/hs-mcp)** - ⭐ 21
   Haskell server/client for MCP (Model Context Protocol)

2979. **[codebase-context](https://github.com/PatrickSys/codebase-context)** - ⭐ 21
   MCP server for codebase intelligence — patterns, conventions, architecture, and rationale for AI coding agents

2980. **[zotero-mcp-server](https://github.com/swairshah/zotero-mcp-server)** - ⭐ 21
   MCP server to expose local zotero repository to MCP clients 

2981. **[mcpc](https://github.com/micl2e2/mcpc)** - ⭐ 21
   Cross-platform C SDK for Model Context Protocol (MCP), in modern🚀 C23.

2982. **[Unity-AI-ProBuilder](https://github.com/IvanMurzak/Unity-AI-ProBuilder)** - ⭐ 21
   AI-powered 3D modeling tools for Unity ProBuilder. Enables AI assistants to create and manipulate editable meshes through natural language commands. Create primitive shapes, extrude faces, bevel edges, apply materials, merge objects, and perform advanced mesh operations like bridging and subdivision.

2983. **[NiFiMCP](https://github.com/ms82119/NiFiMCP)** - ⭐ 21
   An MCP Server and client for communicating with Nifi (v1.28)

2984. **[notebooklm-mcp-secure](https://github.com/Pantheon-Security/notebooklm-mcp-secure)** - ⭐ 21
   Secure NotebookLM MCP Server - Query Google NotebookLM from Claude/AI agents with 14 security hardening layers

2985. **[help-scout-mcp-server](https://github.com/drewburchfield/help-scout-mcp-server)** - ⭐ 21
   MCP server for Help Scout - search conversations, threads, and inboxes with AI agents

2986. **[datawrapper-mcp](https://github.com/palewire/datawrapper-mcp)** - ⭐ 21
   A Model Context Protocol (MCP) server for creating Datawrapper charts using AI assistants.

2987. **[PowerShell.MCP](https://github.com/yotsuda/PowerShell.MCP)** - ⭐ 21
   The universal MCP server for Claude Code and other MCP-compatible clients. One installation gives AI access to 10,000+ PowerShell modules and any CLI tool. You and AI collaborate in the same console with full transparency. Supports Windows, Linux, and macOS.

2988. **[mcp-server-runner](https://github.com/yonaka15/mcp-server-runner)** - ⭐ 20
   A WebSocket server implementation for running Model Context Protocol (MCP) servers. This application enables MCP servers to be accessed via WebSocket connections, facilitating integration with web applications and other network-enabled clients.

2989. **[mcp-ai-agent](https://github.com/fkesheh/mcp-ai-agent)** - ⭐ 20
   A TypeScript library that enables AI agents to leverage MCP (Model Context Protocol) servers for enhanced capabilities. This library integrates with the AI SDK to provide a seamless way to connect to MCP servers and use their tools in AI-powered applications.

2990. **[easymcp](https://github.com/promptmesh/easymcp)** - ⭐ 20
   A high performance MCP client sdk for python

2991. **[mcp-server-memos-py](https://github.com/RyoJerryYu/mcp-server-memos-py)** - ⭐ 20
   A Python package enabling LLM models to interact with the Memos server via the MCP interface for searching, creating, retrieving, and managing memos.

2992. **[PDB-MCP-Server](https://github.com/Augmented-Nature/PDB-MCP-Server)** - ⭐ 20
   A Model Context Protocol (MCP) server that provides access to the Protein Data Bank (PDB) - the worldwide repository of information about the 3D structures of proteins, nucleic acids, and complex assemblies.

2993. **[mcp-prompt-optimizer](https://github.com/Bubobot-Team/mcp-prompt-optimizer)** - ⭐ 20
   Advanced MCP server providing cutting-edge prompt optimization tools with research-backed strategies

2994. **[guidance-for-scalable-model-inference-and-agentic-ai-on-amazon-eks](https://github.com/aws-solutions-library-samples/guidance-for-scalable-model-inference-and-agentic-ai-on-amazon-eks)** - ⭐ 20
   Comprehensive, scalable ML inference architecture using Amazon EKS, leveraging Graviton processors for cost-effective CPU-based inference and GPU instances for accelerated inference. Guidance provides a complete end-to-end platform for deploying LLMs with agentic AI capabilities, including RAG and MCP

2995. **[mssqlclient-mcp-server](https://github.com/aadversteeg/mssqlclient-mcp-server)** - ⭐ 20
   A Microsoft SQL Server client implementing the Model Context Protocol (MCP). This server provides SQL query capabilities through a simple MCP interface.

2996. **[mcp-mesh](https://github.com/dhyansraj/mcp-mesh)** - ⭐ 20
   Enterprise-grade distributed AI agent framework | Develop → Deploy → Observe | K8s-native | Dynamic DI | Auto-failover | Multi-LLM | Python + TypeScript

2997. **[mcp-free-usdc-transfer](https://github.com/magnetai/mcp-free-usdc-transfer)** - ⭐ 20
   MCP (Model Context Protocol) server - free usdc transfer powered by Coinbase CDP

2998. **[mcp-file-operations-server](https://github.com/bsmi021/mcp-file-operations-server)** - ⭐ 20
   A Model Context Protocol (MCP) server that provides enhanced file operation capabilities with streaming, patching, and change tracking support.

2999. **[cucumberstudio-mcp](https://github.com/HeroSizy/cucumberstudio-mcp)** - ⭐ 20
   MCP Server for Cucumber Studio

3000. **[aws-s3-mcp](https://github.com/samuraikun/aws-s3-mcp)** - ⭐ 20
   MCP server to integrate AWS S3 and LLM

3001. **[knowledgebase-mcp](https://github.com/biocontext-ai/knowledgebase-mcp)** - ⭐ 20
   BioContextAI Knowledgebase MCP server for biomedical agentic AI 

3002. **[registry](https://github.com/biocontext-ai/registry)** - ⭐ 20
   The BioContextAI Registry for biomedical MCP servers

3003. **[agent-twitter-client-mcp](https://github.com/ryanmac/agent-twitter-client-mcp)** - ⭐ 20
   A Model Context Protocol (MCP) server that integrates with X using the @elizaOS `agent-twitter-client` package, allowing AI models to interact with Twitter without direct API access.

3004. **[mcp-diagnostics-extension](https://github.com/newbpydev/mcp-diagnostics-extension)** - ⭐ 20
   VS Code extension that exposes diagnostic problems via Model Context Protocol (MCP) for AI agents and tools

3005. **[minime-mcp](https://github.com/manujbawa/minime-mcp)** - ⭐ 20
   Universal infinite memory layer for Developer AI assistants. One shared brain across Claude, Cursor, Windsurf & more. 100% local, built on MCP standard. Stop re-explaining context

3006. **[lotus-wisdom-mcp](https://github.com/linxule/lotus-wisdom-mcp)** - ⭐ 19
   MCP server for structured problem-solving using the Lotus Sutra's wisdom framework. Beautiful visualizations, multiple thinking approaches, compatible with various MCP clients (e.g., Claude Desktop, Cursor, Cherry Studio).

3007. **[gemini-mcp-client](https://github.com/angrysky56/gemini-mcp-client)** - ⭐ 19
   A MCP (Model Context Protocol) client that uses Google Gemini AI models for intelligent tool usage and conversation handling.  Tested working nicely with Claude Desktop as an MCP Server currently. Based on untested AI gen code by a non-coder use at own risk.

3008. **[starbase](https://github.com/metorial/starbase)** - ⭐ 19
   Connect, explore, and test any MCP server with AI models 🤖 ⚡

3009. **[flutter-ai-labs](https://github.com/theshivamlko/flutter-ai-labs)** - ⭐ 19
   A curated collection of LLM-powered Flutter apps built using RAG, AI Agents, Multi-Agent Systems, MCP, and Voice Agents.

3010. **[mcp](https://github.com/EmilLindfors/mcp)** - ⭐ 19
    A crate for making MCP (Model Context Protocol) compatible programs with rust

3011. **[perplexity-mcp-server](https://github.com/cyanheads/perplexity-mcp-server)** - ⭐ 19
   A Perplexity API MCP server that unlocks Perplexity's search-augmented AI capabilities for LLM agents. Features robust error handling, secure input validation, and transparent reasoning with the showThinking parameter.

3012. **[mcp-frontend](https://github.com/shaharia-lab/mcp-frontend)** - ⭐ 19
   Frontend for MCP (Model Context Protocol) Kit for Go - A Complete MCP solutions for ready to use

3013. **[mcp-server-mariadb](https://github.com/abel9851/mcp-server-mariadb)** - ⭐ 19
   An mcp server that provides read-only access to MariaDB.

3014. **[mcp-server](https://github.com/paperinvest/mcp-server)** - ⭐ 19
   Official MCP server for Paper's trading platform - enables AI assistants to interact with Paper's API

3015. **[agent-mcp](https://github.com/grupa-ai/agent-mcp)** - ⭐ 19
   MCPAgent for Grupa.AI Multi-agent Collaboration Network (MACNET) with Model Context Protocol (MCP) capabilities baked in

3016. **[html-to-markdown-mcp](https://github.com/levz0r/html-to-markdown-mcp)** - ⭐ 19
   MCP server for converting HTML to Markdown using Turndown.js. Fetch web pages and convert them to clean, formatted Markdown.

3017. **[linux-command-mcp](https://github.com/xkiranj/linux-command-mcp)** - ⭐ 19
   MCP server and client for running Linux commands

3018. **[mcp-server-client-demo](https://github.com/S1LV3RJ1NX/mcp-server-client-demo)** - ⭐ 19
   Streamable HTTP based MCP server and Client demo with auto registry, Dockerfile setup and env. 

3019. **[mcp-web-scraper](https://github.com/Decodo/mcp-web-scraper)** - ⭐ 19
   The Decodo MCP server which enables MCP clients to interface with services.

3020. **[autotask-mcp](https://github.com/asachs01/autotask-mcp)** - ⭐ 19
   MCP server for Kaseya Autotask PSA — 39 tools for companies, tickets, projects, time entries, and more

3021. **[MCP-Mastery-with-Claude-and-Langchain](https://github.com/laxmimerit/MCP-Mastery-with-Claude-and-Langchain)** - ⭐ 19
   Build MCP servers & clients with Python, Streamlit, ChromaDB, LangChain, LangGraph agents, and Ollama integrations

3022. **[mcp](https://github.com/zuplo/mcp)** - ⭐ 19
   A fetch API based TypeScript SDK for MCP

3023. **[openapi2mcptools](https://github.com/2013xile/openapi2mcptools)** - ⭐ 19
   OpenAPI specifications => MCP (Model Context Protocol) tools

3024. **[suse-ai-up](https://github.com/SUSE/suse-ai-up)** - ⭐ 19
   A comprehensive platform for managing and proxying Model Context Protocol (MCP) servers, providing scalable AI service orchestration across multiple microservices.

3025. **[ai-cli](https://github.com/manusa/ai-cli)** - ⭐ 19
   ai-cli lets you go from zero to AI-powered in seconds in a safe, automated and tailored way.

3026. **[local_faiss_mcp](https://github.com/nonatofabio/local_faiss_mcp)** - ⭐ 19
   Local FAISS vector store as an MCP server – drop-in local RAG for Claude / Copilot / Agents.

3027. **[mcpls](https://github.com/bug-ops/mcpls)** - ⭐ 19
   Universal MCP to LSP bridge - expose Language Server Protocol capabilities as MCP tools for AI agents

3028. **[qdrant-mcp-server](https://github.com/mhalder/qdrant-mcp-server)** - ⭐ 19
   MCP server for semantic search using local Qdrant vector database and OpenAI embeddings

3029. **[jenkins-mcp-enterprise](https://github.com/Jordan-Jarvis/jenkins-mcp-enterprise)** - ⭐ 19
   The most advanced Jenkins MCP server available - Enterprise debugging, multi-instance management, AI-powered failure analysis, vector search, and configurable diagnostics for complex CI/CD pipelines.

3030. **[rlm-claude](https://github.com/EncrEor/rlm-claude)** - ⭐ 19
   Recursive Language Models for Claude Code - Infinite memory solution inspired by MIT CSAIL paper

3031. **[eleven.shopping](https://github.com/elevenlabs/eleven.shopping)** - ⭐ 18
   ElevenLabs Agent with Storefront MCP UI Server & MCP UI client

3032. **[typescript-mcp-client](https://github.com/CodelyTV/typescript-mcp-client)** - ⭐ 18

3033. **[openpyxl-mcp-server](https://github.com/jonemo/openpyxl-mcp-server)** - ⭐ 18
   A thin wrapper around the OpenPyXl Python library that exposes some of its features as Model Context Protocol (MCP) server. This allows Claude and other MCP clients to fetch data from Excel files.

3034. **[sufetch](https://github.com/productdevbook/sufetch)** - ⭐ 18
   Type-safe OpenAPI clients with MCP server for AI-driven API exploration

3035. **[SimpleMcp.Demo](https://github.com/hassanhabib/SimpleMcp.Demo)** - ⭐ 18
   Simplest Possible Demo for Building MCP Server & Client

3036. **[mcpbi](https://github.com/jonaolden/mcpbi)** - ⭐ 18
   PowerBI MCP server to give LLM clients (Claude, GH Copilot,etc) context from locally running PowerBI Desktop instances.

3037. **[mcp-copilot](https://github.com/tshu-w/mcp-copilot)** - ⭐ 18
   A meta MCP server that seamlessly scales LLMs to 1000+ MCP servers through automatic routing.

3038. **[mcp-libsql](https://github.com/Xexr/mcp-libsql)** - ⭐ 18
   Secure MCP server for libSQL databases with comprehensive tools, connection pooling, and transaction support. Built with TypeScript for Claude Desktop, Claude Code, Cursor, and other MCP clients.

3039. **[mcp-link](https://github.com/AuraFriday/mcp-link)** - ⭐ 18
   Let AI agents like ChatGPT & Claude use real-world local/remote tools you approve via browser extension + optional MCP server

3040. **[gpt2099.nu](https://github.com/cablehead/gpt2099.nu)** - ⭐ 18
   a Nushell cross.stream extension to interact with LLMs and MCP servers

3041. **[Devmind-MCP](https://github.com/JochenYang/Devmind-MCP)** - ⭐ 18
   DevMind MCP provides **persistent memory capabilities** for AI assistants through the Model Context Protocol (MCP). It enables AI to remember context across conversations, automatically track development activities, and retrieve relevant information intelligently.

3042. **[seedream-image-mcp](https://github.com/wearzdk/seedream-image-mcp)** - ⭐ 18
   🚀 PixelMCP | 为你的 Cursor、Claude Code 等集成AI绘画能力，让AI生成的页面不再单调！

3043. **[mcp-chat-studio](https://github.com/JoeCastrom/mcp-chat-studio)** - ⭐ 18
   A powerful MCP testing tool with multi-provider LLM support (Ollama, OpenAI, Claude, Gemini). Test, debug, and develop MCP servers with a modern UI.

3044. **[mcp-agent](https://github.com/joshuaalpuerto/mcp-agent)** - ⭐ 18
   Lightweight, focused utilities to manage connections and execute MCP tools with minimal integration effort. Use it to directly call tools or build simple agents within your current architecture.

3045. **[Zammad-MCP](https://github.com/basher83/Zammad-MCP)** - ⭐ 18
   A Model Context Protocol (MCP) server for Zammad integration, enabling AI assistants to interact with tickets, users, and organizations.

3046. **[mcpx](https://github.com/AIGC-Hackers/mcpx)** - ⭐ 18
   Token-efficient MCP client: TypeScript schemas instead of JSON, LLM-friendly syntax, batch calls, TOON output. Built for Claude/GPT automations.

3047. **[mcp-server-microsoft-paint](https://github.com/ghuntley/mcp-server-microsoft-paint)** - ⭐ 18

3048. **[mcp-chain-of-draft-prompt-tool](https://github.com/brendancopley/mcp-chain-of-draft-prompt-tool)** - ⭐ 18
   MCP prompt tool applying Chain-of-Draft (CoD) reasoning - BYOLLM

3049. **[codeprism](https://github.com/rustic-ai/codeprism)** - ⭐ 18
   An experimental, 100% AI-generated, high-performance code intelligence server providing AI assistants with a graph-based understanding of codebases.

3050. **[Augmented-Nature-UniProt-MCP-Server](https://github.com/Augmented-Nature/Augmented-Nature-UniProt-MCP-Server)** - ⭐ 18
   A comprehensive Model Context Protocol (MCP) server providing advanced access to the UniProt protein database. 

3051. **[mcp-oauth-proxy](https://github.com/obot-platform/mcp-oauth-proxy)** - ⭐ 18
   Oauth 2.1 proxy server that can autheticate client and proxy requests to mcp server

3052. **[mcp-yfinance](https://github.com/9nate-drake/mcp-yfinance)** - ⭐ 18
   MCP Server for fething yfinance financial data into Claude Desktop

3053. **[gh-mcp](https://github.com/shuymn/gh-mcp)** - ⭐ 18
   A GitHub CLI extension that seamlessly runs the github-mcp-server in Docker using your existing gh authentication. Eliminates manual PAT setup by automatically retrieving GitHub credentials and launching the MCP server with proper authentication.

3054. **[eraser-io-mcp-server](https://github.com/buck-0x/eraser-io-mcp-server)** - ⭐ 18
   A Python MCP (Model Context Protocol) server and CLI tool to render diagrams using the Eraser API.

3055. **[ACP-MCP-Server](https://github.com/GongRzhe/ACP-MCP-Server)** - ⭐ 18
   A bridge server that connects Agent Communication Protocol (ACP) agents with Model Context Protocol (MCP) clients, enabling seamless integration between ACP-based AI agents and MCP-compatible tools like Claude Desktop.

3056. **[UCAI](https://github.com/nirholas/UCAI)** - ⭐ 18
   Universal Contract AI Interface (UCAI) 🔗 ABI to MCP | The open standard for connecting AI agents to blockchain. MCP server generator for smart contracts. Claude + Uniswap, Aave, ERC20, NFTs, DeFi. Python CLI, Web3 integration, transaction simulation. Polygon, Arbitrum, Base, Ethereum EVM chains. Claude, GPT, LLM tooling, Solidity, OpenAI.

3057. **[smartlead-mcp-server](https://github.com/jonathan-politzki/smartlead-mcp-server)** - ⭐ 17
   Local version of Smartlead MCP for quick download and deployment to MCP compatible clients or n8n.

3058. **[mcp-http-client-example](https://github.com/slavashvets/mcp-http-client-example)** - ⭐ 17
   Simple example client demonstrating how to connect to MCP servers over HTTP (SSE)

3059. **[rollbar-mcp-server](https://github.com/rollbar/rollbar-mcp-server)** - ⭐ 17
   Pre-release - Model Context Protocol server for Rollbar

3060. **[jiki](https://github.com/teilomillet/jiki)** - ⭐ 17

3061. **[MCP-Development-with-Rust](https://github.com/RustSandbox/MCP-Development-with-Rust)** - ⭐ 17
   This comprehensive learning resource provides two complete tutorials for mastering Model Context Protocol (MCP) development with Rust. From beginner-friendly introductions to production-ready enterprise applications, these tutorials guide you through every aspect of building robust MCP servers.

3062. **[askit](https://github.com/johnrobinsn/askit)** - ⭐ 17
   LLM Function Calling Library and CLI with Support for MCP Servers

3063. **[toolkit-mcp-server](https://github.com/cyanheads/toolkit-mcp-server)** - ⭐ 17
   A Model Context Protocol server providing LLM Agents with system utilities and tools, including IP geolocation, network diagnostics, system monitoring, cryptographic operations, and QR code generation.

3064. **[youtube-mcp-server](https://github.com/0GiS0/youtube-mcp-server)** - ⭐ 17
   Cómo crear MCP Servers y usarlos con GitHub Copilot Chat 🚀💻🤖

3065. **[cmcp](https://github.com/RussellLuo/cmcp)** - ⭐ 17
   A command-line utility for interacting with MCP servers.

3066. **[short-url](https://github.com/fengzhongsen/short-url)** - ⭐ 17
   简单易用的短链接生成工具，完全开源、免费、无需登录，可私有化部署，链接永久有效！

3067. **[it-tools-mcp](https://github.com/wrenchpilot/it-tools-mcp)** - ⭐ 17
   A comprehensive Model Context Protocol (MCP) server that provides access to over 100 IT tools and utilities commonly used by developers, system administrators, and IT professionals. Inspired by https://github.com/CorentinTh/it-tools

3068. **[context-lens](https://github.com/cornelcroi/context-lens)** - ⭐ 17
   Semantic search knowledge base for MCP-enabled AI assistants. Index local files or GitHub repos, query with natural language. Built on LanceDB vector storage. Works with Claude Desktop, Cursor, and other MCP clients.

3069. **[GUARDRAIL](https://github.com/nshkrdotcom/GUARDRAIL)** - ⭐ 17
   GUARDRAIL - MCP Security - Gateway for Unified Access, Resource Delegation, and Risk-Attenuating Information Limits

3070. **[Air-Quality-Trends-Analysis-Project](https://github.com/dyneth02/Air-Quality-Trends-Analysis-Project)** - ⭐ 17
   Full-stack air quality analytics platform built with FastAPI, React, and MySQL. Aggregates multi-source PM2.5/PM10 data, performs multi-city comparison and time-series forecasting (SARIMAX), and integrates an LLM-based planning agent with tiered access, secure APIs, and PDF reporting.

3071. **[MCP-Agent](https://github.com/CursorTouch/MCP-Agent)** - ⭐ 17
   Connect to any MCP servers using agents

3072. **[github-repos-manager-mcp](https://github.com/kurdin/github-repos-manager-mcp)** - ⭐ 17
   GitHub Repos Manager MCP Server that enables your MCP client (e.g., Claude Desktop, Roo Code, etc.) to interact with GitHub repositories using your GitHub personal access token.

3073. **[unity-editor-mcp](https://github.com/ozankasikci/unity-editor-mcp)** - ⭐ 17
   An MCP server and client for LLMs to interact with Unity Projects

3074. **[mcp-server-prometheus](https://github.com/loglmhq/mcp-server-prometheus)** - ⭐ 17
   MCP server for interacting with Prometheus

3075. **[titanmind-whatsapp-mcp](https://github.com/TitanmindAGI/titanmind-whatsapp-mcp)** - ⭐ 17
   A WhatsApp marketing and messaging tool MCP (Model Control Protocol) service using Titanmind. Handles free-form messages (24hr window) and template workflows automatically

3076. **[model-context-protocol-survey](https://github.com/asinghcsu/model-context-protocol-survey)** - ⭐ 17
   Model Context Protocol (MCP)

3077. **[mcp-server-codegraph](https://github.com/CartographAI/mcp-server-codegraph)** - ⭐ 17
   MCP server for graph representation of a codebase

3078. **[mcp-koii](https://github.com/benjaminr/mcp-koii)** - ⭐ 17
   MCP Server for Teenage Engineering EP-133 KO-II

3079. **[context-engineering](https://github.com/timothywarner-org/context-engineering)** - ⭐ 17
   🧠 Stop building AI that forgets. Master MCP (Model Context Protocol) with production-ready semantic memory, hybrid RAG, and the WARNERCO Schematica teaching app. FastMCP + LangGraph + Vector/Graph stores. Your AI assistant's long-term memory starts here.

3080. **[daiv](https://github.com/srtab/daiv)** - ⭐ 17
   Async SWE agents seamlessly integrated on your git platform to automate code issues implementation, reviews, and pipeline repairs.

3081. **[docmole](https://github.com/Vigtu/docmole)** - ⭐ 17
   Dig through any documentation with AI - MCP server for Claude, Cursor, and other AI assistants

3082. **[hasmcp-ce](https://github.com/hasmcp/hasmcp-ce)** - ⭐ 17
   HasMCP Community Edition

3083. **[substack-mcp](https://github.com/marcomoauro/substack-mcp)** - ⭐ 17
   A Model Context Protocol (MCP) Server for Substack enabling LLM clients to interact with Substack's API for automations like creating posts, managing drafts, and more.

3084. **[muxi](https://github.com/ranaroussi/muxi)** - ⭐ 16
   An extensible AI agents framework

3085. **[mcp-email-client](https://github.com/gamalan/mcp-email-client)** - ⭐ 16
   Email Client as MCP Server. Feature: multiple configuration, more than just gmail

3086. **[oneshot](https://github.com/Destiner/oneshot)** - ⭐ 16
   Anthropic MCP client for macOS

3087. **[unity-mcp](https://github.com/wondeks/unity-mcp)** - ⭐ 16
   A Unity MCP server that allows MCP clients like Claude Desktop or Cursor to perform Unity Editor actions.

3088. **[CereBro](https://github.com/rob1997/CereBro)** - ⭐ 16
   A model-agnostic MCP Client-Server for .Net and Unity

3089. **[lite-mcp-client](https://github.com/sligter/lite-mcp-client)** - ⭐ 16
   Lite-MCP-Client是一个基于命令行的轻量级MCP客户端工具

3090. **[EasyMCP](https://github.com/mshojaei77/EasyMCP)** - ⭐ 16
   A beginner-friendly client for the MCP (Model Context Protocol). Connect to SSE, NPX, and UV servers, and integrate with OpenAI for dynamic tool interactions. Perfect for exploring server connections and chat enhancements.

3091. **[google-scholar-mcp](https://github.com/mochow13/google-scholar-mcp)** - ⭐ 16
   An MCP server for Google Scholar written in TypeScript with Streamable HTTP

3092. **[mcp-installer](https://github.com/joobisb/mcp-installer)** - ⭐ 16
   Simplifies the installation and management of MCP (Model Context Protocol) servers across different AI clients.

3093. **[appvector-mcp](https://github.com/Multivariate-AI-Inc/appvector-mcp)** - ⭐ 16
   This MCP server provides programmatic access to AppVector's powerful APIs, enabling you to integrate ASO insights directly into your development and marketing workflows through any MCP Client

3094. **[protocols-io-mcp-server](https://github.com/hqn21/protocols-io-mcp-server)** - ⭐ 16
   An MCP server that enables MCP clients like Claude Desktop to interact with data from protocols.io.

3095. **[mcp-progressive-agentskill](https://github.com/cablate/mcp-progressive-agentskill)** - ⭐ 16
   AgentSkill - Progressive MCP client with three-layer lazy loading. Validates AgentSkills.io pattern for efficient token usage.

3096. **[Agentic-MCP-Skill](https://github.com/cablate/Agentic-MCP-Skill)** - ⭐ 16
   Agentic-MCP, Progressive MCP client with three-layer lazy loading. Validates AgentSkills.io pattern for efficient token usage. Use MCP without pre-install & wasting full-loading

3097. **[mcp-chatbot](https://github.com/mctrinh/mcp-chatbot)** - ⭐ 16
   MCP Chatbot powered by Anthropic Claude. Delivering on‐demand literature search and summarisation for academics and engineers

3098. **[create-mcp](https://github.com/fefergrgrgrg/create-mcp)** - ⭐ 16
   CLI to set up and deploy MCP Servers to Cloudflare Workers in seconds. Just write TypeScript functions to make Cursor MCP tools.

3099. **[pophive-mcp-server](https://github.com/Cicatriiz/pophive-mcp-server)** - ⭐ 16
   *Featured on Claude!* MCP server for accessing near real-time health data from Yale's PopHIVE platform, as well as additional HHS/CDC data

3100. **[fusion-mcp-server](https://github.com/Joe-Spencer/fusion-mcp-server)** - ⭐ 16
   A model context protocol (MCP) server for Autodesk Fusion that provides resources and tools from ADSK to an AI client such as Claude or Cursor.

3101. **[emceepee](https://github.com/eastlondoner/emceepee)** - ⭐ 16
   MCP server to dynamically connect to other MCP servers & exposes the entire MCP protocol via tool calls. Ideal for testing MCPs during development or accessing MCP Server features from clients that do not support notifications, resource templates, prompts or elicitations.

3102. **[arxiv-mcp-server](https://github.com/anuj0456/arxiv-mcp-server)** - ⭐ 16
   MCP server for arXiv.org - Search, analyze, and export academic papers with AI assistants. Features advanced paper discovery, citation analysis, trend tracking, and multi-format exports.

3103. **[videocapture-mcp](https://github.com/13rac1/videocapture-mcp)** - ⭐ 16
   Model Context Protocol (MCP) server to capture images from an OpenCV-compatible webcam or video source

3104. **[rpc-nodes-mcp](https://github.com/chainstacklabs/rpc-nodes-mcp)** - ⭐ 16
   Minimal, fast, and extensible MCP server for interactions with JSON-RPC blockchain nodes

3105. **[aica](https://github.com/dotneet/aica)** - ⭐ 16
   aica(AI Code Analyzer) reviews your code using AI. Supports CLI and GitHub Actions.

3106. **[gumroad-mcp](https://github.com/rmarescu/gumroad-mcp)** - ⭐ 16
   A Model Context Protocol (MCP) server implementation for Gumroad API

3107. **[go-mcp](https://github.com/dstotijn/go-mcp)** - ⭐ 16
   Go library for implementing the Model Context Protocol (MCP).

3108. **[IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server)** - ⭐ 16
   MCP server for Industrial IoT, SCADA and PLC systems. Unifies MQTT sensors, Modbus devices and industrial equipment into a single AI-orchestrable API. Features real-time monitoring, alarms, time-series storage and actuator control.

3109. **[mcp_client](https://github.com/app-appplayer/mcp_client)** - ⭐ 15

3110. **[MCP-Analyzer](https://github.com/klara-research/MCP-Analyzer)** - ⭐ 15
   An MCP server to read MCP logs to debug directly inside the client

3111. **[mistr-agent](https://github.com/itisaevalex/mistr-agent)** - ⭐ 15
   A MCP client that enables Mistral AI models to autonomously execute complex tasks across web and local environments through standardized agentic capabilities.

3112. **[mcp-server](https://github.com/HarperFast/mcp-server)** - ⭐ 15
   An MCP server providing an interface for MCP clients to access data within Harper.

3113. **[sveltekit-mcp-starter](https://github.com/axel-rock/sveltekit-mcp-starter)** - ⭐ 15

3114. **[mcp-this](https://github.com/shane-kercheval/mcp-this)** - ⭐ 15
   mcp-this lets you turn any command-line tool into an MCP tool and create structured prompt templates that any MCP Client (e.g. Claude Desktop) can use. er for any command

3115. **[QCX](https://github.com/QueueLab/QCX)** - ⭐ 15
   Language to Maps

3116. **[django-firebase-mcp](https://github.com/raghavdasila/django-firebase-mcp)** - ⭐ 15
   A production-ready Django app implementing Firebase Model Context Protocol (MCP) server with 14 Firebase tools for AI agents. Features standalone agent, HTTP/stdio transport, LangChain integration, and complete Firebase service coverage (Auth, Firestore, Storage).

3117. **[claude-server](https://github.com/davidteren/claude-server)** - ⭐ 15
   Claude Server is an MCP implementation that enhances Claude's capabilities by providing sophisticated context management across sessions, enabling persistent knowledge organization through hierarchical project contexts and continuous conversation threads stored in a well-structured ~/.claude directory.

3118. **[pinmeto-location-mcp](https://github.com/PinMeTo/pinmeto-location-mcp)** - ⭐ 15
   PinMeTo MCP server that enables users with authorized credentials to unlock their data 

3119. **[grok-faf-mcp](https://github.com/Wolfe-Jam/grok-faf-mcp)** - ⭐ 15
   First MCP server for Grok | FAST⚡️AF • URL-based AI context • Vercel-deployed

3120. **[mcp-server-amazon](https://github.com/rigwild/mcp-server-amazon)** - ⭐ 15
   🛍📦 Unofficial Amazon Model Context Protocol Server (MCP) - Search products and purchase directly from Claude AI! ✨

3121. **[awesome-dxt-mcp](https://github.com/MCPStar/awesome-dxt-mcp)** - ⭐ 15
   🚀 A curated list of awesome Desktop Extensions (DXT) and MCP servers for Claude Desktop. Discover, share, and contribute to the growing ecosystem of AI-powered local tools and automations.

3122. **[npm-search-mcp-server](https://github.com/btwiuse/npm-search-mcp-server)** - ⭐ 15
   MCP server for searching npm packages

3123. **[mcp-client-and-proxy](https://github.com/appsecco/mcp-client-and-proxy)** - ⭐ 15
   A universal MCP client with proxying feature to interact with MCP Servers which support STDIO transport.

3124. **[mcp-server-python-template](https://github.com/sontallive/mcp-server-python-template)** - ⭐ 15
   This template provides a streamlined foundation for building Model Context Protocol (MCP) servers in Python. It's designed to make AI-assisted development of MCP tools easier and more efficient.

3125. **[autowpmcp](https://github.com/Njengah/autowpmcp)** - ⭐ 15
   AutoWP MCP (Model Context Protocol) server connects Claude to WordPress site and allows users to ask Claude to write blog posts and automatically publish them to WordPress sites.

3126. **[mcp-graphql-forge](https://github.com/toolprint/mcp-graphql-forge)** - ⭐ 15
   MCP that can proxy any GraphQL API and expose graphql operations as mcp tools.

3127. **[mcp-tui](https://github.com/msabramo/mcp-tui)** - ⭐ 15
   MCP host app w/ textual user interface, in Python

3128. **[ebay-mcp](https://github.com/YosefHayim/ebay-mcp)** - ⭐ 15
   eBay MCP Server

3129. **[Blender-MCP-Server](https://github.com/poly-mcp/Blender-MCP-Server)** - ⭐ 15
   MCP server addon for Blender - Control Blender via AI agents through 51 powerful tools. Made to be used with PolyMCP for intelligent tool orchestration. Features thread-safe execution, auto-dependency installation, and complete 3D workflow automation.

3130. **[mcp](https://github.com/yandex-cloud/mcp)** - ⭐ 15
   Yandex Cloud MCP Servers

3131. **[mcp-server-unitycatalog](https://github.com/ognis1205/mcp-server-unitycatalog)** - ⭐ 15
   Unity Catalog AI Model Context Protocol Server

3132. **[claude-mcp-scheduler](https://github.com/tonybentley/claude-mcp-scheduler)** - ⭐ 15
   Use Claude API to prompt remote agents on a cron interval but use local MCPs to handle tool calls for context

3133. **[qmt-mcp-server](https://github.com/jm12138/qmt-mcp-server)** - ⭐ 15
   基于 QMT 平台股票行情的 MCP 服务器，用于提供股票市场数据下载和查询的功能。

3134. **[chatgpt-app-typescript-template](https://github.com/pomerium/chatgpt-app-typescript-template)** - ⭐ 15
   ChatGPT app template using Pomerium, OpenAI Apps SDK and Model Context Protocol (MCP), with a Node.js server and React widgets.

3135. **[Frontapp-MCP](https://github.com/zqushair/Frontapp-MCP)** - ⭐ 15
   MCP server and client for Frontapp

3136. **[mcp-gateway](https://github.com/unrelated-ai/mcp-gateway)** - ⭐ 15
   Transform any HTTP endpoint into an MCP server. Aggregate multiple MCP servers, manage configuration profiles, and serve them through a unified gateway with multi-tenant isolation.

3137. **[universal-crypto-mcp](https://github.com/nirholas/universal-crypto-mcp)** - ⭐ 15
   Universal MCP server for AI agents to interact with any* blockchain via natural language and plugins. Supports swaps, bridges, gas, staking, lending, and more across Ethereum, Arbitrum, Base, Polygon, BSC, and testnets. 

3138. **[systemprompt-mcp-core](https://github.com/Ejb503/systemprompt-mcp-core)** - ⭐ 14
   The core MCP extension for Systemprompt MCP multimodal client

3139. **[Open-MCP-Client](https://github.com/GongRzhe/Open-MCP-Client)** - ⭐ 14
   ChatMCP is a powerful command-line chat interface that connects to multiple LLM providers (OpenAI, Anthropic, Groq, etc.) and extends their capabilities with tools using the Model Context Protocol (MCP).

3140. **[signal-mcp-client](https://github.com/piebro/signal-mcp-client)** - ⭐ 14
   An MCP client that uses signal for sending and receiving messages.

3141. **[vite-plugin-mcp-client-tools](https://github.com/atesgoral/vite-plugin-mcp-client-tools)** - ⭐ 14
   Pluggable Vite MCP plugin that brings client-side tools to your existing Vite setup

3142. **[llm-sse-mcp-demo-2025](https://github.com/nlinhvu/llm-sse-mcp-demo-2025)** - ⭐ 14
   This project demonstrates the integration between LLM clients and MCP (Model Context Protocol) servers using Server-Sent Events (SSE) for real-time communication.

3143. **[mcp-bundler](https://github.com/wrtnlabs/mcp-bundler)** - ⭐ 14
   Is the MCP configuration too complicated? You can easily share your own simplified setup!

3144. **[mcp-turso-cloud](https://github.com/spences10/mcp-turso-cloud)** - ⭐ 14
   🗂️ A Model Context Protocol (MCP) server that provides integration with Turso databases for LLMs. This server implements a two-level authentication system to handle both organization-level and database-level operations, making it easy to manage and query Turso databases directly from LLMs.

3145. **[ntfy-mcp-server](https://github.com/cyanheads/ntfy-mcp-server)** - ⭐ 14
   An MCP (Model Context Protocol) server designed to interact with the ntfy push notification service. It enables LLMs and AI agents to send notifications to your devices with extensive customization options.

3146. **[the-academy](https://github.com/im-knots/the-academy)** - ⭐ 14
   A Socratic dialogue engine for AI agents. 

3147. **[mcpterm](https://github.com/dwrtz/mcpterm)** - ⭐ 14
   An MCP tool server that provides stateful, TUI-compatible terminal sessions.

3148. **[work-memory-mcp](https://github.com/moontmsai/work-memory-mcp)** - ⭐ 14
   Never lose context again - persistent memory management system for AI-powered workflows across multiple tools

3149. **[hoot](https://github.com/Portkey-AI/hoot)** - ⭐ 14
   MCP Testing Tool — Like Postman, but for the Model Context Protocol.

3150. **[uk-case-law-mcp-server](https://github.com/georgejeffers/uk-case-law-mcp-server)** - ⭐ 14
   MCP server for UK case law using The National Archives API. Enables LLMs to search, retrieve, and cite UK legal judgments.

3151. **[mcp-server-templates](https://github.com/Data-Everything/mcp-server-templates)** - ⭐ 14
   A flexible platform that provides Docker & Kubernetes backends, a lightweight CLI (mcpt), and client utilities for seamless MCP integration. Spin up servers from templates, route requests through a single endpoint with load balancing, and support both deployed (HTTP) and local (stdio) transports — all with sensible defaults and YAML-based configs.

3152. **[mcp-ipfs](https://github.com/alexbakers/mcp-ipfs)** - ⭐ 14
   🪐 MCP IPFS Server 

3153. **[mcp-client-for-weather-example](https://github.com/a-persimmons/mcp-client-for-weather-example)** - ⭐ 14
   一个MCP客户端实践：实现LLM调用天气MCP服务端查询天气的快速示例

3154. **[deep-research](https://github.com/troyhantech/deep-research)** - ⭐ 14
   A minimalist deep research framework for any OpenAI API compatible LLMs. 

3155. **[hive-crypto-mcp](https://github.com/hive-intel/hive-crypto-mcp)** - ⭐ 14
   Hive Intelligence Crypto MCP | The Ultimate Cryptocurrency MCP for AI Assistants - Unified access to crypto, DeFi, and Web3 analytics 

3156. **[google-mcp](https://github.com/vakharwalad23/google-mcp)** - ⭐ 14
   Collection of Google-native tools (e.g., Gmail, Calendar) for the MCP

3157. **[ultrathink](https://github.com/husniadil/ultrathink)** - ⭐ 14
   MCP server for sequential thinking and complex problem-solving. Built iteratively using itself. Features confidence scoring,   assumption tracking, and multi-session support.

3158. **[mcp-server-subagent](https://github.com/dvcrn/mcp-server-subagent)** - ⭐ 14
   MCP for letting agents delegate tasks to sub-agents (Claude Code, Aider, Q)

3159. **[mcp-server-gemini-pro](https://github.com/gurveeer/mcp-server-gemini-pro)** - ⭐ 14
   A state-of-the-art Model Context Protocol (MCP) server that provides seamless integration with Google's Gemini AI models. This server enables Claude Desktop and other MCP-compatible clients to leverage the full power of Gemini's advanced AI capabilities.

3160. **[skill-to-mcp](https://github.com/biocontext-ai/skill-to-mcp)** - ⭐ 14
   Convert AI Skills (Claude Skills format) to MCP server resources - Part of BioContextAI

3161. **[hass-mcp-server](https://github.com/ganhammar/hass-mcp-server)** - ⭐ 14
   A Home Assistant Custom Component that provides an MCP (Model Context Protocol) server using HTTP transport, allowing AI assistants like Claude to interact with your Home Assistant instance over HTTP

3162. **[cursor-feedback-extension](https://github.com/jianger666/cursor-feedback-extension)** - ⭐ 14
   Save your Cursor monthly quota! Unlimited AI interactions in one conversation via MCP feedback loop.

3163. **[leanmcp-sdk](https://github.com/LeanMCP/leanmcp-sdk)** - ⭐ 14
   TypeScript SDK for building Model Context Protocol servers with built-in support for Auth, Elicitation, and MCP-Apps (including ChatGPT Apps).

3164. **[opentargets-mcp](https://github.com/nickzren/opentargets-mcp)** - ⭐ 14
   MCP server for Open Targets Data

3165. **[spring-ai-mcp-deepseek](https://github.com/firefly0512/spring-ai-mcp-deepseek)** - ⭐ 13
   使用 Spring AI 整合 MCP 服务，包括 MCP server 和 deepseek client

3166. **[llamacppMCPClientDemo](https://github.com/brucepro/llamacppMCPClientDemo)** - ⭐ 13
   standalone react MCP client using SSE

3167. **[sample-multi-tenant-saas-mcp-server](https://github.com/aws-samples/sample-multi-tenant-saas-mcp-server)** - ⭐ 13
   Multi-Tenant remote MCP server with Amazon Cognito and remote client with Amazon Bedrock hosted on AWS

3168. **[mcp-chat-client](https://github.com/Ceeon/mcp-chat-client)** - ⭐ 13
   基于高德地图MCP服务的聊天客户端

3169. **[mcp-client-compatibility](https://github.com/tadata-org/mcp-client-compatibility)** - ⭐ 13

3170. **[mcp-client-laravel](https://github.com/RedberryProducts/mcp-client-laravel)** - ⭐ 13
   Laravel-native client for Model Context Protocol (MCP) servers. Built by Redberry (Diamond-tier Laravel partner). Used by LarAgent and other frameworks to enable AI agent functionality.

3171. **[mcp-web-client](https://github.com/hemanth/mcp-web-client)** - ⭐ 13
   A web-based client for connecting to MCP servers with OAuth support

3172. **[mcp-perplexity-server](https://github.com/PoliTwit1984/mcp-perplexity-server)** - ⭐ 13
   A Model Context Protocol (MCP) server for intelligent code analysis and debugging using Perplexity AI’s API, seamlessly integrated with the Claude desktop client.

3173. **[mcp-more](https://github.com/toosean/mcp-more)** - ⭐ 13
   A modern desktop application for managing Model Context Protocol (MCP) servers.

3174. **[MCP-Manager-GUI](https://github.com/gabrielbacha/MCP-Manager-GUI)** - ⭐ 13
   MCP Toggle is a simple GUI tool to help you manage MCP servers across clients seamlessly.

3175. **[easy-mcp-use](https://github.com/dforel/easy-mcp-use)** - ⭐ 13
   Easy-MCP-Use is the open source TypeScript library to connect any LLM to any MCP server and build custom agents that have tool access, without using closed source or application clients.

3176. **[mcphawk](https://github.com/tech4242/mcphawk)** - ⭐ 13
   MCPHawk is a new Logging & Monitoring solution for Model Context Protocol (MCP) traffic, providing deep visibility into MCP client-server interactions. It started off as a mix between Wireshark and mcpinspector, purpose-built for the MCP ecosystem, and is now slowly turning into something more.

3177. **[mcp-test-client](https://github.com/crazyrabbitLTC/mcp-test-client)** - ⭐ 13
   MCP Test Client is a TypeScript testing utility for Model Context Protocol (MCP) servers.

3178. **[mcp-config-editor](https://github.com/kaichen/mcp-config-editor)** - ⭐ 13
   A simple GUI for managing MCP servers, for easy toggle mcp servers.

3179. **[deep-directory-tree-mcp](https://github.com/andredezzy/deep-directory-tree-mcp)** - ⭐ 13
   Powerful Model Context Protocol (MCP) implementation for visualizing directory structures with real-time updates, configurable depth, and smart exclusions for efficient project navigation

3180. **[mongo-mcp](https://github.com/1RB/mongo-mcp)** - ⭐ 13
   MCP server that provide tools to LLMs such as claude in cursor to interact with MongoDB

3181. **[django-mcp](https://github.com/hyperb1iss/django-mcp)** - ⭐ 13
    Connect Django apps to AI assistants with Model Context Protocol. Simple decorators expose models, admin functions, and custom tools to Claude and other AI assistants.

3182. **[memory-mcp-server](https://github.com/hpkv-io/memory-mcp-server)** - ⭐ 13
   A MCP (Model Context Protocol) server providing long-term memory for LLMs

3183. **[mcp-web-search-tool](https://github.com/gabrimatic/mcp-web-search-tool)** - ⭐ 13
   A MCP server providing real-time web search capabilities to any AI model.

3184. **[jadx-mcp-server](https://github.com/Qtty/jadx-mcp-server)** - ⭐ 13
   A Pure-Java MCP Server for JaDX Android Reverse Engineering Tool

3185. **[mcp-jest](https://github.com/josharsh/mcp-jest)** - ⭐ 13
   Automated testing for Model Context Protocol servers. Ship MCP Servers with confidence.

3186. **[mcpdog](https://github.com/kinhunt/mcpdog)** - ⭐ 13
   🐕 Universal MCP Server Manager - Configure once, manage multiple MCP servers through a single interface. Perfect for Claude   Desktop, Claude Code, Cursor, Gemini CLI & AI assistants. Web dashboard, auto-detection, unified proxy layer.

3187. **[MCP-Platform](https://github.com/Data-Everything/MCP-Platform)** - ⭐ 13
   A flexible platform that provides Docker & Kubernetes backends, a lightweight CLI (mcpt), and client utilities for seamless MCP integration. Spin up servers from templates, route requests through a single endpoint with load balancing, and support both deployed (HTTP) and local (stdio) transports — all with sensible defaults and YAML-based configs

3188. **[mcp-client-langchain-ts](https://github.com/hideya/mcp-client-langchain-ts)** - ⭐ 13
   Simple MCP Client CLI Implementation Using LangChain ReAct Agent / TypeScript

3189. **[mcp-obsidian](https://github.com/Piotr1215/mcp-obsidian)** - ⭐ 13
   simple mcp server for interacting with local obsidian notes

3190. **[local-skills-mcp](https://github.com/kdpa-llc/local-skills-mcp)** - ⭐ 13
   Universal MCP server enabling any LLM or AI agent to utilize expert skills from your local filesystem. Reduces context consumption through lazy loading. Works with Claude, Cline, and any MCP-compatible client.

3191. **[prompt-engineer-mcp-server](https://github.com/hireshBrem/prompt-engineer-mcp-server)** - ⭐ 13
   Write 10x better prompts using Prompt Engineer MCP server.

3192. **[mcp-windows-automation](https://github.com/mukul975/mcp-windows-automation)** - ⭐ 13
   🚀 AI-Powered Windows Automation Server using Model Context Protocol (MCP) | Control Windows apps, automate tasks, and manage systems through natural language commands with Claude, ChatGPT & other AI assistants | 80+ automation tools

3193. **[google-mcp-remote](https://github.com/vakharwalad23/google-mcp-remote)** - ⭐ 13
   Collection of Google-native tools (e.g., Gmail, Calendar) for the MCP

3194. **[mcp_review_code_tool](https://github.com/wenkil/mcp_review_code_tool)** - ⭐ 13
   A code review tool based on Model Context Protocol (MCP) that leverages OpenAI's capabilities for intelligent code analysis and review. | 基于模型上下文协议(MCP)的代码审查工具，利用OpenAI的能力进行智能代码分析和审查。

3195. **[mcp-server](https://github.com/configcat/mcp-server)** - ⭐ 13
   Official ConfigCat Model Context Protocol (MCP) Server 

3196. **[mcp-time](https://github.com/TheoBrigitte/mcp-time)** - ⭐ 13
   MCP (Model Context Protocol) server which provides utilities to work with time and dates, with natural language, multiple formats and timezone convertion capabilities

3197. **[sherpa](https://github.com/CartographAI/sherpa)** - ⭐ 13
   Chat with any codebase with MCP servers in a single command

3198. **[capture-mcp-server](https://github.com/blencorp/capture-mcp-server)** - ⭐ 13
   AI-native Model Context Protocol (MCP) server that integrates SAM.gov, USASpending.gov, and Tango APIs to capture and analyze federal procurement and spending data through natural language queries. Responses include both human-readable text and structured JSON so MCP-compatible clients can consume the data programmatically.

3199. **[mlb-mcp](https://github.com/etweisberg/mlb-mcp)** - ⭐ 13
   MCP server for advanced baseball analytics (statcast, fangraphs, baseball reference, mlb stats API) with client demo 

3200. **[mcp-spotify-player](https://github.com/vsaez/mcp-spotify-player)** - ⭐ 13
   MCP server to manage Spotify from MCP clients

3201. **[predictive-maintenance-mcp](https://github.com/LGDiMaggio/predictive-maintenance-mcp)** - ⭐ 13
   AI-Powered Predictive Maintenance & Fault Diagnosis through Model Context Protocol. An open-source framework for integrating Large Language Models with predictive maintenance and fault diagnosis workflows.

3202. **[teamcity-mcp](https://github.com/Daghis/teamcity-mcp)** - ⭐ 13
   Model Context Protocol (MCP) server for JetBrains TeamCity: control builds, tests, agents and configs from AI coding assistants.

3203. **[codepilot](https://github.com/rohittcodes/codepilot)** - ⭐ 13
   A multi-agent CLI tool powered by Swarms-rs and Composio

3204. **[openwebui-mcp-setup](https://github.com/sonzentherevolution/openwebui-mcp-setup)** - ⭐ 13
    Universal MCPO/MCP bridge for Open Web UI with AI-powered configuration. Automated setup generation, Docker support, beginner-friendly. Any AI assistant can instantly convert MCP configs to   working Open Web UI integrations.

3205. **[mcp-meme-sticky](https://github.com/nkapila6/mcp-meme-sticky)** - ⭐ 13
   Create AI generated memes using MCP Meme Sticky. Can converted generated memes into stickers for Telegram or WhatsApp (WA coming soon).  ✨ no APIs required ✨.

3206. **[llama-nexus](https://github.com/LlamaEdge/llama-nexus)** - ⭐ 12
   A gateway service designed to manage and orchestrate OpenAI-compatible API servers with MCP support.

3207. **[st_rag_mcp](https://github.com/digital-duck/st_rag_mcp)** - ⭐ 12
   MCP streamlit client with RAG support for tool search

3208. **[n8n-coolify-mcp-tools](https://github.com/wrediam/n8n-coolify-mcp-tools)** - ⭐ 12
   This workflow leverages the Community n8n MCP Client and my new Coolify MCP Server to interact with your Coolify infrastructure using MCP (Model Context Protocol). 

3209. **[mcp-server-manager](https://github.com/infinitimeless/mcp-server-manager)** - ⭐ 12
   A tool to create, build, and manage MCP servers for use with Claude and other MCP clients

3210. **[MCP-Client-Server-for-agents](https://github.com/qmatteoq/MCP-Client-Server-for-agents)** - ⭐ 12
   This project demonstrates a Model Context Protocol (MCP) server and client implementation in .NET

3211. **[mcp-safe-run](https://github.com/ithena-one/mcp-safe-run)** - ⭐ 12
   Tired of hardcoding secrets like API keys in your MCP client configuration (e.g., mcp.json, claude_desktop_config.json)? mcp-secure-launcher lets you run your existing MCP servers securely without modifying them.

3212. **[xcf](https://github.com/CodeFreezeAI/xcf)** - ⭐ 12
   Xcode MCP Server xcf is a 100% Swift based allowing you to integrate Xcode with your favorite AI IDE or MCP Client

3213. **[CursorMCPMonitor](https://github.com/willibrandon/CursorMCPMonitor)** - ⭐ 12
   Real-time monitoring tool for Model Context Protocol (MCP) interactions in Cursor AI editor. Track, analyze, and debug AI context exchanges between LLM clients and servers. Supports log rotation, pattern matching, and color-coded event visualization.

3214. **[SchemaPin](https://github.com/ThirdKeyAI/SchemaPin)** - ⭐ 12
   The SchemaPin protocol for cryptographically signing and verifying AI agent tool schemas to prevent supply-chain attacks.

3215. **[Tinvo](https://github.com/imxcstar/Tinvo)** - ⭐ 12
   LLM AI Client based on Blazor. (openai, chatgpt, llama, ollama, onnx, deepseekr1...)

3216. **[signoz-mcp-server](https://github.com/DrDroidLab/signoz-mcp-server)** - ⭐ 12
   Connect your Signoz Instance with Cursor, Claude Desktop or any other MCP Compatible Client

3217. **[gemma-mcp](https://github.com/monatis/gemma-mcp)** - ⭐ 12
   MCP Client for Gemma-3

3218. **[muster](https://github.com/giantswarm/muster)** - ⭐ 12
   MCP tool management and workflow proxy

3219. **[Convert-Markdown-PDF-MCP](https://github.com/seanivore/Convert-Markdown-PDF-MCP)** - ⭐ 12
   Markdown To PDF Conversion MCP

3220. **[vmware-esxi-mcp](https://github.com/uldyssian-sh/vmware-esxi-mcp)** - ⭐ 12
   Professional Model Context Protocol (MCP) server for VMware ESXi hypervisor management. Enterprise-ready solution with secure interfaces for ESXi operations, VM lifecycle management, and infrastructure monitoring.

3221. **[owl-mcp](https://github.com/ai4curation/owl-mcp)** - ⭐ 12
   MCP server for OWL applications

3222. **[porkbun-mcp-server](https://github.com/miraclebakelaser/porkbun-mcp-server)** - ⭐ 12
   MCP server implementation for managing domains, DNS, and SSL via the Porkbun API.

3223. **[proxy-base-agent](https://github.com/TheProxyCompany/proxy-base-agent)** - ⭐ 12
   A stateful agent with 100% reliable tool use. Build custom agents on any LLM with guaranteed state consistency.

3224. **[automagik-tools](https://github.com/namastexlabs/automagik-tools)** - ⭐ 12
   From API to AI in 30 Seconds - Transform any API into an intelligent MCP agent that learns, adapts, and speaks human

3225. **[create-mcp-server-kit](https://github.com/Epi-1120/create-mcp-server-kit)** - ⭐ 12
   Scaffold a production-ready Model Context Protocol (MCP) server in seconds.

3226. **[memory-visualizer](https://github.com/mjherich/memory-visualizer)** - ⭐ 12
   Interactive visualizer for Anthropic's Memory MCP knowledge graphs. Instantly explore, debug, and analyze entities, relations, and observations from memory.json files in the Model Context Protocol.

3227. **[MIST](https://github.com/CLoaKY233/MIST)** - ⭐ 12
   MCP server empowering AI assistants with real-world capabilities: Gmail, Calendar, Tasks, Git integration, and note management. Bridges AI assistants to external services through standardized protocol with secure authentication.

3228. **[mcp-salesforce](https://github.com/AiondaDotCom/mcp-salesforce)** - ⭐ 12
   🚀 Complete MCP (Model Context Protocol) server for Salesforce integration with Claude Desktop. Provides seamless OAuth authentication, universal CRUD operations on any Salesforce object.

3229. **[llms-txt-generator](https://github.com/aircodelabs/llms-txt-generator)** - ⭐ 12
   The ultimate AI-powered generator for llms.txt and llms-full.txt files. 

3230. **[ckan-mcp-server](https://github.com/ondics/ckan-mcp-server)** - ⭐ 12
   A Model Context Protocol (MCP) server for the CKAN API that enables browsing and managing CKAN data portals through MCP-compatible clients.

3231. **[claude_autoapprove](https://github.com/PyneSys/claude_autoapprove)** - ⭐ 12
   Autoapprove support for claude

3232. **[gsd-task-manager](https://github.com/vscarpenter/gsd-task-manager)** - ⭐ 12
   Stop juggling, start finishing. GSD Task Manager makes it easy to sort your to-dos into what’s urgent and what’s important, so you can finally get stuff done without burning out. It’s simple, visual, and works entirely offline.

3233. **[vector_mcp](https://github.com/sergiobayona/vector_mcp)** - ⭐ 12
   A server implementation for the Model Context Protocol (MCP) in Ruby.

3234. **[local-mcp-gateway](https://github.com/DXHeroes/local-mcp-gateway)** - ⭐ 12
   Aggregate multiple MCP servers into a single endpoint with web UI, OAuth 2.1, and profile-based tool management

3235. **[ia-na-pratica](https://github.com/Code4Delphi/ia-na-pratica)** - ⭐ 12
   IA na Prática: LLM, RAG, MCP, Agents, Function Calling, Multimodal, TTS/STT e mais

3236. **[RAG-MCP](https://github.com/cr21/RAG-MCP)** - ⭐ 12
   Simple RAG implementation from scratch using MCP, focusing on Perception, Memory, Decision and Action

3237. **[PackageFlow](https://github.com/runkids/PackageFlow)** - ⭐ 12
   A visual DevOps hub for npm scripts, Git, workflows, and deploy — controllable by AI via MCP.

3238. **[ggMCP4VSCode](https://github.com/n2ns/ggMCP4VSCode)** - ⭐ 12
   Google Gemini Model Context Protocol (MCP) Client for VS Code. Connect AI assistants to local context & tools.

3239. **[mcp-delphi](https://github.com/flydev-fr/mcp-delphi)** - ⭐ 12
   Delphi and Lazarus/FPC MCP server: build/clean pascal projects via MCP tools.

3240. **[pentest-mcp-server](https://github.com/LayeSec006/pentest-mcp-server)** - ⭐ 12
   MCP server for penetration testing

3241. **[mcp.zig](https://github.com/muhammad-fiaz/mcp.zig)** - ⭐ 12
   A comprehensive Model Context Protocol (MCP) library for Zig — bringing MCP support to the Zig ecosystem.

3242. **[SQL_MCP_Server](https://github.com/pawankumar94/SQL_MCP_Server)** - ⭐ 12
   SQLGenius is an AI-powered SQL assistant that converts natural language to SQL queries using Vertex AI's Gemini Pro. Built with MCP and Streamlit, it provides an intuitive interface for BigQuery data exploration with real-time visualization and schema management.

3243. **[nestjs-mcp](https://github.com/orbit-codes/nestjs-mcp)** - ⭐ 12
   An opinionated MCP module for NestJS

3244. **[snowflake-mcp-server](https://github.com/dynamike/snowflake-mcp-server)** - ⭐ 12
   MCP Server for connecting to Snowflake with read-only questions

3245. **[mcp-server-kintone](https://github.com/macrat/mcp-server-kintone)** - ⭐ 12
   MCP server for kintone

3246. **[mcp-server-webscan](https://github.com/bsmi021/mcp-server-webscan)** - ⭐ 12
   A Model Context Protocol (MCP) server for web content scanning and analysis. This server provides tools for fetching, analyzing, and extracting information from web pages.

3247. **[sarvam-mcp-server](https://github.com/Shobhit-Nagpal/sarvam-mcp-server)** - ⭐ 12
   talk to sarvam APIs directly, without code.

3248. **[swift-context-protocol](https://github.com/1amageek/swift-context-protocol)** - ⭐ 12
   swift-context-protocol is a Swift-based implementation of the Model Context Protocol (MCP) for AI contexts. It leverages Swift’s distributed actor model to enable type-safe, asynchronous remote invocation of tools, resources, and prompts.

3249. **[mcp-server-weather-js](https://github.com/hideya/mcp-server-weather-js)** - ⭐ 12
   Simple Weather MCP Server Example

3250. **[agent-identity-protocol](https://github.com/ArangoGutierrez/agent-identity-protocol)** - ⭐ 12
   Agent Identity Protocol - Zero-trust security layer for AI agents. Policy enforcement proxy for MCP with Human-in-the-Loop approval, DLP scanning, and audit logging.

3251. **[md2confluence-mcp](https://github.com/Gyeom/md2confluence-mcp)** - ⭐ 12
   MCP server to upload Markdown to Confluence. Auto-converts Mermaid diagrams, code blocks, images, and tables.

3252. **[gtm-mcp-server](https://github.com/paolobietolini/gtm-mcp-server)** - ⭐ 12
   An MCP server for Google Tag Manager. Connect it to your LLM, authenticate once, and start managing GTM through natural language.

3253. **[context-kit](https://github.com/eyalzh/context-kit)** - ⭐ 11
   A CLI tool and MCP client, used to create spec files for AI coding agents with context baked in

3254. **[mcp_client_rust](https://github.com/darinkishore/mcp_client_rust)** - ⭐ 11

3255. **[mcp-client](https://github.com/EuclideanAI/mcp-client)** - ⭐ 11
   A custom Model Context Protocol (MCP) Client interface with integrated LLM agent chat capabilities built with Next.js and the Vercel AI SDK

3256. **[MCP_Client](https://github.com/andrewdeng318/MCP_Client)** - ⭐ 11

3257. **[trebuchet](https://github.com/fuzzball-muck/trebuchet)** - ⭐ 11
   A MUD/MUCK/MUSH chat client with MCP/GUI support.

3258. **[mcp-wikipedia](https://github.com/algonacci/mcp-wikipedia)** - ⭐ 11
   MCP server to give client the ability to access Wikipedia pages

3259. **[systemprompt-mcp-gmail](https://github.com/Ejb503/systemprompt-mcp-gmail)** - ⭐ 11
   A specialized Model Context Protocol (MCP) server that enables you to search, read, delete and send emails from your Gmail account, leveraging an AI Agent to help with each operation.  Optimized for Systemprompt MCP Voice client.

3260. **[mcp-client-app](https://github.com/RegiByte/mcp-client-app)** - ⭐ 11
   A mcp client chat application built for learning purposes

3261. **[mcp-browser-automation](https://github.com/hrmeetsingh/mcp-browser-automation)** - ⭐ 11
   Model Context Protocol based AI Agent that runs a browser from Claude desktop

3262. **[simple-nodejs-mcp-client](https://github.com/sawa-zen/simple-nodejs-mcp-client)** - ⭐ 11
   This is a study repository for implementing a Model Context Protocol (MCP) client. It features a simple interactive MCP client implemented in Node.js.

3263. **[goldrush-mcp-server](https://github.com/covalenthq/goldrush-mcp-server)** - ⭐ 11
   This project provides a MCP (Model Context Protocol) server that exposes Covalent's GoldRush APIs as MCP resources and tools. It is implemented in TypeScript using @modelcontextprotocol/sdk and @covalenthq/client-sdk.

3264. **[langchain-mcp-tools-ts-usage](https://github.com/hideya/langchain-mcp-tools-ts-usage)** - ⭐ 11
   MCP Tools Usage From LangChain ReAct Agent / Example in TypeScript

3265. **[mcp-chat-widget](https://github.com/aimdoc-ai/mcp-chat-widget)** - ⭐ 11
   Configure, host and embed MCP-enabled chat widgets for your website or product. Lightweight and extensible Chatbase clone to remotely configure and embed your agents anywhere.

3266. **[oauth-callback](https://github.com/kriasoft/oauth-callback)** - ⭐ 11
   Lightweight OAuth 2.0 authorization code capture for CLI tools & desktop   apps. Works with Node.js, Deno, Bun. MCP SDK ready.

3267. **[semantictool](https://github.com/promptmesh/semantictool)** - ⭐ 11
   tool management service for performing vector tool calling at scale.

3268. **[davinci-mcp-professional](https://github.com/Positronikal/davinci-mcp-professional)** - ⭐ 11
   An enterprise-grade MCP server that exposes the full functionality of DaVinci Resolve and DaVinci Resolve Studio (through version 20) to either Claude Desktop or Cursor MCP clients. Fully configured and tested as a Claude Desktop Extension making installation as easy as clicking a button. Supports both Windows and Macintosh.

3269. **[mcpconnect](https://github.com/rocket-connect/mcpconnect)** - ⭐ 11
   Inspect and debug Model Context Protocol servers directly in your browser.

3270. **[osmmcp](https://github.com/NERVsystems/osmmcp)** - ⭐ 11
   OpenStreetMap MCP server providing precision geospatial tools for LLMs via Model Context Protocol. Features geocoding, routing, nearby places, neighborhood analysis, EV charging stations, and more.

3271. **[locust-mcp-server](https://github.com/QAInsights/locust-mcp-server)** - ⭐ 11
   A Model Context Protocol (MCP) server implementation for running Locust load tests. This server enables seamless integration of Locust load testing capabilities with AI-powered development environments.

3272. **[scorable-mcp](https://github.com/root-signals/scorable-mcp)** - ⭐ 11
   MCP for Scorable Evaluation Platform

3273. **[mcp-boilerplate](https://github.com/iamsrikanthnani/mcp-boilerplate)** - ⭐ 11
   A powerful, production-ready MCP server implementing the Model Context Protocol with robust SSE transport, built-in tools, and comprehensive error handling. Seamlessly connect AI models to data sources with enterprise-grade stability and performance.

3274. **[emcp](https://github.com/joeymeere/emcp)** - ⭐ 11
   A framework for building simple MCP servers with custom middleware

3275. **[local-history-mcp](https://github.com/xxczaki/local-history-mcp)** - ⭐ 11
   MCP server for accessing VS Code/Cursor's Local History

3276. **[puppeteer-mcp-server](https://github.com/sultannaufal/puppeteer-mcp-server)** - ⭐ 11
   Self-hosted Puppeteer MCP server with remote SSE access, API key authentication, and Docker deployment. Complete tool suite for browser automation via Model Context Protocol.

3277. **[temple-bridge](https://github.com/templetwo/temple-bridge)** - ⭐ 11
   The Sovereign Stack: MCP server binding local AI capabilities with governance protocols. 100% local operation with memory, conscience, and recursive observation.

3278. **[programmatic-tool-calling-ai-sdk](https://github.com/cameronking4/programmatic-tool-calling-ai-sdk)** - ⭐ 11
   ⚡ Cut LLM inference costs 80% with Programmatic Tool Calling. Instead of N tool call round-trips, generate JavaScript to orchestrate tools in Vercel Sandbox. Supports Anthropic, OpenAI, 100+ models via AI Gateway. Novel MCP Bridge for external service integration.

3279. **[_b00t_](https://github.com/elasticdotventures/_b00t_)** - ⭐ 11
   🥾 _b00t_:  brians dotfiles aka state of the art agentic tooling & context initialization

3280. **[dx-toolkit](https://github.com/youdotcom-oss/dx-toolkit)** - ⭐ 11
   Open-source toolkit enabling developers to integrate You.com's AI capabilities into their workflows

3281. **[openalgo-mcp](https://github.com/marketcalls/openalgo-mcp)** - ⭐ 11
   Documentation

3282. **[taiga-ui-mcp](https://github.com/taiga-family/taiga-ui-mcp)** - ⭐ 11
   Taiga UI MCP server providing documentation search and scaffolding tools.

3283. **[inspector](https://github.com/mcp-use/inspector)** - ⭐ 11
   Modern MCP Inspector for remote mcp servers with support for Apps SDK

3284. **[mcp-add](https://github.com/paoloricciuti/mcp-add)** - ⭐ 11
   Universal cli to add an MCP server to a variety of clients

3285. **[AgentStack](https://github.com/ssdeanx/AgentStack)** - ⭐ 11
   AgentStack is a production-grade multi-agent framework built on Mastra, delivering 50+ enterprise tools, 25+ specialized agents, and A2A/MCP orchestration for scalable AI systems. Focuses on financial intelligence, RAG pipelines, observability, and secure governance.

3286. **[ChatSpatial](https://github.com/cafferychen777/ChatSpatial)** - ⭐ 11
   🧬 Analyze spatial transcriptomics data through natural language conversation. Stop writing code, start having conversations with your data. MCP server for Claude Desktop and other LLM agents.

3287. **[outlook-mcp](https://github.com/XenoXilus/outlook-mcp)** - ⭐ 11
   MCP server for Microsoft Office 365 Outlook – email, calendar & SharePoint integration for Claude, ChatGPT, and AI assistants via Microsoft Graph API

3288. **[companies-house-mcp](https://github.com/stefanoamorelli/companies-house-mcp)** - ⭐ 11
   🇬🇧🏦 MCP server for UK Companies House API - Search companies, retrieve detailed information, filing history, officers, and charges data through the Model Context Protocol

3289. **[garmin-connect-mcp](https://github.com/eddmann/garmin-connect-mcp)** - ⭐ 11
   MCP server enabling LLMs to interact with Garmin Connect - activities, health metrics, sleep data, and training analysis

3290. **[File-Organizer-MCP](https://github.com/kridaydave/File-Organizer-MCP)** - ⭐ 11
   This MCP server will organize your files using connections to MCP using clients like Claude, Cursor and Gemini Cli

3291. **[slack-mcp-server](https://github.com/jtalk22/slack-mcp-server)** - ⭐ 11
   Full Slack access for Claude - DMs, channels, search. No OAuth. No admin approval. Just works.

3292. **[dav-mcp](https://github.com/PhilflowIO/dav-mcp)** - ⭐ 11
   Transform AI agents into orchestrating assistants managing calendars, contacts, and tasks

3293. **[lyra-tool-discovery](https://github.com/nirholas/lyra-tool-discovery)** - ⭐ 11
   AI powered automation toolkit which acts as an agent that discovers MCP servers for you. Point it at GitHub/npm/configure your own discovery, let GPT or Claude analyze the API or MCP or any tool, get ready-to-ship plugin configs. Zero manual work.

3294. **[claude-context-local](https://github.com/MikeO-AI/claude-context-local)** - ⭐ 10
   🔒 Privacy-first MCP server for Claude using PostgreSQL + Ollama. Local alternative to cloud-based code context with full data sovereignty. No API keys, no external calls, 100% local.

3295. **[langchain-mcp-client](https://github.com/datalayer/langchain-mcp-client)** - ⭐ 10
   🦜🔗 LangChain Model Context Protocol (MCP) Client

3296. **[mcp-client-langchain-py](https://github.com/hideya/mcp-client-langchain-py)** - ⭐ 10
   Simple MCP Client CLI Implementation Using LangChain ReAct Agent / Python

3297. **[mcp_client_openai](https://github.com/liangpn/mcp_client_openai)** - ⭐ 10
   适配Openai SDK构建MCP Client

3298. **[mcp-serverman](https://github.com/benhaotang/mcp-serverman)** - ⭐ 10
   a cli/mcp server tool for managing mcp server json config file with version control, profiles and multi-client support

3299. **[py-mcp-sse](https://github.com/jayliangdl/py-mcp-sse)** - ⭐ 10
   MCP Client 与 MCP Server基于SSE方式的样例实现（Python版本）

3300. **[mcpkit](https://github.com/cybertheory/mcpkit)** - ⭐ 10
   Easy to use Official MCP Registry Client UI. npx @cybertheory/mcpkit

3301. **[AIFoundry-MCPConnector-FabricGraphQL](https://github.com/LazaUK/AIFoundry-MCPConnector-FabricGraphQL)** - ⭐ 10
   MCP Client and Server apps to demo integration of Azure OpenAI-based AI agent with a Data Warehouse, exposed through GraphQL in Microsoft Fabric.

3302. **[server](https://github.com/mcpfinder/server)** - ⭐ 10
   MCPfinder 🔧🤖 is a service that enables LLMs, running through client applications that support the MCP protocol, to dynamically discover and access new tools, features, and capabilities. When a user requests functionality the AI doesn’t have, it can simply ask MCP Finder to locate relevant MCP servers, expanding its toolset in real time.

3303. **[kanboard-mcp](https://github.com/ChristianJStarr/kanboard-mcp)** - ⭐ 10
   Transform your Kanboard.org into an AI-powered project management powerhouse! This plugin enables complete control over Kanboard through the Model Context Protocol (MCP), allowing AI assistants like Cursor, Claude, and other MCP clients to manage your projects through natural language commands.

3304. **[emotion_ai](https://github.com/angrysky56/emotion_ai)** - ⭐ 10
   The Aura Emotion AI system has chroma with a local embedding model, memvid qr code mp4 infinite memory, brainwave and neurochemical simulations, sociobiological reasoning, autonomous subsystem processing with a Gemini flash model so the main model is less taxed, is a MCP client with adaptive tool learning and MCP server. 

3305. **[mcp-express-adapter](https://github.com/Moe03/mcp-express-adapter)** - ⭐ 10
   Run multiple MCP clients on a NodeJS Express server (adapter/middleware)

3306. **[mcp-trace](https://github.com/zabirauf/mcp-trace)** - ⭐ 10
   A TUI to probe the calls between MCP client and server

3307. **[mcp-server-blog](https://github.com/portal-labs-infrastructure/mcp-server-blog)** - ⭐ 10
   Example of a MCP implementation using TypeScript and OAuth.

3308. **[unity-mcp-template](https://github.com/dunward/unity-mcp-template)** - ⭐ 10
   Simple template project for controlling Unity via MCP

3309. **[awesome-mcp-hardware](https://github.com/beriberikix/awesome-mcp-hardware)** - ⭐ 10
   Awesome list of MCP servers for interacting with hardware and the physical world.

3310. **[polaris](https://github.com/octu0/polaris)** - ⭐ 10
   Distributed AI Agent Framework

3311. **[mcp-agent-proxy](https://github.com/mashh-lab/mcp-agent-proxy)** - ⭐ 10
   An MCP server that exposes local and remote agents across different servers as MCP tools.

3312. **[amazon-seller-mcp](https://github.com/enginterzi/amazon-seller-mcp)** - ⭐ 10
   Transform Your Amazon Business with AI - The first Model Context Protocol (MCP) client that seamlessly connects Claude and other AI agents to Amazon's Selling Partner API, enabling intelligent automation of your entire seller workflow from inventory management to listing optimization.

3313. **[auto-mcp-client](https://github.com/down-to-earth1994/auto-mcp-client)** - ⭐ 10
   基于Spring AI 封装了 mcp-client 服务，目的使web网页智能体也能通过 stdio 和 HTTP SSE（Server-Sent Events） 与 MCP Server 进行交互。项目实现了自动化的连接管理机制，包括自动初始化连接、健康检查、超时关闭以及链接复用等功能

3314. **[mcp-kit](https://github.com/shaharia-lab/mcp-kit)** - ⭐ 10
   MCP (Model Context Protocol) Kit for Go - A Complete MCP solutions for ready to use

3315. **[CodeCompass](https://github.com/alvinveroy/CodeCompass)** - ⭐ 10
   CodeCompass: AI-powered Vibe Coding with MCP. Connects Git repositories to AI assistants like Claude, using Ollama for privacy or OpenAI for cloud. Integrates with VSCode, Cursor, and more.

3316. **[french-tax-mcp](https://github.com/cornelcroi/french-tax-mcp)** - ⭐ 10
   MCP server for French tax calculations and information - enables AI assistants to provide accurate French tax guidance

3317. **[springboot-ai-mcp-example](https://github.com/duongminhhieu/springboot-ai-mcp-example)** - ⭐ 10
   Example Spring AI Model Context Protocol (MCP)

3318. **[mcp-space](https://github.com/tharuneshwar-s/mcp-space)** - ⭐ 10
   MCP Space is a no-code platform for building and deploying AI tools using the Model Context Protocol (MCP). Create powerful AI agents through an intuitive chat interface without writing code, then deploy with one click to Cloudflare Workers. Combines a Next.js frontend with Google ADK backend for a seamless AI development experience.

3319. **[mode-manager-mcp](https://github.com/NiclasOlofsson/mode-manager-mcp)** - ⭐ 10
   MCP Memory Agent Server - A VS Code chatmode and instruction manager with library integration

3320. **[mcp-reporter](https://github.com/cyanheads/mcp-reporter)** - ⭐ 10
   mcp-reporter is a streamlined utility that generates comprehensive capability reports for Model Context Protocol servers, empowering developers to easily understand available functionality across their MCP servers ecosystem for both documentation and integration into other tools.

3321. **[mcp-starter-template-ts](https://github.com/onamfc/mcp-starter-template-ts)** - ⭐ 10
   TypeScript starter template for building Model Context Protocol (MCP) servers, designed to help developers create secure and robust AI-agent-compatible services.

3322. **[prometheus-protocol](https://github.com/prometheus-protocol/prometheus-protocol)** - ⭐ 10
   The trust layer for the open agentic web—giving AI agents a passport, a bank account, and a trusted marketplace to securely interact with the world.

3323. **[rec-us-mcp-server](https://github.com/elizabethsiegle/rec-us-mcp-server)** - ⭐ 10
   Book a San Francisco tennis court via MCP server w/ auth

3324. **[mcp-demo](https://github.com/sshh12/mcp-demo)** - ⭐ 10
   URL MCP is a proof of concept stateless MCP server builder that allows users to build MCP servers without writing or hosting code. It's intended for protocol and security experimentation rather than for building real world MCP integrations.

3325. **[AgentX-mcp-servers](https://github.com/AgentX-ai/AgentX-mcp-servers)** - ⭐ 10
   List of open sourced MCP servers. MIT license. Managed by AgentX with love.

3326. **[mcp-tradovate](https://github.com/0xjmp/mcp-tradovate)** - ⭐ 10
   MCP server for the Tradovate platform

3327. **[mcp-claude-hackernews](https://github.com/imprvhub/mcp-claude-hackernews)** - ⭐ 10
   An integration that allows Claude Desktop to interact with Hacker News using the Model Context Protocol (MCP).

3328. **[glasses-mcp](https://github.com/gourraguis/glasses-mcp)** - ⭐ 10
   Glasses MCP is a simple MCP server that lets your AI agent see and capture the web 👓

3329. **[ObsidianMCPServer](https://github.com/otaviocc/ObsidianMCPServer)** - ⭐ 10
   A Model Context Protocol (MCP) server that enables AI assistants to interact with your Obsidian vault 

3330. **[mcp-sys-bridge](https://github.com/leynier/mcp-sys-bridge)** - ⭐ 10
   An implementation of the Model Context Protocol (MCP), acting as a simple bridge to native OS functionalities like clipboard management and URL handling.

3331. **[sec-edgar-agentkit](https://github.com/stefanoamorelli/sec-edgar-agentkit)** - ⭐ 10
   AI agent toolkit for accessing and analyzing SEC EDGAR filing data. Build intelligent agents with LangChain, MCP-use, Gradio, Dify, and smolagents to analyze financial statements, insider trading, and company filings.

3332. **[druid-mcp-server](https://github.com/iunera/druid-mcp-server)** - ⭐ 10
   A comprehensive Model Context Protocol (MCP) server for Apache Druid that provides extensive tools, resources, and AI-assisted prompts for managing and analyzing Druid clusters. Built with Spring Boot and Spring AI, this server enables seamless integration between AI assistants and Apache Druid through standardized MCP protocol.

3333. **[context-engineering-mcp](https://github.com/bralca/context-engineering-mcp)** - ⭐ 10
   Context Engineering is a MCP server that gives AI agents perfect understanding of your codebase. Eliminates context loss, reduces token usage, and generates comprehensive feature plans in minutes. Compatible with Cursor, Claude Code, and VS Code.

3334. **[nautobot_mcp](https://github.com/kvncampos/nautobot_mcp)** - ⭐ 10
   Nautobot Model Context Protocol (MCP) Server - Contains STDIO and HTTP Deployments with Embedding Search and RAG.

3335. **[mcp-client-gen](https://github.com/kriasoft/mcp-client-gen)** - ⭐ 10
   Turn any MCP server into a type-safe TypeScript SDK in seconds - with    OAuth 2.1 and multi-provider support

3336. **[mcp-sqlite-server](https://github.com/prayanks/mcp-sqlite-server)** - ⭐ 10
   These are MCP server implementations for accessing a SQLite database in your MCP client. There is both a SDIO and a SSE implementation.

3337. **[mcp_documents_reader](https://github.com/xt765/mcp_documents_reader)** - ⭐ 10
   Model Context Protocol (MCP) server exposes tools to read multiple document types including DOCX, PDF, Excel, and TXT. This has been tested on Trae Desktop.

3338. **[langgraph-mcp-dataanalysis](https://github.com/gongwon-nayeon/langgraph-mcp-dataanalysis)** - ⭐ 10
   DataAnalysis Agent using LangGraph & MCP server and client

3339. **[claude-faf-mcp](https://github.com/Wolfe-Jam/claude-faf-mcp)** - ⭐ 10
   Anthropic-approved MCP Server | Persistent AI Context | IANA-registered .faf format

3340. **[mcp-go](https://github.com/XiaoConstantine/mcp-go)** - ⭐ 10
   Golang impl of mcp protocol

3341. **[mcpet](https://github.com/shreyaskarnik/mcpet)** - ⭐ 10
   This is a TypeScript-based Model Context Protocol (MCP) server that implements a virtual pet simulation system. It demonstrates core MCP concepts by providing tools for pet care and interaction.

3342. **[miniflux-mcp](https://github.com/tssujt/miniflux-mcp)** - ⭐ 10
   A Model Context Protocol (MCP) server for interacting with Miniflux RSS reader.

3343. **[rigour](https://github.com/rigour-labs/rigour)** - ⭐ 10
   Local-first quality gate + fix-loop controller for AI coding agents (CLI + MCP).

3344. **[cv-resume-builder-mcp](https://github.com/eyaab/cv-resume-builder-mcp)** - ⭐ 10
   AI-powered CV and resume builder using Model Context Protocol. Automatically sync your achievements from Jira, Credly, LinkedIn, and git. Keep your CV always up-to-date.

3345. **[pentesting-cyber-mcp](https://github.com/hackersatyamrastogi/pentesting-cyber-mcp)** - ⭐ 10
   🔐 50+ MCP Security Servers for AI-Powered Pentesting | Integrate Nmap, Burp Suite, Nuclei, Shodan, BloodHound, Semgrep, Trivy | Model Context Protocol for Cybersecurity

3346. **[mcp-spring-ai-mcp-client](https://github.com/chaozai0304/mcp-spring-ai-mcp-client)** - ⭐ 10
   使用java实现mcp client了解底层的调用机制，demo示例

3347. **[mcp-optimizer](https://github.com/StacklokLabs/mcp-optimizer)** - ⭐ 10
   MCP server that acts as an intelligent intermediary between AI clients and multiple MCP servers

3348. **[github-to-mcp](https://github.com/nirholas/github-to-mcp)** - ⭐ 10
   Convert GitHub repositories to MCP servers automatically. Extract tools from OpenAPI, GraphQL & REST APIs for Claude Desktop, Cursor, Windsurf, Cline & VS Code. AI-powered code generation creates type-safe TypeScript/Python MCP servers. Zero config setup - just paste a repo URL. Built for AI assistants & LLM tool integration.

3349. **[awesome-mcp](https://github.com/timunbasah3/awesome-mcp)** - ⭐ 10
   🚀 Discover and explore a curated list of MCP servers, tools, and resources for AI assistants, enhancing your development and productivity.

3350. **[biomed-agent](https://github.com/nickzren/biomed-agent)** - ⭐ 10
   Connecting AI agent to biomedical data

### MCP Clients

*MCP client applications that connect to MCP servers*

1. **[chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)** - ⭐ 41,151
   CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企业微信应用、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

2. **[bytebot](https://github.com/bytebot-ai/bytebot)** - ⭐ 10,378
   Bytebot is a self-hosted AI desktop agent that automates computer tasks through natural language commands, operating within a containerized Linux desktop environment.

3. **[valuecell](https://github.com/ValueCell-ai/valuecell)** - ⭐ 9,025
   ValueCell is a community-driven, multi-agent platform for financial applications.

4. **[deepchat](https://github.com/ThinkInAIXYZ/deepchat)** - ⭐ 5,482
   🐬DeepChat - A smart assistant that connects powerful AI to your personal world

5. **[ruoyi-ai](https://github.com/ageerle/ruoyi-ai)** - ⭐ 4,755
   RuoYi AI 是一个全栈式 AI 开发平台，旨在帮助开发者快速构建和部署个性化的 AI 应用。

6. **[koog](https://github.com/JetBrains/koog)** - ⭐ 3,706
   Koog is the official Kotlin framework for building predictable, fault-tolerant and enterprise-ready AI agents across all platforms – from backend services to Android and iOS, JVM, and even in-browser environments. Koog is based on our AI products expertise and provides proven solutions for complex LLM and AI problems

7. **[shippie](https://github.com/mattzcarey/shippie)** - ⭐ 2,327
   extendable code review and QA agent 🚢

8. **[open-mcp-client](https://github.com/CopilotKit/open-mcp-client)** - ⭐ 1,642

9. **[supermemory-mcp](https://github.com/supermemoryai/supermemory-mcp)** - ⭐ 1,607
   Your memories are in ChatGPT... But nowhere else. Universal Memory MCP makes your memories available to every single LLM. No logins or paywall. One command to set it up.

10. **[openinference](https://github.com/Arize-ai/openinference)** - ⭐ 846
   OpenTelemetry Instrumentation for AI Observability

11. **[VectorCode](https://github.com/Davidyz/VectorCode)** - ⭐ 791
   A code repository indexing tool to supercharge your LLM experience.

12. **[HyperChat](https://github.com/BigSweetPotatoStudio/HyperChat)** - ⭐ 709
   HyperChat is a Chat client that strives for openness, utilizing APIs from various LLMs to achieve the best Chat experience, as well as implementing productivity tools through the MCP protocol.

13. **[flow-like](https://github.com/TM9657/flow-like)** - ⭐ 587
   Flow-Like: Strongly Typed Enterprise Scale Workflows. Built for scalability, speed, seamless AI integration and rich customization.

14. **[GalwayBus](https://github.com/joreilly/GalwayBus)** - ⭐ 581
   Galway Bus Kotlin Multiplatform project using Jetpack Compose and SwiftUI 

15. **[caswaf](https://github.com/casbin/caswaf)** - ⭐ 556
   Casbin AI & MCP security gateway for HTTP, online demo: https://door.caswaf.com

16. **[fleur](https://github.com/fleuristes/fleur)** - ⭐ 532
   The easiest way to discover and install MCPs

17. **[a2a-x402](https://github.com/google-agentic-commerce/a2a-x402)** - ⭐ 446
   The A2A x402 Extension brings cryptocurrency payments to the Agent-to-Agent (A2A) protocol, enabling agents to monetize their services through on-chain payments. This extension revives the spirit of HTTP 402 "Payment Required" for the decentralized agent ecosystem.

18. **[PlanExe](https://github.com/PlanExeOrg/PlanExe)** - ⭐ 334
   Create a plan from a description in minutes

19. **[self-dify](https://github.com/datawhalechina/self-dify)** - ⭐ 327
   本教程将全面指导你如何快速搭建自己的AI应用环境，从Docker桌面版的安装与配置开始，到本地部署Dify并自定义AI助手功能，让你轻松实现“猜病例”、“甜蜜哄人”、“新生入学指南”、“小红书读书卡片”与“面试宝典”等多种特色AI应用。并教会你从基础智能体到使用工作流，再到知识库、DeepResearch、数据库、MCP、复杂任务编排等高阶任务，由浅到深的学习掌握基于dify的大模型应用开发。

20. **[mcp-toolbox-sdk-python](https://github.com/googleapis/mcp-toolbox-sdk-python)** - ⭐ 157
   Python SDK for interacting with the MCP Toolbox for Databases. 

21. **[web-hacker](https://github.com/VectorlyApp/web-hacker)** - ⭐ 153
   Reverse engineer web apps

22. **[terminal-ai](https://github.com/dwmkerr/terminal-ai)** - ⭐ 150
   Unopinionated AI for the Shell. A lightweight AI CLI for scripts, pipelines, and automation, with a universal client for MCP, A2A, and other AI protocols. .

23. **[ai](https://github.com/WordPress/ai)** - ⭐ 121
   Demonstrate and deliver AI features by combining all AI Building Blocks into a unified WordPress experience.

24. **[airbyte-agent-connectors](https://github.com/airbytehq/airbyte-agent-connectors)** - ⭐ 102
   🐙 Drop-in tools that give AI agents reliable, permission-aware access to external systems.

25. **[FlowUpdater](https://github.com/FlowArg/FlowUpdater)** - ⭐ 98
   The free and open source solution to update Minecraft.

26. **[mcp-manager](https://github.com/petiky/mcp-manager)** - ⭐ 96
   This is a visual client tool used to manage MCP (Model Context Protocol). With this tool, you can easily manage and operate the MCP environment without manually performing complex command-line operations.

27. **[ai-microcore](https://github.com/Nayjest/ai-microcore)** - ⭐ 91
   A handy lib for smooth interaction with large language models (LLMs) and crafting AI apps.

28. **[hm_editor](https://github.com/huimeicloud/hm_editor)** - ⭐ 77
   一款轻量级、可扩展的、跨平台的、专为医疗信息化设计的电子病历编辑器内核，为EMR（电子病历系统）提供专业的结构化病历编辑与AI接入解决方案。

29. **[mcp-toolbox-sdk-js](https://github.com/googleapis/mcp-toolbox-sdk-js)** - ⭐ 64
   Javascript SDK for interacting with the MCP Toolbox for Databases.

30. **[researcher_agent](https://github.com/lgesuellip/researcher_agent)** - ⭐ 63
   An application built on the Model Context Protocol (MCP) that transforms any website into highly relevant content based on your queries. The app seamlessly integrates with platforms like X, Slack, and among others.

31. **[MCPE-Client-Sources](https://github.com/Turkeii/MCPE-Client-Sources)** - ⭐ 55

32. **[revit-mcp-commandset](https://github.com/revit-mcp/revit-mcp-commandset)** - ⭐ 47
   🔄 Revit-MCP Client | Core implementation of the Revit-MCP protocol that connects LLMs with Revit. Includes essential CRUD commands for Revit elements enabling AI-driven BIM automation.

33. **[revit-mcp-commandset](https://github.com/mcp-servers-for-revit/revit-mcp-commandset)** - ⭐ 47
   🔄 Revit-MCP Client | Core implementation of the Revit-MCP protocol that connects LLMs with Revit. Includes essential CRUD commands for Revit elements enabling AI-driven BIM automation.

34. **[deepsecure](https://github.com/DeepTrail/deepsecure)** - ⭐ 42
   Effortlessly secure your AI agents and AI-powered workflows — from prototype to production. Get easy-to-use identity, credential, and access management built for fast-moving AI developers.

35. **[mcp-client-python-example](https://github.com/alejandro-ao/mcp-client-python-example)** - ⭐ 38

36. **[flowllm](https://github.com/FlowLLM-AI/flowllm)** - ⭐ 32
   FlowLLM: Simplifying LLM-based HTTP/MCP Service Development

37. **[mcp-web-client](https://github.com/jinruoxinchen/mcp-web-client)** - ⭐ 28
   MCP Web Client project

38. **[mcpx4j](https://github.com/dylibso/mcpx4j)** - ⭐ 26
   Java client library for https://mcp.run - call portable and secure tools for your AI Agents and Apps

39. **[axonflow](https://github.com/getaxonflow/axonflow)** - ⭐ 26
   AxonFlow — Source-available AI control plane for production LLM systems

40. **[mcpx-py](https://github.com/dylibso/mcpx-py)** - ⭐ 25
   Python client library for https://mcp.run - call portable & secure tools for your AI Agents and Apps

41. **[mcp-client](https://github.com/liuwenzhoa/mcp-client)** - ⭐ 23

42. **[awesome-netsuite-ai](https://github.com/michoelchaikin/awesome-netsuite-ai)** - ⭐ 22
   A curated list of awesome NetSuite AI resources, tools, articles, and community contributions focused on the NetSuite AI Connector Service and MCP (Model Context Protocol) integration.

43. **[luma-api-mcp](https://github.com/lumalabs/luma-api-mcp)** - ⭐ 20
   Powered by Ray (video) and Photon (image) models by Luma AI

44. **[desktop4mistral](https://github.com/hathibelagal-dev/desktop4mistral)** - ⭐ 18
   A desktop client with MCP support for Mistral LLMs

45. **[fast-mcp-client](https://github.com/aswincandra/fast-mcp-client)** - ⭐ 11
   MCP Client Implemented to FastAPI

46. **[novelcrafter-mcp](https://github.com/deadshot465/novelcrafter-mcp)** - ⭐ 10
   An experimental desktop client for using Claude Desktop's MCP with Novelcrafter codices.

47. **[chatbot-spring-ai-mcp-telegram-client](https://github.com/mohamedYoussfi/chatbot-spring-ai-mcp-telegram-client)** - ⭐ 10

### Tools & Libraries

*Development tools and libraries for working with MCP*

1. **[n8n](https://github.com/n8n-io/n8n)** - ⭐ 173,525
   Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

2. **[kong](https://github.com/Kong/kong)** - ⭐ 42,707
   🦍 The API and AI Gateway

3. **[FastGPT](https://github.com/labring/FastGPT)** - ⭐ 27,101
   FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

4. **[kratos](https://github.com/go-kratos/kratos)** - ⭐ 25,422
   Your ultimate Go microservices framework for the cloud-native era.

5. **[excelize](https://github.com/qax-os/excelize)** - ⭐ 20,277
   Go language library for reading and writing Microsoft Excel™ (XLAM / XLSM / XLSX / XLTM / XLTX) spreadsheets

6. **[plate](https://github.com/udecode/plate)** - ⭐ 15,896
   Rich-text editor with AI, MCP, and shadcn/ui

7. **[AstrBot](https://github.com/AstrBotDevs/AstrBot)** - ⭐ 15,686
   Agentic IM Chatbot infrastructure that integrates lots of IM platforms, LLMs, plugins and AI features. Your clawdbot alternative. ✨

8. **[LangBot](https://github.com/langbot-app/LangBot)** - ⭐ 14,244
   Production-grade platform for building IM bots / 生产级即时通信机器人开发平台. Bots for QQ / QQ频道 / Discord / LINE / WeChat(微信, 企业微信)/ Telegram / 飞书 / 钉钉 / Slack e.g. Integrated with ChatGPT(GPT), DeepSeek, Dify, n8n, Langflow, Coze, Claude, Google Gemini, Nano Banana, Kimi, PPIO, Ollama, MiniMax, SiliconFlow, Qwen, Moonshot, MCP etc. LLM & Agent & RAG

9. **[Fay](https://github.com/xszyou/Fay)** - ⭐ 12,179
   fay是一个帮助数字人（2.5d、3d、移动、pc、网页）或大语言模型（openai兼容、deepseek）连通业务系统的mcp框架。

10. **[ui](https://github.com/creativetimofficial/ui)** - ⭐ 11,512
   Open-source components, blocks, and AI agents designed to speed up your workflow. Import them seamlessly into your favorite tools through Registry and MCPs.

11. **[note-gen](https://github.com/codexu/note-gen)** - ⭐ 10,720
   A cross-platform Markdown AI note-taking software.

12. **[langchain4j](https://github.com/langchain4j/langchain4j)** - ⭐ 10,665
   LangChain4j is an open-source Java library that simplifies the integration of LLMs into Java applications through a unified API, providing access to popular LLMs and vector databases. It makes implementing RAG, tool calling (including support for MCP), and agents easy. LangChain4j integrates seamlessly with various enterprise Java frameworks.

13. **[astron-agent](https://github.com/iflytek/astron-agent)** - ⭐ 9,346
   Enterprise-grade, commercial-friendly agentic workflow platform for building next-generation SuperAgents.

14. **[OpenMetadata](https://github.com/open-metadata/OpenMetadata)** - ⭐ 8,650
   OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column level lineage, and seamless team collaboration.

15. **[53AIHub](https://github.com/53AI/53AIHub)** - ⭐ 8,439
   53AI Hub is an open-source AI portal, which enables you to quickly build a operational-level AI portal to launch and operate AI agents, prompts, and AI tools. It supports seamless integration with development platforms like Coze, Dify, FastGPT, RAGFlow.

16. **[Upsonic](https://github.com/Upsonic/Upsonic)** - ⭐ 7,773
   Agent Framework For Fintech and Banks

17. **[lamda](https://github.com/firerpa/lamda)** - ⭐ 7,602
    The most powerful Android RPA agent framework, next generation of mobile automation robots.

18. **[adk-go](https://github.com/google/adk-go)** - ⭐ 6,860
   An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

19. **[Viper](https://github.com/FunnyWolf/Viper)** - ⭐ 4,948
   Adversary simulation and Red teaming platform with AI

20. **[magic](https://github.com/dtyq/magic)** - ⭐ 4,458
   Super Magic. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system)

21. **[Yuxi-Know](https://github.com/xerrors/Yuxi-Know)** - ⭐ 4,265
   结合LightRAG 知识库的知识图谱智能体平台。 An agent platform that integrates a LightRAG knowledge base and knowledge graphs. Build with LangChain v1 + Vue + FastAPI, support DeepAgents、MinerU PDF、Neo4j 、MCP.

22. **[ENScan_GO](https://github.com/wgpsec/ENScan_GO)** - ⭐ 4,203
   一款基于各大企业信息API的工具，解决在遇到的各种针对国内企业信息收集难题。一键收集控股公司ICP备案、APP、小程序、微信公众号等信息聚合导出。支持MCP接入

23. **[nexent](https://github.com/ModelEngine-Group/nexent)** - ⭐ 4,115
   Nexent is a zero-code platform for auto-generating agents — no orchestration, no complex drag-and-drop required. Nexent also offers powerful capabilities for agent running control, data processing and MCP tools.

24. **[ag2](https://github.com/ag2ai/ag2)** - ⭐ 4,108
   AG2 (formerly AutoGen): The Open-Source AgentOS. Join us at: https://discord.gg/sNGSwQME3x

25. **[kubefwd](https://github.com/txn2/kubefwd)** - ⭐ 4,037
   Bulk port forwarding Kubernetes services for local development.

26. **[manifest](https://github.com/mnfst/manifest)** - ⭐ 3,303
   A shadcn/ui library for building ChatGPT Apps and MCP Apps

27. **[semantic-router](https://github.com/vllm-project/semantic-router)** - ⭐ 3,165
   System Level Intelligent Router for Mixture-of-Models at Cloud, Data Center and Edge

28. **[solon](https://github.com/opensolon/solon)** - ⭐ 2,704
   🔥 Java enterprise application development framework for full scenario: Restrained, Efficient, Open, Ecologicalll!!! 700% higher concurrency 50% memory savings Startup is 10 times faster. Packing 90% smaller; Compatible with java8 ~ java25; Supports LTS. (Replaceable spring)

29. **[ultracite](https://github.com/haydenbleasel/ultracite)** - ⭐ 2,661
   A highly opinionated, zero-configuration linter and formatter.

30. **[easy-vibe](https://github.com/datawhalechina/easy-vibe)** - ⭐ 2,465
   Vibe coding from 0 to 1 ｜把想法做成真正能上线的产品｜首个交互式教程｜零基础也能学会的 AI 编程实战

31. **[harbor](https://github.com/av/harbor)** - ⭐ 2,412
   One command brings a complete pre-wired LLM stack with hundreds of services to explore.

32. **[amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli)** - ⭐ 1,886
   ✨ Agentic chat experience in your terminal. Build applications using natural language.

33. **[generative-ai](https://github.com/genieincodebottle/generative-ai)** - ⭐ 1,760
   Comprehensive resources on Generative AI, including a detailed roadmap, projects, use cases, interview preparation, and coding preparation.

34. **[MinecraftDev](https://github.com/minecraft-dev/MinecraftDev)** - ⭐ 1,709
   Plugin for IntelliJ IDEA that gives special support for Minecraft modding projects.

35. **[d2mcpp](https://github.com/mcpp-community/d2mcpp)** - ⭐ 1,493
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

36. **[MultiAgentPPT](https://github.com/johnson7788/MultiAgentPPT)** - ⭐ 1,478
   MultiAgentPPT 是一个集成了 A2A（Agent2Agent）+ MCP（Model Context Protocol）+ ADK（Agent Development Kit） 架构的智能化演示文稿生成系统，支持通过多智能体协作和流式并发机制

37. **[mcpelauncher-manifest](https://github.com/minecraft-linux/mcpelauncher-manifest)** - ⭐ 1,439
   The main repository for the Linux and Mac OS Bedrock edition Minecraft launcher.

38. **[superset](https://github.com/superset-sh/superset)** - ⭐ 1,402
   The command center for coding agents - Run a team of Claude Code, OpenCode, Codex, or any other agents on your machine

39. **[mcpp-standard](https://github.com/Sunrisepeak/mcpp-standard)** - ⭐ 1,372
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

40. **[NagaAgent](https://github.com/Xxiii8322766509/NagaAgent)** - ⭐ 1,325
   A simple yet powerful agent framework for personal assistants, designed to enable intelligent interaction, multi-agent collaboration, and seamless tool integration.

41. **[paperdebugger](https://github.com/PaperDebugger/paperdebugger)** - ⭐ 1,319
   A Plugin-Based Multi-Agent System for In-Editor Academic Writing, Review, and Editing

42. **[awesome-hacking-lists](https://github.com/taielab/awesome-hacking-lists)** - ⭐ 1,285
   A curated collection of top-tier penetration testing tools and productivity utilities across multiple domains. Join us to explore, contribute, and enhance your hacking toolkit!

43. **[BuildingAI](https://github.com/BidingCC/BuildingAI)** - ⭐ 1,229
   BuildingAI is an enterprise-grade open-source intelligent agent platform designed for AI developers, AI entrepreneurs, and forward-thinking organizations. Through a visual configuration interface (Do It Yourself), you can build native enterprise AI applications without code. The platform offers native capabilities such as intelligent agents, MCP...

44. **[langchain4j-aideepin](https://github.com/moyangzhan/langchain4j-aideepin)** - ⭐ 1,157
   基于AI的工作效率提升工具（聊天、绘画、知识库、工作流、 MCP服务市场、语音输入输出、长期记忆） | Ai-based productivity tools (Chat,Draw,RAG,Workflow,MCP marketplace, ASR,TTS, Long-term memory etc)

45. **[any-agent](https://github.com/mozilla-ai/any-agent)** - ⭐ 1,095
   A single interface to use and evaluate different agent frameworks 

46. **[Gearboy](https://github.com/drhelius/Gearboy)** - ⭐ 1,078
   Game Boy / Gameboy Color emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

47. **[AIPex](https://github.com/AIPexStudio/AIPex)** - ⭐ 1,049
   AIPex: AI browser automation assistant, no migration and privacy first. Alternative to Manus Browser Operator、 Claude Chrome and Agent Browser

48. **[zen](https://github.com/sheshbabu/zen)** - ⭐ 1,013
   Selfhosted notes app. Single golang binary, notes stored as markdown within SQLite, full-text search, very low resource usage

49. **[open-trading-api](https://github.com/koreainvestment/open-trading-api)** - ⭐ 1,006
   Korea Investment & Securities Open API Github

50. **[openops](https://github.com/openops-cloud/openops)** - ⭐ 988
   The batteries-included, No-Code FinOps automation platform, with the AI you trust.

51. **[chunkhound](https://github.com/chunkhound/chunkhound)** - ⭐ 985
   Local first codebase intelligence

52. **[arduino-mcp2515](https://github.com/autowp/arduino-mcp2515)** - ⭐ 963
   Arduino MCP2515 CAN interface library

53. **[claude-chatgpt-mcp](https://github.com/syedazharmbnr1/claude-chatgpt-mcp)** - ⭐ 773
   A Claude MCP tool to interact with the ChatGPT desktop app on macOS

54. **[amical](https://github.com/amicalhq/amical)** - ⭐ 742
   🎙️ AI Dictation App - Open Source and Local-first ⚡ Type 3x faster, no keyboard needed. 🆓 Powered by open source models, works offline, fast and accurate.

55. **[bytechef](https://github.com/bytechefhq/bytechef)** - ⭐ 729
   Open-source, AI-native, low-code platform for API orchestration, workflow automation, and AI agent integration across internal systems and SaaS products.

56. **[MCPELauncher](https://github.com/zhuowei/MCPELauncher)** - ⭐ 727
   Source code for BlockLauncher, a launcher that patches Minecraft for Android

57. **[aderyn](https://github.com/Cyfrin/aderyn)** - ⭐ 713
   Solidity Static Analyzer that easily integrates into your editor

58. **[voicemode](https://github.com/mbailey/voicemode)** - ⭐ 699
   Natural voice conversations with Claude Code

59. **[JiwuChat](https://github.com/KiWi233333/JiwuChat)** - ⭐ 698
   JiwuChat 🍂 : 轻量级跨平台IM聊天应用，集成AI机器人( DeepSeek/Gemini/Kimi... )、音视频通话及AI购物。支持多端消息同步，自定义主题，高效便捷  🍒

60. **[Sentient](https://github.com/existence-master/Sentient)** - ⭐ 674
   A personal AI assistant for everyone

61. **[infio-copilot](https://github.com/infiolab/infio-copilot)** - ⭐ 635
   A Cursor-inspired AI assistant for Obsidian that offers smart autocomplete and interactive chat with your selected notes

62. **[WHartTest](https://github.com/MGdaasLab/WHartTest)** - ⭐ 615
   WHartTest 是基于 Django REST Framework 与现代大模型技术打造的 AI 驱动测试自动化平台。平台聚合自然语言理解、知识库检索与嵌入搜索能力，结合 LangChain 与 MCP（Model Context Protocol） 工具调用，实现从需求到可执行测试用例的自动化生成与管理，帮助测试团队提升效率与覆盖率。

63. **[cloudsword](https://github.com/wgpsec/cloudsword)** - ⭐ 593
   一款帮助云租户发现和测试云上风险、增强云上防护能力的综合性开源工具

64. **[chatlog_alpha](https://github.com/teest114514/chatlog_alpha)** - ⭐ 571
   原 [chatlog]项目（一个微信数据库读取及提供mcp服务开源软件）的二次开发，会尽可能同步最新开源解密源码

65. **[IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP)** - ⭐ 562
   Say goodbye to the complex, verbose, and laggy interaction mode of IDA Pro MCP

66. **[LightAgent](https://github.com/wanxingai/LightAgent)** - ⭐ 524
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

67. **[marmot](https://github.com/marmotdata/marmot)** - ⭐ 502
   Marmot helps teams discover, understand, and leverage their data with powerful search and lineage visualisation tools. It's designed to make data accessible for everyone.

68. **[auto-commenter](https://github.com/rokpiy/auto-commenter)** - ⭐ 485
   A Claude skill that automatically posts personalized, authentic comments in your target communities.

69. **[tool-ui](https://github.com/assistant-ui/tool-ui)** - ⭐ 478
   UI components for AI interfaces

70. **[AIWriteX](https://github.com/iniwap/AIWriteX)** - ⭐ 465
   AIWriteX是基于CrewAI、AIForge的新一代智能内容创作平台，从微信公众号自动化工具起步，正在重新定义AI辅助内容创作的边界，融合"AI+创意+搜索+借鉴"四重能力，多种超绝玩法，内容创作充满无限可能。

71. **[ai-code-helper](https://github.com/liyupi/ai-code-helper)** - ⭐ 463
   2025 年 AI 编程助手实战项目（作者：程序员鱼皮），基于 Spring Boot 3.5 + Java 21 + LangChain4j + AI 构建智能编程学习与求职辅导机器人，覆盖 AI 大模型接入、LangChain4j 核心特性、流式对话、Prompt 工程、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、Web 爬虫、安全防护、Vue.js 前端开发、SSE 服务端推送等企业级 AI 应用开发技术。帮助开发者掌握 AI 时代必备技能，熟悉 LangChain 框架，提升编程学习效率和求职竞争力，成为企业需要的 AI 全栈开发人才。

72. **[ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill)** - ⭐ 462
   An IOS Simulator Skill for ClaudeCode. Use it to optimise Claude's ability to build, run and interact with your apps, without using up any of the available token/context budget.

73. **[LightAgent](https://github.com/wxai-space/LightAgent)** - ⭐ 430
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

74. **[browser-operator-core](https://github.com/BrowserOperator/browser-operator-core)** - ⭐ 430
   Browser Operator - The AI browser with built in Multi-Agent platform! Open source alternative to ChatGPT Atlas, Perplexity Comet, Dia and Microsoft CoPilot Edge Browser

75. **[mcp-cn-a-stock](https://github.com/elsejj/mcp-cn-a-stock)** - ⭐ 405
   这是一个为大模型提供 A 股数据的的 MCP(Model Content Protocol) 服务。

76. **[groundhog](https://github.com/ghuntley/groundhog)** - ⭐ 392
   Groundhog's primary purpose is to teach people how Cursor and all these other coding agents work under the hood. If you understand how these coding assistants work from first principles, then you can drive these tools harder (or perhaps make your own!).

77. **[mcpi](https://github.com/martinohanlon/mcpi)** - ⭐ 387
   Minecraft: Pi Edition API Python Library

78. **[volcano-sdk](https://github.com/Kong/volcano-sdk)** - ⭐ 386
   🌋 Build AI agents that seamlessly combine LLM reasoning with real-world actions via MCP tools — in just a few lines of TypeScript.

79. **[azan-mcp](https://github.com/ahmedeltaher/azan-mcp)** - ⭐ 382
   Azan + Prayer Time + MCP + AI Agents + Islamic + Salah + A lightweight MCP library to calculate prayer times and trigger Azan with a single tool call. If you’re building an AI agent or prayer application, there’s no need to deal with astronomical calculations, timezones, or edge cases again.

80. **[bridle](https://github.com/neiii/bridle)** - ⭐ 377
   TUI / CLI config manager for agentic harnesses (Amp, Claude Code, Opencode, Goose, Copilot CLI, Crush, Droid)

81. **[Adafruit-MCP23017-Arduino-Library](https://github.com/adafruit/Adafruit-MCP23017-Arduino-Library)** - ⭐ 376
   Arduino Library for Adafruit MCP23017

82. **[pokemon-chat](https://github.com/skygazer42/pokemon-chat)** - ⭐ 366
   基于 LightRAG、LangGraph、MCP、RagFlow、微调LLMs宝可梦主题的智能聊天助手

83. **[graphrag-toolkit](https://github.com/awslabs/graphrag-toolkit)** - ⭐ 361
   Python toolkit for building graph-enhanced GenAI applications

84. **[exograph](https://github.com/exograph/exograph)** - ⭐ 341
   Build production-ready backends in minutes

85. **[MCprep](https://github.com/Moo-Ack-Productions/MCprep)** - ⭐ 341
   Blender python addon to increase workflow for creating minecraft renders and animations

86. **[UE5-MCP](https://github.com/VedantRGosavi/UE5-MCP)** - ⭐ 340
   MCP for Unreal Engine 5

87. **[eechat](https://github.com/Lucassssss/eechat)** - ⭐ 333
   🚀 Powerful Local AI Chat Application - Mcp, Secure, Efficient, Personalized 本地化部署的大模型客户端

88. **[depyler](https://github.com/paiml/depyler)** - ⭐ 327
   Compiles Python to Rust, helping transition off of Python to Energy Efficient and Safe Rust Code

89. **[Gearsystem](https://github.com/drhelius/Gearsystem)** - ⭐ 323
   Sega Master System / Game Gear / SG-1000 emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

90. **[MCPanelViewController](https://github.com/matthewcheok/MCPanelViewController)** - ⭐ 319
   Drop-in panel control for iOS with blurring background and screen-edge activation gestures.

91. **[ChattyPlay-Agent](https://github.com/P1kaj1uu/ChattyPlay-Agent)** - ⭐ 319
   本项目基于React+TypeScript+Hono实现，已接入OpenAI SDK、MCP服务和Agent相关大模型，扩展实时黄金和K线图，以及文生图服务(无需再代理和APIKey)，同时支持腾讯视频、爱奇艺、优酷、芒果TV、哔哩哔哩、网易云音乐等平台会员视频破解可在线解析、动漫漫画畅享阅读和论文降重（适配PC端、移动端）

92. **[news-agents](https://github.com/eugeneyan/news-agents)** - ⭐ 313
   📰 Building News Agents to Summarize News with MCP, Q, and tmux

93. **[awesome-slash](https://github.com/avifenesh/awesome-slash)** - ⭐ 312
   AI writes code. This automates everything else. 9 plugins · 39 agents · 24 skills · for Claude Code, OpenCode, Codex.

94. **[CookHero](https://github.com/Decade-qiu/CookHero)** - ⭐ 308
   CookHero是一个基于 LLM + RAG + Agent + 多模态的智能饮食与烹饪管理平台，支持智能菜谱查询、个性化饮食计划、AI 饮食记录、营养分析、Web 搜索增强，以及可扩展的 ReAct Agent / Subagent 工具体系，帮助厨房新手轻松成为“烹饪英雄”。

95. **[napi](https://github.com/nanoapi-io/napi)** - ⭐ 294
   Software architecture tooling for the AI age

96. **[building-an-agentic-system](https://github.com/gerred/building-an-agentic-system)** - ⭐ 280
   An in-depth book and reference on building agentic systems like Claude Code

97. **[pydantic-deepagents](https://github.com/vstorm-co/pydantic-deepagents)** - ⭐ 271
   Python Deep Agent framework built on top of Pydantic-AI, designed to help you quickly build production-grade autonomous AI agents with planning, filesystem operations, subagent delegation, skills, and structured outputs—in just 10 lines of code.

98. **[edumcp](https://github.com/aieducations/edumcp)** - ⭐ 267
   EDUMCP is a protocol that integrates the Model Context Protocol (MCP) with applications in the education field, dedicated to achieving seamless interconnection and interoperability among different AI models, educational applications, smart hardware, and teaching AGENTs.

99. **[MCPDict](https://github.com/MaigoAkisame/MCPDict)** - ⭐ 259
   Android App: 漢字古今中外讀音查詢

100. **[ai4eh](https://github.com/ethiack/ai4eh)** - ⭐ 249
   AI for Ethical Hacking - Workshop

101. **[oreilly-ai-agents](https://github.com/sinanuozdemir/oreilly-ai-agents)** - ⭐ 249
   An introduction to the world of AI Agents

102. **[MCP-Defender](https://github.com/MCP-Defender/MCP-Defender)** - ⭐ 246
   Desktop app that automatically scans and blocks malicious MCP traffic in AI apps like Cursor, Claude, VS Code and Windsurf.

103. **[MCPMappingViewer](https://github.com/bspkrs/MCPMappingViewer)** - ⭐ 244
   A small GUI for viewing the mappings from Minecraft obfuscated code names to MCP code names.

104. **[MCPConfig](https://github.com/MinecraftForge/MCPConfig)** - ⭐ 240
   Public facing repo for MCP SRG mappings.

105. **[Minecraft-Deobfuscator3000](https://github.com/SimplyProgrammer/Minecraft-Deobfuscator3000)** - ⭐ 234
   Powerful and universal deobfuscator for Minecraft mods and java decompiler!

106. **[MCPU](https://github.com/cpldcpu/MCPU)** - ⭐ 232
   MCPU - A Minimal 8Bit CPU in a 32 Macrocell CPLD

107. **[stock-scanner-mcp](https://github.com/wbsu2003/stock-scanner-mcp)** - ⭐ 231
   这是一个基于 FastAPI-MCP 的股票分析服务，旨在通过 MCP 工具函数接口提供股票相关的综合数据和分析能力，包括价格、评分、技术报告和 AI 分析。

108. **[mcpfp](https://github.com/MauritsWilke/mcpfp)** - ⭐ 221
   A website to generate Minecraft profile pictures

109. **[AuditLuma](https://github.com/Vistaminc/AuditLuma)** - ⭐ 217
   AuditLuma是一个AI+智能体代码审计系统，它利用多个AI代理和先进的技术，包括多代理合作协议（MCP）和Self-RAG（检索增强生成），为代码库提供全面的安全分析，目前已经支持ollama部署的本地大模型

110. **[McPicker-iOS](https://github.com/kmcgill88/McPicker-iOS)** - ⭐ 215
   McPicker is a customizable, closure driven UIPickerView drop-in solution with animations that is rotation ready.

111. **[Toucan](https://github.com/TheAgentArk/Toucan)** - ⭐ 215
   Official repo of Toucan: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments

112. **[mcpat](https://github.com/HewlettPackard/mcpat)** - ⭐ 209
   An integrated power, area, and timing modeling framework for multicore and manycore architectures

113. **[langchain_data_agent](https://github.com/eosho/langchain_data_agent)** - ⭐ 208
   NL2SQL - Ask questions in plain English, get SQL queries and results. Powered by LangGraph.

114. **[weam](https://github.com/weam-ai/weam)** - ⭐ 202
   Web app for teams of 20+ members. In-built connections to major LLMs via API. Share chats, prompts, and agents in team or private folders. Modern, fully responsive stack (Next.js, Node.js). Deploy your own vibe-coded AI apps, agents, or workflows—or use ready-made solutions from the library.

115. **[BaseLayer](https://github.com/zwgnr/BaseLayer)** - ⭐ 200
   Re-usable multi part components built on React Aria and TailwindCSS. 

116. **[MCP-919](https://github.com/Marcelektro/MCP-919)** - ⭐ 190
   Fully working & decompiled MCP for Minecraft 1.8.9 

117. **[MCPScan](https://github.com/antgroup/MCPScan)** - ⭐ 189

118. **[mangaba_ai](https://github.com/Mangaba-ai/mangaba_ai)** - ⭐ 184
   Repositório minimalista para criação de agentes de IA inteligentes e versáteis com protocolos A2A (Agent-to-Agent) e MCP (Model Context Protocol).

119. **[cupcake](https://github.com/eqtylab/cupcake)** - ⭐ 176
   A native policy enforcement layer for AI coding agents. Built on OPA/Rego.

120. **[bluebox](https://github.com/VectorlyApp/bluebox)** - ⭐ 174
   Reverse engineer web apps

121. **[bluebox-sdk](https://github.com/VectorlyApp/bluebox-sdk)** - ⭐ 169
   Reverse engineer web apps

122. **[agentic-ai-systems](https://github.com/ThibautMelen/agentic-ai-systems)** - ⭐ 164
   🐔 Agentic systems explained with chickens. Workflows, agents & orchestration made simple. Mermaid diagrams included

123. **[codecompanion-history.nvim](https://github.com/ravitemer/codecompanion-history.nvim)** - ⭐ 163
   A history management extension for codecompanion AI chat plugin that enables saving, browsing and restoring chat sessions.

124. **[Weave](https://github.com/liaotxcn/Weave)** - ⭐ 156
   A highly efficient, secure, and stable application development platform with excellent performance, easy scalability, and deep integration of AI capabilities such as LLM, AI Chat, RAG, and Agents.高效、安全、稳定的服务研发平台，具备良好性能，同时易扩展，深度集成LLM、AIChat、RAG、Agent等AI能力

125. **[ZenOps](https://github.com/opsre/ZenOps)** - ⭐ 150
   🧘 通过钉钉、飞书、企微智能机器人用自然语言查询运维资源的工具。

126. **[rocketship](https://github.com/rocketship-ai/rocketship)** - ⭐ 140
   A QA testing framework for your coding agent.

127. **[toon-java](https://github.com/toon-format/toon-java)** - ⭐ 139
   ☕ Community-driven Java implementation of TOON

128. **[x-mcp](https://github.com/xpzouying/x-mcp)** - ⭐ 138
   小红书创作中心

129. **[mcp-toolkit](https://github.com/charIesding/mcp-toolkit)** - ⭐ 137
   utilities for mcp

130. **[mcp-audit](https://github.com/apisec-inc/mcp-audit)** - ⭐ 133
   See what your AI agents can access. Scan MCP configs for exposed secrets, shadow APIs, and AI models. Generate AI-BOMs for compliance.

131. **[awesome-ai-repositories](https://github.com/altengineer/awesome-ai-repositories)** - ⭐ 125
   A curated list of open source repositories for AI Engineers

132. **[claude-ipc-mcp](https://github.com/jdez427/claude-ipc-mcp)** - ⭐ 123
   AI-to-AI communication protocol for Claude, Gemini, and other AI assistants

133. **[Z.ai2api](https://github.com/hmjz100/Z.ai2api)** - ⭐ 122
   将 Z.ai Chat 代理为 OpenAI/Anthropic Compatible 格式，支持多模型列表映射、免令牌、智能处理思考链、图片上传等功能；Z.ai ZtoApi z2api ZaitoApi zai X-Signature 签名 GLM 4.5 v 4.6

134. **[AgentNexus](https://github.com/wozhenbang2004/AgentNexus)** - ⭐ 113
   Multi-Agent,MCP,RAG,SpringAI1.0.0,RE-ACT

135. **[5-Day-AI-Agents-Intensive-Course-with-Google](https://github.com/sdivyanshu90/5-Day-AI-Agents-Intensive-Course-with-Google)** - ⭐ 111
   5-Day Gen AI Intensive Course with Google

136. **[Gearcoleco](https://github.com/drhelius/Gearcoleco)** - ⭐ 110
   ColecoVision emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

137. **[STAMP](https://github.com/KatherLab/STAMP)** - ⭐ 110
   Solid Tumor Associative Modeling in Pathology

138. **[kalouk-mcp](https://github.com/fabianabarca/kalouk-mcp)** - ⭐ 107
   Servidor de contexto de Kalouk para agentes de inteligencia artificial.

139. **[AgentFly](https://github.com/Agent-One-Lab/AgentFly)** - ⭐ 106
   Scalable and extensible reinforcement learning for LM agents.

140. **[mcp-in-action](https://github.com/huangjia2019/mcp-in-action)** - ⭐ 103
   极客时间MCP新课已经上线！超2000同学一起开启MCP学习之旅！

141. **[5-Day-AI-Agents-Intensive-Course-with-Google](https://github.com/anxiong2025/5-Day-AI-Agents-Intensive-Course-with-Google)** - ⭐ 101
   谷歌5天AI Agents强化课程

142. **[Squirrel](https://github.com/hakoniwaa/Squirrel)** - ⭐ 91
   ai memory for coding

143. **[coplay-unity-plugin](https://github.com/CoplayDev/coplay-unity-plugin)** - ⭐ 83
   Unity plugin for Coplay

144. **[Complementarity.jl](https://github.com/chkwon/Complementarity.jl)** - ⭐ 79
   provides a modeling interface for mixed complementarity problems (MCP) and math programs with equilibrium problems (MPEC) via JuMP 

145. **[smart-customer-service-system](https://github.com/traveler-leon/smart-customer-service-system)** - ⭐ 78
   构建一个基于大模型的智能客服系统，可提供静态知识问答(静态数据)、动态知识问答（数据库），业务办理（api调用）等功能，同时系统具有自我学习能力。定期的反思可让系统变得更强大。

146. **[TensorBlock-Studio](https://github.com/TensorBlock/TensorBlock-Studio)** - ⭐ 73
   A lightweight, open, and extensible multi-LLM interaction studio.

147. **[onemcp-hub](https://github.com/ipenywis/onemcp-hub)** - ⭐ 73
   OneMCP feature requests, bugs and improvements 

148. **[lycoris](https://github.com/solaoi/lycoris)** - ⭐ 72
   Real-time speech recognition & AI-powered note-taking app for macOS with offline/online modes, multilingual transcription, and Japanese translation support.

149. **[nvim-gemini-companion](https://github.com/gutsavgupta/nvim-gemini-companion)** - ⭐ 71
   A Neovim plugin to integrate Gemini CLI well (+ Qwen-code now)

150. **[quarkus-workshop-langchain4j](https://github.com/quarkusio/quarkus-workshop-langchain4j)** - ⭐ 69
   Quarkus Langchain4J Workshop

151. **[protocol-launcher](https://github.com/zhensherlock/protocol-launcher)** - ⭐ 66
   One-click launch URL generator for protocol-based apps

152. **[tiktok-mcp](https://github.com/yap-audio/tiktok-mcp)** - ⭐ 65
   A Model Context Protocol service for TikTok video discovery and metadata extraction.

153. **[seekchat](https://github.com/seekrays/seekchat)** - ⭐ 61
   ✨ A Sleek and Powerful AI Desktop Assistant that supports MCP integration✨

154. **[Roomey_AI_Voice_Agent](https://github.com/augmentedstartups/Roomey_AI_Voice_Agent)** - ⭐ 60
   Roomey is a multi-purpose Voice Agent designed to run your personal and business life.

155. **[Grapheteria](https://github.com/beubax/Grapheteria)** - ⭐ 60
   Grapheteria: A structured framework bringing uniformity to agent orchestration!

156. **[OneCite](https://github.com/HzaCode/OneCite)** - ⭐ 52
   📚 An intelligent toolkit to automatically parse, complete, and format academic references.

157. **[chm-converter](https://github.com/DTDucas/chm-converter)** - ⭐ 49
   chm to markdown and vectorDB

158. **[houdini-mcp](https://github.com/capoom/houdini-mcp)** - ⭐ 49
   Houdini integration through the Model Context Protocol

159. **[mcp-java8-sdk](https://github.com/krrr/mcp-java8-sdk)** - ⭐ 46
   Backported Model Context Protocol SDK for Java 8

160. **[asya](https://github.com/deliveryhero/asya)** - ⭐ 40
   🎭 Actors on Kubernetes for scalable Gen AI

161. **[ummon](https://github.com/Nayshins/ummon)** - ⭐ 36
   The semantic layer for software engineering: Connect   code to meaning, build on understanding

162. **[xiaozhi-MCPTools](https://github.com/ZhongZiTongXue/xiaozhi-MCPTools)** - ⭐ 34
   一个图形化界面的小智MCP服务连接器，包含多种工具！ 自动部署服务，方便小白给小智Ai添加MCP工具

163. **[advanced-reason-mcp](https://github.com/Kuon-dev/advanced-reason-mcp)** - ⭐ 33
   Enhanced version of "Sequential Thinking" MCP

164. **[Wireshark_mcp](https://github.com/jayimu/Wireshark_mcp)** - ⭐ 32
   Wireshark MCP 是一个基于 Model Context Protocol (MCP) 的服务器，允许 AI 助手通过 tshark 命令行工具进行交互。该工具提供了丰富的网络数据分析功能，支持实时抓包和离线分析。

165. **[zentrun](https://github.com/andrewsky-labs/zentrun)** - ⭐ 31
   Prompt-driven automation platform - Transform natural language into executable workflows

166. **[prompt-pro](https://github.com/timothywarner-org/prompt-pro)** - ⭐ 31
   Master AI prompting for business innovation. O'Reilly Live Learning course by Tim Warner covering ChatGPT, Claude, Copilot, and enterprise prompt engineering with MCP implementation.

167. **[awesome-mcp-list](https://github.com/notedit/awesome-mcp-list)** - ⭐ 28
   Awesome Model Context Protocol Service List

168. **[adk-mcp-gemma3](https://github.com/arjunprabhulal/adk-mcp-gemma3)** - ⭐ 27
   Build AI Agent using Google ADK , MCP and Gemma 3 model

169. **[shebe](https://github.com/rhobimd-oss/shebe)** - ⭐ 26
   Fast BM25 full-text search for code repositories with MCP integration for AI coding agents.

170. **[shebe](https://github.com/shebe-oss/shebe)** - ⭐ 26
   Fast BM25 full-text search for code repositories with MCP integration for AI coding agents.

171. **[hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298](https://github.com/LinkedInLearning/hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298)** - ⭐ 25
   this repo is for linkedin learning course: Hands-On AI: Building AI Agents with Model Context Protocol (MCP) and Agent2Agent (A2A)

172. **[codai](https://github.com/codai-agent/codai)** - ⭐ 24
   Codai is an AI programming tool that boosts coding efficiency and empowers non-programmers. Its future plans include introducing a local database, enabling customization, and building a versatile AI terminal. It aims to popularize AI programming and lead the AI Programming+ era.

173. **[cursor-like-pro](https://github.com/gifflet/cursor-like-pro)** - ⭐ 17
   Cursor IDE like Pro

174. **[MCPStack](https://github.com/MCP-Pipeline/MCPStack)** - ⭐ 16
   Stack & Orchestrate MCP Tools — The Scikit-Learn-Pipeline Way , For LLMs

175. **[mcp-labs](https://github.com/thangchung/mcp-labs)** - ⭐ 16
   All things about MCP experiments.⭐️ Star to support our work!

176. **[n8n-operator](https://github.com/jakub-k-slys/n8n-operator)** - ⭐ 15
   Kubernetes Operator for N8n, a fair-code workflow automation platform with native AI capabilities.

177. **[ai-tools](https://github.com/elsejj/ai-tools)** - ⭐ 13
   ai-tools  call your llm based tools through shortcut (ctrl-q) in any application

178. **[feather_wand_agent](https://github.com/QAInsights/feather_wand_agent)** - ⭐ 13
   Feather Wand Agent is a comprehensive AI-powered toolkit for performance testing and monitoring. It integrates multiple industry-standard performance testing tools (JMeter, k6, Gatling, and Locust) into a single, unified interface, allowing users to execute and analyze performance tests through natural language interactions.

179. **[mkinf-run](https://github.com/mkinf-io/mkinf-run)** - ⭐ 13
   mkinf run API

180. **[ai-agents](https://github.com/rjmurillo/ai-agents)** - ⭐ 12
   Multi-agent system for software development

181. **[mcp-tools](https://github.com/shaharia-lab/mcp-tools)** - ⭐ 11
   Tools for MCP (Model Context Protocol) written in Go

182. **[Unity-AI-Tools-Template](https://github.com/IvanMurzak/Unity-AI-Tools-Template)** - ⭐ 10
   Unity MCP Tool template project

### Examples

*Example projects demonstrating MCP usage*

1. **[YC-Killer](https://github.com/sahibzada-allahyar/YC-Killer)** - ⭐ 2,659
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

2. **[AI-Agents-Library](https://github.com/sahibzada-allahyar/AI-Agents-Library)** - ⭐ 2,610
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

3. **[claude-mcp-examples](https://github.com/charIesding/claude-mcp-examples)** - ⭐ 151
   examples of claude with mcp integration

4. **[End-to-End-Agentic-Ai-Automation-Lab](https://github.com/MDalamin5/End-to-End-Agentic-Ai-Automation-Lab)** - ⭐ 46
   This repository contains hands-on projects, code examples, and deployment workflows. Explore multi-agent systems, LangChain, LangGraph, AutoGen, CrewAI, RAG, MCP, automation with n8n, and scalable agent deployment using Docker, AWS, and BentoML.

5. **[claude-mcp](https://github.com/thinkbigcd/claude-mcp)** - ⭐ 11
   claude and mcp integration examples and tutorials

### Documentation

*Documentation, tutorials, and learning resources*

1. **[modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)** - ⭐ 7,139
   Specification and documentation for the Model Context Protocol

2. **[ai-guide](https://github.com/liyupi/ai-guide)** - ⭐ 6,483
   程序员鱼皮的 AI 资源大全 + Vibe Coding 零基础教程，分享大模型选择指南（DeepSeek / GPT / Gemini / Claude）、最新 AI 资讯、Prompt 提示词大全、AI 知识百科（RAG / MCP / A2A）、AI 编程技巧、AI 工具用法（Cursor / Claude Code / TRAE / Lovable / Agent Skills）、AI 开发框架教程（Spring AI / LangChain）、AI 产品变现指南，帮你快速掌握 AI 技术，走在时代前沿。本项目为开源文档版本，已升级为鱼皮 AI 导航网站

3. **[jar-analyzer](https://github.com/jar-analyzer/jar-analyzer)** - ⭐ 1,922
   Jar Analyzer - 一个 JAR 包 GUI 分析工具，方法调用关系搜索，方法调用链 DFS 算法分析，模拟 JVM 的污点分析验证 DFS 结果，字符串搜索，Java Web 组件入口分析，CFG 程序分析，JVM 栈帧分析，自定义表达式搜索，紧跟 AI 技术发展，支持 MCP 调用，支持 n8n 工作流，文档：https://docs.qq.com/doc/DV3pKbG9GS0pJS0tk

4. **[LLM-Agents-Ecosystem-Handbook](https://github.com/oxbshw/LLM-Agents-Ecosystem-Handbook)** - ⭐ 477
   One-stop handbook for building, deploying, and understanding LLM agents with 60+ skeletons, tutorials, ecosystem guides, and evaluation tools.

5. **[pew-pew-plaza-packs](https://github.com/appboypov/pew-pew-plaza-packs)** - ⭐ 83
   AI-powered project management framework based on an opinionated view on effective prompts and a highly modular approach to building effective agents, workflows, templates, prompts and context documents.

6. **[Agent-Fusion](https://github.com/krokozyab/Agent-Fusion)** - ⭐ 53
    Agent Fusion is a local RAG semantic search engine that gives AI agents instant access to your code, documentation (Markdown, Word, PDF). Query    your codebase from code agents without hallucinations. Runs 100% locally, includes a lightweight embedding model, and optional multi-agent task    orchestration. Deploy with a single JAR

7. **[codedox](https://github.com/chriswritescode-dev/codedox)** - ⭐ 27
    A powerful system for crawling documentation websites, extracting code snippets, and providing fast search capabilities via MCP (Model Context Protocol) integration.

8. **[Q4_learning](https://github.com/DanielHashmi/Q4_learning)** - ⭐ 12
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

