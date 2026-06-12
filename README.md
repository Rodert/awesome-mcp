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

## 📚 Projects (4865 total)

> Last updated: **2026-06-12**

### MCP Servers

*MCP server implementations that provide protocol services*

1. **[ECC](https://github.com/affaan-m/ECC)** - ⭐ 213,670
   The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

2. **[everything-claude-code](https://github.com/affaan-m/everything-claude-code)** - ⭐ 185,825
   The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

3. **[dify](https://github.com/langgenius/dify)** - ⭐ 144,904
   Production-ready platform for agentic workflow development.

4. **[open-webui](https://github.com/open-webui/open-webui)** - ⭐ 141,155
   User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

5. **[gemini-cli](https://github.com/google-gemini/gemini-cli)** - ⭐ 105,182
   An open-source AI agent that brings the power of Gemini directly into your terminal.

6. **[cc-switch](https://github.com/farion1231/cc-switch)** - ⭐ 98,753
   A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Gemini CLI & Hermes Agent. Only official website: ccswitch.io

7. **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** - ⭐ 88,903
   A collection of MCP servers.

8. **[servers](https://github.com/modelcontextprotocol/servers)** - ⭐ 87,083
   Model Context Protocol Servers

9. **[netdata](https://github.com/netdata/netdata)** - ⭐ 79,123
   The fastest path to AI-powered full stack observability, even for lean teams.

10. **[ragflow](https://github.com/infiniflow/ragflow)** - ⭐ 78,943
   RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

11. **[lobehub](https://github.com/lobehub/lobehub)** - ⭐ 78,531
   🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

12. **[lobe-chat](https://github.com/lobehub/lobe-chat)** - ⭐ 70,553
   :exploding_head: LobeHub - The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

13. **[awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** - ⭐ 64,226
   A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

14. **[Scrapling](https://github.com/D4Vinci/Scrapling)** - ⭐ 63,145
   🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

15. **[anything-llm](https://github.com/Mintplex-Labs/anything-llm)** - ⭐ 60,921
   The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

16. **[TrendRadar](https://github.com/sansan0/TrendRadar)** - ⭐ 59,331
   ⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS, and smart alerts.🎯 告别信息过载，你的 AI 舆情监控助手与热点筛选工具！聚合多平台热点 +  RSS 订阅，支持关键词精准筛选。AI 智能筛选新闻 + AI 翻译 +  AI 分析简报直推手机，也支持接入 MCP 架构，赋能 AI 自然语言对话分析、情感洞察与趋势预测等。支持 Docker ，数据本地/云端自持。集成微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 等渠道智能推送。

17. **[ruflo](https://github.com/ruvnet/ruflo)** - ⭐ 59,039
   🌊 The leading agent meta-harness for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning swarm intelligence, RAG integration, and native Claude Code / Codex Integration

18. **[context7](https://github.com/upstash/context7)** - ⭐ 57,201
   Context7 Platform -- Up-to-date code documentation for LLMs and AI code editors

19. **[mempalace](https://github.com/MemPalace/mempalace)** - ⭐ 55,412
   The best-benchmarked open-source AI memory system. And it's free.

20. **[LocalAI](https://github.com/mudler/LocalAI)** - ⭐ 46,794
   LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

21. **[JeecgBoot](https://github.com/jeecgboot/JeecgBoot)** - ⭐ 46,709
   AI 低代码平台「低代码 + 零代码」双驱动！低代码可一键生成前后端代码;零代码可 5 分钟搭建系统;AI Skills 一句话画流程、设计表单、生成整套系统。内置 AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领「AI 生成 → 在线配置 → 代码生成 → 手工合并->AI修改」开发模式，消除 Java 项目 80% 的重复工作，提效而不失灵活。

22. **[CowAgent](https://github.com/zhayujie/CowAgent)** - ⭐ 45,236
   Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-model, multi-channel. Lightweight, extensible, one-line install. (formerly chatgpt-on-wechat)

23. **[chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** - ⭐ 43,411
   Chrome DevTools for coding agents

24. **[antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)** - ⭐ 40,409
   Installable GitHub library of 1,500+ agentic skills for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and more. Includes specialized plugins, installer CLI, bundles, workflows, and official/community skill collections.

25. **[mempalace](https://github.com/milla-jovovich/mempalace)** - ⭐ 40,200
   The highest-scoring AI memory system ever benchmarked. And it's free.

26. **[LibreChat](https://github.com/danny-avila/LibreChat)** - ⭐ 38,931
   Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active

27. **[cherry-studio](https://github.com/CherryHQ/cherry-studio)** - ⭐ 37,347
   Cherry Studio boosts your productivity with unified AI access, Agent capabilities, and 300+ assistants in one desktop application.

28. **[goose](https://github.com/block/goose)** - ⭐ 37,288
   an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

29. **[UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)** - ⭐ 36,316
   The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra

30. **[ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub)** - ⭐ 35,688
   In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

31. **[PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate)** - ⭐ 34,761
   [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/MCP/Docker/Zotero

32. **[AstrBot](https://github.com/AstrBotDevs/AstrBot)** - ⭐ 34,482
   AI Agent Assistant & development framework that integrates lots of IM platforms, LLMs, plugins and AI feature, and can be your openclaw alternative. ✨

33. **[playwright-mcp](https://github.com/microsoft/playwright-mcp)** - ⭐ 33,792
   Playwright MCP server

34. **[1Panel](https://github.com/1Panel-dev/1Panel)** - ⭐ 33,113
   🔥 1Panel provides an intuitive web interface and MCP Server to manage websites, files, containers, databases, and LLMs on a Linux server.

35. **[nacos](https://github.com/alibaba/nacos)** - ⭐ 33,016
   an easy-to-use dynamic service discovery, configuration and service management platform for building AI cloud native applications.

36. **[ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)** - ⭐ 31,435
   Learn it. Build it. Ship it for others.

37. **[github-mcp-server](https://github.com/github/github-mcp-server)** - ⭐ 30,591
   GitHub's official MCP Server

38. **[claude-plugins-official](https://github.com/anthropics/claude-plugins-official)** - ⭐ 29,941
   Official, Anthropic-managed directory of high quality Claude Code Plugins.

39. **[composio](https://github.com/ComposioHQ/composio)** - ⭐ 28,732
   Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to help you build AI agents that turn intent into action.

40. **[gpt-researcher](https://github.com/assafelovic/gpt-researcher)** - ⭐ 27,649
   An autonomous agent that conducts deep research on any data using any LLM providers

41. **[xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)** - ⭐ 27,250
   An MCP-based chatbot | 一个基于MCP的聊天机器人

42. **[Agent-Reach](https://github.com/Panniantong/Agent-Reach)** - ⭐ 26,441
   Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

43. **[repomix](https://github.com/yamadashy/repomix)** - ⭐ 26,196
   📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

44. **[kratos](https://github.com/go-kratos/kratos)** - ⭐ 25,729
   Your ultimate Go microservices framework for the cloud-native era.

45. **[fastmcp](https://github.com/PrefectHQ/fastmcp)** - ⭐ 25,602
   🚀 The fast, Pythonic way to build MCP servers and clients.

46. **[serena](https://github.com/oraios/serena)** - ⭐ 25,267
   A powerful MCP toolkit for coding, providing semantic retrieval and editing capabilities  - the IDE for your agent

47. **[mastra](https://github.com/mastra-ai/mastra)** - ⭐ 24,974
   From the team behind Gatsby, Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack.

48. **[gin-vue-admin](https://github.com/flipped-aurora/gin-vue-admin)** - ⭐ 24,777
   🚀Vite+Vue3+Gin拥有AI辅助的基础开发平台，企业级业务AI+开发解决方案，内置mcp辅助服务，内置skills管理，支持TS和JS混用。它集成了JWT鉴权、权限管理、动态路由、显隐可控组件、分页封装、多点登录拦截、资源权限、上传下载、代码生成器、表单生成器和可配置的导入导出等开发必备功能。

49. **[headroom](https://github.com/chopratejas/headroom)** - ⭐ 23,501
   Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, same answers. Library, proxy, MCP server.

50. **[python-sdk](https://github.com/modelcontextprotocol/python-sdk)** - ⭐ 23,296
   The official Python SDK for Model Context Protocol servers and clients

51. **[fastmcp](https://github.com/jlowin/fastmcp)** - ⭐ 22,902
   🚀 The fast, Pythonic way to build MCP servers and clients

52. **[activepieces](https://github.com/activepieces/activepieces)** - ⭐ 22,714
   AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • AI Automation / AI Agent with MCPs • AI Workflows & AI Agents • MCPs for AI Agents

53. **[blender-mcp](https://github.com/ahujasid/blender-mcp)** - ⭐ 22,618

54. **[GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents)** - ⭐ 22,513
   50+ tutorials and implementations for Generative AI Agent techniques, from basic conversational bots to complex multi-agent systems.

55. **[n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** - ⭐ 21,683
   A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you

56. **[MaxKB](https://github.com/1Panel-dev/MaxKB)** - ⭐ 21,229
   🔥 MaxKB is an open-source platform for building enterprise-grade agents.  强大易用的开源企业级智能体平台。

57. **[agents-towards-production](https://github.com/NirDiamant/agents-towards-production)** - ⭐ 20,699
   End-to-end, code-first tutorials for building production-grade GenAI agents. From prototype to enterprise deployment.

58. **[page-agent](https://github.com/alibaba/page-agent)** - ⭐ 18,497
   JavaScript in-page GUI agent. Control web interfaces with natural language.

59. **[code-review-graph](https://github.com/tirth8205/code-review-graph)** - ⭐ 18,400
   Local-first code intelligence graph for MCP and CLI. Builds a persistent map of your codebase so AI coding tools read only what matters, with benchmarked context reductions on reviews and large-repo workflows.

60. **[FunASR](https://github.com/modelscope/FunASR)** - ⭐ 17,851
   Industrial-grade speech recognition toolkit: 170x realtime, 50+ languages, speaker diarization, emotion detection, streaming, and OpenAI-compatible API.

61. **[openfang](https://github.com/RightNow-AI/openfang)** - ⭐ 17,809
   Open-source Agent Operating System

62. **[nuclear](https://github.com/nukeop/nuclear)** - ⭐ 17,784
   Streaming music player that finds free music for you

63. **[context-mode](https://github.com/mksglu/context-mode)** - ⭐ 17,207
   Context window optimization for AI coding agents. Sandboxes tool output, 98% reduction. 15 platforms

64. **[Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)** - ⭐ 16,517
   Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc.

65. **[mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** - ⭐ 16,511
   This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration.

66. **[mcp-toolbox](https://github.com/googleapis/mcp-toolbox)** - ⭐ 15,591
   MCP Toolbox for Databases is an open source MCP server for databases.

67. **[Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)** - ⭐ 15,417
   754 structured cybersecurity skills for AI agents · Mapped to 5 frameworks: MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND & NIST AI RMF · agentskills.io standard · Works with Claude Code, GitHub Copilot, Codex CLI, Cursor, Gemini CLI & 20+ platforms · 26 security domains · Apache 2.0

68. **[trigger.dev](https://github.com/triggerdotdev/trigger.dev)** - ⭐ 15,312
   Trigger.dev – build and deploy fully‑managed AI agents and workflows

69. **[claude-flow](https://github.com/ruvnet/claude-flow)** - ⭐ 15,103
   🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

70. **[Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP)** - ⭐ 15,084
   MCP server to provide Figma layout information to AI coding agents like Cursor

71. **[electerm](https://github.com/electerm/electerm)** - ⭐ 14,257
   📻Terminal/ssh/sftp/ftp/telnet/serialport/RDP/VNC/Spice client(linux, mac, win)

72. **[OpenMetadata](https://github.com/open-metadata/OpenMetadata)** - ⭐ 14,172
   The Open Context Layer for Data and AI ,  OpenMetadata is the open platform for building trusted data context and business semantics for humans, AI assistants, and agents.

73. **[xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp)** - ⭐ 14,110
   MCP for xiaohongshu.com

74. **[Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)** - ⭐ 14,058
   Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with automatic conflict detection

75. **[genai-toolbox](https://github.com/googleapis/genai-toolbox)** - ⭐ 13,975
   MCP Toolbox for Databases is an open source MCP server for databases.

76. **[memU](https://github.com/NevaMind-AI/memU)** - ⭐ 13,836
   The memory harness for proactive AI agents — structured storage, intent capture, 10x token reduction.

77. **[casdoor](https://github.com/casdoor/casdoor)** - ⭐ 13,760
   An open-source Agent-first Identity and Access Management (IAM) /LLM MCP & agent gateway and auth server with web UI supporting OpenClaw, MCP, OAuth, OIDC, SAML, CAS, LDAP, SCIM, WebAuthn, TOTP, MFA, Face ID, Google Workspace, Azure AD

78. **[filestash](https://github.com/mickael-kerjean/filestash)** - ⭐ 13,423
   :file_folder: What Dropbox should have been if it was based on SFTP, S3, FTP, SMB, NFS, WebDAV, Git, and more

79. **[awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps)** - ⭐ 12,776
   A collection of projects showcasing RAG, agents, workflows, and other AI use cases

80. **[typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** - ⭐ 12,647
   The official TypeScript SDK for Model Context Protocol servers and clients

81. **[gateway](https://github.com/Portkey-AI/gateway)** - ⭐ 12,041
   A blazing fast AI Gateway with integrated guardrails. Route to 1,600+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.

82. **[Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)** - ⭐ 11,966
   ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea discovery, and experiment automation. No framework, no lock-in — works with Claude Code, Codex, OpenClaw, or any LLM agent.

83. **[oh-my-pi](https://github.com/can1357/oh-my-pi)** - ⭐ 11,956
   ⌥  AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, browser, subagents, and more

84. **[kubeshark](https://github.com/kubeshark/kubeshark)** - ⭐ 11,951
   eBPF-powered network observability for Kubernetes. Indexes L4/L7 traffic with full K8s context, decrypts TLS without keys. Queryable by AI agents via MCP and humans via dashboard.

85. **[fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)** - ⭐ 11,911
   Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth!

86. **[mcp-chrome](https://github.com/hangwin/mcp-chrome)** - ⭐ 11,902
   Chrome MCP Server is a Chrome extension-based Model Context Protocol (MCP) server that exposes your Chrome browser functionality to AI assistants like Claude, enabling complex browser automation, content analysis, and semantic search.

87. **[Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** - ⭐ 11,839
   "Vibe-Trading: Your Personal Trading Agent"

88. **[claude-context](https://github.com/zilliztech/claude-context)** - ⭐ 11,823
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

89. **[superset](https://github.com/superset-sh/superset)** - ⭐ 11,749
   Code Editor for the AI Agents Era - Run an army of Claude Code, Codex, etc. on your machine

90. **[pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server)** - ⭐ 11,594
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

91. **[XHS-Downloader](https://github.com/JoeanAmier/XHS-Downloader)** - ⭐ 11,522
   小红书（XiaoHongShu、RedNote）链接提取/作品采集工具：提取账号发布、收藏、点赞、专辑作品链接；提取搜索结果作品、用户链接；采集小红书作品信息；提取小红书作品下载地址；下载小红书作品文件

92. **[nginx-ui](https://github.com/0xJacky/nginx-ui)** - ⭐ 11,206
   Yet another WebUI for Nginx

93. **[unity-mcp](https://github.com/CoplayDev/unity-mcp)** - ⭐ 10,579
   Unity MCP acts as a bridge between AI assistants and your Unity Editor. Give your LLM tools to manage assets, control scenes, edit scripts, and automate tasks within Unity.

94. **[mcp-use](https://github.com/mcp-use/mcp-use)** - ⭐ 10,089
   The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & MCP Servers for AI Agents.

95. **[inspector](https://github.com/modelcontextprotocol/inspector)** - ⭐ 10,052
   Visual testing tool for MCP servers

96. **[zen-mcp-server](https://github.com/BeehiveInnovations/zen-mcp-server)** - ⭐ 9,890
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

97. **[MemOS](https://github.com/MemTensor/MemOS)** - ⭐ 9,809
   Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings

98. **[xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)** - ⭐ 9,791
   本项目为xiaozhi-esp32提供后端服务，帮助您快速搭建ESP32设备控制服务器。Backend service for xiaozhi-esp32, helps you quickly build an ESP32 device control server.

99. **[voltagent](https://github.com/VoltAgent/voltagent)** - ⭐ 9,560
   AI Agent Engineering Platform built on an Open Source TypeScript AI Agent Framework

100. **[hexstrike-ai](https://github.com/0x4m4/hexstrike-ai)** - ⭐ 9,529
   HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, GPT, Copilot, etc.) autonomously run 150+ cybersecurity tools for automated pentesting, vulnerability discovery, bug bounty automation, and security research. Seamlessly bridge LLMs with real-world offensive security capabilities.

101. **[ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp)** - ⭐ 9,309
   AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP.

102. **[mcp](https://github.com/awslabs/mcp)** - ⭐ 9,254
   Open source MCP Servers for AWS

103. **[GhidraMCP](https://github.com/LaurieWired/GhidraMCP)** - ⭐ 9,196
   MCP Server for Ghidra

104. **[mcp-go](https://github.com/mark3labs/mcp-go)** - ⭐ 8,797
   A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

105. **[awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources)** - ⭐ 8,521
   🧑‍🚀 全世界最好的LLM资料总结（多模态生成、Agent、辅助编程、AI审稿、数据处理、模型训练、模型推理、o1 模型、MCP、小语言模型、视觉语言模型） | Summary of the world's best LLM resources.

106. **[kreuzberg](https://github.com/kreuzberg-dev/kreuzberg)** - ⭐ 8,482
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, images, and structured information from PDFs, Office documents, images, and 97+ formats. Available for Rust, Python, Ruby, Java, Go, PHP, Elixir, C#, R, C, TypeScript (Node/Bun/Wasm/Deno)- or use via CLI, REST API, or MCP server.

107. **[mcp-agent](https://github.com/lastmile-ai/mcp-agent)** - ⭐ 8,369
   Build effective agents using Model Context Protocol and simple workflow patterns

108. **[git-mcp](https://github.com/idosal/git-mcp)** - ⭐ 8,161
   Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project

109. **[webiny-js](https://github.com/webiny/webiny-js)** - ⭐ 7,992
   Open-source, self-hosted CMS platform on AWS serverless (Lambda, DynamoDB, S3). TypeScript framework with multi-tenancy, lifecycle hooks, GraphQL API, and AI-assisted development via MCP server. Built for developers at large organizations.

110. **[Upsonic](https://github.com/Upsonic/Upsonic)** - ⭐ 7,877
   Build autonomous AI agents in Python.

111. **[QuantDinger](https://github.com/brokermr810/QuantDinger)** - ⭐ 7,855
   AI quantitative trading platform for crypto, stocks, and forex with backtesting, live trading, market data, and multi-agent research.vibe-trading ,trading-agents,ai-trader,ai-trading

112. **[EverOS](https://github.com/EverMind-AI/EverOS)** - ⭐ 7,323
   Self-evolving memory across Agent and platform. The one portable memory layer for every agent they use - Claude Code, Codex, OpenClaw, Hermes, and more

113. **[oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)** - ⭐ 7,289
   #1 OpenCode Plugin- Battery included. ASYNC SUBAGENTS (YES LIKE CLAUDE CODE) · Curated agents with proper models · Crafted tools like LSP/AST included · Curated MCPs · Claude Code Compatible Layer — Steroids for your OpenCode. The Best LLM Agent Experience is Here.

114. **[Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH)** - ⭐ 7,268
   MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients

115. **[browser-tools-mcp](https://github.com/AgentDeskAI/browser-tools-mcp)** - ⭐ 7,236
   Monitor browser logs directly from Cursor and other MCP compatible IDEs.

116. **[jcode](https://github.com/1jehuang/jcode)** - ⭐ 7,019
   Coding Agent Harness

117. **[registry](https://github.com/modelcontextprotocol/registry)** - ⭐ 6,916
   A community driven registry service for Model Context Protocol (MCP) servers.

118. **[cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp)** - ⭐ 6,830
   TalkToFigma: MCP integration between AI Agent (Cursor, Claude Code) and Figma, allowing Agentic AI to communicate with Figma for reading designs and modifying them programmatically.

119. **[mcp](https://github.com/BrowserMCP/mcp)** - ⭐ 6,656
   Browser MCP is a Model Context Provider (MCP) server that allows AI applications to control your browser

120. **[unstract](https://github.com/Zipstack/unstract)** - ⭐ 6,647
   LLM-Driven Extraction of Unstructured Data — Built for API Deployments & ETL Pipeline Workflows

121. **[firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)** - ⭐ 6,543
   🔥 Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients.

122. **[microsandbox](https://github.com/superradcompany/microsandbox)** - ⭐ 6,485
   🧱 easy, fast, local microvms for untrusted workloads. use as dev container, ai agent sandbox,  ci/cd, and more.

123. **[awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients)** - ⭐ 6,471
   A collection of MCP clients.

124. **[open-multi-agent](https://github.com/open-multi-agent/open-multi-agent)** - ⭐ 6,365
   From a goal to a task DAG, automatically. TypeScript-native multi-agent orchestration.

125. **[DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP)** - ⭐ 6,160
   This is MCP server for Claude that gives it terminal control, file system search and diff file editing capabilities

126. **[refly](https://github.com/refly-ai/refly)** - ⭐ 6,135
   The first open-source agent skills builder. 🦞

127. **[harness-sdk](https://github.com/strands-agents/harness-sdk)** - ⭐ 6,108
   A model-driven approach to building AI agents in just a few lines of code.

128. **[open-multi-agent](https://github.com/JackChen-me/open-multi-agent)** - ⭐ 6,083
   From a goal to a task DAG, automatically. TypeScript-native multi-agent orchestration with MCP and live tracing. Three runtime dependencies.

129. **[OmniRoute](https://github.com/diegosouzapw/OmniRoute)** - ⭐ 6,053
   Never stop coding. Free AI gateway: one endpoint, 160+ providers (50+ free), connect Claude Code, Codex, Cursor, Cline & Copilot to FREE Claude/GPT/Gemini. RTK+Caveman stacked compression saves 15-95% tokens, smart auto-fallback, MCP/A2A, multimodal APIs, Desktop/PWA.

130. **[Everywhere](https://github.com/Sylinko/Everywhere)** - ⭐ 6,041
   On-screen aware AI assistant for your desktop. Uses current app context, multiple LLMs, and MCP tools to help you act across apps.

131. **[CodePilot](https://github.com/op7418/CodePilot)** - ⭐ 5,997
   A multi-model AI agent desktop client — connect any AI provider, extend with MCP & skills, control from your phone. Built with Electron + Next.js.

132. **[sdk-python](https://github.com/strands-agents/sdk-python)** - ⭐ 5,996
   A model-driven approach to building AI agents in just a few lines of code.

133. **[stitch-skills](https://github.com/google-labs-code/stitch-skills)** - ⭐ 5,991
   A library of Agent Skills designed to work with the Stitch MCP server. Each skill follows the Agent Skills open standard, for compatibility with coding agents such as Antigravity, Gemini CLI, Claude Code, Cursor.

134. **[Windows-MCP](https://github.com/CursorTouch/Windows-MCP)** - ⭐ 5,943
   MCP Server for Computer Use in Windows

135. **[Everywhere](https://github.com/DearVa/Everywhere)** - ⭐ 5,931
   Context-aware AI assistant for your desktop. Ready to respond intelligently, seamlessly integrating multiple LLMs and MCP tools.

136. **[Horizon](https://github.com/Thysrael/Horizon)** - ⭐ 5,902
   📡 Your own AI-powered news radar. Generates daily briefings in English & Chinese. | 用 AI 构建你专属的新闻雷达

137. **[XcodeBuildMCP](https://github.com/getsentry/XcodeBuildMCP)** - ⭐ 5,893
   A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects.

138. **[whatsapp-mcp](https://github.com/lharries/whatsapp-mcp)** - ⭐ 5,770
   WhatsApp MCP server

139. **[jscpd](https://github.com/kucherenko/jscpd)** - ⭐ 5,760
   Copy/paste detector for programming source code, supports 223 formats. AI-ready with token-efficient reporter, skill and MCP server.

140. **[osaurus](https://github.com/osaurus-ai/osaurus)** - ⭐ 5,760
   Own your AI. The native macOS harness for AI agents -- any model, persistent memory, autonomous execution, cryptographic identity. Built in Swift. Fully offline. Open source.

141. **[bb-browser](https://github.com/epiral/bb-browser)** - ⭐ 5,752
   Your browser is the API. CLI + MCP server for AI agents to control Chrome with your login state.

142. **[klavis](https://github.com/Klavis-AI/klavis)** - ⭐ 5,747
   Klavis AI:  MCP integration platforms that let AI agents use tools reliably at any scale

143. **[learn-ai-engineering](https://github.com/ashishps1/learn-ai-engineering)** - ⭐ 5,695
   Learn AI and LLMs from scratch using free resources

144. **[bifrost](https://github.com/maximhq/bifrost)** - ⭐ 5,691
   Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.

145. **[awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)** - ⭐ 5,590
   Awesome MCP Servers - A curated list of Model Context Protocol servers

146. **[UltraRAG](https://github.com/OpenBMB/UltraRAG)** - ⭐ 5,579
   A Low-Code MCP Framework for Building Complex and Innovative RAG Pipelines

147. **[mcp-playwright](https://github.com/executeautomation/mcp-playwright)** - ⭐ 5,550
   Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in Claude Desktop, Cline, Cursor IDE and More 🔌

148. **[awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)** - ⭐ 5,503
   Tutorials, Guides and Agent Skills Directories

149. **[mcp-atlassian](https://github.com/sooperset/mcp-atlassian)** - ⭐ 5,387
   MCP server for Atlassian tools (Confluence, Jira)

150. **[mission-control](https://github.com/builderz-labs/mission-control)** - ⭐ 5,278
   Self-hosted AI agent orchestration platform: dispatch tasks, run multi-agent workflows, monitor spend, and govern operations from one mission control dashboard.

151. **[rikkahub](https://github.com/rikkahub/rikkahub)** - ⭐ 5,263
   RikkaHub is an Android APP that supports for multiple LLM providers.

152. **[5ire](https://github.com/nanbingxyz/5ire)** - ⭐ 5,241
   5ire is a cross-platform desktop AI assistant, MCP client. It compatible with major service providers,  supports local knowledge base and  tools via model context protocol servers .

153. **[openagent](https://github.com/the-open-agent/openagent)** - ⭐ 5,231
   ⚡️next-generation personal AI assistant powered by LLM, RAG and agent loops, supporting computer-use, browser-use and coding agent, demo: https://demo.openagentai.org

154. **[superpowers-zh](https://github.com/jnMetaCode/superpowers-zh)** - ⭐ 5,203
   🦸 AI 编程超能力 · 中文增强版 — superpowers（116k+ ⭐）完整汉化 + 6 个中国原创 skills，让 Claude Code / Copilot CLI / Hermes Agent / Cursor / Windsurf / Kiro / Gemini CLI 等 16 款 AI 编程工具真正会干活

155. **[hooker](https://github.com/CreditTone/hooker)** - ⭐ 5,181
   🔥🔥 hooker is a Frida-based reverse engineering toolkit for Android. It offers a user-friendly CLI, universal scripts, auto hook generation, memory roaming to detect activities/services, one-click SOCKS5 proxy setup, Frida JustTrustMe, and BoringSSL unpinning for all apps.

156. **[mobile-mcp](https://github.com/mobile-next/mobile-mcp)** - ⭐ 5,181
   Model Context Protocol Server for Mobile Automation and Scraping (iOS, Android, Emulators, Simulators and Real Devices)

157. **[astron-rpa](https://github.com/iflytek/astron-rpa)** - ⭐ 5,177
   Agent-ready RPA suite with out-of-the-box automation tools. Built for individuals and enterprises.

158. **[microsandbox](https://github.com/zerocore-ai/microsandbox)** - ⭐ 5,174
   opensource secure local-first sandboxes for ai agents

159. **[semble](https://github.com/MinishLab/semble)** - ⭐ 5,081
   Fast and Accurate Code Search for Agents. Uses ~98% fewer tokens than grep+read

160. **[magic-mcp](https://github.com/21st-dev/magic-mcp)** - ⭐ 5,079
   It's like v0 but in your Cursor/WindSurf/Cline. 21st dev Magic MCP server for working with your frontend like Magic

161. **[sandbox](https://github.com/agent-infra/sandbox)** - ⭐ 5,071
   All-in-One Sandbox for AI Agents that combines Browser, Shell, File, MCP and VSCode Server in a single Docker container.

162. **[qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm)** - ⭐ 5,043
   Claude Skill: Multi-source content processor for NotebookLM. Supports WeChat articles, web pages, YouTube, PDF, Markdown, search queries → Podcast/PPT/MindMap/Quiz etc.

163. **[gaianet-node](https://github.com/GaiaNet-AI/gaianet-node)** - ⭐ 5,027
   Install, run and deploy your own decentralized AI agent service

164. **[unidbg](https://github.com/zhkl0228/unidbg)** - ⭐ 5,011
   Allows you to emulate an Android native library, and an experimental  iOS emulation

165. **[FinanceToolkit](https://github.com/JerBouma/FinanceToolkit)** - ⭐ 4,952
   Transparent and Efficient Financial Analysis

166. **[mcp-ui](https://github.com/MCP-UI-Org/mcp-ui)** - ⭐ 4,904
   UI over MCP. Create next-gen UI experiences with the protocol and SDK!

167. **[mockserver-monorepo](https://github.com/mock-server/mockserver-monorepo)** - ⭐ 4,888
   MockServer enables easy mocking of any system you integrate with via HTTP or HTTPS with clients written in Java, JavaScript and Ruby.  MockServer also includes a proxy that introspects all proxied traffic including encrypted SSL traffic and supports Port Forwarding, Web Proxying (i.e. HTTP proxy), HTTPS Tunneling Proxying (using HTTP CONNECT) and SOCKS Proxying (i.e. dynamic port forwarding).

168. **[Kiln](https://github.com/Kiln-AI/Kiln)** - ⭐ 4,877
   Build, Evaluate, and Optimize AI Systems. Includes evals, RAG, agents, fine-tuning, synthetic data generation, dataset management, MCP, and more.

169. **[solace-agent-mesh](https://github.com/SolaceLabs/solace-agent-mesh)** - ⭐ 4,873
   An event-driven framework designed to build and orchestrate multi-agent AI systems. It enables seamless integration of AI agents with real-world data sources and systems, facilitating complex, multi-step workflows.

170. **[notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli)** - ⭐ 4,851
   Programmatic access to Google NotebookLM — via command-line interface (CLI), Model Context Protocol (MCP) server, and AI agent skills.

171. **[byterover-cli](https://github.com/campfirein/byterover-cli)** - ⭐ 4,844
   ByteRover CLI (brv) - The portable memory layer for  autonomous coding agents (formerly Cipher)

172. **[aci](https://github.com/aipotheosis-labs/aci)** - ⭐ 4,800
   ACI.dev is the open source tool-calling platform that hooks up 600+ tools into any agentic IDE or custom AI agent through direct function calling or a unified MCP server. The birthplace of VibeOps.

173. **[excalidraw-mcp](https://github.com/excalidraw/excalidraw-mcp)** - ⭐ 4,708
   Fast and streamable Excalidraw MCP App

174. **[Peekaboo](https://github.com/openclaw/Peekaboo)** - ⭐ 4,695
   Peekaboo is a macOS CLI & optional MCP server that enables AI agents to capture screenshots of applications, or the entire system, with optional visual question answering through local or remote AI models.

175. **[go-sdk](https://github.com/modelcontextprotocol/go-sdk)** - ⭐ 4,675
   The official Go SDK for Model Context Protocol servers and clients. Maintained in collaboration with Google.

176. **[Olares](https://github.com/beclab/Olares)** - ⭐ 4,667
   Olares: An Open-Source Personal Cloud to Reclaim Your Data

177. **[PPTAgent](https://github.com/icip-cas/PPTAgent)** - ⭐ 4,635
   An Agentic Framework for Reflective PowerPoint Generation

178. **[mcporter](https://github.com/openclaw/mcporter)** - ⭐ 4,620
   Call MCPs via TypeScript, masquerading as simple TypeScript API. Or package them as cli.

179. **[deep-research](https://github.com/u14app/deep-research)** - ⭐ 4,609
   Use any LLMs (Large Language Models) for Deep Research. Support SSE API and MCP server.

180. **[exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)** - ⭐ 4,565
   Exa MCP for web search and web crawling!

181. **[casibase](https://github.com/casibase/casibase)** - ⭐ 4,503
   ⚡️AI Cloud OS: Open-source enterprise-level AI knowledge base and MCP (model-context-protocol)/A2A (agent-to-agent) management platform with admin UI, user management and Single-Sign-On⚡️, supports ChatGPT, Claude, Llama, Ollama, HuggingFace, etc., chat bot demo: https://ai.casibase.com, admin UI demo: https://ai-admin.casibase.com

182. **[m_flow](https://github.com/FlowElement-ai/m_flow)** - ⭐ 4,476
   A bio-inspired cognitive memory engine — a new paradigm for Graph RAG.

183. **[CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI)** - ⭐ 4,434
   CyberStrikeAI is an AI-native security testing platform built in Go. It integrates 100+ security tools, an intelligent orchestration engine, role-based testing with predefined security roles, a skills system with specialized testing skills, and comprehensive lifecycle management capabilities.

184. **[ouroboros](https://github.com/Q00/ouroboros)** - ⭐ 4,422
   Agent OS: Stop prompting. Start specifying.

185. **[notion-mcp-server](https://github.com/makenotion/notion-mcp-server)** - ⭐ 4,413
   Official Notion MCP Server

186. **[claude-seo](https://github.com/AgriciDaniel/claude-seo)** - ⭐ 4,396
   Universal SEO skill for Claude Code. 19 sub-skills, 12 subagents, 3 extensions (DataForSEO, Firecrawl, Banana). Technical SEO, E-E-A-T, schema, GEO/AEO, backlinks, local SEO, maps intelligence, Google APIs, and PDF/Excel reporting.

187. **[drawio-mcp](https://github.com/jgraph/drawio-mcp)** - ⭐ 4,363

188. **[dograh](https://github.com/dograh-hq/dograh)** - ⭐ 4,357
   Open source voice AI platform. Self-hosted alternative to Vapi and Retell. On Prem, BYOK across  Speech to Speech or LLM/STT/TTS, with a visual workflow builder, MCP native and telephony support.

189. **[lemonade](https://github.com/lemonade-sdk/lemonade)** - ⭐ 4,331
   Lemonade helps users discover and run local AI apps by serving optimized LLMs right from their own GPUs and NPUs. Join our discord: https://discord.gg/5xXzkMu8Zk

190. **[csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk)** - ⭐ 4,325
   The official C# SDK for Model Context Protocol servers and clients. Maintained in collaboration with Microsoft.

191. **[engram](https://github.com/Gentleman-Programming/engram)** - ⭐ 4,301
   Persistent memory system for AI coding agents. Agent-agnostic Go binary with SQLite + FTS5, MCP server, HTTP API, CLI, and TUI.

192. **[claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)** - ⭐ 4,291
   Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CLI, and OpenCode across ideation, coding, experiments, writing, and publication.

193. **[claude-code-guide](https://github.com/zebbern/claude-code-guide)** - ⭐ 4,287
   Claude Code Guide - Setup, Commands, workflows, agents, skills & tips-n-tricks go from beginner to power user!

194. **[mcporter](https://github.com/steipete/mcporter)** - ⭐ 4,284
   Call MCPs via TypeScript, masquerading as simple TypeScript API. Or package them as cli.

195. **[httprunner](https://github.com/httprunner/httprunner)** - ⭐ 4,280
   HttpRunner 是一款开源的 API/UI 测试框架，简单易用，功能强大，具有丰富的插件化机制和高度的可扩展能力。

196. **[mcpo](https://github.com/open-webui/mcpo)** - ⭐ 4,252
   A simple, secure MCP-to-OpenAPI proxy server

197. **[spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** - ⭐ 4,226
   A Model Context Protocol (MCP) server that provides structured spec-driven development workflow tools for AI-assisted software development, featuring a real-time web dashboard and VSCode extension for monitoring and managing your project's progress directly in your development environment.

198. **[learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai)** - ⭐ 4,220
   Learn Agentic AI using Dapr Agentic Cloud Ascent (DACA) Design Pattern and Agent-Native Cloud Technologies: OpenAI Agents SDK, Memory, MCP, A2A, Knowledge Graphs, Dapr, Rancher Desktop, and Kubernetes.

199. **[mcp](https://github.com/google/mcp)** - ⭐ 4,189
   Google 💚 MCP

200. **[mcp-server-chart](https://github.com/antvis/mcp-server-chart)** - ⭐ 4,150
   🤖 A visualization mcp & skills contains 25+ visual charts using @antvis. Using for chart generation and data analysis.

201. **[awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)** - ⭐ 4,150
   A curated list of Model Context Protocol (MCP) servers

202. **[XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP)** - ⭐ 4,145
   A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects.

203. **[godot-mcp](https://github.com/Coding-Solo/godot-mcp)** - ⭐ 4,129
   MCP server for interfacing with Godot game engine. Provides tools for launching the editor, running projects, and capturing debug output.

204. **[ciso-assistant-community](https://github.com/intuitem/ciso-assistant-community)** - ⭐ 4,128
   CISO Assistant is a one-stop-shop GRC platform for Risk Management, AppSec, Compliance & Audit, TPRM, BIA, Privacy, and Reporting. It supports 150+ global frameworks with automatic control mapping, including ISO 27001, NIST CSF, SOC 2, CIS, PCI DSS, NIS2, DORA, GDPR, HIPAA, CMMC, and more.

205. **[go-whatsapp-web-multidevice](https://github.com/aldinokemal/go-whatsapp-web-multidevice)** - ⭐ 4,071
   GOWA - WhatsApp REST API with support for UI, Multi Account, Webhooks, and MCP, and Chatwoot. Built with Golang for efficient memory use.

206. **[opensquilla](https://github.com/opensquilla/opensquilla)** - ⭐ 3,993
   OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

207. **[directories](https://github.com/leerob/directories)** - ⭐ 3,930
   Find rules and MCP servers

208. **[community-plugins](https://github.com/cursor/community-plugins)** - ⭐ 3,928
   Find rules and MCP servers

209. **[excel-mcp-server](https://github.com/haris-musa/excel-mcp-server)** - ⭐ 3,922
   A Model Context Protocol server for Excel file manipulation

210. **[telegram-search](https://github.com/groupultra/telegram-search)** - ⭐ 3,918
   🔍 导出并模糊搜索 Telegram 聊天记录 | Export and fuzzy search your Telegram chat history

211. **[directories](https://github.com/pontusab/directories)** - ⭐ 3,896
   The Cursor & Windsurf community, find rules and MCPs

212. **[mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** - ⭐ 3,887
   MCP server that interacts with Obsidian via the Obsidian rest API community plugin

213. **[octelium](https://github.com/octelium/octelium)** - ⭐ 3,876
   A next-gen FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA platform, API/AI/MCP gateway, a PaaS, an ngrok-alternative and a homelab infrastructure.

214. **[AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard)** - ⭐ 3,874
   A full-stack AI Red Teaming platform securing AI ecosystems via OpenClaw Security Scan, Agent Scan, Skills Scan, MCP scan, AI Infra scan and LLM jailbreak evaluation.

215. **[mcp-context-forge](https://github.com/IBM/mcp-context-forge)** - ⭐ 3,871
   An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/gRPC APIs, exposing a unified endpoint with centralized discovery, guardrails and management. Optimizes Agent & Tool calling, and supports plugins.

216. **[mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** - ⭐ 3,851

217. **[archestra](https://github.com/archestra-ai/archestra)** - ⭐ 3,825
   Enterprise AI Platform with guardrails, MCP registry, gateway & orchestrator

218. **[fast-agent](https://github.com/evalstate/fast-agent)** - ⭐ 3,818
   Code, Build and Evaluate agents - excellent Model and Skills/MCP/ACP Support

219. **[Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3)** - ⭐ 3,808
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

220. **[rocketride-server](https://github.com/rocketride-org/rocketride-server)** - ⭐ 3,799
   High-performance AI pipeline engine with a C++ core and 50+ Python-extensible nodes. Build, debug, and scale LLM workflows with 13+ model providers, 8+ vector databases, and agent orchestration, all from your IDE. Includes VS Code extension, TypeScript/Python SDKs, and Docker deployment.

221. **[mcp-feedback-enhanced](https://github.com/Minidoracat/mcp-feedback-enhanced)** - ⭐ 3,792
   Enhanced MCP server for interactive user feedback and command execution in AI-assisted development, featuring dual interface support (Web UI and Desktop Application) with intelligent environment detection and cross-platform compatibility.

222. **[atmosphere](https://github.com/Atmosphere/atmosphere)** - ⭐ 3,779
   Real-time transport layer for Java AI agents. Build once with @Agent — deliver over WebSocket, SSE, gRPC, and WebTransport/HTTP3. Talk MCP, A2A and AG-UI.

223. **[zotero-mcp](https://github.com/54yyyu/zotero-mcp)** - ⭐ 3,763
   Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss papers, get summaries, analyze citations, and more.

224. **[CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext)** - ⭐ 3,707
   An MCP server plus a CLI tool that indexes local code into a graph database to provide context to AI assistants.

225. **[OB1](https://github.com/NateBJones-Projects/OB1)** - ⭐ 3,661
   Open Brain — The infrastructure layer for your thinking. One database, one AI gateway, one chat channel — any AI plugs in. No middleware, no SaaS.

226. **[cipher](https://github.com/campfirein/cipher)** - ⭐ 3,637
   Byterover Cipher is an opensource memory layer specifically designed for coding agents. Compatible with Cursor, Codex, Claude Code, Windsurf, Cline, Claude Desktop, Gemini CLI, AWS's Kiro, VS Code, Roo Code, Trae, Amp Code and Warp through MCP. Built by https://byterover.dev/

227. **[awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents)** - ⭐ 3,636
   162 production-ready AI agent templates for OpenClaw. SOUL.md configs across 19 categories. Submit yours!

228. **[core](https://github.com/opensumi/core)** - ⭐ 3,631
   A framework helps you quickly build AI Native IDE products. MCP Client, supports Model Context Protocol (MCP) tools via MCP server.

229. **[playwriter](https://github.com/remorses/playwriter)** - ⭐ 3,591
   Chrome extension & CLI to let agents control your browser. Runs Playwright snippets in a stateful sandbox. Available as CLI or MCP

230. **[langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters)** - ⭐ 3,560
   LangChain 🔌 MCP

231. **[tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp)** - ⭐ 3,559
   AI-assisted TradingView chart analysis — connect Claude Code to your TradingView Desktop for personal workflow automation

232. **[osaurus](https://github.com/dinoki-ai/osaurus)** - ⭐ 3,548
   AI edge infrastructure for macOS. Run local or cloud models, share tools across apps via MCP, and power AI workflows with a native, always-on runtime.

233. **[EverMemOS](https://github.com/EverMind-AI/EverMemOS)** - ⭐ 3,546
   A memory OS that makes your OpenClaw agents more personal while saving tokens.

234. **[MCP-Chinese-Getting-Started-Guide](https://github.com/liaokongVFX/MCP-Chinese-Getting-Started-Guide)** - ⭐ 3,518
   Model Context Protocol(MCP) 编程极速入门

235. **[rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)** - ⭐ 3,515
   The official Rust SDK for the Model Context Protocol

236. **[boost](https://github.com/laravel/boost)** - ⭐ 3,504
   Laravel-focused MCP server for augmenting your AI powered local development experience.

237. **[Generative-Media-Skills](https://github.com/SamurAIGPT/Generative-Media-Skills)** - ⭐ 3,502
   Multi-modal Generative Media Skills for AI Agents (Claude Code, Cursor, Gemini CLI). High-quality image, video, and audio generation powered by muapi.ai.

238. **[SimpleMem](https://github.com/aiming-lab/SimpleMem)** - ⭐ 3,500
   SimpleMem: Efficient Lifelong Memory for LLM Agents — Text & Multimodal

239. **[dagu](https://github.com/dagucloud/dagu)** - ⭐ 3,478
   Local-first workflow engine with a Web UI for small teams. Define DAGs in a declarative YAML format. Self-contained and no DBMS required. Use any AI agent to manage your DAGs.

240. **[java-sdk](https://github.com/modelcontextprotocol/java-sdk)** - ⭐ 3,468
   The official Java SDK for Model Context Protocol servers and clients. Maintained in collaboration with Spring AI

241. **[AionUi](https://github.com/iOfficeAI/AionUi)** - ⭐ 3,452
   Free, local, open-source GUI app for Gemini CLI, Claude Code, Codex, Qwen Code, Goose Cli, Auggie, and more — Enhanced Chat UI, WebUI, Multi-Agent & Multi-LLM, MCP Integration | 🌟 Star if you like it!

242. **[swarmpit](https://github.com/swarmpit/swarmpit)** - ⭐ 3,449
   Lightweight AI-friendly Docker Swarm management

243. **[mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase)** - ⭐ 3,369
   Allow LLMs to control a browser with Browserbase and Stagehand

244. **[py-xiaozhi](https://github.com/huangjunsen0406/py-xiaozhi)** - ⭐ 3,358
   Open-source AI assistant ecosystem with MCP integrations, multimodal workflows, IoT support, and cross-platform voice interaction.

245. **[PeopleInSpace](https://github.com/joreilly/PeopleInSpace)** - ⭐ 3,346
   Kotlin Multiplatform sample with SwiftUI, Jetpack Compose, Compose for Wear, Compose for Desktop, and Compose for Web clients along with Ktor backend.

246. **[codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** - ⭐ 3,341
   High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 159 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.

247. **[ha-mcp](https://github.com/homeassistant-ai/ha-mcp)** - ⭐ 3,339
   The Unofficial and Awesome Home Assistant MCP Server

248. **[openpencil](https://github.com/ZSeven-W/openpencil)** - ⭐ 3,326
   The world's first open-source AI-native vector design tool and the first to feature concurrent Agent Teams. Design-as-Code. Turn prompts into UI directly on the live canvas. A modern alternative to Pencil.

249. **[metorial](https://github.com/metorial/metorial)** - ⭐ 3,305
   Connect any AI model to 1200+ integrations (MCP, CLI, API)

250. **[mcp](https://github.com/microsoft/mcp)** - ⭐ 3,303
   Catalog of official Microsoft MCP (Model Context Protocol) server implementations for AI-powered data access and tool integration

251. **[goclaw](https://github.com/nextlevelbuilder/goclaw)** - ⭐ 3,249
   GoClaw - GoClaw is OpenClaw rebuilt in Go — with multi-tenant isolation, 5-layer security, and native concurrency. Deploy AI agent teams at scale without compromising on safety.

252. **[Peekaboo](https://github.com/steipete/Peekaboo)** - ⭐ 3,244
   Peekaboo is a macOS CLI & optional MCP server that enables AI agents to capture screenshots of applications, or the entire system, with optional visual question answering through local or remote AI models.

253. **[agentgateway](https://github.com/agentgateway/agentgateway)** - ⭐ 3,236
   Next Generation Agentic Proxy for AI Agents and MCP servers

254. **[neo](https://github.com/neomjs/neo)** - ⭐ 3,202
   Neo.mjs is a self-evolving software organism: a professional end-to-end AI engineering team whose cross-model swarm inhabits live apps via Neural Link, Active Hybrid GraphRAG, DreamService, and self-healing loops.

255. **[basic-memory](https://github.com/basicmachines-co/basic-memory)** - ⭐ 3,201
   AI conversations that actually remember. Never re-explain your project to your AI again. Join our Discord: https://discord.gg/tyvKNccgqN

256. **[fastmcp](https://github.com/punkpeye/fastmcp)** - ⭐ 3,188
   A TypeScript framework for building MCP servers.

257. **[design-extract](https://github.com/Manavarya09/design-extract)** - ⭐ 3,162
   Extract any website's complete design system with one command. DTCG tokens, semantic+primitive+composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters (iOS SwiftUI, Android Compose, Flutter, WordPress), Tailwind v4, Figma variables, shadcn/ui, CSS health audit, WCAG remediation, Chrome extension. MIT, Playwright, Node 20+.

258. **[mcp-grafana](https://github.com/grafana/mcp-grafana)** - ⭐ 3,133
   MCP server for Grafana

259. **[Unity-MCP](https://github.com/IvanMurzak/Unity-MCP)** - ⭐ 3,129
   AI Skills, MCP Tools, and CLI for Unity Engine. Full AI develop and test loop. Use cli for quick setup. Efficient token usage, advanced tools. Any C# method may be turned into a tool by a single line. Works with Claude Code, Gemini, Copilot, Cursor and any other absolutely for free.

260. **[tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp)** - ⭐ 3,079
   Real-time crypto & stock screening, advanced technical indicators, Bollinger Bands intelligence, candlestick patterns + native Claude Desktop integration. Multi-exchange (Binance, KuCoin, Bybit+). Open-source AI trading infrastructure.

261. **[TuriX-CUA](https://github.com/TurixAI/TuriX-CUA)** - ⭐ 3,058
   This is the official website for TuriX Computer-use-Agent

262. **[harbor](https://github.com/av/harbor)** - ⭐ 3,057
   Stop configuring your AI stack. Start using it. One command brings a complete pre-wired LLM stack with hundreds of services to explore.

263. **[vitemcp](https://github.com/punkpeye/vitemcp)** - ⭐ 3,056
   A TypeScript framework for building MCP servers.

264. **[buildwithclaude](https://github.com/davepoon/buildwithclaude)** - ⭐ 3,047
   A single hub to find Claude Skills, Agents, Commands, Hooks, Plugins, and Marketplace collections to extend Claude Code, Claude Desktop, Agent SDK and OpenClaw

265. **[core](https://github.com/cheshire-cat-ai/core)** - ⭐ 3,041
   AI agent microservice

266. **[n8n-nodes-mcp](https://github.com/nerding-io/n8n-nodes-mcp)** - ⭐ 3,015
   n8n custom node for MCP

267. **[kagent](https://github.com/kagent-dev/kagent)** - ⭐ 2,979
   Cloud Native Agentic AI | Discord: https://bit.ly/kagentdiscord

268. **[dbhub](https://github.com/bytebase/dbhub)** - ⭐ 2,953
   Zero-dependency, token-efficient database MCP server for Postgres, MySQL, SQL Server, MariaDB, SQLite.

269. **[FireRed-OpenStoryline](https://github.com/FireRedTeam/FireRed-OpenStoryline)** - ⭐ 2,897
   FireRed-OpenStoryline is an AI video editing agent that transforms manual editing into intention-driven directing through natural language interaction, LLM-powered planning, and precise tool orchestration. It facilitates transparent, human-in-the-loop creation with reusable Style Skills for consistent, professional storytelling.

270. **[SocratiCode](https://github.com/giancarloerra/SocratiCode)** - ⭐ 2,896
   Enterprise-grade (40m+ LOC) codebase intelligence, zero-setup, local & private Plugin/Skill/Extension or MCP: hybrid semantic search, polyglot dependency graphs, symbol-level impact analysis & call-flow, interactive HTML viewer, cross-project & branch-aware search, DB/API/infra knowledge. 61% less tokens, 84% fewer calls, 37x faster. Cloud in beta.

271. **[anything-analyzer](https://github.com/Mouseww/anything-analyzer)** - ⭐ 2,896
   全能协议分析工具：浏览器抓包 + MITM 代理 + 指纹伪装 + AI 分析 + MCP Server 无缝对接 AI Agent/IDE   |  All-in-one protocol analysis toolkit — built-in browser capture, MITM proxy, JS hooks, fingerprint spoofing, AI analysis & MCP server for agent integration

272. **[postgres-mcp](https://github.com/crystaldba/postgres-mcp)** - ⭐ 2,882
   Postgres MCP Pro provides configurable read/write access and performance analysis for you and your AI agents.

273. **[fli](https://github.com/punitarani/fli)** - ⭐ 2,858
   Google Flights MCP, CLI and Python Library

274. **[arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)** - ⭐ 2,846
   A Model Context Protocol server for searching and analyzing arXiv papers

275. **[NotFair](https://github.com/nowork-studio/NotFair)** - ⭐ 2,830
   Open-source Claude Code skills for SEO, GEO, Google Ads, Meta Ads

276. **[shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server)** - ⭐ 2,789
   A mcp server to allow LLMS gain context about shadcn ui component structure,usage and installation,compaitable with react,svelte 5,vue & React Native

277. **[notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp)** - ⭐ 2,753
   MCP server for NotebookLM - Let your AI agents (Claude Code, Codex) research documentation directly with grounded, citation-backed answers from Gemini. Persistent auth, library management, cross-client sharing. Zero hallucinations, just your knowledge base.

278. **[moltis](https://github.com/moltis-org/moltis)** - ⭐ 2,733
   A secure persistent personal agent server in Rust. One binary, sandboxed execution, multi-provider LLMs, voice, memory, Telegram, WhatsApp, Discord, Teams, and MCP tools. Secure by design, runs on your hardware.

279. **[mcp](https://github.com/supabase/mcp)** - ⭐ 2,733
   Connect Supabase to your AI assistants

280. **[markdownify-mcp](https://github.com/zcaceres/markdownify-mcp)** - ⭐ 2,731
   A Model Context Protocol server for converting almost anything to Markdown

281. **[ddgs](https://github.com/deedy5/ddgs)** - ⭐ 2,717
   A metasearch library that aggregates results from diverse web search services

282. **[supabase-mcp](https://github.com/supabase-community/supabase-mcp)** - ⭐ 2,710
   Connect Supabase to your AI assistants

283. **[agent-device](https://github.com/callstack/agent-device)** - ⭐ 2,702
   CLI to control iOS and Android devices for AI agents

284. **[agent-deck](https://github.com/asheshgoplani/agent-deck)** - ⭐ 2,692
   Terminal session manager for AI coding agents. One TUI for Claude, Gemini, OpenCode, Codex, and more.

285. **[supergateway](https://github.com/supercorp-ai/supergateway)** - ⭐ 2,678
   Run MCP stdio servers over SSE and SSE over stdio. AI gateway.

286. **[ableton-mcp](https://github.com/ahujasid/ableton-mcp)** - ⭐ 2,677

287. **[google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp)** - ⭐ 2,660
   Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search & Drive with AI - Comprehensive Google Workspace / G Suite MCP Server & CLI Tool

288. **[lean-ctx](https://github.com/yvgude/lean-ctx)** - ⭐ 2,638
   Control what your AI can see. LeanCTX (Lean Context) is the context intelligence layer for AI agents — one local Rust binary that decides what they read, remembers what they learn, guards what they touch, and proves what they save. 60–90% fewer tokens as the receipt. 76 MCP tools, 30+ agents, local-first.

289. **[slackdump](https://github.com/rusq/slackdump)** - ⭐ 2,635
   Save or export your private and public Slack messages, threads, files, and users locally without admin privileges.

290. **[toprank](https://github.com/nowork-studio/toprank)** - ⭐ 2,621
   Open-source Claude Code skills for SEO, GEO, Google Ads, Meta Ads

291. **[mcp-proxy](https://github.com/sparfenyuk/mcp-proxy)** - ⭐ 2,587
   A bridge between Streamable HTTP and stdio MCP transports

292. **[nunu](https://github.com/go-nunu/nunu)** - ⭐ 2,575
   A CLI tool for building Go applications.

293. **[kreuzberg](https://github.com/Goldziher/kreuzberg)** - ⭐ 2,561
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Go, and TypeScript/Node.js—or use via CLI, REST API, or MCP server.

294. **[agent-scan](https://github.com/snyk/agent-scan)** - ⭐ 2,560
   Security scanner for AI agents, MCP servers and agent skills.

295. **[awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)** - ⭐ 2,555
   A trilingual (繁中 / English / 简中) learning roadmap for agentic AI: from LLM basics to multi-agent systems, with 240+ curated resources and hands-on examples. 中文 AI agent 學習地圖。

296. **[skills](https://github.com/microsoft/skills)** - ⭐ 2,539
   Skills, MCP servers, Custom Agents, Agents.md for SDKs to ground Coding Agents

297. **[wanwu](https://github.com/UnicomAI/wanwu)** - ⭐ 2,528
   China Unicom's Yuanjing Wanwu Agent Platform is an enterprise-grade, multi-tenant AI agent development platform. It helps users build applications such as intelligent agents, workflows, and rag, and also supports model management. The platform features a developer-friendly license, and we welcome all developers to build upon the platform.

298. **[claude-context-mode](https://github.com/mksglu/claude-context-mode)** - ⭐ 2,522
   MCP is the protocol for tool access. We're the virtualization layer for context.

299. **[MCP-SuperAssistant](https://github.com/srbhptl39/MCP-SuperAssistant)** - ⭐ 2,493
   Brings MCP to ChatGPT, DeepSeek, Perplexity, Grok, Gemini, Google AI Studio, OpenRouter, DeepSeek, T3 Chat and more...

300. **[sentrux](https://github.com/sentrux/sentrux)** - ⭐ 2,459
   Real-time architectural sensor that helps AI agents close the feedback loop, enabling recursive self-improvement of code quality. Pure Rust.

301. **[brightdata-mcp](https://github.com/brightdata/brightdata-mcp)** - ⭐ 2,446
   A powerful Model Context Protocol (MCP) server that provides an all-in-one solution for public web access.

302. **[obsidian-local-rest-api](https://github.com/coddingtonbear/obsidian-local-rest-api)** - ⭐ 2,438
   A secure REST API and Model Context Protocol (MCP) server for your vault.

303. **[ext-apps](https://github.com/modelcontextprotocol/ext-apps)** - ⭐ 2,412
   Official repo for spec & SDK of MCP Apps protocol - standard for UIs embedded AI chatbots, served by MCP servers

304. **[tabularis](https://github.com/TabularisDB/tabularis)** - ⭐ 2,408
   Open-source database client for PostgreSQL, MySQL/MariaDB and SQLite with SQL notebooks, visual EXPLAIN, AI and MCP built in. Hackable with plugins.

305. **[metamcp](https://github.com/metatool-ai/metamcp)** - ⭐ 2,405
   MCP Aggregator, Orchestrator, Middleware, Gateway in one docker

306. **[ghidra-mcp](https://github.com/bethington/ghidra-mcp)** - ⭐ 2,401
   Ghidra MCP Server — 200+ MCP tools for AI-powered reverse engineering. GUI plugin + headless server, lazy tool loading, convention enforcement, batch operations, Ghidra Server integration, and Docker deployment.

307. **[agent-device](https://github.com/callstackincubator/agent-device)** - ⭐ 2,390
   CLI to control iOS and Android devices for AI agents

308. **[yu-ai-agent](https://github.com/liyupi/yu-ai-agent)** - ⭐ 2,387
   编程导航 AI 开发实战新项目，基于 Spring Boot 3 + Java 21 + Spring AI 构建 AI 恋爱大师应用和 ReAct 模式自主规划智能体YuManus，覆盖 AI 大模型接入、Spring AI 核心特性、Prompt 工程和优化、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、AI Agent 开发（Manas Java 实现）、Cursor AI 工具等核心知识。用一套教程将程序员必知必会的 AI 技术一网打尽，帮你成为 AI 时代企业的香饽饽，给你的简历和求职大幅增加竞争力。

309. **[radar](https://github.com/skyhook-io/radar)** - ⭐ 2,372
   The missing open source Kubernetes UI. Topology, event timeline, and service traffic — plus resource browsing and Helm management.

310. **[google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp)** - ⭐ 2,368

311. **[super-agent-party](https://github.com/heshengtao/super-agent-party)** - ⭐ 2,361
   ⭐ All-in-one AI companion! Super Agent Party = Self hosted neuro sama + openclaw! ⭐ 全能AI伴侣！超级智能体派对 = 自托管neuro sama + openclaw!

312. **[onecli](https://github.com/onecli/onecli)** - ⭐ 2,360
   Open-source credential gateway with a built-in vault. give your AI agents access to services without exposing keys.

313. **[claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills)** - ⭐ 2,357
   425 plugins, 2,810 skills, 200 agents for Claude Code. Open-source marketplace at tonsofskills.com with the ccpi CLI package manager.

314. **[jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp)** - ⭐ 2,295
   Plugin for JADX to integrate MCP server

315. **[modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol)** - ⭐ 2,294
   The official MCP server implementation for the Perplexity API Platform

316. **[code-graph-rag](https://github.com/vitali87/code-graph-rag)** - ⭐ 2,286
   The ultimate RAG for your monorepo. Query, understand, and edit multi-language codebases with the power of AI and knowledge graphs

317. **[linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server)** - ⭐ 2,282
   Open-source MCP server for LinkedIn. Give Claude and any MCP-compatible AI assistant access to profiles, companies, jobs, and messages.

318. **[comfyui_LLM_party](https://github.com/heshengtao/comfyui_LLM_party)** - ⭐ 2,274
   LLM Agent Framework in ComfyUI includes MCP sever, Omost,GPT-sovits, ChatTTS,GOT-OCR2.0, and FLUX prompt nodes,access to Feishu,discord,and adapts to all llms with similar openai / aisuite interfaces, such as o1,ollama, gemini, grok, qwen, GLM, deepseek, kimi,doubao. Adapted to local llms, vlm, gguf such as llama-3.3 Janus-Pro, Linkage graphRAG

319. **[repowise](https://github.com/repowise-dev/repowise)** - ⭐ 2,268
   Codebase intelligence for AI-assisted engineering teams: code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.

320. **[gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool)** - ⭐ 2,237
   MCP server that enables AI assistants to interact with Google Gemini CLI, leveraging Gemini's massive token window for large file analysis and codebase understanding

321. **[mcp2cli](https://github.com/knowsuchagency/mcp2cli)** - ⭐ 2,226
   Turn any MCP, OpenAPI, or GraphQL server into a CLI — at runtime, with zero codegen

322. **[chatmcp](https://github.com/daodao97/chatmcp)** - ⭐ 2,194
   ChatMCP is an AI chat client implementing the Model Context Protocol (MCP).

323. **[mcp-server](https://github.com/financial-datasets/mcp-server)** - ⭐ 2,188
   An MCP server for interacting with the Financial Datasets stock market API.

324. **[mcp-crawl4ai-rag](https://github.com/coleam00/mcp-crawl4ai-rag)** - ⭐ 2,186
   Web Crawling and RAG Capabilities for AI Agents and AI Coding Assistants

325. **[open-seo](https://github.com/every-app/open-seo)** - ⭐ 2,181
   Open source alternative to Semrush and Ahrefs

326. **[vexa](https://github.com/Vexa-ai/vexa)** - ⭐ 2,177
   Open-source meeting transcription API for Google Meet, Microsoft Teams & Zoom. Auto-join bots, real-time WebSocket transcripts, MCP server for AI agents. Self-host or use hosted SaaS.

327. **[ShipSwift](https://github.com/signerlabs/ShipSwift)** - ⭐ 2,169
   AI-native SwiftUI component library with full-stack recipes — connect via MCP for instant access.

328. **[Aix-DB](https://github.com/apconw/Aix-DB)** - ⭐ 2,156
   Aix-DB 基于 LangChain/LangGraph 框架，结合 MCP Skills 多智能体协作架构，实现自然语言到数据洞察的端到端转换。

329. **[mcphub](https://github.com/samanhappy/mcphub)** - ⭐ 2,153
   A unified hub for centrally managing and dynamically orchestrating multiple MCP servers/APIs into separate endpoints with flexible routing strategies.

330. **[Unla](https://github.com/AmoyLab/Unla)** - ⭐ 2,138
   🧩 MCP Gateway - A lightweight gateway service that instantly transforms existing MCP Servers and APIs into MCP servers with zero code changes. Features Docker deployment and management UI, requiring no infrastructure modifications.

331. **[carbon](https://github.com/crbnos/carbon)** - ⭐ 2,131
   Carbon is an open source ERP, MES and QMS for manufacturing. Perfect for complex assembly, contract manufacturing, and configure to order manufacturing.

332. **[mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager)** - ⭐ 2,111
   Shrimp Task Manager is a task tool built for AI Agents, emphasizing chain-of-thought, reflection, and style consistency. It converts natural language into structured dev tasks with dependency tracking and iterative refinement, enabling agent-like developer behavior in reasoning AI systems.

333. **[claude-code-subagents-collection](https://github.com/davepoon/claude-code-subagents-collection)** - ⭐ 2,098
   Claude Code Subagents & Commands Collection + CLI Tool

334. **[fusio](https://github.com/apioo/fusio)** - ⭐ 2,097
   Self-Hosted API Management for Builders

335. **[claude-peers-mcp](https://github.com/louislva/claude-peers-mcp)** - ⭐ 2,095
   Allow all your Claude Codes to message each other ad-hoc!

336. **[tavily-mcp](https://github.com/tavily-ai/tavily-mcp)** - ⭐ 2,092
   Production ready MCP server with real-time search, extract, map & crawl.

337. **[DevDocs](https://github.com/cyberagiinc/DevDocs)** - ⭐ 2,089
   Completely free, private, UI based Tech Documentation MCP server. Designed for coders and software developers in mind. Easily integrate into Cursor, Windsurf, Cline, Roo Code, Claude Desktop App

338. **[Claude-Code-Everything-You-Need-to-Know](https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know)** - ⭐ 2,082
   The ultimate all-in-one guide to mastering Claude Code. From setup, prompt engineering, commands, hooks, workflows, automation, and integrations, to MCP servers, tools, and the BMAD method—packed with step-by-step tutorials, real-world examples, and expert strategies to make this the global go-to repo for Claude mastery.

339. **[Hands-On-AI-Engineering](https://github.com/Sumanth077/Hands-On-AI-Engineering)** - ⭐ 2,076
   A curated collection of practical AI projects implementing OCR systems, RAG, AI agents, and other AI use cases.

340. **[Observal](https://github.com/BlazeUp-AI/Observal)** - ⭐ 2,075
   Observal is a unified agent registry and analytics platform.

341. **[mcp-router](https://github.com/mcp-router/mcp-router)** - ⭐ 2,047
   A Unified MCP Server Management App (MCP Manager).

342. **[beelzebub](https://github.com/beelzebub-labs/beelzebub)** - ⭐ 2,045
   A secure low code deception runtime framework, leveraging AI for System Virtualization.

343. **[mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw)** - ⭐ 2,043
   MCP server and Claude Code skill for Excalidraw — programmatic canvas toolkit to create, edit, and export diagrams via AI agents with real-time canvas sync.

344. **[ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp)** - ⭐ 2,040
   MCP server for interacting with the iOS simulator

345. **[awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit)** - ⭐ 2,027
   The most comprehensive toolkit for Claude Code -- 135 agents, 35 curated skills, 42 commands, 176+ plugins, 20 hooks, 15 rules, 7 templates, 14 MCP configs, 26 companion apps, 52 ecosystem entries, and more.

346. **[superglue](https://github.com/superglue-ai/superglue)** - ⭐ 2,020
   superglue (YC W25) builds integrations and tools from natural language. Get production-grade tools for long tail and enterprise systems.

347. **[mcpso](https://github.com/chatmcp/mcpso)** - ⭐ 2,016
   directory for Awesome MCP Servers

348. **[agentset](https://github.com/agentset-ai/agentset)** - ⭐ 2,012
   The open-source RAG platform: built-in citations, deep research, 22+ file formats, partitions, MCP server, and more.

349. **[inspector](https://github.com/MCPJam/inspector)** - ⭐ 2,012
   Testing and evaluation platform to chat, inspect, and debug MCP servers, MCP apps, and ChatGPT apps.

350. **[docmd](https://github.com/docmd-io/docmd)** - ⭐ 2,011
   Build production-ready documentation from Markdown in seconds. No React, no bloat, just content.

351. **[esp32_nat_router](https://github.com/martin-ger/esp32_nat_router)** - ⭐ 1,999
   An AI-enabled NAT Router/Firewall for the ESP32

352. **[mcp-cli](https://github.com/IBM/mcp-cli)** - ⭐ 1,985

353. **[mcp_agent_mail](https://github.com/Dicklesworthstone/mcp_agent_mail)** - ⭐ 1,982
   Asynchronous coordination layer for AI coding agents: identities, inboxes, searchable threads, and advisory file leases over FastMCP + Git + SQLite

354. **[witsy](https://github.com/Kochava-Studios/witsy)** - ⭐ 1,981
   Witsy: desktop AI assistant / universal MCP client

355. **[paperbanana](https://github.com/llmsresearch/paperbanana)** - ⭐ 1,981
   Open source implementation and extension of Google Research’s PaperBanana for automated academic figures, diagrams, and research visuals, expanded to new domains like slide generation.

356. **[unreal-mcp](https://github.com/chongdashu/unreal-mcp)** - ⭐ 1,971
   Enable AI assistant clients like Cursor, Windsurf and Claude Desktop to control Unreal Engine through natural language using the Model Context Protocol (MCP).

357. **[executor](https://github.com/RhysSullivan/executor)** - ⭐ 1,966
   The missing integration layer for AI agents. Let them call any OpenAPI / MCP / GraphQL / custom js functions in secure environment.

358. **[mcpb](https://github.com/modelcontextprotocol/mcpb)** - ⭐ 1,962
   Desktop Extensions: One-click local MCP server installation in desktop apps

359. **[korean-law-mcp](https://github.com/chrisryugj/korean-law-mcp)** - ⭐ 1,946
   국가법령정보MCP v4.4 | 법제처 42개 API → 9개 MCP 도구. 법령·판례·조례·조약 + 다단계 리서치(legal_research) + 정밀분석(legal_analysis: 인용검증·판례생사·행위시법·영향그래프) | 42 Korean legal APIs → 9 MCP tools

360. **[witsy](https://github.com/nbonamy/witsy)** - ⭐ 1,928
   Witsy: desktop AI assistant / universal MCP client

361. **[llm-for-zotero](https://github.com/yilewang/llm-for-zotero)** - ⭐ 1,922
   A research agent system deeply rooted in your Zotero library.

362. **[dembrandt](https://github.com/dembrandt/dembrandt)** - ⭐ 1,920
   Extract any website’s design system into tokens in seconds: logo, colors, typography, borders & more. One command.

363. **[contextplus](https://github.com/forloopcodes/contextplus)** - ⭐ 1,918
   Semantic Intelligence for Large-Scale Engineering. Context+ is an MCP server designed for developers who demand 99% accuracy. By combining RAG, Tree-sitter AST, Spectral Clustering, and Obsidian-style linking, Context+ turns a massive codebase into a searchable, hierarchical feature graph.

364. **[butterbase](https://github.com/butterbase-ai/butterbase)** - ⭐ 1,917
   Open-source backend-as-a-service. Postgres, auth, storage, functions, AI gateway, MCP.

365. **[mcp-memory-service](https://github.com/doobidoo/mcp-memory-service)** - ⭐ 1,911
   Open-source persistent memory for AI agent pipelines (LangGraph, CrewAI, AutoGen) and Claude. REST API + knowledge graph + autonomous consolidation.

366. **[jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp)** - ⭐ 1,910
   The leading, most token-efficient MCP server for GitHub source code exploration via tree-sitter AST parsing

367. **[yomo](https://github.com/yomorun/yomo)** - ⭐ 1,907
   🦖 Serverless AI Agent Framework with Geo-distributed Edge AI Infra.

368. **[beelzebub](https://github.com/mariocandela/beelzebub)** - ⭐ 1,904
   A secure low code honeypot framework, leveraging AI for System Virtualization.

369. **[ai-agents-from-zero](https://github.com/didilili/ai-agents-from-zero)** - ⭐ 1,897
    🚀 2026 最系统的 AI Agent 速成指南｜智能体实战教程 · 完整学习路径  + 实战项目 + 面试题库 · 对标大模型应用开发工程师岗位 · 覆盖LangChain / LangGraph / Coze / Dify / MCP / skills / LLM / RAG / 提示词 · 企业级部署与微调 · 从0到企业级落地 + 从学习到上线项目 + 面试准备一体化

370. **[mcp-cli](https://github.com/chrishayuk/mcp-cli)** - ⭐ 1,891

371. **[toolhive](https://github.com/stacklok/toolhive)** - ⭐ 1,871
   ToolHive is an enterprise-grade platform for running and managing Model Context Protocol (MCP) servers.

372. **[tldx](https://github.com/brandonyoungdev/tldx)** - ⭐ 1,869
   Bulk domain availability checking via RDAP, DNS, and WHOIS, with prefix/suffix permutations, regex patterns, MCP, and multiple output formats

373. **[js-reverse-mcp](https://github.com/zhizhuodemao/js-reverse-mcp)** - ⭐ 1,847
   为 AI Agent 设计的 JS 逆向 MCP Server，内置反检测，基于 chrome-devtools-mcp 重构 | JS reverse engineering MCP server with agent-first tool design and built-in anti-detection. Rebuilt from chrome-devtools-mcp.

374. **[cocoindex-code](https://github.com/cocoindex-io/cocoindex-code)** - ⭐ 1,841
   A super light-weight embedded code search engine CLI (AST based) that just works - saves 70% token and improves speed for coding agent  🌟 Star if you like it!

375. **[opendia](https://github.com/aaronjmars/opendia)** - ⭐ 1,827
   Connect your browser to AI models. Just use Dia on Chrome, Arc or Firefox.

376. **[py-gpt](https://github.com/szczyglis-dev/py-gpt)** - ⭐ 1,823
   Desktop AI Assistant powered by GPT-5, GPT-4, o1, o3, Gemini, Claude, Ollama, DeepSeek, Perplexity, Grok, Bielik, chat, vision, voice, RAG, image and video generation, agents, tools, MCP, plugins, speech synthesis and recognition, web search, memory, presets, assistants,and more. Linux, Windows, Mac

377. **[MAI-UI](https://github.com/Tongyi-MAI/MAI-UI)** - ⭐ 1,820
   MAI-UI: Real-World Centric Foundation GUI Agents ranging from 2B to 235B

378. **[sanic-web](https://github.com/apconw/sanic-web)** - ⭐ 1,817
   一个轻量级、支持全链路且易于二次开发的大模型应用项目(Large Model Data Assistant) 支持DeepSeek/Qwen3等大模型 基于 Dify 、LangChain/LangGraph、Ollama&Vllm、Sanic 和 Text2SQL 📊 等技术构建的一站式大模型应用开发项目，采用 Vue3、TypeScript 和 Vite 5 打造现代UI。它支持通过 ECharts 📈 实现基于大模型的数据图形化问答，具备处理 CSV 文件 📂 表格问答的能力。同时，能方便对接第三方开源 RAG 系统 检索系统 🌐等，以支持广泛的通用知识问答。

379. **[AIaW](https://github.com/NitroRCr/AIaW)** - ⭐ 1,814
   AI as Workspace - An elegant AI chat client. Full-featured, lightweight. Support multiple workspaces, plugin system, cross-platform, local first + real-time cloud sync, Artifacts, MCP | 更好的 AI 客户端

380. **[figma-console-mcp](https://github.com/southleft/figma-console-mcp)** - ⭐ 1,813
   Your design system as an API. Connect AI to Figma for extraction, creation, and debugging.

381. **[ai-engineering-interview-questions](https://github.com/amitshekhariitbhu/ai-engineering-interview-questions)** - ⭐ 1,812
   Your Cheat Sheet for AI Engineering Interview – Questions and Answers.

382. **[azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp)** - ⭐ 1,805
   The MCP server for Azure DevOps, bringing the power of Azure DevOps directly to your agents.

383. **[mcp-server-mysql](https://github.com/benborla/mcp-server-mysql)** - ⭐ 1,804
   A Model Context Protocol server that provides read-only access to MySQL databases. This server enables LLMs to inspect database schemas and execute read-only queries.

384. **[paper-search-mcp](https://github.com/openags/paper-search-mcp)** - ⭐ 1,793
   MCP, CLI, Skills for searching and downloading academic papers from multiple sources like arXiv, PubMed, bioRxiv, etc.

385. **[Dive](https://github.com/OpenAgentPlatform/Dive)** - ⭐ 1,792
   Dive is an open-source MCP Host Desktop Application that seamlessly integrates with any LLMs supporting function calling capabilities. ✨

386. **[awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering)** - ⭐ 1,783
   Awesome list for AI agent harness engineering: tools, patterns, evals, memory, MCP, permissions, observability, and orchestration.

387. **[contextplus](https://github.com/ForLoopCodes/contextplus)** - ⭐ 1,780
   Semantic Intelligence for Large-Scale Engineering. Context+ is an MCP server designed for developers who demand 99% accuracy. By combining RAG, Tree-sitter AST, Spectral Clustering, and Obsidian-style linking, Context+ turns a massive codebase into a searchable, hierarchical feature graph.

388. **[mcphub.nvim](https://github.com/ravitemer/mcphub.nvim)** - ⭐ 1,779
   An MCP client for Neovim that seamlessly integrates MCP servers into your editing workflow with an intuitive interface for managing, testing, and using MCP servers with your favorite chat plugins.

389. **[plik](https://github.com/root-gg/plik)** - ⭐ 1,777
   Plik is a temporary file upload system (Wetransfer like) in Go.

390. **[mcp-unity](https://github.com/CoderGamester/mcp-unity)** - ⭐ 1,768
   Model Context Protocol (MCP) plugin to connect with Unity Editor — designed for Cursor, Claude Code, Codex, Windsurf and other IDEs

391. **[pg-aiguide](https://github.com/timescale/pg-aiguide)** - ⭐ 1,761
   MCP server and Claude plugin for Postgres skills and documentation. Helps AI coding tools generate better PostgreSQL code.

392. **[AssetOpsBench](https://github.com/IBM/AssetOpsBench)** - ⭐ 1,759
   AssetOpsBench - Industry 4.0: A unified benchmark and framework for building, orchestrating, and evaluating domain-specific AI agents for Industry 4.0 asset operations and maintenance, with 460+ scenarios, 5 specialist agents (IoT, FMSR, TSFM, Work Order,...), and multi-agent orchestration blueprints (MetaAgent, AgentHive) over MCP.

393. **[BeeCount](https://github.com/TNT-Likely/BeeCount)** - ⭐ 1,747
   Local-first bookkeeping for iOS/Android/Web · Self-hosted cloud + iCloud/WebDAV/S3 sync · AI capture · MCP | 本地优先的跨端记账 · 自建云 + iCloud/WebDAV/S3 同步 · AI 记账 · MCP

394. **[kubb](https://github.com/kubb-labs/kubb)** - ⭐ 1,738
   🧡 The meta framework for code generation. Automate OpenAPI to type-safe TypeScript, Zod, and TanStack Query with a modular, plugin-based engine.

395. **[grepai](https://github.com/yoanbernabeu/grepai)** - ⭐ 1,735
   Semantic Search & Call Graphs for AI Agents (100% Local)

396. **[awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins)** - ⭐ 1,731
   A curated list of Plugins that let you extend Claude Code with custom commands, agents, hooks, and MCP servers through the plugin system.

397. **[interactive-feedback-mcp](https://github.com/noopstudios/interactive-feedback-mcp)** - ⭐ 1,721
   Interactive User Feedback MCP

398. **[skybridge](https://github.com/alpic-ai/skybridge)** - ⭐ 1,716
   Skybridge is a full-stack TypeScript framework for MCP Apps and ChatGPT Apps. Type-safe. React-powered. Platform-agnostic.

399. **[anyquery](https://github.com/julien040/anyquery)** - ⭐ 1,715
   Query anything (GitHub, Notion, +40 more) with SQL and let LLMs (ChatGPT, Claude) connect to using MCP

400. **[pilot-shell](https://github.com/maxritter/pilot-shell)** - ⭐ 1,709
   How real engineers run Claude Code: spec-driven planning, enforced TDD, persistent memory, and quality enforcement on all levels. Make Claude Code production-ready.

401. **[mcp](https://github.com/MicrosoftDocs/mcp)** - ⭐ 1,699
   Official Microsoft Learn MCP Server and CLI tool – powering LLMs and AI agents with real-time, trusted Microsoft docs & code samples.

402. **[blitz-mac](https://github.com/blitzdotdev/blitz-mac)** - ⭐ 1,698
   Native macOS App Store Connect tool with MCP. Submit iOS apps to App Store with AI agents

403. **[awesome-hermes-agent](https://github.com/SamurAIGPT/awesome-hermes-agent)** - ⭐ 1,697
   A curated list of skills, plugins, tools, integrations, and resources for Hermes Agent by Nous Research

404. **[GrokSearch](https://github.com/GuDaStudio/GrokSearch)** - ⭐ 1,695
   Integrate Grok's powerful real-time search capabilities into Claude via the MCP protocol!

405. **[zenfeed](https://github.com/glidea/zenfeed)** - ⭐ 1,692
   Make RSS 📰 great again with AI 🧠✨!!

406. **[routa](https://github.com/phodal/routa)** - ⭐ 1,680
   Workspace-first multi-agent coordination platform for AI development, with shared Specs, Kanban orchestration, and MCP/ACP/   A2A support across web and desktop.

407. **[lanhu-mcp](https://github.com/dsphper/lanhu-mcp)** - ⭐ 1,678
   ⚡ 需求分析效率提升 200%！全球首个为 AI 编程时代设计的团队协作 MCP 服务器，自动分析需求自动编写前后端代码，下载切图

408. **[kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server)** - ⭐ 1,676
   Model Context Protocol (MCP) server for Kubernetes and OpenShift

409. **[slack-mcp-server](https://github.com/korotovsky/slack-mcp-server)** - ⭐ 1,661
   The most powerful MCP Slack Server with no permission requirements, Apps support, GovSlack, DMs, Group DMs and smart history fetch logic.

410. **[gitlab-mcp](https://github.com/zereight/gitlab-mcp)** - ⭐ 1,655
   First gitlab mcp for you, building together

411. **[jshookmcp](https://github.com/vmoranv/jshookmcp)** - ⭐ 1,647
   js hook toolkit that all you need

412. **[antigravity-sdk-python](https://github.com/google-antigravity/antigravity-sdk-python)** - ⭐ 1,646
   A Python library for building AI agents that leverage the full power of Google Antigravity.

413. **[claude-code-rust](https://github.com/lorryjovens-hub/claude-code-rust)** - ⭐ 1,637
   🚀 Rust 全量重构的 Claude Code - 性能提升 2.5x，体积减少 97% | High-performance Rust implementation of Claude Code with 2.5x faster startup and 97% smaller binary

414. **[core](https://github.com/RedPlanetHQ/core)** - ⭐ 1,636
   Your Personal AI OS

415. **[n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server)** - ⭐ 1,623
   MCP server that provides tools and resources for interacting with n8n API

416. **[mcp-brasil](https://github.com/Mcp-Brasil/mcp-brasil)** - ⭐ 1,620
   MCP Server para 70 APIs públicas brasileiras

417. **[codemcp](https://github.com/ezyang/codemcp)** - ⭐ 1,613
   Coding assistant MCP for Claude Desktop

418. **[ai](https://github.com/stripe/ai)** - ⭐ 1,603
   One-stop shop for building AI-powered products and businesses with Stripe.

419. **[mcp-server-guide](https://github.com/figma/mcp-server-guide)** - ⭐ 1,594
   A guide on how to use the Figma MCP server

420. **[mcptools](https://github.com/f/mcptools)** - ⭐ 1,592
   A command-line interface for interacting with MCP (Model Context Protocol) servers using both stdio and HTTP transport.

421. **[open-cowork](https://github.com/OpenCoworkAI/open-cowork)** - ⭐ 1,587
   Open-source AI agent desktop app for Windows & macOS. One-click install Claude Code, MCP tools, and Skills — with sandbox isolation, multi-model support, and Feishu/Slack integration.

422. **[Continuous-Claude-v2](https://github.com/parcadei/Continuous-Claude-v2)** - ⭐ 1,575
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

423. **[docker-mcp-tutorial](https://github.com/theNetworkChuck/docker-mcp-tutorial)** - ⭐ 1,564
   Complete tutorial materials for building MCP servers with Docker - from NetworkChuck's video

424. **[mcp-language-server](https://github.com/isaacphi/mcp-language-server)** - ⭐ 1,541
   mcp-language-server gives MCP enabled clients access semantic tools like get definition, references, rename, and diagnostics.

425. **[hotpath-rs](https://github.com/pawurb/hotpath-rs)** - ⭐ 1,540
   Quickly find bottlenecks in Rust - one profiler for CPU, time, memory, and async code.

426. **[rulego](https://github.com/rulego/rulego)** - ⭐ 1,539
   ⛓️RuleGo is a lightweight, high-performance, embedded, next-generation component orchestration rule engine framework for Go.

427. **[php-sdk](https://github.com/modelcontextprotocol/php-sdk)** - ⭐ 1,534
   The official PHP SDK for Model Context Protocol servers and clients. Maintained in collaboration with The PHP Foundation.

428. **[datagouv-mcp](https://github.com/datagouv/datagouv-mcp)** - ⭐ 1,533
   Official data.gouv.fr Model Context Protocol (MCP) server that allows AI chatbots to search, explore, and analyze datasets from the French national Open Data platform, directly through conversation.

429. **[mcp-installer](https://github.com/anaisbetts/mcp-installer)** - ⭐ 1,530
   An MCP server that installs other MCP servers for you

430. **[better-agents](https://github.com/langwatch/better-agents)** - ⭐ 1,529
   Standards for building agents, better

431. **[NagaAgent](https://github.com/RTGS2017/NagaAgent)** - ⭐ 1,524
   A simple yet powerful agent framework for personal assistants, designed to enable intelligent interaction, multi-agent collaboration, and seamless tool integration.

432. **[PrismerCloud](https://github.com/Prismer-AI/PrismerCloud)** - ⭐ 1,523
   Prismer Cloud

433. **[MCP-Reborn](https://github.com/Hexeption/MCP-Reborn)** - ⭐ 1,520
   MCP-Reborn is an MCP (Mod Coder Pack) for Minecraft for making modded clients and researching its code. (1.13-1.21.4)

434. **[opennews-mcp](https://github.com/6551Team/opennews-mcp)** - ⭐ 1,516
   News Aggregation · AI Ratings · Trading Signals · Real-time Updates

435. **[tavily-key-generator](https://github.com/skernelx/tavily-key-generator)** - ⭐ 1,511
   Multi-service toolkit for Tavily and Firecrawl signup automation, key validation, and isolated proxy pools.

436. **[MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP)** - ⭐ 1,510
   Official MiniMax Model Context Protocol (MCP) server that enables interaction with powerful Text to Speech, image generation and video generation APIs.

437. **[ghost-os](https://github.com/ghostwright/ghost-os)** - ⭐ 1,504
   Full computer-use for AI agents. Self-learning workflows. Native macOS. No screenshots required.

438. **[claudian](https://github.com/YishenTu/claudian)** - ⭐ 1,493
   An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault

439. **[Risuai](https://github.com/kwaroran/Risuai)** - ⭐ 1,490
   Make your own story. User-friendly software for LLM roleplaying

440. **[mcp-brasil](https://github.com/jxnxts/mcp-brasil)** - ⭐ 1,487
   MCP Server para 41 APIs públicas brasileiras

441. **[aso-skills](https://github.com/Eronred/aso-skills)** - ⭐ 1,479
   AI agent skills for App Store Optimization (ASO) and app marketing. Built for indie developers, app marketers, and growth teams who want Cursor, Claude Code, or any Agent Skills-compatible AI assistant to help with keyword research, metadata optimization, competitor analysis, and app growth.

442. **[code-mode](https://github.com/universal-tool-calling-protocol/code-mode)** - ⭐ 1,478
   🔌 Plug-and-play library to enable agents to call MCP and UTCP tools via code execution.

443. **[mcp-remote](https://github.com/geelen/mcp-remote)** - ⭐ 1,468

444. **[mcp-scan](https://github.com/invariantlabs-ai/mcp-scan)** - ⭐ 1,458
   Security scanner for AI agents, MCP servers and agent skills.

445. **[iMCP](https://github.com/mattt/iMCP)** - ⭐ 1,452
   A macOS app that provides an MCP server to your Messages, Contacts, Reminders and more

446. **[mcp-gateway](https://github.com/docker/mcp-gateway)** - ⭐ 1,447
   docker mcp CLI plugin / MCP Gateway

447. **[nixopus](https://github.com/nixopus/nixopus)** - ⭐ 1,446
   Run production apps without thinking about infrastructure. On your server or ours. Fully agentic.

448. **[docs-mcp-server](https://github.com/arabold/docs-mcp-server)** - ⭐ 1,440
   Grounded Docs MCP Server: Open-Source Alternative to Context7, Nia, and Ref.Tools

449. **[lime](https://github.com/limecloud/lime)** - ⭐ 1,440
     AI content workspace for Chinese creators: desktop writing, research, prompt   library, knowledge base, and multi-model workflows.

450. **[mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant)** - ⭐ 1,434
   An official Qdrant Model Context Protocol (MCP) server implementation

451. **[data-api-builder](https://github.com/Azure/data-api-builder)** - ⭐ 1,430
   Data API builder provides modern REST, GraphQL endpoints and MCP tools to your Azure Databases and on-prem stores.

452. **[phantom](https://github.com/ghostwright/phantom)** - ⭐ 1,429
   An AI co-worker with its own computer. Self-evolving, persistent memory, MCP server, secure credential collection, email identity. Built on the Claude Agent SDK.

453. **[claude-pilot](https://github.com/maxritter/claude-pilot)** - ⭐ 1,418
   Claude Code is powerful. Pilot makes it reliable. Start a task, grab a coffee, come back to production-grade code. Tests enforced. Context preserved. Quality automated.

454. **[MeiGen-AI-Design-MCP](https://github.com/jau123/MeiGen-AI-Design-MCP)** - ⭐ 1,416
   Supports GPT Image 2, Nanobanana & ComfyUI, with a 1,400+ prompt library, carefully crafted hooks and a multi-task orchestration system

455. **[mcpvault](https://github.com/bitbonsai/mcpvault)** - ⭐ 1,410
   A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access

456. **[mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** - ⭐ 1,407
   MCP Server for kubernetes management commands

457. **[swift-sdk](https://github.com/modelcontextprotocol/swift-sdk)** - ⭐ 1,407
   The official Swift SDK for Model Context Protocol servers and clients.

458. **[open-webSearch](https://github.com/Aas-ee/open-webSearch)** - ⭐ 1,406
   Multi-engine MCP server, CLI, and local daemon for agent web search and content retrieval — skill-guided workflows, no API keys.

459. **[terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server)** - ⭐ 1,403
   The Terraform MCP Server provides seamless integration with Terraform ecosystem, enabling advanced automation and interaction capabilities for Infrastructure as Code (IaC) development.

460. **[elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp)** - ⭐ 1,402
   The official ElevenLabs MCP server

461. **[kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk)** - ⭐ 1,388
   The official Kotlin SDK for Model Context Protocol servers and clients. Maintained in collaboration with JetBrains

462. **[npcpy](https://github.com/NPC-Worldwide/npcpy)** - ⭐ 1,386
   The python library for research and development in NLP, multimodal LLMs, Agents, ML, Knowledge Graphs, and more.

463. **[cunzhi](https://github.com/imhuso/cunzhi)** - ⭐ 1,377
   告别AI提前终止烦恼，助力AI更加持久

464. **[mcp-obsidian](https://github.com/smithery-ai/mcp-obsidian)** - ⭐ 1,373
   A connector for Claude Desktop to read and search an Obsidian vault.

465. **[stock-api](https://github.com/zhangxiangliang/stock-api)** - ⭐ 1,370
   查询 A 股、美股、港股与场内基金行情，并通过 Node.js、浏览器、CLI 或 MCP 快速接入。

466. **[deepwiki-mcp](https://github.com/regenrek/deepwiki-mcp)** - ⭐ 1,364
   📖 MCP server for fetch deepwiki.com and get latest knowledge in Cursor and other Code Editors

467. **[claude-init](https://github.com/cfrs2005/claude-init)** - ⭐ 1,358
   Claude Code 中文开发套件 - 为中国开发者定制的零门槛 AI 编程环境。一键安装完整中文化体验，集成 MCP 服务器、智能上下文管理、安全扫描，支持免翻墙访问。让 AI 编程更简单。

468. **[amical](https://github.com/amicalhq/amical)** - ⭐ 1,355
   🎙️ AI Dictation App - Open Source and Local-first ⚡ Type 3x faster, no keyboard needed. 🆓 Powered by open source models, works offline, fast and accurate.

469. **[LangAlpha](https://github.com/ginlix-ai/LangAlpha)** - ⭐ 1,348
   Claude Code for Finance

470. **[mcp-windbg](https://github.com/svnscha/mcp-windbg)** - ⭐ 1,345
   Model Context Protocol for WinDbg.

471. **[relaticle](https://github.com/relaticle/relaticle)** - ⭐ 1,341
   Open-source CRM with native AI agent support. 30 MCP tools, REST API, self-hosted. Built with Laravel & Filament

472. **[trpc-agent-go](https://github.com/trpc-group/trpc-agent-go)** - ⭐ 1,341
   A Go framework for building production agent systems with graph workflows, tools, memory, A2A, AG-UI, MCP, evaluation, and observability.

473. **[webclaw](https://github.com/0xMassi/webclaw)** - ⭐ 1,340
   Fast, local-first web content extraction for LLMs. Scrape, crawl, extract structured data — all from Rust. CLI, REST API, and MCP server.

474. **[OpenContracts](https://github.com/Open-Source-Legal/OpenContracts)** - ⭐ 1,335
   Humans and AI agents, building knowledge bases together. Self-hosted document annotation, version control, semantic search, and MCP.

475. **[ai-devkit](https://github.com/codeaholicguy/ai-devkit)** - ⭐ 1,333
   Make AI coding agents follow a repeatable engineering workflow with planning, memory, verification, skills, and review. One config. All agents. Same workflow.

476. **[apify-mcp-server](https://github.com/apify/apify-mcp-server)** - ⭐ 1,326
   The Apify MCP server enables your AI agents to extract data from social media, search engines, maps, e-commerce sites, or any other website using thousands of ready-made scrapers, crawlers, and automation tools available on the Apify Store.

477. **[nanobot](https://github.com/obot-platform/nanobot)** - ⭐ 1,324
   Build MCP Agents

478. **[vllm-mlx](https://github.com/waybarrios/vllm-mlx)** - ⭐ 1,324
   OpenAI and Anthropic compatible server for Apple Silicon. Run LLMs and vision-language models (Llama, Qwen-VL, LLaVA) with continuous batching, MCP tool calling, and multimodal support. Native MLX backend, 400+ tok/s. Works with Claude Code.

479. **[agency-orchestrator](https://github.com/jnMetaCode/agency-orchestrator)** - ⭐ 1,311
   🚀 One sentence → multi-AI-role collaboration → complete plan in minutes. 211+ expert roles, zero-code YAML, 9 LLM providers (6 free). 一句话调度多个AI专家自动协作，几分钟交付完整方案。

480. **[nanobot](https://github.com/nanobot-ai/nanobot)** - ⭐ 1,309
   Build MCP Agents

481. **[damn-vulnerable-MCP-server](https://github.com/harishsg993010/damn-vulnerable-MCP-server)** - ⭐ 1,306
   Damn Vulnerable MCP Server

482. **[apple-docs-mcp](https://github.com/kimsungwhee/apple-docs-mcp)** - ⭐ 1,304
   MCP server for Apple Developer Documentation - Search iOS/macOS/SwiftUI/UIKit docs, WWDC videos, Swift/Objective-C APIs & code examples in Claude, Cursor & AI assistants

483. **[langchain4j-aideepin](https://github.com/moyangzhan/langchain4j-aideepin)** - ⭐ 1,303
   基于AI的工作效率提升工具（聊天、绘画、知识库、工作流、 MCP服务市场、语音输入输出、长期记忆） | Ai-based productivity tools (Chat,Draw,RAG,Workflow,MCP marketplace, ASR,TTS, Long-term memory etc)

484. **[sourcey](https://github.com/sourcey/sourcey)** - ⭐ 1,302
   Precision documentation from OpenAPI, MCP, Doxygen, and Markdown guides. Static HTML you own.

485. **[agent-teams-ai](https://github.com/777genius/agent-teams-ai)** - ⭐ 1,300
   You're the boss, agents are your team. They handle tasks on their own, message each other, and review each other's work. You just watch the kanban board and give high-level commands. Codex/Claude/OpenCode(200+ models, 75+ LLM providers, free models no auth). Build your AI company with multiple teams.

486. **[codedb](https://github.com/justrach/codedb)** - ⭐ 1,300
   Zig code intelligence server and MCP toolset for AI agents. Fast tree, outline, symbol, search, read, edit, deps, snapshot, and remote GitHub repo queries.

487. **[mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server)** - ⭐ 1,295
   A Model Context Protocol (MCP) server that enables secure interaction with MySQL databases

488. **[xhs-toolkit](https://github.com/aki66938/xhs-toolkit)** - ⭐ 1,294
   📕 小红书创作者MCP工具包 - 支持与AI客户端集成的内容创作和发布工具

489. **[browserwing](https://github.com/browserwing/browserwing)** - ⭐ 1,294
   BrowserWing turns your browser actions into MCP commands Or Claude Skill, allowing AI agents to control browsers efficiently and reliably. Say goodbye to slow, token-heavy LLM interactions — let agents call commands directly for faster automation. Perfect for AI-driven tasks, browser automation, and boosting productivity.

490. **[xiaozhi-esp32-server-java](https://github.com/joey-zhou/xiaozhi-esp32-server-java)** - ⭐ 1,279
   小智ESP32的Java企业级管理平台，提供设备监控、音色定制、角色切换和对话记录管理的前后端及服务端一体化解决方案

491. **[drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server)** - ⭐ 1,278
   Draw.io Model Context Protocol (MCP) Server

492. **[ros-mcp-server](https://github.com/robotmcp/ros-mcp-server)** - ⭐ 1,278
   Connect AI models like Claude & GPT with robots using MCP and ROS.

493. **[sre](https://github.com/SmythOS/sre)** - ⭐ 1,277
   The SmythOS Runtime Environment (SRE) is an open-source, cloud-native runtime for agentic AI. Secure, modular, and production-ready, it lets developers build, run, and manage intelligent agents across local, cloud, and edge environments.

494. **[antigravity-workspace-template](https://github.com/study8677/antigravity-workspace-template)** - ⭐ 1,274
   Give Claude Code, Cursor, Codex CLI a ChatGPT for your codebase. Multi-agent knowledge engine, grounded Q&A with file paths and line numbers. Works in any AI IDE.

495. **[xmcp](https://github.com/basementstudio/xmcp)** - ⭐ 1,272
   The TypeScript MCP framework

496. **[minutes](https://github.com/silverstein/minutes)** - ⭐ 1,270
   Every meeting, every idea, every voice note — searchable by your AI. Open-source, privacy-first conversation memory layer.

497. **[cli](https://github.com/TanStack/cli)** - ⭐ 1,266
   The official TanStack CLI - Project Scaffolding, MCP Server, Agent Skills Installation, etc

498. **[agor](https://github.com/preset-io/agor)** - ⭐ 1,257
   Orchestrate Claude Code, Codex, and Gemini sessions on a multiplayer canvas. Manage git worktrees, track AI conversations, and visualize your team's agentic work in real-time.

499. **[mcp-adapter](https://github.com/WordPress/mcp-adapter)** - ⭐ 1,256
   An MCP adapter that bridges the Abilities API to the Model Context Protocol, enabling MCP clients to discover and invoke WordPress plugin, theme, and core abilities programmatically.

500. **[wenyan-mcp](https://github.com/caol64/wenyan-mcp)** - ⭐ 1,249
   文颜 MCP Server 可以让 AI 自动将 Markdown 文章排版后发布至微信公众号。

501. **[Agent-MCP](https://github.com/rinadelph/Agent-MCP)** - ⭐ 1,245
   Agent-MCP is a framework for creating multi-agent systems that enables coordinated, efficient AI collaboration through the Model Context Protocol (MCP). The system is designed for developers building AI applications that benefit from multiple specialized agents working in parallel on different aspects of a project.

502. **[fim-one](https://github.com/fim-ai/fim-one)** - ⭐ 1,241
   Open-source agent platform for Global × China enterprises — wire every system through one agent core. Self-hosted, any LLM.

503. **[web-eval-agent](https://github.com/refreshdotdev/web-eval-agent)** - ⭐ 1,240
   An MCP server that autonomously evaluates web applications.

504. **[duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server)** - ⭐ 1,234
   A Model Context Protocol (MCP) server that provides web search capabilities through DuckDuckGo, with additional features for content fetching and parsing.

505. **[KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server)** - ⭐ 1,232
   KiCAD MCP is a Model Context Protocol (MCP) implementation that enables Large Language Models (LLMs) like Claude to directly interact with KiCAD for printed circuit board design.

506. **[web-eval-agent](https://github.com/withRefresh/web-eval-agent)** - ⭐ 1,226
   An MCP server that autonomously evaluates web applications.

507. **[sceneview](https://github.com/sceneview/sceneview)** - ⭐ 1,224
   3D & AR SDK for Android (Jetpack Compose + Filament), iOS (SwiftUI + RealityKit), and Web. AI-first: llms.txt, MCP server, Copilot/Cursor rules. The only Compose-native 3D library.

508. **[mcp-golang](https://github.com/metoro-io/mcp-golang)** - ⭐ 1,223
   Write Model Context Protocol servers in few lines of go code. Docs at https://mcpgolang.com . Created by https://metoro.io

509. **[RisuAI](https://github.com/kwaroran/RisuAI)** - ⭐ 1,222
   Make your own story. User-friendly software for LLM roleplaying

510. **[davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp)** - ⭐ 1,220
   MCP server integration for DaVinci Resolve Studio

511. **[burp-ai-agent](https://github.com/six2dez/burp-ai-agent)** - ⭐ 1,219
   Burp Suite extension that adds built-in MCP tooling, AI-assisted analysis, privacy controls, passive and active scanning and more

512. **[AIPex](https://github.com/AIPexStudio/AIPex)** - ⭐ 1,210
   AIPex: AI browser automation assistant, no migration and privacy first. Alternative to Manus Browser Operator、 Claude Chrome and Agent Browser

513. **[A2V](https://github.com/Devin-AXIS/A2V)** - ⭐ 1,200
   A2V: Next-Gen AI Value Compute Protocol.

514. **[jarvis](https://github.com/isair/jarvis)** - ⭐ 1,198
   A 100% private AI voice assistant that lives on your computer (works offline). Talk naturally as if Jarvis is a third person in the room, and get conversational responses. It remembers everything, knows location and time, can check the web, control Chrome, track nutrition, and more with support for unlimited MCPs / tools without context rot.

515. **[hister](https://github.com/asciimoo/hister)** - ⭐ 1,195
   Your own search engine

516. **[agents](https://github.com/inkeep/agents)** - ⭐ 1,195
   Create AI Agents in a No-Code Visual Builder or TypeScript SDK with full 2-way sync. For shipping AI assistants and multi-agent AI workflows.

517. **[tradememory-protocol](https://github.com/mnemox-ai/tradememory-protocol)** - ⭐ 1,195
   Decision audit trail + persistent memory for AI trading agents. Outcome-weighted recall, SHA-256 tamper detection, 17 MCP tools.

518. **[telegram-mcp](https://github.com/chigwell/telegram-mcp)** - ⭐ 1,194
   Telegram MCP server powered by Telethon to let MCP clients read chats, manage groups, and send/modify messages, media, contacts, and settings.

519. **[himarket](https://github.com/higress-group/himarket)** - ⭐ 1,191
   HiMarket is an enterprise-level "AI Capability Marketplace and Developer Ecosystem Hub." It is not merely a simple aggregation of traditional APIs, but rather a comprehensive platform that packages, publishes, manages, and operates core AI assets such as enterprise Model APIs, MCP Servers, Agent APIs, etc., through standardized product formats.

520. **[ApeRAG](https://github.com/apecloud/ApeRAG)** - ⭐ 1,190
   ApeRAG: Production-ready GraphRAG with multi-modal indexing, AI agents, MCP support, and scalable K8s deployment

521. **[nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** - ⭐ 1,190
   A lightweight, rollbackable, and visual Long-Term Memory Server for MCP Agents. Say goodbye to Vector RAG and amnesia. Empower your AI with persistent, graph-like structured memory across any model, session, or tool. Drop-in replacement for OpenClaw.

522. **[azure-skills](https://github.com/microsoft/azure-skills)** - ⭐ 1,189
   Official agent plugin providing skills and MCP server configurations for Azure scenarios.

523. **[mcp-cli](https://github.com/philschmid/mcp-cli)** - ⭐ 1,185
   Lighweight CLI to interact with MCP servers

524. **[fast-mcp](https://github.com/yjacquin/fast-mcp)** - ⭐ 1,180
   A Ruby Implementation of the Model Context Protocol

525. **[short-video-maker](https://github.com/gyoridavid/short-video-maker)** - ⭐ 1,176
   Creates short videos for TikTok, Instagram Reels, and YouTube Shorts using the Model Context Protocol (MCP) and a REST API.

526. **[brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server)** - ⭐ 1,174

527. **[LetsFG](https://github.com/LetsFG/LetsFG)** - ⭐ 1,167
   Agent-native flight search & booking. Saved $116 across 5 routes vs Google Flights (verified). 400+ airlines in 5 seconds. Join the community - Star and spread the word

528. **[todo-for-ai](https://github.com/todo-for-ai/todo-for-ai)** - ⭐ 1,167
   🤖 A comprehensive task management system specifically designed for AI assistants. Supports project management, task tracking, team collaboration, and seamless AI integration through MCP (Model Context Protocol). Built with modern tech stack including React, Flask, and Docker. Try it now at https://todo4ai.org/

529. **[jarvis-registry](https://github.com/ascending-llc/jarvis-registry)** - ⭐ 1,165
   Connect any AI copilot or autonomous agent to your enterprise tools — through a single, secure MCP/Agent gateway with built-in identity, access control, and full observability.

530. **[Gearboy](https://github.com/drhelius/Gearboy)** - ⭐ 1,156
   Game Boy / Game Boy Color / Super Game Boy emulator, debugger and embedded MCP server for macOS, Windows, Linux, BSD and RetroArch.

531. **[anysearch-mcp-server](https://github.com/anysearch-ai/anysearch-mcp-server)** - ⭐ 1,153
   Unified real-time search engine skill for AI agents.

532. **[tabularis](https://github.com/debba/tabularis)** - ⭐ 1,153
   A lightweight, cross-platform database client for developers. Supports MySQL, PostgreSQL and SQLite. Hackable with plugins. Built for speed, security, and aesthetics.

533. **[jupyter-mcp-server](https://github.com/datalayer/jupyter-mcp-server)** - ⭐ 1,152
   🪐 🔧 Model Context Protocol (MCP) Server for Jupyter.

534. **[tuui](https://github.com/AI-QL/tuui)** - ⭐ 1,148
   A desktop MCP client designed as a tool unitary utility integration, accelerating AI adoption through the Model Context Protocol (MCP) and enabling cross-vendor LLM API orchestration.

535. **[trustgraph](https://github.com/trustgraph-ai/trustgraph)** - ⭐ 1,147
   Programmable Context for the AI Stack. Build. Version. Deploy. The full lifecycle platform for Context Graphs.

536. **[ktx](https://github.com/Kaelio/ktx)** - ⭐ 1,145
   ktx is an executable context layer for data and analytics agents 🐙 Allow Claude Code, Codex, or any other AI agent to query data accurately and with full context of your company

537. **[google-calendar-mcp](https://github.com/nspady/google-calendar-mcp)** - ⭐ 1,139
   MCP integration for Google Calendar to manage events.

538. **[keeper.sh](https://github.com/ridafkih/keeper.sh)** - ⭐ 1,137
   Calendar sync tool & universal calendar MCP server. Aggregate, sync and control calendars on Google, Outlook, Office 365, iCloud, CalDAV or ICS.

539. **[everything-claude-code-zh](https://github.com/xu-xiang/everything-claude-code-zh)** - ⭐ 1,130
   everything-claude-code 中文翻译项目：完整的 Claude Code 配置集合（agents, skills, hooks, commands, rules, MCPs）。源自 Anthropic 黑客松获胜者的实战配置，助力中文工程师高效理解与使用 Claude Code。

540. **[weave](https://github.com/Ataraxy-Labs/weave)** - ⭐ 1,126
   Entity-level git merge driver. Resolves false conflicts git invents when independent agents edit the same file. ~95% reduction vs. line-based merge.

541. **[ref-tools-mcp](https://github.com/ref-tools/ref-tools-mcp)** - ⭐ 1,126
   Helping coding agents never make mistakes working with public or private libraries without wasting the context window.

542. **[ai-dev-tools-zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)** - ⭐ 1,123
   AI Dev Tools Zoomcamp is a free course that helps you use AI tools to write better code, faster. We're starting the first cohort of this course on November 18, 2025! Sign up here to join us 👇🏼

543. **[opentwitter-mcp](https://github.com/6551Team/opentwitter-mcp)** - ⭐ 1,122
   Twitter/X Data · User Profiles · Tweet Search · Follower Events · KOL Tracking

544. **[ai-setup](https://github.com/caliber-ai-org/ai-setup)** - ⭐ 1,120
   Continuously sync your AI setups with one command. Codebase tailor suited agent skills, MCPs and config files for Claude Code, Cursor, and Codex.

545. **[better-chatbot](https://github.com/keinsaasforever/better-chatbot)** - ⭐ 1,118
   Formerly Better Chatbot. Navigator is an open-source AI workspace for agents, MCP and workflow automation.

546. **[better-chatbot](https://github.com/cgoinglove/better-chatbot)** - ⭐ 1,116
   Just a Better Chatbot. Powered by Agent & MCP & Workflows.

547. **[codesight](https://github.com/Houseofmvps/codesight)** - ⭐ 1,115
   Universal AI context generator. Saves thousands of tokens per conversation in Claude Code, Cursor, Copilot, Codex, and more.

548. **[iwe](https://github.com/iwe-org/iwe)** - ⭐ 1,115
   Markdown memory system for you and your AI agent

549. **[quickstart-resources](https://github.com/modelcontextprotocol/quickstart-resources)** - ⭐ 1,114
   A repository of servers and clients from the Model Context Protocol tutorials

550. **[freecad-mcp](https://github.com/neka-nat/freecad-mcp)** - ⭐ 1,105
   FreeCAD MCP(Model Context Protocol) server

551. **[llmwiki](https://github.com/lucasastorian/llmwiki)** - ⭐ 1,100
   Open Source Implementation of Karpathy's LLM Wiki. Upload documents, connect your Claude account via MCP, and have it write your wiki !

552. **[kordoc](https://github.com/chrisryugj/kordoc)** - ⭐ 1,091
   모두 파싱해버리겠다 — HWP3·HWP·HWPX·HWPML·PDF·XLS·XLSX·DOCX → Markdown. 신구대조·양식 자동 채우기·MCP 통합 (CLI + MCP Server) | Parse Korean documents (HWP3-5, HWPX, HWPML, PDF, Office) to Markdown — CLI + MCP Server with form-filler & diff

553. **[MCPJungle](https://github.com/mcpjungle/MCPJungle)** - ⭐ 1,090
   One place to manage & connect to all your MCP servers

554. **[tools](https://github.com/strands-agents/tools)** - ⭐ 1,089
   A set of tools that gives agents powerful capabilities.

555. **[figma-mcp-go](https://github.com/vkhanhqui/figma-mcp-go)** - ⭐ 1,087
   Figma MCP for free users — no rate limits, full read/write, text to designs, designs to code

556. **[thClaws](https://github.com/thClaws/thClaws)** - ⭐ 1,085
   Open-source AI agent harness in native Rust — GUI, CLI, headless, and webapp from one binary. Multi-provider, MCP, skills, plugins, agent teams.

557. **[better-icons](https://github.com/better-auth/better-icons)** - ⭐ 1,080
   Skill and MCP server for searching and retrieving icons

558. **[devops-ai-guidelines](https://github.com/VersusControl/devops-ai-guidelines)** - ⭐ 1,079
   First AI Journey for DevOps - with comprehensive learning paths, practical tips, and enterprise guidelines

559. **[cocos-mcp-server](https://github.com/DaxianLee/cocos-mcp-server)** - ⭐ 1,073
   一款全面的、便捷的cocos creator AI MCP服务插件，适用于3.8.0以上cocos版本，一键安装，一键启动。A comprehensive and convenient cocos creator AI MCP service plug-in, suitable for cocos versions above 3.8.0, one-click installation and one-click start.

560. **[awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers)** - ⭐ 1,072
   Remote MCP Servers

561. **[WebMCP](https://github.com/MiguelsPizza/WebMCP)** - ⭐ 1,070
   Bringing the power of MCP to the web

562. **[flock](https://github.com/Onelevenvy/flock)** - ⭐ 1,069
   A desktop multi-agent harness built with Rust, Tauri, and React, powered by langgraph-rust.

563. **[Gemini-Nexus](https://github.com/yeahhe365/Gemini-Nexus)** - ⭐ 1,065
   Gemini Nexus 是一款面向浏览器场景的 AI 助手扩展，集成 Gemini Web、Gemini API 与 OpenAI 兼容接口，支持网页上下文、图像处理、工具调用和 MCP 浏览器控制。

564. **[Proxima](https://github.com/Zen4-bit/Proxima)** - ⭐ 1,064
   Multi-AI MCP Server - Connect ChatGPT, Claude, Gemini & Perplexity to your coding tools without any API

565. **[lets-learn-mcp-python](https://github.com/microsoft/lets-learn-mcp-python)** - ⭐ 1,060
   MCP Python Tutorial

566. **[RedNote-MCP](https://github.com/iFurySt/RedNote-MCP)** - ⭐ 1,059
   🚀MCP server for accessing RedNote(XiaoHongShu, xhs).

567. **[xiaoyaosearch](https://github.com/dtsola/xiaoyaosearch)** - ⭐ 1,056
   小遥搜索，听懂你的话、看懂你的图，用AI找到本地任何文件。让搜索像聊天一样简单。XiaoyaoSearch: Understands your words, reads your images, finds any local file with AI. Making search as easy as chatting.

568. **[fetcher-mcp](https://github.com/jae-jae/fetcher-mcp)** - ⭐ 1,056
   MCP server for fetch web page content using Playwright headless browser.

569. **[SearChat](https://github.com/sear-chat/SearChat)** - ⭐ 1,053
   Search + Chat = SearChat(AI Chat with Search), Support OpenAI/Anthropic/VertexAI/Gemini, DeepResearch, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

570. **[open-codex-computer-use](https://github.com/iFurySt/open-codex-computer-use)** - ⭐ 1,050
   👾 Open Computer Use – Open-Source Alternative to Codex Computer Use

571. **[SearChat](https://github.com/yokingma/SearChat)** - ⭐ 1,050
   Search + Chat = SearChat(AI Chat with Search), Support OpenAI/Anthropic/VertexAI/Gemini, DeepResearch, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

572. **[mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server)** - ⭐ 1,048
   A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters.

573. **[minima](https://github.com/dmayboroda/minima)** - ⭐ 1,047
   On-premises conversational RAG with configurable containers

574. **[mirobody](https://github.com/thetahealth/mirobody)** - ⭐ 1,047
   Your Data, Your AI — Health, Finance & More. Open Source, Privacy-First.

575. **[Awesome-MCP-Servers](https://github.com/YuzeHao2023/Awesome-MCP-Servers)** - ⭐ 1,047
   A curated list of Model Context Protocol (MCP) servers

576. **[skales](https://github.com/skalesapp/skales)** - ⭐ 1,041
   Your personal AI desktop agent for Windows, macOS, Linux & Android. Set a goal, it works on its own. Teams (pair two desktops, agents + humans), Agent2Agent, Workflows, Codework, multi-agent orgs, desktop + browser automation. 15+ AI providers, BYOK. No Docker, no terminal. Agent Skills (SKILL.md). Migration importer. Recurring autonomous tasks.

577. **[Pixelle-MCP](https://github.com/AIDC-AI/Pixelle-MCP)** - ⭐ 1,040
   An Open-Source Multimodal AIGC Solution based on ComfyUI + MCP + LLM  https://pixelle.ai

578. **[CloudBase-MCP](https://github.com/TencentCloudBase/CloudBase-MCP)** - ⭐ 1,034
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app.

579. **[mcp-server-chatsum](https://github.com/chatmcp/mcp-server-chatsum)** - ⭐ 1,029
   Query and Summarize your chat messages.

580. **[724-office](https://github.com/wangziqi06/724-office)** - ⭐ 1,027
   7/24 Office — Self-evolving AI Agent system. 36 tools, 10,000 lines pure Python, modular architecture, MCP plugins, three-layer memory, nudge system, AI mirror, 24/7 production.

581. **[cs](https://github.com/boyter/cs)** - ⭐ 1,026
   codespelunker - CLI code search tool that understands code structure and ranks results by relevance. No indexing required with CLI, TUI, MCP and HTTP support.

582. **[search_with_ai](https://github.com/yokingma/search_with_ai)** - ⭐ 1,025
   AI Search Chat , Support DeepResearch, OpenAI/Anthropic/VertexAI/Gemini, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

583. **[mcp-boilerplate](https://github.com/iannuttall/mcp-boilerplate)** - ⭐ 1,022
   A remote Cloudflare MCP server boilerplate with user authentication and Stripe for paid tools.

584. **[unreal-engine-mcp](https://github.com/flopperam/unreal-engine-mcp)** - ⭐ 1,016
   Control Unreal Engine 5.5+ through AI with natural language. Build incredible 3D worlds and architectural masterpieces using MCP. Create entire towns, medieval castles, modern mansions, challenging mazes, and complex structures with AI-powered commands.

585. **[reactuse](https://github.com/childrentime/reactuse)** - ⭐ 1,015
   115+ production-ready React Hooks for sensors, UI, state & browser APIs. Tree-shakable, SSR-safe, TypeScript-first. Used by Shopee, PDD & Ctrip. Inspired by VueUse.

586. **[MassGen](https://github.com/massgen/MassGen)** - ⭐ 1,010
   🚀 MassGen is an open-source multi-agent scaling system that runs in your terminal, autonomously orchestrating frontier models and agents to collaborate, reason, and produce high-quality results. | Join us on Discord: discord.massgen.ai

587. **[google-meta-ads-ga4-mcp](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp)** - ⭐ 1,009
   MCP server for Google Ads, Meta Ads & GA4 — works with ChatGPT, Claude, Cursor, n8n, Windsurf & more. 250+ tools for campaign management, analytics & optimization.

588. **[cve-mcp-server](https://github.com/mukul975/cve-mcp-server)** - ⭐ 1,007
   Production-grade MCP server giving Claude 27 security intelligence tools across 21 APIs — CVE lookup, EPSS scoring, CISA KEV, MITRE ATT&CK, Shodan, VirusTotal, and more.

589. **[muapi-cli](https://github.com/SamurAIGPT/muapi-cli)** - ⭐ 1,001
   Official CLI for muapi.ai — generate images, videos & audio from the terminal. MCP server, 14 AI models, npm + pip installable.

590. **[mcpdoc](https://github.com/langchain-ai/mcpdoc)** - ⭐ 999
   Expose llms-txt to IDEs for development

591. **[awesome-devops-mcp-servers](https://github.com/rohitg00/awesome-devops-mcp-servers)** - ⭐ 998
   A curated list of awesome MCP servers focused on DevOps tools and capabilities.

592. **[ThinkWatch](https://github.com/ThinkWatchProject/ThinkWatch)** - ⭐ 995
   Enterprise AI bastion host for secure AI API and MCP access, with unified proxying, RBAC, audit logs, rate limiting, and cost tracking across OpenAI, Anthropic, Gemini, and self-hosted LLMs.

593. **[eide](https://github.com/github0null/eide)** - ⭐ 993
   An embedded development environment for mcs51/stm8/avr/cortex-m/riscv on VsCode.

594. **[hope-agent](https://github.com/shiwenwen/hope-agent)** - ⭐ 989
   🦭跨端交接、越用越懂你的桌面 AI 助手——也能服务化常驻、跑在云上 | Desktop AI that hands off across your devices and gets to know you better — also runs headless on a NAS or in the cloud

595. **[openapi-servers](https://github.com/open-webui/openapi-servers)** - ⭐ 986
   OpenAPI Tool Servers

596. **[chatlog_alpha](https://github.com/teest114514/chatlog_alpha)** - ⭐ 982
   原 [chatlog]项目（一个微信数据库解密读取及提供mcp服务、http服务的开源软件），现已支持通过微信clawbot接口推送消息，可以实时转发全部或指定消息到clawbot

597. **[meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp)** - ⭐ 981
   MCP server to manage Facebook and Instagram Ads (Meta Ads)

598. **[mcp-gsc](https://github.com/AminForou/mcp-gsc)** - ⭐ 980
   Google Search Console Insights with Claude AI for SEOs

599. **[qgis_mcp](https://github.com/jjsantos01/qgis_mcp)** - ⭐ 980
   Model Context Protocol (MCP) that allows LLMs to use QGIS Desktop

600. **[token-savior](https://github.com/Mibayy/token-savior)** - ⭐ 980
   The MCP server that turns Claude into the only coding agent hitting 100% on a real benchmark. -77% active tokens, -76% wall time, 0 losses across 96 tasks on Claude Opus 4.7. Structural code navigation + persistent memory. Works with every MCP client.

601. **[arkon](https://github.com/nduckmink/arkon)** - ⭐ 980
   Arkon: Enterprise AI Knowledge Hub & MCP Server. Self-hosted knowledge base for teams to manage RAG contexts, access policies, and AI skills. Connect Claude and other LLMs via Model Context Protocol (MCP) for automated, secure organizational knowledge integration.

602. **[MODULAR-RAG-MCP-SERVER](https://github.com/jerry-ai-dev/MODULAR-RAG-MCP-SERVER)** - ⭐ 978
   A modular RAG (Retrieval-Augmented Generation) system with MCP Server architecture. Using Skill to make AI follow each step of the spec and complete the code 100% by AI.

603. **[yargi-mcp](https://github.com/saidsurucu/yargi-mcp)** - ⭐ 978
   MCP Server For Turkish Legal Databases

604. **[agentic-radar](https://github.com/splx-ai/agentic-radar)** - ⭐ 978
   A security scanner for your LLM agentic workflows

605. **[gemini-nexus](https://github.com/yeahhe365/gemini-nexus)** - ⭐ 976
   Gemini Nexus 是一款深度集成 Google Gemini 能力的 Chrome 扩展程序。它不仅仅是一个侧边栏插件，而是通过注入式的悬浮工具栏、强大的图像 AI 处理以及前沿的浏览器控制协议 (MCP)，将 AI 的触角伸向网页浏览的每一个交互细节。

606. **[ollama-mcp-bridge](https://github.com/patruff/ollama-mcp-bridge)** - ⭐ 974
   Bridge between Ollama and MCP servers, enabling local LLMs to use Model Context Protocol tools

607. **[claude-delegator](https://github.com/jarrodwatts/claude-delegator)** - ⭐ 973
   Delegate tasks to Codex and Gemini directly from within Claude Code.

608. **[excel-mcp-server](https://github.com/negokaz/excel-mcp-server)** - ⭐ 969
   A Model Context Protocol (MCP) server that reads and writes MS Excel data

609. **[mcpm.sh](https://github.com/pathintegral-institute/mcpm.sh)** - ⭐ 968
   CLI MCP package manager & registry for all platforms and all clients. Search & configure MCP servers. Advanced Router & Profile features.

610. **[code-index-mcp](https://github.com/johnhuang316/code-index-mcp)** - ⭐ 964
   A Model Context Protocol (MCP) server that helps large language models index, search, and analyze code repositories with minimal setup

611. **[mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)** - ⭐ 962
   Scan MCP servers for potential threats & security findings.

612. **[matlab-mcp-core-server](https://github.com/matlab/matlab-mcp-core-server)** - ⭐ 960
   Run MATLAB® using AI applications with the official MATLAB MCP Server from MathWorks®. This MCP server for MATLAB supports a wide range of coding agents like Claude Code® and Visual Studio® Code.

613. **[mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains)** - ⭐ 959
   A model context protocol server to work with JetBrains IDEs: IntelliJ, PyCharm, WebStorm, etc. Also, works with Android Studio

614. **[mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j)** - ⭐ 959
   Neo4j Labs Model Context Protocol servers

615. **[awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw)** - ⭐ 958
   A curated list of OpenClaw resources, tools, skills, tutorials & articles. OpenClaw (formerly Moltbot / Clawdbot) — open-source self-hosted AI agent for WhatsApp, Telegram, Discord & 50+ integrations.

616. **[AI-Gateway](https://github.com/Azure-Samples/AI-Gateway)** - ⭐ 943
   Labs to explore AI Models, MCP servers, and Agents with the AI Gateway powered by Azure API Management and Microsoft Foundry 🚀

617. **[OpenDerisk](https://github.com/derisk-ai/OpenDerisk)** - ⭐ 943
   AI-Native Risk Intelligence Systems, OpenDeRisk——Your application system risk intelligent manager provides 7* 24-hour comprehensive and in-depth protection.

618. **[x-reader](https://github.com/runesleo/x-reader)** - ⭐ 943
   Universal content reader MCP Server for 10+ platforms

619. **[web-search-mcp](https://github.com/mrkrsl/web-search-mcp)** - ⭐ 941
   A simple, locally hosted Web Search MCP server for use with Local LLMs

620. **[mcp-browser-use](https://github.com/Saik0s/mcp-browser-use)** - ⭐ 939

621. **[chatgpt-cli](https://github.com/kardolus/chatgpt-cli)** - ⭐ 933
   ChatGPT CLI is a powerful, multi-provider command-line interface for working with modern LLMs. It supports OpenAI, Azure, Perplexity, LLaMA, and more, with features like streaming, interactive chat, prompt files, image/audio I/O, MCP tool calls, and an experimental agent mode for safe, multi-step automation.

622. **[MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge)** - ⭐ 929
   A middleware to provide an openAI compatible endpoint that can call MCP tools

623. **[12306-mcp](https://github.com/Joooook/12306-mcp)** - ⭐ 928
   This is a 12306 ticket search server based on the Model Context Protocol (MCP).

624. **[mcp-framework](https://github.com/QuantGeekDev/mcp-framework)** - ⭐ 921
   The Typescript MCP Framework

625. **[arcade-mcp](https://github.com/ArcadeAI/arcade-mcp)** - ⭐ 919
   MCP Server Framework and Tool Development library for building custom capabilities into agents.

626. **[shellfirm](https://github.com/kaplanelad/shellfirm)** - ⭐ 917
   Safety guardrails for ai coding agents and human terminal commands

627. **[wassette](https://github.com/microsoft/wassette)** - ⭐ 916
   Wassette: A security-oriented runtime that runs WebAssembly Components via MCP

628. **[memory-bank-mcp](https://github.com/alioshr/memory-bank-mcp)** - ⭐ 912
   A Model Context Protocol (MCP) server implementation for remote memory bank management, inspired by Cline Memory Bank.

629. **[mcp-sequential-thinking](https://github.com/arben-adm/mcp-sequential-thinking)** - ⭐ 910

630. **[nuxt-mcp-dev](https://github.com/antfu/nuxt-mcp-dev)** - ⭐ 909
   MCP server helping models to understand your Vite/Nuxt app better.

631. **[kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server)** - ⭐ 909
   Published in CNCF Landscape: A MCP server for Kubernetes.

632. **[CloudBase-AI-ToolKit](https://github.com/TencentCloudBase/CloudBase-AI-ToolKit)** - ⭐ 909
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app in one click.

633. **[mcp-course](https://github.com/huggingface/mcp-course)** - ⭐ 907

634. **[stitch-mcp](https://github.com/davideast/stitch-mcp)** - ⭐ 904
   A CLI for moving AI-generated UI designs from Google’s Stitch platform into your development workflow.

635. **[mcp-google-sheets](https://github.com/xing5/mcp-google-sheets)** - ⭐ 904
   This MCP server integrates with your Google Drive and Google Sheets, to enable creating and modifying spreadsheets.

636. **[butterbase-oss](https://github.com/butterbase-ai/butterbase-oss)** - ⭐ 903
   Open-source backend-as-a-service. Postgres, auth, storage, functions, AI gateway, MCP.

637. **[mcp-notion-server](https://github.com/suekou/mcp-notion-server)** - ⭐ 901
   A Model Context Protocol server for connecting Notion to MCP-compatible clients

638. **[flow-like](https://github.com/Rheosoph/flow-like)** - ⭐ 898
   Flow-Like: Strongly Typed Enterprise Scale Workflows. Built for scalability, speed, seamless AI integration and rich customization.

639. **[openapi-mcp-server](https://github.com/janwilmake/openapi-mcp-server)** - ⭐ 895
   Allow AI to wade through complex OpenAPIs using Simple Language

640. **[MCProtocolLib](https://github.com/GeyserMC/MCProtocolLib)** - ⭐ 892
   A library for communication with a Minecraft client/server.

641. **[mcp-searxng](https://github.com/ihor-sokoliuk/mcp-searxng)** - ⭐ 892
   Private web search for AI assistants via SearXNG — supports Claude, Cursor, and any MCP client

642. **[annas-mcp](https://github.com/iosifache/annas-mcp)** - ⭐ 890
   MCP server and CLI tool for searching and downloading documents from Anna's Archive

643. **[zotero-mcp](https://github.com/cookjohn/zotero-mcp)** - ⭐ 889
   It's a plugin extension in Zotero.  Zotero MCP Plugin enables integration between AI assistants and Zotero through MCP. Zotero MCP Plugin 是一个 Zotero 插件，通过 MCP协议实现 AI 助手与 Zotero深度集成。插件支持文献检索、元   数据管理、全文分析和智能问答等功能，让 Claude、ChatGPT 等 AI 工具能够直接访问和操作您的文献库。

644. **[mcp-server](https://github.com/PortSwigger/mcp-server)** - ⭐ 889
   MCP Server for Burp

645. **[mq](https://github.com/harehare/mq)** - ⭐ 886
   A jq-like Markdown query language for command-line processing

646. **[agent-kit](https://github.com/inngest/agent-kit)** - ⭐ 886
   AgentKit: Build multi-agent networks in TypeScript with deterministic routing and rich tooling via MCP.

647. **[nekro-agent](https://github.com/KroMiose/nekro-agent)** - ⭐ 885
   NekroAgent 是一个面向多人互动场景的跨平台 Agent 框架，集 Claude Code 沙盒执行、工作区编排、长期记忆、结构化 MCP 管理与可视化控制台于一体，兼具高扩展性、多模态交互、实时状态推送和自动化运行能力。项目支持 QQ、Discord、Telegram、Minecraft、BilibiliLive、WeChat、Email、SSE(SDK) 等多种平台接入，应用于构建高智能聊天机器人，可扩展为具备代码执行、工具调用、插件协作和复杂任务处理能力的通用 Agent 系统

648. **[mix.core](https://github.com/mixcore/mix.core)** - ⭐ 885
   🚀 A future-proof enterprise web CMS supporting both headless and decoupled approaches. Build any type of app with customizable APIs on ASP.NET Core/.NET Core. Completely open-source and designed for flexibility. Since 2018.

649. **[hyper-mcp](https://github.com/hyper-mcp-rs/hyper-mcp)** - ⭐ 880
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

650. **[awesome-mcp-list](https://github.com/MobinX/awesome-mcp-list)** - ⭐ 879
   A concise list for mcp servers

651. **[work-iq](https://github.com/microsoft/work-iq)** - ⭐ 877
   MCP Server and CLI for accessing Work IQ

652. **[restheart](https://github.com/SoftInstigate/restheart)** - ⭐ 877
   The Agent-Ready Backend for MongoDB.

653. **[excalidraw-mcp-app](https://github.com/antonpk1/excalidraw-mcp-app)** - ⭐ 876
   Excalidraw MCP App Server — hand-drawn diagrams for Claude

654. **[LaunchStack](https://github.com/Deodat-Lawson/LaunchStack)** - ⭐ 870
   AI-powered StartUp Accelerator Engine built with Next.js, LangChain, PostgreSQL + pgvector. Upload, organize, and chat with documents. Includes predictive missing-document detection, role-based workflows, and page-level insight extraction.

655. **[flow-like](https://github.com/TM9657/flow-like)** - ⭐ 865
   Flow-Like: Strongly Typed Enterprise Scale Workflows. Built for scalability, speed, seamless AI integration and rich customization.

656. **[mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** - ⭐ 864
   MCP server enabling persistent memory for Claude through a local knowledge graph - fork focused on local development

657. **[octocode](https://github.com/bgauryy/octocode)** - ⭐ 863
   MCP server for semantic code research and context generation on real-time using LLM patterns | Search naturally across public & private repos based on your permissions | Transform any accessible codebase/s into AI-optimized knowledge on simple and complex flows | Find real implementations and live docs from anywhere

658. **[stackql](https://github.com/stackql/stackql)** - ⭐ 862
   Query, provision and operate Cloud and SaaS resources and APIs using an extensible SQL based framework

659. **[claude_agent_teams_ui](https://github.com/777genius/claude_agent_teams_ui)** - ⭐ 860
   You're the CTO, agents are your team. They handle tasks on their own, message each other, and review each other's work. You just watch the kanban board and give high-level commands. Codex/Claude/OpenCode(75+ LLM providers). Build your AI company.

660. **[pydantic-deepagents](https://github.com/vstorm-co/pydantic-deepagents)** - ⭐ 859
   Build Claude Code–style deep agents in Python: tool-calling, sandboxed execution, multi-agent teams, skills, checkpoints, and unlimited context — all on Pydantic AI.

661. **[agentshield](https://github.com/affaan-m/agentshield)** - ⭐ 856
   AI agent security scanner. Detect vulnerabilities in agent configurations, MCP servers, and tool permissions. Available as CLI, GitHub Action, ECC plugin, and GitHub App integration. 🛡️

662. **[agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws)** - ⭐ 853
   Official, AWS-supported MCP servers, skills, and plugins to help AI agents build on AWS

663. **[powerbi-modeling-mcp](https://github.com/microsoft/powerbi-modeling-mcp)** - ⭐ 851
   The Power BI Modeling MCP Server, brings Power BI semantic modeling capabilities to your AI agents.

664. **[pi-mcp-adapter](https://github.com/nicobailon/pi-mcp-adapter)** - ⭐ 850
   Token-efficient MCP adapter for Pi coding agent

665. **[Foundry](https://github.com/promptise-com/Foundry)** - ⭐ 849
   The foundation layer for agentic intelligence.

666. **[ruby-sdk](https://github.com/modelcontextprotocol/ruby-sdk)** - ⭐ 846
   The official Ruby SDK for the Model Context Protocol.

667. **[server](https://github.com/php-mcp/server)** - ⭐ 846
   Core PHP implementation for the Model Context Protocol (MCP) server

668. **[Octocode](https://github.com/bgauryy/Octocode)** - ⭐ 845
   MCP server for semantic code research and context generation on real-time using LLM patterns | Search naturally across public & private repos based on your permissions | Transform any accessible codebase/s into AI-optimized knowledge on simple and complex flows | Find real implementations and live docs from anywhere

669. **[coderunner](https://github.com/instavm/coderunner)** - ⭐ 844
   A local sandbox for your AI agents

670. **[octocode-mcp](https://github.com/bgauryy/octocode-mcp)** - ⭐ 842
   MCP server for semantic code research and context generation on real-time using LLM patterns | Search naturally across public & private repos based on your permissions | Transform any accessible codebase/s into AI-optimized knowledge on simple and complex flows | Find real implementations and live docs from anywhere

671. **[ScienceClaw](https://github.com/beita6969/ScienceClaw)** - ⭐ 841
   🔬🦞 A self-evolving AI research colleague for scientists. 285 skills, zero hallucination, persistent memory.

672. **[ainativelang](https://github.com/sbhooley/ainativelang)** - ⭐ 839
   AINL helps turn AI from "a smart conversation" into "a structured worker."  It is designed for teams building AI workflows that need multiple steps, state and memory, tool use, repeatable execution, validation and control, and lower dependence on long prompt loops.  AINL is a compact, graph-canonical, AI-native programming system for (READ: README)

673. **[yokai](https://github.com/ankorstore/yokai)** - ⭐ 835
   Simple, modular, and observable Go framework for backend applications.

674. **[cheatengine-mcp-bridge](https://github.com/miscusi-peek/cheatengine-mcp-bridge)** - ⭐ 835
   Connect Cursor, Copilot & Claude AI directly to Cheat Engine via MCP. Automate reverse engineering, pointer scanning, and memory analysis using natural language.

675. **[hyper-mcp](https://github.com/tuananh/hyper-mcp)** - ⭐ 835
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

676. **[bank-api](https://github.com/erwinkramer/bank-api)** - ⭐ 834
   The Bank API is a design reference project suitable to bootstrap development for a compliant and modern API.

677. **[hyper-mcp](https://github.com/joseph-wortmann/hyper-mcp)** - ⭐ 834
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

678. **[gcloud-mcp](https://github.com/googleapis/gcloud-mcp)** - ⭐ 831
   gcloud MCP server

679. **[cyberboss](https://github.com/WenXiaoWendy/cyberboss)** - ⭐ 831
   一个接入微信的本地生活 Agent Bridge，让 Codex / Claude Code 拥有时间感、行踪感、随机唤醒和自主唤醒能力，用主动陪伴替代所有番茄钟和效率工具，自动记录日记、维护生活时间轴、发送文件和表情包，并调用 MCP / 本地工具。

680. **[scira-mcp-chat](https://github.com/zaidmukaddam/scira-mcp-chat)** - ⭐ 830
   A minimalistic MCP client with a good feature set.

681. **[awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins)** - ⭐ 829
   Awesome Claude Code plugins — a curated list of slash commands, subagents, MCP servers, and hooks for Claude Code

682. **[golf](https://github.com/golf-mcp/golf)** - ⭐ 829
   Production-Ready MCP Server Framework • Build, deploy & scale secure AI agent infrastructure • Includes Auth, Observability, Debugger, Telemetry & Runtime • Run real-world MCPs powering AI Agents

683. **[MCP-Security-Checklist](https://github.com/slowmist/MCP-Security-Checklist)** - ⭐ 829
   A comprehensive security checklist for MCP-based AI tools. Built by SlowMist to safeguard LLM plugin ecosystems.

684. **[k8m](https://github.com/weibaohui/k8m)** - ⭐ 829
   一款轻量级、跨平台的 Mini Kubernetes AI Dashboard，支持大模型+智能体+MCP(支持设置操作权限)，集成多集群管理、智能分析、实时异常检测等功能，支持多架构并可单文件部署，助力高效集群管理与运维优化。

685. **[supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server)** - ⭐ 828
   Query MCP enables end-to-end management of Supabase via chat interface: read & write query executions, management API support, automatic migration versioning, access to logs and much more.

686. **[cupertino](https://github.com/mihaelamj/cupertino)** - ⭐ 828
   A local Apple Documentation crawler and MCP server. Written in Swift.

687. **[universal-db-mcp](https://github.com/Anarkh-Lee/universal-db-mcp)** - ⭐ 826
   通用数据库 MCP 连接器：支持 MySQL、PostgreSQL、Oracle、MongoDB 等 17 种数据库，支持 Claude Desktop、Cursor、Windsurf、VS Code、ChatGPT 等 50+ 平台，用自然语言查询和分析数据

688. **[JSReverser-MCP](https://github.com/NoOne-hub/JSReverser-MCP)** - ⭐ 824
   JSReverser-MCP 是一个面向 JavaScript 逆向分析的 MCP 工具，专门用于帮助开发者在真实浏览器环境中高效定位前端核心逻辑。它   将脚本检索、断点调试、函数 Hook、网络请求追踪、调用链分析、混淆还原和风险评估整合为统一能力，可直接接入 Claude、   Codex、Cursor 等支持 MCP 的客户端。你可以连接已开启的 Chrome，在登录态页面下持续采样请求参数与返回数据，快速定位签名、   加密、鉴权和关键业务流程。工具同时支持自动化页面操作与结构化报告导出，适合用于接口分析、安全研究、前端调试与工程排障等   场景

689. **[browser-use-mcp-server](https://github.com/kontext-security/browser-use-mcp-server)** - ⭐ 823
   Browse the web, directly from Cursor etc.

690. **[gemini-skill](https://github.com/WJZ-P/gemini-skill)** - ⭐ 823
   gemini drawing MCP & skill through browser, can be used in openclaw or any agent that supports MCP. Gemini画图 MCP和sill，支持龙虾或任何agent使用٩(๑>◡<๑)۶

691. **[obot](https://github.com/obot-platform/obot)** - ⭐ 822
   Complete MCP Platform -- Hosting, Registry, Gateway, and Chat Client

692. **[glean](https://github.com/LeslieLeung/glean)** - ⭐ 820
   A self-hosted RSS reader and personal knowledge management tool.

693. **[browser-use-mcp-server](https://github.com/kontext-dev/browser-use-mcp-server)** - ⭐ 818
   Browse the web, directly from Cursor etc.

694. **[heurist-agent-framework](https://github.com/heurist-network/heurist-agent-framework)** - ⭐ 817
   A flexible multi-interface AI agent framework for building agents with reasoning, tool use, memory, deep research, blockchain interaction, MCP, and agents-as-a-service.

695. **[macos-automator-mcp](https://github.com/steipete/macos-automator-mcp)** - ⭐ 817
   An MCP server to run AppleScript and JXA (JavaScript for Automation) to macOS.

696. **[alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server)** - ⭐ 816
   Alpaca’s official MCP Server lets you trade stocks, ETFs, crypto, and options, run data analysis, and build strategies in plain English directly from your favorite LLM tools and IDEs

697. **[agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)** - ⭐ 815
   A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.

698. **[oxideterm](https://github.com/AnalyseDeCircuit/oxideterm)** - ⭐ 815
   AI-native workspace for local shells and remote machines.Zero Electron, zero OpenSSL, zero telemetry, and no app subscription.

699. **[AITreasureBox](https://github.com/superiorlu/AITreasureBox)** - ⭐ 814
   🤖 Automatically collected AI repos, tools, websites, papers & tutorials. 实用AI百宝箱 💎

700. **[DeepMCPAgent](https://github.com/cryxnet/DeepMCPAgent)** - ⭐ 813
   Model-agnostic plug-n-play LangChain/LangGraph agents powered entirely by MCP tools over HTTP/SSE.

701. **[acemcp](https://github.com/qy527145/acemcp)** - ⭐ 813
   一个将ACE(Augment Context Engine) 做成MCP的项目

702. **[context-space](https://github.com/context-space/context-space)** - ⭐ 810
   Ultimate Context Engineering Infrastructure, starting from MCPs and Integrations

703. **[toolfront](https://github.com/statespace-tech/toolfront)** - ⭐ 809
   Turn your data into shareable RAG apps in minutes. All in pure Markdown. Zero boilerplate.

704. **[mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse)** - ⭐ 801
   Connect ClickHouse to your AI assistants.

705. **[codegraph-rust](https://github.com/Jakedismo/codegraph-rust)** - ⭐ 801
   100% Rust implementation of code graphRAG with blazing fast AST+FastML parsing, surrealDB backend and advanced agentic code analysis tools through MCP for efficient code agent context management

706. **[vllora](https://github.com/vllora/vllora)** - ⭐ 800
   Debug your AI agents

707. **[vibetest-use](https://github.com/browser-use/vibetest-use)** - ⭐ 799
   Vibetest MCP - automated QA testing using Browser-Use agents

708. **[Context](https://github.com/indragiek/Context)** - ⭐ 798
   Native macOS client for Model Context Protocol (MCP)

709. **[xmcp](https://github.com/xdevplatform/xmcp)** - ⭐ 798
   MCP server for the X API

710. **[k-dense-byok](https://github.com/K-Dense-AI/k-dense-byok)** - ⭐ 797
   An AI co-scientist powered by Scientific Agent Skills running on your desktop.

711. **[llm-server-docs](https://github.com/varunvasudeva1/llm-server-docs)** - ⭐ 787
   End-to-end documentation to set up your own local & fully private LLM server on Debian. Equipped with chat, web search, RAG, model management, MCP servers, image generation, and TTS.

712. **[claude-video-vision](https://github.com/jordanrendric/claude-video-vision)** - ⭐ 786
   Give Claude the ability to watch and understand videos — Claude Code plugin with frame extraction and multimodal audio analysis

713. **[reverse-api-engineer](https://github.com/kalil0321/reverse-api-engineer)** - ⭐ 785
   The agent that turns websites into APIs!

714. **[openpets](https://github.com/alvinunreal/openpets)** - ⭐ 784
   Desktop pets for AI coding agents. Install pets, connect Claude Code via MCP, and see live coding status on your desktop.

715. **[samples](https://github.com/strands-agents/samples)** - ⭐ 784
   Agent samples built using the Strands Agents SDK.

716. **[argo](https://github.com/xark-argo/argo)** - ⭐ 784
   ARGO is an open-source AI Agent platform that brings Local Manus to your desktop. With one-click model downloads, seamless closed LLM integration, and offline-first RAG knowledge bases, ARGO becomes a DeepResearch powerhouse for autonomous thinking, task planning, and 100% of your data stays locally. Support Win/Mac/Docker.

717. **[nuwax](https://github.com/nuwax-ai/nuwax)** - ⭐ 782
   Nuwax Agent OS - An enterprise-grade AI Agent Development and Operation Platform - Providing a complete solution for agent creation and distribution, knowledge base management, model proxy, memory system, and plugin ecosystem.

718. **[drift](https://github.com/dadbodgeoff/drift)** - ⭐ 781
   Codebase intelligence for AI. Detects patterns & conventions + remembers decisions across sessions. MCP server for any IDE. Offline CLI.

719. **[fetch-mcp](https://github.com/zcaceres/fetch-mcp)** - ⭐ 781
   A flexible HTTP fetching Model Context Protocol server.

720. **[room](https://github.com/quoroom-ai/room)** - ⭐ 779
   Open-source earning-focused swarm intelligence engine. Self-governing AI collectives (queen, workers, quorum voting) running locally via MCP. Works with Claude Code, Codex, or pay-per-use APIs.

721. **[ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server)** - ⭐ 779
   A Model Context Protocol (MCP) server for interacting with Microsoft 365 and Office services through the Graph API

722. **[mcp-marketplace](https://github.com/cline/mcp-marketplace)** - ⭐ 778
   This is the official repository for submitting MCP servers to be included in Cline's MCP Marketplace. If you’ve built an MCP server and want it to be discoverable and easily installable by millions of developers using Cline, submit your server here.

723. **[atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server)** - ⭐ 776
   Remote MCP Server that securely connects Jira and Confluence with your LLM, IDE, or agent platform of choice.

724. **[bytechef](https://github.com/bytechefhq/bytechef)** - ⭐ 772
   Open-source platform that unifies AI agent orchestration and workflow automation — autonomy and precision in one platform.

725. **[pdf-reader-mcp](https://github.com/SylphxAI/pdf-reader-mcp)** - ⭐ 770
   📄 Production-ready MCP server for PDF processing - 5-10x faster with parallel processing and 94%+ test coverage

726. **[mcp](https://github.com/hyperbrowserai/mcp)** - ⭐ 768
   A MCP server implementation for hyperbrowser

727. **[NornicDB](https://github.com/orneryd/NornicDB)** - ⭐ 768
   Nornicdb is a distributed low-latency, Graph+Vector, Temporal MVCC with all sub-ms HNSW search, graph traversal, and writes. Using Neo4j Bolt/Cypher and qdrant's gRPC means you can switch with no changes while adding intelligent features like schemas, managed embeddings, reranking+llm, GPU accel, Auto-TLP, Policy-based Memory Decay, and MCP server.

728. **[runno](https://github.com/taybenlor/runno)** - ⭐ 767
   Sandboxed runtime for programming languages and WASI binaries. Works in the browser, on your server, or via MCP.

729. **[context-portal](https://github.com/GreatScottyMac/context-portal)** - ⭐ 765
   Context Portal (ConPort): A memory bank MCP server building a project-specific knowledge graph to supercharge AI assistants. Enables powerful Retrieval Augmented Generation (RAG) for context-aware development in your IDE.

730. **[mcp](https://github.com/laravel/mcp)** - ⭐ 765
   Rapidly build MCP servers for your Laravel applications.

731. **[tapo](https://github.com/mihai-dinculescu/tapo)** - ⭐ 765
   🦀 Rust API, 🐍 Python API, and 🤖 MCP Server for TP-Link Tapo smart devices

732. **[next-devtools-mcp](https://github.com/vercel/next-devtools-mcp)** - ⭐ 765
   Next.js Development for Coding Agent

733. **[pentest-ai](https://github.com/0xSteph/pentest-ai)** - ⭐ 763
   Offensive-security MCP server with 205 wrapped tools, 17 specialist agents, and 60 SPA-aware probes for OWASP Top 10. CLI + MCP, BYO LLM. No API key needed on MCP path.

734. **[zennotes](https://github.com/ZenNotes/zennotes)** - ⭐ 762
   Keyboard-first local Markdown notes with Vim motions, diagrams, and MCP integration.

735. **[android-mcp-server](https://github.com/minhalvp/android-mcp-server)** - ⭐ 761
   An MCP server that provides control over Android devices via adb

736. **[cli](https://github.com/smithery-ai/cli)** - ⭐ 761
   Install, manage and develop MCP servers and skills for agents

737. **[clojure-mcp](https://github.com/bhauman/clojure-mcp)** - ⭐ 760
   Clojure MCP

738. **[Wax](https://github.com/christopherkarani/Wax)** - ⭐ 757
   Single-file memory layer for AI agents, sub mili-second RAG on Apple Silicon. Metal Optimized On-Device. No Server. No API. One File. Pure Swift

739. **[llm-functions](https://github.com/sigoden/llm-functions)** - ⭐ 756
   Easily create LLM tools and agents using plain Bash/JavaScript/Python functions.

740. **[AgentX](https://github.com/lucky-aeon/AgentX)** - ⭐ 755
   AgentX 致力于让小白也能无门槛通过自然语言打造属于自己的 Agent。AgentX 采用了自研 MCP 网关，模型高可用组件打造高可用

741. **[AgentChat](https://github.com/Shy2593666979/AgentChat)** - ⭐ 754
   AgentChat 是一个基于 LLM 的智能体交流平台，内置默认 Agent 并支持用户自定义 Agent。通过多轮对话和任务协作，Agent 可以理解并协助完成复杂任务。项目集成 LangChain、Function Call、MCP 协议、RAG、Memory、HITL、Skill、Milvus 和 ElasticSearch 等技术，实现高效的知识检索与工具调用，使用 FastAPI 构建高性能后端服务。

742. **[lisa.py](https://github.com/ant4g0nist/lisa.py)** - ⭐ 751
   LLDB MCP Integration + other helpful commands

743. **[openmcp-client](https://github.com/LSTM-Kirigaya/openmcp-client)** - ⭐ 748
   All in one vscode plugin for mcp developer

744. **[generative-ui](https://github.com/CopilotKit/generative-ui)** - ⭐ 747
   Generative UI examples for: AG-UI, A2UI/Open-JSON-UI, and MCP Apps.

745. **[cuga-agent](https://github.com/cuga-project/cuga-agent)** - ⭐ 744
   CUGA is an open-source generalist agent harness for the enterprise, supporting complex task execution on web and APIs, OpenAPI/MCP integrations, composable architecture, reasoning modes, and policy-aware features.

746. **[reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant)** - ⭐ 744
   MCP server for reverse engineering tasks in Ghidra 👩‍💻

747. **[yahoo-finance2](https://github.com/gadicc/yahoo-finance2)** - ⭐ 741
   Unofficial API for Yahoo Finance with CLI, MCP and Agent Skill

748. **[awesome-mcp-servers](https://github.com/TensorBlock/awesome-mcp-servers)** - ⭐ 738
   A comprehensive collection of Model Context Protocol (MCP) servers

749. **[lark-openapi-mcp](https://github.com/larksuite/lark-openapi-mcp)** - ⭐ 737
   飞书/Lark官方 OpenAPI MCP

750. **[mcp-client-for-ollama](https://github.com/jonigl/mcp-client-for-ollama)** - ⭐ 736
   Harness the power of local LLMs with this TUI MCP Client for Ollama. Featuring all core MCP primitives (tools, prompts, resources), agent mode, multi-server, model switching, streaming responses, human-in-the-loop, thinking mode, model params config, system prompts, and saved preferences.

751. **[just-prompt](https://github.com/disler/just-prompt)** - ⭐ 733
   just-prompt is an MCP server that provides a unified interface to top LLM providers (OpenAI, Anthropic, Google Gemini, Groq, DeepSeek, and Ollama)

752. **[ship-safe](https://github.com/asamassekou10/ship-safe)** - ⭐ 727
   CLI security scanner built for the agentic era. Detects CI/CD misconfigs, agent permission risks, MCP tool injection, hardcoded secrets, and DMCA-flagged AI dependencies.

753. **[MCP](https://github.com/jina-ai/MCP)** - ⭐ 726
   Official Jina AI Remote MCP Server

754. **[sentry-mcp](https://github.com/getsentry/sentry-mcp)** - ⭐ 725
   An MCP server for interacting with Sentry via LLMs.

755. **[anything-to-notebooklm](https://github.com/joeseesun/anything-to-notebooklm)** - ⭐ 724
   Claude Skill: Multi-source content processor for NotebookLM. Supports WeChat articles, web pages, YouTube, PDF, Markdown, search queries → Podcast/PPT/MindMap/Quiz etc.

756. **[HowToCook-mcp](https://github.com/worryzyy/HowToCook-mcp)** - ⭐ 724
   基于Anduin2017 / HowToCook （程序员在家做饭指南）的mcp server

757. **[mcp-server-docker](https://github.com/ckreiling/mcp-server-docker)** - ⭐ 723
   MCP server for Docker

758. **[codexia](https://github.com/milisp/codexia)** - ⭐ 723
   Agent Workstation for Codex CLI + Claude Code — with task scheduler, git worktree & remote control, skills management

759. **[mcpcan](https://github.com/Kymo-MCP/mcpcan)** - ⭐ 722
   MCPCAN is a centralized management platform for MCP services. It deploys each MCP service using a container deployment method. The platform supports container monitoring and MCP service token verification, solving security risks and enabling rapid deployment of MCP services. It uses SSE, STDIO, and STREAMABLEHTTP access protocols to deploy MCP。

760. **[hoop](https://github.com/hoophq/hoop)** - ⭐ 721
   One gateway in front of every protocol. Same policy across MCP, LLMs, databases and containers. Wire-level enforcement at under 5ms.

761. **[idea-reality-mcp](https://github.com/mnemox-ai/idea-reality-mcp)** - ⭐ 718
   Pre-build reality check for AI coding agents. Scans GitHub, HN, npm, PyPI, Product Hunt. MCP server. 290+ stars.

762. **[open-ptc-agent](https://github.com/Chen-zexi/open-ptc-agent)** - ⭐ 717
   An open source implementation of code execution with MCP (Programatic Tool Calling)

763. **[obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp)** - ⭐ 716
   A simple MCP server for Obsidian

764. **[passage-of-time-mcp](https://github.com/jlumbroso/passage-of-time-mcp)** - ⭐ 714
   🤖🕰️ An MCP server that gives language models temporal awareness and time calculation abilities. Teaching AI the significance of the passage of time through collaborative tool development.

765. **[stash](https://github.com/alash3al/stash)** - ⭐ 712
   Stash — persistent memory layer for AI agents. Episodes, facts, and working context stored in Postgres. MCP server included. Self-hosted, single binary, no cloud required.

766. **[pentest-agents](https://github.com/H-mmer/pentest-agents)** - ⭐ 712
   Bug bounty agent framework for Claude Code, Codex, Gemini, Cursor, Windsurf, Copilot, and OpenClaw — 48 agents, 26 commands, 19 CLI tools, 2 MCP servers, autonomous hunt loops, exploit chain builder.

767. **[MCP-Kali-Server](https://github.com/Wh0am123/MCP-Kali-Server)** - ⭐ 712
   MCP configuration to connect AI agent to a Linux machine.

768. **[axon](https://github.com/harshkedia177/axon)** - ⭐ 711
   Graph-powered code intelligence engine — indexes codebases into a knowledge graph, exposed via MCP tools for AI agents and a CLI for developers.

769. **[reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy)** - ⭐ 711
   Clean, LLM-optimized Reddit MCP server. Browse posts, search content, analyze users. No fluff, just Reddit data.

770. **[ai-trader](https://github.com/whchien/ai-trader)** - ⭐ 711
   Backtrader-powered backtesting framework for algorithmic trading, featuring 20+ strategies, multi-market support, CLI tools, and an integrated MCP server for professional traders.

771. **[pipelock](https://github.com/luckyPipewrench/pipelock)** - ⭐ 707
   Open-source AI agent firewall for MCP security and agent egress. Scans mediated HTTP, MCP, A2A, and WebSocket traffic for exfiltration, SSRF, and prompt injection, and emits mediator-signed action receipts: verifiable audit evidence from outside the agent.

772. **[MemoMind](https://github.com/24kchengYe/MemoMind)** - ⭐ 706
   Give your AI agent a brain that remembers. Local memory system for Claude Code — 100% private, GPU-accelerated, zero cloud dependency.

773. **[langgraph-mcp-agents](https://github.com/braincrew-lab/langgraph-mcp-agents)** - ⭐ 706
   LangGraph-powered ReAct agent with Model Context Protocol (MCP) integration. A Streamlit web interface for dynamically configuring, deploying, and interacting with AI agents capable of accessing various data sources and APIs through MCP tools.

774. **[UnrealClaude](https://github.com/Natfii/UnrealClaude)** - ⭐ 706
   Claude Code CLI integration for Unreal Engine 5.7 - Get AI coding assistance with built-in UE5.7 documentation context directly in the editor.

775. **[Unreal_mcp](https://github.com/ChiR24/Unreal_mcp)** - ⭐ 705
   A comprehensive Model Context Protocol (MCP) server that enables AI assistants to control Unreal Engine through the native C++ Automation Bridge plugin. Built with TypeScript and C++.

776. **[unbrowse](https://github.com/unbrowse-ai/unbrowse)** - ⭐ 704
   Unbrowse — api native browser MCP/SDK for any agent. Auto-discovers APIs from browser traffic, generates skills on the fly to call APIs directly 100x faster, 80% cheaper locally.

777. **[ktx-ai-data-agents-context](https://github.com/Kaelio/ktx-ai-data-agents-context)** - ⭐ 702
   ktx is an executable context layer for data and analytics agents 🐙 Allow Claude Code, Codex, and any AI agent to query data accurately through MCP with skills, memory and a semantic layer

778. **[awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security)** - ⭐ 701
   🔥🔒 Awesome MCP (Model Context Protocol) Security 🖥️

779. **[langgraph-mcp-agents](https://github.com/teddynote-lab/langgraph-mcp-agents)** - ⭐ 700
   LangGraph-powered ReAct agent with Model Context Protocol (MCP) integration. A Streamlit web interface for dynamically configuring, deploying, and interacting with AI agents capable of accessing various data sources and APIs through MCP tools.

780. **[mcp-proxy](https://github.com/tbxark/mcp-proxy)** - ⭐ 697
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single HTTP server.

781. **[codanna](https://github.com/bartolli/codanna)** - ⭐ 693
   Local code intelligence MCP server and CLI for AI coding agents

782. **[docsagent](https://github.com/docsagent/docsagent)** - ⭐ 693
   DocsAgent is a local-first AI documents assistant that lets you securely index and chat with thousands of desktop documents with zero cloud leakage.

783. **[openyak](https://github.com/openyak/openyak)** - ⭐ 692
   Open-source local-first AI agent for desktop work. No account, no telemetry: use local models with Ollama/Rapid-MLX or bring your own provider key.

784. **[WebMCP](https://github.com/jasonjmcghee/WebMCP)** - ⭐ 691
   Early WebMCP proposal / implementation - since evolved and worked on by much more capable folks that develop the web: https://github.com/webmachinelearning/webmcp

785. **[Feishu-MCP](https://github.com/cso1z/Feishu-MCP)** - ⭐ 689
    Feishu / Lark 飞书文档与任务管理工具，支持 MCP 服务器和 CLI + Skill 两种使用方式，可无缝集成 Cursor、Claude Code、Cline 等 AI 编码工具

786. **[agent-kit](https://github.com/KeyID-AI/agent-kit)** - ⭐ 689
   Give Claude/Cursor email powers. 27 MCP tools — inbox, send, reply, contacts, search. Free, no signup.

787. **[mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry)** - ⭐ 687
   Enterprise-ready MCP Gateway & Registry that centralizes AI development tools with secure OAuth authentication, dynamic tool discovery, and unified access for both autonomous AI agents and AI coding assistants. Transform scattered MCP server chaos into governed, auditable tool access with Keycloak/Entra integration.

788. **[mcp-gateway](https://github.com/microsoft/mcp-gateway)** - ⭐ 686
   MCP Gateway is a reverse proxy and management layer for MCP servers, enabling scalable, session-aware stateful routing and lifecycle management of MCP servers in Kubernetes environments.

789. **[stealth-browser-mcp](https://github.com/vibheksoni/stealth-browser-mcp)** - ⭐ 686
   The only browser automation that bypasses anti-bot systems. AI writes network hooks, clones UIs pixel-perfect via simple chat.

790. **[mcpc](https://github.com/apify/mcpc)** - ⭐ 683
   A universal CLI client for MCP. mcpc supports persistent sessions, stdio/HTTP, OAuth 2.1, tasks, JSON output for code mode, proxy for AI sandboxes, x402, and more.

791. **[mcp-obsidian](https://github.com/bitbonsai/mcp-obsidian)** - ⭐ 681
   A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access

792. **[mcp-client-cli](https://github.com/adhikasp/mcp-client-cli)** - ⭐ 677
   A simple CLI to run LLM prompt and implement MCP client.

793. **[mcp-mem0](https://github.com/coleam00/mcp-mem0)** - ⭐ 676
   MCP server for long term agent memory with Mem0. Also useful as a template to get you started building your own MCP server with Python!

794. **[laravel-restify](https://github.com/BinarCode/laravel-restify)** - ⭐ 675
   Laravel API for Ai Agents and humans.

795. **[FofaMap](https://github.com/asaotomo/FofaMap)** - ⭐ 673
   FofaMap v2.0 是一款基于 Python3 开发的全网首个 AI 驱动红队资产测绘智能体。在延续原有 FOFA 数据采集、存活检测、统计聚合、图标 Hash 及批量查询等核心功能的基础上，2.0 版本原生支持 MCP 协议，可无缝接入 Cursor、Claude 等 AI 平台。其核心内置了 AI 自我反思机制，能根据查询结果自动调优语法，并智能联动 Nuclei 推荐精准扫描策略，实现从“被动采集”到“主动智能决策”的红队作业进化。

796. **[colab-mcp](https://github.com/googlecolab/colab-mcp)** - ⭐ 673
   An MCP server for interacting with Google Colab

797. **[mcp-nixos](https://github.com/utensils/mcp-nixos)** - ⭐ 673
   MCP-NixOS - Model Context Protocol Server for NixOS resources

798. **[mineru-tianshu](https://github.com/magicyuan876/mineru-tianshu)** - ⭐ 672
   天枢 - 企业级 AI 一站式数据预处理平台 | PDF/Office转Markdown | 支持MCP协议AI助手集成 | Vue3+FastAPI全栈方案 | 文档解析 | 多模态信息提取

799. **[mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch)** - ⭐ 670

800. **[go-mcp](https://github.com/ThinkInAIXYZ/go-mcp)** - ⭐ 669
   Go-MCP is a powerful Go(Golang) version of the MCP SDK that implements the Model Context Protocol (MCP) to facilitate seamless communication between external systems and AI applications.

801. **[clihub](https://github.com/thellimist/clihub)** - ⭐ 666
   Turn any MCP server into CLI

802. **[RAGLight](https://github.com/Bessouat40/RAGLight)** - ⭐ 665
   RAGLight is a modular framework for Retrieval-Augmented Generation (RAG). It makes it easy to plug in different LLMs, embeddings, and vector stores, and now includes seamless MCP integration to connect external tools and data sources.

803. **[rhinomcp](https://github.com/jingcheng-chen/rhinomcp)** - ⭐ 665
   RhinoMCP connects Rhino 3D to AI Agent through the Model Context Protocol (MCP)

804. **[jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server)** - ⭐ 663
   MCP server for JADX-AI Plugin

805. **[wcgw](https://github.com/rusiaaman/wcgw)** - ⭐ 662
   Shell and coding agent on mcp clients

806. **[AnyTool](https://github.com/HKUDS/AnyTool)** - ⭐ 659
   "AnyTool: Universal Tool-Use Layer for AI Agents"

807. **[MCP-Nest](https://github.com/rekog-labs/MCP-Nest)** - ⭐ 659
   A NestJS module to effortlessly create Model Context Protocol (MCP) servers for exposing AI tools, resources, and prompts.

808. **[llm-search](https://github.com/snexus/llm-search)** - ⭐ 658
   Querying local documents, powered by LLM

809. **[Android-MCP](https://github.com/CursorTouch/Android-MCP)** - ⭐ 657
   MCP Server for interacting with Android Devices.

810. **[opencode-studio](https://github.com/Microck/opencode-studio)** - ⭐ 657
   web GUI for securely managing local OpenCode configuration

811. **[docling-mcp](https://github.com/docling-project/docling-mcp)** - ⭐ 655
   Making docling agentic through MCP

812. **[opentabs](https://github.com/opentabs-dev/opentabs)** - ⭐ 655
   Browser automation clicks buttons. OpenTabs calls APIs.

813. **[yacy_grid_mcp](https://github.com/yacy/yacy_grid_mcp)** - ⭐ 654
   The YaCy Grid Master Connect Program

814. **[vibe](https://github.com/mondaycom/vibe)** - ⭐ 653
   🎨 Vibe Design System - Official monday.com UI resources for application development in React.js

815. **[MetasploitMCP](https://github.com/GH05TCREW/MetasploitMCP)** - ⭐ 652
   MCP Server for Metasploit

816. **[cclsp](https://github.com/ktnyt/cclsp)** - ⭐ 652
   Claude Code LSP: enhance your Claude Code experience with non-IDE dependent LSP integration.

817. **[mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server)** - ⭐ 650
   Go server implementing Model Context Protocol (MCP) for filesystem operations.

818. **[zerobox](https://github.com/afshinm/zerobox)** - ⭐ 648
   Lightweight, cross-platform process sandboxing powered by OpenAI Codex's runtime. Sandbox any command with file, network, and credential controls.

819. **[flux-operator](https://github.com/controlplaneio-fluxcd/flux-operator)** - ⭐ 648
   GitOps on Autopilot Mode

820. **[a-share-mcp-is-just-i-need](https://github.com/24mlight/a-share-mcp-is-just-i-need)** - ⭐ 647

821. **[specification.website](https://github.com/jdevalk/specification.website)** - ⭐ 647
   Website specification — HTML, accessibility, security, SEO, agent-readiness. Platform-agnostic, sourced, MIT.

822. **[enrichmcp](https://github.com/featureform/enrichmcp)** - ⭐ 645
   EnrichMCP is a python framework for building data driven MCP servers

823. **[vmlx](https://github.com/jjang-ai/vmlx)** - ⭐ 644
   vMLX - JANGTQ Uber Compressed MLX Models - L2 Disk Cache (survives restart) + L1 Paged (super fast ttft) + Hybrid SSM Scheduler  + Cont Batching + etc!

824. **[python-utcp](https://github.com/universal-tool-calling-protocol/python-utcp)** - ⭐ 644
   Official python implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

825. **[claude-code-plugins-plus](https://github.com/jeremylongshore/claude-code-plugins-plus)** - ⭐ 641
   Claude Code Plugins Hub — browse and install 243 plugins (175 with Agent Skills v1.2.0). First 100% compliant with Anthropic 2025 Skills schema.

826. **[GhidrAssistMCP](https://github.com/symgraph/GhidrAssistMCP)** - ⭐ 641
   An native MCP server extension for Ghidra

827. **[workers-mcp](https://github.com/cloudflare/workers-mcp)** - ⭐ 640
   Talk to a Cloudflare Worker from Claude Desktop!

828. **[DeepSeek-Code-Whale](https://github.com/usewhale/DeepSeek-Code-Whale)** - ⭐ 639
   Whale — blazingly fast, terminal-first AI coding agent for DeepSeek. ~98% prompt cache hit rate, 1M context, MCP tools, dynamic workflows.

829. **[mcp-google-ads](https://github.com/cohnen/mcp-google-ads)** - ⭐ 636
   An MCP tool that connects Google Ads with Claude AI/Cursor and others, allowing you to analyze your advertising data through natural language conversations. This integration gives you access to campaign information, performance metrics, keyword analytics, and ad management—all through simple chat with Claude, Cursor or Windsurf.

830. **[rustunnel](https://github.com/joaoh82/rustunnel)** - ⭐ 634
   Self-hosted, secure tunnel server in Rust. Expose local HTTP/HTTPS/TCP/UDP services to the public internet via TLS-encrypted WebSocket. Open-source, pay-as-you-go managed option, MCP server for AI agents.

831. **[probe](https://github.com/probelabs/probe)** - ⭐ 634
   AI-friendly semantic code search engine for large codebases. Combines ripgrep speed with tree-sitter AST parsing. Powers AI coding assistants with precise, context-aware code understanding.

832. **[dexto](https://github.com/truffle-ai/dexto)** - ⭐ 631
   A coding agent and general agent harness for building and orchestrating agentic applications.

833. **[adb-mcp](https://github.com/mikechambers/adb-mcp)** - ⭐ 629

834. **[prism-insight](https://github.com/dragon1086/prism-insight)** - ⭐ 625
   AI-based stock analysis and trading system

835. **[aimock](https://github.com/CopilotKit/aimock)** - ⭐ 624
   Mock everything your AI app talks to — LLM APIs, MCP, A2A, AG-UI, vector DBs, search. One package, one port, zero dependencies.

836. **[mem-agent-mcp](https://github.com/firstbatchxyz/mem-agent-mcp)** - ⭐ 624
   mem-agent mcp server

837. **[notebooklm-mcp](https://github.com/jacob-bd/notebooklm-mcp)** - ⭐ 624

838. **[mcp-proxy](https://github.com/TBXark/mcp-proxy)** - ⭐ 624
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single HTTP server.

839. **[google-ads-mcp](https://github.com/googleads/google-ads-mcp)** - ⭐ 623

840. **[garmin_mcp](https://github.com/Taxuspt/garmin_mcp)** - ⭐ 622
   MCP server to access Garmin data

841. **[MindOS](https://github.com/GeminiLight/MindOS)** - ⭐ 621
   MindOS is a Human-AI Collaborative Mind System, where human thinks and agents act. Globally sync your mind for all agents: transparent, controllable, and evolving symbiotically.

842. **[tome](https://github.com/runebookai/tome)** - ⭐ 621
   a magical LLM desktop client that makes it easy for *anyone* to use LLMs and MCP

843. **[apple-doc-mcp](https://github.com/MightyDillah/apple-doc-mcp)** - ⭐ 620
   MCP server providing seamless access to Apple Developer Documentation with smart search and wildcard support

844. **[phpMyFAQ](https://github.com/thorsten/phpMyFAQ)** - ⭐ 619
   phpMyFAQ - Open Source FAQ web application for PHP 8.3+ and MySQL, PostgreSQL and other databases

845. **[scarf](https://github.com/awizemann/scarf)** - ⭐ 618
   Native macOS and iOS App for the Hermes AI agent — multi-window, multi-server (local + remote over SSH). Chat, dashboard, sessions, memory, cron, MCP, and more.

846. **[OpenOSINT](https://github.com/OpenOSINT/OpenOSINT)** - ⭐ 618
   AI-powered OSINT agent with interactive REPL, MCP server, and CLI. 16 tools. Works with Claude, GPT-4, or local models. For authorized security research only.

847. **[Overture](https://github.com/SixHq/Overture)** - ⭐ 618
   Overture is an open-source, locally running web interface delivered as an MCP (Model Context Protocol) server that visually maps out the execution plan of any AI coding agent as an interactive flowchart/graph before the agent begins writing code.

848. **[claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** - ⭐ 617
   A Model Context Protocol (MCP) that allows Claude Desktop and other AI tools (Claude Code, Cursor, Antigravity, etc.) to read, analyze, and modify Figma designs

849. **[LLMTornado](https://github.com/lofcz/LLMTornado)** - ⭐ 617
   The .NET library to build AI agents with 30+ built-in connectors.

850. **[codeg](https://github.com/xintaofei/codeg)** - ⭐ 617
   A unified workspace for local AI coding agents (Claude Code, Codex, Gemini CLI, etc.) — desktop app, standalone server, or Docker. Conversation aggregation, git worktree workflows, MCP/Skills management, chat channel integration (Telegram, Lark, iLink), and integrated terminal, all accessible from any browser.

851. **[cloud-run-mcp](https://github.com/GoogleCloudPlatform/cloud-run-mcp)** - ⭐ 615
   MCP server to deploy apps to Cloud Run

852. **[awesome-a2a](https://github.com/ai-boost/awesome-a2a)** - ⭐ 614
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place.

853. **[Get-Started-with-Web3](https://github.com/beihaili/Get-Started-with-Web3)** - ⭐ 614
   Open-source bilingual AI-native Web3 curriculum: wallets, Bitcoin, Ethereum, DeFi, L2, DAO, smart accounts, llms.txt and MCP

854. **[cnki-skills](https://github.com/cookjohn/cnki-skills)** - ⭐ 614
   CNKI (中国知网) skills for Claude Code — search, browse journals, download PDFs, export to Zotero via Chrome DevTools MCP

855. **[storybloq](https://github.com/Storybloq/storybloq)** - ⭐ 612
   Cross-session context for Claude Code. CLI + MCP server + /story skill that tracks tickets, issues, handovers, and roadmap in a .story/ directory.

856. **[minecraft-mcp-server](https://github.com/yuniko-software/minecraft-mcp-server)** - ⭐ 611
   A Minecraft MCP Server powered by Mineflayer API. It allows to control a Minecraft character in real-time, allowing AI assistants to build structures, explore the world, and interact with the game environment through natural language instruction

857. **[mcp-link](https://github.com/automation-ai-labs/mcp-link)** - ⭐ 610
   Convert Any OpenAPI V3 API to MCP Server

858. **[mcp-handler](https://github.com/vercel/mcp-handler)** - ⭐ 610
   Easily spin up an MCP Server on Next.js, Nuxt, Svelte, and more

859. **[awesome-web3-mcp-servers](https://github.com/demcp/awesome-web3-mcp-servers)** - ⭐ 609
   DeMCP is the first Decentralized MCP network, offering SSE proxies for MCP services and mainstream LLMs, tackling trust and security with TEE and blockchain.

860. **[ktx-ai-data-agents-mcp-context-skills](https://github.com/Kaelio/ktx-ai-data-agents-mcp-context-skills)** - ⭐ 609
   ktx is an executable context layer for data and analytics agents 🐙 Allow Claude Code, Codex, and any AI agent to query data accurately through MCP with skills, memory and a semantic layer

861. **[mcp-server-neon](https://github.com/neondatabase/mcp-server-neon)** - ⭐ 609
   MCP server for interacting with Neon Management API and databases

862. **[vault](https://github.com/vaultmcp/vault)** - ⭐ 609
   MCP prompt-injection scanning proxy — runtime security for MCP tool responses

863. **[appproxy](https://github.com/ys1231/appproxy)** - ⭐ 609
   基于flutter的Android vpn代理工具支持mcp调用， Android VPN Proxy Tool Based on Flutter

864. **[blueprint-mcp](https://github.com/ArcadeAI/blueprint-mcp)** - ⭐ 608
   Diagram generation for understanding codebases and system architecture using Nano Banana Pro.

865. **[daydreams](https://github.com/daydreamsai/daydreams)** - ⭐ 608
   Daydreams is a set of tools for building agents for commerce

866. **[mda](https://github.com/sno-ai/mda)** - ⭐ 607
   MDA Open Spec — a Markdown superset for agent-facing documents. One .mda source compiles to drop-in SKILL.md, AGENTS.md, MCP-SERVER.md, and CLAUDE.md. JSON Schema validated, with typed dependency graph, footnote relationships, and Sigstore-anchored signatures. For agentskills.io and AAIF runtimes.

867. **[google-search](https://github.com/web-agent-master/google-search)** - ⭐ 604
   A Playwright-based Node.js tool that bypasses search engine anti-scraping mechanisms to execute Google searches. Local alternative to SERP APIs with MCP server integration.

868. **[Burrow](https://github.com/caezium/Burrow)** - ⭐ 603
   A free, open-source, native macOS GUI for the Mole CLI (mo): clean, uninstall, optimize, analyze disk, and watch live status. Plus long-range history + an MCP server for AI agents.

869. **[UnrealGenAISupport](https://github.com/prajwalshettydev/UnrealGenAISupport)** - ⭐ 603
   Unreal Engine plugin for LLM/GenAI models & MCP UE5 server. OpenAI GPT-5, Deepseek R1, Claude Opus/Sonnet, Gemini 3, Grok 4, Alibaba Qwen, Kimi, ElevenLabs TTS, Inworld, OpenRouter, Groq, GLM, Ollama, Local, Meshy, Tripo, Hunyuan3D, Rodin, fal, Dashscope, Seedream. NPC AI, agentic, chat, 3D gen, TTS, multimodal, image gen. UnrealMCP/UnrealClaude

870. **[spotify-mcp](https://github.com/varunneal/spotify-mcp)** - ⭐ 603
   MCP to connect your LLM with Spotify.

871. **[openapi-mcp-generator](https://github.com/harsha-iiiv/openapi-mcp-generator)** - ⭐ 601
   A tool that converts OpenAPI specifications to MCP server

872. **[manim-mcp-server](https://github.com/abhiemj/manim-mcp-server)** - ⭐ 600

873. **[tsidp](https://github.com/tailscale/tsidp)** - ⭐ 599
   A simple OIDC / OAuth Identity Provider (IdP) server for your tailnet.

874. **[evo-ai](https://github.com/evolution-foundation/evo-ai)** - ⭐ 598
   Evo AI is an open-source platform for creating and managing AI agents, enabling integration with different AI models and services.

875. **[FinanceMCP](https://github.com/guangxiangdebizi/FinanceMCP)** - ⭐ 598
   这是一个金融领域相关的mcp,本项目通过集成 Tushare API 和 Binance API 为语言模型（如Claude）提供全面的实时金融数据访问能力，支持股票、基金、债券、宏观经济指标、稳定币、虚拟货币等多维度金融数据分析。其中也包含了金融数据查询、财经新闻查询、国家统计局数据查询等

876. **[line-bot-mcp-server](https://github.com/line/line-bot-mcp-server)** - ⭐ 598
   MCP server that integrates the LINE Messaging API to connect an AI Agent to the LINE Official Account.

877. **[medusa](https://github.com/Pantheon-Security/medusa)** - ⭐ 597
   AI-first security scanner with 79 analyzers, 40,000+ detection rules, and repo poisoning detection for AI/ML, LLM agents, and MCP servers. Scan any GitHub repo with: medusa scan --git user/repo

878. **[borsa-mcp](https://github.com/saidsurucu/borsa-mcp)** - ⭐ 596
   MCP Server for Turkish & American Stock Exchange and Fund Data

879. **[FantasyPremierLeague](https://github.com/joreilly/FantasyPremierLeague)** - ⭐ 595
   Fantasy Premier League Kotlin/Compose Multiplatform sample

880. **[rails_ai_agents](https://github.com/ThibautBaissac/rails_ai_agents)** - ⭐ 594
   Specialized AI skills, agents, rules and hooks for modern Rails AI driven-development + Spec-Driven-Development kit + MCP

881. **[bm.md](https://github.com/miantiao-me/bm.md)** - ⭐ 589
   更好用的 Markdown 排版助手｜一键适配微信公众号、网页与图片。

882. **[MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe)** - ⭐ 589
   MCP-Universe is a comprehensive framework designed for RL training, benchmarking, and developing AI agents for general tool-use.

883. **[evo-ai](https://github.com/EvolutionAPI/evo-ai)** - ⭐ 588
   Evo AI is an open-source platform for creating and managing AI agents, enabling integration with different AI models and services.

884. **[maverick-mcp](https://github.com/wshobson/maverick-mcp)** - ⭐ 588
   MaverickMCP - Personal Stock Analysis MCP Server

885. **[UnrealMCP](https://github.com/kvick-games/UnrealMCP)** - ⭐ 587
   MCP to allow AI agents to control Unreal

886. **[OpenContext](https://github.com/0xranx/OpenContext)** - ⭐ 586
   A personal context store for AI agents and assistants—reuse your existing coding agent CLI (Codex/Claude/OpenCode) with built‑in Skills/tools and a desktop GUI to capture, search, and reuse project knowledge across agents and repos.

887. **[heym](https://github.com/heymrun/heym)** - ⭐ 586
   Build AI workflows by prompt or visual canvas. Heym is source-available and self-hosted, with agents, RAG, MCP, HITL, observability, evals, token cost tracking and more.

888. **[MimikaStudio](https://github.com/BoltzmannEntropy/MimikaStudio)** - ⭐ 585
   MimikaStudio - A local-first application for macOS (Apple Silicon) + Agentic MCP Support

889. **[FLUJO](https://github.com/mario-andreschak/FLUJO)** - ⭐ 585
   MCP-Hub and -Inspector, Multi-Model Workflow and Chat Interface

890. **[skill-creator](https://github.com/sandiiarov/skill-creator)** - ⭐ 585
   Turn any MCP server, OpenAPI spec, or GraphQL endpoint into a CLI at runtime.

891. **[echokit_server](https://github.com/second-state/echokit_server)** - ⭐ 585
   Open Source Voice Agent Platform

892. **[obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server)** - ⭐ 584
   MCP server for Obsidian vaults — read, write, search, and surgically edit notes, tags, and frontmatter via the Local REST API plugin. STDIO or Streamable HTTP.

893. **[langgraph-mcp](https://github.com/esxr/langgraph-mcp)** - ⭐ 583
   LangGraph solution template for MCP

894. **[claude-codex-settings](https://github.com/fcakyon/claude-codex-settings)** - ⭐ 583
   My personal Claude Code and OpenAI Codex setup with battle-tested skills, commands, hooks, agents and MCP servers that I use daily.

895. **[MinerU-Document-Explorer](https://github.com/opendatalab/MinerU-Document-Explorer)** - ⭐ 583
   Agent-native knowledge engine with MCP tools for document indexing, wiki organization, fast retrieval and deep reading across PDF/DOCX/PPTX/Markdown

896. **[mcp-sequentialthinking-tools](https://github.com/spences10/mcp-sequentialthinking-tools)** - ⭐ 583
   🧠 An adaptation of the MCP Sequential Thinking Server to guide tool usage. This server provides recommendations for which MCP tools would be most effective at each stage.

897. **[mcp-mermaid](https://github.com/hustcc/mcp-mermaid)** - ⭐ 580
   ❤️ Generate mermaid diagram and chart with AI MCP dynamically.

898. **[mcp-pointer](https://github.com/etsd-tech/mcp-pointer)** - ⭐ 579
   MCP tool: let you point at DOM elements for your favorite agentic coding tool. Let AI see what you see.

899. **[dbt-mcp](https://github.com/dbt-labs/dbt-mcp)** - ⭐ 578
   A MCP (Model Context Protocol) server for interacting with dbt.

900. **[x64DbgMCPServer](https://github.com/AgentSmithers/x64DbgMCPServer)** - ⭐ 576
   x64DbgMCPServer made from c# with Claude, Windsurf and Cursor support

901. **[Godot-MCP](https://github.com/ee0pdt/Godot-MCP)** - ⭐ 576
   An MCP for Godot that lets you create and edit games in the Godot game engine with tools like Claude

902. **[mateclaw](https://github.com/matevip/mateclaw)** - ⭐ 576
   🤖 MateClaw — Your second brain with Multi-Agent Orchestration, MCP Protocol, Skills & Memory, Dream, and Multi-Channel Support. Built on Spring AI Alibaba.

903. **[swarmclaw](https://github.com/swarmclawai/swarmclaw)** - ⭐ 576
   Open-source self-hosted AI agent runtime and multi-agent framework for autonomous agent swarms. Agent memory, MCP tools, schedules, delegation, and 23+ LLM providers (Claude, GPT, Gemini, OpenRouter, Ollama). A practical Claude Code and LangChain alternative.

904. **[home-assistant-vibecode-agent](https://github.com/Coolver/home-assistant-vibecode-agent)** - ⭐ 575
   Home Assistant MCP server agent. Enable Claude Code, Cursor, VS Code or any MCP-enabled IDE to help you vibe-code and manage Home Assistant: create and debug automations, design dashboards, tweak themes, modify configs, and deploy changes using natural language

905. **[mcp.el](https://github.com/lizqwerscott/mcp.el)** - ⭐ 575
   An Mcp client inside Emacs

906. **[homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp)** - ⭐ 575
   A MCP server for Home Assistant

907. **[mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub)** - ⭐ 574
   A growing collection of MCP servers bringing offensive security tools to AI assistants. Nmap, Ghidra, Nuclei, SQLMap, Hashcat and more.

908. **[OpenSail](https://github.com/TesslateAI/OpenSail)** - ⭐ 573
   OpenSail is the open-source alternative to Codex App, Claude Desktop, Cursor, and Cowork for agentic software work.

909. **[kraken-cli](https://github.com/krakenfx/kraken-cli)** - ⭐ 571
   The first AI-native CLI for trading crypto, stocks, forex, and derivatives.

910. **[sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)** - ⭐ 571
   Official SonarQube MCP Server for code quality and security in AI agents

911. **[google-docs-mcp](https://github.com/a-bonus/google-docs-mcp)** - ⭐ 570
   The Ultimate Google Docs, Sheets, Drive, Gmail, & Google Calendar MCP Server. This MCP (primarily for use in Claude Desktop) gains full access to your google suite and lets claude do its thing.

912. **[bernstein](https://github.com/sipyourdrink-ltd/bernstein)** - ⭐ 569
   Audit-grade multi-agent orchestration for CLI coding agents (Claude Code, Codex, Gemini CLI, +40 more). HMAC-chained audit log, signed agent cards, per-artefact lineage, air-gap deploy. The orchestrator your compliance team will sign off on. https://bernstein.run

913. **[vite-plugin-vue-mcp](https://github.com/webfansplz/vite-plugin-vue-mcp)** - ⭐ 567
   Vite plugin that enables a MCP server helping models to understand your Vue app better.

914. **[open-harness](https://github.com/MaxGfeller/open-harness)** - ⭐ 566
   A code-first, composable SDK to build powerful AI agents

915. **[multimodal-agents-course](https://github.com/the-ai-merge/multimodal-agents-course)** - ⭐ 565
   An MCP Multimodal AI Agent with eyes and ears!

916. **[ChatbotX](https://github.com/ChatbotXIO/ChatbotX)** - ⭐ 564
   All-in-one chat marketing platform for agentic workflows via APIs, CLI, and MCP. An open-source alternative to ManyChat, Chatfuel, and Wati 🤖

917. **[Box](https://github.com/jegly/Box)** - ⭐ 562
   Private on-device AI suite for Android. Fork of Google AI Edge Gallery with llama.cpp, whisper.cpp, stable-diffusion.cpp, GGUF import, voice chat, vision AI, on-device image generation, biometric lock, encrypted history, and CPU/NPU/GPU acceleration.

918. **[chroma-mcp](https://github.com/chroma-core/chroma-mcp)** - ⭐ 560
   A Model Context Protocol (MCP) server implementation that provides database capabilities for Chroma

919. **[rails-mcp-server](https://github.com/maquina-app/rails-mcp-server)** - ⭐ 560
   A Ruby gem implementation of a Model Context Protocol (MCP) server for Rails projects. This server allows LLMs (Large Language Models) to interact with Rails projects through the Model Context Protocol.

920. **[ssh-mcp-server](https://github.com/classfang/ssh-mcp-server)** - ⭐ 559
   基于 SSH 的 MCP 服务 🧙‍♀️。已被MCP官方收录 🎉。 SSH MCP Server 🧙‍♀️. It has been included in the community MCP repository 🎉.

921. **[iterm-mcp](https://github.com/ferrislucas/iterm-mcp)** - ⭐ 559
   A Model Context Protocol server that executes commands in the current iTerm session - useful for REPL and CLI assistance

922. **[mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript)** - ⭐ 559
   This is an MCP server that allows you to directly download transcripts of YouTube videos.

923. **[human-skill-tree](https://github.com/24kchengYe/human-skill-tree)** - ⭐ 557
   🌳 AI-Powered Skill Tree for Lifelong Human Learning. 30+ skills from K-12 to career & social intelligence, built on cognitive science. | 人类养成记：AI 驱动的终身学习技能树

924. **[polymarket-mcp-server](https://github.com/caiovicentino/polymarket-mcp-server)** - ⭐ 557
   🤖 AI-Powered MCP Server for Polymarket - Enable Claude to trade prediction markets with 45 tools, real-time monitoring, and enterprise-grade safety features

925. **[mcp-server-weread](https://github.com/freestylefly/mcp-server-weread)** - ⭐ 556
   微信读书MCP

926. **[mcp-shield](https://github.com/riseandignite/mcp-shield)** - ⭐ 556
   Security scanner for MCP servers

927. **[casbin-gateway](https://github.com/casbin/casbin-gateway)** - ⭐ 555
   Casbin AI & MCP security gateway for HTTP, online demo: https://door.caswaf.com

928. **[caswaf](https://github.com/casbin/caswaf)** - ⭐ 555
   Casbin AI & MCP security gateway for HTTP, online demo: https://door.caswaf.com

929. **[awesome-ai-tools-for-ui](https://github.com/maxbogo/awesome-ai-tools-for-ui)** - ⭐ 554
   Curated list of awesome AI tools to build beautiful UI/UX.

930. **[mcp-pandoc](https://github.com/vivekVells/mcp-pandoc)** - ⭐ 554
   MCP server for document format conversion using pandoc.

931. **[llm-mcp-rag](https://github.com/KelvinQiu802/llm-mcp-rag)** - ⭐ 551
   LLM + MCP + RAG = Magic

932. **[Mantic.sh](https://github.com/marcoaapfortes/Mantic.sh)** - ⭐ 550
   A structural code search engine for Al agents.

933. **[vestige](https://github.com/samvallad33/vestige)** - ⭐ 550
   Cognitive memory for AI agents — FSRS-6 spaced repetition, 29 brain modules, 3D dashboard, single 22MB Rust binary. MCP server for Claude, Cursor, VS Code, Xcode, JetBrains.

934. **[auto-browser](https://github.com/LvcidPsyche/auto-browser)** - ⭐ 548
   Give your AI agent a real browser — with a human in the loop. Open-source MCP-native browser agent.

935. **[apple-health-mcp](https://github.com/neiltron/apple-health-mcp)** - ⭐ 547
   MCP server for querying Apple Health data with natural language and SQL

936. **[fastapi-mcp-langgraph-template](https://github.com/NicholasGoh/fastapi-mcp-langgraph-template)** - ⭐ 547
   A modern template for agentic orchestration — built for rapid iteration and scalable deployment using highly customizable, community-supported tools like MCP, LangGraph, and more.

937. **[ida-mcp-rs](https://github.com/blacktop/ida-mcp-rs)** - ⭐ 545
   Headless IDA Pro MCP Server

938. **[tda](https://github.com/irockel/tda)** - ⭐ 543
   TDA - Thread Dump Analyzer (for Java). Analyze your Thread Dumps with a GUI or use it as MCP Server.

939. **[mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)** - ⭐ 542

940. **[swarmvault](https://github.com/swarmclawai/swarmvault)** - ⭐ 541
   The local-first LLM Wiki: open-source knowledge graph builder, RAG knowledge base, and agent memory store. Built on Andrej Karpathy's pattern. An Obsidian alternative for personal knowledge management, AI second brain, and durable Claude Code / Codex / OpenClaw memory.

941. **[pg-mcp-server](https://github.com/stuzero/pg-mcp-server)** - ⭐ 539

942. **[haiku.rag](https://github.com/ggozad/haiku.rag)** - ⭐ 538
   Opinionated agentic RAG powered by LanceDB, Pydantic AI, and Docling

943. **[mcp](https://github.com/cloudflare/mcp)** - ⭐ 536
   MCP server for the Cloudflare API

944. **[ethora](https://github.com/dappros/ethora)** - ⭐ 536
   SDK monorepo for Ethora chat / messaging platform. (1) Pick an SDK for your frontend stack. (2) Integrate manually or using ethora-setup. (3) Optionally configure app settings, deploy AI agents etc. Server: ethora.com cloud [free]. Dedicated server + SLA option for enterprise customers.

945. **[travel-hacking-toolkit](https://github.com/borski/travel-hacking-toolkit)** - ⭐ 535
   AI-powered travel hacking and search with cash, points, miles, and award flights. Drop-in skills and MCP servers for Claude, Codex, and OpenCode.

946. **[godot-ai](https://github.com/hi-godot/godot-ai)** - ⭐ 535
   Production-grade MCP server and AI tools for the Godot engine. A Snap to install. Totally free and fun.

947. **[awesome-copilot-agents](https://github.com/Code-and-Sorts/awesome-copilot-agents)** - ⭐ 534
   ✨ A curated list of awesome GitHub instructions, prompt, skills, MCPs and agent markdown files for enhancing your GitHub Copilot AI experience.

948. **[concierge](https://github.com/concierge-hq/concierge)** - ⭐ 534
   🚀 Universal SDK for building next-gen MCP servers

949. **[work-iq-mcp](https://github.com/microsoft/work-iq-mcp)** - ⭐ 534
   MCP Server and CLI for accessing Work IQ

950. **[dolphin-mcp](https://github.com/QuixiAI/dolphin-mcp)** - ⭐ 534

951. **[ScienceClaw](https://github.com/AgentTeam-TaichuAI/ScienceClaw)** - ⭐ 533
   ScienceClaw is a personal research assistant built with LangChain DeepAgents and AIO Sandbox infrastructure, adopting a completely new architecture beyond OpenClaw. It offers stronger security, better transparency, and a more user-friendly experience.

952. **[pgmcp](https://github.com/subnetmarco/pgmcp)** - ⭐ 533
   An MCP server to query any Postgres database in natural language.

953. **[butterbase-skills](https://github.com/butterbase-ai/butterbase-skills)** - ⭐ 532
   Plugin for Butterbase.ai

954. **[gateway](https://github.com/centralmind/gateway)** - ⭐ 531
   Universal MCP-Server for your Databases optimized for LLMs and AI-Agents.

955. **[youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server)** - ⭐ 531
   MCP Server for YouTube API, enabling video management, Shorts creation, and advanced analytics

956. **[LLM-Agents-Ecosystem-Handbook](https://github.com/oxbshw/LLM-Agents-Ecosystem-Handbook)** - ⭐ 529
   One-stop handbook for building, deploying, and understanding LLM agents with 60+ skeletons, tutorials, ecosystem guides, and evaluation tools.

957. **[mcp-redis](https://github.com/redis/mcp-redis)** - ⭐ 529
   The official Redis MCP Server is a natural language interface designed for agentic applications to manage and search data in Redis efficiently

958. **[mcp-youtube](https://github.com/anaisbetts/mcp-youtube)** - ⭐ 528
   A Model-Context Protocol Server for YouTube

959. **[joinly](https://github.com/joinly-ai/joinly)** - ⭐ 526
   Make your meetings accessible to AI Agents

960. **[resend-mcp](https://github.com/resend/resend-mcp)** - ⭐ 526
   The official MCP server to send emails and interact with Resend

961. **[claude-code-mastery](https://github.com/TheDecipherist/claude-code-mastery)** - ⭐ 524
   The complete guide to Claude Code: CLAUDE.md, hooks, skills, MCP servers, and commands

962. **[biomcp](https://github.com/genomoncology/biomcp)** - ⭐ 523
   BioMCP: Biomedical Model Context Protocol

963. **[talk-to-girlfriend-ai](https://github.com/arlanrakh/talk-to-girlfriend-ai)** - ⭐ 522
   im busy building ai agents so why not let an ai talk to my girlfriend? (i am single)

964. **[n8n-workflow-builder](https://github.com/makafeli/n8n-workflow-builder)** - ⭐ 521
   AI assistant integration for n8n workflow automation through Model Context Protocol (MCP). Connect Claude Desktop, ChatGPT, and other AI assistants to n8n for natural language workflow management.

965. **[UnityMCP](https://github.com/jackwrichards/UnityMCP)** - ⭐ 519

966. **[ghostcrew](https://github.com/GH05TCREW/ghostcrew)** - ⭐ 515
   GhostCrew is an AI agent framework for bug bounty hunting, red-team operations, pentesting, and operator education. It integrates LLM autonomy, multi-agent coordination, and MCP extensibility with a minimal core toolset, supported by RAG for context-aware reasoning, a persistent internal state, reproducible workflows, and interactive assistance.

967. **[MCPSpy](https://github.com/alex-ilgayev/MCPSpy)** - ⭐ 514
   MCP Monitoring with eBPF

968. **[memorix](https://github.com/AVIDS2/memorix)** - ⭐ 514
   Open-source cross-agent memory layer for coding agents via MCP. Compatible with Cursor, Claude Code, Codex, Windsurf, Gemini CLI, GitHub Copilot, Kiro, OpenCode, Antigravity, and Trae.

969. **[desktop](https://github.com/openyak/desktop)** - ⭐ 513
   Yak is all you need

970. **[mcp-get](https://github.com/michaellatman/mcp-get)** - ⭐ 511

971. **[claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you)** - ⭐ 510
   Enable any LLM (e.g. Claude) to interactively debug any language for you via MCP and a VS Code Extension

972. **[GhidrAssistMCP](https://github.com/jtang613/GhidrAssistMCP)** - ⭐ 510
   An MCP extension for Ghidra

973. **[sigmap](https://github.com/manojmallick/sigmap)** - ⭐ 510
   97% token reduction for AI coding sessions — zero deps, 31 languages, MCP server

974. **[mcp-server-bash-sdk](https://github.com/muthuishere/mcp-server-bash-sdk)** - ⭐ 509
   Yes Mcp server in bash

975. **[multimodal-agents-course](https://github.com/multi-modal-ai/multimodal-agents-course)** - ⭐ 507
   An MCP Multimodal AI Agent with eyes and ears!

976. **[todoist-mcp](https://github.com/Doist/todoist-mcp)** - ⭐ 506
   A set of tools to connect to AI agents, to allow them to use Todoist on a user's behalf. Includes MCP support.

977. **[yutu](https://github.com/eat-pray-ai/yutu)** - ⭐ 504
   The AI-powered toolkit that grows your YouTube channel on autopilot.

978. **[ios-mcp](https://github.com/witchan/ios-mcp)** - ⭐ 504
   iOS MCP: MCP management tool for jailbroken iPhones, enabling developers and AI agents to inspect and control devices.

979. **[mcp-registry](https://github.com/docker/mcp-registry)** - ⭐ 503
   Official Docker MCP registry

980. **[WireMCP](https://github.com/0xKoda/WireMCP)** - ⭐ 502
   An MCP for WireShark (tshark). Empower LLM's with realtime network traffic analysis capability

981. **[open-multi-agent-canvas](https://github.com/CopilotKit/open-multi-agent-canvas)** - ⭐ 502
   The open-source multi-agent chat interface that lets you manage multiple agents in one dynamic conversation and add MCP servers for deep research

982. **[metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server)** - ⭐ 501
   Model Context Protocol (MCP) to enable AI LLMs to trade using MetaTrader platform

983. **[claw-orchestrator](https://github.com/Enderfga/claw-orchestrator)** - ⭐ 500
   Run Claude Code, Codex, Gemini, Cursor Agent and custom coding CLIs as one unified runtime for claw-style agent systems. Runs standalone, with first-class OpenClaw plugin support.

984. **[mcp-security](https://github.com/google/mcp-security)** - ⭐ 498

985. **[things-mcp](https://github.com/hald/things-mcp)** - ⭐ 498
   Things.app MCP Server

986. **[ironcurtain](https://github.com/provos/ironcurtain)** - ⭐ 498
   A secure* runtime for autonomous AI agents. Policy from plain-English constitutions. (*https://ironcurtain.dev)

987. **[ssh-mcp](https://github.com/tufantunc/ssh-mcp)** - ⭐ 498
   MCP server exposing SSH control for Linux servers via Model Context Protocol.

988. **[web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)** - ⭐ 497
   🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support

989. **[copilot-mcp](https://github.com/VikashLoomba/copilot-mcp)** - ⭐ 494
   A VSCode extension that lets you find and install Agent Skills and MCP Apps to use with GitHub Copilot, Claude Code, and Codex CLI.

990. **[PentestAgent](https://github.com/GH05TCREW/PentestAgent)** - ⭐ 493
   All-in-one offensive security toolbox with AI agent and MCP architecture. Integrates tools like Nmap, Metasploit, FFUF, SQLMap. Enables pentesting, bug bounty hunting, threat hunting, and reporting. RAG-based responses with local knowledge base support.

991. **[mcp-hub](https://github.com/ravitemer/mcp-hub)** - ⭐ 493
   A centralized manager for Model Context Protocol (MCP) servers with dynamic server management and monitoring

992. **[UnityMCP](https://github.com/Arodoid/UnityMCP)** - ⭐ 491

993. **[mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd)** - ⭐ 490
   An implementation of Model Context Protocol (MCP) server for Argo CD.

994. **[yupi-hot-monitor](https://github.com/liyupi/yupi-hot-monitor)** - ⭐ 490
   2026 年编程导航 AI 编程实战新项目，基于 Node.js + Express + React + OpenRouter 的 AI 热点监控工具，支持多信息源聚合抓取（Twitter / Bing / HackerNews / B 站等 7+ 平台）、AI 查询扩展、AI 真假识别与相关性分析、WebSocket 实时推送、邮件通知、多维度筛选排序，并将热点监控能力封装为 Agent Skills 技能包。覆盖 Prisma + SQLite 数据库、Socket.io 实时通信、Axios + Cheerio 网页爬虫、OpenRouter 大模型接入、Aceternity UI 炫酷前端、node-cron 定时任务、VSCode Copilot Vibe Coding + MCP

995. **[CoexistAI](https://github.com/SPThole/CoexistAI)** - ⭐ 490
   CoexistAI is a modular, developer-friendly research assistant framework . It enables you to build, search, summarize, and automate research workflows using LLMs, web search, Reddit, YouTube, and mapping tools—all with simple MCP tool calls or API calls or Python functions.

996. **[docfork](https://github.com/docfork/docfork)** - ⭐ 489
   Docfork - Up-to-date docs for AI Coding Agents.

997. **[mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck)** - ⭐ 489
   Local MCP server for DuckDB and MotherDuck

998. **[vibe-check-mcp-server](https://github.com/PV-Bhat/vibe-check-mcp-server)** - ⭐ 489
   Vibe Check is a tool that provides mentor-like feedback to AI Agents, preventing tunnel-vision, over-engineering and reasoning lock-in for complex and long-horizon agent workflows. KISS your over-eager AI Agents goodbye! Effective for: Coding, Ambiguous Tasks, High-Risk tasks

999. **[claude-code-skills](https://github.com/levnikolaevich/claude-code-skills)** - ⭐ 488
   Plugin suite + bundled MCP servers for Claude Code. Full delivery lifecycle: Agile pipeline with multi-model AI review, project bootstrap, documentation generation, codebase audits, performance optimization, community workflows. Includes hex-line (hash-verified editing), hex-graph (code knowledge graph), and hex-ssh (remote SSH) MCP servers.

1000. **[mcp-remote-macos-use](https://github.com/baryhuang/mcp-remote-macos-use)** - ⭐ 487
   The only general AI agent that does NOT requires extra API key, giving you full control on your local and remote MacOs from Claude Desktop App

1001. **[codex-mcp-server](https://github.com/tuannvm/codex-mcp-server)** - ⭐ 487
   MCP server wrapper for OpenAI Codex CLI that enables Claude Code to leverage Codex's AI capabilities directly.

1002. **[agents](https://github.com/unifapi-agent/agents)** - ⭐ 487
   Open-source marketing agents for Claude, ChatGPT, Codex, OpenClaw & Hermes. One plugin: SEO audits, GEO / AI-visibility, local SEO, KOL pricing, social listening & competitive intelligence from read-only public data over MCP.

1003. **[MCP-Zero](https://github.com/xfey/MCP-Zero)** - ⭐ 487
   MCP-Zero: Active Tool Discovery for Autonomous LLM Agents

1004. **[WyckoffTradingAgent](https://github.com/YoungCan-Wang/WyckoffTradingAgent)** - ⭐ 487
   Open-source Wyckoff trading agent and AI stock screener for volume-price analysis, A-share screening, CLI workflows, and MCP tools.灵感来自秋生trader @Hoyooyoo

1005. **[mcp-bench](https://github.com/Accenture/mcp-bench)** - ⭐ 486
   MCP-Bench: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers

1006. **[cordum](https://github.com/cordum-io/cordum)** - ⭐ 486
   The open agent control plane. Govern autonomous AI agents with pre-execution policy enforcement, approval gates, and audit trails. Works with LangChain, CrewAI, MCP, and any framework.

1007. **[xhs-mcp](https://github.com/jobsonlook/xhs-mcp)** - ⭐ 486
   小红书MCP服务 x-s x-t js逆向

1008. **[mcpe](https://github.com/ReMinecraftPE/mcpe)** - ⭐ 486
   ReMinecraftPE - A custom experience based on Minecraft PE as of 2011.

1009. **[NetCoreKevin](https://github.com/junkai-li/NetCoreKevin)** - ⭐ 485
   🤖基于.NET搭建的企业级中台AI知识库智能体开源架构：Skills技能管理、AI-Qdrant知识库、知识库重排模型、AI联网搜索、智能体权限管控、AgentFramework、RAG检索增强、本地Ollama AI模型调用、智能体技能可控加载、领域事件、一库多租户、Log4、Jwt、CAP、SignalR、Mcp、Ioc、Hangfire、RabbitMQ、Xunit、前端（Vue + Ant Design）

1010. **[mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite)** - ⭐ 485
   MCP Server to interact with Google Gsuite prodcuts

1011. **[ctx](https://github.com/stevesolun/ctx)** - ⭐ 484
   Skill, agent, MCP, and harness recommendations for Claude Code/custom LLMs: 102,928-node LLM-wiki graph, 91,464 skills, 467 agents, 10,790 MCPs, 207 harnesses, and capped execution recommendations.

1012. **[Agent](https://github.com/macOS26/Agent)** - ⭐ 482
   Mac Agent for macOS 26: the agentic AI harness for your Mac Desktop. Computer use, automation, scripting, coding, and more. Powered by 18+ providers across local and cloud LLMs.

1013. **[skills-for-fabric](https://github.com/microsoft/skills-for-fabric)** - ⭐ 482
   A collection of skills and MCP systems to enable users of CLI, VSCode, Claude to operate over Microsoft Fabric

1014. **[docker-mcp](https://github.com/QuantGeekDev/docker-mcp)** - ⭐ 482
   A docker MCP Server (modelcontextprotocol)

1015. **[skills](https://github.com/unifapi-agent/skills)** - ⭐ 482
   AI agent skills for UnifAPI MCP and public-data workflows

1016. **[kubeledger](https://github.com/realopslabs/kubeledger)** - ⭐ 481
   System of Record for Kubernetes cost accounting: per-namespace CPU, memory and GPU usage, with the 30% non-allocatable overhead made visible. Connects to AI assistants via MCP (Claude, Gemini, Mistral, Cursor) for plain-language analysis. Formerly Kube-Opex-Analytics.

1017. **[todoist-ai](https://github.com/Doist/todoist-ai)** - ⭐ 478
   A set of tools to connect to AI agents, to allow them to use Todoist on a user's behalf. Includes MCP support.

1018. **[director](https://github.com/fdmtl/director)** - ⭐ 478
   MCP Playbooks for AI agents

1019. **[camel-examples](https://github.com/apache/camel-examples)** - ⭐ 476
   Apache Camel Examples

1020. **[director](https://github.com/director-run/director)** - ⭐ 476
   MCP Playbooks for AI agents

1021. **[MakeMoneyWithAI](https://github.com/garylab/MakeMoneyWithAI)** - ⭐ 476
   A list of open-source AI projects you can use to generate income easily.

1022. **[unifapi](https://github.com/unif-api/unifapi)** - ⭐ 476
   UnifAPI — One Unified API for AI Agents

1023. **[apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server)** - ⭐ 476
   A MCP Server for APK Tool (Part of Android Reverse Engineering MCP Suites)

1024. **[atlas-mcp-server](https://github.com/cyanheads/atlas-mcp-server)** - ⭐ 475
   A Model Context Protocol (MCP) server for ATLAS, a Neo4j-powered task management system for LLM Agents - implementing a three-tier architecture (Projects, Tasks, Knowledge) to manage complex workflows. Now with Deep Research.

1025. **[roam-code](https://github.com/Cranot/roam-code)** - ⭐ 474
   Local codebase intelligence CLI + MCP server for AI coding agents: SQLite code graph, 28 languages, 238 commands, 224 MCP tools, change-safety gates, audit evidence, zero API keys.

1026. **[n8n-claw](https://github.com/freddy-schuetz/n8n-claw)** - ⭐ 473
   OpenClaw-inspired autonomous AI agent built entirely in n8n. Adaptive RAG-powered memory, Skills via MCP templates, Expert Agents with delegated sub-agents, proactive task management, media understanding - self-hosted with one setup script

1027. **[laravel](https://github.com/php-mcp/laravel)** - ⭐ 473
   An SDK building Laravel MCP servers

1028. **[ai-dive-deep](https://github.com/Belkins/ai-dive-deep)** - ⭐ 470
   Vlad's Playbook — the operator's field manual where every artifact is live, clickable, and forwardable. 39 chapters · 25 interactive widgets · 3 embedded case studies (AFC pitch + sanitized client audit). Read it → dive.vladyslavpodoliako.com

1029. **[Lynkr](https://github.com/Fast-Editor/Lynkr)** - ⭐ 468
   Streamline your workflow with Lynkr, a CLI tool that acts as an HTTP proxy for efficient code interactions using Claude Code CLI.

1030. **[kicad-mcp](https://github.com/lamaalrajih/kicad-mcp)** - ⭐ 468
   Model Context Protocol server for KiCad on Mac, Windows, and Linux

1031. **[aser](https://github.com/AmeNetwork/aser)** - ⭐ 467
   Aser is a lightweight, self-assembling AI Agent frame.

1032. **[mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb)** - ⭐ 467
   Search Airbnb using your AI Agent

1033. **[blockrun-mcp](https://github.com/BlockRunAI/blockrun-mcp)** - ⭐ 465
   Live data for AI agents — search, research, markets, crypto, X/Twitter. Pay-per-call via x402 micropayments.

1034. **[doctor](https://github.com/sisig-ai/doctor)** - ⭐ 465
   Doctor is a tool for discovering, crawl, and indexing web sites to be exposed as an MCP server for LLM agents.

1035. **[kmcp](https://github.com/kagent-dev/kmcp)** - ⭐ 464
   CLI tool and Kubernetes Controller for building, testing and deploying MCP servers

1036. **[applescript-mcp](https://github.com/peakmojo/applescript-mcp)** - ⭐ 462
   MCP server that execute applescript giving you full control of your Mac

1037. **[geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill)** - ⭐ 461
   GEO (Generative Engine Optimization) toolkit — audit, optimize, and make websites visible to AI search engines (ChatGPT, Perplexity, Claude, Gemini). Based on Princeton KDD 2024 research.

1038. **[awesome-mcp-devtools](https://github.com/punkpeye/awesome-mcp-devtools)** - ⭐ 460
   A curated list of developer tools, SDKs, libraries, and testing utilities for Model Context Protocol (MCP) server development.

1039. **[mcp-cli](https://github.com/apify/mcp-cli)** - ⭐ 459
   mcpc is a CLI client for MCP. It supports persistent sessions, stdio/HTTP, OAuth 2.1, JSON output for code mode, proxy for AI sandboxes, and much more.

1040. **[puppeteer-mcp-server](https://github.com/merajmehrabi/puppeteer-mcp-server)** - ⭐ 459
   This MCP server provides browser automation capabilities through Puppeteer, allowing interaction with both new browser instances and existing Chrome windows.

1041. **[prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server)** - ⭐ 459
   A Model Context Protocol (MCP) server that enables AI agents and LLMs to query and analyze Prometheus metrics through standardized interfaces.

1042. **[freee-mcp](https://github.com/freee/freee-mcp)** - ⭐ 456
   Model Context Protocol (MCP) server for freee API integration

1043. **[agent](https://github.com/1mcp-app/agent)** - ⭐ 454
   A unified Model Context Protocol server implementation that aggregates multiple MCP servers into one.

1044. **[gemini-cli-desktop](https://github.com/Piebald-AI/gemini-cli-desktop)** - ⭐ 454
   Web/desktop UI for Gemini CLI/Qwen Code.  Manage projects, switch between tools, search across past conversations, and manage MCP servers, all from one multilingual interface, locally or remotely.

1045. **[lunar](https://github.com/TheLunarCompany/lunar)** - ⭐ 454
   lunar.dev: Agent native MCP Gateway for governance and security

1046. **[claude-code-statusline](https://github.com/rz1989s/claude-code-statusline)** - ⭐ 453
   Transform your Claude Code terminal with atomic precision statusline. Features flexible layouts, real-time cost tracking, MCP monitoring, prayer times, and beautiful themes.

1047. **[welsonjs](https://github.com/gnh1201/welsonjs)** - ⭐ 451
   WelsonJS - Build a Windows app on the Windows built-in JavaScript engine

1048. **[life-sciences](https://github.com/anthropics/life-sciences)** - ⭐ 448
   Repo for the Claude Code Marketplace to use with the Claude for Life Sciences Launch. This will continue to host the marketplace.json long-term, but not the actual MCP servers.

1049. **[airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server)** - ⭐ 447
   🗂️🤖 Airtable Model Context Protocol Server, for allowing AI systems to interact with your Airtable bases

1050. **[nexus](https://github.com/grafbase/nexus)** - ⭐ 446
   Govern & Secure your AI

1051. **[nexus](https://github.com/nexus-ai-labs/nexus)** - ⭐ 446
   Govern & Secure your AI

1052. **[learn-low-code-agentic-ai](https://github.com/panaversity/learn-low-code-agentic-ai)** - ⭐ 445
   Low-Code Full-Stack Agentic AI Development using LLMs, n8n, Loveable, UXPilot, Supabase and MCP. Class Videos: https://www.youtube.com/playlist?list=PL0vKVrkG4hWq5T6yqCtUL7ol9rDuEyzBH

1053. **[mcp-send-email](https://github.com/resend/mcp-send-email)** - ⭐ 444
   Send emails directly from Cursor with this email sending MCP server

1054. **[designing-real-world-ai-agents-workshop](https://github.com/iusztinpaul/designing-real-world-ai-agents-workshop)** - ⭐ 443
   Hands-on workshop: Build a multi-agent AI system from scratch — Deep Research Agent + Writing Workflow served as MCP servers. Includes code, slides, and video

1055. **[ZeroToken](https://github.com/AMOS144/ZeroToken)** - ⭐ 442
   ZeroToken — Record once, automate forever. A lightweight MCP for agent-driven browser automation, script recording, and scheduled execution.

1056. **[anytype-mcp](https://github.com/anyproto/anytype-mcp)** - ⭐ 440
   An MCP server enabling AI assistants to interact with Anytype - your encrypted, local and collaborative wiki - to organize objects, lists, and more through natural language.

1057. **[stitch](https://github.com/gemini-cli-extensions/stitch)** - ⭐ 440
   The Stitch extension for Gemini CLI enables you to interact with the Stitch MCP server using natural language commands.

1058. **[Security-Detections-MCP](https://github.com/MHaggis/Security-Detections-MCP)** - ⭐ 440
   MCP to help Defenders Detection Engineer Harder and Smarter

1059. **[sandboxed.sh](https://github.com/Th0rgal/sandboxed.sh)** - ⭐ 440
   Safe runtime for autonomous on-chain AI agents: isolated sandboxes, Library skills, encrypted secrets, and OKX read-only security checks.

1060. **[mcp-cli](https://github.com/wong2/mcp-cli)** - ⭐ 438
   A CLI inspector for the Model Context Protocol

1061. **[azure-ai-travel-agents](https://github.com/Azure-Samples/azure-ai-travel-agents)** - ⭐ 437
   A robust enterprise application sample (deployed on ACA) that leverages MCP and multiple AI agents orchestrated by Langchain.js, Llamaindex.TS and Microsoft Agent Framework.

1062. **[strava-mcp](https://github.com/r-huijts/strava-mcp)** - ⭐ 437
   A Model Context Protocol (MCP) server that connects to Strava API, providing tools to access Strava data through LLMs

1063. **[azmx](https://github.com/AzmxAI/azmx)** - ⭐ 435
   AZMX AI — The sovereign agent platform.

1064. **[RenderDocMCP](https://github.com/halby24/RenderDocMCP)** - ⭐ 434

1065. **[katmer-code](https://github.com/hkcanan/katmer-code)** - ⭐ 433
   Claude Code inside Obsidian — academic research skills, inline diff editing, MCP support

1066. **[mcp](https://github.com/baidu-maps/mcp)** - ⭐ 432
   Baidu Map MCP Server

1067. **[kratos-transport](https://github.com/tx7do/kratos-transport)** - ⭐ 432
   kratos transport layer extension, support: rabbitmq,kafka,rocketmq,activemq,apollo,mcp,tcp,websocket...

1068. **[mcpstore](https://github.com/whillhill/mcpstore)** - ⭐ 431
   开盒即用的优雅管理mcp服务 | 结合Agent框架 | 作者听劝 | 已发布pypi | Vue页面demo

1069. **[Redbook-Search-Comment-MCP2.0](https://github.com/chenningling/Redbook-Search-Comment-MCP2.0)** - ⭐ 430
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client（如Claude for Desktop），帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布AI生成评论等操作。

1070. **[mcp-server-spec-driven-development](https://github.com/formulahendry/mcp-server-spec-driven-development)** - ⭐ 430
   Spec-Driven Development MCP Server, not just Vibe Coding

1071. **[shinkai-local-ai-agents](https://github.com/dcSpark/shinkai-local-ai-agents)** - ⭐ 429
   Shinkai is a two click install App that allows you to create Local AI agents in 5 minutes or less using a simple UI.  Supports: MCPs, Remote and Local AI, Crypto and Payments.

1072. **[nexus](https://github.com/Nexus-Router/nexus)** - ⭐ 429
   Govern & Secure your AI

1073. **[openclaw-claude-code](https://github.com/Enderfga/openclaw-claude-code)** - ⭐ 428
   OpenClaw plugin — turn Claude Code CLI into a programmable, headless coding engine with plenty of tools, agent teams, and multi-model proxy

1074. **[coolify-mcp](https://github.com/StuMason/coolify-mcp)** - ⭐ 426
   MCP server for Coolify — 42 optimized tools for managing self-hosted PaaS through AI assistants

1075. **[elementor-mcp](https://github.com/msrbuilds/elementor-mcp)** - ⭐ 424
   WordPress plugin that turns Elementor into an MCP server — 118+ AI-ready tools for building, editing, and managing page designs programmatically.

1076. **[aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol](https://github.com/microsoft/aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol)** - ⭐ 423

1077. **[station](https://github.com/cloudshipai/station)** - ⭐ 422
   Station is our open-source runtime that lets teams deploy agents on their own infrastructure with full control.

1078. **[skylos](https://github.com/duriantaco/skylos)** - ⭐ 422
   Open-source Python, TypeScript, and Go SAST with dead code detection. Finds secrets, exploitable   flows, and AI regressions. VS Code extension, GitHub Action, and MCP server for AI agents.

1079. **[mcpadapt](https://github.com/grll/mcpadapt)** - ⭐ 422
   Unlock 650+ MCP servers tools in your favorite agentic framework.

1080. **[claude-codepro](https://github.com/maxritter/claude-codepro)** - ⭐ 422
   Production-Grade Development Environment for Claude Code. Quality automated. Context optimized. Testing enforced. Ship with confidence. ✔️

1081. **[unifi-mcp](https://github.com/sirkirby/unifi-mcp)** - ⭐ 422
   MCP servers for the UniFi suite of applications, Network, Protect, Access, and Drive

1082. **[mcp](https://github.com/salesforcecli/mcp)** - ⭐ 421
   MCP Server for interacting with Salesforce instances

1083. **[mcpmark](https://github.com/eval-sys/mcpmark)** - ⭐ 420
   MCPMark is a comprehensive, stress-testing MCP benchmark designed to evaluate model and agent capabilities in real-world MCP use.

1084. **[after-effects-mcp](https://github.com/Dakkshin/after-effects-mcp)** - ⭐ 419
   MCP Server for Adobe After Effects. Enables remote control (compositions, text, shapes, solids, properties) via the Model Context Protocol using ExtendScript.

1085. **[speakeasy](https://github.com/speakeasy-api/speakeasy)** - ⭐ 419
   Build APIs your users love ❤️ with Speakeasy. ✨ Polished and type-safe SDKs. 🌐 Terraform providers, MCP servers, CLIs and Contract Tests for your API. OpenAPI native.

1086. **[memento-mcp](https://github.com/gannonh/memento-mcp)** - ⭐ 418
   Memento MCP: A Knowledge Graph Memory System for LLMs

1087. **[chatluna](https://github.com/ChatLunaLab/chatluna)** - ⭐ 417
   多平台模型接入，可扩展，多种输出格式，提供大语言模型聊天服务的插件 | A bot plugin for LLM chat with multi-model integration, extensibility, and various output formats

1088. **[PerformanceMonitor](https://github.com/erikdarlingdata/PerformanceMonitor)** - ⭐ 417
   Free, open-source SQL Server performance monitoring — 32 collectors, real-time alerts, graphical plan viewer, MCP server for AI analysis. Supports SQL 2016-2025, Azure SQL, AWS RDS.

1089. **[mcp-selenium](https://github.com/angiejones/mcp-selenium)** - ⭐ 416
   An MCP implementation for Selenium WebDriver

1090. **[edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp)** - ⭐ 416
   An MCP service designed for deploying HTML content to EdgeOne Pages and obtaining an accessible public URL.

1091. **[kagimcp](https://github.com/kagisearch/kagimcp)** - ⭐ 415
   The Official Model Context Protocol (MCP) server for Kagi Search & other tools.

1092. **[agent-builder](https://github.com/strands-agents/agent-builder)** - ⭐ 415
   An example agent demonstrating streaming, tool use, and interactivity from your terminal. This agent builder can help you to build your own agents and tools.

1093. **[entroly](https://github.com/juyterman1000/entroly)** - ⭐ 414
   Cut your Claude / OpenAI / Gemini bill 70–95% on AI coding. Local proxy that compresses context, keeps provider caches hot, and verifies LLM output ($0 hallucination guard). Drop-in for Cursor, Claude Code, Codex, Aider + 34 more and custom providers — 30s, no code changes

1094. **[memora](https://github.com/agentic-box/memora)** - ⭐ 410
   Give your AI agents persistent memory.

1095. **[lsbot](https://github.com/ruilisi/lsbot)** - ⭐ 409
   Lean & Secure Bot

1096. **[mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy)** - ⭐ 409
   A MCP (model context protocol) server that gives the LLM access to and knowledge about relational databases like SQLite, Postgresql, MySQL & MariaDB, Oracle, and MS-SQL.

1097. **[mcp](https://github.com/mondaycom/mcp)** - ⭐ 408
   Enable AI agents to work reliably - giving them secure access to structured data, tools to take action, and the context needed to make smart decisions.

1098. **[mcp-reddit](https://github.com/adhikasp/mcp-reddit)** - ⭐ 407
   A Model Context Protocol (MCP) server that provides tools for fetching and analyzing Reddit content.

1099. **[open-skills](https://github.com/instavm/open-skills)** - ⭐ 407
   OpenSkills: Run Claude Skills Locally using any LLM

1100. **[token-optimizer-mcp](https://github.com/ooples/token-optimizer-mcp)** - ⭐ 407
   Intelligent token optimization for Claude Code - achieving 95%+ token reduction through caching, compression, and smart tool intelligence

1101. **[distributed-load-testing-on-aws](https://github.com/aws-solutions/distributed-load-testing-on-aws)** - ⭐ 406
   Distributed Load Testing on AWS automates performance testing at scale, demonstrating how systems behave under different load conditions and helping identify potential performance issues throughout their lifecycle.

1102. **[f2c-mcp](https://github.com/f2c-ai/f2c-mcp)** - ⭐ 406
   F2C MCP Server

1103. **[droidmind](https://github.com/hyperb1iss/droidmind)** - ⭐ 406
   Control your Android devices with AI using Model Context Protocol

1104. **[ai4j](https://github.com/LnYo-Cly/ai4j)** - ⭐ 405
   一款JavaSDK用于快速接入AI大模型应用，整合多平台大模型，如OpenAi、智谱Zhipu(ChatGLM)、深度求索DeepSeek、月之暗面Moonshot(Kimi)、腾讯混元Hunyuan、零一万物(01)等等，提供统一的输入输出(对齐OpenAi)消除差异化，优化函数调用(Tool Call)，优化RAG调用、支持向量数据库(Pinecone)、内置联网增强，并且支持JDK1.8，为用户提供快速整合AI的能力。

1105. **[STS2MCP](https://github.com/Gennadiyev/STS2MCP)** - ⭐ 404
   Full agentic runs for Slay the Spire 2. A mod that exposes in-game state, and the MCP server for the mod.

1106. **[agentcontrolplane](https://github.com/humanlayer/agentcontrolplane)** - ⭐ 404
   ACP is the Agent Control Plane - a distributed agent scheduler optimized for simplicity, clarity, and control. It is designed for outer-loop agents that run without supervision, and make asynchronous tool calls like requesting human feedback on key operations. Full MCP support.

1107. **[cursor-rules-java](https://github.com/jabrena/cursor-rules-java)** - ⭐ 404
   An opinionated, AI-native development workflow for Java Enterprise — reusable Skills, Agents, Commands, and MCP servers combined with a human-in-the-loop model to modernize real-world SDLC practices.

1108. **[RestClient.Net](https://github.com/MelbourneDeveloper/RestClient.Net)** - ⭐ 404
   The safest way to make REST calls in C# with an MCP Generator

1109. **[ast-grep-mcp](https://github.com/ast-grep/ast-grep-mcp)** - ⭐ 402

1110. **[mcp-youtube-transcript](https://github.com/jkawamoto/mcp-youtube-transcript)** - ⭐ 402
   MCP server retrieving transcripts of YouTube videos

1111. **[solon-ai](https://github.com/opensolon/solon-ai)** - ⭐ 401
   Java AI application development framework (supports LLM-tool,skill; RAG; MCP; Agent-ReAct,Team-Agent). Compatible with java8 ~ java25. It can also be embedded in SpringBoot, jFinal, Vert.x, Quarkus, and other frameworks.

1112. **[MCP-SecurityTools](https://github.com/Ta0ing/MCP-SecurityTools)** - ⭐ 400
   MCP-SecurityTools 是一个专注于收录和更新网络安全领域 MCP 的开源项目，旨在汇总、整理和优化各类与 MCP 相关的安全工具、技术及实战经验。

1113. **[skillz](https://github.com/intellectronica/skillz)** - ⭐ 399
   An MCP server for loading skills (shim for non-claude clients).

1114. **[novamira](https://github.com/use-novamira/novamira)** - ⭐ 399
   MCP server that gives AI agents full access to WordPress through PHP execution and filesystem operations

1115. **[Agentfy](https://github.com/Agentfy-io/Agentfy)** - ⭐ 397
   🤖 Agentfy is a modular microservices architecture designed to process user requests and execute workflows across multiple social media platforms.  ASK ONCE, LET THE AGENT DO THE REST!

1116. **[twitter-mcp](https://github.com/EnesCinr/twitter-mcp)** - ⭐ 397
   A Model Context Protocol server allows to interact with Twitter, enabling posting tweets and searching Twitter.

1117. **[tentix](https://github.com/labring/tentix)** - ⭐ 397
   TenTix (10x Efficiency) - An AI native customer service platform with 10x accelerated resolution. Support MCP extension, and AI knowlage base system.

1118. **[one-mcp](https://github.com/burugo/one-mcp)** - ⭐ 396
   A centralized reverse-proxy platform for MCP servers — manage, group, and export as Skills from a single endpoint.

1119. **[mcp-code-graph](https://github.com/JudiniLabs/mcp-code-graph)** - ⭐ 396
   MCP Server for code graph analysis and visualization by CodeGPT

1120. **[octocode](https://github.com/Muvon/octocode)** - ⭐ 396
   Semantic code searcher and codebase utility

1121. **[Context-Engine](https://github.com/Context-Engine-AI/Context-Engine)** - ⭐ 395
   Context-Engine MCP - Agentic Context Compression Suite

1122. **[mcp-apple-notes](https://github.com/RafalWilinski/mcp-apple-notes)** - ⭐ 395
   Talk with your notes in Claude. RAG over your Apple Notes using Model Context Protocol.

1123. **[Software-planning-mcp](https://github.com/NightTrek/Software-planning-mcp)** - ⭐ 394
   An experiment in software planning using MCP

1124. **[todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server)** - ⭐ 393
   MCP server for Todoist integration enabling natural language task management with Claude

1125. **[mcp-graphql](https://github.com/blurrah/mcp-graphql)** - ⭐ 392
   Model Context Protocol server for GraphQL

1126. **[claude-skills-mcp](https://github.com/K-Dense-AI/claude-skills-mcp)** - ⭐ 392
   MCP server for searching and retrieving Claude Agent Skills using vector search

1127. **[automation-mcp](https://github.com/ashwwwin/automation-mcp)** - ⭐ 391
   Control your Mac with detailed mouse, keyboard, screen, and window management capabilities.

1128. **[CAD-MCP](https://github.com/daobataotie/CAD-MCP)** - ⭐ 391
   CAD MCP Server

1129. **[outlook-mcp](https://github.com/ryaker/outlook-mcp)** - ⭐ 391
   MCP server for Claude to access Outlook data via Microsoft Graph API

1130. **[groq-desktop-beta](https://github.com/groq/groq-desktop-beta)** - ⭐ 390
   Local Groq Desktop chat app with MCP support

1131. **[bazi-mcp](https://github.com/cantian-ai/bazi-mcp)** - ⭐ 389
   MCP server for Bazi (八字) information

1132. **[devopness](https://github.com/devopness/devopness)** - ⭐ 389
   DevOps Happiness: 1-click or 1-prompt MCP. Deploy apps + infra + CI/CD on your cloud. Happy humans + reliable agents. 🚀

1133. **[minion-agent](https://github.com/femto/minion-agent)** - ⭐ 389
   A simple agent framework that's capable of browser use + mcp + auto instrument + plan + deep  research + more

1134. **[applescript-mcp](https://github.com/joshrutkowski/applescript-mcp)** - ⭐ 389
   A macOS AppleScript MCP server

1135. **[mcp-calculator](https://github.com/78/mcp-calculator)** - ⭐ 388
   Xiaozhi MCP sample program

1136. **[db-mcp-server](https://github.com/FreePeak/db-mcp-server)** - ⭐ 387
   A powerful multi-database server implementing the Model Context Protocol (MCP) to provide AI assistants with structured access to databases.

1137. **[ableton-live-mcp-server](https://github.com/Simon-Kansara/ableton-live-mcp-server)** - ⭐ 387
   MCP Server implementation for Ableton Live OSC control

1138. **[mcp-hfspace](https://github.com/evalstate/mcp-hfspace)** - ⭐ 386
   MCP Server to Use HuggingFace spaces, easy configuration and Claude Desktop mode.

1139. **[skillport](https://github.com/gotalab/skillport)** - ⭐ 385
   Bring Agent Skills to Any AI Agent and Coding Agent — via CLI or MCP. Manage once, serve anywhere.

1140. **[mcp](https://github.com/IBM/mcp)** - ⭐ 383
   A collection of Model Context Protocol (MCP) servers, clients and developer tools by IBM.

1141. **[clawreins](https://github.com/pegasi-ai/clawreins)** - ⭐ 383
   Runtime security for OpenClaw agents. Scan, fix, monitor.

1142. **[mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** - ⭐ 382
   A Model Context Protocol (MCP) server that provides tools for interacting with Trello boards.

1143. **[binary_ninja_mcp](https://github.com/fosdickio/binary_ninja_mcp)** - ⭐ 382
   A Binary Ninja plugin containing an MCP server that enables seamless integration with your favorite LLM/MCP client.

1144. **[mcp-k8s-go](https://github.com/strowk/mcp-k8s-go)** - ⭐ 382
   MCP server connecting to Kubernetes

1145. **[mcp-aktools](https://github.com/aahl/mcp-aktools)** - ⭐ 381
   📈 提供股票、加密货币的数据查询和分析功能MCP服务器

1146. **[studio](https://github.com/decocms/studio)** - ⭐ 381
   Open-source control plane for your AI agents. Connect tools, hire agents, track every token and dollar

1147. **[azan-mcp](https://github.com/ahmedeltaher/azan-mcp)** - ⭐ 380
   Azan + Prayer Time + MCP + AI Agents + Islamic + Salah + A lightweight MCP library to calculate prayer times and trigger Azan with a single tool call. If you’re building an AI agent or prayer application, there’s no need to deal with astronomical calculations, timezones, or edge cases again.

1148. **[beever-atlas](https://github.com/Beever-AI/beever-atlas)** - ⭐ 380
   Your First LLM-Wiki Conversation Knowledge Base

1149. **[bagel](https://github.com/Extelligence-ai/bagel)** - ⭐ 380
   Chat with your robotics, drone, and IoT data — ChatGPT for the physical world.

1150. **[PlanExe](https://github.com/PlanExeOrg/PlanExe)** - ⭐ 380
   Create a plan from a description in minutes

1151. **[xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server)** - ⭐ 380
   MCP Server implementation for Xcode integration

1152. **[labs-ai-tools-for-devs](https://github.com/docker/labs-ai-tools-for-devs)** - ⭐ 379
   Your trusted home for discovering MCP tools – seamlessly integrated into Docker

1153. **[evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server)** - ⭐ 379
   MCP server that provides LLMs with tools for interacting with EVM networks

1154. **[abcoder](https://github.com/cloudwego/abcoder)** - ⭐ 378
   deep, reliable and confidential coding-context

1155. **[mcp-teams-server](https://github.com/InditexTech/mcp-teams-server)** - ⭐ 378
   An MCP (Model Context Protocol) server implementation for Microsoft Teams integration, providing capabilities to read messages, create messages, reply to messages, mention members.

1156. **[graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server)** - ⭐ 376
   Model Context Protocol (MCP) Server for Graphlit Platform

1157. **[mcp-gateway](https://github.com/lasso-security/mcp-gateway)** - ⭐ 376
   A plugin-based gateway that orchestrates other MCPs and allows developers to build upon it enterprise-grade agents.

1158. **[ai-agent-team](https://github.com/peterfei/ai-agent-team)** - ⭐ 376
   AI Agent Team-拥有24/7专业AI开发团队：产品经理、前端开发、后端开发、测试工程师、DevOps工程师、技术负责人。一键安装，支持中英文命令，大幅提升开发效率！

1159. **[1c_mcp](https://github.com/vladimir-kharin/1c_mcp)** - ⭐ 376
   Инструмент для создания MCP-серверов в 1С:Предприятие путем разработки расширения конфигурации. Позволяет интегрировать данные и функциональность 1С с AI-ассистентами (Claude, Cursor и т.д.). Включает Python-прокси и пример расширения 1С с готовыми инструментами.

1160. **[CAAL](https://github.com/CoreWorxLab/CAAL)** - ⭐ 375
   Local voice assistant that learns new abilities via auto-discovered n8n workflows exposed as tools via MCP

1161. **[mcp](https://github.com/oracle/mcp)** - ⭐ 375
   Repository containing MCP (Model Context Protocol) servers that provides a suite of tools for managing and interacting with Oracle products.

1162. **[iam-policy-autopilot](https://github.com/awslabs/iam-policy-autopilot)** - ⭐ 374
   IAM Policy Autopilot is an open source static code analysis tool that helps you quickly create baseline AWS IAM policies that you can refine as your application evolves. This tool is available as a command-line utility and MCP server for use within AI coding assistants for quickly building IAM policies.

1163. **[RetroMCP-Java](https://github.com/MCPHackers/RetroMCP-Java)** - ⭐ 374
   A rewrite of MCP to provide support for many versions of Minecraft which were never supported by original MCP

1164. **[private-journal-mcp](https://github.com/obra/private-journal-mcp)** - ⭐ 374
   A lightweight MCP server that provides Claude with a private journaling capability to process feelings and thoughts

1165. **[MCPSharp](https://github.com/afrise/MCPSharp)** - ⭐ 373
   MCPSharp is a .NET library that helps you build Model Context Protocol (MCP) servers and clients - the standardized API protocol used by AI assistants and models.

1166. **[Gearsystem](https://github.com/drhelius/Gearsystem)** - ⭐ 373
   Sega Master System / Game Gear / SG-1000 emulator, debugger and embedded MCP server for macOS, Windows, Linux, BSD and RetroArch.

1167. **[vscode-mcp-server](https://github.com/juehang/vscode-mcp-server)** - ⭐ 373
   MCP server to expose VS Code editing features to an LLM for AI coding

1168. **[mnemo](https://github.com/MnemoAI/mnemo)** - ⭐ 373
   A MCP-Ready Intelligence Engine for Data & Agent-as-a-Service.

1169. **[mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops)** - ⭐ 373
   An MCP server for Azure DevOps

1170. **[run-model-context-protocol-servers-with-aws-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda)** - ⭐ 372
   Run existing Model Context Protocol (MCP) stdio-based servers in AWS Lambda functions

1171. **[docfork-mcp](https://github.com/docfork/docfork-mcp)** - ⭐ 372
   Docfork MCP - Up-to-date Docs for AI Agents.

1172. **[Construction-Hazard-Detection](https://github.com/yihong1120/Construction-Hazard-Detection)** - ⭐ 372
   Enhances construction site safety using YOLO for object detection, identifying hazards like workers without helmets or safety vests, and proximity to machinery or vehicles. HDBSCAN clusters safety cone coordinates to create monitored zones. Post-processing algorithms improve detection accuracy.

1173. **[hermes-mcp](https://github.com/cloudwalk/hermes-mcp)** - ⭐ 371
   Elixir Model Context Protocol (MCP) SDK

1174. **[Anemoi](https://github.com/Coral-Protocol/Anemoi)** - ⭐ 370
   Anemoi: A Semi-Centralized Multi-agent Systems Based on Agent-to-Agent Communication MCP server from Coral Protocol

1175. **[daymon](https://github.com/daymonio/daymon)** - ⭐ 370
   Daymon puts your favorite AI to work 24/7. It schedules, remembers, and orchestrates your own virtual team. Free.

1176. **[lingti-bot](https://github.com/ruilisi/lingti-bot)** - ⭐ 370
   🐕⚡「极简至上 效率为王 秒级接入 一链即用」的 AI Bot

1177. **[minthcm](https://github.com/minthcm/minthcm)** - ⭐ 369
   Open-source HCM system for managing HR processes with AI agents. Full data ownership, MCP/A2A-native, no vendor lock-in.

1178. **[solomd](https://github.com/zhitongblog/solomd)** - ⭐ 369
   A markdown editor — and the bridge to your LLM. Local-first, MIT, ~15 MB. Bundled MCP server lets Claude Code / Codex / Cursor drive your vault directly. 14 AI providers BYOK.

1179. **[mcp2mqtt](https://github.com/mcp2everything/mcp2mqtt)** - ⭐ 368
   本项目通过将 MCP 协议转换为 MQTT 协议，我们能够利用强大的大型语言模型（LLMs），就能轻松操控您的智能家居、机器人或其他硬件设备。

1180. **[tfmcp](https://github.com/nwiizo/tfmcp)** - ⭐ 368
   🌍 Terraform Model Context Protocol (MCP) Tool - An experimental CLI tool that enables AI assistants to manage and operate Terraform environments. Supports reading Terraform configurations, analyzing plans, applying configurations, and managing state with Claude Desktop integration. ⚡️

1181. **[ebook-mcp](https://github.com/onebirdrocks/ebook-mcp)** - ⭐ 367
   A MCP server that supports mainstream eBook formats including EPUB, PDF and more. Simplify your eBook user experience with LLM.

1182. **[touchdesigner-mcp](https://github.com/8beeeaaat/touchdesigner-mcp)** - ⭐ 366
   MCP server for TouchDesigner

1183. **[mcp-sdk-php](https://github.com/logiscape/mcp-sdk-php)** - ⭐ 366
   Model Context Protocol SDK for PHP

1184. **[VTCode](https://github.com/vinhnx/VTCode)** - ⭐ 365
   VT Code - Semantic coding agent in the terminal

1185. **[spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server)** - ⭐ 364
   Lightweight MCP server for Spotify

1186. **[lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp)** - ⭐ 364
   Lean Theorem Prover MCP

1187. **[meta-ads-analyzer](https://github.com/mathiaschu/meta-ads-analyzer)** - ⭐ 363
   Meta Ads Analyzer skill + MCP server for Claude Code. Breakdown Effect, Learning Phase, and expert-level campaign diagnosis.

1188. **[desktop](https://github.com/agentify-sh/desktop)** - ⭐ 362
   Agentify Desktop lets Codex/Claude/OpenCode  control your logged-in ChatGPT, Claude, AiStudio, Gemini, Grok, Perplexity web sessions via MCP, parallel hidden/visible tabs, file upload + image download

1189. **[mssql_mcp_server](https://github.com/RichardHan/mssql_mcp_server)** - ⭐ 362
   A Model Context Protocol (MCP) server for Microsoft SQL Server that enables secure database interactions through a controlled interface. Allows AI assistants to safely list tables, read data, and execute SQL queries while maintaining security and structure.

1190. **[x64dbgMCP](https://github.com/Wasdubya/x64dbgMCP)** - ⭐ 362
   Model Context Protocol for x64dbg & x32dbg

1191. **[nanobanana-mcp-server](https://github.com/zhongweili/nanobanana-mcp-server)** - ⭐ 362
   AI image generation MCP server powered by Google Gemini, with smart model selection and 4K output

1192. **[Awesome-Gemini-Omni-API-Prompts](https://github.com/Anil-matcha/Awesome-Gemini-Omni-API-Prompts)** - ⭐ 361
   Curated Google Gemini Omni prompts & API examples — text-to-video, image-to-video, video edit via the Gemini Omni API on muapi.ai. Python wrapper, MCP server, REST examples.

1193. **[BloodHound-MCP-AI](https://github.com/MorDavid/BloodHound-MCP-AI)** - ⭐ 360
   BloodHound-MCP-AI is integration that connects BloodHound with AI through Model Context Protocol, allowing security professionals to analyze Active Directory attack paths using natural language instead of complex Cypher queries.

1194. **[hookdeck-cli](https://github.com/hookdeck/hookdeck-cli)** - ⭐ 359
   CLI for Hookdeck: forward webhooks to localhost (ngrok alternative), manage and query Event Gateway resources (sources, connections, destinations, events), run the MCP server for AI agents. Free for dev.

1195. **[godot-mcp](https://github.com/tomyud1/godot-mcp)** - ⭐ 359
   MCP Server and Godot Plugin for AI-assisted game development

1196. **[pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp)** - ⭐ 359
   MCP server for PageIndex. PageIndex is a vectorless reasoning-based RAG system which uses multi-step reasoning and tree search to retrieve information like a human expert would.

1197. **[pinion-os](https://github.com/chu2bard/pinion-os)** - ⭐ 357
   Client SDK, Claude plugin and skill framework for the Pinion protocol. x402 micropayments on Base.

1198. **[EDDI](https://github.com/labsai/EDDI)** - ⭐ 357
   Config-driven engine that turns JSON into production-grade AI agents. Multi-agent orchestration, 12+ LLM providers, MCP/A2A protocols, RAG, persistent memory, and enterprise compliance (EU AI Act, GDPR, HIPAA). Built on Quarkus.

1199. **[mcp-database-server](https://github.com/executeautomation/mcp-database-server)** - ⭐ 355
   MCP Database Server is a new MCP Server which helps connect with Sqlite, SqlServer and Posgresql Databases

1200. **[vtcode](https://github.com/vinhnx/vtcode)** - ⭐ 355
   VT Code - Semantic coding agent in the terminal

1201. **[hol-guard](https://github.com/hashgraph-online/hol-guard)** - ⭐ 354
   AI antivirus for developer agents: protect Codex, Claude Code, Cursor, Gemini, OpenCode, plugins, skills, MCP servers, and AI harnesses before tools run.

1202. **[Google-Scholar-MCP-Server](https://github.com/JackKuo666/Google-Scholar-MCP-Server)** - ⭐ 354
   A MCP Server for Google Scholar: 🔍 Enable AI assistants to search and access Google Scholar papers through a simple MCP interface.

1203. **[Ace-Mcp-Node](https://github.com/yeuxuan/Ace-Mcp-Node)** - ⭐ 354
   Acemcp 是一个高性能的 MCP (Model Context Protocol) 服务器，专为 AI 助手（如 Claude、GPT 等）提供代码库索引和语义搜索能力。通过 Acemcp，AI 助手可以：  🔍 快速搜索和理解大型代码库 📊 获取带行号的精确代码片段 🤖 自动增量更新索引 🌐 通过 Web 界面管理和调试

1204. **[comfyui-mcp-server](https://github.com/joenorton/comfyui-mcp-server)** - ⭐ 353
   lightweight Python-based MCP (Model Context Protocol) server for local ComfyUI

1205. **[mcp_massive](https://github.com/massive-com/mcp_massive)** - ⭐ 352
   An MCP server for Massive.com Financial Market Data

1206. **[Claude-Code-Frontend-Design-Toolkit](https://github.com/wilwaldon/Claude-Code-Frontend-Design-Toolkit)** - ⭐ 352
   Everything I've found that actually makes Claude Code output better-looking frontends. Skills, plugins, MCP servers, CLAUDE.md tricks

1207. **[gptr-mcp](https://github.com/assafelovic/gptr-mcp)** - ⭐ 351
   MCP server for enabling LLM applications to perform deep research via the MCP protocol

1208. **[discord-mcp](https://github.com/SaseQ/discord-mcp)** - ⭐ 350
   A MCP server for the Discord integration. Enable your AI assistants to seamlessly interact with Discord. Enhance your Discord experience with powerful automation capabilities.

1209. **[mcp-for-next.js](https://github.com/vercel-labs/mcp-for-next.js)** - ⭐ 350

1210. **[base-mcp](https://github.com/base/base-mcp)** - ⭐ 348
   A Model Context Protocol (MCP) server that provides onchain tools for LLMs, allowing them to interact with the Base network and Coinbase API.

1211. **[purple](https://github.com/erickochen/purple)** - ⭐ 348
   Free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 16 cloud providers, monitors live SSH tunnels and manages Docker and Podman containers fleet-wide. Plus scp, Vault SSH certs and an MCP server for AI agents.

1212. **[revit-mcp](https://github.com/revit-mcp/revit-mcp)** - ⭐ 347
   AI-Powered Revit Modeling

1213. **[interactive-mcp](https://github.com/ttommyth/interactive-mcp)** - ⭐ 347
   Vibe coding should have human in the loop! interactive-mcp: Local, cross-platform MCP server for interact with your AI Agent

1214. **[frida-mcp](https://github.com/dnakov/frida-mcp)** - ⭐ 346
   MCP stdio server for frida

1215. **[mcp-server](https://github.com/mapbox/mcp-server)** - ⭐ 346
   Mapbox Model Context Protocol (MCP) server

1216. **[django-mcp-server](https://github.com/gts360/django-mcp-server)** - ⭐ 345
   Django MCP Server is a Django extensions to easily enable AI Agents to interact with Django Apps through the Model Context Protocol it works equally well on WSGI and ASGI

1217. **[linear-mcp-server](https://github.com/jerhadf/linear-mcp-server)** - ⭐ 344
   A server that integrates Linear's project management system with the Model Context Protocol (MCP) to allow LLMs to interact with Linear.

1218. **[polymarket-paper-trader](https://github.com/agent-next/polymarket-paper-trader)** - ⭐ 343
   Paper trading simulator for Polymarket — built for AI agents. MCP server, live order books, strategy backtesting. Install: npx clawhub install polymarket-paper-trader

1219. **[MemoryMesh](https://github.com/CheMiguel23/MemoryMesh)** - ⭐ 343
   A knowledge graph server that uses the Model Context Protocol (MCP) to provide structured memory persistence for AI models.

1220. **[devtools-debugger-mcp](https://github.com/ScriptedAlchemy/devtools-debugger-mcp)** - ⭐ 343
   An MCP server exposing full Chrome DevTools Protocol debugging: breakpoints, step/run, call stacks, eval, and source maps.

1221. **[clawdcursor](https://github.com/AmrDab/clawdcursor)** - ⭐ 342
   MCP-powered fallback layer that lets AI agents execute tasks through the GUI when APIs, tools, or direct integrations are unavailable. Cross-OS, accessibility-first, local-only.

1222. **[mcp-google-map](https://github.com/cablate/mcp-google-map)** - ⭐ 342
   A powerful Model Context Protocol (MCP) server providing comprehensive Google Maps API integration with LLM processing capabilities.

1223. **[mcp-server-12306](https://github.com/drfccv/mcp-server-12306)** - ⭐ 342
   12306 MCP Server​​ 是一个基于 ​​Model Context Protocol (MCP)​​ 的高性能火车票查询后端系统。它通过标准化接口提供官方 12306 的实时数据服务，包括余票查询、车站信息、列车经停站、中转换乘方案等核心功能。

1224. **[Octopoda-OS](https://github.com/RyjoxTechnologies/Octopoda-OS)** - ⭐ 342
   The open-source memory operating system for AI agents. Persistent memory, semantic search, loop detection, agent messaging, crash recovery, and real-time observability.

1225. **[kindly-web-search-mcp-server](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server)** - ⭐ 342
   Kindly Web Search MCP Server: Web search + robust content retrieval for AI coding tools (Claude Code, Codex, Cursor, GitHub Copilot, Gemini, etc.) and AI agents (Claude Desktop, OpenClaw, Hermes, etc.). Supports Serper, Tavily, and SearXNG.

1226. **[Aegis](https://github.com/Justin0504/Aegis)** - ⭐ 341
   Runtime policy enforcement for AI agents. Cryptographic audit trail, human-in-the-loop approvals, kill switch. Zero code changes.

1227. **[MaaMCP](https://github.com/MAA-AI/MaaMCP)** - ⭐ 341
   基于 MaaFramework 的 MCP 服务器 为 AI 助手提供 Android 设备和 Windows 桌面自动化能力

1228. **[obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin)** - ⭐ 340
   High-performance Model Context Protocol (MCP) server for Obsidian that provides AI tools with direct vault access through semantic operations and HTTP transport.

1229. **[deepseek-mcp-server](https://github.com/DMontgomery40/deepseek-mcp-server)** - ⭐ 340
   Model Context Protocol server for DeepSeek's advanced language models

1230. **[agent-skills](https://github.com/microsoft/agent-skills)** - ⭐ 340
   Skills, MCP servers, Custom Coding Agents, Agents.md for SDKs to ground Coding Agents

1231. **[mcsmcp](https://github.com/microsoft/mcsmcp)** - ⭐ 340
   Lab for creating an MCP Server and using it in Microsoft Copilot Studio.

1232. **[real-estate-mcp](https://github.com/tae0y/real-estate-mcp)** - ⭐ 340
   🏠 Ask Claude about Korean apartment prices — powered by 국토교통부 open API

1233. **[tinystruct](https://github.com/tinystruct/tinystruct)** - ⭐ 339
   A lightweight, modular Java application framework for web and CLI development,         designed for AI integration and plugin-based architecture.         Enabling developers to create robust solutions with ease for building efficient and scalable applications.

1234. **[zypher-agent](https://github.com/corespeed-io/zypher-agent)** - ⭐ 338
   A minimal yet powerful framework for creating AI agents with full control over tools, providers, and execution flow.

1235. **[scrumboy](https://github.com/markrai/scrumboy)** - ⭐ 338
   Self-hosted kanban & project management with shareable boards, voice commands, sticky-notes and MCP support

1236. **[mesh](https://github.com/decocms/mesh)** - ⭐ 337
   One secure endpoint for every MCP server. Deploy anywhere.

1237. **[DebugMCP](https://github.com/microsoft/DebugMCP)** - ⭐ 337
   Gift your VS Code agent a real debugger: breakpoints, stepping, inspection.

1238. **[redd-archiver](https://github.com/19-84/redd-archiver)** - ⭐ 336
   A PostgreSQL-backed archive generator that creates browsable HTML archives from link aggregator platforms including Reddit, Voat, and Ruqqus.

1239. **[telegram-mcp](https://github.com/chaindead/telegram-mcp)** - ⭐ 336
   Telegram MCP for managing dialogs, messages, drafts, read statuses, and more.

1240. **[agentic-ai-apis](https://github.com/cporter202/agentic-ai-apis)** - ⭐ 336
   The ultimate collection of APIs for building autonomous AI agents — 2,036 production-ready APIs across Agents, AI Models, and MCP Servers. Stop wasting weeks building infrastructure. Plug these in and ship your agent today.

1241. **[awesome-cursor-mpc-server](https://github.com/kleneway/awesome-cursor-mpc-server)** - ⭐ 336
   Example of an MCP server with custom tools that can be called directly from cursor

1242. **[claude-code-tool-manager](https://github.com/tylergraydev/claude-code-tool-manager)** - ⭐ 336
   GUI app to manage MCP servers for Claude Code

1243. **[wexin-read-mcp](https://github.com/Bwkyd/wexin-read-mcp)** - ⭐ 335
   能够让大模型阅读微信公众号文章，使用浏览器模拟绕过反爬虫。

1244. **[moling](https://github.com/gojue/moling)** - ⭐ 335
   MoLing is a computer-use and browser-use based MCP server. It is a locally deployed, dependency-free office AI assistant.

1245. **[cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** - ⭐ 335
   Cross-Code Organizer (formerly Claude Code Organizer): cross-harness config dashboard for Claude Code, Codex CLI, MCP servers, skills, memories, agents, sessions, security scanning, context budget, and backups.

1246. **[mcp-server-code-execution-mode](https://github.com/elusznik/mcp-server-code-execution-mode)** - ⭐ 334
   An MCP server that executes Python code in isolated rootless containers with optional MCP server proxying. Implementation of Anthropic's and Cloudflare's ideas for reducing MCP tool definitions context bloat.

1247. **[investor-agent](https://github.com/ferdousbhai/investor-agent)** - ⭐ 333
   A Model Context Protocol server for building an investor agent

1248. **[open-mcp](https://github.com/wegotdocs/open-mcp)** - ⭐ 333

1249. **[mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts)** - ⭐ 332

1250. **[mcp-odoo](https://github.com/tuanle96/mcp-odoo)** - ⭐ 332
   MCP Server for Odoo

1251. **[paws-on-mcp](https://github.com/hemanth/paws-on-mcp)** - ⭐ 331
   A comprehensive Model Context Protocol (MCP) server implementing the latest specification.

1252. **[laravel-mcp-server](https://github.com/opgginc/laravel-mcp-server)** - ⭐ 331
   A Laravel package for implementing secure Model Context Protocol servers using Streamable HTTP and SSE transport, providing real-time communication and a scalable tool system for enterprise environments.

1253. **[CodeGraphContext](https://github.com/Shashankss1205/CodeGraphContext)** - ⭐ 331
   An MCP server plus a CLI tool that indexes local code into a graph database to provide context to AI assistants.

1254. **[css-mcp](https://github.com/stolinski/css-mcp)** - ⭐ 330

1255. **[ddddocr](https://github.com/86maid/ddddocr)** - ⭐ 329
   ddddocr rust 版本，ocr_api_server rust 版本，二进制版本，验证码识别，不依赖 opencv 库，跨平台运行，AI MCP 支持，a simple OCR API server, very easy to deploy。

1256. **[mcp-server-macos-use](https://github.com/mediar-ai/mcp-server-macos-use)** - ⭐ 329
   AI agent that controls computer with OS-level tools, MCP compatible, works with any model

1257. **[facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server)** - ⭐ 328

1258. **[godot-mcp-pro](https://github.com/youichi-uda/godot-mcp-pro)** - ⭐ 328
   162 MCP tools for AI-powered Godot 4 development. Scene, animation, 3D, physics, particles, audio, shader, input simulation, runtime analysis, navigation, testing & more. $15 one-time.

1259. **[mcp-servers-hub](https://github.com/apappascs/mcp-servers-hub)** - ⭐ 326
   Discover the most comprehensive and up-to-date collection of MCP servers in the market. This repository serves as a centralized hub, offering an extensive catalog of open-source and proprietary MCP servers, complete with features, documentation links, and contributors.

1260. **[agent-trade-kit](https://github.com/okx/agent-trade-kit)** - ⭐ 326
   OKX trading MCP server — connect AI agents to spot, swap, futures, options & grid bots via the Model Context Protocol.

1261. **[safe-mcp](https://github.com/safe-agentic-framework/safe-mcp)** - ⭐ 325
   SAFE-MCP is a comprehensive security framework for documenting and mitigating threats in the AI Agent ecosystem.

1262. **[generator](https://github.com/context-hub/generator)** - ⭐ 324
   CTX: a tool that solves the context management gap when working with LLMs like ChatGPT or Claude. It helps developers organize and automatically collect information from their codebase into structured documents that can be easily shared with AI assistants.

1263. **[ClimateTraceKMP](https://github.com/joreilly/ClimateTraceKMP)** - ⭐ 324
   Kotlin/Compose Multiplatform project to show climate related emission data from https://climatetrace.org/data.

1264. **[HarnessKit](https://github.com/RealZST/HarnessKit)** - ⭐ 324
   More than a skill manager — manage skills, MCP servers, plugins, hooks, CLIs, configs, memory & rules across every AI coding agent. 🌟 Star if you like it!

1265. **[anki-mcp-server](https://github.com/ankimcp/anki-mcp-server)** - ⭐ 323
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Anki, the spaced repetition flashcard application.

1266. **[langconnect-client](https://github.com/teddynote-lab/langconnect-client)** - ⭐ 323
   A Modern GUI Interface for Vector Database Management(Supports MCP integration)

1267. **[mcp940](https://github.com/WangTingZheng/mcp940)** - ⭐ 323
   Source code of minecraft 1.12

1268. **[code-sandbox-mcp](https://github.com/Automata-Labs-team/code-sandbox-mcp)** - ⭐ 322
   An MCP server to create secure code sandbox environment for executing code within Docker containers. This MCP server provides AI applications with a safe and isolated environment for running code while maintaining security through containerization.

1269. **[MCPControl](https://github.com/claude-did-this/MCPControl)** - ⭐ 322
   MCP server for Windows OS automation

1270. **[Rube](https://github.com/ComposioHQ/Rube)** - ⭐ 322
   Rube is a Model Context Protocol (MCP) server that connects your AI tools to 500+ apps like Gmail, Slack, GitHub, and Notion. Simply install it in your AI client, authenticate once with your apps, and start asking your AI to perform real actions like "Send an email" or "Create a task."

1271. **[autocad-mcp](https://github.com/puran-water/autocad-mcp)** - ⭐ 322
   MCP server for AutoCAD LT v3.1: freehand AutoLISP execution, 8 consolidated tools, File IPC + ezdxf backends, focus-free dispatch, undo/redo, P&ID symbols, and robust IPC with ESC prefix and UTF-8 fallback. Companion agent skill: puran-water/autocad-drafting

1272. **[mcp-documentation-server](https://github.com/andrea9293/mcp-documentation-server)** - ⭐ 321
   MCP Documentation Server - Bridge the AI Knowledge Gap.  ✨ Features: Document management • Gemini integration • AI-powered semantic search • File uploads • Smart chunking • Multilingual support • Zero-setup  🎯 Perfect for: New frameworks • API docs • Internal guides

1273. **[mcp_flutter](https://github.com/Arenukvern/mcp_flutter)** - ⭐ 321
   MCP Toolkit for Flutter AI Agent Driven Development (MCP/CLI + custom client side tools) - via closed feedback loop (visual & semantic snapshot) and high client side customization adaptable for any Flutter app. Nowadays it is often called as agentic harness.

1274. **[cymbal-air-toolbox-demo](https://github.com/GoogleCloudPlatform/cymbal-air-toolbox-demo)** - ⭐ 321
   Demo of a customer service agent (Cymbal Air) using LangGraph, Tools, and RAG to interact with Google Cloud Databases via MCP Toolbox.

1275. **[h5i](https://github.com/h5i-dev/h5i)** - ⭐ 321
   Next-Gen AI-Aware Git. Auditable sandbox, prompt-aware commits, 95% less token waste, 3.5x richer PR brief, 1.8x faster multi-agent loops.

1276. **[sap-ai-mcp-servers](https://github.com/marianfoo/sap-ai-mcp-servers)** - ⭐ 321
   A complete list of SAP MCP Servers and SAP AI Skills

1277. **[emcee](https://github.com/mattt/emcee)** - ⭐ 321
   MCP generator for OpenAPIs 🫳🎤💥

1278. **[napi](https://github.com/nanoapi-io/napi)** - ⭐ 321
   Software architecture tooling for the AI age

1279. **[mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)** - ⭐ 321
   🔍 A Model Context Protocol (MCP) server providing unified access to multiple search engines (Tavily, Brave, Kagi, Exa), AI tools (Kagi FastGPT, Exa, Linkup), and content extraction services (Firecrawl, Tavily, Kagi). Includes GitHub search. All through a single interface.

1280. **[codemogger](https://github.com/glommer/codemogger)** - ⭐ 320
   Codemogger is a code indexing library and MCP server for AI coding agents

1281. **[mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search)** - ⭐ 320

1282. **[pydantic-resolve](https://github.com/allmonday/pydantic-resolve)** - ⭐ 319
   A universal data composition tool that generates JSON RPC, GraphQL, and even MCP.

1283. **[penpot-mcp](https://github.com/penpot/penpot-mcp)** - ⭐ 319
   Penpot's official MCP Server

1284. **[mcp-neovim-server](https://github.com/bigcodegen/mcp-neovim-server)** - ⭐ 318
   Control Neovim using Model Context Protocol (MCP) and the official neovim/node-client JavaScript library

1285. **[marionette_mcp](https://github.com/leancodepl/marionette_mcp)** - ⭐ 318
   MCP server enabling AI agents to interact with Flutter apps at runtime - let them inspect widgets, simulate taps, enter text, scroll, and take screenshots.

1286. **[Minecraft-Hack-BaseClient](https://github.com/OxideWaveLength/Minecraft-Hack-BaseClient)** - ⭐ 318
   This is a Minecraft Base Client

1287. **[AI-Kline](https://github.com/QuantML-C/AI-Kline)** - ⭐ 318
   Python-based stock analysis tool that combines traditional technical analysis with AI prediction capabilities.  Providing comprehensive stock analysis and forecasting using K-line charts, technical indicators, financial data, and news data. With CMD/WEB/MCP supported.

1288. **[imagesorcery-mcp](https://github.com/sunriseapps/imagesorcery-mcp)** - ⭐ 318
   An MCP server providing tools for image processing operations

1289. **[autogenstudio-skills](https://github.com/madtank/autogenstudio-skills)** - ⭐ 317
   Repo of skills for autogen studio using model context protocol (mcp)

1290. **[deep-research-mcp](https://github.com/teelaitila/deep-research-mcp)** - ⭐ 317

1291. **[sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp)** - ⭐ 316
   A SEC EDGAR MCP (Model Context Protocol) Server

1292. **[TradingAgents-MCPmode](https://github.com/guangxiangdebizi/TradingAgents-MCPmode)** - ⭐ 315
   TradingAgents-MCPmode 是一个创新的多智能体交易分析系统，集成了 Model Context Protocol (MCP) 工具，实现了智能化的股票分析和交易决策流程。系统通过多个专业化智能体的协作，提供全面的市场分析、投资建议和风险管理。

1293. **[mcp-ical](https://github.com/Omar-V2/mcp-ical)** - ⭐ 315
   A Model Context Protocol Server that allows you to interact with your MacOS Calendar through natural language.

1294. **[mcp-linker](https://github.com/milisp/mcp-linker)** - ⭐ 314
   mcp store manager, add & syncs MCP server configurations across clients like Claude code, Cursor💡mcphub

1295. **[gemini-kit](https://github.com/nth5693/gemini-kit)** - ⭐ 314
   🚀 19 AI Agents + 44 Commands for Gemini CLI - Code 10x faster with auto planning, testing, review & security

1296. **[mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** - ⭐ 313
   Model Context Protocol (MCP) server that enables AI assistants to securely interact with Odoo ERP systems through standardized resources and tools for data retrieval and manipulation.

1297. **[octo-terminal-releases](https://github.com/johunsang/octo-terminal-releases)** - ⭐ 313
   Octo Terminal — The ultimate vibe coding terminal. AI-powered IDE with Claude, Codex, Ollama built-in. Terminal + editor + notes + browser in one app. Tauri + React + Rust.

1298. **[agents](https://github.com/astronomer/agents)** - ⭐ 312
   AI agent tooling for data engineering workflows.

1299. **[mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest)** - ⭐ 311
   A Model Context Protocol (MCP) server that helps read GitHub repository structure and important files.

1300. **[h1-brain](https://github.com/PatrikFehrenbach/h1-brain)** - ⭐ 311
   MCP server that connects AI assistants to HackerOne for bug bounty hunting

1301. **[Ori-Mnemos](https://github.com/aayoawoyemi/Ori-Mnemos)** - ⭐ 310
   Local-first persistent agentic memory powered by Recursive Memory Harness (RMH). Open source must win.

1302. **[guild](https://github.com/mathomhaus/guild)** - ⭐ 309
   Shared context, memory, and task coordination across AI coding agents. Single Go binary, local SQLite, hybrid keyword and semantic search.

1303. **[obsidian-mcp](https://github.com/newtype-01/obsidian-mcp)** - ⭐ 309
   Obsidian MCP (Model Context Protocol) Server

1304. **[XActions](https://github.com/nirholas/XActions)** - ⭐ 309
   ⚡ The Complete X/Twitter Automation Toolkit — Scrapers, MCP server for AI agents (Claude/GPT), CLI, browser scripts. No API fees. Open source. Unfollow people who don't follow back. Monitor real-time analytics. Auto follow, like, comment, scrape, without API.

1305. **[deep-research-mcp](https://github.com/Ozamatash/deep-research-mcp)** - ⭐ 309

1306. **[mcp-server-tree-sitter](https://github.com/wrale/mcp-server-tree-sitter)** - ⭐ 309
   MCP Server for Tree-sitter

1307. **[yahoo-finance-mcp](https://github.com/Alex2Yang97/yahoo-finance-mcp)** - ⭐ 308
   This is a Model Context Protocol (MCP) server that provides comprehensive financial data from Yahoo Finance. It allows you to retrieve detailed information about stocks, including historical prices, company information, financial statements, options data, and market news.

1308. **[mcp-local-rag](https://github.com/shinpr/mcp-local-rag)** - ⭐ 308
   Local-first RAG server for developers. Semantic + keyword search for code and technical docs. Works with MCP or CLI. Fully private, zero setup.

1309. **[mcprouter](https://github.com/chatmcp/mcprouter)** - ⭐ 307
   api router for MCP Servers

1310. **[mcp-server-simulator-ios-idb](https://github.com/InditexTech/mcp-server-simulator-ios-idb)** - ⭐ 307
   A Model Context Protocol (MCP) server that enables LLMs to interact with iOS simulators through natural language commands.

1311. **[openmcp](https://github.com/getdatanaut/openmcp)** - ⭐ 306
   Turn any openapi file into an mcp server, with just the tools you need.

1312. **[appium-mcp](https://github.com/appium/appium-mcp)** - ⭐ 305
   Appium MCP on Steroids!

1313. **[sdk](https://github.com/smithery-ai/sdk)** - ⭐ 305
   Smithery helps AI agents access external services via a unified gateway.

1314. **[AIDA](https://github.com/Vasco0x4/AIDA)** - ⭐ 305
   AI-Driven Security Assessment - Connect AI to 400+ pentesting tools via MCP

1315. **[xero-mcp-server](https://github.com/XeroAPI/xero-mcp-server)** - ⭐ 304
   An MCP server that integrates with the MCP protocol. https://modelcontextprotocol.io/introduction

1316. **[doris-mcp-server](https://github.com/apache/doris-mcp-server)** - ⭐ 303
   Apache Doris MCP Server

1317. **[mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws)** - ⭐ 303
   AWS MCP Proxy Server

1318. **[mcp-server-mas-sequential-thinking](https://github.com/FradSer/mcp-server-mas-sequential-thinking)** - ⭐ 303
   An advanced sequential thinking process using a Multi-Agent System (MAS) built with the Agno framework and served via MCP.

1319. **[MARM-Systems](https://github.com/Lyellr88/MARM-Systems)** - ⭐ 303
   Stop re-explaining yourself to AI. MARM offers persistent memory, cross-agent context sharing, write queues, swarm-ready presets, and compaction for clean recall. Includes a live web dashboard for managing memories, logs, and sessions. MCP connects over HTTP & STDIO and works with major LLMs like Claude, Codex, Grok, Gemini, and other models.

1320. **[mcpsvr](https://github.com/nanbingxyz/mcpsvr)** - ⭐ 303
   Discover Exceptional MCP Servers

1321. **[llm-context.py](https://github.com/cyberchitta/llm-context.py)** - ⭐ 302
   Share code with LLMs via Model Context Protocol or clipboard. Rule-based customization enables easy switching between different tasks (like code review and documentation). Includes smart code outlining.

1322. **[Lucid](https://github.com/get-Lucid/Lucid)** - ⭐ 302
   An intelligence layer grounding autonomous agents in verified, real-time knowledge at scale.

1323. **[Dex](https://github.com/davekilleen/Dex)** - ⭐ 301
   Your AI Chief of Staff — a personal operating system starter kit that adapts to your role. No coding required.

1324. **[computer-use-mcp](https://github.com/domdomegg/computer-use-mcp)** - ⭐ 301
   💻 Give AI models complete control of your computer (probably a bad idea)

1325. **[obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp)** - ⭐ 301
   Connect Claude Code and other AI tools to your Obsidian notes using Model Context Protocol (MCP)

1326. **[perplexity-mcp](https://github.com/jsonallen/perplexity-mcp)** - ⭐ 301
   A Model Context Protocol (MCP) server that provides web search functionality using Perplexity AI's API.

1327. **[automcp](https://github.com/NapthaAI/automcp)** - ⭐ 301
   Easily convert tool, agents and orchestrators from existing agent frameworks to MCP servers

1328. **[mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code)** - ⭐ 301
   MCP implementation of Claude Code capabilities and more

1329. **[mcp-sse](https://github.com/sidharthrajaram/mcp-sse)** - ⭐ 301
   A working pattern for SSE-based MCP clients and servers

1330. **[gemini-antigravity-cli](https://github.com/testerlingcodo/gemini-antigravity-cli)** - ⭐ 301
   gemini antigravity 2.0 cli google terminal ai agent tool agy migration guide mcp server plugin slash commands gemini 3.5 flash coding agent tool free

1331. **[chrome-devtools-mcp](https://github.com/benjaminr/chrome-devtools-mcp)** - ⭐ 299
   An MCP Server for Chrome DevTools, following the Chrome DevTools Protocol. Integrates with Claude Desktop and Claude Code.

1332. **[aider-mcp-server](https://github.com/disler/aider-mcp-server)** - ⭐ 299
   Minimal MCP Server for Aider

1333. **[DeepWideResearch](https://github.com/puppyone-ai/DeepWideResearch)** - ⭐ 299
   Agentic RAG for any scenario. Customize sources, depth, and width

1334. **[hass-mcp](https://github.com/voska/hass-mcp)** - ⭐ 299
   Home Assistant MCP Server

1335. **[mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp)** - ⭐ 298
   An MCP server that securely interfaces with your iMessage database via the Model Context Protocol (MCP), allowing LLMs to query and analyze iMessage conversations. It includes robust phone number validation, attachment processing, contact management, group chat handling, and full support for sending and receiving messages.

1336. **[spring-ai-summary](https://github.com/java-ai-tech/spring-ai-summary)** - ⭐ 298
   SpringAI，LLM，MCP，Embedding

1337. **[certctl](https://github.com/shankar0123/certctl)** - ⭐ 298
   Self-hosted certificate lifecycle automation platform. Any CA, any server, zero human intervention. Full REST API, web dashboard, and agent-based deployment where private keys never leave your infrastructure. Includes CLI, MCP server for AI assistants, and compliance mapping for SOC 2, PCI-DSS, and NIST.

1338. **[mcp-server](https://github.com/volcengine/mcp-server)** - ⭐ 298
   Volcengine MCP Servers

1339. **[AgentRecall-MCP](https://github.com/Goldentrii/AgentRecall-MCP)** - ⭐ 297
   Persistent, correction-driven memory for AI agents. Cross-session, cross-platform (Claude Code, Codex, Gemini — any MCP client). Learns from mistakes, compresses context to save tokens, consolidates knowledge overnight. npm: agent-recall-mcp

1340. **[aws-mcp](https://github.com/RafalWilinski/aws-mcp)** - ⭐ 296
   Talk with your AWS using Claude. Model Context Protocol (MCP) server for AWS. Better Amazon Q alternative.

1341. **[MCP-Server-Playwright](https://github.com/VikashLoomba/MCP-Server-Playwright)** - ⭐ 296
   MCP server for browser automation using Playwright

1342. **[browser-control-mcp](https://github.com/eyalzh/browser-control-mcp)** - ⭐ 295
   MCP server paired with a browser extension that enables AI agents to control the user's browser.

1343. **[geminimcp](https://github.com/GuDaStudio/geminimcp)** - ⭐ 295
   Gemini-MCP is an MCP server that encapsulates Google's Gemini CLI tool into a standard MCP protocol interface, enabling Claude Code to invoke Gemini for AI-assisted programming tasks.

1344. **[consult7](https://github.com/szeider/consult7)** - ⭐ 295
   MCP server to consult a language model with large context size

1345. **[utcp-specification](https://github.com/universal-tool-calling-protocol/utcp-specification)** - ⭐ 295
   The specification for the Universal Tool Calling Protocol

1346. **[perplexity-mcp](https://github.com/DaInfernalCoder/perplexity-mcp)** - ⭐ 294
   A Model Context Protocol (MCP) server for research and documentation assistance using Perplexity AI. Won 1st @ Cline Hackathon

1347. **[AetherLink](https://github.com/1600822305/AetherLink)** - ⭐ 293
   AetherLink is a cross-platform AI assistant application that supports multiple mainstream AI models (OpenAI, Google Gemini, Anthropic Claude, Grok, etc.). Built with React, TypeScript, and Capacitor, it delivers a seamless conversational experience. Key features include customizable model configurations, multi-topic chat management, AI reasoning vi

1348. **[rosetta](https://github.com/griddynamics/rosetta)** - ⭐ 293
   Meta-prompting, context engineering, and centralized instructions management for AI coding agents

1349. **[ticktick-mcp](https://github.com/jacepark12/ticktick-mcp)** - ⭐ 292
   MCP server that interacts with TickTick (Dida 365) via the TickTick Open API

1350. **[remote-mcp-server-with-auth](https://github.com/coleam00/remote-mcp-server-with-auth)** - ⭐ 291
   Template for a remote MCP server with GitHub OAuth - following best practices for building MCP servers so you can take this as a starting point for any MCP server you want to build!

1351. **[CoWork-OS](https://github.com/CoWork-OS/CoWork-OS)** - ⭐ 291
   Local-first personal agentic OS and everything app for coding, knowledge work, web design, automations, and artifacts.

1352. **[claudit-sec](https://github.com/HarmonicSecurity/claudit-sec)** - ⭐ 291
   Security audit tool for Claude Desktop and Claude Code on macOS — single-command visibility into MCP servers, extensions, plugins, connectors, scheduled tasks, and permissions.

1353. **[lets-learn-mcp-csharp](https://github.com/microsoft/lets-learn-mcp-csharp)** - ⭐ 291

1354. **[mcp](https://github.com/Snowflake-Labs/mcp)** - ⭐ 291
   MCP Server for Snowflake including Cortex AI, object management, SQL orchestration, semantic view consumption, and more

1355. **[blender-mcp-vxai](https://github.com/VxASI/blender-mcp-vxai)** - ⭐ 291

1356. **[copilot-plugins](https://github.com/github/copilot-plugins)** - ⭐ 290
   The official GitHub Copilot plugins collection — MCP servers, skills, hooks, and other extensibility tools for GitHub Copilot.

1357. **[AEnvironment](https://github.com/inclusionAI/AEnvironment)** - ⭐ 290
   Standardized environment infrastructure for Agentic AI development.

1358. **[sketchup-mcp](https://github.com/mhyrr/sketchup-mcp)** - ⭐ 290
   Sketchup Model Context Protocol

1359. **[tableau-mcp](https://github.com/tableau/tableau-mcp)** - ⭐ 290
   Tableau's official MCP Server. Helping Agents see and understand data.

1360. **[zapier-mcp](https://github.com/zapier/zapier-mcp)** - ⭐ 290
   Connect your AI to thousands of apps with the Model Context Protocol.

1361. **[flutter-skill](https://github.com/ai-dashboad/flutter-skill)** - ⭐ 289
   AI-powered E2E testing for 10 platforms. 253 MCP tools. Zero config. Works with Claude, Cursor, Windsurf, Copilot. Test Flutter, React Native, iOS, Android, Web, Electron, Tauri, KMP, .NET MAUI — all from natural language.

1362. **[apollo-mcp-server](https://github.com/apollographql/apollo-mcp-server)** - ⭐ 289
   Apollo MCP Server

1363. **[reddit-mcp](https://github.com/Arindam200/reddit-mcp)** - ⭐ 289
   Model Context Protocol server implementation for Reddit

1364. **[elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server)** - ⭐ 289
   A Model Context Protocol (MCP) server implementation that provides Elasticsearch and OpenSearch interaction.

1365. **[cpp-mcp](https://github.com/hkr04/cpp-mcp)** - ⭐ 289
   Lightweight C++ MCP (Model Context Protocol) SDK

1366. **[harnss](https://github.com/OpenSource03/harnss)** - ⭐ 289
   Open-source, desktop client/UI build to harness Claude Code, Codex and any other Agent accepting Agent Client Protocol. Run multiple AI coding agents side by side with rich tool visualization, MCP integrations, built-in terminal, git, browser and just about anything else you may need.

1367. **[daan](https://github.com/pluveto/daan)** - ⭐ 289
   ✨Lightweight LLM Client with MCP 🔌 & Characters 👤

1368. **[agent-skills-hub](https://github.com/zhuyansen/agent-skills-hub)** - ⭐ 289
   Discover and compare open-source Agent Skills, tools & MCP servers — with quality scoring, trending analysis, and automated GitHub sync

1369. **[claude-in-mobile](https://github.com/AlexGladkov/claude-in-mobile)** - ⭐ 288
   MCP server for mobile and desktop automation — Android (via ADB), iOS Simulator (via simctl), and Desktop (Compose Multiplatform). Like Claude in Chrome but for mobile devices and desktop apps

1370. **[dext](https://github.com/cesarliws/dext)** - ⭐ 288
   Dext - Modern Full Stack Framework for Delphi

1371. **[laravel-claude-code-setup](https://github.com/laraben/laravel-claude-code-setup)** - ⭐ 288
   One-command setup for AI-powered Laravel development with Claude Code and MCP servers

1372. **[intervals-mcp-server](https://github.com/mvilanova/intervals-mcp-server)** - ⭐ 288
   Model Context Protocol (MCP) server for connecting Claude and ChatGPT with the Intervals.icu API.

1373. **[tmux-mcp](https://github.com/nickgnd/tmux-mcp)** - ⭐ 288
   A MCP server for our beloved terminal multiplexer tmux.

1374. **[mcp-manager](https://github.com/amxv/mcp-manager)** - ⭐ 287
   simple web ui to manage mcp (model context protocol) servers in the claude app

1375. **[nova-proximity](https://github.com/Nova-Hunting/nova-proximity)** - ⭐ 287
   Nova-Proximity is a MCP and Agent Skills security scanner powered with NOVA

1376. **[meGPT](https://github.com/adrianco/meGPT)** - ⭐ 286
   Code to process many kinds of content by an author into an MCP server

1377. **[o3-search-mcp](https://github.com/yoshiko-pg/o3-search-mcp)** - ⭐ 286
   MCP server for OpenAI o3 web search

1378. **[alfanous](https://github.com/Alfanous-team/alfanous)** - ⭐ 285
   Alfanous is an Arabic search engine API provides the simple and advanced search in Quran , more features and many interfaces...

1379. **[agentseal](https://github.com/getagentseal/agentseal)** - ⭐ 285
   Security toolkit for AI agents. Scan your machine for dangerous skills and MCP configs, monitor for supply chain attacks, test prompt injection resistance, and audit live MCP servers for tool poisoning.

1380. **[Alice](https://github.com/pmbstyle/Alice)** - ⭐ 285
   Alice is a voice-first desktop AI assistant application built with Vue.js, Vite, and Electron. Advanced memory system, function calling, MCP support, optional fully local use, and more.

1381. **[safe-mcp](https://github.com/SAFE-MCP/safe-mcp)** - ⭐ 285
   SAFE-MCP is a comprehensive security framework for documenting and mitigating threats in the AI Agent ecosystem.

1382. **[mcp-server](https://github.com/strands-agents/mcp-server)** - ⭐ 285
   This MCP server provides documentation about Strands Agents to your GenAI tools, so you can use your favorite AI coding assistant to vibe-code Strands Agents.

1383. **[FileScopeMCP](https://github.com/admica/FileScopeMCP)** - ⭐ 284
   Analyzes your codebase identifying important files based on dependency relationships. Generates diagrams and importance scores per file, helping AI assistants understand the codebase. Automatically parses popular programming languages such as Python, C, C++, Rust, Zig, Lua.

1384. **[mcp-logseq](https://github.com/ergut/mcp-logseq)** - ⭐ 284
   MCP server to interact with LogSeq via its Local HTTP API - enabling AI assistants like Claude to seamlessly read, write, and manage your LogSeq graph.

1385. **[capa](https://github.com/infragate/capa)** - ⭐ 284
   One capabilities.yaml wires skills, tools, rules, sub-agents, MCP servers, and plugins into Cursor, Claude Code, Codex, Windsurf, GitHub Copilot, and 30+ other AI coding agents

1386. **[awesome-fintech](https://github.com/moov-io/awesome-fintech)** - ⭐ 284
   A curated collection of open source fintech libraries and resources.

1387. **[claude-modular](https://github.com/oxygen-fragment/claude-modular)** - ⭐ 284
   Production-ready modular Claude Code framework with 30+ commands, token optimization, and MCP server integration. Achieves 2-10x productivity gains through   systematic command organization and hierarchical configuration.

1388. **[domain-check](https://github.com/saidutt46/domain-check)** - ⭐ 284
   Fast, universal domain availability checker - 1,200+ TLDs, pattern generation, RDAP with WHOIS fallback. CLI + Rust library + MCP server for AI agents.

1389. **[mcp-gdrive](https://github.com/isaacphi/mcp-gdrive)** - ⭐ 283
   Model Context Protocol (MCP) Server for reading from Google Drive and editing Google Sheets

1390. **[unity-cli-loop](https://github.com/hatayama/unity-cli-loop)** - ⭐ 282
   Your Unity project's AI autopilot. Compile, test, debug, repeat—until it just works.

1391. **[data-go-mcp-servers](https://github.com/Koomook/data-go-mcp-servers)** - ⭐ 282
   Korea public data portal (data.go.kr) API MCP servers

1392. **[claude-code-organizer](https://github.com/mcpware/claude-code-organizer)** - ⭐ 282
   Dashboard to manage Claude Code memories, configs, and MCP servers — security scanner for tool poisoning, context token budget tracker, duplicate cleanup, scope management. npx @mcpware/claude-code-organizer

1393. **[human-mcp](https://github.com/mrgoonie/human-mcp)** - ⭐ 282
   Bringing Human Capabilities to AI Agents

1394. **[model-context-protocol-resources](https://github.com/cyanheads/model-context-protocol-resources)** - ⭐ 281
   Exploring the Model Context Protocol (MCP) through practical guides, clients, and servers I've built while learning about this new protocol.

1395. **[rust-docs-mcp-server](https://github.com/Govcraft/rust-docs-mcp-server)** - ⭐ 281
   🦀 Prevents outdated Rust code suggestions from AI assistants. This MCP server fetches current crate docs, uses embeddings/LLMs, and provides accurate context via a tool call.

1396. **[DeepWideResearch](https://github.com/PuppyAgent/DeepWideResearch)** - ⭐ 281
   Agentic RAG for any scenario. Customize sources, depth, and width

1397. **[awesome-mcp-servers](https://github.com/PipedreamHQ/awesome-mcp-servers)** - ⭐ 280
   A collection of MCP servers

1398. **[sudocode](https://github.com/sudocode-ai/sudocode)** - ⭐ 280
   Lightweight agent orchestration dev tool that lives in your repo

1399. **[mcp-manager](https://github.com/zueai/mcp-manager)** - ⭐ 280
   simple web ui to manage mcp (model context protocol) servers in the claude app

1400. **[mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server)** - ⭐ 279
   A Model Context Protocol Server for MongoDB

1401. **[metorial-index](https://github.com/metorial/metorial-index)** - ⭐ 279
   Metorial MCP Index - An ever growing list of open source MCP servers 📁 🎉

1402. **[MCP-handle](https://github.com/WeatherPal-AI/MCP-handle)** - ⭐ 278
   MCP integration platforms making AI-Agents developers focusing on their own tasks

1403. **[next-lens](https://github.com/1weiho/next-lens)** - ⭐ 277
   A CLI that scans Next.js routes and provides quick insights from your terminal, web UI, and MCP.

1404. **[api-agent](https://github.com/agoda-com/api-agent)** - ⭐ 277
   Universal MCP server for GraphQL/REST APIs

1405. **[quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** - ⭐ 276
   The QuickBooks MCP Server lets AI assistants access QuickBooks data via a standard interface. It uses the Model Context Protocol to expose QBO features as callable tools, enabling developers to build AI apps that fetch real-time QBO data through MCP.

1406. **[mcp-reasoner](https://github.com/Jacck/mcp-reasoner)** - ⭐ 276
   A systematic reasoning MCP server implementation for Claude Desktop with beam search and thought evaluation.

1407. **[Context-Engine](https://github.com/m1rl0k/Context-Engine)** - ⭐ 276
   Context-Engine MCP - Agentic Context Compression Suite

1408. **[deepcontext-mcp](https://github.com/Wildcard-Official/deepcontext-mcp)** - ⭐ 276
   DeepContext is an MCP server that adds symbol-aware semantic search to Claude Code, Codex CLI, and other agents for faster, smarter context on large codebases.

1409. **[dify-mcp-server](https://github.com/YanxingLiu/dify-mcp-server)** - ⭐ 276
   Model Context Protocol (MCP) Server for dify workflows

1410. **[oreilly-ai-agents](https://github.com/sinanuozdemir/oreilly-ai-agents)** - ⭐ 275
   An introduction to the world of AI Agents

1411. **[flyto-core](https://github.com/flytohub/flyto-core)** - ⭐ 274
   The open-source execution engine for AI agents. 412 modules, MCP-native, triggers, queue, versioning, metering.

1412. **[ultra-mcp](https://github.com/RealMikeChong/ultra-mcp)** - ⭐ 274
   100x Your Claude Code, Gemini CLI, Cursor and/or any coding tools with MCP client support

1413. **[DashClaw](https://github.com/ucsandman/DashClaw)** - ⭐ 274
   🛡️The governance runtime for AI agents. Intercept actions, enforce guard policies, require approvals, and produce audit-ready decision trails.

1414. **[AdStrike](https://github.com/capture0x/AdStrike)** - ⭐ 273
   AI-powered modular Active Directory red-team framework for authorized penetration testing, AD enumeration, attack-path analysis,   Kerberos/ADCS workflows, reporting, operator automation, and MCP server integration.

1415. **[hevy-mcp](https://github.com/chrisdoc/hevy-mcp)** - ⭐ 271
   Manage your Hevy workouts, routines, folders, and exercise templates. Create and update sessions faster, organize plans, and search exercises to build workouts quickly. Stay synced with changes so your training log is always up to date.

1416. **[ida-multi-mcp](https://github.com/MeroZemory/ida-multi-mcp)** - ⭐ 271
   Multi-instance IDA Pro MCP server — analyze multiple binaries simultaneously through a single MCP endpoint.

1417. **[proximity](https://github.com/Nova-Hunting/proximity)** - ⭐ 271
   Proximity is a MCP security scanner powered with NOVA

1418. **[jinni](https://github.com/smat-dev/jinni)** - ⭐ 271
   Bring your project into LLM context - tool and MCP server

1419. **[Godot-MCP-Native](https://github.com/yurineko73/Godot-MCP-Native)** - ⭐ 271
   一款支持godot开源引擎的的mcp插件，支持常见godot引擎操作，使用Godot原生实现MCPServer，无需安装依赖，开箱即用，支持多种AI工具调用。An MCP plugin that supports the open-source Godot engine, enabling common Godot engine operations. It implements the MCP Server using Godot's native HTTP, requires no dependency installation, is ready to use out of the box, and supports invocation by various AI tools.

1420. **[claude-ai-mcp](https://github.com/anthropics/claude-ai-mcp)** - ⭐ 270
   Report issues related to MCP integration with Claude here.

1421. **[BitFun](https://github.com/GCWing/BitFun)** - ⭐ 270
   BitFun is an Agentic Development Environment (ADE，AI IDE) featuring a cutting-edge Code Agent system with four modes — Agentic, Plan, Debug, and Review. Extensible via MCP, Skills, custom Agents and Rules. Built with Rust + TypeScript for an ultra-lightweight, fluid cross-platform experience.

1422. **[vibing-steampunk](https://github.com/oisee/vibing-steampunk)** - ⭐ 270
   vs-punk: ADT to MCP bridge - Vibe code in ABAP / AMDP

1423. **[OpenCode-Everything-You-Need-to-Know](https://github.com/wesammustafa/OpenCode-Everything-You-Need-to-Know)** - ⭐ 270
   The ultimate all-in-one guide to mastering OpenCode. From installation, Zen model router setup, TUI mastery, commands, skills, agents, workflows, automation, and integrations, to MCP servers, plugins, packed with step-by-step tutorials, real-world examples, and expert strategies to make this the global go-to repo for OpenCode mastery.

1424. **[proximity](https://github.com/fr0gger/proximity)** - ⭐ 269
   Proximity is a MCP security scanner powered with NOVA

1425. **[openapi-to-mcpserver](https://github.com/higress-group/openapi-to-mcpserver)** - ⭐ 268
   A tool&lib that can automatically convert OpenAPI documents into Higress remote MCP server configurations.

1426. **[mcp-openapi-server](https://github.com/ivo-toby/mcp-openapi-server)** - ⭐ 268
   MCP Server (Model Context Protocol) for turning OpenAPI specifications into a MCP Resource

1427. **[osp_marketing_tools](https://github.com/open-strategy-partners/osp_marketing_tools)** - ⭐ 267
   A Model Context Protocol (MCP) server that empowers LLMs to use some of Open Srategy Partners' core writing and product marketing techniques.

1428. **[g-search-mcp](https://github.com/jae-jae/g-search-mcp)** - ⭐ 266
   A powerful MCP server for Google search that enables parallel searching with multiple keywords simultaneously.

1429. **[kite-mcp-server](https://github.com/zerodha/kite-mcp-server)** - ⭐ 266
   Zerodha Kite MCP server

1430. **[xiaozhi-client](https://github.com/shenjingnan/xiaozhi-client)** - ⭐ 265
   小智AI客户端，目前主要用于MCP的对接

1431. **[enterprise-mcp-course](https://github.com/decodingai-magazine/enterprise-mcp-course)** - ⭐ 264
   Learn to build from scratch an AI PR reviewer integrated with GitHub, Slack and Asana that scales within your organization.

1432. **[project-nova](https://github.com/dujonwalker/project-nova)** - ⭐ 264
   A multi-agent AI architecture that connects 25+ specialized agents through n8n and MCP servers. Project NOVA routes requests to domain-specific experts, enabling control of applications from knowledge bases to DAWs, home automation to development tools. Includes system prompts, Dockerfiles, and workflows for a complete AI assistant ecosystem.

1433. **[mcp-proxy](https://github.com/punkpeye/mcp-proxy)** - ⭐ 264
   A TypeScript streamable HTTP and SSE proxy for MCP servers that use stdio transport.

1434. **[godot-mcp](https://github.com/tugcantopaloglu/godot-mcp)** - ⭐ 264
   MCP server for full Godot 4.x engine control — 149 tools for AI-driven game development

1435. **[vulnerable-mcp-servers-lab](https://github.com/appsecco/vulnerable-mcp-servers-lab)** - ⭐ 263
   A collection of servers which are deliberately vulnerable to learn Pentesting MCP Servers.

1436. **[nextcloud-mcp-server](https://github.com/cbcoutinho/nextcloud-mcp-server)** - ⭐ 263
   Nextcloud MCP Server

1437. **[servicenow-mcp](https://github.com/echelon-ai-labs/servicenow-mcp)** - ⭐ 262
   MCP Server for ServiceNow

1438. **[awesome-claude](https://github.com/JSONbored/awesome-claude)** - ⭐ 262
   HeyClaude is a curated registry and distribution surface for Claude and AI-workflow assets: agents, MCP servers, skills, commands, hooks, rules, guides, tools, jobs, Raycast feeds, static data exports, and an npm MCP package.

1439. **[mastergo-magic-mcp](https://github.com/mastergo-design/mastergo-magic-mcp)** - ⭐ 262
   MasterGo Magic MCP is a standalone MCP (Model Context Protocol) service designed to connect MasterGo design tools with AI models.

1440. **[pctx](https://github.com/portofcontext/pctx)** - ⭐ 262
   pctx is the execution layer for agentic tool calls. It auto-converts agent tools and MCP servers into code that runs in secure sandboxes for token-efficient workflows.

1441. **[mcp-servers-nix](https://github.com/natsukium/mcp-servers-nix)** - ⭐ 261
   A Nix-based configuration framework for Model Control Protocol (MCP) servers with ready-to-use packages.

1442. **[wikipedia-mcp](https://github.com/Rudra-ravi/wikipedia-mcp)** - ⭐ 261
   A Model Context Protocol (MCP) server that retrieves information from Wikipedia to provide context to LLMs.

1443. **[erickwendel-contributions-mcp](https://github.com/ErickWendel/erickwendel-contributions-mcp)** - ⭐ 260
   A Model Context Protocol (MCP) server that provides tools to query Erick Wendel's contributions across different platforms

1444. **[camoufox-reverse-mcp](https://github.com/WhiteNightShadow/camoufox-reverse-mcp)** - ⭐ 260
   🔧 反检测浏览器 MCP Server | 35 个 JS 逆向工具 + C++ 引擎层 JSVMP 指纹追踪

1445. **[unity-mcp-server](https://github.com/AnkleBreaker-Studio/unity-mcp-server)** - ⭐ 259
   Unity MCP Server — 268 tools for AI-assisted game development. Connect Claude, Cursor, or any MCP client to Unity Editor & Unity Hub. Scene management, GameObjects, components, builds, profiling, Shader Graph, Amplify, terrain, physics, NavMesh, animation, MPPM multiplayer & more. Free & open source by AnkleBreaker Studio.

1446. **[Mimir](https://github.com/orneryd/Mimir)** - ⭐ 259
   Mimir - Fully open and customizable memory bank with semantic vector search capabilities for locally indexed files (Code Intelligence) and stored memories that are shared across sessions and chat contexts allowing worker agent to learn from errors in past runs. Includes Drag and Drop multi-agent orchestration

1447. **[codeindex](https://github.com/scheidydude/codeindex)** - ⭐ 259
   Repo dependency analyzer with **blast-radius impact scoring** for AI-assisted development.

1448. **[STS2-Agent](https://github.com/CharTyr/STS2-Agent)** - ⭐ 258
   杀戮尖塔2的MOD，将杀戮尖塔2的游戏状态与操作暴露为本地 HTTP API 包装成 MCP Server，供支持 MCP 的AI客户端直接调用

1449. **[corpusos](https://github.com/Corpus-OS/corpusos)** - ⭐ 258
   Open-source protocol suite standardizing LLM, Vector, Graph, and Embedding infrastructure across LangChain, LlamaIndex, AutoGen, CrewAI, Semantic Kernel, and MCP. 3,330+ conformance tests. One protocol. Any framework. Any provider.

1450. **[agentrove](https://github.com/Mng-dev-ai/agentrove)** - ⭐ 258
   Your own Claude Code UI, sandbox, in-browser VS Code, terminal, multi-provider support (Anthropic, OpenAI, GitHub Copilot, OpenRouter), custom skills, and MCP servers.

1451. **[mcp](https://github.com/neo4j/mcp)** - ⭐ 257
   Neo4j official MCP Server

1452. **[api200](https://github.com/API-200/api200)** - ⭐ 256
   API 200 is an open source API gateway to simplify 3rd-party integrations. Import endpoints, set up caching, retries, and mocks. Access all services via one URL. Monitor logs, track errors, and get alerts on API incidents.

1453. **[swiss-ai-call-agent](https://github.com/Chrissotino/swiss-ai-call-agent)** - ⭐ 256
   Enterprise-grade AI Call Agent for the Swiss market – inbound & outbound calls, multilingual (DE/FR/IT), MCP architecture, Claude AI decision engine, real-time dashboard

1454. **[postman-mcp-server](https://github.com/postmanlabs/postman-mcp-server)** - ⭐ 256
   Connect your AI to your APIs on Postman

1455. **[mcp-server-gemini](https://github.com/aliargun/mcp-server-gemini)** - ⭐ 255
   MCP server implementation for Google's Gemini API

1456. **[agent-craft](https://github.com/Annyfee/agent-craft)** - ⭐ 255
   AI Agent 教学仓库 | 系统化 LangChain、RAG、LangGraph、MCP 全栈实战代码 | 万字博客详解 | 开源可运行示例 | 从零构建智能体

1457. **[Claude-Skills](https://github.com/borghei/Claude-Skills)** - ⭐ 255
   338 AI skills across 16 domains. PM is the deepest (66 skills — discovery, execution, strategy frameworks, GTM, Jira/Linear/Notion). Plus engineering, marketing, C-level (CAIO/CDO/CCO/GC/VPE), compliance + audit-prep, new research/ domain, vertical advisors. 74 expert agents, 784+ stdlib Python tools. 11 AI assistants.

1458. **[agentregistry](https://github.com/agentregistry-dev/agentregistry)** - ⭐ 254
   Fast-track AI innovation with a centralized, trusted, curated registry

1459. **[code-reasoning](https://github.com/mettamatt/code-reasoning)** - ⭐ 254
   A code reasoning MCP server, a fork of sequential-thinking

1460. **[a2a-directory](https://github.com/sing1ee/a2a-directory)** - ⭐ 254
   Agent2Agent (A2A) – AgentCards, Servers, Clients, Docs

1461. **[awesome-osint-mcp-servers](https://github.com/soxoj/awesome-osint-mcp-servers)** - ⭐ 254
   🔌 A curated list of OSINT MCP servers. Pull requests are welcomed!

1462. **[mcp-trends-hub](https://github.com/baranwang/mcp-trends-hub)** - ⭐ 253
   基于 Model Context Protocol (MCP) 协议的全网热点趋势一站式聚合服务

1463. **[c2sagent](https://github.com/C2SAgent/c2sagent)** - ⭐ 253
   C2S Agent is an lightweight AI Agent construction platform that provides configurable online Agents and MCP services, You can configure any HTTP request interface as an MCP tool. C2S Agent 是一个轻量级的AI Agent构建平台，提供在线可配置的Agent，MCP，您可以一个HTTP请求的接口配置成为一个MCP工具，Agent之间可以进行自交流。并提供了单端口多A2A服务，MCP服务的解决方案

1464. **[admin](https://github.com/decocms/admin)** - ⭐ 253
   Define and compose secure MCPs in TypeScript. Generate AI workflows and agents with React + Tailwind UI. Deploy anywhere.

1465. **[claude-config-editor](https://github.com/gagarinyury/claude-config-editor)** - ⭐ 253
   Claude Config Editor is a lightweight web tool that helps you clean and optimize your Claude Code/Desktop config files (.claude.json). Analyze project sizes, bulk delete chat histories, export data for backup, manage servers visually, and speed up Claude—all locally, with auto-backup, no dependencies, and cross-platform support.

1466. **[lokka](https://github.com/merill/lokka)** - ⭐ 253
   MCP (Model Context Protocol) for Microsoft 365. Includes support for Microsoft Graph and other services

1467. **[mcpproxy-go](https://github.com/smart-mcp-proxy/mcpproxy-go)** - ⭐ 253
   Supercharge AI Agents, Safely

1468. **[mcpfusion](https://github.com/vinkius-labs/mcpfusion)** - ⭐ 253
   MCP Fusion - The TypeScript framework for secure MCP servers.

1469. **[mcp-email-server](https://github.com/ai-zerolab/mcp-email-server)** - ⭐ 252
   IMAP and SMTP via MCP Server

1470. **[aci-mcp](https://github.com/aipotheosis-labs/aci-mcp)** - ⭐ 252
   MCP server(s) for Aipolabs ACI.dev

1471. **[mcp-dev-latam](https://github.com/codespar/mcp-dev-latam)** - ⭐ 252
   MCP servers for Brazilian services — payments, fiscal, banking, communication. Generated by CodeSpar.

1472. **[deeppowers](https://github.com/deeppowers/deeppowers)** - ⭐ 252
   DEEPPOWERS is a Fully Homomorphic Encryption (FHE) framework built for MCP (Model Context Protocol), aiming to provide end-to-end privacy protection and high-efficiency computation for the upstream and downstream ecosystem of the MCP protocol.

1473. **[hydra-mcp-solana](https://github.com/hydra-mcp/hydra-mcp-solana)** - ⭐ 252
   hydra-ai

1474. **[Claude-Code-AI-Design](https://github.com/Julpygo/Claude-Code-AI-Design)** - ⭐ 252
   Claude Design Anthropic Tool Download April 2026 Figma to Code AI Agent Research Preview Claude Code CLI Integration React 19 Tailwind v4 Support Model Context Protocol MCP Server Setup Design Systems Automation UI UX Prototyping Next.js Component Generation Best Developer Tools 2026 Free Tutorial

1475. **[mcp-chatbot](https://github.com/3choff/mcp-chatbot)** - ⭐ 251
   A simple CLI chatbot that demonstrates the integration of the Model Context Protocol (MCP).

1476. **[notebooklm-skill](https://github.com/claude-world/notebooklm-skill)** - ⭐ 251
   NotebookLM does the research, Claude writes the content. Research → Synthesis → Content Creation → Publishing. Claude Code Skill + MCP Server.

1477. **[Charles-mcp](https://github.com/heizaheiza/Charles-mcp)** - ⭐ 251
   Charles Proxy MCP server for AI agents with live capture, structured traffic analysis, and agent-friendly tool contracts

1478. **[mcp2py](https://github.com/MaximeRivest/mcp2py)** - ⭐ 251
   Turn any MCP server into a Python module

1479. **[moor](https://github.com/varandrew/moor)** - ⭐ 251
   Moor is a local MCP control plane for Mac. It gives every coding agent one safe, observable, configurable gateway to your MCP servers.

1480. **[vurb.ts](https://github.com/vinkius-labs/vurb.ts)** - ⭐ 251
   TypeScript framework for building production MCP servers. Fluent tool API, FSM gating, presenters, semantic routing, cache hints, Zod validation. Model-View-Agent architecture for the Model Context Protocol.

1481. **[AgentRecall](https://github.com/Goldentrii/AgentRecall)** - ⭐ 250
   AI Session Memory with Think-Execute-Reflect Quality Loops — give your agent a brain that survives every session. Built on the Intelligent Distance principle.

1482. **[photoshop-python-api-mcp-server](https://github.com/loonghao/photoshop-python-api-mcp-server)** - ⭐ 250
   A Model Context Protocol (MCP) server that interfaces with Adobe Photoshop's Python API. Enables LLMs to execute image editing operations, automate workflows, and manage Photoshop tasks through structured commands and context-aware interactions.

1483. **[mcp-foundry](https://github.com/microsoft-foundry/mcp-foundry)** - ⭐ 250
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

1484. **[foundry-mcp-server](https://github.com/PraneshASP/foundry-mcp-server)** - ⭐ 250
   An experimental MCP Server for foundry built for Solidity devs

1485. **[VibeUE](https://github.com/kevinpbuckley/VibeUE)** - ⭐ 249
   Unreal Engine Vibe Coding tool

1486. **[LycheeMem](https://github.com/LycheeMem/LycheeMem)** - ⭐ 249
   Lightweight Long-Term Memory for LLM Agents.

1487. **[radare2-mcp](https://github.com/radareorg/radare2-mcp)** - ⭐ 249
   MCP stdio server for radare2

1488. **[monarch-mcp-server](https://github.com/robcerda/monarch-mcp-server)** - ⭐ 249
   MCP Server for use with Monarch Money

1489. **[forgetful](https://github.com/ScottRBK/forgetful)** - ⭐ 249
   Opensource Memory for Agents

1490. **[call.md](https://github.com/video-db/call.md)** - ⭐ 249
   Turn meetings into live agent loops. Record, transcribe, and analyze meetings with real-time AI intelligence — before, during, and after calls.

1491. **[video-editing-mcp](https://github.com/burningion/video-editing-mcp)** - ⭐ 248
   MCP Interface for Video Jungle

1492. **[mcp-telegram](https://github.com/dryeab/mcp-telegram)** - ⭐ 248
   MCP Server for Telegram

1493. **[JoySafeter](https://github.com/jd-opensource/JoySafeter)** - ⭐ 248
   🚀 JoySafeter: An enterprise AI Agent Platform—Not just chatting. building、running、testing, and tracing autonomous Agent Teams with visual orchestration...

1494. **[mcp_chatbot](https://github.com/keli-wen/mcp_chatbot)** - ⭐ 248
   A chatbot implementation compatible with MCP (terminal / streamlit supported)

1495. **[MoltBrain](https://github.com/nhevers/MoltBrain)** - ⭐ 248
   Long-term memory layer for OpenClaw & MoltBook agents that learns and recalls your project context automatically.

1496. **[trading_skills](https://github.com/staskh/trading_skills)** - ⭐ 248
   Claude powered advisor system for option traders

1497. **[dat](https://github.com/hexinfo/dat)** - ⭐ 247
   Asking yours data in a natural language way through pre-modeling (data models and semantic models).

1498. **[hf-mcp-server](https://github.com/huggingface/hf-mcp-server)** - ⭐ 247
   Hugging Face MCP Server

1499. **[MCPBench](https://github.com/modelscope/MCPBench)** - ⭐ 247
   The evaluation benchmark on MCP servers

1500. **[claude-recall](https://github.com/nhevers/claude-recall)** - ⭐ 247
   Long-term memory layer for MoltBot & Claude Code that learns and recalls your project context automatically

1501. **[suppr-mcp](https://github.com/WildDataX/suppr-mcp)** - ⭐ 247
    超能文献|AI驱动的文档翻译与学术搜索服务。支持PDF、DOCX、PPTX等多格式文档的高质量翻译（支持11种语言），特别优化了数学公式翻译。同时提供PubMed学术文献智能搜索功能。更多访问：https://suppr.wilddata.cn

1502. **[pasal](https://github.com/ilhamfp/pasal)** - ⭐ 246
   Pasal.id - The first open, AI-native Indonesian legal platform. MCP server + REST API + web app giving AI grounded access Indonesian laws.

1503. **[yt-dlp-mcp](https://github.com/kevinwatt/yt-dlp-mcp)** - ⭐ 246
   A Model Context Protocol (MCP) server that bridges Video & Audio content with Large Language Models using yt-dlp.

1504. **[Google-Research-MCP](https://github.com/mixelpixx/Google-Research-MCP)** - ⭐ 246
   MCP Server built for use with Claude Code, Claude Desktop, VS Code, Cline  - enable google search and ability to follow links and research websites

1505. **[gram](https://github.com/speakeasy-api/gram)** - ⭐ 246
   Securely scale AI usage across your organization.  Control plane for building, securing and monitoring your agents, mcp and skills.

1506. **[mysql_mcp_server_pro](https://github.com/wenb1n-dev/mysql_mcp_server_pro)** - ⭐ 246
   Model Context Protocol (MCP) server that supports secure interaction with MySQL databases and has anomaly analysis capabilities.更加牛逼！更加好用！不仅止于mysql的增删改查功能； 还包含了数据库异常分析能力；且便于开发者们进行个性化的工具扩展

1507. **[weather-mcp-server](https://github.com/ezh0v/weather-mcp-server)** - ⭐ 245
   A lightweight Model Context Protocol (MCP) server that enables AI assistants like Claude to retrieve and interpret real-time weather data. Discuss on Hacker News:

1508. **[firebase-mcp](https://github.com/gannonh/firebase-mcp)** - ⭐ 245
   🔥 Model Context Protocol (MCP) server for Firebase.

1509. **[mcp-prompt-server](https://github.com/gdli6177/mcp-prompt-server)** - ⭐ 245
   这是一个基于Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地使用。

1510. **[claude_code-gemini-mcp](https://github.com/RaiAnsar/claude_code-gemini-mcp)** - ⭐ 245
   Simplified Gemini for Claude Code.

1511. **[YourMemory](https://github.com/sachitrafa/YourMemory)** - ⭐ 245
   Agentic AI memory with Ebbinghaus forgetting curve decay. +16pp better recall than Mem0 on LoCoMo.

1512. **[synapse-ai](https://github.com/synapseorch-ai/synapse-ai)** - ⭐ 245
   Build AI agents that actually do things. Synapse is an open-source platform for creating, connecting, and orchestrating AI agents powered by any LLM — local, cloud or CLIs.

1513. **[Windows-MCP.Net](https://github.com/AIDotNet/Windows-MCP.Net)** - ⭐ 244
   A .NET-based Windows desktop automation MCP (Model Context Protocol) server that provides AI assistants with the ability to interact with the Windows desktop environment.

1514. **[mcp-ssh-manager](https://github.com/bvisible/mcp-ssh-manager)** - ⭐ 244
   MCP SSH Server: 37 tools for remote SSH management | Claude Code & OpenAI Codex | DevOps automation, backups, database operations, health monitoring

1515. **[mcp-todoist](https://github.com/greirson/mcp-todoist)** - ⭐ 244
   MCP server that connects Claude to Todoist for natural language task and project   management with bulk operations

1516. **[mcp-compass](https://github.com/liuyoshio/mcp-compass)** - ⭐ 244
   MCP Discovery & Recommendation Service - Find the right MCP server for your needs

1517. **[embodied-claude](https://github.com/lifemate-ai/embodied-claude)** - ⭐ 243
   Claudeに身体性を与えるMCP群

1518. **[readwise-skills](https://github.com/readwiseio/readwise-skills)** - ⭐ 243
   Agent skills for your Readwise and Reader data, powered by the Readwise MCP server/CLI.  Triage your inbox, quiz yourself on what you've read, build a personalized now-reading page, and more.

1519. **[linux-mcp-server](https://github.com/rhel-lightspeed/linux-mcp-server)** - ⭐ 243
   Tools to allow LLM clients to interact with Linux systems remotely

1520. **[mcp-maigret](https://github.com/w0h1v/mcp-maigret)** - ⭐ 243
   MCP server for maigret, a powerful OSINT tool that collects user account information from various public sources.

1521. **[mcp-maigret](https://github.com/BurtTheCoder/mcp-maigret)** - ⭐ 242
   MCP server for maigret, a powerful OSINT tool that collects user account information from various public sources.

1522. **[omnicoreagent](https://github.com/omnirexflora-labs/omnicoreagent)** - ⭐ 242
   Open Python agent harness for production AI apps: tools, MCP, memory, workspace, telemetry, subagents, background tasks, and OmniServe APIs.

1523. **[chat-mcp](https://github.com/AI-QL/chat-mcp)** - ⭐ 241
   A Desktop Chat App that leverages MCP(Model Context Protocol) to interface with other LLMs.

1524. **[ha-mcp-for-xiaozhi](https://github.com/c1pher-cn/ha-mcp-for-xiaozhi)** - ⭐ 241
   Homeassistant MCP server for 小智AI

1525. **[mcp-server-code-runner](https://github.com/formulahendry/mcp-server-code-runner)** - ⭐ 241
   Code Runner MCP Server

1526. **[figma-mcp-bridge](https://github.com/gethopp/figma-mcp-bridge)** - ⭐ 241
   Figma Plugin & MCP server to bypass API limits

1527. **[mcp-echarts](https://github.com/hustcc/mcp-echarts)** - ⭐ 241
   🧬 Generate visual charts using ECharts with AI MCP dynamically, used for chart generation and data analysis.

1528. **[plane-mcp-server](https://github.com/makeplane/plane-mcp-server)** - ⭐ 241
   Plane's Official Model Context Protocol Server 🔌 ⌨️ 🔥

1529. **[anki-mcp-server](https://github.com/nailuoGG/anki-mcp-server)** - ⭐ 241
   MCP server for Anki via AnkiConnect

1530. **[QuickDesk](https://github.com/barry-ran/QuickDesk)** - ⭐ 240
   QuickDesk is the first AI-native remote desktop — an open-source, free application with a built-in MCP (Model Context Protocol) Server that lets any AI agent see and control remote computers.

1531. **[jebmcp](https://github.com/flankerhqd/jebmcp)** - ⭐ 240

1532. **[mcp-engine-public](https://github.com/maxanatsko/mcp-engine-public)** - ⭐ 240
   The SemanticOps MCP (formerly MCP Engine) is a Power BI tool that lets AI assistants like Claude interact with your Power BI models programmatically: read your model structure, run DAX queries, modify your semantic model, and perform advanced analytics - all through natural conversation.

1533. **[claude-code-mcpinstall](https://github.com/undeadpickle/claude-code-mcpinstall)** - ⭐ 240
   Easy guide to installing Claude Code MCPs globally on your machine.

1534. **[sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers)** - ⭐ 239
   Sample implementations of AI Agents and MCP Servers running on AWS Serverless compute

1535. **[playwright-mcp](https://github.com/cloudflare/playwright-mcp)** - ⭐ 239
   Playwright MCP fork that works with Cloudflare Browser Rendering

1536. **[PIXRA](https://github.com/dodufish/PIXRA)** - ⭐ 239
   Pixelize the real world on-chain

1537. **[mcp-feedback-collector](https://github.com/sanshao85/mcp-feedback-collector)** - ⭐ 239
   一个现代化的 Model Context Protocol (MCP) 服务器，为AI助手提供交互式用户反馈收集功能。

1538. **[remote-swe-agents](https://github.com/aws-samples/remote-swe-agents)** - ⭐ 238
   Autonomous SWE agent working in the cloud!

1539. **[MCP-connect](https://github.com/EvalsOne/MCP-connect)** - ⭐ 238
   Enables cloud-based AI services to access local Stdio based MCP servers via HTTP requests

1540. **[mcp-on-vercel](https://github.com/vercel-labs/mcp-on-vercel)** - ⭐ 238

1541. **[antd-components-mcp](https://github.com/zhixiaoqiang/antd-components-mcp)** - ⭐ 238
   An MCP service for Ant Design components query | 一个减少 Ant Design 组件代码生成幻觉的 MCP 服务，包含系统提示词、组件文档、API 文档、代码示例和更新日志查询

1542. **[Google-Search-MCP-Server](https://github.com/mixelpixx/Google-Search-MCP-Server)** - ⭐ 237
   MCP Server built for use with Claude Code, Claude Desktop, VS Code, Cline  - enable google search and ability to follow links and research websites

1543. **[facebook-ads-library-mcp](https://github.com/proxy-intell/facebook-ads-library-mcp)** - ⭐ 237
   MCP Server for Facebook ADs Library - Get instant answers from FB's ad library

1544. **[ai-code-interface.el](https://github.com/tninja/ai-code-interface.el)** - ⭐ 237
   Unified Emacs interface supporting OpenAI Codex, GitHub Copilot CLI, Claude Code, Gemini CLI, Opencode, and more

1545. **[cdp-bridge-mcp](https://github.com/Unagi-cq/cdp-bridge-mcp)** - ⭐ 237
   MCP server that bridges clients to a real browser through CDP and a companion extension.

1546. **[arcticdb_mcp](https://github.com/YMuskrat/arcticdb_mcp)** - ⭐ 237
   MCP server for ArcticDB

1547. **[NFTIAI](https://github.com/Axarb/NFTIAI)** - ⭐ 236
   NFTI AI — NFTI your AI Agents & Virtual IP. Bridging intelligent agents, MCP protocols, and RWA to create a new era of digital sovereignty.

1548. **[cryptocurrency.cv](https://github.com/nirholas/cryptocurrency.cv)** - ⭐ 236
   Free crypto news API - real-time aggregator for Bitcoin, Ethereum, DeFi, Solana & altcoins. No API key required. RSS/Atom feeds, JSON REST API, historical archive with market context, embeddable widgets, ChatGPT plugin, Claude MCP server, SDKs (Python, TypeScript, Go, React, PHP). AI/LLM ready. Vibe coding friendly. Open source.

1549. **[ruby_llm-mcp](https://github.com/patvice/ruby_llm-mcp)** - ⭐ 236
   Full-featured MCP support for Ruby and RubyLLM—making it easy to build structured, composable LLM workflows in pure Ruby.

1550. **[xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server)** - ⭐ 236
   A Model Context Protocol (MCP) server that enables natural language queries to databases

1551. **[mcp-twikit](https://github.com/adhikasp/mcp-twikit)** - ⭐ 235
   A Model Context Protocol (MCP) server for interacting with Twitter.

1552. **[ai-polymarket-agent](https://github.com/kaktusesquire6rmu/ai-polymarket-agent)** - ⭐ 235
   Enable Claude, ChatGPT, and other AI agents to analyze markets, fetch real-time odds, and execute trades on Polymarket using the Model Context Protocol (MCP).

1553. **[figma-flutter-mcp](https://github.com/mhmzdev/figma-flutter-mcp)** - ⭐ 235
   An MCP server that provides the coding agents Figma's design token to write Flutter code.

1554. **[mcp-server-tauri](https://github.com/hypothesi/mcp-server-tauri)** - ⭐ 234
   A Model Context Protocol (MCP) server and plugin for Tauri v2 development

1555. **[Lambda-MCP-Server](https://github.com/mikegc-aws/Lambda-MCP-Server)** - ⭐ 234
   Creates a simple MCP tool server with "streaming" HTTP.

1556. **[mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server)** - ⭐ 234
   mindmap, mcp server, artifact

1557. **[phone-mcp](https://github.com/hao-cyber/phone-mcp)** - ⭐ 233
   A phone control plugin for MCP that allows you to control your Android phone through ADB commands to connect any human

1558. **[qveris-agent-toolkit](https://github.com/QVerisAI/qveris-agent-toolkit)** - ⭐ 233
   Open-source toolkit for the QVeris capability routing network: CLI, MCP server, Python SDK, skills, and REST API docs for agents to discover, inspect, call, and audit real-world tools.

1559. **[mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus)** - ⭐ 233
   Model Context Protocol Servers for Milvus

1560. **[smart-tree](https://github.com/8b-is/smart-tree)** - ⭐ 232
   Smart Tree: not just a tree, a philosophy. A context-aware, AI-crafted replacement for 20+ tools with MEM8 quantum compression, semantic search, AST-smart editing, and partnership memory. Crafted with care by human + AI—accept no knock-offs.

1561. **[memex](https://github.com/iamtouchskyer/memex)** - ⭐ 232
   Zettelkasten-based persistent memory for AI coding agents. Works with Claude Code, Cursor, VS Code Copilot, Codex, Windsurf & any MCP client. No vector DB — just markdown + git sync.

1562. **[persistent-ai-memory](https://github.com/savantskie/persistent-ai-memory)** - ⭐ 232
   A persistent local memory for AI, LLMs, or Copilot in VS Code.

1563. **[Context-Engineering-for-Multi-Agent-Systems](https://github.com/Denis2054/Context-Engineering-for-Multi-Agent-Systems)** - ⭐ 231
   Save thousands of lines of code by building universal, domain-agnostic Multi-Agent Systems (MAS) through high-level semantic orchestration. This repository provides a production-ready blueprint for the Agentic Era, allowing you to replace rigid, hard-coded workflows with a dynamic transparent Context Engine that provides 100% transparency.

1564. **[composer-trade-mcp](https://github.com/invest-composer/composer-trade-mcp)** - ⭐ 230
   Composer's MCP server lets MCP-enabled LLMs like Claude backtest trading ideas and automatically invest in them for you

1565. **[domainstack.io](https://github.com/jakejarvis/domainstack.io)** - ⭐ 230
   🧰 All-in-one domain name intelligence as a service

1566. **[MaxMSP-MCP-Server](https://github.com/tiianhk/MaxMSP-MCP-Server)** - ⭐ 230
   MCP (Model Context Protocol) Server for Max (Max/MSP/Jitter)

1567. **[StatsPAI](https://github.com/brycewang-stanford/StatsPAI)** - ⭐ 229
   StatsPAI is the first agent-native Python library for causal inference and applied econometrics — unified API, broad cross-method coverage, structured result objects, machine-readable schemas, an MCP server, and R/Stata parity validation.

1568. **[uber-eats-mcp-server](https://github.com/ericzakariasson/uber-eats-mcp-server)** - ⭐ 229

1569. **[MiroRL](https://github.com/MiroMindAI/MiroRL)** - ⭐ 229
   MiroRL is  an MCP-first reinforcement learning framework for deep research agent.

1570. **[penpot-mcp](https://github.com/montevive/penpot-mcp)** - ⭐ 229
   Penpot MCP server

1571. **[zabbix-mcp-server](https://github.com/mpeirone/zabbix-mcp-server)** - ⭐ 228
   🔌 Complete MCP server for Zabbix integration — Connect AI assistants to Zabbix monitoring with a single unified tool covering 100% of Zabbix APIs. Includes read-only mode and documentation tools for seamless exploration of hosts, items, triggers, templates, problems, and more.

1572. **[mermaid-mcp-server](https://github.com/peng-shawn/mermaid-mcp-server)** - ⭐ 228
   A Model Context Protocol (MCP) server that converts Mermaid diagrams to PNG images

1573. **[plate-playground-template](https://github.com/udecode/plate-playground-template)** - ⭐ 228
   Plate AI template with React 19, Next 16, Tailwind 4, MCP.

1574. **[composio](https://github.com/warpdot-dev/composio)** - ⭐ 228
   typescript python sdk ai-agents anthropic openapi langchain openai-agents llamaindex mastra vercel-ai mcp oauth saas llm integrations agent-tools automation cloudflare google-gemini tooling rag multi-provider developer-sdk composable-actions webhook-triggers

1575. **[mcp-foundry](https://github.com/azure-ai-foundry/mcp-foundry)** - ⭐ 227
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

1576. **[ai-counsel](https://github.com/blueman82/ai-counsel)** - ⭐ 227
   True deliberative consensus MCP server where AI models debate and refine positions across multiple rounds

1577. **[mcp-server-commands](https://github.com/g0t4/mcp-server-commands)** - ⭐ 227
   Model Context Protocol server to run commands (tool: `runProcess`)

1578. **[cobolt](https://github.com/platinum-hill/cobolt)** - ⭐ 227
   This is a cross-platform desktop application that allows you to chat with locally hosted LLMs and enjoy features like MCP support

1579. **[ArcRift](https://github.com/Eshaan-Nair/ArcRift)** - ⭐ 226
   Persistent local memory layer for AI. ArcRift uses a Chrome extension and a native MCP server to sync context and decisions from your browser chats (Claude, ChatGPT, DeepSeek) straight to your local IDE agents (Cursor, Claude Code, Windsurf)  powered by a local SQLite knowledge graph.

1580. **[human-in-the-loop](https://github.com/KOBA789/human-in-the-loop)** - ⭐ 226
   An MCP (Model Context Protocol) server that allows AI assistants to ask questions to humans via Discord.

1581. **[mcp-n8n-workflow-builder](https://github.com/salacoste/mcp-n8n-workflow-builder)** - ⭐ 226
   AI-powered n8n workflow automation through natural language. MCP server enabling Claude AI & Cursor IDE to create, manage, and monitor workflows via Model Context Protocol. Multi-instance support, 17 tools, comprehensive docs. Build workflows conversationally without manual JSON editing.

1582. **[DrissionPageMCP](https://github.com/wxhzhwxhzh/DrissionPageMCP)** - ⭐ 226
   基于DrissionPage和FastMCP的浏览器自动化MCP服务器，提供丰富的浏览器操作API供AI调用

1583. **[DeLive](https://github.com/XimilalaXiang/DeLive)** - ⭐ 226
   System audio capture + multi-provider ASR + local-first AI review workspace. Floating live captions, 12 ASR backends, 60+ languages, AI summary/chat/mindmap, Open API, MCP server, and Agent Skill.

1584. **[agent-skills](https://github.com/jdrhyne/agent-skills)** - ⭐ 225
   A collection of AI agent skills for Clawdbot, Claude Code, Codex

1585. **[cli](https://github.com/modelstudioai/cli)** - ⭐ 225
   Official Model Studio CLI（阿里云百炼 CLI）built for AI Agent frameworks, exposing models, search, multimodal, and workflow capabilities as structured tool calls.

1586. **[razorpay-mcp-server](https://github.com/razorpay/razorpay-mcp-server)** - ⭐ 225
   Razorpay's Official MCP Server

1587. **[mcp-server-gsc](https://github.com/ahonn/mcp-server-gsc)** - ⭐ 224
   A Model Context Protocol (MCP) server providing access to Google Search Console

1588. **[claudex](https://github.com/Mng-dev-ai/claudex)** - ⭐ 224
   Your own Claude Code UI, sandbox, in-browser VS Code, terminal, multi-provider support (Anthropic, OpenAI, GitHub Copilot, OpenRouter), custom skills, and MCP servers.

1589. **[skyll](https://github.com/assafelovic/skyll)** - ⭐ 223
   A tool for autonomous agents like OpenClaw to discover and learn skills autonomously

1590. **[google_ads_mcp](https://github.com/google-marketing-solutions/google_ads_mcp)** - ⭐ 223
   The Google Ads MCP Server is an implementation of the Model Context Protocol (MCP) that enables Large Language Models (LLMs), such as Gemini, to interact directly with the Google Ads API.

1591. **[unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server)** - ⭐ 223
   🔎 A MCP server for Unsplash image search.

1592. **[renderdoc-mcp](https://github.com/JiaboLi-GitHub/renderdoc-mcp)** - ⭐ 223
   An MCP server for RenderDoc: Empowering AI assistants to analyze GPU frame captures and debug graphics pipelines.

1593. **[AutoResearch-SibylSystem](https://github.com/Sibyl-Research-Team/AutoResearch-SibylSystem)** - ⭐ 223
   Fully Autonomous AI Research System with Self-Evolution, built natively on Claude Code

1594. **[ATaC](https://github.com/ATaC-team/ATaC)** - ⭐ 222
   Record and Replay AI Agent Trajectories.

1595. **[git-mcp-server](https://github.com/cyanheads/git-mcp-server)** - ⭐ 222
   An MCP (Model Context Protocol) server enabling LLMs and AI agents to interact with Git repositories. Provides tools for comprehensive Git operations including clone, commit, branch, diff, log, status, push, pull, merge, rebase, worktree, tag management, and more, via the MCP standard. STDIO & HTTP.

1596. **[ClaudeR](https://github.com/IMNMV/ClaudeR)** - ⭐ 222
   Connect RStudio to Claude Code, Codex, Gemini, and other LLM agents via MCP. Multi-agent orchestration, automated manuscript   auditing, and zero-config setup with uvx

1597. **[blockbench-mcp-plugin](https://github.com/jasonjgardner/blockbench-mcp-plugin)** - ⭐ 222
   Adds MCP server to Blockbench

1598. **[langgraph-whatsapp-agent](https://github.com/lgesuellip/langgraph-whatsapp-agent)** - ⭐ 222
   A template for building WhatsApp agents using LangGraph and Twilio. This project enables you to deploy AI agents that interact with users via WhatsApp, process messages and images, and invoke custom graph-based agents. It integrates with MCP and runs on the LangGraph Platform.

1599. **[learn-agentic-ai-from-low-code-to-code](https://github.com/panaversity/learn-agentic-ai-from-low-code-to-code)** - ⭐ 222
   Build production-grade agents with OpenAI AgentKit, a no-code platfrom.

1600. **[llamacloud-mcp](https://github.com/run-llama/llamacloud-mcp)** - ⭐ 222

1601. **[Windows-MCP.Net](https://github.com/shuyu-labs/Windows-MCP.Net)** - ⭐ 222
   A .NET-based Windows desktop automation MCP (Model Context Protocol) server that provides AI assistants with the ability to interact with the Windows desktop environment.

1602. **[effect-mcp](https://github.com/tim-smart/effect-mcp)** - ⭐ 222

1603. **[image-gen-server](https://github.com/fengin/image-gen-server)** - ⭐ 221
   一个能与Cursor集成的图片生成mcp server工具，实现调用即梦逆向接口

1604. **[agent-mcp-lab](https://github.com/WaveSpeedAI/agent-mcp-lab)** - ⭐ 221

1605. **[mcp-dev-brasil](https://github.com/codespar/mcp-dev-brasil)** - ⭐ 219
   MCP servers for Brazilian services — payments, fiscal, banking, communication. Generated by CodeSpar.

1606. **[home-assistant-cursor-agent](https://github.com/Coolver/home-assistant-cursor-agent)** - ⭐ 219
   Enable Cursor AI, VS Code, or any MCP-enabled IDE to help you manage Home Assistant: create automations, modify configs, and deploy changes using natural language

1607. **[Corbell](https://github.com/Corbell-AI/Corbell)** - ⭐ 219
   AI-powered spec generation and review using multi-repo code graph intelligence for backend teams that ship to production.

1608. **[registry-broker-skills](https://github.com/hashgraph-online/registry-broker-skills)** - ⭐ 219
   AI agent skills for the Universal Registry - search, chat, and register 72,000+ agents across 14+ protocols. Works with Claude, Codex, Cursor, OpenClaw, and any AI assistant.

1609. **[shopify-mcp](https://github.com/GeLi2001/shopify-mcp)** - ⭐ 218
   MCP server for Shopify api, usable on mcp hosts such as Claude and Cursor

1610. **[claudepro-directory](https://github.com/JSONbored/claudepro-directory)** - ⭐ 217
   HeyClaude (formerly Claude Pro Directory) is a searchable collection of pre-built AI skills, agents, MCP servers, guides, hooks, statuslines, and other custom configs, designed to enhance Claude, Codex, Cursor, OpenClaw, and various other agentic workflows/platforms.

1611. **[mevzuat-mcp](https://github.com/saidsurucu/mevzuat-mcp)** - ⭐ 217
   MCP Server for Searching Turkish Legislation

1612. **[integrate-mcp-with-copilot](https://github.com/skills/integrate-mcp-with-copilot)** - ⭐ 217
   Learn how to use MCP Servers with GitHub Copilot

1613. **[craft-agents-oss](https://github.com/warpdot-dev/craft-agents-oss)** - ⭐ 217
   electron anthropic claude-agent-sdk mcp bun websocket thin-client multi-llm openapi skills automations oauth desktop-ai github-copilot google-ai chatgpt devtools apache-2 headless-server pi-sdk vscode-alternative linux macos windows

1614. **[mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript)** - ⭐ 216
   DataForSEO API modelcontextprotocol server

1615. **[jebmcp](https://github.com/dawnslab/jebmcp)** - ⭐ 216

1616. **[Geargrafx](https://github.com/drhelius/Geargrafx)** - ⭐ 216
   PC Engine / TurboGrafx-16 / SuperGrafx / PCE CD-ROM² emulator, debugger, and embedded MCP server for macOS, Windows, Linux, BSD and RetroArch.

1617. **[airbroke](https://github.com/icoretech/airbroke)** - ⭐ 216
   🔥 Lightweight, Airbrake/Sentry-compatible, PostgreSQL-based Open Source Error Catcher

1618. **[pbi-desktop-mcp-public](https://github.com/maxanatsko/pbi-desktop-mcp-public)** - ⭐ 216
   The MCP Engine is a Power BI tool that lets AI assistants like Claude interact with your Power BI models programmatically: read your model structure, run DAX queries, create and modify measures, manage relationships, and perform advanced analytics - all through natural conversation.

1619. **[mcp_code_executor](https://github.com/bazinga012/mcp_code_executor)** - ⭐ 215
   The MCP Code Executor is an MCP server that allows LLMs to execute Python code within a specified Conda environment.

1620. **[BifrostMCP](https://github.com/biegehydra/BifrostMCP)** - ⭐ 215
   VSCode Extension with an MCP server that exposes semantic tools like Find Usages and Rename to LLMs

1621. **[openchrome](https://github.com/shaun0927/openchrome)** - ⭐ 215
   Open-source browser automation MCP server. Control your real Chrome from any AI agent.

1622. **[ableton-mcp-extended](https://github.com/uisato/ableton-mcp-extended)** - ⭐ 215
   Ableton Live MCP (Model Context Protocol) server that allows control directly through AI assistants.

1623. **[mcp-server-wazuh](https://github.com/gbrigandi/mcp-server-wazuh)** - ⭐ 214
   MCP Server for Wazuh SIEM

1624. **[vibevideo-mcp](https://github.com/hyepartners-gmail/vibevideo-mcp)** - ⭐ 214
   Agent MCP for ffmpeg

1625. **[metorial-platform](https://github.com/metorial/metorial-platform)** - ⭐ 214
   The engine powering hundreds of thousands of MCP connections 🤖 🔥

1626. **[mathom](https://github.com/stephenlacy/mathom)** - ⭐ 214
   Run and monitor MCP servers locally

1627. **[google-analytics-mcp](https://github.com/surendranb/google-analytics-mcp)** - ⭐ 214
   Google Analytics 4 data to AI agents, agentic workflows, and MCP clients. Give agents analysis-ready access to website traffic, user behavior, and performance data with schema discovery, server-side aggregation, and safe defaults that reduce data wrangling.

1628. **[skill-manager](https://github.com/wanghuan9/skill-manager)** - ⭐ 214
   SkillDock is a skill manager and MCP manager for installing, viewing, updating, and syncing AI skills and MCP servers, with Git-aware updates to track upstream changes and local modifications. SkillDock 是一个用于安装、查看、更新和同步 AI skills 与 MCP servers 的 skill 管理工具和 MCP 管理工具，并支持 Git-aware 更新，用于跟踪上游变更和本地修改。

1629. **[sqrl](https://github.com/DataSQRL/sqrl)** - ⭐ 213
   Data Pipeline Automation Framework to build MCP servers, data APIs, and data lakes with SQL.

1630. **[claude-context-local](https://github.com/FarhanAliRaza/claude-context-local)** - ⭐ 213
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent. Embeddings are created and stored locally. No API cost.

1631. **[awesome-trading-agents](https://github.com/LLMQuant/awesome-trading-agents)** - ⭐ 213
   Curated list of LLM-driven trading agents, MCP servers, and agent skills for market research, strategy, and execution.

1632. **[firefox-devtools-mcp](https://github.com/mozilla/firefox-devtools-mcp)** - ⭐ 213
   Model Context Protocol server for Firefox DevTools - enables AI assistants to inspect and control Firefox browser through the Remote Debugging Protocol

1633. **[lihil](https://github.com/raceychan/lihil)** - ⭐ 213
   2X faster ASGI web framework for python, offering high-level development, low-level performance.

1634. **[Chanakya-Local-Friend](https://github.com/Rishabh-Bajpai/Chanakya-Local-Friend)** - ⭐ 213
   Chanakya is an advanced, open-source, and self-hostable voice assistant designed for privacy, power, and flexibility. It leverages local AI/ML models to ensure your data stays with you. It Integrates with 1000+ third-party MCP servers including Home Assistant.

1635. **[ht-mcp](https://github.com/memextech/ht-mcp)** - ⭐ 212
   Pure Rust implementation of MCP server for headless terminal

1636. **[binary-ninja-headless-mcp](https://github.com/mrphrazer/binary-ninja-headless-mcp)** - ⭐ 212
   Headless Binary Ninja MCP server — giving AI agents deep reverse-engineering capabilities via 180 tools.

1637. **[gibber-mcp](https://github.com/antonpk1/gibber-mcp)** - ⭐ 211
   Tiny MCP server with cryptography tools, sufficient to establish end-to-end encryption between LLM agents

1638. **[sora-mcp](https://github.com/Doriandarko/sora-mcp)** - ⭐ 211
   An MCP server to use Sora video generation APIs

1639. **[AutomatedEmulation](https://github.com/iknowjason/AutomatedEmulation)** - ⭐ 211
   An automated Adversary Emulation lab with terraform and MCP server.  Build Caldera techniques and operations assisted with LLMs.  Built for IaC stability, consistency, and speed.

1640. **[burp-mcp-agents](https://github.com/six2dez/burp-mcp-agents)** - ⭐ 211
   Practical setup guides and helpers to connect Burp Suite MCP Server to multiple AI backends (Codex, Gemini, Ollama, ...).

1641. **[apple-health-mcp-server](https://github.com/the-momentum/apple-health-mcp-server)** - ⭐ 211
   MCP server for querying Apple Health data with natural language using DuckDB under the hood.

1642. **[Autono](https://github.com/vortezwohl/Autono)** - ⭐ 211
   A ReAct-Based Highly Robust Autonomous Agent (Harness) Framework.

1643. **[k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server)** - ⭐ 210
   K8s-mcp-server is a Model Context Protocol (MCP) server that enables AI assistants like Claude to securely execute Kubernetes commands. It provides a bridge between language models and essential Kubernetes CLI tools including kubectl, helm, istioctl, and argocd, allowing AI systems to assist with cluster management, troubleshooting, and deployments

1644. **[WeChat-MCP](https://github.com/BiboyQG/WeChat-MCP)** - ⭐ 210
   WeChat-MCP: let Openclaw/Claude/ChatGPT and other AI assistants read and reply to WeChat for you

1645. **[open-webui-plugins](https://github.com/Classic298/open-webui-plugins)** - ⭐ 210
   A curated collection of Open WebUI plugins - tools, skills, filters, pipes, and actions that extend your AI chat experience.

1646. **[mcp-taskmanager](https://github.com/kazuph/mcp-taskmanager)** - ⭐ 210

1647. **[Claude-code-ChatInWindows](https://github.com/LKbaba/Claude-code-ChatInWindows)** - ⭐ 210
   Full-featured GUI for Claude Code CLI in VS Code — Windows (no WSL) & macOS. Third-party API, MCP plugins, Skills, Hooks, real-time token tracking. Actively maintained.

1648. **[automagik-genie](https://github.com/namastexlabs/automagik-genie)** - ⭐ 210
   🧞 Automagik Genie – bootstrap, update, and roll back AI agent workspaces with a single CLI + MCP toolkit.

1649. **[discordmcp](https://github.com/v-3/discordmcp)** - ⭐ 210
   Discord MCP Server for Claude Integration

1650. **[shodh-memory](https://github.com/varun29ankuS/shodh-memory)** - ⭐ 210
   Cognitive memory for AI agents — learns from use, forgets what's irrelevant, strengthens what matters. Single binary, fully offline.

1651. **[live-coding-music-mcp](https://github.com/williamzujkowski/live-coding-music-mcp)** - ⭐ 210
   A Model Context Protocol (MCP) server that gives Claude direct control over Strudel.cc for AI-assisted music generation and live coding.

1652. **[melrose](https://github.com/emicklei/melrose)** - ⭐ 209
   interactive programming of melodies, producing MIDI

1653. **[markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server)** - ⭐ 209
   An MCP server for converting Markdown to interactive mind maps with export support (PNG/JPG/SVG).

1654. **[figma-mcp](https://github.com/MatthewDailey/figma-mcp)** - ⭐ 209
   ModelContextProtocol for Figma's REST API

1655. **[lumen](https://github.com/ory/lumen)** - ⭐ 209
   Save 30% token costs when using Claude Code, Codex, OpenCode for free - with open source, local semantic search. Works for small and large codebases and monorepos! Enterprise-ready and fully compliant via Ollama and SQLite-vec.

1656. **[mcp-server-deep-research](https://github.com/reading-plus-ai/mcp-server-deep-research)** - ⭐ 209

1657. **[security-investigator](https://github.com/SCStelz/security-investigator)** - ⭐ 209
   Automated security investigation tool using Microsoft MCP Servers, GitHub Copilot, Python Modules and custom copilot-instructions.

1658. **[opik-mcp](https://github.com/comet-ml/opik-mcp)** - ⭐ 208
   Model Context Protocol (MCP) implementation for Opik enabling seamless IDE integration and unified access to prompts, projects, traces, and metrics.

1659. **[PerformanceStudio](https://github.com/erikdarlingdata/PerformanceStudio)** - ⭐ 208
   Free, open-source SQL Server execution plan analyzer — cross-platform GUI + CLI with 30 analysis rules, missing index detection, SSMS extension. Built-in MCP server for AI-assisted plan review.

1660. **[mikrotik-mcp](https://github.com/jeff-nasseri/mikrotik-mcp)** - ⭐ 208
   MCP server for Mikrotik

1661. **[mcp-launchpad](https://github.com/kenneth-liao/mcp-launchpad)** - ⭐ 208
   A lightweight CLI for efficiently discovering (search) and executing tools from multiple MCP (Model Context Protocol) servers.

1662. **[memory-graph](https://github.com/memory-graph/memory-graph)** - ⭐ 208
   A graph DB-based MCP memory server for coding agents with intelligent relationship tracking

1663. **[drawio2go](https://github.com/Menghuan1918/drawio2go)** - ⭐ 208
   A modern DrawIO editor application.  AI-Powered, Human-AI Collaboration | AI 加持，人机共绘drawio

1664. **[mcp_forge](https://github.com/mlzoo/mcp_forge)** - ⭐ 208
   这是一个专为开发企业级MCP server而设计的通用开发框架

1665. **[protoc-gen-go-mcp](https://github.com/redpanda-data/protoc-gen-go-mcp)** - ⭐ 208
   Go protobuf compiler extension to turn any gRPC service into an MCP server

1666. **[mcp-linkedin](https://github.com/adhikasp/mcp-linkedin)** - ⭐ 207
   A Model Context Protocol (MCP) server that provides tools to interact with LinkedIn's Feeds and Job API.

1667. **[comfy-pilot](https://github.com/ConstantineB6/comfy-pilot)** - ⭐ 207
   MCP server + embedded terminal that lets Claude Code see and edit your ComfyUI workflows

1668. **[nosia](https://github.com/dilolabs/nosia)** - ⭐ 207
   Self-hosted AI RAG + MCP Platform

1669. **[osint-tools-mcp-server](https://github.com/frishtik/osint-tools-mcp-server)** - ⭐ 207
   MCP server exposing multiple OSINT tools for AI assistants like Claude

1670. **[Doyunha-Gopeak](https://github.com/HaD0Yun/Doyunha-Gopeak)** - ⭐ 207
   GoPeak — The most comprehensive MCP server for Godot Engine. 95+ tools: scene management, GDScript LSP, DAP debugger, screenshot capture, input injection, ClassDB introspection, CC0 asset library. npx gopeak

1671. **[uLoopMCP](https://github.com/hatayama/uLoopMCP)** - ⭐ 207
   Your Unity project's AI autopilot. Compile, test, debug, repeat—until it just works.

1672. **[ai-infrastructure-agent](https://github.com/VersusControl/ai-infrastructure-agent)** - ⭐ 207
   AI Infrastructure Agent is an intelligent system that allows you to manage AWS infrastructure using natural language commands.

1673. **[AutoRedTeam-Orchestrator](https://github.com/Coff0xc/AutoRedTeam-Orchestrator)** - ⭐ 206
   Enterprise AI Red Team Platform | 企业级AI红队平台 | 132 MCP Tools | Pure Python Engines | SDK+CLI+MCP | Auto-Download sqlmap/nuclei/ffuf | Production C2 | LLM Enhanced | Docker Sandbox | SARIF CI/CD | 1980 Tests

1674. **[dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp)** - ⭐ 206
   MCP server for Dynatrace Observability

1675. **[mcp-servers-for-revit](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit)** - ⭐ 206
   🔥💧🤖 Sparx fork of the mcp-servers-for-revit/revit-mcp project

1676. **[nowledge-mem](https://github.com/nowledge-co/nowledge-mem)** - ⭐ 206
   Memory and context manager just works.

1677. **[mcp-redmine](https://github.com/runekaagaard/mcp-redmine)** - ⭐ 206
   A redmine MCP server covering close to 100% of redmines API

1678. **[Remote-MCP](https://github.com/ssut/Remote-MCP)** - ⭐ 206
   A type-safe solution to remote MCP communication, enabling effortless integration for centralized management of Model Context.

1679. **[mcp-context-protector](https://github.com/trailofbits/mcp-context-protector)** - ⭐ 206
   MCP security wrapper

1680. **[agent-trade-kit](https://github.com/6551-Team/agent-trade-kit)** - ⭐ 205
   OKX Agent Trade Kit: MCP server and CLI to connect AI assistants (Claude, Cursor) to your OKX account via Model Context Protocol. Local, MIT, TypeScript monorepo.

1681. **[notion_mcp](https://github.com/danhilse/notion_mcp)** - ⭐ 205
   A simple MCP integration that allows Claude to read and manage a personal Notion todo list

1682. **[mcp-rb](https://github.com/funwarioisii/mcp-rb)** - ⭐ 205
   A lightweight Ruby framework for building MCP servers with a Sinatra-like DSL

1683. **[cachebro](https://github.com/glommer/cachebro)** - ⭐ 205
   File cache with diff tracking for AI coding agents. Drop-in MCP server that cuts token usage by 26%.

1684. **[QMT-MCP](https://github.com/guangxiangdebizi/QMT-MCP)** - ⭐ 205
    QMT-MCP 模块化量化交易助手

1685. **[claude-self-reflect](https://github.com/ramakay/claude-self-reflect)** - ⭐ 205
   Claude forgets everything. This fixes that. 🔗 www.npmjs.com/package/claude-self-reflect

1686. **[langchain-mcp](https://github.com/rectalogic/langchain-mcp)** - ⭐ 205
   Model Context Protocol tool support for LangChain

1687. **[android-skills-mcp](https://github.com/skydoves/android-skills-mcp)** - ⭐ 205
   An MCP server and CLI packager for official Android skills.

1688. **[OSWorld-MCP](https://github.com/X-PLUG/OSWorld-MCP)** - ⭐ 205

1689. **[nano-agent](https://github.com/disler/nano-agent)** - ⭐ 204
   A MCP Server for a small scale engineering agents with multi-provider LLM support.

1690. **[SharpToolsMCP](https://github.com/kooshi/SharpToolsMCP)** - ⭐ 204
   A suite of MCP tools for AIs to analyze and modify C# solutions with high signal, Roslyn powered context.

1691. **[AgentCrew](https://github.com/saigontechnology/AgentCrew)** - ⭐ 204
   Chat application with multi-agents system supports multi-models and MCP

1692. **[sap-skills](https://github.com/secondsky/sap-skills)** - ⭐ 204
   Production-ready Claude Code skills for SAP development - 35 skills covering BTP, CAP, Fiori, ABAP, HANA, Analytics Cloud, and more

1693. **[OmniFocus-MCP](https://github.com/themotionmachine/OmniFocus-MCP)** - ⭐ 204
   Let LLMs interface with your tasks and projects through the Model Context Protocol. Add, organize, and query your OmniFocus database with natural language commands.

1694. **[mcp-fusion](https://github.com/vinkius-labs/mcp-fusion)** - ⭐ 204
   MCP Fusion - The framework for AI-native MCP servers.

1695. **[mongodb-lens](https://github.com/furey/mongodb-lens)** - ⭐ 203
   🍃🔎 MongoDB Lens: Full Featured MCP Server for MongoDB Databases

1696. **[aleph](https://github.com/Hmbown/aleph)** - ⭐ 203
   Skill + MCP server to turn your agent into an RLM. Load context, iterate with search/code/think tools, converge on answers.

1697. **[backlog-mcp-server](https://github.com/nulab/backlog-mcp-server)** - ⭐ 203

1698. **[gemini-mcp](https://github.com/RLabs-Inc/gemini-mcp)** - ⭐ 203
   MCP Server that enables Claude code to interact with Gemini

1699. **[CrowdSentinels-AI-MCP](https://github.com/thomasxm/CrowdSentinels-AI-MCP)** - ⭐ 203
   AI-powered threat hunting and incident response MCP server for Elasticsearch/OpenSearch

1700. **[y-cli](https://github.com/luohy15/y-cli)** - ⭐ 202
   A Tiny Terminal Chat App for AI Models with MCP Client Support

1701. **[node9-proxy](https://github.com/node9-ai/node9-proxy)** - ⭐ 202
   The Execution Security Layer for the Agentic Era. Providing deterministic "Sudo" governance and audit logs for autonomous AI agents.

1702. **[flights-mcp](https://github.com/ravinahp/flights-mcp)** - ⭐ 202
   An MCP server to search for flights.

1703. **[ai-skills](https://github.com/sanjay3290/ai-skills)** - ⭐ 202
   Collection of agent skills for AI coding assistants

1704. **[scholar-search-mcp](https://github.com/Silung/scholar-search-mcp)** - ⭐ 202
   An MCP server for academic paper search that integrates with AI assistants (e.g., Claude Code, Cursor), enabling them to search and retrieve academic paper metadata.

1705. **[waldzell-mcp](https://github.com/waldzellai/waldzell-mcp)** - ⭐ 202
   Waldzell AI's monorepo of MCP servers. Use in Claude Desktop, Cline, Roo Code, and more!

1706. **[dario](https://github.com/askalf/dario)** - ⭐ 201
   Local LLM router. One endpoint for Claude Max/Pro, OpenAI, OpenRouter, Groq, Ollama, LiteLLM, any OpenAI-compat URL — your tools don't need to change. OAuth for Claude subscriptions, multi-account pool, MCP server. Zero runtime deps.

1707. **[rmcp](https://github.com/finite-sample/rmcp)** - ⭐ 201
   R MCP Server

1708. **[open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp)** - ⭐ 201
   An OpenStreetMap MCP server implementation that enhances LLM capabilities with location-based services and geospatial data.

1709. **[RelaMind](https://github.com/El-12stu/RelaMind)** - ⭐ 200
   基于 AI 的个人成长轨迹分析系统，通过记录生活、回顾历史、分析模式帮助用户更好地理解自己，实现持续成长。包含智能路由、RAG 检索、自主任务智能体等功能。

1710. **[mcp](https://github.com/hopx-ai/mcp)** - ⭐ 200

1711. **[codefire-app](https://github.com/websitebutlers/codefire-app)** - ⭐ 200
   CodeFire gives AI coding tools persistent memory, task tracking, and project intelligence. A desktop companion for the AI-native workflow.

1712. **[mcp-guardian](https://github.com/eqtylab/mcp-guardian)** - ⭐ 199
   Manage / Proxy / Secure your MCP Servers

1713. **[mangaba_ai](https://github.com/Mangaba-ai/mangaba_ai)** - ⭐ 199
   Repositório minimalista para criação de agentes de IA inteligentes e versáteis com protocolos A2A (Agent-to-Agent) e MCP (Model Context Protocol).

1714. **[ghost-mcp](https://github.com/MFYDev/ghost-mcp)** - ⭐ 199
   A Model Context Protocol (MCP) server for interacting with Ghost CMS through LLM interfaces like Claude. Allow you to control your Ghost blog by simply asking Claude etc.

1715. **[smart-coding-mcp](https://github.com/omar-haris/smart-coding-mcp)** - ⭐ 199
   An extensible Model Context Protocol (MCP-Local-MRL-RAG-AST) server that provides intelligent semantic code search for AI assistants. Built with local AI models, inspired by Cursor's semantic search.

1716. **[wavefront](https://github.com/rootflo/wavefront)** - ⭐ 199
   🔥🔥🔥 Enterprise AI middleware, alternative to unifyapps, n8n, lyzr

1717. **[utcp-mcp](https://github.com/universal-tool-calling-protocol/utcp-mcp)** - ⭐ 199
   All-in-one MCP server that can connect your AI agents to any native endpoint, powered by UTCP

1718. **[mcp-proxy-server](https://github.com/adamwattis/mcp-proxy-server)** - ⭐ 198
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single interface

1719. **[Nano-Banana-MCP](https://github.com/ConechoAI/Nano-Banana-MCP)** - ⭐ 198
   A Nano Banana MCP server, which you can integrate to cursor/claude code and any mcp client

1720. **[gcp-mcp](https://github.com/eniayomi/gcp-mcp)** - ⭐ 198
   A Model Context Protocol (MCP) server that enables AI assistants like Claude to interact with your Google Cloud Platform environment. This allows for natural language querying and management of your GCP resources during conversations.

1721. **[omem](https://github.com/ourmem/omem)** - ⭐ 198
   Shared Memory That Never Forgets — persistent memory for AI agents with Space-based sharing across agents and teams. Plugins for OpenCode, Claude Code, OpenClaw, MCP Server.

1722. **[bear-notes-mcp](https://github.com/vasylenko/bear-notes-mcp)** - ⭐ 198
   MCP Server for Bear note taking app available as Claude Desktop extension or standalone server for any other AI tool

1723. **[EdgeBox](https://github.com/BIGPPWONG/EdgeBox)** - ⭐ 197
   A fully-featured, GUI-powered local LLM Agent sandbox with complete MCP protocol support.   Features both CLI and full desktop environment, enabling AI agents to operate browsers, terminal, and other desktop applications just like humans. Based on E2B oss code.

1724. **[x64dbg-mcp](https://github.com/SetsunaYukiOvO/x64dbg-mcp)** - ⭐ 197
   MCP server plugin for x64dbg debugger - enables AI agents and external tools to control debugging via JSON-RPC 2.0 over HTTP/SSE;Develop with cursor/windsurf

1725. **[agentrq](https://github.com/agentrq/agentrq)** - ⭐ 196
   AgentRQ: Human-in-loop realtime conversational task manager for AI Agents.

1726. **[ProxmoxMCP](https://github.com/canvrno/ProxmoxMCP)** - ⭐ 196
   MCP for Proxmox integration in Cline

1727. **[LeanKG](https://github.com/FreePeak/LeanKG)** - ⭐ 196
   LeanKG: Stop Burning Tokens. Start Coding Lean.

1728. **[cognition-wheel](https://github.com/Hormold/cognition-wheel)** - ⭐ 196
   A Model Context Protocol (MCP) server that implements a "wisdom of crowds" approach to AI reasoning by consulting multiple state-of-the-art language models in parallel and synthesizing their responses.

1729. **[tmcp](https://github.com/paoloricciuti/tmcp)** - ⭐ 196
   Typescript SDK to build MCP servers in an agnostic way

1730. **[unifi-network-mcp](https://github.com/sirkirby/unifi-network-mcp)** - ⭐ 196
   MCP server implementation for the UniFi network application

1731. **[mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server)** - ⭐ 195
   Connects MCP to major 3D printer APIs (Orca, FULU's Orca/Bambu, OctoPrint, Klipper, Duet, Repetier, Prusa, Creality). Control prints, monitor status, and perform advanced STL operations like scaling, rotation, sectional editing, and base extension. Includes slicing and visualization.

1732. **[mcp-portal-transparencia](https://github.com/dutradotdev/mcp-portal-transparencia)** - ⭐ 195
   MCP para orquestração automatizada de chamadas à API do Portal da Transparência do Governo Federal brasileiro

1733. **[gistpad-mcp](https://github.com/lostintangent/gistpad-mcp)** - ⭐ 195
   📓 An MCP server for managing your personal knowledge, daily notes, and re-usable prompts via GitHub Gists

1734. **[MCP-server-client-computer-use-ai-sdk](https://github.com/mediar-ai/MCP-server-client-computer-use-ai-sdk)** - ⭐ 195

1735. **[AutoDocs](https://github.com/TrySita/AutoDocs)** - ⭐ 195
   We handle what engineers and IDEs won't: generating and maintaining technical documentation for your codebase, while also providing search with dependency-aware context to help your AI tools understand your codebase and its conventions.

1736. **[affine-mcp-server](https://github.com/DAWNCR0W/affine-mcp-server)** - ⭐ 194
   Model Context Protocol server for AFFiNE. Connect AI assistants to AFFiNE workspaces, documents, databases, and collaboration APIs over stdio or HTTP.

1737. **[agent-graph](https://github.com/keta1930/agent-graph)** - ⭐ 194
   Agent Graph is a Multi-Agent System built on the principles of Context Engineering

1738. **[mcp-agent-graph](https://github.com/keta1930/mcp-agent-graph)** - ⭐ 194
   MCP Agent Graph is a Multi-Agent System built on the principles of Context Engineering

1739. **[MCP-Checklists](https://github.com/MCP-Manager/MCP-Checklists)** - ⭐ 194

1740. **[bluebox](https://github.com/VectorlyApp/bluebox)** - ⭐ 194
   Index the world's undocumented APIs

1741. **[easy-mcp](https://github.com/zcaceres/easy-mcp)** - ⭐ 194
   Absurdly easy Model Context Protocol Servers in Typescript

1742. **[freecad_mcp](https://github.com/bonninr/freecad_mcp)** - ⭐ 193
   FreecadMCP connects Freecad to Claude AI and other MCP-ready tools like Cursor through the Model Context Protocol (MCP), allowing Claude to directly interact with and control Freecad. This integration enables prompt assisted CAD 3d Design.

1743. **[supabase-mcp](https://github.com/coleam00/supabase-mcp)** - ⭐ 193
   Supabase MCP server created in Python.

1744. **[aseprite-mcp](https://github.com/diivi/aseprite-mcp)** - ⭐ 193
   MCP server for interacting with the Aseprite API

1745. **[task-orchestrator](https://github.com/jpicklyk/task-orchestrator)** - ⭐ 193
   Server-enforced workflow discipline for AI agents. An MCP server providing persistent work items, dependency graphs, quality gates, and actor attribution. Schemas define what agents must produce — the server blocks the call if they don't. Works with any MCP-compatible client.

1746. **[paperless-mcp](https://github.com/nloui/paperless-mcp)** - ⭐ 193
   An MCP (Model Context Protocol) server for interacting with a Paperless-NGX API server. This server provides tools for managing documents, tags, correspondents, and document types in your Paperless-NGX instance.

1747. **[mcp-proxy-server](https://github.com/ptbsare/mcp-proxy-server)** - ⭐ 193
   This server acts as a central hub for Model Context Protocol (MCP) resource servers.

1748. **[akshare-one-mcp](https://github.com/zwldarren/akshare-one-mcp)** - ⭐ 193
   MCP server that provides access to Chinese stock market data using akshare-one

1749. **[perfetto-mcp](https://github.com/antarikshc/perfetto-mcp)** - ⭐ 192
   This is a Model Context Protocol (MCP) server that gets answers from your Perfetto Traces. It turns natural‑language prompts into focused Perfetto analyses.

1750. **[mcp-server-excel](https://github.com/sbroenne/mcp-server-excel)** - ⭐ 192
   Excel MCP Server & CLI - 23 tools, 214 operations for AI-powered Excel automation via COM API

1751. **[facebook-ads-library-mcp](https://github.com/talknerdytome-labs/facebook-ads-library-mcp)** - ⭐ 192
   MCP Server for Facebook ADs Library - Get instant answers from FB's ad library

1752. **[agentseal](https://github.com/AgentSeal/agentseal)** - ⭐ 191
   Security toolkit for AI agents. Scan your machine for dangerous skills and MCP configs, monitor for supply chain attacks, test prompt injection resistance, and audit live MCP servers for tool poisoning.

1753. **[tokensave](https://github.com/aovestdipaperino/tokensave)** - ⭐ 191
   The most comprehensive code intelligence MCP server for AI coding agents. 40+ tools, 30+ languages, 9 agent integrations. Pre-indexed semantic knowledge graphs for instant code understanding — fewer tokens, fewer tool calls, 100% local.

1754. **[auto-mcp](https://github.com/brizzai/auto-mcp)** - ⭐ 191
   Transform any OpenAPI/Swagger definition into a fully-featured Model Context Protocol (MCP) server

1755. **[GrokSearch-rs](https://github.com/Episkey-G/GrokSearch-rs)** - ⭐ 191
   Rust MCP server for Grok web search and Tavily-backed source retrieval

1756. **[quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server)** - ⭐ 191
   This extension enables developers to implement the MCP server features easily.

1757. **[quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers)** - ⭐ 191
   Model Context Protocol Servers in Quarkus

1758. **[install-mcp](https://github.com/supermemoryai/install-mcp)** - ⭐ 191
   A simple CLI to install MCP servers into any client - auth included!

1759. **[chiasmus](https://github.com/yogthos/chiasmus)** - ⭐ 191
   Chiasmus is an MCP server that gives language models access to formal verification

1760. **[seo-mcp](https://github.com/cnych/seo-mcp)** - ⭐ 190
   A free SEO tool MCP (Model Control Protocol) service based on Ahrefs data. Includes features such as backlinks, keyword ideas, and more.

1761. **[awesome-mcp-korea](https://github.com/darjeeling/awesome-mcp-korea)** - ⭐ 190
   A curated list of MCP servers for the Korean market, including legal, commerce, public data, and local services integrations.

1762. **[mcp-dotnet-samples](https://github.com/microsoft/mcp-dotnet-samples)** - ⭐ 190
   A comprehensive set of samples of creating and using MCP servers and clients with .NET

1763. **[Uni-CLI](https://github.com/olo-dot-io/Uni-CLI)** - ⭐ 190
   Operations substrate for AI agents that use real software: 311 sites/tools, logged-in browsers, desktop apps, local tools, MCP, policy, evidence, AgentEnvelope v2, and self-repair.

1764. **[strudel-mcp-server](https://github.com/williamzujkowski/strudel-mcp-server)** - ⭐ 190
   A Model Context Protocol (MCP) server that gives Claude direct control over Strudel.cc for AI-assisted music generation and live coding.

1765. **[mcp-server-siri-shortcuts](https://github.com/dvcrn/mcp-server-siri-shortcuts)** - ⭐ 189
   MCP for calling Siri Shorcuts from LLMs

1766. **[gigabrain](https://github.com/legendaryvibecoder/gigabrain)** - ⭐ 189
   Local-first memory layer for OpenClaw, Codex App, and Codex CLI: capture, recall, dedupe, and native sync.

1767. **[mcp](https://github.com/magicuidesign/mcp)** - ⭐ 189
   Official Magic UI MCP server.

1768. **[meilisearch-mcp](https://github.com/meilisearch/meilisearch-mcp)** - ⭐ 189
   A Model Context Protocol (MCP) server for interacting with Meilisearch through LLM interfaces.

1769. **[sunpeak](https://github.com/Sunpeak-AI/sunpeak)** - ⭐ 189
   Server-agnostic MCP testing framework and full-stack MCP App framework for ChatGPT Apps, Claude Connectors, and more.

1770. **[opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server)** - ⭐ 189
   Unified MCP server for querying OpenTelemetry traces across multiple backends (Jaeger, Tempo, Traceloop, etc.), enabling AI agents to analyze distributed traces for automated debugging and observability.

1771. **[Easy-MCP-AutoCad](https://github.com/zh19980811/Easy-MCP-AutoCad)** - ⭐ 189
   这个项目是一个基于Model Context Protocol (MCP)的AutoCAD集成服务器，它允许通过自然语言与AutoCAD进行交互。通过这个服务器，用户可以使用Claude等大型语言模型来创建、修改和分析AutoCAD图纸，同时还可以存储和查询CAD元素的相关数据。目前制作参考学习，仅实现端到端之间的通信，具体工具函数尚未晚上

1772. **[pullmd](https://github.com/AeternaLabsHQ/pullmd)** - ⭐ 188
   Self-hosted URL- and file-to-Markdown service for humans and AI agents - web pages, documents, images, audio, YouTube. PWA + REST + MCP + Claude Code skill, Reddit-aware, refreshable share links.

1773. **[antigravity-link-extension](https://github.com/cafeTechne/antigravity-link-extension)** - ⭐ 188
   Mobile companion for Google's Antigravity IDE. Mirror AI sessions on your phone, send messages, stop generation, automate via 9 MCP tools or OpenAPI.

1774. **[mcp-toolbox-sdk-python](https://github.com/googleapis/mcp-toolbox-sdk-python)** - ⭐ 188
   Python SDK for interacting with the MCP Toolbox for Databases.

1775. **[openapi-mcp](https://github.com/ckanthony/openapi-mcp)** - ⭐ 187
   Dockerized MCP Server to allow your AI agent to access any API with existing api docs

1776. **[mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition)** - ⭐ 187
   MCP server providing access to the comprehensive OpenNutrition food database with 300,000+ food items, nutritional data, and barcode lookups

1777. **[bilibili-mcp-server](https://github.com/huccihuang/bilibili-mcp-server)** - ⭐ 187
   MCP Server for the Bilibili API, supporting various operations.

1778. **[mcp-injection-experiments](https://github.com/invariantlabs-ai/mcp-injection-experiments)** - ⭐ 187
   Code snippets to reproduce MCP tool poisoning attacks.

1779. **[memov](https://github.com/memovai/memov)** - ⭐ 187
   Give git-like & traceable memory to OpenClaw and any coding agents. By https://memov.ai/ aka Entire CLI for every coding agents by MCP.

1780. **[code-sandbox-mcp](https://github.com/philschmid/code-sandbox-mcp)** - ⭐ 187

1781. **[mcp-chat](https://github.com/PipedreamHQ/mcp-chat)** - ⭐ 187
   Examples of using Pipedream's MCP server in your app or AI agent.

1782. **[ida-mcp-server-plugin](https://github.com/taida957789/ida-mcp-server-plugin)** - ⭐ 187
   IDA Pro Plugin for serving MCP SSE server for cursor / claude

1783. **[mcp-usecase](https://github.com/teddynote-lab/mcp-usecase)** - ⭐ 187

1784. **[mcp-agent-langchainjs](https://github.com/Azure-Samples/mcp-agent-langchainjs)** - ⭐ 186
   Serverless AI agent using LangChain.js and Model Context Protocol (MCP) integration to order burgers from a burger restaurant

1785. **[AI-company](https://github.com/CronusL-1141/AI-company)** - ⭐ 186
   Multi-agent team operating system for Claude Code. 108 MCP tools, 40+ agent templates, 10 lifecycle hooks, 7 pipeline workflows. Persistent teams, structured meetings, task wall, real-time React dashboard. No LangChain/AutoGen — pure CC native integration.

1786. **[Omni-Adapter](https://github.com/HuChundong/Omni-Adapter)** - ⭐ 186
   多平台 文生图/图生图 等能力接入MCP

1787. **[ProxmoxMCP-Plus](https://github.com/RekklesNA/ProxmoxMCP-Plus)** - ⭐ 186
   Use MCP and OpenAPI to safely control Proxmox VE VMs, LXCs, backups, and snapshots from LLMs and AI agents.

1788. **[superset-mcp](https://github.com/aptro/superset-mcp)** - ⭐ 185
   connect to 50+ data stores via superset mcp server. Can use with open ai agent sdk, Claude app, cursor, windsurf

1789. **[mcp-server](https://github.com/bitwarden/mcp-server)** - ⭐ 185
   MCP server for interaction with Bitwarden.

1790. **[dify-plugin-tools-mcp_sse](https://github.com/junjiem/dify-plugin-tools-mcp_sse)** - ⭐ 185
   Dify 1.0 Plugin MCP HTTP with SSE or Streamable HTTP transport Tools

1791. **[netbox-mcp-server](https://github.com/netboxlabs/netbox-mcp-server)** - ⭐ 185
   Model Context Protocol (MCP) server for read-only interaction with NetBox data in LLMs

1792. **[docs](https://github.com/strands-agents/docs)** - ⭐ 185
   Documentation for the Strands Agents SDK. A model-driven approach to building AI agents in just a few lines of code.

1793. **[tripo-mcp](https://github.com/VAST-AI-Research/tripo-mcp)** - ⭐ 185
   Official MCP server for Tripo

1794. **[litemcp](https://github.com/wong2/litemcp)** - ⭐ 185
   A TypeScript framework for building MCP servers elegantly

1795. **[resolve-claude-mcp](https://github.com/barckley75/resolve-claude-mcp)** - ⭐ 184
   Connect DaVinci Resolve Studio to Claude AI through the Model Context Protocol (MCP)

1796. **[a2a_mcp-example](https://github.com/ishanExtreme/a2a_mcp-example)** - ⭐ 184
   An example showing how A2A and MCP can be used together

1797. **[lsp-mcp](https://github.com/jonrad/lsp-mcp)** - ⭐ 184
   An Model Context Protocol (MCP) server that provides LLMs/AI Agents with the capabilities of a language server protocol (LSP) server. This gives the AI the ability to get language aware context from the codebase.

1798. **[siconos](https://github.com/siconos/siconos)** - ⭐ 184
   Simulation framework for nonsmooth dynamical systems

1799. **[armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp)** - ⭐ 183
   The MCP server for interacting with Blockchain, Swaps, Strategic Planning and more.

1800. **[meta-mcp](https://github.com/brijr/meta-mcp)** - ⭐ 183
   MCP Server for connecting to the Meta Marketing API

1801. **[agentor](https://github.com/CelestoAI/agentor)** - ⭐ 183
   Open source version of Claude Managed Agents. Fastest way to build and deploy reliable AI agents, MCP tools and  agent-to-agent.

1802. **[mcp-bridge](https://github.com/firekula/mcp-bridge)** - ⭐ 183
   这是一个为 Cocos Creator 设计的 MCP (Model Context Protocol) 桥接插件，用于连接外部 AI 工具与 Cocos Creator 编辑器，实现对场景、节点等资源的自动化操作。

1803. **[Wazuh-MCP-Server](https://github.com/gensecaihq/Wazuh-MCP-Server)** - ⭐ 183
   AI-powered security operations for Wazuh SIEM—use any MCP-compatible client to ask security questions in plain English. Faster threat detection, incident triage, and compliance checks with real-time monitoring and anomaly spotting. Production-ready MCP server for conversational SOC workflows.

1804. **[mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server)** - ⭐ 183

1805. **[aelf-skills](https://github.com/AElfProject/aelf-skills)** - ⭐ 182
   Unified aelf skills hub for discovery, routing, bootstrap, and health checks across OpenClaw, Codex, Cursor, and Claude Code.

1806. **[aws-mcp-server](https://github.com/alexei-led/aws-mcp-server)** - ⭐ 182
   A lightweight service that enables AI assistants to execute AWS CLI commands (in safe containerized environment) through the Model Context Protocol (MCP). Bridges Claude, Cursor, and other MCP-aware AI tools with AWS CLI for enhanced cloud infrastructure management.

1807. **[cloud-mcp-server](https://github.com/alexei-led/cloud-mcp-server)** - ⭐ 182
   A lightweight service that enables AI assistants to execute AWS CLI commands (in safe containerized environment) through the Model Context Protocol (MCP). Bridges Claude, Cursor, and other MCP-aware AI tools with AWS CLI for enhanced cloud infrastructure management.

1808. **[lucid-agents](https://github.com/daydreamsai/lucid-agents)** - ⭐ 182
   Lucid Agents Commerce SDK. Bootstrap AI agents in 60 seconds that can pay, sell, and participate in agentic commerce supply chains. Our protocol agnostic SDK provides CLI-generated templates and drop-in adapters for Hono, Express, Next.js, and TanStack, giving you instant access to crypto/fiat payment rails (AP2, A2A, x402, ERC8004).

1809. **[dataseo-mcp](https://github.com/egebese/dataseo-mcp)** - ⭐ 182
   A free SEO research tool using Model Context Protocol (MCP) powered by Ahrefs data. Get backlink analysis, keyword research, traffic estimation, and more — directly in your AI-powered IDE.

1810. **[MakerAi](https://github.com/gustavoeenriquez/MakerAi)** - ⭐ 182
   The AI Operating System for Delphi. 100% native framework with RAG 2.0, autonomous agents, MCP protocol, and universal LLM connector. Supports OpenAI, Claude, Gemini, Ollama, and more. Delphi 10.4+ (limited), full support from Delphi 12 Athens.

1811. **[Gopeak-godot-mcp](https://github.com/HaD0Yun/Gopeak-godot-mcp)** - ⭐ 182
   GoPeak — The most comprehensive MCP server for Godot Engine. 95+ tools: scene management, GDScript LSP, DAP debugger, screenshot capture, input injection, ClassDB introspection, CC0 asset library. npx gopeak

1812. **[thinkchain](https://github.com/martinbowling/thinkchain)** - ⭐ 182
   🧠 Advanced Claude streaming interface with interleaved thinking, dynamic tool discovery, and MCP integration. Watch Claude think through problems in real-time while executing tools with live progress updates.

1813. **[mcp-openai-gemini-llama-example](https://github.com/philschmid/mcp-openai-gemini-llama-example)** - ⭐ 182

1814. **[anki-mcp-server](https://github.com/scorzeth/anki-mcp-server)** - ⭐ 182
   An MCP server for Anki

1815. **[4D-ARE](https://github.com/ybeven/4D-ARE)** - ⭐ 181
   Build LLM agents that explain why, not just what. Attribution-driven agent requirements engineering framework. Based on the 4D-ARE Paper - https://arxiv.org/abs/2601.04556

1816. **[spring-ai-playground](https://github.com/JM-Lab/spring-ai-playground)** - ⭐ 180
   Safe local execution layer for AI agent tools. Build, validate, and publish MCP tools with a no-pass-no-run workflow — cross-platform desktop app powered by Spring AI.

1817. **[open-responses-server](https://github.com/teabranch/open-responses-server)** - ⭐ 180
   Wraps any OpenAI API interface as Responses with MCPs support so it supports Codex. Adding any missing stateful features. Ollama and Vllm compliant.

1818. **[google-slides-mcp](https://github.com/matteoantoci/google-slides-mcp)** - ⭐ 179
   MCP Server for Google Slides

1819. **[icm](https://github.com/rtk-ai/icm)** - ⭐ 179
   Permanent memory for AI agents. Single binary, zero dependencies, MCP native.

1820. **[mcp-victoriametrics](https://github.com/VictoriaMetrics/mcp-victoriametrics)** - ⭐ 179
   The implementation of Model Context Protocol (MCP) server for VictoriaMetrics

1821. **[xiaoi](https://github.com/xvhuan/xiaoi)** - ⭐ 179
   小爱音箱语音通知工具：提供 CLI/TUI/MCP/Webhook 一键播报与控制音量，支持 PM2 常驻部署，支持docker部署。

1822. **[ClawMem](https://github.com/yoloshii/ClawMem)** - ⭐ 179
   On-device memory layer for AI agents. Claude Code, Hermes and OpenClaw. Hooks + MCP server + hybrid RAG search.

1823. **[mcp-scholarly](https://github.com/adityak74/mcp-scholarly)** - ⭐ 178
   A MCP server to search for accurate academic articles.

1824. **[claude-code-mcp](https://github.com/auchenberg/claude-code-mcp)** - ⭐ 178
   claude-code-mcp

1825. **[bernstein](https://github.com/chernistry/bernstein)** - ⭐ 178
   Deterministic orchestrator for 30+ CLI AI coding agents. Git worktree isolation, HMAC audit trail, MCP server mode.

1826. **[Revornix](https://github.com/Qingyon-AI/Revornix)** - ⭐ 178
   Revornix is an open-source, local-first AI information/markdown workspace. It helps you collect fragmented inputs, turn them into structured knowledge, generate reports with images and podcast audio, and deliver the output through automated notifications.

1827. **[rust-mcp-sdk](https://github.com/rust-mcp-stack/rust-mcp-sdk)** - ⭐ 178
   A high-performance, asynchronous toolkit for building MCP servers and clients in Rust.

1828. **[smythos-studio](https://github.com/SmythOS/smythos-studio)** - ⭐ 178
   SmythOS Studio: Open-Source Visual AI Agent Builder and deployable runtime stack from SmythOS. Start with an intuitive drag-and-drop workspace, extend with custom code, and deploy your agents anywhere — local, cloud, or edge — with full governance and control.

1829. **[mcp-text-editor](https://github.com/tumf/mcp-text-editor)** - ⭐ 178

1830. **[claude-historian-mcp](https://github.com/Vvkmnn/claude-historian-mcp)** - ⭐ 178
   📜 An MCP server for conversation history search and retrieval in Claude Code

1831. **[yuque-ecosystem](https://github.com/yuque/yuque-ecosystem)** - ⭐ 178
   Yuque AI Ecosystem — MCP Server, Skills & Plugin for Yuque (语雀)

1832. **[mcp-server-reddit](https://github.com/Hawstein/mcp-server-reddit)** - ⭐ 177
   A Model Context Protocol (MCP) server that provides tools for fetching Reddit content, including frontpage posts, subreddit information and hot posts, post details, and comments.

1833. **[skunit](https://github.com/mehrandvd/skunit)** - ⭐ 177
   skUnit is a testing tool for AI units, such as IChatClient, MCP Servers and agents.

1834. **[mcptools](https://github.com/posit-dev/mcptools)** - ⭐ 177
   Model Context Protocol For R

1835. **[aws-finops-mcp-server](https://github.com/ravikiranvm/aws-finops-mcp-server)** - ⭐ 177
   An MCP (Model Context Protocol) server that brings powerful AWS FinOps capabilities directly into your AI assistant. Analyze cloud costs, audit for waste, and get budget insights using natural language, all while keeping your credentials secure on your local machine.

1836. **[mcp-telegram](https://github.com/sparfenyuk/mcp-telegram)** - ⭐ 177
   MCP server to work with Telegram through MTProto

1837. **[tomcp](https://github.com/Ami3466/tomcp)** - ⭐ 176
   Turn any website or doc into an MCP server

1838. **[pg-mcp-server](https://github.com/ericzakariasson/pg-mcp-server)** - ⭐ 176
   MCP Server for Postgres

1839. **[jdocmunch-mcp](https://github.com/jgravelle/jdocmunch-mcp)** - ⭐ 176
   The leading, most token-efficient MCP server for documentation exploration and retrieval via structured section indexing

1840. **[mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb)** - ⭐ 176
   A Model Context Protocol (MCP) server implementation for DuckDB, providing database interaction capabilities

1841. **[MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce)** - ⭐ 176
   MCP Salesforce connector

1842. **[yuque-mcp-server](https://github.com/yuque/yuque-mcp-server)** - ⭐ 176
   Yuque MCP Server - Model Context Protocol server for Yuque API

1843. **[aghub](https://github.com/AkaraChen/aghub)** - ⭐ 175
   One hub for every AI coding agent. Unified configuration management for 22+ assistants.

1844. **[Companion](https://github.com/mattt/Companion)** - ⭐ 175
   Your neighborhood friendly MCP utility for macOS, iOS, and visionOS

1845. **[mcp-shell-server](https://github.com/tumf/mcp-shell-server)** - ⭐ 175

1846. **[seo-research-mcp](https://github.com/egebese/seo-research-mcp)** - ⭐ 174
   A free SEO research tool using Model Context Protocol (MCP) powered by Ahrefs data. Get backlink analysis, keyword research, traffic estimation, and more — directly in your AI-powered IDE.

1847. **[command](https://github.com/scopecraft/command)** - ⭐ 174
   Scopecraft Command - A CLI and MCP server for Markdown-Driven Task Management (MDTM)

1848. **[mcp-server-starrocks](https://github.com/StarRocks/mcp-server-starrocks)** - ⭐ 174
   StarRocks MCP (Model Context Protocol) Server

1849. **[agentql-mcp](https://github.com/tinyfish-io/agentql-mcp)** - ⭐ 174
   Model Context Protocol server that integrates AgentQL's data extraction capabilities.

1850. **[awesome-x402](https://github.com/xpaysh/awesome-x402)** - ⭐ 174
   🚀 Curated list of x402 resources: HTTP 402 Payment Required protocol for blockchain payments, crypto micropayments, AI agents, API monetization. Includes SDKs (TypeScript, Python, Rust), examples, facilitators (Coinbase, Cloudflare), MCP integration, tutorials. Accept USDC payments with one line of code. Perfect for AI agent economy.

1851. **[codex-mcp-server](https://github.com/cexll/codex-mcp-server)** - ⭐ 173
   Codex Mcp Server

1852. **[keyboard-local](https://github.com/keyboard-dev/keyboard-local)** - ⭐ 173
   One MCP Server, All Your Apps, Privacy First

1853. **[mcp](https://github.com/MariaDB/mcp)** - ⭐ 173
   MariaDB MCP (Model Context Protocol) server implementation

1854. **[awesome-claude-dxt](https://github.com/milisp/awesome-claude-dxt)** - ⭐ 173
   Awesome Claude Desktop Extensions (dxt) (not only Claude) mcpb

1855. **[mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp)** - ⭐ 173
   A mongo db server for the model context protocol (MCP)

1856. **[mcp-access-point](https://github.com/sxhxliang/mcp-access-point)** - ⭐ 173
   Turn a web server into an MCP server in one click without making any code changes.

1857. **[toolsdk-mcp-registry](https://github.com/toolsdk-ai/toolsdk-mcp-registry)** - ⭐ 173
   MCPSDK.dev(ToolSDK.ai)'s Awesome MCP Servers and Packages Registry and Database with Structured JSON configurations. Supports OAuth2.1, DCR...

1858. **[bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js)** - ⭐ 172
   Bilibili video search MCP (Model Context Protocol) service - 哔哩哔哩视频搜索MCP服务

1859. **[gate22](https://github.com/aipotheosis-labs/gate22)** - ⭐ 172
   Open-source MCP gateway and control plane for teams to govern which tools agents can use, what they can do, and how it’s audited—across agentic IDEs like Cursor, or other agents and AI tools.

1860. **[gbox](https://github.com/babelcloud/gbox)** - ⭐ 172
   Cli and MCP for gbox. Enable AI agents to operate Android/Browser/Desktop like human.

1861. **[mcp-crash-course](https://github.com/emarco177/mcp-crash-course)** - ⭐ 171
   Hands-on crash course for the Model Context Protocol (MCP) with project-based branches on Streamable-HTTP, LangChain adapters, and Docker.

1862. **[mcp-apache-spark-history-server](https://github.com/kubeflow/mcp-apache-spark-history-server)** - ⭐ 171
   MCP Server and CLI for Apache Spark History Server. Debug Spark applications from AI agents, scripts, or the terminal.

1863. **[cli-mcp-server](https://github.com/MladenSU/cli-mcp-server)** - ⭐ 171
   Command line interface for MCP clients with secure execution and customizable security policies

1864. **[PolyMCP](https://github.com/poly-mcp/PolyMCP)** - ⭐ 171
   Polymcp provides a simple and efficient way to interact with MCP servers using custom agents

1865. **[dbt-llm-agent](https://github.com/pragunbhutani/dbt-llm-agent)** - ⭐ 171
   LLM based AI Agent to automate Data Analysis for dbt projects with remote MCP server

1866. **[clix](https://github.com/spideystreet/clix)** - ⭐ 171
   X from terminal. No API keys needed. Just plug your AI Agent.

1867. **[jmap-mcp](https://github.com/wyattjoh/jmap-mcp)** - ⭐ 171
   A Model Context Protocol (MCP) server that provides tools for interacting with JMAP (JSON Meta Application Protocol) email servers. Built with Deno and using the jmap-jam client library.

1868. **[Text2Sql.Net](https://github.com/AIDotNet/Text2Sql.Net)** - ⭐ 170
   Text2Sql.Net 是一个使用DotNet和Semantic Kernel开发的Text2Sql工具

1869. **[mcp-shark](https://github.com/mcp-shark/mcp-shark)** - ⭐ 170
   Wireshark-like forensic analysis for Model Context Protocol communications  Capture, inspect, and investigate all HTTP requests and responses between your IDE and MCP servers

1870. **[OverleafMCP](https://github.com/mjyoo2/OverleafMCP)** - ⭐ 170
   Model Context Protocol (MCP) server that lets AI assistants read Overleaf projects, parse LaTeX document structure, and push          section-level edits back via Git. Compatible with Claude Desktop, Cursor, Windsurf, and any MCP client.

1871. **[mcp-solver](https://github.com/szeider/mcp-solver)** - ⭐ 170
   Model Context Protocol (MCP) server for constraint optimization and solving"

1872. **[dify-mcp-client](https://github.com/3dify-project/dify-mcp-client)** - ⭐ 169
   MCP Client as an Agent Strategy Plugin. Support GUI operation via UI-TARS-SDK.

1873. **[openclaw-mcp](https://github.com/freema/openclaw-mcp)** - ⭐ 169
   🦞 MCP server for OpenClaw - secure bridge between Claude.ai and your self-hosted OpenClaw assistant with OAuth2 authentication

1874. **[y-gui](https://github.com/luohy15/y-gui)** - ⭐ 169
   A Tiny Web Chat App for AI Models with MCP Client Support

1875. **[memtrace-public](https://github.com/syncable-dev/memtrace-public)** - ⭐ 169
   Structural memory for AI coding agents. Bi-temporal graph, MCP-native, zero LLM calls. Cursor · Claude Code · Codex · Hermes · VS Code · Windsurf.

1876. **[xhs-mcp-server](https://github.com/aicu-icu/xhs-mcp-server)** - ⭐ 168
   小红书MCP服务器 | 秒级工具调用执行，笔记用户搜索、通知消息监控等；打造2026最简单、最快速、最精准、最好用的小红书MCPServer！

1877. **[c4-genai-suite](https://github.com/codecentric/c4-genai-suite)** - ⭐ 168
   c4 GenAI Suite

1878. **[domscribe](https://github.com/patchorbit/domscribe)** - ⭐ 168
   Domscribe is a pixel-to-code development tool that bridges the gap between running web applications and their source code.

1879. **[sibyl-research-system](https://github.com/Sibyl-Research-Team/sibyl-research-system)** - ⭐ 168
   Fully Autonomous AI Research System with Self-Evolution, built natively on Claude Code

1880. **[MegaMemory](https://github.com/0xK3vin/MegaMemory)** - ⭐ 167
   Persistent project knowledge graph for coding agents. MCP server with semantic search, in-process embeddings, and web explorer.

1881. **[agnix](https://github.com/agent-sh/agnix)** - ⭐ 167
   The missing linter and lsp for AI coding assistants. Validate CLAUDE.md, AGENTS.md, SKILL.md, hooks, MCP. Plugin for all major IDEs included, with autofixes.

1882. **[refref](https://github.com/amicalhq/refref)** - ⭐ 167
   🌟 Open Source Referral and Affiliate Marketing Platform - Launch your referral program in minutes!

1883. **[paper-search-mcp-nodejs](https://github.com/Dianel555/paper-search-mcp-nodejs)** - ⭐ 167
   A Node.js implementation of the Model Context Protocol (MCP) server for searching and downloading academic papers from multiple sources, including **Web of Science**, arXiv, and more.

1884. **[In-Memoria](https://github.com/pi22by7/In-Memoria)** - ⭐ 167
   Persistent Intelligence Infrastructure for AI Agents

1885. **[google-drive-mcp](https://github.com/piotr-agier/google-drive-mcp)** - ⭐ 167
   A Model Context Protocol (MCP) server that provides secure integration with Google Drive, Docs, Sheets, Slides and Calendar. It allows Claude Desktop and other MCP clients to manage files in Google Drive through a standardized interface.

1886. **[toolbase](https://github.com/Toolbase-AI/toolbase)** - ⭐ 167
   A desktop application that adds powerful tools to Claude and AI platforms

1887. **[knowledge-base-server](https://github.com/willynikes2/knowledge-base-server)** - ⭐ 167
   Make every AI agent you use smarter. Persistent memory with SQLite FTS5, MCP server, Obsidian sync, and self-learning intelligence pipeline.

1888. **[mcp-server-weread](https://github.com/ChenyqThu/mcp-server-weread)** - ⭐ 166

1889. **[CyberStrike](https://github.com/CyberStrikeus/CyberStrike)** - ⭐ 166
   AI-powered offensive security agent. Autonomous pentesting with 13+ specialized agents, 120+ OWASP test cases, 15+ LLM providers, and Bolt remote tool servers. Your AI red team.

1890. **[mcp-server-langfuse](https://github.com/langfuse/mcp-server-langfuse)** - ⭐ 166
   Model Context Protocol (MCP) Server for Langfuse Prompt Management. This server allows you to access and manage your Langfuse prompts through the Model Context Protocol.

1891. **[UnityNaturalMCP](https://github.com/notargs/UnityNaturalMCP)** - ⭐ 166
   UnityNaturalMCP is an MCP server implementation for Unity that aims for a "natural" user experience.

1892. **[instagram_dm_mcp](https://github.com/trypeggy/instagram_dm_mcp)** - ⭐ 166
   Instagram Direct messages MCP

1893. **[mengram](https://github.com/alibaizhanov/mengram)** - ⭐ 165
   Human-like memory for AI agents — semantic, episodic & procedural. Experience-driven procedures that learn from failures. Free API, Python & JS SDKs, LangChain, CrewAI & OpenClaw integrations.

1894. **[mcp-dock](https://github.com/OldJii/mcp-dock)** - ⭐ 165
   MCP Server & Config Manager for 14 AI Clients — Cursor, VS Code, Claude Code, Gemini CLI, Windsurf, Zed, TRAE, Kiro, JetBrains & more. 8500+ servers, 4400+ skills.

1895. **[tiktok-mcp](https://github.com/Seym0n/tiktok-mcp)** - ⭐ 165
   Model Context Protocol (MCP) with TikTok integration

1896. **[ggsrun](https://github.com/tanaikech/ggsrun)** - ⭐ 165
   A high-performance concurrent Google Drive CLI and native Model Context Protocol (MCP) Server for LLM/AI agents. Natively execute Google Apps Script (GAS) dynamically, recursive upload/download, and manage Drive infrastructure.

1897. **[Axon.MCP.Server](https://github.com/ali-kamali/Axon.MCP.Server)** - ⭐ 164
   Transform your codebase into an intelligent knowledge base for AI-powered development with Cursor IDE, Google AntiGravity, and MCP-enabled assistants

1898. **[mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed)** - ⭐ 164
   MCP server for searching and querying PubMed medical papers/research database

1899. **[Log-Analyzer-with-MCP](https://github.com/awslabs/Log-Analyzer-with-MCP)** - ⭐ 164
   A Model Context Protocol (MCP) server that provides AI assistants access to AWS CloudWatch Logs for analysis, searching, and correlation

1900. **[recall](https://github.com/joseairosa/recall)** - ⭐ 164
   Persistent cross-session memory for Claude & AI agents. Self-host on Redis/Valkey, or use the managed SaaS at recallmcp.com.

1901. **[ServiceGraph](https://github.com/nostrband/ServiceGraph)** - ⭐ 164
   AI Agent skills for a structured catalog of 100k+ US professional-services firms

1902. **[awesome-a2a](https://github.com/pab1it0/awesome-a2a)** - ⭐ 164
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place.

1903. **[memorizer](https://github.com/petabridge/memorizer)** - ⭐ 164
   Vector-search powered agent memory MCP server

1904. **[mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow)** - ⭐ 164

1905. **[eShopLite](https://github.com/Azure-Samples/eShopLite)** - ⭐ 163
   eShopLite is a set of reference .NET applications implementing an eCommerce site with features like Semantic Search, MCP, Reasoning models and more.

1906. **[data-verify-mcp](https://github.com/CCCpan/data-verify-mcp)** - ⭐ 163
   中国数据核验 MCP Server | 身份核验/企业查询/车辆信息/OCR识别/风险评估 | 10个Tool覆盖5大类 | 微信: chenganp | 邮箱: 345048305@qq.com

1907. **[mcp-codex-dev](https://github.com/FYZAFH/mcp-codex-dev)** - ⭐ 163
   MCP Server for Codex CLI integration - stateful code writing and review workflows

1908. **[remote-mcp-server](https://github.com/gleanwork/remote-mcp-server)** - ⭐ 163
   Remote MCP Server that securely connects Enterprise context with your LLM, IDE, or agent platform of choice.

1909. **[code-assistant](https://github.com/stippi/code-assistant)** - ⭐ 163
   An LLM-powered, autonomous coding assistant. Also offers an MCP and ACP mode.

1910. **[mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server)** - ⭐ 162
   A Model Context Protocol server for MySQL database operations

1911. **[turbo-flow](https://github.com/marcuspat/turbo-flow)** - ⭐ 162
   Advanced Agentic Development Environment Supporting Devpods, Rackspace Spot Instances, Github Codespaces, Google Cloud Shell, and more!  Features 600+ AI subagents, Claude Flow, SPARC methodology, and automatic context loading! Deploy intelligent multi-agent swarms, coordinate autonomous workflows.

1912. **[mcp-rubber-duck](https://github.com/nesquikm/mcp-rubber-duck)** - ⭐ 162
   An MCP server that acts as a bridge to query multiple OpenAI-compatible LLMs with MCP tool access. Just like rubber duck debugging, explain your problems to various AI "ducks" who can actually research and get different perspectives!

1913. **[mcp-client-slackbot](https://github.com/sooperset/mcp-client-slackbot)** - ⭐ 162
   Simple Slackbot MCP Client

1914. **[XPack-MCP-Marketplace](https://github.com/xpack-ai/XPack-MCP-Marketplace)** - ⭐ 162
   The world’s first open-source MCP monetization platform, to quickly create and sell your own MCP server in just minutes. | XPack 是全球首个开源 MCP 交易平台，帮助你在10分钟内快速搭建自己的 MCP 商店并立刻开始销售 MCP 服务。

1915. **[mcp-summarizer](https://github.com/0xshellming/mcp-summarizer)** - ⭐ 161
   MCP Server for AI Summarization

1916. **[mcp-bsl-platform-context](https://github.com/alkoleft/mcp-bsl-platform-context)** - ⭐ 161
   MCP сервер для AI-ассистентов (справка по синтаксису и объектной модели 1С:Предприятие)

1917. **[isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp)** - ⭐ 161
   Isaac Simulation MCP Extension and Server

1918. **[mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate)** - ⭐ 161
   MCP (Model Context Protocol) server for Weaviate

1919. **[zig-mcp](https://github.com/zig-wasm/zig-mcp)** - ⭐ 161
   Model Context Protocol (MCP) server that provides up-to-date documentation for the Zig programming language standard library and builtin functions

1920. **[spotinfo](https://github.com/alexei-led/spotinfo)** - ⭐ 160
   CLI for exploring AWS EC2 Spot inventory. Inspect AWS Spot instance types, saving, price, and interruption frequency.

1921. **[awesome-ai-for-economists](https://github.com/hanlulong/awesome-ai-for-economists)** - ⭐ 160
   A curated list of AI tools, libraries, and resources for economics research, teaching, and policy analysis. Maintained by the OpenEcon team.

1922. **[gis-mcp](https://github.com/mahdin75/gis-mcp)** - ⭐ 160
   A Model Context Protocol (MCP) server implementation that connects Large Language Models (LLMs) to GIS operations using GIS libraries, enabling AI assistants to perform geospatial operations and transformations.

1923. **[scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server)** - ⭐ 160
   Scrapeless Mcp Server

1924. **[solana-mcp](https://github.com/sendaifun/solana-mcp)** - ⭐ 160
   A Model Context Protocol server for interacting with the Solana blockchain, powered by the Solana Agent Kit (https://github.com/sendaifun/solana-agent-kit)

1925. **[Text2Sql.Net](https://github.com/shuyu-labs/Text2Sql.Net)** - ⭐ 160
   Text2Sql.Net 是一个使用DotNet和Semantic Kernel开发的Text2Sql工具

1926. **[mcp-server-manifest](https://github.com/Zomato/mcp-server-manifest)** - ⭐ 160

1927. **[compliant-llm](https://github.com/fiddlecube/compliant-llm)** - ⭐ 159
   Build Secure and Compliant AI agents and MCP Servers. YC W23

1928. **[glade-mcp](https://github.com/Glade-tool/glade-mcp)** - ⭐ 159
   Connect any MCP-compatible AI client (Claude Code, Cursor, Windsurf) to Unity or Godot. 235+ granular tools, a Unity-aware system prompt, game design document project context, script semantic search, and skill calibration.

1929. **[typst-mcp](https://github.com/johannesbrandenburger/typst-mcp)** - ⭐ 159
   Typst MCP Server is an MCP (Model Context Protocol) implementation that helps AI models interact with Typst, a markup-based typesetting system. The server provides tools for converting between LaTeX and Typst, validating Typst syntax, and generating images from Typst code.

1930. **[FirstData](https://github.com/MLT-OSS/FirstData)** - ⭐ 159
   The World's Most Comprehensive, Authoritative, and Structured Open Source Data Source Knowledge Base

1931. **[PocketRisu](https://github.com/PocketRisu/PocketRisu)** - ⭐ 159
   Self-hosted AI roleplay chat platform you run on your PC or personal server, forked from Risuai

1932. **[actual-mcp](https://github.com/s-stefanov/actual-mcp)** - ⭐ 159
   Model Context Protocol for Actual Budget API

1933. **[resolve-mcp](https://github.com/barckley75/resolve-mcp)** - ⭐ 158
   Connect DaVinci Resolve Studio to Claude AI through the Model Context Protocol (MCP)

1934. **[hanzi-browse](https://github.com/hanzili/hanzi-browse)** - ⭐ 158
   let any ai agent use the local browser

1935. **[cursor-notebook-mcp](https://github.com/jbeno/cursor-notebook-mcp)** - ⭐ 158
   Model Context Protocol (MCP) server designed to allow AI agents within Cursor to interact with Jupyter Notebook (.ipynb) files

1936. **[claude-code-open](https://github.com/kill136/claude-code-open)** - ⭐ 158
   Open source AI coding platform with Web IDE, multi-agent system, 37+ tools, MCP protocol. MIT licensed.

1937. **[spiceflow](https://github.com/remorses/spiceflow)** - ⭐ 158
   Simple API & React framework, fully type safe, OpenAPI, RSC, MCP, type safe client, streaming with SSE

1938. **[bocha-search-mcp](https://github.com/BochaAI/bocha-search-mcp)** - ⭐ 157
   Bocha Search MCP Server.

1939. **[zettelkasten-mcp](https://github.com/entanglr/zettelkasten-mcp)** - ⭐ 157
   A Model Context Protocol (MCP) server that implements the Zettelkasten knowledge management methodology, allowing you to create, link, explore and synthesize atomic notes through Claude and other MCP-compatible clients.

1940. **[wa_llm](https://github.com/ilanbenb/wa_llm)** - ⭐ 157
   A WhatsApp bot that can participate in group conversations, powered by AI. The bot monitors group messages and responds when mentioned.

1941. **[alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server)** - ⭐ 156

1942. **[SwiftMCP](https://github.com/Cocoanetics/SwiftMCP)** - ⭐ 156
   Model Context Protocol Server for Swift

1943. **[fetch-mcp](https://github.com/egoist/fetch-mcp)** - ⭐ 156
   An MCP server for fetching URLs / Youtube video transcript.

1944. **[make-mcp-server](https://github.com/integromat/make-mcp-server)** - ⭐ 156
   Make MCP Server

1945. **[refref](https://github.com/refrefhq/refref)** - ⭐ 156
   🌟 Open Source Referral and Affiliate Marketing Platform - Launch your referral program in minutes!

1946. **[web3-research-mcp](https://github.com/aaronjmars/web3-research-mcp)** - ⭐ 155
   Deep Research for crypto - free & fully local

1947. **[chatgpt-copilot](https://github.com/feiskyer/chatgpt-copilot)** - ⭐ 155
   ChatGPT Copilot Extension for Visual Studio Code

1948. **[payram-mcp](https://github.com/PayRam/payram-mcp)** - ⭐ 155
   Connect to hosted payram helper at: https://mcp.payram.com

1949. **[mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce)** - ⭐ 155
   Salesforce MCP Server

1950. **[mcp-1panel](https://github.com/1Panel-dev/mcp-1panel)** - ⭐ 154
   mcp-1panel is an implementation of the Model Context Protocol (MCP) server for 1Panel.

1951. **[google-workspace-mcp](https://github.com/aaronsb/google-workspace-mcp)** - ⭐ 154
   A Model Context Protocol (MCP) server that provides authenticated access to Google Workspace APIs, offering integrated Authentication, Gmail, Calendar, and Drive functionality

1952. **[mcp-server-example](https://github.com/alejandro-ao/mcp-server-example)** - ⭐ 154
   A simple MCP server to search for documentation (tutorial)

1953. **[notion-mcp-server](https://github.com/awkoy/notion-mcp-server)** - ⭐ 154
   Notion MCP server for Claude, Cursor, ChatGPT & Claude Desktop. Connect AI agents to Notion via Model Context Protocol — pages, databases, blocks, comments, files.

1954. **[zotero-mcp](https://github.com/kujenga/zotero-mcp)** - ⭐ 154
   Model Context Protocol (MCP) server for the Zotero API, in Python

1955. **[mcp-server-metamcp](https://github.com/metatool-ai/mcp-server-metamcp)** - ⭐ 154
   MCP Server MetaMCP manages all your other MCPs in one MCP.

1956. **[python-mcp-server-client](https://github.com/GobinFan/python-mcp-server-client)** - ⭐ 153
   支持查询主流agent框架技术文档的MCP server（支持stdio和sse两种传输协议）, 支持 langchain、llama-index、autogen、agno、openai-agents-sdk、mcp-doc、camel-ai 和 crew-ai

1957. **[GEmojiSharp](https://github.com/hlaueriksson/GEmojiSharp)** - ⭐ 153
   :octocat: GitHub Emoji for C#, dotnet and beyond

1958. **[OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP)** - ⭐ 153
   Connect any Open Data to any LLM with Model Context Protocol.

1959. **[ollama-mcp](https://github.com/rawveg/ollama-mcp)** - ⭐ 153
   An MCP Server for Ollama

1960. **[k8s-mcp-server](https://github.com/reza-gholizade/k8s-mcp-server)** - ⭐ 153
   Manage Your Kubernetes Cluster with k8s mcp-server

1961. **[hypertool-mcp](https://github.com/toolprint/hypertool-mcp)** - ⭐ 153
   Dynamically expose tools from proxied servers based on an Agent Persona

1962. **[agentanycast](https://github.com/AgentAnycast/agentanycast)** - ⭐ 152
   Connect AI agents across any network — zero config, encrypted, skill-based routing

1963. **[node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp)** - ⭐ 152
   A Node.js–based Model Context Protocol server that spins up disposable Docker containers to execute arbitrary JavaScript.

1964. **[guidance-for-deploying-model-context-protocol-servers-on-aws](https://github.com/aws-solutions-library-samples/guidance-for-deploying-model-context-protocol-servers-on-aws)** - ⭐ 152
   This Guidance demonstrates how to securely run Model Context Protocol (MCP) servers on the AWS Cloud using containerized architecture. It helps organizations implement industry-standard OAuth 2.0 authentication while protecting server deployments with multiple security layers, including content delivery networks and web application firewalls.

1965. **[mcp-discord](https://github.com/hanweg/mcp-discord)** - ⭐ 152
   MCP server for discord bot

1966. **[google-surf-mcp](https://github.com/HarimxChoi/google-surf-mcp)** - ⭐ 152
   ✨Anti-Bot Search MCP: No API Key✨

1967. **[claude-code-karma](https://github.com/JayantDevkar/claude-code-karma)** - ⭐ 152
   Dashboard for monitoring claude code sessions.

1968. **[mcp-outline](https://github.com/Vortiago/mcp-outline)** - ⭐ 152
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Outline documentation services.

1969. **[aicode-toolkit](https://github.com/AgiFlow/aicode-toolkit)** - ⭐ 151
   Toolkit for Coding Agents to work reliably with repo of any size.

1970. **[unreal-analyzer-mcp](https://github.com/ayeletstudioindia/unreal-analyzer-mcp)** - ⭐ 151
   MCP server for Unreal Engine 5

1971. **[eion](https://github.com/eiondb/eion)** - ⭐ 151
   Shared Memory Storage for Multi-Agent Systems

1972. **[eclipse-chatgpt-plugin](https://github.com/gradusnikov/eclipse-chatgpt-plugin)** - ⭐ 151
   Eclipse IDE as an MCP Server for AI Agents

1973. **[mcp-gateway](https://github.com/lightconetech/mcp-gateway)** - ⭐ 151
   A gateway demo for MCP SSE Server

1974. **[mcp-server-serper](https://github.com/marcopesani/mcp-server-serper)** - ⭐ 151
   Serper MCP Server supporting search and webpage scraping

1975. **[mcp-interviewer](https://github.com/microsoft/mcp-interviewer)** - ⭐ 151
   Catch MCP server issues before your agents do.

1976. **[decipher-research-agent](https://github.com/mtwn105/decipher-research-agent)** - ⭐ 151
   Turn topics, links, and files into AI-generated research notebooks — summarize, explore, and ask anything.

1977. **[any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp)** - ⭐ 151
   MCP Server for using any LLM as a Tool

1978. **[claude-desktop-extension-bear-notes](https://github.com/vasylenko/claude-desktop-extension-bear-notes)** - ⭐ 151
   Claude Desktop extension with bundled MCP Server for Bear note taking app

1979. **[tinymcp](https://github.com/golioth/tinymcp)** - ⭐ 150
   Let LLMs control embedded devices via the Model Context Protocol.

1980. **[aai-gateway](https://github.com/gybob/aai-gateway)** - ⭐ 150
   Install MCP servers and skills once, share across all your AI agents — with 90% less context overhead.

1981. **[relay](https://github.com/prism-php/relay)** - ⭐ 150
   An MCP client tool for Prism

1982. **[website-downloader](https://github.com/pskill9/website-downloader)** - ⭐ 150
   MCP server to download entire websites

1983. **[mcp-metatrader5-server](https://github.com/Qoyyuum/mcp-metatrader5-server)** - ⭐ 150
   A Model Context Protocol (MCP) server for interacting with the MetaTrader 5 trading platform. This server provides AI assistants with tools and resources to access market data, perform trading operations, and analyze trading history.

1984. **[mcp_server_exe](https://github.com/shadowcz007/mcp_server_exe)** - ⭐ 150
   小智 & Cursor 的 MCP 启动器 - MCP For Cursor&xiaozhi。打包成可执行文件。Turn MCP server into an executable file

1985. **[mcp-client-go](https://github.com/yincongcyincong/mcp-client-go)** - ⭐ 150
   mcp client for Go (Golang). Integrate multiple  Model Context Protocol (MCP) servers

1986. **[quick-data-mcp](https://github.com/disler/quick-data-mcp)** - ⭐ 149
   Prompt focused MCP Server for .json and .csv agentic data analytics for Claude Code

1987. **[LMStudio-MCP](https://github.com/infinitimeless/LMStudio-MCP)** - ⭐ 149
   A Model Control Protocol (MCP) server that allows Claude to communicate with locally running LLM models via LM Studio.

1988. **[Express-REST-API-and-MCP-Server-Framework](https://github.com/iolufemi/Express-REST-API-and-MCP-Server-Framework)** - ⭐ 149
   Express REST API and MCP Server Framework is a comprehensive development framework for building RESTful APIs and MCP servers with Express.js. It provides a complete template for creating production-ready APIs using Node.js, Express, Mongoose (MongoDB), and Sequelize (SQL databases).

1989. **[MCPHub-Desktop](https://github.com/Jeamee/MCPHub-Desktop)** - ⭐ 149
   Desktop APP for Discover and Install MCP Servers

1990. **[mcp-toolkit](https://github.com/nuxt-modules/mcp-toolkit)** - ⭐ 149
   Create MCP servers directly in your Nuxt application. Define tools, resources, and prompts with a simple and intuitive API.

1991. **[UnityMCPIntegration](https://github.com/quazaai/UnityMCPIntegration)** - ⭐ 149
   Enable AI Agents to Control Unity

1992. **[regenerator2000](https://github.com/ricardoquesada/regenerator2000)** - ⭐ 149
   An interactive disassembler for the CPU 6502, focused mostly on Commodore 8-bit computers. Features a TUI with modern features like x-ref, undo/redo, arrows, keyboard-driven, mcp server, VICE debugger and more!

1993. **[figma-mcp-server](https://github.com/TimHolden/figma-mcp-server)** - ⭐ 149
   Model Context Protocol server implementation for Figma API

1994. **[CreatorBox](https://github.com/xiesx123/CreatorBox)** - ⭐ 149
   🚀🎬灵活、高效、可扩展，专属剪辑配音工具箱，释放创作潜力 . Flexible, efficient, and scalable toolbox for editing and dubbing, unleashing creative potential

1995. **[raindrop-mcp](https://github.com/adeze/raindrop-mcp)** - ⭐ 148
   Raindrop MCP Server

1996. **[play-store-mcp](https://github.com/antoniolg/play-store-mcp)** - ⭐ 148
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1997. **[pubmearch](https://github.com/Darkroaster/pubmearch)** - ⭐ 148
   A PubMed MCP server.

1998. **[ultimate_mcp_client](https://github.com/Dicklesworthstone/ultimate_mcp_client)** - ⭐ 148
   Async Python client for the Model Context Protocol with interactive CLI and reactive Web UI, connecting AI models to MCP servers via stdio and SSE

1999. **[math-mcp](https://github.com/EthanHenrickson/math-mcp)** - ⭐ 148
   A Model Context Protocol (MCP) server that provides basic mathematical and statistical functions to Large Language Models (LLMs). This server enables LLMs to perform accurate numerical calculations through a simple API.

2000. **[mcp-server-calculator](https://github.com/githejie/mcp-server-calculator)** - ⭐ 148
   A Model Context Protocol server for calculating.

2001. **[comet-mcp](https://github.com/hanzili/comet-mcp)** - ⭐ 148
   MCP Server connecting to Perplexity Comet browser

2002. **[paiml-mcp-agent-toolkit](https://github.com/paiml/paiml-mcp-agent-toolkit)** - ⭐ 148
   Pragmatic AI Labs MCP Agent Toolkit - An MCP Server designed to make code with agents more deterministic

2003. **[plan-cascade](https://github.com/Taoidle/plan-cascade)** - ⭐ 148
   AI-powered cascading development framework. Decompose complex projects into parallel executable tasks with auto-generated PRDs, design docs, and multi-agent collaboration (Claude Code, Codex, Aider).

2004. **[dedalus-mcp-python](https://github.com/dedalus-labs/dedalus-mcp-python)** - ⭐ 147
   A simple and performant Model Context Protocol framework for Python.

2005. **[meta_skill](https://github.com/Dicklesworthstone/meta_skill)** - ⭐ 147
   Local-first skill management platform for AI coding agents: dual SQLite+Git persistence, semantic search, bandit-optimized suggestions, and MCP integration

2006. **[loki-mcp](https://github.com/grafana/loki-mcp)** - ⭐ 147
   An MCP ( Model Context Protocol ) Server for Grafana Loki

2007. **[codeql-mcp](https://github.com/JordyZomer/codeql-mcp)** - ⭐ 147
   This project runs a Model Context Protocol (MCP) server that wraps the CodeQL query server. It enables tools like [Cursor](https://cursor.sh/) or AI agents to interact with CodeQL through structured commands.

2008. **[adloop](https://github.com/kLOsk/adloop)** - ⭐ 147
   An MCP server that gives your AI assistant read + write access to Google Ads and GA4 — with safety guardrails that prevent accidental spend.

2009. **[claude-prompts](https://github.com/minipuft/claude-prompts)** - ⭐ 147
   MCP prompt template server: hot-reload, thinking frameworks, quality gates

2010. **[kom](https://github.com/weibaohui/kom)** - ⭐ 147
   kom 是一个用于 Kubernetes 操作的工具，SDK级的kubectl、client-go的使用封装。并且支持作为管理k8s 的 MCP server。 它提供了一系列功能来管理 Kubernetes 资源，包括创建、更新、删除和获取资源，甚至使用SQL查询k8s资源。这个项目支持多种 Kubernetes 资源类型的操作，并能够处理自定义资源定义（CRD）。 通过使用 kom，你可以轻松地进行资源的增删改查和日志获取以及操作POD内文件等动作。

2011. **[mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket)** - ⭐ 146
   Node.js/TypeScript MCP server for Atlassian Bitbucket. Enables AI systems (LLMs) to interact with workspaces, repositories, and pull requests via tools (list, get, comment, search). Connects AI directly to version control workflows through the standard MCP interface.

2012. **[postman-mcp-server](https://github.com/delano/postman-mcp-server)** - ⭐ 146
   An MCP server that provides access to Postman.

2013. **[openwebui-extensions](https://github.com/Fu-Jie/openwebui-extensions)** - ⭐ 146
   A collection of enhancements, plugins, and prompts for Open WebUI, developed and curated for personal use to extend functionality and improve experience.

2014. **[bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp)** - ⭐ 146
   Bitbucket MCP - A Model Context Protocol (MCP) server for integrating with Bitbucket Cloud and Server APIs

2015. **[mssql-mcp](https://github.com/Aaronontheweb/mssql-mcp)** - ⭐ 145
   MSSQL Server MCP implementation written in C#

2016. **[MCP-PostgreSQL-Ops](https://github.com/call518/MCP-PostgreSQL-Ops)** - ⭐ 145
   🔍Professional MCP server for PostgreSQL operations & monitoring: 30+ extension-independent tools for performance analysis, table bloat detection, autovacuum monitoring, schema introspection, and database management. Supports PostgreSQL 12+.

2017. **[ultimate_mcp_server](https://github.com/Dicklesworthstone/ultimate_mcp_server)** - ⭐ 145
   Comprehensive MCP server exposing dozens of capabilities to AI agents: multi-provider LLM delegation, browser automation, document processing, vector ops, and cognitive memory systems

2018. **[linkedin-mcp-server](https://github.com/eliasbiondo/linkedin-mcp-server)** - ⭐ 145
   🔗 A Model Context Protocol (MCP) server for LinkedIn — search people, companies, and jobs, scrape profiles, and get structured data via any MCP-compatible AI client.

2019. **[goku](https://github.com/jcaromiq/goku)** - ⭐ 145
   Goku is an HTTP load testing application written in Rust

2020. **[frontmcp](https://github.com/agentfront/frontmcp)** - ⭐ 144
   TypeScript-first framework for the Model Context Protocol (MCP). You write clean, typed code; FrontMCP handles the protocol, transport, DI, session/auth, and execution flow.

2021. **[uaip](https://github.com/concierge-hq/uaip)** - ⭐ 144
   Universal Agent Interactive Protocol (UAIP) is an open standard for ordered and verifiable interactions between autonomous services and AI agents.

2022. **[powerpoint](https://github.com/supercurses/powerpoint)** - ⭐ 144
   A MCP Server for creating Powerpoint Presentations

2023. **[anubis-mcp](https://github.com/zoedsoupe/anubis-mcp)** - ⭐ 144
   Elixir Model Context Protocol (MCP) SDK (hermes-mcp fork)

2024. **[mcp-servers](https://github.com/charIesding/mcp-servers)** - ⭐ 143
   mcp server implementations

2025. **[esp-mcp](https://github.com/horw/esp-mcp)** - ⭐ 143
   Centralize ESP32 related commands and simplify getting started with seamless, LLM-driven interaction and help.

2026. **[Gemini-mcp](https://github.com/LKbaba/Gemini-mcp)** - ⭐ 143
   MCP server implementation for Google's Gemini API

2027. **[ReActMCP](https://github.com/mshojaei77/ReActMCP)** - ⭐ 143
   ReActMCP is a reactive MCP client that empowers AI assistants to instantly respond with real-time, Markdown-formatted web search insights powered by the Exa API.

2028. **[mcp-memory](https://github.com/Puliczek/mcp-memory)** - ⭐ 143
   🔥🖥️ MCP Memory is a MCP Server that gives MCP Clients (Cursor, Claude, Windsurf and more) the ability to remember information about users (preferences, behaviors) across conversations.

2029. **[mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server)** - ⭐ 142
   A Model Context Protocol (MCP) server that provides secure, read-only access to BigQuery datasets. Enables Large Language Models (LLMs) to safely query and analyze data through a standardized interface.

2030. **[mcpd](https://github.com/mozilla-ai/mcpd)** - ⭐ 142
   Declaratively define and run required tools across environments, from local development to containerized cloud deployments.

2031. **[mcp-k8s](https://github.com/silenceper/mcp-k8s)** - ⭐ 142
   A Kubernetes MCP (Model Control Protocol) server that enables interaction with Kubernetes clusters through MCP tools.

2032. **[openagent](https://github.com/Th0rgal/openagent)** - ⭐ 142
   Self-hosted orchestrator for AI autonomous agents. Run Claude Code & Open Code in isolated linux workspaces. Manage your skills, configs and encrypted secrets with a git repo.

2033. **[jupyter-ai-agents](https://github.com/datalayer/jupyter-ai-agents)** - ⭐ 141
   🪐 🤖 AI Agents for JupyterLab with 🔧 MCP tools - Chat interface for optimized notebook interaction and code execution.

2034. **[reddit-mcp-server](https://github.com/eliasbiondo/reddit-mcp-server)** - ⭐ 141
   🔗 A zero-config Model Context Protocol (MCP) server for Reddit — search posts, browse subreddits, scrape user activity, and get structured data via any MCP-compatible AI client. No API keys or authentication needed.

2035. **[ig-mcp](https://github.com/jlbadano/ig-mcp)** - ⭐ 141
   A production-ready Model Context Protocol (MCP) server that enables AI applications to seamlessly interact with Instagram Business accounts.

2036. **[Polymcp](https://github.com/poly-mcp/Polymcp)** - ⭐ 141
   Polymcp provides a simple and efficient way to interact with MCP servers using custom agents

2037. **[rust-mcp-filesystem](https://github.com/rust-mcp-stack/rust-mcp-filesystem)** - ⭐ 141
   Blazing-fast, asynchronous MCP server for seamless filesystem operations.

2038. **[MCP-X](https://github.com/TimeCyber/MCP-X)** - ⭐ 141
   这是一个MCP客户端，让你轻松配置各个大模型，对接各种MCP Server而开发。This is an MCP client that allows you to easily configure various large models and develop interfaces with various MCP servers.

2039. **[gtasks-mcp](https://github.com/zcaceres/gtasks-mcp)** - ⭐ 141
   A Google Tasks Model Context Protocol Server for Claude

2040. **[gRPC-zig](https://github.com/ziglana/gRPC-zig)** - ⭐ 141
   blazigly fast gRPC/MCP client & server implementation in zig

2041. **[datagov-mcp](https://github.com/aviveldan/datagov-mcp)** - ⭐ 140
   MCP server for Israel Government Data

2042. **[claudeus-wp-mcp](https://github.com/deus-h/claudeus-wp-mcp)** - ⭐ 140
   Claudeus WordPress MCP Server

2043. **[Hegelion](https://github.com/Hmbown/Hegelion)** - ⭐ 140
   Dialectical reasoning architecture for LLMs (Thesis → Antithesis → Synthesis)

2044. **[SecureMCP](https://github.com/makalin/SecureMCP)** - ⭐ 140
   SecureMCP is a security auditing tool designed to detect vulnerabilities and misconfigurations in applications using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction). It proactively identifies threats like OAuth token leakage, prompt injection vulnerabilities, rogue MCP servers, and tool poisoning attacks.

2045. **[mcp-server-datadog](https://github.com/winor30/mcp-server-datadog)** - ⭐ 140

2046. **[Awesome-MCP](https://github.com/AlexMili/Awesome-MCP)** - ⭐ 139
   Awesome ModelContextProtocol resources - A curated list of MCP resources

2047. **[rails-ai-context](https://github.com/crisnahine/rails-ai-context)** - ⭐ 139
   38 MCP tools that give AI agents live access to your Rails schema, models, routes & conventions. Works with Claude Code, Cursor, Copilot, OpenCode, Codex CLI. Zero config.

2048. **[ksail](https://github.com/devantler-tech/ksail)** - ⭐ 139
   Tool for creating, maintaining and operating Kubernetes clusters with ease.

2049. **[graphiti-mcp-server](https://github.com/gifflet/graphiti-mcp-server)** - ⭐ 139
   Graphiti MCP Server

2050. **[glade-mcp-unity](https://github.com/Glade-tool/glade-mcp-unity)** - ⭐ 139
   Connect any MCP-compatible AI client (Claude Code, Cursor, Windsurf) to your Unity Editor. 235+ granular tools, a Unity-aware system prompt, game design document project context, script semantic search, and skill calibration.

2051. **[forgemax](https://github.com/postrv/forgemax)** - ⭐ 139
   Code Mode inspired local sandboxed MCP Gateway - collapses N servers x M tools into 2 tools (~1,000 tokens)

2052. **[systemprompt-code-orchestrator](https://github.com/systempromptio/systemprompt-code-orchestrator)** - ⭐ 139
     MCP server for orchestrating AI coding agents (Claude Code CLI & Gemini CLI). Features task management, process execution, Git integration, and dynamic resource discovery. Full TypeScript implementation with Docker support and Cloudflare Tunnel integration.

2053. **[charlotte](https://github.com/TickTockBent/charlotte)** - ⭐ 139
   Token-efficient browser MCP server — structured web pages for AI agents, not raw accessibility dumps

2054. **[hayhooks](https://github.com/deepset-ai/hayhooks)** - ⭐ 138
   Easily deploy Haystack pipelines as REST APIs and MCP Tools.

2055. **[dify-plugin-agent-mcp_sse](https://github.com/junjiem/dify-plugin-agent-mcp_sse)** - ⭐ 138
   Dify 1.0 Plugin Support MCP Tools Agent strategies

2056. **[mcp-read-website-fast](https://github.com/just-every/mcp-read-website-fast)** - ⭐ 138
   Quickly reads webpages and converts to markdown for fast, token efficient web scraping

2057. **[mcp-montano-server](https://github.com/lucasmontano/mcp-montano-server)** - ⭐ 138
   Simple MCP Server Implementation

2058. **[doc-ops-mcp](https://github.com/Tele-AI/doc-ops-mcp)** - ⭐ 138
   MCP server for seamless document format conversion and processing

2059. **[mcp-arr](https://github.com/aplaceforallmystuff/mcp-arr)** - ⭐ 137
   MCP server for *arr media management suite

2060. **[mcp-ts-core](https://github.com/cyanheads/mcp-ts-core)** - ⭐ 137
   Agent-native TypeScript framework for building MCP servers. Declarative definitions with auth, multi-backend storage, OpenTelemetry, and first-class support for Bun/Node/Cloudflare Workers.

2061. **[agent-toolkit](https://github.com/datacommonsorg/agent-toolkit)** - ⭐ 137
   Tools and agents for interacting with the Data Commons Knowledge Graph using the Model Context Protocol (MCP).

2062. **[pentest-mcp](https://github.com/DMontgomery40/pentest-mcp)** - ⭐ 137
   NOT for educational purposes: An MCP server for professional penetration testers including STDIO/HTTP/SSE support, nmap, go/dirbuster, nikto, JtR, hashcat, wordlist building, and more.

2063. **[OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server)** - ⭐ 137
   Devin's attempt at creating an OpenSCAD MCP Server that takes a user prompt and generates a preview image and 3d file.

2064. **[Kagi-Session2API-MCP](https://github.com/KSroido/Kagi-Session2API-MCP)** - ⭐ 137
   Free Kagi Search MCP server — access search and summarizer via session tokens, no API key needed. Works with Claude Desktop, Cursor, Windsurf, Hermes and any MCP client.

2065. **[Gitingest-MCP](https://github.com/puravparab/Gitingest-MCP)** - ⭐ 137
   mcp server for gitingest

2066. **[ontosphere](https://github.com/ThHanke/ontosphere)** - ⭐ 137
   Browser-based RDF/ontology knowledge graph editor — load RDF from files, URLs or SPARQL endpoints; author nodes and edges on the canvas; run OWL-RL reasoning; apply multi-algorithm layout and clustering. AI-native via MCP tool surface and relay bridge. Fully client-side, no backend required.

2067. **[mcp-endpoint-server](https://github.com/xinnan-tech/mcp-endpoint-server)** - ⭐ 137
   xiaozhi mcp接入点服务器，用于自定义mcp服务注册，方便拓展小智服务端工具调用

2068. **[lyraios](https://github.com/GalaxyLLMCI/lyraios)** - ⭐ 136
   LYRAI is a Model Context Protocol (MCP) operating system for multi-AI AGENTs designed to extend the functionality of AI applications by enabling them to interact with financial networks and blockchain public chains. The server offers a range of advanced AI assistants, including blockchain public chain operations (SOLANA,ETH,BSC,etc.)

2069. **[-mcp-to-skill-converter](https://github.com/GBSOSS/-mcp-to-skill-converter)** - ⭐ 136
      Convert any MCP server into a Claude Skill with 90% context savings

2070. **[Financial-Modeling-Prep-MCP-Server](https://github.com/imbenrabi/Financial-Modeling-Prep-MCP-Server)** - ⭐ 136
   A Model Context Protocol (MCP) implementation for Financial Modeling Prep, enabling AI assistants to access and analyze financial data, stock information, company fundamentals, and market insights.

2071. **[design-systems-mcp](https://github.com/southleft/design-systems-mcp)** - ⭐ 136
   I'm your specialized design systems assistant. Ask me about components, tokens, patterns, and best practices.

2072. **[toolhive-studio](https://github.com/stacklok/toolhive-studio)** - ⭐ 136
   ToolHive is an application that allows you to install, manage and run MCP servers and connect them to AI agents

2073. **[mcp-chat](https://github.com/Flux159/mcp-chat)** - ⭐ 135
   Open Source Generic MCP Client for testing & evaluating mcp servers and agents

2074. **[UnityMCP](https://github.com/isuzu-shiranui/UnityMCP)** - ⭐ 135
   Unity Editor integration with Model Context Protocol (MCP) enabling AI assistants like Claude to interact with Unity projects. Features a TypeScript MCP server and C# Unity plugin with extensible command handler architecture, TCP/IP communication, and dynamic plugin discovery.

2075. **[ZotLink](https://github.com/TonybotNi/ZotLink)** - ⭐ 135
   Production‑ready MCP server for Zotero to save open preprints (arXiv, CVF, bio/med/chemRxiv) with rich metadata and smart PDF attachments — with upcoming support for publisher databases (Nature, Science, IEEE Xplore, Springer).

2076. **[crawl4ai-mcp-server](https://github.com/weidwonder/crawl4ai-mcp-server)** - ⭐ 135
   用于提供给本地开发者的 LLM的高效互联网搜索&内容获取的MCP Server， 节省你的token

2077. **[ChatPPT-MCP](https://github.com/YOOTeam/ChatPPT-MCP)** - ⭐ 135
   The AI-powered PPT generation service based on ChatPPT can create presentations based on themes, requirements, or uploaded documents, supporting online editing and downloading.基于chatppt进行的AI PPT生成服务，可以满足基于主题或者要求、以及上传文档进行生成ppt，以及美化换模板、修改配色字体等，支持在线编辑与下载。

2078. **[ETOS-LLM-Studio](https://github.com/Eric-Terminal/ETOS-LLM-Studio)** - ⭐ 134
   A native LLM client for iOS & Apple Watch. Run local GGUF models offline via llama.cpp, or connect to OpenAI/Claude/Gemini. Features local RAG, Model Context Protocol (MCP) tools, Siri Shortcuts, and cross-device sync. Built with Swift.

2079. **[easy-code-reader](https://github.com/FangYuan33/easy-code-reader)** - ⭐ 134
   A powerful MCP server for intelligently reading Java source code (For Jar and local project).

2080. **[mkinf](https://github.com/mkinf-io/mkinf)** - ⭐ 134
   mkinf SDK to interact with mkinf hub MCP servers

2081. **[qgis-mcp](https://github.com/nkarasiak/qgis-mcp)** - ⭐ 134
   Connect QGIS to Claude AI through the Model Context Protocol (MCP)

2082. **[mcp-linear](https://github.com/tacticlaunch/mcp-linear)** - ⭐ 134
   MCP server that enables AI assistants to interact with Linear project management system through natural language, allowing users to retrieve, create, and update issues, projects, and teams.

2083. **[mcp-gateway](https://github.com/acehoss/mcp-gateway)** - ⭐ 133
   A flexible gateway server that bridges Model Context Protocol (MCP) STDIO servers to MCP HTTP+SSE and REST API, enabling multi-instance MCP servers to be exposed over HTTP.

2084. **[aks-mcp](https://github.com/Azure/aks-mcp)** - ⭐ 133
   A Model Context Protocol (MCP) server that enables AI assistants to interact with AKS clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and AKS.

2085. **[mcp-probe](https://github.com/conikeec/mcp-probe)** - ⭐ 133
   A Model Context Protocol (MCP) client library and debugging toolkit in Rust. This foundation provides both a production-ready SDK for building MCP integrations and the core architecture for an interactive debugger.

2086. **[mcp-think-tool](https://github.com/DannyMac180/mcp-think-tool)** - ⭐ 133
   An MCP server implementing the think tool for Claude

2087. **[Multi-Source-Media-MCP-Server](https://github.com/Decade-qiu/Multi-Source-Media-MCP-Server)** - ⭐ 133
   An MCP Tool Implementation for Multi-Source Image Access & Generation

2088. **[reddit-mcp-server](https://github.com/jordanburke/reddit-mcp-server)** - ⭐ 133
   ⚙️ A Model Context Protocol (MCP) that provides tools for fetching and creating Reddit content

2089. **[llm.rb](https://github.com/llmrb/llm.rb)** - ⭐ 133
   Ruby's most capable AI runtime

2090. **[mcp-auth-proxy](https://github.com/sigbit/mcp-auth-proxy)** - ⭐ 133
   MCP Auth Proxy is a secure OAuth 2.1 authentication proxy for Model Context Protocol (MCP) servers

2091. **[magg](https://github.com/sitbon/magg)** - ⭐ 133
   Magg: The MCP Aggregator

2092. **[Matryoshka](https://github.com/yogthos/Matryoshka)** - ⭐ 133
   MCP server for token-efficient large document analysis via the use of REPL state

2093. **[ida-headless-mcp](https://github.com/zboralski/ida-headless-mcp)** - ⭐ 133
   Headless IDA Pro binary analysis via Model Context Protocol

2094. **[buttplug-mcp](https://github.com/ConAcademy/buttplug-mcp)** - ⭐ 132
   Buttplug.io Model Context Protocol (MCP) Server

2095. **[prism-coder](https://github.com/dcostenco/prism-coder)** - ⭐ 132
   The Mind Palace for AI Agents - HIPAA-hardened Cognitive Architecture with on-device LLM (prism-coder:7b), Hebbian learning, ACT-R spreading activation, adversarial evaluation, persistent memory, multi-agent Hivemind and visual dashboard. Zero API keys required.

2096. **[hub-mcp](https://github.com/docker/hub-mcp)** - ⭐ 132
   Docker Hub MCP Server

2097. **[xcodeproj-mcp-server](https://github.com/giginet/xcodeproj-mcp-server)** - ⭐ 132
   A Model Context Protocol Server to manipulate *.xcodeproj

2098. **[mcp-watch](https://github.com/kapilduraphe/mcp-watch)** - ⭐ 132
   A comprehensive security scanner for Model Context Protocol (MCP) servers that detects vulnerabilities and security issues in your MCP server implementations.

2099. **[ragrabbit](https://github.com/madarco/ragrabbit)** - ⭐ 132
   Open Source, Self-Hosted, AI Search and LLM.txt for your website

2100. **[esankhyiki-mcp](https://github.com/nso-india/esankhyiki-mcp)** - ⭐ 132
   This repository consists of Source Code for Model Context Protocol (MCP) Pilot Project being undertaken by Ministry of Statistics and Programme Implementation and source code for the same is being shared under  MIT License.

2101. **[omega-memory](https://github.com/omega-memory/omega-memory)** - ⭐ 132
   Persistent memory for AI coding agents

2102. **[narsil-mcp](https://github.com/postrv/narsil-mcp)** - ⭐ 132
   Rust MCP server for comprehensive code intelligence - 90 tools, 32 languages, security scanning, call graphs, and more

2103. **[N8N2MCP](https://github.com/Super-Chain/N8N2MCP)** - ⭐ 132
   Convert N8N agent / workflow into MCP servers, you can use it in Claude / Cursor / Super Chain

2104. **[mcp-server](https://github.com/webflow/mcp-server)** - ⭐ 132
   Model Context Protocol (MCP) server for the Webflow Data API.

2105. **[orchestkit](https://github.com/yonatangross/orchestkit)** - ⭐ 132
   The Complete AI Development Toolkit for Claude Code — 89 skills, 31 agents, 99 hooks. Production-ready patterns for full-stack development.

2106. **[mcp-server-asana](https://github.com/roychri/mcp-server-asana)** - ⭐ 131

2107. **[mcp-server](https://github.com/browserstack/mcp-server)** - ⭐ 130
   BrowserStack's Official MCP Server

2108. **[beyond-mcp](https://github.com/disler/beyond-mcp)** - ⭐ 130
   It's time to push beyond MCP Servers... Right?

2109. **[mcp-server-ccxt](https://github.com/doggybee/mcp-server-ccxt)** - ⭐ 130
   High-performance CCXT MCP server for cryptocurrency exchange integration

2110. **[awesome-crypto-mcp-servers](https://github.com/badkk/awesome-crypto-mcp-servers)** - ⭐ 129
   A collection of crypto MCP servers.

2111. **[teslamate-mcp](https://github.com/cobanov/teslamate-mcp)** - ⭐ 129
   A Model Context Protocol (MCP) server that provides access to your TeslaMate database, allowing AI assistants to query Tesla vehicle data and analytics.

2112. **[prism-mcp](https://github.com/dcostenco/prism-mcp)** - ⭐ 129
   The Mind Palace for AI Agents - HIPAA-hardened Cognitive Architecture with on-device LLM (prism-coder:7b), Hebbian learning, ACT-R spreading activation, adversarial evaluation, persistent memory, multi-agent Hivemind and visual dashboard. Zero API keys required.

2113. **[exstruct](https://github.com/harumiWeb/exstruct)** - ⭐ 129
   Conversion from Excel to structured JSON (tables, shapes, charts) for LLM/RAG pipelines, and autonomous Excel reading and writing by AI agents through MCP integration.

2114. **[mcp-streamable-http](https://github.com/invariantlabs-ai/mcp-streamable-http)** - ⭐ 129
   Example implementation of MCP Streamable HTTP client/server in Python and TypeScript.

2115. **[jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp)** - ⭐ 129
   A Model Context Protocol (MCP) for Jupyter Notebook

2116. **[iphone-mcp](https://github.com/Lakr233/iphone-mcp)** - ⭐ 129
   A Model Context Protocol (MCP) server for automating iPhone tasks with Appium. Supports app control, UI interactions, and screenshot capture via streamable HTTP.

2117. **[laravel-toon](https://github.com/mischasigtermans/laravel-toon)** - ⭐ 129
   TOON encoding for Laravel. Encode data for AI/LLMs with ~50% fewer tokens than JSON.

2118. **[octagon-mcp-server](https://github.com/OctagonAI/octagon-mcp-server)** - ⭐ 129
   A free MCP server to analyze and extract insights from public filings, earnings transcripts, financial metrics, stock market data, private market transactions, and deep web-based research within Claude Desktop and other popular MCP clients.

2119. **[mcp-devtools](https://github.com/sammcj/mcp-devtools)** - ⭐ 129
   A modular MCP server that provides commonly used developer tools for AI coding agents

2120. **[indonesia-gov-apis](https://github.com/suryast/indonesia-gov-apis)** - ⭐ 129
   🇮🇩 50+ Indonesian Government APIs & Data Sources — BPS, OJK, BPJPH, BPOM, Bank Indonesia, IDX, BMKG + MCP servers. Python examples, scraping patterns, and practical gotchas.

2121. **[linear-mcp](https://github.com/cline/linear-mcp)** - ⭐ 128
   a private MCP server for accessing Linear

2122. **[dart-mcp-server](https://github.com/its-dart/dart-mcp-server)** - ⭐ 128
   Dart AI Model Context Protocol (MCP) server

2123. **[specs-workflow-mcp](https://github.com/kingkongshot/specs-workflow-mcp)** - ⭐ 128
   Intelligent spec workflow management MCP server

2124. **[laravel-loop](https://github.com/kirschbaum-development/laravel-loop)** - ⭐ 128
   Laravel Loop is a powerful Model Context Protocol (MCP) server designed specifically for Laravel applications. It connects your Laravel application with AI assistants using the MCP protocol.

2125. **[mcp-evals](https://github.com/mclenhard/mcp-evals)** - ⭐ 128
   A Node.js package and GitHub Action for evaluating MCP (Model Context Protocol) tool implementations using LLM-based scoring. This helps ensure your MCP server's tools are working correctly and performing well.

2126. **[IB_MCP](https://github.com/rcontesti/IB_MCP)** - ⭐ 128
   This project provides an Interactive Brokers (IB) API interface using the Model Context Protocol (MCP).

2127. **[mcp-server-aws](https://github.com/rishikavikondala/mcp-server-aws)** - ⭐ 128
   A Model Context Protocol server implementation for operations on AWS resources

2128. **[mcp-victoriametrics](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics)** - ⭐ 128
   The implementation of Model Context Protocol (MCP) server for VictoriaMetrics

2129. **[aws-cost-explorer-mcp-server](https://github.com/aarora79/aws-cost-explorer-mcp-server)** - ⭐ 127
   MCP server for understanding AWS spend

2130. **[computer-control-mcp](https://github.com/AB498/computer-control-mcp)** - ⭐ 127
   MCP server that provides computer control capabilities, like mouse, keyboard, OCR, etc. using PyAutoGUI, RapidOCR, ONNXRuntime. Similar to 'computer-use' by Anthropic. With Zero External Dependencies.

2131. **[template-repo](https://github.com/AndrewAltimit/template-repo)** - ⭐ 127
   Agent orchestration & security template featuring MCP tool building, agent2agent workflows, mechanistic interpretability on sleeper agents, and agent integration via CLI wrappers

2132. **[spring-ai](https://github.com/eazybytes/spring-ai)** - ⭐ 127
   From Java Dev to AI Engineer: Spring AI Fast Track

2133. **[mcp-server-plugin](https://github.com/JetBrains/mcp-server-plugin)** - ⭐ 127
   JetBrains MCP Server Plugin

2134. **[mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins)** - ⭐ 127
   The Model Context Protocol (MCP) is an open-source implementation that bridges Jenkins with AI language models following Anthropic's MCP specification. This project enables secure, contextual AI interactions with Jenkins tools while maintaining data privacy and security.

2135. **[mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery)** - ⭐ 127
   A Model Context Protocol server that provides access to BigQuery

2136. **[think-mcp-server](https://github.com/PhillipRt/think-mcp-server)** - ⭐ 127

2137. **[portainer-mcp](https://github.com/portainer/portainer-mcp)** - ⭐ 127
   Portainer MCP server

2138. **[mcp-hubspot](https://github.com/baryhuang/mcp-hubspot)** - ⭐ 126
   A Model Context Protocol (MCP) server that enables AI assistants to interact with HubSpot CRM data, providing built-in vector storage and caching mechanisms help overcome HubSpot API limitations while improving response times.

2139. **[mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan)** - ⭐ 126
   MCP server for Shodan — search internet-connected devices, IP reconnaissance, DNS lookups, and CVE/CPE vulnerability intelligence. Works with Claude Code, Codex, Gemini CLI, and Claude Desktop.

2140. **[claude-prompts-mcp](https://github.com/minipuft/claude-prompts-mcp)** - ⭐ 126
   MCP prompt template server: hot-reload, thinking frameworks, quality gates

2141. **[mcp-local-rag](https://github.com/nkapila6/mcp-local-rag)** - ⭐ 126
   "primitive" RAG-like web search model context protocol (MCP) server that runs locally. ✨ no APIs ✨

2142. **[kicad-mcp-pro](https://github.com/oaslananka/kicad-mcp-pro)** - ⭐ 126
   Model Context Protocol server for KiCad PCB and schematic automation, exposing project setup, editing, validation gates, DFM/SI/PI helpers, simulation support, and manufacturing exports.

2143. **[mcp](https://github.com/taskade/mcp)** - ⭐ 126
   🤖 Taskade MCP · Official MCP server and OpenAPI to MCP codegen. Build AI agent tools from any OpenAPI API and connect to Claude, Cursor, and more.

2144. **[awesome-unipds-projects](https://github.com/unipds-engenharia-de-ia-aplicada/awesome-unipds-projects)** - ⭐ 126
   A curated list of original projects built by students of the UNIPDS Software engineering with Applied AI Engineering postgrad course.

2145. **[sysplant](https://github.com/x42en/sysplant)** - ⭐ 126
   Your Windows syscall hooking factory - feat Canterlot's Gate - All accessible over MCP

2146. **[play-store-mcp](https://github.com/devexpert-io/play-store-mcp)** - ⭐ 125
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

2147. **[cloudflare-mcp](https://github.com/mattzcarey/cloudflare-mcp)** - ⭐ 125
   unofficial mcp server for cloudflare api

2148. **[MiniMax-MCP-JS](https://github.com/MiniMax-AI/MiniMax-MCP-JS)** - ⭐ 125
   Official MiniMax Model Context Protocol (MCP) JavaScript implementation that provides seamless integration with MiniMax's powerful AI capabilities including image generation, video generation, text-to-speech, and voice cloning APIs.

2149. **[web-scout-mcp](https://github.com/pinkpixel-dev/web-scout-mcp)** - ⭐ 125
   A powerful MCP server extension providing web search and content extraction capabilities. Integrates DuckDuckGo search functionality and URL content extraction into your MCP environment, enabling AI assistants to search the web and extract webpage content programmatically.

2150. **[aws-lambda-mcp-cookbook](https://github.com/ran-isenberg/aws-lambda-mcp-cookbook)** - ⭐ 125
   This repository provides a working, deployable, open source-based, serverless MCP server blueprint with an AWS Lambda function and AWS CDK Python code with all the best practices and a complete CI/CD pipeline.

2151. **[awesome-openclaw](https://github.com/vincentkoc/awesome-openclaw)** - ⭐ 125
   Curated awesome list for OpenClaw (formerly Moltbot/Clawdbot): skills, plugins, memory systems, MCP tools, deployment stacks, ecosystem platforms, and developer tooling.

2152. **[mcp-client-server](https://github.com/willccbb/mcp-client-server)** - ⭐ 125
   An MCP Server that's also an MCP Client. Useful for letting Claude develop and test MCPs without needing to reset the application.

2153. **[mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal)** - ⭐ 124
   MCP server for VirusTotal API — analyze URLs, files, IPs, and domains with comprehensive security reports, relationship analysis, and pagination support.

2154. **[Delphi-MCP-Server](https://github.com/GDKsoftware/Delphi-MCP-Server)** - ⭐ 124
   Native Delphi Server implementation of the Model Context Protocol (MCP)

2155. **[context-sync](https://github.com/Intina47/context-sync)** - ⭐ 124
   Local persistent memory store for LLM applications including continue.dev, cursor, claude desktop, github copilot, codex, antigravity, etc.

2156. **[turbo-flow-claude](https://github.com/marcuspat/turbo-flow-claude)** - ⭐ 124
   Advanced Agentic Development Environment Supporting Devpods, Rackspace Spot Instances, Github Codespaces, Google Cloud Shell, and more!  Features 600+ AI agents, Claude Flow, SPARC methodology, and automatic context loading! Deploy intelligent multi-agent swarms, coordinate autonomous workflows.

2157. **[nitrostack](https://github.com/nitrocloudofficial/nitrostack)** - ⭐ 124
   The full-stack TypeScript framework to build, test, and deploy production-ready MCP servers and AI-native apps.

2158. **[mcp](https://github.com/pronskiy/mcp)** - ⭐ 124
   🐉 The fast, PHP way to build MCP servers

2159. **[mcp-glootie](https://github.com/AnEntrypoint/mcp-glootie)** - ⭐ 123
   wanna develop an app ❓

2160. **[server-google-news](https://github.com/ChanMeng666/server-google-news)** - ⭐ 123
   【Star-crossed coders unite!⭐️】Model Context Protocol (MCP) server implementation providing Google News search capabilities via SerpAPI, with automatic news categorization and multi-language support.

2161. **[obsidian-web-mcp](https://github.com/jimprosser/obsidian-web-mcp)** - ⭐ 123
   Secure remote MCP server for Obsidian vaults -- access your notes from Claude, your phone, or any MCP client, anywhere. OAuth 2.0 auth, Cloudflare Tunnel, atomic writes safe for Obsidian Sync.

2162. **[google-tag-manager-mcp-server](https://github.com/stape-io/google-tag-manager-mcp-server)** - ⭐ 123
   MCP server for Google Tag Manager

2163. **[ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp)** - ⭐ 123
   Using ffmpeg command line to achieve an mcp server, can be very convenient, through the dialogue to achieve the local video search, tailoring, stitching, playback,clip, overlay, concat and other functions

2164. **[ASI](https://github.com/vNeeL-code/ASI)** - ⭐ 123
   Android ✧ Gemma Integration into Android System Intelligence

2165. **[mcp-gm](https://github.com/AnEntrypoint/mcp-gm)** - ⭐ 122
   wanna develop an app ❓

2166. **[MCP-Workspace-Server](https://github.com/answerlink/MCP-Workspace-Server)** - ⭐ 122
   🚀 Beyond Filesystem - Complete AI Development Environment - One MCP Server provides full Agent capability stack: web development, code execution, data processing, image generation. No need for multiple tools, configure once. Perfect support for Dify, FastGPT, Cherry Studio.       文件操作、Python/Node.js 代码执行、Web 应用一键部署（支持泛域名）、Excel 处理、图像生成。开箱即用

2167. **[remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)** - ⭐ 122
   This is a quickstart template to easily build and deploy a custom remote MCP server to the cloud using Azure functions. You can clone/restore/run on your local machine with debugging, and `azd up` to have it in the cloud in a couple minutes.  The MCP server is secured by design using

2168. **[Pare](https://github.com/Dave-London/Pare)** - ⭐ 122
   Dev tools, optimized for agents. Structured, token-efficient MCP servers for git, test runners, npm, Docker, and more.

2169. **[zabbix-mcp-server](https://github.com/initMAX/zabbix-mcp-server)** - ⭐ 122
   MCP server for the complete Zabbix API - 237 tools, multi-server, OAuth 2.1 + bearer auth, PDF reports, systemd ready. Works with ChatGPT, Claude, VS Code, Codex, JetBrains and any MCP client.

2170. **[env-doctor](https://github.com/mitulgarg/env-doctor)** - ⭐ 122
   Debug your GPU, CUDA, and AI stacks across local, Docker, and CI/CD (CLI and MCP server)

2171. **[IntelliConnect](https://github.com/ruanrongman/IntelliConnect)** - ⭐ 122
   本项目为xiaozhi-esp32提供后端服务  |  A Powerful AI agent IoT platform core.

2172. **[mcp-package-version](https://github.com/sammcj/mcp-package-version)** - ⭐ 122
   An MCP server that provides LLMs with the latest stable package versions when coding

2173. **[mcp-svelte-docs](https://github.com/spences10/mcp-svelte-docs)** - ⭐ 122
   🔍 MCP server that lets you search and access Svelte documentation with built-in caching

2174. **[mcp-mianshiya-server](https://github.com/yuyuanweb/mcp-mianshiya-server)** - ⭐ 122
   基于 Spring AI 的面试鸭搜索题目的 MCP Server 服务，快速让 AI 搜索企业面试真题和答案

2175. **[MiniClaw](https://github.com/8421bit/MiniClaw)** - ⭐ 121
   🦞 A Digital Life Embryo for your MCP Client. An intelligent micro-kernel with Nociception, Memory Apoptosis, and a Curiosity Drive. Evolve your AI Copilot into a sentient partner for Claude Desktop, Qoderwork, Cursor, and beyond.

2176. **[augments-mcp-server](https://github.com/augmnt/augments-mcp-server)** - ⭐ 121
   Comprehensive MCP server providing real-time framework documentation access for Claude Code with intelligent caching, multi-source integration, and context-aware assistance.

2177. **[Taiwan-Health-MCP](https://github.com/healthymind-tech/Taiwan-Health-MCP)** - ⭐ 121

2178. **[n8n-mcp-server](https://github.com/illuminaresolutions/n8n-mcp-server)** - ⭐ 121
   MCP server implementation for n8n workflow automation

2179. **[muppet](https://github.com/muppet-dev/muppet)** - ⭐ 121
   MCP Servers SDK for TypeScript

2180. **[mcp_proxy_rust](https://github.com/tidewave-ai/mcp_proxy_rust)** - ⭐ 121
   A proxy to use HTTP/SSE MCPs from STDIO clients

2181. **[ffmpeg-mcp](https://github.com/egoist/ffmpeg-mcp)** - ⭐ 120
   An MCP server for FFmpeg

2182. **[mcp](https://github.com/frappe/mcp)** - ⭐ 120
   Frappe MCP allows Frappe apps to function as MCP servers

2183. **[xiaohongshu-mcp-python](https://github.com/luyike221/xiaohongshu-mcp-python)** - ⭐ 120
   xiaohongshu-mcp-python 是一个基于现代 Python 技术栈开发的小红书内容自动化发布工具，通过 Model Context Protocol（MCP）协议为 AI 客户端提供强大的小红书操作能力。项目核心功能包括小红书账户登录管理、图文内容发布、视频内容发布、内容搜索与获取、帖子详情查看以及评论互动等。支持多种图片格式（JPG、PNG、GIF）和视频格式（MP4、MOV、AVI），既可处理本地文件路径，也支持 HTTP/HTTPS 链接，为用户提供灵活的内容发布方案。  该工具特别适合内容创作者、营销人员和开发者使用，能够显著提升小红书内容发布的效率和自动化程度。通过标准化的 MCP 接口，用户可以轻松地将小红书操作能力集成到各种 AI 工作流中，实现智能化的内容管理

2184. **[fastmail-mcp](https://github.com/MadLlama25/fastmail-mcp)** - ⭐ 120
   A Model Context Protocol (MCP) server that provides access to the Fastmail API, enabling AI assistants to interact with email, contacts, and calendar data. Includes a DXT (desktop extension) for Claude Desktop.

2185. **[google-sheets-mcp](https://github.com/mkummer225/google-sheets-mcp)** - ⭐ 120
   Google Sheets MCP Server 📊🤖

2186. **[mcp-hubspot](https://github.com/peakmojo/mcp-hubspot)** - ⭐ 120
   A Model Context Protocol (MCP) server that enables AI assistants to interact with HubSpot CRM data, providing built-in vector storage and caching mechanisms help overcome HubSpot API limitations while improving response times.

2187. **[spring-ai-playground](https://github.com/spring-ai-community/spring-ai-playground)** - ⭐ 120
   Safe local execution layer for AI agent tools. Build, validate, and publish MCP tools with a no-pass-no-run workflow — cross-platform desktop app powered by Spring AI.

2188. **[mcp-ts-template](https://github.com/cyanheads/mcp-ts-template)** - ⭐ 119
   TypeScript template for building Model Context Protocol (MCP) servers. Ships with declarative tools/resources, pluggable auth, multi-backend storage, OpenTelemetry observability, and first-class support for both local and edge (Cloudflare Workers) runtimes.

2189. **[mcp-jfrog](https://github.com/jfrog/mcp-jfrog)** - ⭐ 119
   Model Context Protocol (MCP) Server for the JFrog Platform API, enabling repository management, build tracking, release lifecycle management, and more.

2190. **[elevenlabs-mcp-server](https://github.com/mamertofabian/elevenlabs-mcp-server)** - ⭐ 119

2191. **[MySearch-Proxy](https://github.com/skernelx/MySearch-Proxy)** - ⭐ 119
   Unified search MCP, proxy console, and skill for Tavily, Firecrawl, and Social / X.

2192. **[agenticmail](https://github.com/agenticmail/agenticmail)** - ⭐ 118
   Email & SMS infrastructure for AI agents — send and receive real email and text messages programmatically

2193. **[polymarket-mcp](https://github.com/berlinbra/polymarket-mcp)** - ⭐ 118
   MCP Server for PolyMarket API

2194. **[falcon-mcp](https://github.com/CrowdStrike/falcon-mcp)** - ⭐ 118
   Connect AI agents to CrowdStrike Falcon for automated security analysis and threat hunting

2195. **[Embody](https://github.com/dylanroscover/Embody)** - ⭐ 118
   MCP server for TouchDesigner — build, wire, and debug networks with AI. Plus git-diffable externalization.

2196. **[gopher-mcp](https://github.com/GopherSecurity/gopher-mcp)** - ⭐ 118
   MCP C++ SDK - Model Context Protocol implementation in CPP with enterprise-grade security, observability and connectivity.

2197. **[memorizer-v1](https://github.com/petabridge/memorizer-v1)** - ⭐ 118
   Vector-search powered agent memory MCP server

2198. **[diagram-mcp-server](https://github.com/andrewmoshu/diagram-mcp-server)** - ⭐ 117
   An MCP server that seamlessly creates infrastructure diagrams for AWS, Azure, GCP, Kubernetes and more

2199. **[VisionCraft-MCP-Server](https://github.com/augmentedstartups/VisionCraft-MCP-Server)** - ⭐ 117
   VisionCraft MCP delivers up-to-date, specialized computer vision and Gen-AI knowledge directly to Claude and other AI assistants.

2200. **[ynab-mcp-server](https://github.com/calebl/ynab-mcp-server)** - ⭐ 117
   Model Context Protocol for YNAB (you need a budget)

2201. **[dottedsign-mcp](https://github.com/DottedSign-Official/dottedsign-mcp)** - ⭐ 117
   A DottedSign MCP server that enables AI assistants (Claude, ChatGPT) to manage signing tasks, templates, and document status via natural language.

2202. **[kodit](https://github.com/helixml/kodit)** - ⭐ 117
   👩‍💻 MCP server to index external repositories

2203. **[mcp-server](https://github.com/InterviewReady/mcp-server)** - ⭐ 117
   An MCP server for InterviewReady

2204. **[outline-mcp-server](https://github.com/mmmeff/outline-mcp-server)** - ⭐ 117
   It's an MCP server... for Outline (the documentation platform!)

2205. **[mcp-armor](https://github.com/aira-security/mcp-armor)** - ⭐ 116
   MCP Armor continuously secures and monitors Model Context Protocol operations through static and dynamic scans, revealing hidden risks in agent-to-tool communications.

2206. **[arbor](https://github.com/Anandb71/arbor)** - ⭐ 116
   Graph-native code intelligence that replaces embedding-based RAG with deterministic program understanding.

2207. **[EDT-MCP](https://github.com/DitriXNew/EDT-MCP)** - ⭐ 116
   MCP for 1C:EDT

2208. **[mcp-hetzner](https://github.com/dkruyt/mcp-hetzner)** - ⭐ 116
   A Model Context Protocol (MCP) server for interacting with the Hetzner Cloud API. This server allows language models to manage Hetzner Cloud resources through structured functions.

2209. **[cli](https://github.com/mcpgod/cli)** - ⭐ 116
   Fine-grained control over model context protocol (MCP) clients, servers, and tools. Context is God.

2210. **[brave-search-mcp](https://github.com/mikechao/brave-search-mcp)** - ⭐ 116
   An MCP Server implementation that integrates the Brave Search API, providing, Web Search, Local Points of Interest Search, Image Search, Video Search, News Search and LLM Context Search capabilities

2211. **[pocketbase-mcp](https://github.com/mrwyndham/pocketbase-mcp)** - ⭐ 116
   MCP server for building PocketBase apps really quickly - Need a front end quick consider FastPocket

2212. **[forge-orchestrator](https://github.com/nxtg-ai/forge-orchestrator)** - ⭐ 116
   Forge Orchestrator: Multi-AI task orchestration. File locking, knowledge capture, drift detection. Rust.

2213. **[sandbox-mcp](https://github.com/pottekkat/sandbox-mcp)** - ⭐ 116
   A Model Context Protocol (MCP) server that enables LLMs to run ANY code safely in isolated Docker containers.

2214. **[mcp-prompts](https://github.com/sparesparrow/mcp-prompts)** - ⭐ 116
   Model Context Protocol server for managing, storing, and providing prompts and prompt templates for LLM interactions.

2215. **[modex](https://github.com/theronic/modex)** - ⭐ 116
   Modex is a Clojure MCP Library to augment your AI models with Tools, Resources & Prompts using Clojure (Model Context Protocol). Implements MCP Server & Client.

2216. **[remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)** - ⭐ 115
   Azure API Management as AI Gateway to Remote MCP servers.

2217. **[remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python)** - ⭐ 115
   Getting Started with Remote MCP Servers using Azure Functions (Python)

2218. **[healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public)** - ⭐ 115
   A Model Context Protocol (MCP) server providing AI assistants with access to healthcare data and medical information tools, including FDA drug info, PubMed, medRxiv, NCBI Bookshelf, clinical trials, ICD-10, DICOM metadata, and a medical calculator.

2219. **[oracle-mcp-server](https://github.com/danielmeppiel/oracle-mcp-server)** - ⭐ 115
   MCP Server for working with large Oracle databases

2220. **[winremote-mcp](https://github.com/dddabtc/winremote-mcp)** - ⭐ 115
   Windows Remote MCP Server — 40+ tools for desktop automation, process management, file operations via FastMCP

2221. **[mirroir-mcp](https://github.com/jfarcand/mirroir-mcp)** - ⭐ 115
   MCP server for controlling a real iPhone via macOS iPhone Mirroring...and any MacOs app. Screenshot, tap, swipe, type — from any MCP client.

2222. **[MCppServer](https://github.com/Noeli14/MCppServer)** - ⭐ 115
   Fast and super efficient Minecraft Server written in C++

2223. **[google-ai-mode-mcp](https://github.com/PleasePrompto/google-ai-mode-mcp)** - ⭐ 115
   MCP server for free Google AI Mode search with citations. Query optimization, CAPTCHA handling, multi-agent support. Works with Claude Code, Cursor, Cline, Windsurf.

2224. **[action_mcp](https://github.com/seuros/action_mcp)** - ⭐ 115
   Rails Engine with MCP compliant Spec.

2225. **[socket-mcp](https://github.com/SocketDev/socket-mcp)** - ⭐ 115
   Model Context Protocol server for socket.dev integration

2226. **[fhir-mcp-server](https://github.com/wso2/fhir-mcp-server)** - ⭐ 115
   FHIR MCP Server – helping you expose any FHIR Server or API as a MCP Server.

2227. **[JavaSinkTracer_MCP](https://github.com/Zacarx/JavaSinkTracer_MCP)** - ⭐ 115
   基于函数级污点分析的 Java 源代码漏洞审计工具JavaSinkTracer，通过 Model Context Protocol (MCP) 为 AI 助手提供安全分析能力。

2228. **[mcp-server-synology](https://github.com/atom2ueki/mcp-server-synology)** - ⭐ 114
   💾 Model Context Protocol (MCP) server for Synology NAS - Enables AI assistants (Claude, Cursor, Continue) to manage files, downloads, and system operations through secure API integration. Features Docker deployment, auto-authentication, and comprehensive file system tools.

2229. **[swagger-mcp](https://github.com/dcolley/swagger-mcp)** - ⭐ 114
   Swagger to MCP server

2230. **[native-devtools-mcp](https://github.com/sh3ll3x3c/native-devtools-mcp)** - ⭐ 114
   MCP server for computer use & browser automation  - screenshot, OCR, click, type, find_text, Chrome/Electron CDP, template matching. macOS, Windows & Android. Works with Claude, Cursor, and any MCP client.

2231. **[foxy-contexts](https://github.com/strowk/foxy-contexts)** - ⭐ 114
   Foxy contexts is a library for building context servers supporting Model Context Protocol

2232. **[AgenticGoKit](https://github.com/AgenticGoKit/AgenticGoKit)** - ⭐ 113
   Open-source Agentic AI framework in Go for building, orchestrating, and deploying intelligent agents. LLM-agnostic, event-driven, with multi-agent workflows, MCP tool discovery, and production-grade observability.

2233. **[codebadger](https://github.com/Lekssays/codebadger)** - ⭐ 113
   🦡 codebadger is a containerized Model Context Protocol (MCP) server that gives AI agents and LLMs deep, queryable access to a codebase's structure and data flow through Joern Code Property Graphs (CPGs).

2234. **[sourcerer-mcp](https://github.com/st3v3nmw/sourcerer-mcp)** - ⭐ 113
   MCP for semantic code search & navigation that reduces token waste

2235. **[MCP-oura](https://github.com/YuzeHao2023/MCP-oura)** - ⭐ 113
   MCP server for Oura API integration

2236. **[mcp-checkpoint](https://github.com/aira-security/mcp-checkpoint)** - ⭐ 112
   MCP Checkpoint continuously secures and monitors Model Context Protocol operations through static and dynamic scans, revealing hidden risks in agent-to-tool communications.

2237. **[awesome-mcp-enterprise](https://github.com/bh-rat/awesome-mcp-enterprise)** - ⭐ 112
   A curated list of awesome MCP (Model Context Protocol) tools, platforms, and services for enterprises.

2238. **[notion-mcp](https://github.com/ccabanillas/notion-mcp)** - ⭐ 112
   A Model Context Protocol (MCP) server implementation for Notion integration, providing a standardized interface for interacting with Notion's API.

2239. **[crypto-indicators-mcp](https://github.com/kukapay/crypto-indicators-mcp)** - ⭐ 112
   An MCP server providing a range of cryptocurrency technical analysis indicators and strategies.

2240. **[punkpeye_awesome-mcp-servers](https://github.com/MCP-Mirror/punkpeye_awesome-mcp-servers)** - ⭐ 112
   Mirror of https://github.com/punkpeye/awesome-mcp-servers

2241. **[yfinance-mcp](https://github.com/narumiruna/yfinance-mcp)** - ⭐ 112

2242. **[agent-bridge](https://github.com/raysonmeng/agent-bridge)** - ⭐ 112
   A local bridge for bidirectional collaboration between Claude Code and Codex. 连接 Claude Code 与 Codex 的本地实时协作桥接工具。

2243. **[mcp_client](https://github.com/theailanguage/mcp_client)** - ⭐ 112
   MCP Client Implementation using Python, LangGraph and Gemini

2244. **[x-twitter-scraper](https://github.com/Xquik-dev/x-twitter-scraper)** - ⭐ 112
   Twitter scraper API skill for tweet search, advanced Twitter search, profile tweets, follower export, media download, monitors, webhooks, MCP, and posting automation: send tweets and replies.

2245. **[vscode-as-mcp-server](https://github.com/acomagu/vscode-as-mcp-server)** - ⭐ 111
   Expose VSCode features such as file viewing and editing as MCP, enabling advanced AI-assisted coding directly from tools like Claude Desktop

2246. **[spring-documentation-mcp-server](https://github.com/andrlange/spring-documentation-mcp-server)** - ⭐ 111
   Spring Boot based MCP Server provide full Spring Ecosystem Documentation for LLMs

2247. **[gemini-cli-mcp-server](https://github.com/centminmod/gemini-cli-mcp-server)** - ⭐ 111

2248. **[cesium-mcp](https://github.com/gaopengbin/cesium-mcp)** - ⭐ 111
   AI-powered CesiumJS 3D globe control  49 tools for camera, entities, layers, animation & spatial analysis via Model Context Protocol (MCP). Natural language to 3D GIS.

2249. **[DINO-X-MCP](https://github.com/IDEA-Research/DINO-X-MCP)** - ⭐ 111
   Official DINO-X Model Context Protocol (MCP) server that empowers LLMs with real-world visual perception through image object detection, localization, and captioning APIs.

2250. **[idun-agent-platform](https://github.com/Idun-Group/idun-agent-platform)** - ⭐ 111
   🟪 Open source Agent Governance Platform that turns any LangGraph or ADK agent into a production-ready service. Supports: AG-UI, CopilotKit API, OpenTelemetry, MCP, memory, guardrails, SSO, RBAC.

2251. **[mcp-windows-desktop-automation](https://github.com/mario-andreschak/mcp-windows-desktop-automation)** - ⭐ 111
   A Model Context Protocol (MCP) server for Windows desktop automation using AutoIt.

2252. **[mcpauth](https://github.com/mcpauth/mcpauth)** - ⭐ 111
   Authentication for MCP Servers

2253. **[Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP](https://github.com/newideas99/Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP)** - ⭐ 111
   🧠 MCP server implementing RAT (Retrieval Augmented Thinking) - combines DeepSeek's reasoning with GPT-4/Claude/Mistral responses, maintaining conversation context between interactions.

2254. **[mcp.science](https://github.com/pathintegral-institute/mcp.science)** - ⭐ 111
   Open Source MCP Servers for Scientific Research

2255. **[langgraph-ai](https://github.com/piyushagni5/langgraph-ai)** - ⭐ 111
   A comprehensive collection of LangGraph implementations, tutorials, and advanced AI workflows covering Agentic RAG systems, MCP (Model Context Protocol) development, and practical AI application patterns.

2256. **[Fabric-Analytics-MCP](https://github.com/santhoshravindran7/Fabric-Analytics-MCP)** - ⭐ 111
   A Model Context Protocol (MCP) server that enables AI assistants to securely access and analyze Microsoft Fabric Analytics data through authenticated API calls.

2257. **[MCP-searxng](https://github.com/SecretiveShell/MCP-searxng)** - ⭐ 111
   MCP server for connecting agentic systems to search systems via searXNG

2258. **[mcp-reticle](https://github.com/soth-ai/mcp-reticle)** - ⭐ 111
   Reticle intercepts, visualizes, and profiles JSON-RPC traffic between your LLM and MCP servers in real-time, with zero latency overhead. Stop debugging blind. Start seeing everything.

2259. **[apple-rag-mcp](https://github.com/BingoWon/apple-rag-mcp)** - ⭐ 110
    MCP server providing AI agents with instant access to Apple developer documentation via RAG technology

2260. **[iai-mcp](https://github.com/CodeAbra/iai-mcp)** - ⭐ 110
   The best-benchmarked open-source memory system for AI coding assistants

2261. **[MCP2Lambda](https://github.com/danilop/MCP2Lambda)** - ⭐ 110
   Run any AWS Lambda function as a Large Language Model (LLM) tool without code changes using Anthropic's Model Context Protocol (MCP).

2262. **[dash-mcp-server](https://github.com/Kapeli/dash-mcp-server)** - ⭐ 110
   MCP server for Dash, the macOS documentation browser

2263. **[reddit-research-mcp](https://github.com/king-of-the-grackles/reddit-research-mcp)** - ⭐ 110
   Turn Reddit's chaos into structured insights with full citations. MCP server for competitive analysis, customer discovery, and market research. Zero-setup hosted solution with semantic search across 20,000+ subreddits.

2264. **[mcp-image](https://github.com/shinpr/mcp-image)** - ⭐ 110
   MCP server for AI image generation and editing with automatic prompt optimization and quality presets. Powered by Gemini (Nano Banana 2 & Pro), with optional OpenAI GPT Image support.

2265. **[code-pathfinder](https://github.com/shivasurya/code-pathfinder)** - ⭐ 110
   AI-Native Static Code Analysis for modern security teams. Built for finding vulnerabilities, advanced structural search, derive insights and supports MCP

2266. **[powerbi-mcp](https://github.com/sulaiman013/powerbi-mcp)** - ⭐ 110
   MCP server for natural language interaction with Power BI datasets

2267. **[livebook_tools](https://github.com/thmsmlr/livebook_tools)** - ⭐ 110
   Powertools for livebook.dev — AI Code Editing, MCP Servers, and Running Livebooks from the CLI

2268. **[a2a-mcp-tutorial](https://github.com/Tsadoq/a2a-mcp-tutorial)** - ⭐ 110
   A tutorial on how to use Model Context Protocol by Anthropic and Agent2Agent Protocol by Google

2269. **[SmartDB_MCP](https://github.com/wenb1n-dev/SmartDB_MCP)** - ⭐ 110
   Universal database MCP server connecting to MySQL, PostgreSQL, SQL Server, MariaDB,DM8,Oracle,not only provides basic database connection such as OAuth 2.0 authentication , health checks, SQL optimization, and index health detection

2270. **[embedded-debugger-mcp](https://github.com/Adancurusul/embedded-debugger-mcp)** - ⭐ 109
   A Model Context Protocol server for embedded debugging with probe-rs - supports ARM Cortex-M, RISC-V debugging via J-Link, ST-Link, and more

2271. **[server-wp-mcp](https://github.com/emzimmer/server-wp-mcp)** - ⭐ 109

2272. **[mcp-sqlite](https://github.com/jparkerweb/mcp-sqlite)** - ⭐ 109
   🐇 Model Context Protocol (MCP) server that provides comprehensive SQLite database interaction capabilities

2273. **[game-asset-mcp](https://github.com/MubarakHAlketbi/game-asset-mcp)** - ⭐ 109
   An MCP server for creating 2D/3D game assets from text using Hugging Face AI models.

2274. **[kibitz](https://github.com/nick1udwig/kibitz)** - ⭐ 109
   The coding agent for professionals

2275. **[ogham-mcp](https://github.com/ogham-mcp/ogham-mcp)** - ⭐ 109
   Shared memory MCP server — persistent, searchable, cross-client Claude, Opencode

2276. **[rust-docs-mcp](https://github.com/snowmead/rust-docs-mcp)** - ⭐ 109
   MCP server for agents to explore rust docs, analyze source code, and build with confidence

2277. **[flexible-graphrag](https://github.com/stevereiner/flexible-graphrag)** - ⭐ 109
   Flexible GraphRAG: Python, LlamaIndex, Docker Compose: 8 Graph dbs, 10 Vector dbs, OpenSearch, Elasticsearch, Alfresco. 13 data sources (9 auto-sync), KG auto-building, schemas, LLMs, Docling or LlamaParse doc processing, GraphRAG, RAG only, Hybrid search, AI chat. React, Vue, Angular frontends, FastAPI backend, REST API, MCP Server. Please 🌟 Star

2278. **[browser-debugger-cli](https://github.com/szymdzum/browser-debugger-cli)** - ⭐ 109
   CLI tool for agents to quickly access browser telemetry (DOM, network, console) via Chrome DevTools Protocol.

2279. **[mcp-trino](https://github.com/tuannvm/mcp-trino)** - ⭐ 109
   A high-performance Model Context Protocol (MCP) server for Trino implemented in Go.

2280. **[one-search-mcp](https://github.com/yokingma/one-search-mcp)** - ⭐ 109
   🚀 OneSearch MCP Server: Web Search & Scraper & Extract,  Support agent-browser, SearXNG, Tavily, DuckDuckGo, Bing, etc.

2281. **[asyncmcp](https://github.com/bh-rat/asyncmcp)** - ⭐ 108
   Async transport layers for MCP

2282. **[Alicization-Town](https://github.com/ceresOPA/Alicization-Town)** - ⭐ 108
    **⚔️ Alicization Town** is a decentralized, multi-agent pixel sandbox world powered by the **Model Context Protocol (MCP)**.    **⚔️ Alicization Town** 是一个基于 **MCP (Model Context Protocol)** 架构的去中心化多智能体像素沙盒世界。

2283. **[payloadcmsmcp](https://github.com/disruption-hub/payloadcmsmcp)** - ⭐ 108
   Payload CMS MCP Server

2284. **[model-context-protocol-mcp-hands-on-with-agentic-ai-2034200](https://github.com/LinkedInLearning/model-context-protocol-mcp-hands-on-with-agentic-ai-2034200)** - ⭐ 108
   This is a code repository for the LinkedIn Learning course Model Context Protocol (MCP): Hands-On with Agentic AI [ASI] [TEXT] [MODELS]

2285. **[mcpm](https://github.com/MCP-Club/mcpm)** - ⭐ 108
   A command-line tool for managing MCP servers in Claude App. Also can run a MCP Server to help you manage all your MCP Servers

2286. **[github-stars](https://github.com/miantiao-me/github-stars)** - ⭐ 108
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

2287. **[windbg-ext-mcp](https://github.com/NadavLor/windbg-ext-mcp)** - ⭐ 108
   WinDbg-ext-MCP bridges your favorite LLM client (like Cursor, Claude, or VS Code) with WinDbg, enabling real-time, AI assisted kernel debugging. Write prompts in your AI coding assistant and receive instant, context-aware analysis and insights from your live kernel debugging session.

2288. **[mcp-client](https://github.com/punkpeye/mcp-client)** - ⭐ 108
   An MCP client for Node.js.

2289. **[share-best-mcp](https://github.com/shareAI-lab/share-best-mcp)** - ⭐ 108
   世界上最好的MCP Servers的列表,The best mcp servers in the world.

2290. **[minesweeper-mcp-server](https://github.com/tonypan2/minesweeper-mcp-server)** - ⭐ 108
   An MCP server for playing Minesweeper

2291. **[snippy](https://github.com/Azure-Samples/snippy)** - ⭐ 107
   🧩 Build AI-powered MCP Tools with Azure Functions, Durable Agents & Cosmos vector search. Features orchestrated multi-agent workflows using OpenAI.

2292. **[gemini-mcp-desktop-client](https://github.com/duke7able/gemini-mcp-desktop-client)** - ⭐ 107
   first gemini based desktop client for MCP

2293. **[selfhosted-supabase-mcp](https://github.com/HenkDz/selfhosted-supabase-mcp)** - ⭐ 107
   An MCP Server for your Self Hosted Supabase

2294. **[awesome-context-engineering](https://github.com/jihoo-kim/awesome-context-engineering)** - ⭐ 107
   A curated list of awesome open-source libraries for context engineering (Long-term memory, MCP: Model Context Protocol, Prompt/RAG Compression, Multi-Agent)

2295. **[csharp-runner](https://github.com/sdcb/csharp-runner)** - ⭐ 107
   fast, secure c# runner

2296. **[arxiv-latex-mcp](https://github.com/takashiishida/arxiv-latex-mcp)** - ⭐ 107
   MCP server that uses arxiv-to-prompt to fetch and process arXiv LaTeX sources for precise interpretation of mathematical expressions in scientific papers.

2297. **[slack-mcp-server](https://github.com/ubie-oss/slack-mcp-server)** - ⭐ 107
   A Slack MCP server

2298. **[xclaude-plugin](https://github.com/conorluddy/xclaude-plugin)** - ⭐ 106
   iOS development ClaudeCode plugin for mindful token and context usage. Contains modular MCPs that group various Xcode/IDB tools based on your current workflow.

2299. **[deepl-mcp-server](https://github.com/DeepLcom/deepl-mcp-server)** - ⭐ 106
   A Model Context Protocol (MCP) server that provides translation capabilities using the DeepL API.

2300. **[okx-agent-trade-kit](https://github.com/dex-original/okx-agent-trade-kit)** - ⭐ 106
   okx trading bot okx agent mcp cli cryptocurrency okx api automated trading typescript okx trading bot model context protocol cursor ai trading crypto spot futures okx trading bot npm pnpm okx mcp open source quant defi cex okx trading bot algorithmic trading crypto bot okx trading bot okx api mcp okx trading bot crypto mcp

2301. **[deep-code-reasoning-mcp](https://github.com/evalops/deep-code-reasoning-mcp)** - ⭐ 106
   A Model Context Protocol (MCP) server that provides advanced code analysis and reasoning capabilities powered by Google's Gemini AI

2302. **[mcp-server-apple-events](https://github.com/FradSer/mcp-server-apple-events)** - ⭐ 106
   MCP server providing native macOS integration with Apple Reminders and Calendar via EventKit

2303. **[chat.md](https://github.com/rusiaaman/chat.md)** - ⭐ 106
   An md file as a chat interface and editable history in one.

2304. **[ToolsForMCPServer](https://github.com/tanaikech/ToolsForMCPServer)** - ⭐ 106
   The Gemini CLI confirmed that the MCP server built with Google Apps Script (GAS), a low-code platform, offers immense possibilities. If you've created snippets for GAS, these could be revitalized and/or leveraged in new ways by using them as the MCP server. The Gemini CLI and other MCP clients will be useful in achieving this.

2305. **[go-utcp](https://github.com/universal-tool-calling-protocol/go-utcp)** - ⭐ 106
    Official Go implementation of the UTCP

2306. **[academic-search-mcp-server](https://github.com/afrise/academic-search-mcp-server)** - ⭐ 105
   Academic Paper Search MCP Server for Claude Desktop integration. Allows Claude to access data from Semantic Scholar and Crossref.

2307. **[fullstack-langgraph-nextjs-agent](https://github.com/agentailor/fullstack-langgraph-nextjs-agent)** - ⭐ 105
     Production-ready Next.js template for building AI agents with LangGraph.js. Features MCP integration for dynamic tool loading, human-in-the-loop tool approval, persistent conversation memory   with PostgreSQL, and real-time streaming responses. Built with TypeScript, React, Prisma, and Tailwind CSS.

2308. **[GenesisCore](https://github.com/AIGODLIKE/GenesisCore)** - ⭐ 105
   One click installation! BlenderMCP tool that supports DeepSeek, Claude, and others, fully integrated into Blender!

2309. **[deep-code-reasoning-mcp](https://github.com/haasonsaas/deep-code-reasoning-mcp)** - ⭐ 105
   A Model Context Protocol (MCP) server that provides advanced code analysis and reasoning capabilities powered by Google's Gemini AI

2310. **[askimo](https://github.com/haiphucnguyen/askimo)** - ⭐ 105
   Local-first AI agent platform for desktop and CLI. Chat, RAG search, multi-step Plans workflows, MCP tools, and Agents integration. Supports OpenAI, Claude, Gemini, Grok, Ollama, LM Studio and more

2311. **[sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server)** - ⭐ 105
   An MCP server that provides safe, read-only access to SQLite databases through Model Context Protocol (MCP). This server is built with the FastMCP framework, which enables LLMs to explore and query SQLite databases with built-in safety features and query validation.

2312. **[ZipAgent](https://github.com/JiayuXu0/ZipAgent)** - ⭐ 105
   轻量级AI Agent框架，让你5分钟构建专属智能助手。Lightweight AI Agent framework. Build your AI assistant in 5 minutes.

2313. **[ApkMCP-Auto](https://github.com/kggzs/ApkMCP-Auto)** - ⭐ 105
   本项目是一个 Android 逆向工程工具集合，通过 MCP (Model Context Protocol) 协议将 AI 助手（如 Claude）与专业的 Android 反编译工具连接起来，实现智能化的 APK 分析与修改。

2314. **[linggen-memory](https://github.com/linggen/linggen-memory)** - ⭐ 105
   A local-first memory layer for AI (Cursor, Zed, Claude). Persistent architectural context via semantic search.

2315. **[splunk-mcp](https://github.com/livehybrid/splunk-mcp)** - ⭐ 105
   A Model Context Protocol (MCP) implementation for Splunk Enterprise and Cloud integration with Cursor IDE or Claude

2316. **[flowlens-mcp-server](https://github.com/magentic/flowlens-mcp-server)** - ⭐ 105
   FlowLens is an open-source MCP server that gives your coding agent (Claude Code, Cursor, Copilot, Codex) full browser context for in-depth debugging and regression testing.

2317. **[memory-mcp-server](https://github.com/okooo5km/memory-mcp-server)** - ⭐ 105
   A Model Context Protocol server that provides knowledge graph management capabilities.

2318. **[typescript-utcp](https://github.com/universal-tool-calling-protocol/typescript-utcp)** - ⭐ 105
   Official typescript implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

2319. **[agentcare-mcp](https://github.com/Kartha-AI/agentcare-mcp)** - ⭐ 104
   MCP Server for EMRs with FHIR

2320. **[freqtrade-mcp](https://github.com/kukapay/freqtrade-mcp)** - ⭐ 104
   An MCP server that integrates with the Freqtrade cryptocurrency trading bot.

2321. **[linggen](https://github.com/linggen/linggen)** - ⭐ 104
   A local-first memory layer for AI (Cursor, Zed, Claude). Persistent architectural context via semantic search.

2322. **[AutoGenesis](https://github.com/microsoft/AutoGenesis)** - ⭐ 104
   AutoGenesis is an AI-powered automated testing framework based on Model Context Protocol (MCP), supporting multiple platforms including desktop applications (Windows/macOS) and mobile applications (iOS/Android).

2323. **[vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server)** - ⭐ 104
   Official Vectorize MCP Server

2324. **[a2ajava](https://github.com/vishalmysore/a2ajava)** - ⭐ 104
   Pure java implementation of Google A2A protocol. Integrate your spring boot java applications with A2A protocol , includes client and sever both. Any agent built with a2ajava will also be exposed as MCP tool automatically

2325. **[claude-emporium](https://github.com/Vvkmnn/claude-emporium)** - ⭐ 104
   🏛 [UNDER CONSTRUCTION] A (roman) claude plugin marketplace

2326. **[alibaba-cloud-ops-mcp-server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server)** - ⭐ 103
   AlibabaCloud CloudOps MCP Server

2327. **[alibabacloud-ack-mcp-server](https://github.com/aliyun/alibabacloud-ack-mcp-server)** - ⭐ 103
   Alibaba Cloud's ack-mcp-server unifies container operations capabilities, enabling AI assistants and third-party AI agents to perform complex tasks via natural language through the MCP protocol, empowering container-native AIOps. DingTalk discussion group:  70080006301

2328. **[ARIES](https://github.com/Chieko-Seren/ARIES)** - ⭐ 103
   顺便一提，我们支持 RWKV | 「Intel 2025 人工智能创新大赛」🚀AutoOPS: Provide the chaos brought by language models to the operation and maintenance industry! 🏆使用 LLM 提供的动力实现全自动运维，支持 Windows Server/Linux/macOS/Cisco IOS，可进行全网自动管理，让我们颠覆运维行业【带外管理/自动运维/IoT设备管理/WebHook监控/任意平台/全模态Workflow】

2329. **[chronulus-mcp](https://github.com/ChronulusAI/chronulus-mcp)** - ⭐ 103
   MCP Server for Chronulus AI Forecasting and Prediction Agents

2330. **[smileyCoin](https://github.com/fefergrgrgrg/smileyCoin)** - ⭐ 103
   simple web ui to manage mcp (model context protocol) servers in the claude app

2331. **[gemini-desktop](https://github.com/kkrishnan90/gemini-desktop)** - ⭐ 103
   The MCP Gemini Electron App is a cross-platform desktop application that creates a seamless chat interface for Google's Gemini AI models with extensible capabilities through a Model Context Protocol (MCP) framework.

2332. **[http-oauth-mcp-server](https://github.com/NapthaAI/http-oauth-mcp-server)** - ⭐ 103
   Remote MCP server (SEE + Streamable HTTP) implementing the MCP spec's authorization extension. Use directly from your agents, or from Cursor / Claude with mcp-remote

2333. **[ruby-mcp-client](https://github.com/simonx1/ruby-mcp-client)** - ⭐ 103
   This is a Ruby implementation of MCP (Model Context Protocol) client

2334. **[solana-mcp](https://github.com/solanamcp/solana-mcp)** - ⭐ 103
   Solana Agent Kit MCP Server

2335. **[memory-bank-MCP](https://github.com/tuncer-byte/memory-bank-MCP)** - ⭐ 103
   Memory Bank is an MCP server that helps teams create, manage, and access structured project documentation. It generates and maintains a set of interconnected Markdown documents that capture different aspects of project knowledge, from high-level goals to technical details and day-to-day progress.

2336. **[wanaku](https://github.com/wanaku-ai/wanaku)** - ⭐ 103
   Wanaku MCP Router

2337. **[remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions)** - ⭐ 102
   Landing page for Remote MCP Server efforts in Azure Functions with links to all language stack specific repos.

2338. **[mcp-client-nodejs](https://github.com/ConardLi/mcp-client-nodejs)** - ⭐ 102
   Node.js Client Implementation for Model Context Protocol (MCP)

2339. **[mcp-screenshot-website-fast](https://github.com/just-every/mcp-screenshot-website-fast)** - ⭐ 102
   Quickly screenshots webpages and converts to an LLM friendly size

2340. **[godoc-mcp](https://github.com/mrjoshuak/godoc-mcp)** - ⭐ 102
   go doc mcp server

2341. **[all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol)** - ⭐ 102
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows

2342. **[zendesk-mcp-server](https://github.com/reminia/zendesk-mcp-server)** - ⭐ 102
   A Model Context Protocol server for Zendesk

2343. **[openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp)** - ⭐ 102
   A Model Context Protocol (MCP) tool server for OpenAI's GPT-4o/gpt-image-1 image generation and editing APIs.

2344. **[systemprompt-mcp-server](https://github.com/systempromptio/systemprompt-mcp-server)** - ⭐ 102
   A complete, production-ready implementation of a Model Context Protocol (MCP) server demonstrating OAuth 2.1, tools, prompts, resources, sampling, and notifications using Reddit as a real-world integration example.

2345. **[Abaqus-Control-MCP](https://github.com/Whfkl/Abaqus-Control-MCP)** - ⭐ 102
   让 AI 可以驱动 Abaqus建模。Connect Claude, Cursor, and other MCP clients directly to your active Abaqus/CAE session.

2346. **[sample-agentic-ai-demos](https://github.com/aws-samples/sample-agentic-ai-demos)** - ⭐ 101
   Collection of examples of how to use Model Context Protocol with AWS.

2347. **[pinescript-mcp-server](https://github.com/cklose2000/pinescript-mcp-server)** - ⭐ 101
   A Model Context Protocol (MCP) server for working with TradingView PineScript

2348. **[stock-mcp](https://github.com/huweihua123/stock-mcp)** - ⭐ 101
   专业的金融市场数据 MCP 服务器 - 支持A股/美股/加密货币，原生 MCP 协议，AI Agent 友好

2349. **[btp-sap-odata-to-mcp-server](https://github.com/lemaiwo/btp-sap-odata-to-mcp-server)** - ⭐ 101
   BTP CloudFoundry Node.js MCP server for SAP OData services integration

2350. **[Mureka-mcp](https://github.com/SkyworkAI/Mureka-mcp)** - ⭐ 101
   generate lyrics, song and background music(instrumental). Model Context Protocol (MCP) server.

2351. **[mcp-python-interpreter](https://github.com/yzfly/mcp-python-interpreter)** - ⭐ 101
   MCP Python Interpreter: run python code. Python-mcp-server, mcp-python-server, Code Executor

2352. **[autodev-codebase](https://github.com/anrgct/autodev-codebase)** - ⭐ 100
   A vector embedding-based code semantic search tool with MCP server and multi-model integration. Can be used as a pure CLI tool. Supports Ollama for fully local embedding and reranking, enabling complete offline operation and privacy protection for your code repository

2353. **[complete-intro-to-mcp](https://github.com/btholt/complete-intro-to-mcp)** - ⭐ 100
   The Complete Intro to MCP Servers, as taught for Frontend Masters by Brian Holt

2354. **[claude-code-mcp-enhanced](https://github.com/grahama1970/claude-code-mcp-enhanced)** - ⭐ 100
   Enhanced Claude Code MCP server with orchestration capabilities, reliability improvements, and self-contained execution patterns

2355. **[mpm-vibe-coding](https://github.com/halflifezyf2680/mpm-vibe-coding)** - ⭐ 100
   MPM is an MCP context-engineering layer for Vibe Coding, focused on three delivery bottlenecks: context loss, uncontrolled changes, and non-verifiable outcomes.

2356. **[AgentBoard](https://github.com/igrigorik/AgentBoard)** - ⭐ 100
   A switchboard for AI in your browser: wire in any model, script WebMCP tools, connect remote MCP servers, bring your commands.

2357. **[searxng-mul-mcp](https://github.com/jae-jae/searxng-mul-mcp)** - ⭐ 100
   A Model Context Protocol (MCP) server for SearXNG search engine with multi-query parallel search support

2358. **[mcp-hono-stateless](https://github.com/mhart/mcp-hono-stateless)** - ⭐ 100
   An example Hono MCP server using Streamable HTTP

2359. **[mcp-memory-keeper](https://github.com/mkreyman/mcp-memory-keeper)** - ⭐ 100
   MCP server for persistent context management in AI coding assistants

2360. **[cve-search_mcp](https://github.com/roadwy/cve-search_mcp)** - ⭐ 100
   A Model Context Protocol (MCP) server for querying the CVE-Search API

2361. **[unreal-mcp](https://github.com/runreal/unreal-mcp)** - ⭐ 100
   MCP server for Unreal Engine that uses Unreal Python Remote Execution

2362. **[square-mcp-server](https://github.com/square/square-mcp-server)** - ⭐ 100
   A Model Context Protocol (MCP) server for square

2363. **[monolith](https://github.com/tumourlove/monolith)** - ⭐ 100
   MCP plugin for Unreal Engine 5.7 — gives AI assistants full read/write access to Blueprints, Materials, Niagara VFX, Animation, Mesh, AI (BT/ST/EQS/SO), GAS, Logic Driver, ComboGraph, UI, Audio (Sound Cues + MetaSounds), and more. 1,226 actions across 16 modules. Zero Python dependency.

2364. **[Fusion-360-MCP-Server](https://github.com/AuraFriday/Fusion-360-MCP-Server)** - ⭐ 99
   Control Fusion 360 with any AI through Model Context Protocol (MCP)

2365. **[pywss](https://github.com/czasg/pywss)** - ⭐ 99
   一个轻量级的 Python Web 框架，一站式集成 MCP SSE、StreamHTTP 和 MCPO 协议，助你轻松构建MCP Server🔥

2366. **[mcp-typescript-sdk](https://github.com/emqx/mcp-typescript-sdk)** - ⭐ 99
   A TypeScript SDK for implementing Model Context Protocol (MCP) over MQTT, supporting both browser and Node.js environments.

2367. **[teams-mcp](https://github.com/floriscornel/teams-mcp)** - ⭐ 99
   MCP server providing comprehensive Microsoft Teams and Graph API access for AI assistants including messaging, search, and user management.

2368. **[lapras-mcp-server](https://github.com/lapras-inc/lapras-mcp-server)** - ⭐ 99
   lapras.com 公式MCP Server

2369. **[heimdall-mcp-server](https://github.com/lcbcFoo/heimdall-mcp-server)** - ⭐ 99
   Your AI Coding Assistant's Long-Term Memory

2370. **[mysql-mcp-server-sse](https://github.com/mangooer/mysql-mcp-server-sse)** - ⭐ 99
   MySQL query server based on the MCP sse.Multi-level SQL risk control & injection protection Docker support for quick deployment

2371. **[needle-mcp](https://github.com/needle-ai/needle-mcp)** - ⭐ 99
   Needle MCP Server for easy RAG.Long-term memory for LLMs.

2372. **[mighty-security](https://github.com/NineSunsInc/mighty-security)** - ⭐ 99
   Don't Simply Trust MCP Server Code, Validate and Scan

2373. **[openscad-mcp](https://github.com/quellant/openscad-mcp)** - ⭐ 99
   A Model Context Protocol (MCP) server for OpenSCAD 3D modeling and rendering

2374. **[turbular](https://github.com/raeudigerRaeffi/turbular)** - ⭐ 99
   A MCP server allowing LLM agents to easily connect and retrieve data from any database

2375. **[mcp-graphiti](https://github.com/rawr-ai/mcp-graphiti)** - ⭐ 99
   Graphiti Model Context Protocol (MCP) Server - An MCP server for knowledge graph management via Graphiti

2376. **[homeassistant-mcp](https://github.com/robbrad/homeassistant-mcp)** - ⭐ 99
   Home Assistant MCP Server - Control your smart home with AI assistants via the Model Context Protocol

2377. **[next-mcp-server](https://github.com/vertile-ai/next-mcp-server)** - ⭐ 99
   Help LLMs to understand your Next apps better

2378. **[zed-mcp-server-context7](https://github.com/akbxr/zed-mcp-server-context7)** - ⭐ 98
   Context7 MCP Server for Zed

2379. **[atomic-red-team-mcp](https://github.com/cyberbuff/atomic-red-team-mcp)** - ⭐ 98
   MCP server for Atomic Red Team

2380. **[mcp-server-idapro](https://github.com/fdrechsler/mcp-server-idapro)** - ⭐ 98
   A Model Context Protocol (MCP) server that enables AI assistants to interact with IDA Pro for reverse engineering and binary analysis tasks.

2381. **[Vibe-Coder-MCP](https://github.com/freshtechbro/Vibe-Coder-MCP)** - ⭐ 98
    Vibe-Coder-MCP server extends AI assistants with specialized software development tools.

2382. **[us-gov-open-data-mcp](https://github.com/lzinga/us-gov-open-data-mcp)** - ⭐ 98
   MCP server + TypeScript SDK for 40+ U.S. government data APIs — 250+ tools. Treasury, FRED, Congress, FDA, CDC, FEC, lobbying, and many more. Works with VS Code Copilot, Claude Desktop, Cursor.

2383. **[mcp_on_ruby](https://github.com/nagstler/mcp_on_ruby)** - ⭐ 98
   💎 A Ruby implementation of the Model Context Protocol

2384. **[editor-mcp-server](https://github.com/playcanvas/editor-mcp-server)** - ⭐ 98
   MCP Server for AI automation of the PlayCanvas Editor

2385. **[erpnext-mcp-server](https://github.com/rakeshgangwar/erpnext-mcp-server)** - ⭐ 98
   Connect AI assistants to your ERPNext instance via the Model Context Protocol (MCP) using the official Frappe API.

2386. **[mealie-mcp-server](https://github.com/rldiao/mealie-mcp-server)** - ⭐ 98
   MCP server that exposes Mealie APIs to MCP clients such as Claude Desktop

2387. **[mcp_on_ruby](https://github.com/rubyonai/mcp_on_ruby)** - ⭐ 98
   💎 A Ruby implementation of the Model Context Protocol

2388. **[MasterMCP](https://github.com/slowmist/MasterMCP)** - ⭐ 98
   A demonstration toolkit revealing potential security vulnerabilities in MCP (Model Context Protocol) frameworks through data poisoning, JSON injection, function overriding, and cross-MCP call attacks, exposing AI security issues while providing defense recommendations. For educational and research purposes only.

2389. **[z-image-studio](https://github.com/iconben/z-image-studio)** - ⭐ 97
   A Cli, a webUI, and a MCP server for the Z-Image-Turbo text-to-image generation model (Tongyi-MAI/Z-Image-Turbo base model as well as quantized models)

2390. **[mcp-kit](https://github.com/my-mcp-hub/mcp-kit)** - ⭐ 97
   A CLI tool to create MCP (Model Context Protocol) applications with ease.

2391. **[p4mcp-server](https://github.com/perforce/p4mcp-server)** - ⭐ 97
   [Community Supported] Perforce P4 MCP Server is a Model Context Protocol (MCP) server that integrates with the Perforce P4 version control system.

2392. **[MediaWiki-MCP-Server](https://github.com/ProfessionalWiki/MediaWiki-MCP-Server)** - ⭐ 97
   Model Context Protocol (MCP) Server to connect your AI with any MediaWiki

2393. **[mcp](https://github.com/vuetifyjs/mcp)** - ⭐ 97
   🤖 A Model Context Protocol (MCP) library for use with Agentic chat bots

2394. **[wp-mcp-ultimate](https://github.com/AgriciDaniel/wp-mcp-ultimate)** - ⭐ 96
   WordPress MCP Ultimate — Full MCP server with 58 WordPress abilities. Connect WordPress to any AI via Model Context Protocol.

2395. **[finance-trading-ai-agents-mcp](https://github.com/aitrados/finance-trading-ai-agents-mcp)** - ⭐ 96
   A comprehensive, free MCP server designed specifically for financial analysis and quantitative trading. This specialized platform offers one-click local deployment with a sophisticated department-based architecture that mirrors real financial company operations.

2396. **[AgentUp](https://github.com/always-further/AgentUp)** - ⭐ 96
   Portable , scalable , secure AI Agents

2397. **[langfuse-mcp](https://github.com/avivsinai/langfuse-mcp)** - ⭐ 96
   A Model Context Protocol (MCP) server for Langfuse, enabling AI agents to query Langfuse trace data for enhanced debugging and observability

2398. **[dicom-mcp](https://github.com/ChristianHinge/dicom-mcp)** - ⭐ 96
   Model Context Protocol (MCP) for interacting with dicom servers (PACS etc.)

2399. **[mcp-sse-demo](https://github.com/cnych/mcp-sse-demo)** - ⭐ 96
   claude mcp sse demo with server and client(cli、web)

2400. **[blender-open-mcp](https://github.com/dhakalnirajan/blender-open-mcp)** - ⭐ 96
   Open Models MCP for Blender Using Ollama

2401. **[mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms)** - ⭐ 96
   Version 2.2 - 54 tools available - an MCP server for interacting with the Canvas LMS API. This server allows you to manage courses, assignments, enrollments, and grades within Canvas.

2402. **[NetworkOps_Platform](https://github.com/E-Conners-Lab/NetworkOps_Platform)** - ⭐ 96
   AI-powered network automation via Netbox and Model Context Protocol (MCP). 178 tools for multi-vendor infrastructure   management, self-healing agents, drift detection, and a real-time web dashboard.

2403. **[parallel-browser-mcp](https://github.com/etairl/parallel-browser-mcp)** - ⭐ 96
   An MCP server for parallel browser automation by AI agents with multiple cloud providers

2404. **[codesys-mcp-toolkit](https://github.com/johannesPettersson80/codesys-mcp-toolkit)** - ⭐ 96
   Model Context Protocol server for CODESYS automation platform

2405. **[mcp-taiwan-legal-db](https://github.com/lawchat-oss/mcp-taiwan-legal-db)** - ⭐ 96
   台灣司法院判決 + 全國法規資料庫 MCP server · Query Taiwan legal data from any MCP AI agent

2406. **[bloodhound_mcp](https://github.com/mwnickerson/bloodhound_mcp)** - ⭐ 96
   A Model Context Protocol (MCP) server to converse with data in Bloodhound

2407. **[sparql-llm](https://github.com/sib-swiss/sparql-llm)** - ⭐ 96
   🦜✨ Chat system, MCP server, and reusable components to improve LLMs capabilities when generating SPARQL queries

2408. **[api2mcp4j](https://github.com/TheEterna/api2mcp4j)** - ⭐ 96
   This is a revolutionary AI MCP plugin with excellent pluggable and encapsulated features. With just a few lines of configuration, it can easily integrate into your Spring boot web program and give it MCP capabilities,inheriting the powerful engineering capabilities of the Spring series framework

2409. **[gossiphs](https://github.com/williamfzc/gossiphs)** - ⭐ 96
   "Zero setup" & "Blazingly fast" general code file relationship analysis. With Python & Rust. Based on tree-sitter and git analysis. Support MCP and ready for AI🤖

2410. **[pubmed-mcp-server](https://github.com/cyanheads/pubmed-mcp-server)** - ⭐ 95
   MCP server for the NCBI E-utilities API. Search PubMed, fetch article metadata and full text, generate citations, explore MeSH terms, and discover related research. STDIO or Streamable HTTP.

2411. **[schedcp](https://github.com/eunomia-bpf/schedcp)** - ⭐ 95
   MCP Server for Linux Scheduler Management and Auto optimization

2412. **[leetcode-mcp-server](https://github.com/jinzcdev/leetcode-mcp-server)** - ⭐ 95
   An MCP server enabling automated access to LeetCode's problems, solutions, and public data with optional authentication for user-specific features, supporting leetcode.com & leetcode.cn sites.

2413. **[junos-mcp-server](https://github.com/Juniper/junos-mcp-server)** - ⭐ 95
   This is a Junos Model Context Protocol (MCP) Server project that provides a bridge between MCP-compatible clients (like Claude Desktop) and Juniper Junos network devices.

2414. **[EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP)** - ⭐ 95
   The first open-source Model Context Protocol server enabling AI assistants and applications to interact programmatically with EnergyPlus building energy simulation.

2415. **[oxylabs-mcp](https://github.com/oxylabs/oxylabs-mcp)** - ⭐ 95
   Official Oxylabs MCP integration

2416. **[agent-toolkit](https://github.com/sanity-io/agent-toolkit)** - ⭐ 95
   Collection of resources to help AI agents build better with Sanity.

2417. **[awesome-mcp-servers-devops](https://github.com/WagnerAgent/awesome-mcp-servers-devops)** - ⭐ 95
   A curated, DevOps-focused list of Model Context Protocol (MCP) servers—covering source control, IaC, Kubernetes, CI/CD, cloud, observability, security, and collaboration—with a bias toward maintained, production-ready integrations.

2418. **[identity](https://github.com/agntcy/identity)** - ⭐ 94
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

2419. **[molecule-mcp](https://github.com/ChatMol/molecule-mcp)** - ⭐ 94
   A model-context-protocol server for molecules.

2420. **[generative-ui-playground](https://github.com/CopilotKit/generative-ui-playground)** - ⭐ 94
   Interact with all three types of generative UI, all in one interface

2421. **[mcp-1c](https://github.com/feenlace/mcp-1c)** - ⭐ 94
   MCP server for 1C:Enterprise — AI assistant sees your configuration and generates accurate BSL code. One binary, zero dependencies, 9 tools.

2422. **[wecom-bot-mcp-server](https://github.com/loonghao/wecom-bot-mcp-server)** - ⭐ 94
   A Python server implementation for WeCom (WeChat Work) bot that follows the Model Context Protocol (MCP). This server provides a standardized interface for handling automated messaging and context-aware interactions within enterprise WeChat environments.

2423. **[mem0-mcp](https://github.com/pinkpixel-dev/mem0-mcp)** - ⭐ 94
   ✨ mem0 MCP Server: A memory system using mem0 for AI applications with model context protocl (MCP) integration. Enables long-term memory for AI agents as a drop-in MCP server.

2424. **[surrealmcp](https://github.com/surrealdb/surrealmcp)** - ⭐ 94
   The official MCP server for SurrealDB

2425. **[legion-mcp](https://github.com/TheRaLabs/legion-mcp)** - ⭐ 94
   A server that helps people access and query data in databases using the Legion Query Runner with Model Context Protocol (MCP) in Python.

2426. **[pluggedin-app](https://github.com/VeriTeknik/pluggedin-app)** - ⭐ 94
   The Crossroads for AI Data Exchanges. A unified, self-hostable web interface for discovering, configuring, and managing Model Context Protocol (MCP) servers—bringing together AI tools, workspaces, prompts, and logs from multiple MCP sources (Claude, Cursor, etc.) under one roof.

2427. **[bouvet](https://github.com/vrn21/bouvet)** - ⭐ 94
   Sandbox for Agents

2428. **[semantic-scholar-fastmcp-mcp-server](https://github.com/zongmin-yu/semantic-scholar-fastmcp-mcp-server)** - ⭐ 94
   A FastMCP server implementation for the Semantic Scholar API, providing comprehensive access to academic paper data, author information, and citation networks.

2429. **[awsome_kali_MCPServers](https://github.com/ccq1/awsome_kali_MCPServers)** - ⭐ 93
   awsome kali MCPServers is a set of MCP servers tailored for Kali Linux

2430. **[altium-mcp](https://github.com/coffeenmusic/altium-mcp)** - ⭐ 93
   Altium Model Context Protocol server and Altium API script

2431. **[tradingview-chart-mcp](https://github.com/ertugrul59/tradingview-chart-mcp)** - ⭐ 93
   MCP server that captures TradingView chart images via Selenium — supports any ticker/interval with browser pooling for concurrent performance

2432. **[ollama-mcp-bridge](https://github.com/jonigl/ollama-mcp-bridge)** - ⭐ 93
   Extend the Ollama API with dynamic AI tool integration from multiple MCP (Model Context Protocol) servers. Fully compatible, transparent, and developer-friendly, ideal for building powerful local LLM applications, AI agents, and custom chatbots

2433. **[mcpcat-typescript-sdk](https://github.com/MCPCat/mcpcat-typescript-sdk)** - ⭐ 93
   MCPcat is an analytics platform for MCP server owners 🐱.

2434. **[gospy](https://github.com/monsterxx03/gospy)** - ⭐ 93
   Non-Invasive goroutine inspector

2435. **[mcp-server](https://github.com/OctopusDeploy/mcp-server)** - ⭐ 93
   Octopus Deploy Official MCP Server

2436. **[memory-mcp-server-go](https://github.com/okooo5km/memory-mcp-server-go)** - ⭐ 93
   A Model Context Protocol server that provides knowledge graph management capabilities.

2437. **[photon](https://github.com/portel-dev/photon)** - ⭐ 93
   Define intent once. Photon turns a single TypeScript file into CLI tools, MCP servers, and web interfaces.

2438. **[infobus-mcp](https://github.com/simovilab/infobus-mcp)** - ⭐ 93
   Model Context Protocol server enabling AI assistants to access transit information through standardized interfaces

2439. **[tiger-cli](https://github.com/timescale/tiger-cli)** - ⭐ 93
   Tiger CLI is the command-line interface for Tiger Cloud. It includes an MCP server for helping coding agents write production-level Postgres code.

2440. **[elektron-mcp](https://github.com/zerubeus/elektron-mcp)** - ⭐ 93
   MCP sever for controlling Elektron devices using LLMs

2441. **[chat-ui](https://github.com/AI-QL/chat-ui)** - ⭐ 92
   Single-File AI Chatbot UI with Multimodal & MCP Support: An All-in-One HTML File for a Streamlined Chatbot Conversational Interface

2442. **[unity-mcp-plugin](https://github.com/AnkleBreaker-Studio/unity-mcp-plugin)** - ⭐ 92
   Unity MCP Plugin (UPM) — Editor bridge for AI-assisted game development. Enables Claude, Cursor & MCP-compatible AI to control Unity Editor with 268 tools: scenes, GameObjects, components, builds, profiling, Shader Graph, Amplify Shader Editor, terrain, physics, NavMesh & more. Free & open source.

2443. **[buddy](https://github.com/fiorastudio/buddy)** - ⭐ 92
   A virtual pet companion for your AI — Designed to provide in-context code review feedback with personality. Grow with your buddy and level up together. Works with Claude Code, Codex, CursorCLI, Github CopilotCLI, OpenClaw, and any MCP compatible clients

2444. **[woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server)** - ⭐ 92
   A WooCommerce (MCP) Model Context Protocol server

2445. **[open-mcp-auth-proxy](https://github.com/wso2/open-mcp-auth-proxy)** - ⭐ 92
   Authentication and Authorization Proxy for MCP Servers

2446. **[mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw)** - ⭐ 91
   An MCP stdio to HTTP SSE transport gateway with example server and MCP client

2447. **[perplexity-webui-scraper](https://github.com/henrique-coder/perplexity-webui-scraper)** - ⭐ 91
   An advanced, high-performance Python client, MCP server, and REST API for reverse-engineering Perplexity AI's WebUI.

2448. **[houtini-lm](https://github.com/houtini-ai/houtini-lm)** - ⭐ 91
   MCP server that saves Claude Code tokens by delegating bounded tasks to local or cloud LLMs. Works with LM Studio, Ollama, vLLM, DeepSeek, Groq, Cerebras.

2449. **[litegraph](https://github.com/litegraphdb/litegraph)** - ⭐ 91
   Lightweight graph database with relational, vector, and MCP support, designed to power knowledge and artificial intelligence persistence and retrieval.

2450. **[vibe](https://github.com/michiosw/vibe)** - ⭐ 91
   Open-Source AI-powered web browser. Browse the web with your own LLM API key. Alternative to Dia / Comet.

2451. **[MiniMax-Coding-Plan-MCP](https://github.com/MiniMax-AI/MiniMax-Coding-Plan-MCP)** - ⭐ 91
   Specialized MiniMax Model Context Protocol (MCP) server designed for coding-plan users, featuring AI-powered search and vision analysis APIs optimized for code development workflows

2452. **[ncp](https://github.com/portel-dev/ncp)** - ⭐ 91
   Natural Context Provider (NCP). Your MCPs, supercharged. Find any tool instantly, load on demand, run on schedule, ready for any   client. Smart loading saves tokens and energy.

2453. **[crawl4ai-mcp-server](https://github.com/sadiuysal/crawl4ai-mcp-server)** - ⭐ 91
   🕷️ A lightweight Model Context Protocol (MCP) server that exposes Crawl4AI web scraping and crawling capabilities as tools for AI agents.  Similar to Firecrawl's API but self-hosted and free. Perfect for integrating web scraping into your AI workflows with OpenAI Agents SDK, Cursor, Claude Code, and other MCP-compatible tools.

2454. **[mcp-excel-server](https://github.com/yzfly/mcp-excel-server)** - ⭐ 91
   The Excel MCP Server is a powerful tool that enables natural language interaction with Excel files through the Model Context Protocol (MCP). It provides a comprehensive set of capabilities for reading, analyzing, visualizing, and writing Excel data.

2455. **[mcp-ui](https://github.com/bitshift-byte/mcp-ui)** - ⭐ 90
   基于MCP(Model Context Protocol)的智能聊天应用，支持Web和桌面环境。集成OpenAI/Anthropic API，提供MCP服务器的所有工具能力。简洁现代的UI设计，支持跨平台部署。

2456. **[mcp-ui](https://github.com/machaojin1917939763/mcp-ui)** - ⭐ 90
   基于MCP(Model Context Protocol)的智能聊天应用，支持Web和桌面环境。集成OpenAI/Anthropic API，提供MCP服务器的所有工具能力。简洁现代的UI设计，支持跨平台部署。

2457. **[MCP4EDA](https://github.com/NellyW8/MCP4EDA)** - ⭐ 90
   This is the Github Repo for the paper: MCP4EDA: LLM-Powered Model Context Protocol RTL-to-GDSII Automation with Backend Aware Synthesis Optimization. MCP server for a collection of open-source EDA tools

2458. **[NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server)** - ⭐ 90
   A Model Context Protocol (MCP) server for NASA APIs, providing a standardized interface for AI models to interact with NASA's vast array of data sources.

2459. **[furi](https://github.com/ashwwwin/furi)** - ⭐ 89
   CLI & API for MCP management

2460. **[powerpoint-mcp](https://github.com/Ayushmaniar/powerpoint-mcp)** - ⭐ 89
   Open Source Model Context Protocol server for PowerPoint automation on Windows via pywin32

2461. **[mcp-rest-api](https://github.com/dkmaker/mcp-rest-api)** - ⭐ 89
   A TypeScript-based MCP server that enables testing of REST APIs through Cline. This tool allows you to test and interact with any REST API endpoints directly from your development environment.

2462. **[turbomcp](https://github.com/Epistates/turbomcp)** - ⭐ 89
   A full featured, enterprise grade rust MCP SDK

2463. **[gno](https://github.com/gmickel/gno)** - ⭐ 89
   Local AI-powered document search and editing with first-in-class hybrid retrieval, LLM answers, WebUI, REST API and MCP support for AI clients.

2464. **[mcp-velociraptor](https://github.com/mgreen27/mcp-velociraptor)** - ⭐ 89
   VelociraptorMCP is a Model Context Protocol bridge for exposing LLMs to MCP clients.

2465. **[fred-mcp-server](https://github.com/stefanoamorelli/fred-mcp-server)** - ⭐ 89
   Open-source FRED MCP Server (Federal Reserve Economic Data)

2466. **[office-editor-mcp](https://github.com/theWDY/office-editor-mcp)** - ⭐ 89
   基于MCP(Model Context Protocol)的Office文档处理助手，支持在MCP Client中创建和编辑Word、Excel、Powerpoint文档。

2467. **[apps-sdk-template](https://github.com/alpic-ai/apps-sdk-template)** - ⭐ 88
   A minimalist Typescript ChatGPT App based on the Skybridge framework

2468. **[ChEMBL-MCP-Server](https://github.com/Augmented-Nature/ChEMBL-MCP-Server)** - ⭐ 88
   A comprehensive Model Context Protocol (MCP) server providing advanced access to the ChEMBL chemical database.

2469. **[ue-mcp](https://github.com/db-lyon/ue-mcp)** - ⭐ 88
   Complete Unreal Engine development toolkit exposed as MCP tools.

2470. **[line-desktop-mcp](https://github.com/dtwang/line-desktop-mcp)** - ⭐ 88
   透過 MCP（Model Context Protocol），使 AI 工具能夠與 LINE Desktop 整合，並執行訊息的讀取與發送操作。Through the MCP (Model Context Protocol), AI tools can be integrated with LINE Desktop to perform message reading and sending operations.

2471. **[neurolink](https://github.com/juspay/neurolink)** - ⭐ 88
   Streams are the future of AI powered by unlimited free tokens.

2472. **[claudex](https://github.com/kunwar-shah/claudex)** - ⭐ 88
   MCP server with persistent memory + FTS5 search for Claude Code conversation history. Index your ~/.claude/projects/, expose 10 MCP tools, browse via web UI. MIT-licensed.

2473. **[ccxt-mcp](https://github.com/lazy-dinosaur/ccxt-mcp)** - ⭐ 88
   CCXT MCP Server bridges the gap between AI models and cryptocurrency trading by providing a standardized interface through the Model Context Protocol. Created to empower automated trading strategies, this tool allows AI assistants like Claude and GPT to directly interact with over 100 cryptocurrency exchanges without requiring users to write comple

2474. **[mcpgen](https://github.com/lyeslabs/mcpgen)** - ⭐ 88
   Generate Go MCP server boilerplate from OpenAPI 3 specifications

2475. **[amap-mcp-server](https://github.com/sugarforever/amap-mcp-server)** - ⭐ 88
   高德地图MCP Server，支持stdio, sse和streamable-http

2476. **[Mira](https://github.com/vwww-droid/Mira)** - ⭐ 88
   🔬 Mobile runtime detection workbench for AI (iOS and Android)

2477. **[sp500-mcp-server](https://github.com/zhensherlock/sp500-mcp-server)** - ⭐ 88
   An MCP server and Next.js web app for querying S&P 500 company data from Supabase, with tools for company info, news, officers, and SEC filings, plus embedded MCP App UI resources, Elicitation, and Sampling support.

2478. **[achatbot](https://github.com/ai-bot-pro/achatbot)** - ⭐ 87
   An open source chat bot architecture for voice/vision (and multimodal) assistants,  local(CPU/GPU bound) and remote(I/O bound) to run.

2479. **[mcpmu](https://github.com/Bigsy/mcpmu)** - ⭐ 87
   TUI-based MCP server multiplexer, configure all your MCP's in a single MCP with profiles

2480. **[awesome-openid-connect](https://github.com/cerberauth/awesome-openid-connect)** - ⭐ 87
   OpenID Connect, the authentication protocol and identity layer on top of OAuth 2.0 used in many SSO and adopted in many social logins (Apple, Facebook, Google, ...etc). Find this curated list of providers, services, libraries, and resources to adopt it and know more about existing specs.

2481. **[mcp-dbutils](https://github.com/donghao1393/mcp-dbutils)** - ⭐ 87
   数读 是一件可以让你的大模型安全连接到数据库的MCP工具。| DButils is an all-in-one MCP service that enables your AI to do data analysis by harnessing versatile types of database (sqlite, mysql, postgres, and more) within a unified configuration of multiple connections in a secured way (like SSL and controlled write access).

2482. **[sdl-mcp](https://github.com/GlitterKill/sdl-mcp)** - ⭐ 87
   SDL-MCP (Symbol Delta Ledger MCP Server) is a cards-first context system for coding agents that saves tokens and improves context.

2483. **[mcp-gopls](https://github.com/hloiseau/mcp-gopls)** - ⭐ 87
   Model Context Protocol (MCP) server for Go using gopls – LSP-powered analysis, tests, coverage, and tooling.

2484. **[slidev-mcp](https://github.com/LSTM-Kirigaya/slidev-mcp)** - ⭐ 87
   mcp server for slidev to make web ppt quickly and elegantly

2485. **[remindb](https://github.com/radimsem/remindb)** - ⭐ 87
   An agentic memory database that cuts session tokens by 75–99%. One portable SQLite file — your agent's memory, anywhere.

2486. **[formanator](https://github.com/timrogers/formanator)** - ⭐ 87
   Submit and manage Forma (https://joinforma.com) claims from the command line and Model Context Protocol (MCP) clients

2487. **[youtrack-mcp](https://github.com/tonyzorin/youtrack-mcp)** - ⭐ 87
   Model Context Protocol Server for YouTrack - Multi-platform support (ARM64/Apple Silicon + AMD64) with comprehensive API integration

2488. **[slither-mcp](https://github.com/trailofbits/slither-mcp)** - ⭐ 87
   MCP server for Slither static analysis of Solidity smart contracts

2489. **[github-chat-mcp](https://github.com/AsyncFuncAI/github-chat-mcp)** - ⭐ 86
   A Model Context Protocol (MCP) for analyzing and querying GitHub repositories using the GitHub Chat API.

2490. **[SillyTavern-MCP-Client](https://github.com/bmen25124/SillyTavern-MCP-Client)** - ⭐ 86
   An extension of MCP for SillyTavern.

2491. **[mcp-server](https://github.com/cap-js/mcp-server)** - ⭐ 86
   MCP server for AI-assisted development of CAP applications

2492. **[FrontAgent](https://github.com/ceilf6/FrontAgent)** - ⭐ 86
   AI agent platform for frontend engineering with SDD constraints & MCP-controlled automation. | 面向前端工程的企业级 AI Agent 平台

2493. **[react-agent-hooks](https://github.com/chuanqisun/react-agent-hooks)** - ⭐ 86
   Turn React hooks into LLM tools

2494. **[aivectormemory](https://github.com/Edlineas/aivectormemory)** - ⭐ 86
   aivectormemory 是一款基于 Model Context Protocol (MCP) 开发的OpenClaw、OpenCode、ClaudeCodeAI记忆管理工具。它专门为 Claude、OpenCode、Cursor 和 主流IDE 编程工具设计，通过向量数据库技术解决 AI 在不同对话会话中「健忘」的问题。aivectormemory: A lightweight MCP Server enabling persistent, cross-session memory for AI-powered IDEs via vector search.

2495. **[deterministic-agent-control-protocol](https://github.com/elliot35/deterministic-agent-control-protocol)** - ⭐ 86
   Governance gateway for AI agents — bounded, auditable, session-aware control with MCP proxy, shell proxy & HTTP API. Works with Cursor, Claude Code, Codex, and any MCP-compatible agent.

2496. **[ramparts](https://github.com/highflame-ai/ramparts)** - ⭐ 86
   mcp scan that scans any mcp server for indirect attack vectors and security or configuration vulnerabilities

2497. **[vggt-mps](https://github.com/jmanhype/vggt-mps)** - ⭐ 86
   VGGT 3D Vision Agent optimized for Apple Silicon with Metal Performance Shaders

2498. **[modular-context-obsidian-plugin](https://github.com/klemensgc/modular-context-obsidian-plugin)** - ⭐ 86
   Modular Context | Karpathy LLM Knowledge Base + Gmail & G-Cal — multi-account MCP server for Claude Code, encrypted local-first

2499. **[clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server)** - ⭐ 86
   A Model Context Protocol (MCP) server for Microsoft Clarity

2500. **[agent-tool-protocol](https://github.com/mondaycom/agent-tool-protocol)** - ⭐ 86
   Agent Tool Protocol

2501. **[ragie-mcp-server](https://github.com/ragieai/ragie-mcp-server)** - ⭐ 86
   Ragie Model Context Protocol Server

2502. **[mcp-server-llamacloud](https://github.com/run-llama/mcp-server-llamacloud)** - ⭐ 86
   A MCP server connecting to managed indexes on LlamaCloud

2503. **[uml-mcp](https://github.com/antoinebou12/uml-mcp)** - ⭐ 85
   UML-MCP Server is a UML diagram generation tool based on MCP (Model Context Protocol), which can help users generate various types of UML diagrams through natural language description or directly writing PlantUML and Mermaid and Kroki https://uml-mcp.vercel.app/docs

2504. **[FreeCAD-MCP](https://github.com/ATOI-Ming/FreeCAD-MCP)** - ⭐ 85
   FreeCAD plugin for automating model creation and control via Model Contro Protocol (MCP). Provides a MCP server,GUl panel, and client for running macros,managing documents, and adjusting views.

2505. **[reaper-mcp](https://github.com/bonfire-audio/reaper-mcp)** - ⭐ 85
   A comprehensive Model Context Protocol (MCP) server that enables AI agents to create fully mixed and mastered tracks in REAPER with both MIDI and audio capabilities.

2506. **[godot-mcp](https://github.com/bradypp/godot-mcp)** - ⭐ 85
   A Model Context Protocol (MCP) server for interacting with the Godot game engine.

2507. **[github-stars](https://github.com/ccbikai/github-stars)** - ⭐ 85
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

2508. **[mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci)** - ⭐ 85
   A specialized server implementation for the Model Context Protocol (MCP) designed to integrate with CircleCI's development workflow. This project serves as a bridge between CircleCI's infrastructure and the Model Context Protocol, enabling enhanced AI-powered development experiences.

2509. **[fabric-mcp](https://github.com/ksylvan/fabric-mcp)** - ⭐ 85
   Fabric MCP Server: Seamlessly integrate Fabric AI capabilities into MCP-enabled tools like IDEs and chat interfaces.

2510. **[agentic-tools-mcp](https://github.com/Pimzino/agentic-tools-mcp)** - ⭐ 85
   A comprehensive Model Context Protocol (MCP) server providing AI assistants with powerful task management and agent memories capabilities with project-specific storage.

2511. **[airtable-mcp](https://github.com/rashidazarang/airtable-mcp)** - ⭐ 85
   Airtable integration for AI-powered applications via Anthropic's Model Context Protocol (MCP)

2512. **[purple-mcp](https://github.com/Sentinel-One/purple-mcp)** - ⭐ 85
   Access SentinelOne's Purple AI and security services through the Model Context Protocol (MCP) - query alerts, vulnerabilities, misconfigurations, and inventory

2513. **[mcp-memory-libsql](https://github.com/spences10/mcp-memory-libsql)** - ⭐ 85
   🧠 High-performance persistent memory system for Model Context Protocol (MCP) powered by libSQL. Features vector search, semantic knowledge storage, and efficient relationship management - perfect for AI agents and knowledge graph applications.

2514. **[rohlik-mcp](https://github.com/tomaspavlin/rohlik-mcp)** - ⭐ 85
   MCP server that lets you shop groceries across the Rohlik Group platforms (Rohlik.cz, Knuspr.de, Gurkerl.at, Kifli.hu, Sezamo.ro)

2515. **[mcp](https://github.com/twilio-labs/mcp)** - ⭐ 85
   Monorepo providing 1) OpenAPI to MCP Tool generator 2) Exposing all of Twilio's API as MCP Tools

2516. **[mcp-victorialogs](https://github.com/VictoriaMetrics/mcp-victorialogs)** - ⭐ 85
   The implementation of Model Context Protocol (MCP) server for VictoriaLogs.

2517. **[jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server)** - ⭐ 85
   This is an implementation project of a JVM-based MCP (Model Context Protocol) server. The project aims to provide a standardized MCP server implementation for the JVM platform, enabling AI models to better interact with the Java ecosystem.

2518. **[advanced-unity-mcp](https://github.com/codemaestroai/advanced-unity-mcp)** - ⭐ 84
   Public repository for Advanced Unity MCP by Code Maestro (www.code-maestro.com).

2519. **[mcp-dockmaster](https://github.com/dcSpark/mcp-dockmaster)** - ⭐ 84
   MCP Dockmaster allows you to easily install and manage MCP servers. Available for Mac, Windows and Linux as a Desktop App, CLI and a library.

2520. **[abaqus-mcp-server](https://github.com/jianzhichun/abaqus-mcp-server)** - ⭐ 84
   An MCP (Model Context Protocol) server designed to interact with an already running Abaqus/CAE Graphical User Interface (GUI). It allows for the execution of Python scripts within the Abaqus environment and retrieval of messages from the Abaqus message log/area, all through MCP tools.

2521. **[mcp-server](https://github.com/keboola/mcp-server)** - ⭐ 84
   Model Context Protocol (MCP) Server for the Keboola Platform

2522. **[mcp-github-project-manager](https://github.com/kunwarVivek/mcp-github-project-manager)** - ⭐ 84
   a mcp server to manage github project's functionality

2523. **[spiceflow-framework](https://github.com/remorses/spiceflow-framework)** - ⭐ 84
   Super Simple API framework, type safe, automatic OpenAPI, MCP support, client RPC, streaming with SSE

2524. **[mcp-monitor](https://github.com/seekrays/mcp-monitor)** - ⭐ 84
   A system monitoring tool that exposes system metrics via the Model Context Protocol (MCP). This tool allows LLMs to retrieve real-time system information through an MCP-compatible interface.

2525. **[chimp](https://github.com/softwaremill/chimp)** - ⭐ 84
   Build type-safe, boilerplate-less MCP servers and clients in Scala

2526. **[cursor-rust-tools](https://github.com/terhechte/cursor-rust-tools)** - ⭐ 84
   A MCP server to allow the LLM in Cursor to access Rust Analyzer, Crate Docs and Cargo Commands.

2527. **[Awesome-Claude-MCP-Servers](https://github.com/win4r/Awesome-Claude-MCP-Servers)** - ⭐ 84
   A curated list of Model Context Protocol (MCP) servers optimized for Claude AI assistants.

2528. **[mcp-forge](https://github.com/achetronic/mcp-forge)** - ⭐ 83
   A complete MCP server template that include vitamins (oauth authentication included)

2529. **[altk-evolve](https://github.com/AgentToolkit/altk-evolve)** - ⭐ 83
   Self improving agents through iterations

2530. **[mcp-wolframalpha](https://github.com/akalaric/mcp-wolframalpha)** - ⭐ 83
   A Python-powered Model Context Protocol MCP server and client that uses Wolfram Alpha via API.

2531. **[mcp-node](https://github.com/algolia/mcp-node)** - ⭐ 83
   MCP server for interacting with Algolia

2532. **[claude-swarm](https://github.com/cj-vana/claude-swarm)** - ⭐ 83
   MCP server for orchestrating parallel Claude Code worker swarms with protocol-based behavioral governance, persistent state, and real-time monitoring dashboard

2533. **[ComIDP-MCP-Server](https://github.com/ComPDFKit/ComIDP-MCP-Server)** - ⭐ 83
   A lightweight MCP (Model Context Protocol) server for integrating ComPDF AI with Claude Desktop, enabling AI-powered intelligent document processing and data extraction from PDFs via natural language.

2534. **[xc-mcp](https://github.com/conorluddy/xc-mcp)** - ⭐ 83
   XCode CLI MCP: Convenience wrapper for Xcode CLI tools & iOS Simulator. Progressive disclosure of tool responses to reduce context usage.  Use --mini param for build-only with tiny context footprint.

2535. **[ols4](https://github.com/EBISPOT/ols4)** - ⭐ 83
   The EMBL-EBI Ontology Lookup Service (OLS)

2536. **[gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp)** - ⭐ 83
   Interact seamlessly with GitLab repositories to manage merge requests and issues. Fetch details, add comments, and streamline your code review process with ease.

2537. **[ls-mcp](https://github.com/lirantal/ls-mcp)** - ⭐ 83
   List MCP Server configurations in your system used by AI applications like Cursor, Claude Desktop, VS Code and others

2538. **[zed-mcp-server-github](https://github.com/LoamStudios/zed-mcp-server-github)** - ⭐ 83
   A GitHub MCP Server extension for Zed

2539. **[xiaozhi-mcp-ha](https://github.com/mac8005/xiaozhi-mcp-ha)** - ⭐ 83
   A Home Assistant Custom Integration (HACS) that connects Xiaozhi ESP32 AI chatbot to Home Assistant via MCP

2540. **[viper](https://github.com/ozanunal0/viper)** - ⭐ 83
   🛡️ VIPER: Stay ahead of threats with AI-driven vulnerability intelligence. Prioritize CVEs effectively using NVD, EPSS, CISA KEV, and Google Gemini insights, all on an interactive dashboard

2541. **[MayaMCP](https://github.com/PatrickPalmer/MayaMCP)** - ⭐ 83
   Model Context Protocol (MCP) server implementation for Autodesk Maya

2542. **[mcp-n8n-builder](https://github.com/spences10/mcp-n8n-builder)** - ⭐ 83
   🪄 MCP server for programmatic creation and management of n8n workflows. Enables AI assistants to build, modify, and manage workflows without direct user intervention through a comprehensive set of tools and resources for interacting with n8n's REST API.

2543. **[mcp-server-stability-ai](https://github.com/tadasant/mcp-server-stability-ai)** - ⭐ 83
   MCP Server integrating MCP Clients with Stability AI-powered image manipulation functionalities: generate, edit, upscale, and more.

2544. **[osm-mcp](https://github.com/wiseman/osm-mcp)** - ⭐ 83
   Model Context Protocol server for OpenStreetMap data

2545. **[mcphub](https://github.com/Cognitive-Stack/mcphub)** - ⭐ 82
   MCPHub is an embeddable Model Context Protocol (MCP) solution for AI services. Seamlessly integrate MCP servers with OpenAI Agents, LangChain, and Autogen frameworks through a unified interface. Simplifies configuration, setup, and management of MCP tools across different AI applications.

2546. **[freecad-mcp](https://github.com/contextform/freecad-mcp)** - ⭐ 82
   FreeCAD MCP - Open-source Model Context Protocol server for FreeCAD automation

2547. **[Meting-Agent](https://github.com/ELDment/Meting-Agent)** - ⭐ 82
   🪐 面向 AI 的多音乐平台的 API 代理 • 网易云 • QQ音乐 • 酷狗 • 酷我 🎻 Multi-platform music API agent for AI • NetEase • QQ Music • KuGou • Kuwo

2548. **[windbg-mcp](https://github.com/gengstah/windbg-mcp)** - ⭐ 82
   An MCP (Model Context Protocol) server that turns all pybag Windows debugger functions into native MCP tools. It lets MCP-compatible clients (Claude Desktop, Claude Code, Cowork, OpenAI Codex CLI, Cursor, and custom agents) control user-mode processes, kernel sessions, and crash dump analysis via structured JSON calls.

2549. **[aws-security-mcp](https://github.com/groovyBugify/aws-security-mcp)** - ⭐ 82
   A Model Context Protocol server that connects AI assistants like Claude to AWS security services, allowing them to autonomously query, inspect, and analyze AWS infrastructure for security issues and misconfigurations.

2550. **[mcp-agent](https://github.com/Haohao-end/mcp-agent)** - ⭐ 82
   A modular Python framework implementing the Model Context Protocol (MCP). It features a standardized client-server architecture over StdIO, integrating LLMs with external tools, real-time weather data fetching, and an advanced RAG (Retrieval-Augmented Generation) system.

2551. **[hulunote](https://github.com/hulunote/hulunote)** - ⭐ 82
   AI + Note Hippocampus — Your second brain, powered by AI

2552. **[metabase-mcp](https://github.com/jerichosequitin/metabase-mcp)** - ⭐ 82
   A high-performance Model Context Protocol server for AI integration with Metabase analytics platforms. Features response optimization, robust error handling, and comprehensive data access tools. Featured on Claude.

2553. **[markitdown_mcp_server](https://github.com/KorigamiK/markitdown_mcp_server)** - ⭐ 82
   A Model Context Protocol (MCP) server that converts various file formats to Markdown using the MarkItDown utility.

2554. **[mcp-rs-template](https://github.com/linux-china/mcp-rs-template)** - ⭐ 82
   Model Context Protocol (MCP) CLI server template for Rust

2555. **[agentic-stock-research-system](https://github.com/rooneyrulz/agentic-stock-research-system)** - ⭐ 82
   A sophisticated multi-agent AI system for analyzing Indian NSE-listed stocks using real-time data, technical indicators, news sentiment, and advanced AI reasoning.

2556. **[mcp-discovery](https://github.com/rust-mcp-stack/mcp-discovery)** - ⭐ 82
   A command-line tool written in Rust for discovering and documenting MCP Server capabilities.

2557. **[claude-mermaid](https://github.com/veelenga/claude-mermaid)** - ⭐ 82
   MCP Server to previewing mermaid diagrams with live reload

2558. **[BurpSuite-MCP-Server](https://github.com/X3r0K/BurpSuite-MCP-Server)** - ⭐ 82
   BurpSuite MCP Server:  A powerful Model Context Protocol (MCP) server implementation for BurpSuite, providing programmatic access to Burp's core functionalities.

2559. **[bridge4simulator](https://github.com/AppGram/bridge4simulator)** - ⭐ 81
   An MCP (Model Context Protocol) server that enables AI assistants to control iOS Simulator. Seamlessly integrates with Claude Desktop, Cursor, Claude Code, and other MCP-compatible clients.

2560. **[mcp-server](https://github.com/bitDive/mcp-server)** - ⭐ 81
   BitDive Model Context Protocol (MCP) server. The Autonomous Quality Loop for AI agents. Provides real runtime context, before/after trace comparison, and integration testing workflows.

2561. **[anki-mcp-server](https://github.com/CamdenClark/anki-mcp-server)** - ⭐ 81
   A model context protocol server that connects to Anki through AnkiConnect

2562. **[joplin-mcp-server](https://github.com/dweigend/joplin-mcp-server)** - ⭐ 81
   A Model Context Protocol (MCP) Server for https://joplinapp.org/ that enables note access through the https://modelcontextprotocol.io. Perfect for integration with AI assistants like Claude.

2563. **[ingero](https://github.com/ingero-io/ingero)** - ⭐ 81
   eBPF-based GPU causal observability agent

2564. **[node-candidate-mcp-server](https://github.com/jhgaylor/node-candidate-mcp-server)** - ⭐ 81
   A Model Context Protocol (MCP) server library that gives LLMs access to information about a candidate.

2565. **[code-to-tree](https://github.com/micl2e2/code-to-tree)** - ⭐ 81
   A runtime-free MCP server that converts source code into AST🌲, regardless of language.

2566. **[dreamgraph](https://github.com/mmethodz/dreamgraph)** - ⭐ 81
   DreamGraph is a graph-first cognitive layer (graph → MCP → CLI → dashboard → extension) that builds a persistent knowledge graph to reason, validate changes, and generate docs.

2567. **[mcp-openapi](https://github.com/ReAPI-com/mcp-openapi)** - ⭐ 81
   OpenAPI specification MCP server.

2568. **[sh-disney-mcp](https://github.com/syyuan14/sh-disney-mcp)** - ⭐ 81
   sh-disney-mcp 是一个基于 Model Context Protocol (MCP) 的mcp server，旨在通过标准化的接口，帮助大模型快速获取上海迪士尼乐园的门票价格和售卖状态信息

2569. **[sample-agents-with-nova-act-and-mcp](https://github.com/aws-samples/sample-agents-with-nova-act-and-mcp)** - ⭐ 80
   Discover how to build agents that can perform actions on websites by combining Amazon Nova Act with Model Context Protocol (MCP).

2570. **[mcp-server-any-openapi](https://github.com/baryhuang/mcp-server-any-openapi)** - ⭐ 80
   A MCP server that enables Claude to discover and call any API endpoint through semantic search. Intelligently chunks OpenAPI specifications to handle large API documentation, with built-in request execution capabilities. Perfect for integrating private APIs with Claude Desktop.

2571. **[codebase-mcp](https://github.com/DeDeveloper23/codebase-mcp)** - ⭐ 80
   Model Context Protocol implementation for retrieving codebases using RepoMix

2572. **[google-cloud-mcp](https://github.com/krzko/google-cloud-mcp)** - ⭐ 80
   🤖 A Model Context Protocol (MCP) server for Google Cloud (GCP)

2573. **[mcpc](https://github.com/mcpc-tech/mcpc)** - ⭐ 80
   Build agentic-MCP servers by composing existing MCP tools.

2574. **[MCPay](https://github.com/microchipgnu/MCPay)** - ⭐ 80
   Open-source Infrastructure for MCP and x402

2575. **[ophis](https://github.com/njayp/ophis)** - ⭐ 80
   Transform any Cobra CLI into an MCP server

2576. **[tauri-plugin-mcp](https://github.com/P3GLEG/tauri-plugin-mcp)** - ⭐ 80
   Allows AI agents (e.g., Cursor, Claude Code) to debug within Tauri apps via screenshot capture, window management, DOM access, and simulated user inputs.

2577. **[gtm-mcp-server](https://github.com/paolobietolini/gtm-mcp-server)** - ⭐ 80
   An MCP server for Google Tag Manager. Connect it to your LLM, authenticate once, and start managing GTM through natural language.

2578. **[Ludus-FastMCP](https://github.com/tjnull/Ludus-FastMCP)** - ⭐ 80
   A Model Context Protocol (MCP) server for automating Ludus v1 and v2 cyber range environments through AI assistants. 190+ tools for range management, blueprints, groups, templates, scenarios, and SIEM integration.

2579. **[mcp-client-capabilities](https://github.com/apify/mcp-client-capabilities)** - ⭐ 79
   Index of all Model Context Protocol (MCP) clients and their capabilities

2580. **[RivalSearchMCP](https://github.com/damionrashford/RivalSearchMCP)** - ⭐ 79
   Deterministic research MCP server on FastMCP 3 — 5-engine web search, 9-platform social search, 6 academic DBs, news aggregation, entity profiles, conflict detection, document analysis. No API keys. No in-server LLM. Structured outputs for agent chaining.

2581. **[glif-mcp-server](https://github.com/glifxyz/glif-mcp-server)** - ⭐ 79
   Easily run glif.app AI workflows inside your LLM: image generators, memes, selfies, and more. Glif supports all major multimedia AI models inside one app

2582. **[forgejo-mcp](https://github.com/goern/forgejo-mcp)** - ⭐ 79
   MIRROR ONLY!! This Model Context Protocol (MCP) server provides tools and resources for interacting with the Forgejo (specifically Codeberg.org) REST API.

2583. **[mcp-kafka](https://github.com/kanapuli/mcp-kafka)** - ⭐ 79
   A Model Context Protocol Server to perform Kafka client operations

2584. **[geoserver-mcp](https://github.com/mahdin75/geoserver-mcp)** - ⭐ 79
   A Model Context Protocol (MCP) server implementation that connects LLMs to the GeoServer REST API

2585. **[codemirror-mcp](https://github.com/marimo-team/codemirror-mcp)** - ⭐ 79
   CodeMirror extension to hook up a Model Context Provider (MCP)

2586. **[jira-mcp](https://github.com/nguyenvanduocit/jira-mcp)** - ⭐ 79
   A Go-based MCP (Model Control Protocol) connector for Jira that enables AI assistants like Claude to interact with Atlassian Jira. This tool provides a seamless interface for AI models to perform common Jira operations including issue management, sprint planning, and workflow transitions.

2587. **[fastmcp-boilerplate](https://github.com/punkpeye/fastmcp-boilerplate)** - ⭐ 79
   A simple MCP server built using FastMCP, TypeScript, ESLint, and Prettier.

2588. **[transit-agent](https://github.com/ruby-verma/transit-agent)** - ⭐ 79
   This guide demonstrates how to build an Agentic AI system using Google's Agent Development Kit (ADK) and the Model Context Protocol (MCP).

2589. **[terminal_server](https://github.com/theailanguage/terminal_server)** - ⭐ 79
   MCP server that can execute terminal commands

2590. **[django-ai-boost](https://github.com/vintasoftware/django-ai-boost)** - ⭐ 79
   A MCP server for Django applications, inspired by Laravel Boost.

2591. **[mcp-azure-devops](https://github.com/Vortiago/mcp-azure-devops)** - ⭐ 79
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Azure DevOps services via Python SDK.

2592. **[dramacraft](https://github.com/whatyun/dramacraft)** - ⭐ 79
   DramaCraft 是一个专业的短剧视频编辑 MCP (Model Context Protocol) 服务，集成国产中文大模型 API，实现剪映的智能自动化编辑功能。项目已完成从视频分析到草稿生成的完整解决方案

2593. **[cesium-ai-integrations](https://github.com/CesiumGS/cesium-ai-integrations)** - ⭐ 78
   Cesium AI Integrations is a collection of reference integrations and experiments connecting the Cesium ecosystem with AI systems including Model Context Protocol (MCP) tools, retrieval pipelines, and agent skills.

2594. **[vikunja-mcp](https://github.com/democratize-technology/vikunja-mcp)** - ⭐ 78
   Model Context Protocol server for Vikunja task management. Enables AI assistants to interact with Vikunja instances via MCP.

2595. **[caldav-mcp](https://github.com/dominik1001/caldav-mcp)** - ⭐ 78
   🗓️ A CalDAV Model Context Protocol (MCP) server to expose calendar operations as tools for AI assistants.

2596. **[MySQL_MCP](https://github.com/guangxiangdebizi/MySQL_MCP)** - ⭐ 78
   这是一个功能强大且易用的MySQL数据库MCP（Model Context Protocol）服务器，让你的AI助手可以安全地进行完整的数据库操作，支持多数据库连接管理、增删改查、事务管理和智能回滚功能。

2597. **[imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server)** - ⭐ 78
   An MCP server that provides safe access to your iMessage database through Model Context Protocol (MCP). This server is built with the FastMCP framework and the imessagedb library, enabling LLMs to query and analyze iMessage conversations with proper phone number validation and attachment handling.

2598. **[bc-code-intelligence-mcp](https://github.com/JeremyVyska/bc-code-intelligence-mcp)** - ⭐ 78
   BC Code Intelligence MCP Server - Persona-driven workflow orchestration for Business Central development. Provides 16+ MCP tools, layered knowledge system, and intelligent BC pattern analysis through Model Context Protocol.

2599. **[bing-search-mcp](https://github.com/leehanchung/bing-search-mcp)** - ⭐ 78
   MCP Server for Bing Search API

2600. **[awesome-mcp-best-practices](https://github.com/lirantal/awesome-mcp-best-practices)** - ⭐ 78
   Build Awesome MCPs with Awesome Best Practices for MCP Servers and MCP Clients

2601. **[optuna-mcp](https://github.com/optuna/optuna-mcp)** - ⭐ 78
   The Optuna MCP Server is a Model Context Protocol (MCP) server to interact with Optuna APIs.

2602. **[DecompilerServer](https://github.com/pardeike/DecompilerServer)** - ⭐ 78
   A powerful MCP (Model Context Protocol) server for decompiling and analyzing .NET assemblies, with specialized support for Unity's Assembly-CSharp.dll files. DecompilerServer provides comprehensive decompilation, search, and code analysis capabilities through a rich set of tools and APIs.

2603. **[mcp-server-email](https://github.com/Shy2593666979/mcp-server-email)** - ⭐ 78
   一个基于 MCP (Model Context Protocol) 的邮件服务，支持 LLM 发送带附件的电子邮件及在指定目录中搜索文件。提供安全的 SMTP 传输、多收件人支持和附件模式匹配搜索功能，适用于 Gmail、Outlook、Yahoo、QQ 邮箱和网易 126 邮箱等主流邮箱服务。

2604. **[choturobo](https://github.com/vishalmysore/choturobo)** - ⭐ 78
   Integrate Arduino-based robotics (using the NodeMCU ESP32 or Arduino Nano 368 board) with AI using the MCP (Model Context Protocol) framework from Claude Anthropic

2605. **[wasmcp](https://github.com/wasmcp/wasmcp)** - ⭐ 78
   Build MCP servers with WebAssembly components

2606. **[mcp-fal](https://github.com/am0y/mcp-fal)** - ⭐ 77
   A Model Context Protocol (MCP) server for interacting with fal.ai models and services.

2607. **[tester-mcp-client](https://github.com/apify/tester-mcp-client)** - ⭐ 77
   Model Context Protocol (MCP) Client for Apify's Actors

2608. **[lucidity-mcp](https://github.com/hyperb1iss/lucidity-mcp)** - ⭐ 77
   AI-powered code quality analysis using MCP to help AI assistants review code more effectively. Analyze git changes for complexity, security issues, and more through structured prompts.

2609. **[mcp-reticle](https://github.com/LabTerminal/mcp-reticle)** - ⭐ 77
   Reticle intercepts, visualizes, and profiles JSON-RPC traffic between your LLM and MCP servers in real-time, with zero latency overhead. Stop debugging blind. Start seeing everything.

2610. **[unitree-go2-mcp-server](https://github.com/lpigeon/unitree-go2-mcp-server)** - ⭐ 77
   The Unitree Go2 MCP Server is a server built on the MCP that enables users to control the Unitree Go2 robot using natural language commands interpreted by a LLM.

2611. **[rtfmbro-mcp](https://github.com/marckrenn/rtfmbro-mcp)** - ⭐ 77
   rtfmbro provides always-up-to-date, version-specific package documentation as context for coding agents. An alternative to context7

2612. **[ExternalAttacker-MCP](https://github.com/MorDavid/ExternalAttacker-MCP)** - ⭐ 77
   A modular external attack surface mapping tool integrating tools for automated reconnaissance and bug bounty workflows.

2613. **[devex](https://github.com/ParthKapoor-dev/devex)** - ⭐ 77
   ⚡️ Devex — A Fast, Secure, and Scalable Repl-as-a-Service Platform built for Developers 🚀

2614. **[Sephera](https://github.com/Reim-developer/Sephera)** - ⭐ 77
   Fast local-first Rust CLI for codebase metrics, AST-compressed LLM context bundles, and built-in MCP server.

2615. **[visual-ui-debug-agent-mcp](https://github.com/samihalawa/visual-ui-debug-agent-mcp)** - ⭐ 77
   VUDA is an autonomous debugging agent that empowers AI models to visually analyze, test, and debug web

2616. **[mcp-llm](https://github.com/sammcj/mcp-llm)** - ⭐ 77
    An MCP server that provides LLMs access to other LLMs

2617. **[agent-security-scanner-mcp](https://github.com/sinewaveai/agent-security-scanner-mcp)** - ⭐ 77
   Security scanner MCP server for AI coding agents. Prompt injection firewall, package hallucination detection (4.3M+ packages), 1000+ vulnerability rules with AST & taint analysis, auto-fix.

2618. **[1c-mcp](https://github.com/Untru/1c-mcp)** - ⭐ 77
   Curated list of MCP servers for 1C:Enterprise ecosystem | Каталог MCP-серверов для экосистемы 1С:Предприятие

2619. **[tiny-mcp](https://github.com/wdndev/tiny-mcp)** - ⭐ 77
   Python 实现 MCP client / service

2620. **[mcp-open-library](https://github.com/8enSmith/mcp-open-library)** - ⭐ 76
   A Model Context Protocol (MCP) server for the Internet Archive's Open Library API that enables AI assistants to search for book and author information.

2621. **[cursor10x-mcp](https://github.com/aiurda/cursor10x-mcp)** - ⭐ 76
   The Cursor10x MCP is a persistent multi-dimensional memory system for Cursor that enhances AI assistants with conversation context, project history, and code relationships across sessions.

2622. **[lunchmoney-mcp](https://github.com/akutishevsky/lunchmoney-mcp)** - ⭐ 76
   A Model Context Protocol (MCP) server implementation for LunchMoney, providing programmatic access to personal finance management through LunchMoney's API.

2623. **[codeglide-mcpgen](https://github.com/CodeGlide/codeglide-mcpgen)** - ⭐ 76
   Generation of Secure MCP (Model Context Protocol) Servers from API source code at Scale

2624. **[aguara](https://github.com/garagon/aguara)** - ⭐ 76
   Security scanner for AI agent skills and MCP servers. Static analysis, incident response, no LLM. One binary.   Detection engine behind oktsec.

2625. **[Unity-AI-Animation](https://github.com/IvanMurzak/Unity-AI-Animation)** - ⭐ 76
   AI-powered tools for Unity animation workflow. Create and modify AnimationClips and AnimatorControllers directly through natural language commands.

2626. **[apitap](https://github.com/n1byn1kt/apitap)** - ⭐ 76
   The MCP server that turns any website into an API — no docs, no SDK, no browser. npm: @apitap/core

2627. **[masquerade](https://github.com/postralai/masquerade)** - ⭐ 76
   The Privacy Firewall for LLMs

2628. **[sublinear-time-solver](https://github.com/ruvnet/sublinear-time-solver)** - ⭐ 76
   Rust + WASM sublinear-time solver for asymmetric diagonally dominant systems. Exposes Neumann series, push, and hybrid random-walk algorithms with npm/npx CLI and Flow-Nexus HTTP streaming for swarm cost propagation and verification.

2629. **[xiaozhi-mcp-client](https://github.com/shadowcz007/xiaozhi-mcp-client)** - ⭐ 76
   可视化的配置和管理，给xiaozhi接入mcp

2630. **[mcp-shell](https://github.com/sonirico/mcp-shell)** - ⭐ 76
   Give hands to AI. MCP server to run shell commands securely, auditably, and on demand.

2631. **[lazy-mcp](https://github.com/voicetreelab/lazy-mcp)** - ⭐ 76
     MCP proxy server with lazy loading support - reduces context usage through on-demand tool activation

2632. **[claude-code-source-all-in-one](https://github.com/wuwangzhang1216/claude-code-source-all-in-one)** - ⭐ 76
   Always up-to-date open-source mirror of Claude Code (currently v2.1.123). Run from source with Claude subscription/API, ChatGPT subscription (GPT-5.5 / GPT-5.4), OpenAI-compatible providers, or local Ollama. 18 deep-dive architecture articles included. For educational and reference purposes only.

2633. **[perplexity-mcp-zerver](https://github.com/wysh3/perplexity-mcp-zerver)** - ⭐ 76
   MCP web search using perplexity without any API KEYS

2634. **[mcp-gemini-google-search](https://github.com/yukukotani/mcp-gemini-google-search)** - ⭐ 76
   MCP server for Google Search integration using Gemini's built-in search capabilities

2635. **[anilist-mcp](https://github.com/yuna0x0/anilist-mcp)** - ⭐ 76
   AniList MCP server for accessing anime and manga data

2636. **[roundtable](https://github.com/askbudi/roundtable)** - ⭐ 75
   Zero-configuration MCP server that unifies multiple AI coding assistants (Codex, Claude Code, Cursor, Gemini) through intelligent auto-discovery and standardized interface

2637. **[openzim-mcp](https://github.com/cameronrye/openzim-mcp)** - ⭐ 75
   OpenZIM MCP is a modern, secure, and high-performance MCP (Model Context Protocol) server that enables AI models to access and search ZIM format knowledge bases offline.

2638. **[interactive-brokers-mcp](https://github.com/code-rabi/interactive-brokers-mcp)** - ⭐ 75
   Interactive Brokers MCP Server

2639. **[home-memory](https://github.com/impactjo/home-memory)** - ⭐ 75
   MCP server that lets your AI assistant remember everything about your home.

2640. **[mcp-manager](https://github.com/MediaPublishing/mcp-manager)** - ⭐ 75
   A web-based GUI tool for managing Model Context Protocol (MCP) servers in Claude and Cursor

2641. **[zeromcp](https://github.com/mrexodia/zeromcp)** - ⭐ 75
   Zero-dependency MCP server implementation.

2642. **[CanvasMCPClient](https://github.com/n00bvn/CanvasMCPClient)** - ⭐ 75
   Canvas MCP Client is an open-source, self-hostable dashboard application built around an infinite, zoomable, and pannable canvas. It provides a unified interface for interacting with multiple MCP (Model Context Protocol) servers through a flexible, widget-based system.

2643. **[roblox-executor-mcp](https://github.com/notpoiu/roblox-executor-mcp)** - ⭐ 75
   A MCP Server which allows for direct access to the roblox game client

2644. **[sugar](https://github.com/roboticforce/sugar)** - ⭐ 75
   Persistent memory for AI coding agents. Cross-session context, global knowledge, and autonomous task execution.

2645. **[agentic-coding](https://github.com/sammcj/agentic-coding)** - ⭐ 75
   Agentic Coding Rules, Templates etc...

2646. **[drawio-mcp-server](https://github.com/simonkurtz-MSFT/drawio-mcp-server)** - ⭐ 75
   A Model Context Protocol (MCP) server for programmatic diagram generation using Draw.io (Diagrams.net). This server generates Draw.io XML directly — no browser extension or Draw.io instance required.

2647. **[mcp-llms-txt-explorer](https://github.com/thedaviddias/mcp-llms-txt-explorer)** - ⭐ 75
   MCP to explore websites with llms.txt files

2648. **[openfoam-mcp-server](https://github.com/webworn/openfoam-mcp-server)** - ⭐ 75
   LLM-powered OpenFOAM MCP server for intelligent CFD education with Socratic questioning and expert error resolution

2649. **[gdai-mcp-plugin-godot](https://github.com/3ddelano/gdai-mcp-plugin-godot)** - ⭐ 74
   A MCP server integration for Godot Engine that allows Claude, Cursor, Windsurf, VSCode, etc to perform actions like creating scenes, resources, scripts, reading errors and much more.

2650. **[mcp-server-datahub](https://github.com/acryldata/mcp-server-datahub)** - ⭐ 74
   The official Model Context Protocol (MCP) server for DataHub (https://datahub.com)

2651. **[mcp-ssh](https://github.com/AiondaDotCom/mcp-ssh)** - ⭐ 74
   A Model Context Protocol (MCP) server for managing and controlling SSH connections.

2652. **[ClueoMCP](https://github.com/ClueoFoundation/ClueoMCP)** - ⭐ 74
   🎭 The Personality Layer for LLMs- Transform any MCP-compatible AI with rich, consistent personalities powered by Clueo's Big Five personality engine.

2653. **[airtable-mcp](https://github.com/felores/airtable-mcp)** - ⭐ 74
   Search, create and update Airtable bases, tables, fields, and records using Claude Desktop and MCP (Model Context Protocol) clients

2654. **[svgmaker-mcp](https://github.com/GenWaveLLC/svgmaker-mcp)** - ⭐ 74
   Model Context Protocol server for SVGMaker - AI-powered SVG generation and editing. Seamlessly integrate SVG creation into AI workflows.

2655. **[ipybox](https://github.com/gradion-ai/ipybox)** - ⭐ 74
   Unified execution environment for Python code, shell commands, and programmatic MCP tool calls.

2656. **[raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server)** - ⭐ 74
   An integration that allows LLMs to interact with Raindrop.io bookmarks using the Model Context Protocol (MCP).

2657. **[conductor-tasks](https://github.com/hridaya423/conductor-tasks)** - ⭐ 74
   A task management system designed for AI development

2658. **[gmail-mcp-server](https://github.com/jasonsum/gmail-mcp-server)** - ⭐ 74
   Model Context Protocol (MCP) server for Gmail

2659. **[podman-mcp-server](https://github.com/manusa/podman-mcp-server)** - ⭐ 74
   Model Context Protocol (MCP) server for container runtimes (Podman and Docker)

2660. **[Skills-ContextManager](https://github.com/One-Man-Company/Skills-ContextManager)** - ⭐ 74
   A self-hosted web application for managing AI skills, workflows, and contexts with full MCP (Model Context Protocol) integration. Organize, manage, and dynamically load specialized knowledge bases into any AI Agent just by toggling your Skills On/Off in simple local hosted WEB UI.

2661. **[chess-mcp](https://github.com/pab1it0/chess-mcp)** - ⭐ 74
   A Model Context Protocol server for Chess.com's Published Data API.  This provides access to Chess.com player data, game records, and other public information through standardized MCP interfaces, allowing AI assistants to search and analyze chess information.

2662. **[rust-mcp-schema](https://github.com/rust-mcp-stack/rust-mcp-schema)** - ⭐ 74
   A type-safe implementation of the official Model Context Protocol (MCP) schema in Rust.

2663. **[UnrealMotionGraphicsMCP](https://github.com/winyunq/UnrealMotionGraphicsMCP)** - ⭐ 74
   🚀 UE5-UMG-MCP: A deep-focused MCP for Unreal Engine UMG layout. Designed to maximize AI efficiency within limited context windows by prioritizing precision in UI structure, animations, and blueprint integration.

2664. **[mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye)** - ⭐ 74
   A Model Context Protocol server that provides network asset information based on query conditions. This server allows LLMs to obtain network asset information and supports querying network asset information by zoomeye dork etc.

2665. **[bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp)** - ⭐ 73
   Bitcoin & Lightning Network MCP Server.

2666. **[unreal-api-mcp](https://github.com/Codeturion/unreal-api-mcp)** - ⭐ 73
   Instant, accurate Unreal Engine API lookups instead of expensive source file reads, saving your agent tokens, context, and hallucinations.

2667. **[pitlane-mcp](https://github.com/eresende/pitlane-mcp)** - ⭐ 73
   Token-efficient navigation substrate for AI coding agents. Index code once and retrieve only the symbols you need.

2668. **[firefox-devtools-mcp](https://github.com/globau/firefox-devtools-mcp)** - ⭐ 73
   Model Context Protocol server for Firefox DevTools - enables AI assistants to inspect and control Firefox browser through the Remote Debugging Protocol

2669. **[mcp-toolbox-sdk-js](https://github.com/googleapis/mcp-toolbox-sdk-js)** - ⭐ 73
   Javascript SDK for interacting with the MCP Toolbox for Databases.

2670. **[pentestMCP](https://github.com/RamKansal/pentestMCP)** - ⭐ 73
   pentestMCP: AI-Powered Penetration Testing via MCP, an MCP designed for penetration testers.

2671. **[sanity-mcp-server](https://github.com/sanity-io/sanity-mcp-server)** - ⭐ 73
   Deprecated: Use the remote MCP server at https://mcp.sanity.io instead.

2672. **[Custom-MCP-Server](https://github.com/Sharan-Kumar-R/Custom-MCP-Server)** - ⭐ 73
   MCP server for scraping LinkedIn, Facebook, Instagram profiles and Google search.

2673. **[PowerShell.MCP](https://github.com/yotsuda/PowerShell.MCP)** - ⭐ 73
   The universal MCP server for Claude Code and other MCP-compatible clients. One installation gives AI access to 10,000+ PowerShell modules and any CLI tool. You and AI collaborate in the same console with full transparency. Supports Windows, Linux, and macOS.

2674. **[mcp](https://github.com/abap-ai/mcp)** - ⭐ 72
   ABAP MCP - Model Context Protocol - Server SDK

2675. **[joplin-mcp](https://github.com/alondmnt/joplin-mcp)** - ⭐ 72
   MCP server for the Joplin note taking app

2676. **[mcp-openmemory](https://github.com/baryhuang/mcp-openmemory)** - ⭐ 72
   Simple standalone MCP server giving Claude the ability to remember your conversations and learn from them over time.

2677. **[firefox-devtools-mcp](https://github.com/freema/firefox-devtools-mcp)** - ⭐ 72
   Model Context Protocol server for Firefox DevTools - enables AI assistants to inspect and control Firefox browser through the Remote Debugging Protocol

2678. **[railway-mcp](https://github.com/jason-tan-swe/railway-mcp)** - ⭐ 72
   An unofficial and community-built MCP server for integrating with https://railway.app

2679. **[gdal-mcp](https://github.com/JordanGunn/gdal-mcp)** - ⭐ 72
   Model Context Protocol server that packages GDAL-style geospatial workflows through Python-native libraries (Rasterio, GeoPandas, PyProj, etc.) to give AI agents catalog discovery, metadata intelligence, and raster/vector processing with built-in reasoning guidance and reference resources.

2680. **[mcp-openapi-schema-explorer](https://github.com/kadykov/mcp-openapi-schema-explorer)** - ⭐ 72
   MCP server providing token-efficient access to OpenAPI/Swagger specs via MCP Resource Templates for client-side exploration.

2681. **[modao-proto-mcp](https://github.com/modao-dev/modao-proto-mcp)** - ⭐ 72
   Modao Proto MCP is a standalone MCP (Model Context Protocol) service designed to connect Modao Proto design tools with AI models.

2682. **[OmniMCP](https://github.com/OpenAdaptAI/OmniMCP)** - ⭐ 72
   OmniMCP uses Microsoft OmniParser and Model Context Protocol (MCP) to provide AI models with rich UI context and powerful interaction capabilities.

2683. **[m3](https://github.com/rafiattrach/m3)** - ⭐ 72
   🏥🤖 Query MIMIC-IV medical data using natural language through Model Context Protocol (MCP). Transform healthcare research with AI-powered database interactions - supports both local MIMIC-IV SQLite demo dataset and full BigQuery datasets.

2684. **[github-brain](https://github.com/wham/github-brain)** - ⭐ 72
   An experimental GitHub MCP server with local database.

2685. **[adb-tui](https://github.com/alanisme/adb-tui)** - ⭐ 71
   🤖 Full-featured Android Debug Bridge TUI and MCP server. Control any device by keystroke or AI.

2686. **[ytt-mcp](https://github.com/cottongeeks/ytt-mcp)** - ⭐ 71
   MCP server to fetch YouTube transcripts

2687. **[freepik-mcp](https://github.com/freepik-company/freepik-mcp)** - ⭐ 71
   The Freepik enables popular agent Model Context Protocol (MCP) to integrate with Freepik APIs through function calling.

2688. **[semanticscholar-MCP-Server](https://github.com/JackKuo666/semanticscholar-MCP-Server)** - ⭐ 71
   🔍 This project implements a Model Context Protocol (MCP) server for interacting with the Semantic Scholar API. It provides tools for searching papers, retrieving paper and author details, and fetching citations and references.

2689. **[medical-mcp](https://github.com/JamesANZ/medical-mcp)** - ⭐ 71
   An MCP server that provides comprehensive medical information by querying multiple authoritative medical APIs including FDA, WHO, PubMed, Google Scholar, and RxNorm

2690. **[template-mcp-server](https://github.com/mcpdotdirect/template-mcp-server)** - ⭐ 71
   Template to quickly set up your own MCP server

2691. **[ollama-mcp-client](https://github.com/mihirrd/ollama-mcp-client)** - ⭐ 71
   MCP client for local ollama models

2692. **[trading-mcp](https://github.com/netanelavr/trading-mcp)** - ⭐ 71
   The MCP server that will help you trade smarter (or at least try)

2693. **[pagerduty-mcp-server](https://github.com/PagerDuty/pagerduty-mcp-server)** - ⭐ 71
   PagerDuty's official local MCP (Model Context Protocol) server which provides tools to interact with your PagerDuty account directly from your MCP-enabled client.

2694. **[bookstack-mcp-server](https://github.com/pnocera/bookstack-mcp-server)** - ⭐ 71
   A Model Context Protocol (MCP) server providing full access to BookStack's knowledge management capabilities

2695. **[mcp-servers](https://github.com/pulsemcp/mcp-servers)** - ⭐ 71
   MCP (Model Context Protocol) Servers authored and maintained by the PulseMCP team. We build reliable servers thoughtfully designed specifically for MCP Client-powered workflows.

2696. **[MCP-wolfram-alpha](https://github.com/SecretiveShell/MCP-wolfram-alpha)** - ⭐ 71
   Connect your chat repl to wolfram alpha computational intelligence

2697. **[sub-agents-mcp](https://github.com/shinpr/sub-agents-mcp)** - ⭐ 71
   Define task-specific AI sub-agents in Markdown for any MCP-compatible tool.

2698. **[JazzCashMCP](https://github.com/TehreemArbab/JazzCashMCP)** - ⭐ 71
   Open-source Model Context Protocol (MCP) server for JazzCash — Pakistan's largest mobile-money platform. Hosted Checkout, Mobile Wallet charges, inquiries, and refunds for AI agents.

2699. **[mcp-server-kibana](https://github.com/TocharianOU/mcp-server-kibana)** - ⭐ 71
   MCP server for Kibana, Access search and manage Kibana in MCP Client.

2700. **[rust-analyzer-mcp](https://github.com/zeenix/rust-analyzer-mcp)** - ⭐ 71
   A Model Context Protocol (MCP) server that provides integration with rust-analyzer

2701. **[boilerplate-mcp-server](https://github.com/aashari/boilerplate-mcp-server)** - ⭐ 70
   TypeScript Model Context Protocol (MCP) server boilerplate providing IP lookup tools/resources. Includes CLI support and extensible structure for connecting AI systems (LLMs) to external data sources like ip-api.com. Ideal template for creating new MCP integrations via Node.js.

2702. **[piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server)** - ⭐ 70
   A TypeScript implementation of a Model Context Protocol (MCP) server that integrates with PiAPI's API. PiAPI makes user able to generate media content with Midjourney/Flux/Kling/LumaLabs/Udio/Chrip/Trellis directly from Claude or any other MCP-compatible apps.

2703. **[davinci-resolve-mcp](https://github.com/apvlv/davinci-resolve-mcp)** - ⭐ 70
   A Model Context Protocol (MCP) server for interacting with DaVinci Resolve and Fusion

2704. **[agent-architecture-review-sample](https://github.com/Azure-Samples/agent-architecture-review-sample)** - ⭐ 70
   The Architecture Review Agent is an open-source AI agent sample that reviews software architectures and generates interactive diagrams automatically.

2705. **[mcp-discord](https://github.com/barryyip0625/mcp-discord)** - ⭐ 70
   Implement Discord MCP server enabling AI assistants to interact with the Discord platform.

2706. **[clinicaltrialsgov-mcp-server](https://github.com/cyanheads/clinicaltrialsgov-mcp-server)** - ⭐ 70
   MCP server for the ClinicalTrials.gov v2 API. Search trials, retrieve study details and results, and match patients to eligible trials.

2707. **[voice-mcp-agent](https://github.com/den-vasyliev/voice-mcp-agent)** - ⭐ 70
   A voice assistant application built with the LiveKit Agents framework, capable of using Model Context Protocol (MCP) tools to interact with external services

2708. **[baml-agents](https://github.com/Elijas/baml-agents)** - ⭐ 70
   Building Agents with LLM structured generation (BAML), MCP Tools, and 12-Factor Agents principles

2709. **[MCP-server-Deepseek_R1](https://github.com/kamelirzouni/MCP-server-Deepseek_R1)** - ⭐ 70
   A Model Context Protocol (MCP) server implementation connecting Claude Desktop with DeepSeek's language models (R1/V3)

2710. **[mcd-mcp-server](https://github.com/M-China/mcd-mcp-server)** - ⭐ 70
   McDonald's China MCP Server Integration Guide

2711. **[youtube-connector-mcp](https://github.com/ShellyDeng08/youtube-connector-mcp)** - ⭐ 70
   MCP server for YouTube — search videos, channels, playlists, and transcripts. Works with Claude, Cursor, Windsurf, and any MCP client.

2712. **[CodeMCP](https://github.com/SimplyLiz/CodeMCP)** - ⭐ 70
   Code intelligence for AI assistants - MCP server, CLI, and HTTP API with symbol navigation, impact analysis, and architecture mapping

2713. **[mcp_newsnow](https://github.com/sligter/mcp_newsnow)** - ⭐ 70
   一个基于 Model Context Protocol (MCP) 的新闻聚合服务器，通过 Newsnow API 提供多平台热点新闻和趋势话题。

2714. **[ros2_mcp](https://github.com/wise-vision/ros2_mcp)** - ⭐ 70
   Advanced MCP Server ROS 2 bridging AI agents straight into robotics

2715. **[ableton-copilot-mcp](https://github.com/xiaolaa2/ableton-copilot-mcp)** - ⭐ 70
   An MCP server built on ableton-js enables AI assistants to control Ableton Live in real time, including Arrangement View operations such as song management, track control, MIDI editing, and audio recording, along with other capabilities.

2716. **[lc2mcp](https://github.com/xiaotonng/lc2mcp)** - ⭐ 70
   Convert LangChain tools to FastMCP tools

2717. **[MCP-server-Deepseek_R1](https://github.com/66julienmartin/MCP-server-Deepseek_R1)** - ⭐ 69
   A Model Context Protocol (MCP) server implementation connecting Claude Desktop with DeepSeek's language models (R1/V3)

2718. **[mcp-server-atlassian-jira](https://github.com/aashari/mcp-server-atlassian-jira)** - ⭐ 69
   Node.js/TypeScript MCP server for Atlassian Jira. Equips AI systems (LLMs) with tools to list/get projects, search/get issues (using JQL/ID), and view dev info (commits, PRs). Connects AI capabilities directly into Jira project management and issue tracking workflows.

2719. **[mcp-client-python](https://github.com/alejandro-ao/mcp-client-python)** - ⭐ 69

2720. **[ticktick-mcp-server](https://github.com/alexarevalo9/ticktick-mcp-server)** - ⭐ 69
   A Model Context Protocol (MCP) server designed to integrate with the TickTick task management platform, enabling intelligent context-aware task operations and automation.

2721. **[totem](https://github.com/briangaoo/totem)** - ⭐ 69
   Model Context Protocol server giving Claude (or any MCP client) full read + write access to your Whoop fitness data via the private reverse-engineered iOS API. 47 tools: recovery, sleep, strain, HRV trends, Strength Trainer, journal, Whoop Coach, and smart alarm. TypeScript + zod, auto-refresh Cognito auth.

2722. **[robot_MCP](https://github.com/IliaLarchenko/robot_MCP)** - ⭐ 69
   A simple MCP server for the SO-ARM100 control

2723. **[crash-mcp](https://github.com/nikkoxgonzales/crash-mcp)** - ⭐ 69
   MCP server for structured and efficient reasoning with step validation, branching, and revisions.

2724. **[agenti](https://github.com/nirholas/agenti)** - ⭐ 69
   Give any AI agent a crypto wallet. Agents deserve access to money.  Pay x402 APIs, receive USDC, check balances — autonomously. Works with Claude, LangChain, AutoGen, CrewAI, and any MCP client. EVM + Solana.

2725. **[mxcp](https://github.com/raw-labs/mxcp)** - ⭐ 69
   Model eXecution + Context Protocol: Enterprise-Grade Data-to-AI Infrastructure

2726. **[deepseek-thinker-mcp](https://github.com/ruixingshi/deepseek-thinker-mcp)** - ⭐ 69
   A MCP provider Deepseek reasoning content to MCP-enabled AI Clients, like Claude Desktop. Supports access to Deepseek's CoT from the Deepseek API service or a local Ollama server.

2727. **[agenite](https://github.com/subeshb1/agenite)** - ⭐ 69
   🤖 Build powerful AI agents with TypeScript. Agenite makes it easy to create, compose, and control AI agents with first-class support for tools, streaming, and multi-agent architectures. Switch seamlessly between providers like OpenAI, Anthropic, AWS Bedrock, and Ollama.

2728. **[totem](https://github.com/thebriangao/totem)** - ⭐ 69
   Model Context Protocol server giving Claude (or any MCP client) full read + write access to your Whoop fitness data via the private reverse-engineered iOS API. 47 tools: recovery, sleep, strain, HRV trends, Strength Trainer, journal, Whoop Coach, and smart alarm. TypeScript + zod, auto-refresh Cognito auth.

2729. **[activitywatch-mcp-server](https://github.com/8bitgentleman/activitywatch-mcp-server)** - ⭐ 68
   Model Context Protocol server for ActivityWatch time tracking data

2730. **[nothumanallowed](https://github.com/adoslabsproject-gif/nothumanallowed)** - ⭐ 68
   Epistemic dataset generation engine. 38 AI agents deliberate through multi-round Geth Consensus — producing auditable reasoning traces for AI training. Parliament System, Knowledge Grounding, zero-trust security.

2731. **[mcp-things3](https://github.com/drjforrest/mcp-things3)** - ⭐ 68
   A Model Context Protocol for reading todos and writing todos and projects in the macOS app Things3 using a combination of Applescript and x-call URLs.

2732. **[QuickMCP](https://github.com/gunpal5/QuickMCP)** - ⭐ 68
   Effortlessly Build Model Context Protocol Servers with OpenAPI or Swagger or Google Discovery Specifications

2733. **[hyperterse](https://github.com/hyperterse/hyperterse)** - ⭐ 68
   The MCP framework. Connect your data to your agents.

2734. **[pydantic-rpc](https://github.com/i2y/pydantic-rpc)** - ⭐ 68
   PydanticRPC is a Python library for rapidly exposing Pydantic models as gRPC, ConnectRPC, and MCP services without protobuf files.

2735. **[attio-mcp-server](https://github.com/kesslerio/attio-mcp-server)** - ⭐ 68
   Attio Model Context Protocol (MCP) server implementation

2736. **[mcp-server-node](https://github.com/lucianoayres/mcp-server-node)** - ⭐ 68
   MCP Server implemented in JavaScript using Node.js that demonstrates how to build an MCP server with a custom prompt and custom tools, including one that loads an environment variable from a configuration file, to integrate seamlessly with AI-assisted environments like Cursor IDE.

2737. **[vibe-blocks-mcp](https://github.com/majidmanzarpour/vibe-blocks-mcp)** - ⭐ 68
   Connects Roblox Studio to AI coding editors via the Model Context Protocol (MCP), enabling AI-assisted game development within your Roblox Studio environment.

2738. **[mcp-server-okppt](https://github.com/NeekChaw/mcp-server-okppt)** - ⭐ 68
   这个项目是一个基于MCP (Model Context Protocol) 的服务器工具，名为 "MCP OKPPT Server"。它的核心功能是允许大型语言模型（如Claude、GPT等）通过生成SVG图像来间接设计和创建PowerPoint演示文稿。工具负责将这些SVG图像高质量地插入到PPTX幻灯片中，并保留其矢量特性，确保图像在PowerPoint中可缩放且清晰。

2739. **[vesta-mac-dist](https://github.com/scouzi1966/vesta-mac-dist)** - ⭐ 68
   Vesta macOS Distribution - Official releases and downloads.Vesta AI Chat Assistant for macOS - Built with SwiftUI, Swift MLX  and Apple Intelligence using Apple's on device model on MacOs Tahoe (MacOS 26). Now with side-by-side Qwen3-VL for vison

2740. **[deep-research-mcp-server](https://github.com/ssdeanx/deep-research-mcp-server)** - ⭐ 68
   MCP Deep Research Server using Gemini creating a Research AI Agent

2741. **[mcp](https://github.com/twelvedata/mcp)** - ⭐ 68
   Twelve Data MCP (Model Context Protocol) Server provides seamless, real-time access to financial market data via WebSocket, enabling reliable streaming of price quotes, market metrics, and events directly into your applications.

2742. **[mcp-all-in-one](https://github.com/vtxf/mcp-all-in-one)** - ⭐ 68
   A powerful MCP (Model Context Protocol) service aggregator that combines multiple MCP services into a single unified MCP service with self-configuration capabilities.

2743. **[reaper-reapy-mcp](https://github.com/wegitor/reaper-reapy-mcp)** - ⭐ 68
   Reaper and MCP or AI integration A Python application for controlling REAPER Digital Audio Workstation (DAW) using the MCP(Model context protocol).

2744. **[mcp-swagger-server](https://github.com/zaizaizhao/mcp-swagger-server)** - ⭐ 68
   MCP Swagger Server 将任何符合 OpenAPI/Swagger 规范的 REST API 转换为 Model Context Protocol (MCP) 格式，让 AI 助手能够理解和调用您的 API。

2745. **[nav2_mcp_server](https://github.com/ajtudela/nav2_mcp_server)** - ⭐ 67
   MCP server that provides tools and resources to control and monitor robots using Nav2.

2746. **[adeu](https://github.com/dealfluence/adeu)** - ⭐ 67
   Agentic DOCX Redlining Engine. Enables LLMs to read Word documents and inject native Track Changes (w:ins, w:del) and Comments without breaking formatting. Includes Model Context Protocol (MCP) Server.

2747. **[linkedin-mcpserver](https://github.com/felipfr/linkedin-mcpserver)** - ⭐ 67
   A powerful Model Context Protocol server for LinkedIn API integration

2748. **[mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor)** - ⭐ 67
   MCP (Model Context Protocol) server that enables AI assistants to interact with Storybook design systems. Extract component HTML, analyze styles, and help with design system adoption and refactoring.

2749. **[mcp](https://github.com/getAlby/mcp)** - ⭐ 67
   Connect a bitcoin lightning wallet to your LLM using Nostr Wallet Connect and Model Context Protocol

2750. **[stackoverflow-mcp](https://github.com/gscalzo/stackoverflow-mcp)** - ⭐ 67
   A Model Context Protocol server for querying Stack Overflow to help AI models find programming solutions

2751. **[nautex](https://github.com/hmldns/nautex)** - ⭐ 67
   MCP server for guiding Coding Agents via end-to-end requirements to implementation plan pipeline

2752. **[mcp-bear](https://github.com/jkawamoto/mcp-bear)** - ⭐ 67
   A MCP server for interacting with Bear note-taking software.

2753. **[MCPhoenix](https://github.com/jmanhype/MCPhoenix)** - ⭐ 67
   A simplified implementation of the Model Context Protocol (MCP) server using Elixir's Phoenix Framework.

2754. **[mcp_gradio_client](https://github.com/justjoehere/mcp_gradio_client)** - ⭐ 67
   This is a proof of concept repo on how to create a gradio UI using the Model Context Protocol Client Python SDK.

2755. **[community-servers](https://github.com/mcp-get/community-servers)** - ⭐ 67
   This repository contains a collection of community-maintained Model Context Protocol (MCP) servers. All servers are automatically listed on the MCP Get registry and can be viewed and installed via CLI

2756. **[mcp4k](https://github.com/ondrsh/mcp4k)** - ⭐ 67
   Compiler-driven MCP framework for Kotlin Multiplatform

2757. **[compass](https://github.com/raystack/compass)** - ⭐ 67
   Compass is a context engine that builds a knowledge graph of your organization's metadata, capturing   entities, relationships, and lineage across systems and time, making it discoverable and queryable for   both humans and AI agents.

2758. **[shinzo-ts](https://github.com/shinzo-labs/shinzo-ts)** - ⭐ 67
   TypeScript SDK for MCP server observability, built on OpenTelemetry. Gain insight into agent usage patterns, contextualize tool calls, and analyze server performance across platforms. Integrate with any OpenTelemetry ingest service including the Shinzo platform.

2759. **[mcp-stata](https://github.com/tmonk/mcp-stata)** - ⭐ 67
    A lightweight Model Context Protocol (MCP) server for Stata. Execute commands, inspect data, retrieve stored results (r()/e()), and view graphs in your chat interface. Built for economists who want to integrate LLM assistance into their Stata workflow.

2760. **[memcord](https://github.com/ukkit/memcord)** - ⭐ 67
   🧠 Privacy-first MCP server for AI memory management. Save, search & organize chat history with intelligent  summarization.

2761. **[MCPSpend](https://github.com/andreisirbu91-lab/MCPSpend)** - ⭐ 66
   Real-time cost observability for Model Context Protocol (MCP) tool calls. Wraps any MCP server, attributes spend per tool/project/customer. Free tier 25K calls/mo. EU-hosted

2762. **[mcp-tutorials](https://github.com/chenmingyong0423/mcp-tutorials)** - ⭐ 66
   Model Context Protocol(MCP) 中文教程讲解

2763. **[flapi](https://github.com/DataZooDE/flapi)** - ⭐ 66
   API Framework heavily relying on the power of DuckDB and DuckDB extensions. Ready to build performant and cost-efficient APIs on top of BigQuery or Snowflake  for AI Agents and Data Apps

2764. **[oh-my-kimi](https://github.com/dmae97/oh-my-kimi)** - ⭐ 66
   Production-ready multi-agent orchestration harness for Kimi Code CLI (K2.6): worktree team runtime, DAG/ensemble planning, MCP skill-hooks, quality gates, and local graph memory. | Kimi Code CLI(K2.6)向け本番対応マルチエージェント基盤: worktreeチーム実行、DAG/ensemble計画、MCP/スキルフック、品質ゲート、ローカルグラフ記憶を提供。

2765. **[amazon-mcp](https://github.com/Fewsats/amazon-mcp)** - ⭐ 66
   Amazon MCP server to search & buy products using the L402

2766. **[VibeShift](https://github.com/GroundNG/VibeShift)** - ⭐ 66
   [MCP Server] The Security Agent for AI assisted coding

2767. **[yamcp](https://github.com/hamidra/yamcp)** - ⭐ 66
   Organize your MCP servers in local workspaces, share them as Yet-Another-MCP through a single command

2768. **[join.cloud](https://github.com/kushneryk/join.cloud)** - ⭐ 66
   Join.cloud lets AI agents work together in real-time rooms. Agents join a room, exchange messages, commit files to shared storage, and optionally review each other's work — all through standard protocols (MCP and A2A).

2769. **[OpenStudy](https://github.com/OpenStudy-dev/OpenStudy)** - ⭐ 66
   Self-hostable study dashboard with a built-in MCP server, so that your Claude/ChatGPT subscription becomes x10 more effective for your semester

2770. **[deepview-mcp](https://github.com/ai-1st/deepview-mcp)** - ⭐ 65
   DeepView MCP is a Model Context Protocol server that enables IDEs like Cursor and Windsurf to analyze large codebases using Gemini 2.5 Pro's extensive context window.

2771. **[mcp-sdk](https://github.com/AntigmaLabs/mcp-sdk)** - ⭐ 65
   Minimalistic Rust Implementation Of Model Context Protocol from Anthropic

2772. **[cortex-scout](https://github.com/cortex-works/cortex-scout)** - ⭐ 65
   A unified web extraction and stateful automation engine for AI. Replaces heavy testing frameworks with token-optimized browser control, deep research, and HITL.

2773. **[sharepoint-mcp](https://github.com/DEmodoriGatsuO/sharepoint-mcp)** - ⭐ 65
   SharePoint MCP (Model Context Protocol) - A SharePoint connector for LLM applications. Access SharePoint documents and lists through Microsoft Graph API.

2774. **[academia_mcp](https://github.com/IlyaGusev/academia_mcp)** - ⭐ 65
   Academia MCP server: Tools for automatic scientific research

2775. **[mcp-bridge-api](https://github.com/INQUIRELAB/mcp-bridge-api)** - ⭐ 65
   MCP Bridge is a lightweight, fast, and LLM-agnostic proxy for connecting to multiple Model Context Protocol (MCP) servers through a unified REST API. It enables secure tool execution across diverse environments like mobile, web, and edge devices. Designed for flexibility, scalability, and easy integration with any LLM backend.

2776. **[ClaudeHistoryMCP](https://github.com/jhammant/ClaudeHistoryMCP)** - ⭐ 65
   MCP server for searching and surfacing Claude Code conversation history

2777. **[unraid-mcp](https://github.com/jmagar/unraid-mcp)** - ⭐ 65
   Query, monitor, and manage Unraid servers via GraphQL API through MCP tools. Supports system info, Docker, VMs, array/parity, notifications, plugins, rclone, and live telemetry.

2778. **[mcp-miro](https://github.com/k-jarzyna/mcp-miro)** - ⭐ 65
   Miro integration for Model Context Protocol

2779. **[Kaimon.jl](https://github.com/kahliburke/Kaimon.jl)** - ⭐ 65
   MCP server giving AI agents full access to Julia's runtime via a live Gate — code execution, introspection, debugging, testing, and semantic search

2780. **[lsd-mcp](https://github.com/lsd-so/lsd-mcp)** - ⭐ 65
   LSD Model Context Protocol

2781. **[nutrient-dws-mcp-server](https://github.com/PSPDFKit/nutrient-dws-mcp-server)** - ⭐ 65
   A Model Context Protocol (MCP) server implementation that integrates with the Nutrient Document Web Service (DWS) Processor API, providing powerful PDF processing capabilities for AI assistants.

2782. **[mobile-mcp](https://github.com/runablehq/mobile-mcp)** - ⭐ 65
   A Model Context Protocol (MCP) server that provides mobile automation capabilities.

2783. **[slack-mcp-plugin](https://github.com/slackapi/slack-mcp-plugin)** - ⭐ 65
   Repo containing the configuration information for the Slack MCP to be added to other clients

2784. **[estonia-ai-kit](https://github.com/stefanoamorelli/estonia-ai-kit)** - ⭐ 65
   🇪🇪 Open-source AI SDK for Estonian government and private services. MCP servers and skills. Connect Claude, GPT, agents and models, to Estonia's digital infrastructure.

2785. **[fhir-mcp-server](https://github.com/the-momentum/fhir-mcp-server)** - ⭐ 65
   FHIR MCP Server for handling medical data standard.

2786. **[SageFs](https://github.com/WillEhrendreich/SageFs)** - ⭐ 65
   Sage Mode for F# development — REPL with solution or project loading, Live Testing for FREE, Hot Reload, and session management.

2787. **[ollama-mcp-client](https://github.com/anjor/ollama-mcp-client)** - ⭐ 64

2788. **[Alph](https://github.com/Aqualia/Alph)** - ⭐ 64
   Universal MCP Server Configuration Manager

2789. **[screaming-frog-mcp](https://github.com/bzsasson/screaming-frog-mcp)** - ⭐ 64
   MCP server for Screaming Frog SEO Spider – crawl sites, export data, and manage crawl storage via Claude or any MCP-compatible client

2790. **[mcp-fhir](https://github.com/flexpa/mcp-fhir)** - ⭐ 64
   A Model Context Protocol implementation for FHIR

2791. **[metabase-mcp](https://github.com/hluaguo/metabase-mcp)** - ⭐ 64
   Metabase MCP server provides integration with the Metabase API, enabling LLM with MCP capabilites to directly interact with your analytics data, this server acts as a bridge between your analytics platform and conversational AI.

2792. **[mcp-config](https://github.com/marcusschiesser/mcp-config)** - ⭐ 64
   A CLI tool for easy installation of MCP servers and managing their configuration

2793. **[mcp-cn](https://github.com/mengjian-github/mcp-cn)** - ⭐ 64
   MCP Hub 中国是一个专注于 Model Context Protocol (MCP) 生态的开源平台。它致力于汇聚全球优质的 MCP 服务,提供一站式的解决方案,包括服务发现、接入指南和使用示例,并建立完善的中文生态,欢迎开发者参与贡献和完善平台功能。

2794. **[twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server)** - ⭐ 64
   A Model Context Protocol (MCP) server for Twenty CRM integration. Enables natural language interactions with your CRM data through Claude and other AI assistants. Supports CRUD operations, dynamic schema discovery, and advanced search across people, companies, tasks, and notes.

2795. **[appium-mcp](https://github.com/Rahulec08/appium-mcp)** - ⭐ 64
   AI-powered mobile automation with Model Context Protocol (MCP) integration. Seamlessly control Android & iOS devices through Appium with intelligent visual element detection and recovery. Built for AI agents like Claude to perform complex mobile testing workflows.

2796. **[svelte5-mcp](https://github.com/StudentOfJS/svelte5-mcp)** - ⭐ 64
   A specialized Model Context Protocol (MCP) server for Svelte 5 frontend development

2797. **[mcp-server](https://github.com/UI5/mcp-server)** - ⭐ 64
   The UI5 MCP server improves the developer experience when working with agentic AI and the UI5 framework.

2798. **[time-mcp](https://github.com/yokingma/time-mcp)** - ⭐ 64
   ⏰ Time MCP Server: Giving LLMs Time Awareness Capabilities

2799. **[CornMCP](https://github.com/yuki-20/CornMCP)** - ⭐ 64
   CornMCP is an open-source mono repo that gives AI coding agents (Antigravity, Cursor, Claude Code, Codex), token-saving access to your codebase through the Model Context Protocol (MCP).

2800. **[MCP-Dandan](https://github.com/82ch/MCP-Dandan)** - ⭐ 63
   MCP Security Solution for Agentic AI — real-time proxying, behavior analysis, and malicious tool detection

2801. **[godoctor](https://github.com/danicat/godoctor)** - ⭐ 63
   A Model Context Protocol server for Go developers

2802. **[mcp-think-tank](https://github.com/flight505/mcp-think-tank)** - ⭐ 63
   MCP Think Tank is a powerful Model Context Protocol (MCP) server designed to enhance the capabilities of AI assistants like Cursor and Claude. It provides a structured environment for enhanced reasoning, persistent memory, and responsible tool usage.

2803. **[canvas-mcp](https://github.com/vishalsachdev/canvas-mcp)** - ⭐ 63
   A Model Context Protocol server to run locally and connect to a Canvas LMS

2804. **[quick-mcp-example](https://github.com/ALucek/quick-mcp-example)** - ⭐ 62
   Short and sweet example MCP server / client implementation for Tools, Resources and Prompts.

2805. **[tuisic](https://github.com/Dark-Kernel/tuisic)** - ⭐ 62
   First of its kind, A simple TUI online music streaming application written in c++ with easy vim motions, now with support for Model Context Protocol (MCP)

2806. **[data-gov-il-mcp](https://github.com/DavidOsherdiagnostica/data-gov-il-mcp)** - ⭐ 62
   Advanced MCP server for seamless access to Israeli Government Open Data

2807. **[mcp-durable-object-client](https://github.com/Dhravya/mcp-durable-object-client)** - ⭐ 62
   testing mcps

2808. **[keynote-mcp](https://github.com/easychen/keynote-mcp)** - ⭐ 62
   A Model Context Protocol (MCP) server that enables AI assistants to control Keynote presentations through AppleScript automation.

2809. **[cap-mcp-plugin](https://github.com/gavdilabs/cap-mcp-plugin)** - ⭐ 62
   MCP (Model Context Protocol) server plugin for CAP NodeJS

2810. **[ashra-mcp](https://github.com/getrupt/ashra-mcp)** - ⭐ 62
   A Model Context Protocol server for Ashra

2811. **[mcp-hub](https://github.com/lobstercare/mcp-hub)** - ⭐ 62
   A curated list of awesome Model Context Protocol (MCP) servers.

2812. **[mcp-server-security-standard](https://github.com/mcp-security-standard/mcp-server-security-standard)** - ⭐ 62
   MCP Server Security Standard (MSSS): an open, testable security control standard for certifying MCP servers, with levels, evidence requirements, and reporting schemas.

2813. **[mcp-server-ccxt](https://github.com/Nayshins/mcp-server-ccxt)** - ⭐ 62
   Cryptocurrency Market Data MCP Server

2814. **[toonify-mcp](https://github.com/PCIRCLE-AI/toonify-mcp)** - ⭐ 62
   Context compression plugin for Claude Code. Trims large JSON, logs, stack traces, and source files before they enter the context window.

2815. **[rember-mcp](https://github.com/rember/rember-mcp)** - ⭐ 62
   A Model Context Protocol (MCP) server for Rember.

2816. **[ollama-mcp-db](https://github.com/robdodson/ollama-mcp-db)** - ⭐ 62
   An interactive chat interface that combines Ollama's LLM capabilities with PostgreSQL database access through the Model Context Protocol (MCP).

2817. **[trpc-mcp-go](https://github.com/trpc-group/trpc-mcp-go)** - ⭐ 62
   Go implementation of the Model Context Protocol (MCP) with comprehensive Streamable HTTP, STDIO, and SSE support.

2818. **[mcp-clojure-sdk](https://github.com/unravel-team/mcp-clojure-sdk)** - ⭐ 62
   A Clojure SDK to create MCP servers (and eventually clients)

2819. **[identity-service](https://github.com/agntcy/identity-service)** - ⭐ 61
   AGNTCY Identity Service serves as the central hub for managing and verifying digital identities for your Agentic Services.

2820. **[openproject-mcp-server](https://github.com/AndyEverything/openproject-mcp-server)** - ⭐ 61
   A Model Context Protocol (MCP) server that provides seamless integration with OpenProject API v3.

2821. **[anysite-mcp-server](https://github.com/anysiteio/anysite-mcp-server)** - ⭐ 61
   A Model Context Protocol (MCP) server that provides comprehensive access to LinkedIn data and functionalities using the Anysite API, enabling not only data retrieval but also robust management of user accounts.

2822. **[openclaw-superpowers](https://github.com/ArchieIndian/openclaw-superpowers)** - ⭐ 61
   44 plug-and-play skills for OpenClaw — self-modifying AI agent with cron scheduling, security guardrails, persistent memory, knowledge graphs, and MCP health monitoring. Your agent teaches itself new behaviors during conversation.

2823. **[ocaml-mcp-sdk](https://github.com/bmorphism/ocaml-mcp-sdk)** - ⭐ 61
   OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect library

2824. **[whoop-mcp](https://github.com/briangaoo/whoop-mcp)** - ⭐ 61
   Model Context Protocol server giving Claude (or any MCP client) full read + write access to your Whoop fitness data via the private reverse-engineered iOS API. 47 tools: recovery, sleep, strain, HRV trends, Strength Trainer, journal, Whoop Coach, and smart alarm. TypeScript + zod, auto-refresh Cognito auth.

2825. **[kroger-mcp](https://github.com/CupOfOwls/kroger-mcp)** - ⭐ 61
   A FastMCP server that provides AI assistants like Claude with access to Kroger's grocery shopping functionality through the Model Context Protocol (MCP). This server enables AI assistants to find stores, search products, manage shopping carts, and access Kroger's comprehensive grocery data via the kroger-api python library.

2826. **[mcpr](https://github.com/devOpifex/mcpr)** - ⭐ 61
   Model Context Protocol server and client for R

2827. **[nocodb-mcp-server](https://github.com/edwinbernadus/nocodb-mcp-server)** - ⭐ 61
   nocodb mcp server

2828. **[rag-app-on-aws](https://github.com/genieincodebottle/rag-app-on-aws)** - ⭐ 61
   Build and deploy a full-stack RAG app on AWS with Terraform, using free tier Gemini Pro, real-time web search using Remote MCP server and Streamlit UI with token based authentication.

2829. **[trainingpeaks-mcp](https://github.com/JamsusMaximus/trainingpeaks-mcp)** - ⭐ 61
   TrainingPeaks MCP server for Claude Desktop, Code and Cowork. No API approval needed - works with any account. Query workouts, CTL/ATL/TSB fitness data, power PRs via natural language.

2830. **[notebooklm-mcp-secure](https://github.com/Pantheon-Security/notebooklm-mcp-secure)** - ⭐ 61
   Secure NotebookLM MCP Server - Query Google NotebookLM from Claude/AI agents with 17 security hardening layers

2831. **[ibkr-mcp-server](https://github.com/seriallazer/ibkr-mcp-server)** - ⭐ 61
   MCP Server for IBKR Client

2832. **[smart-pet-with-mcp](https://github.com/shijianzhong/smart-pet-with-mcp)** - ⭐ 61
   一个桌宠形式的mcp client，可以对接任意mcp server,配合测试的mcp server 开源地址：https://github.com/shijianzhong/mcp-server-for-pc

2833. **[mcp-ssh](https://github.com/shuakami/mcp-ssh)** - ⭐ 61
   🔐 SSH MCP Tool - AI-powered SSH management through MCP protocol | 基于MCP协议的SSH工具，为AI提供SSH远程操作能力

2834. **[ebay-mcp](https://github.com/YosefHayim/ebay-mcp)** - ⭐ 61
   Open source local MCP server providing AI assistants with comprehensive access to eBay's Sell APIs. Includes 325 tools for inventory management, order fulfillment, marketing campaigns, analytics, developer tools, and more.

2835. **[hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp)** - ⭐ 61
   A Model Context Protocol server for integrating HackMD's note-taking platform with AI assistants.

2836. **[UnrealMCPBridge](https://github.com/appleweed/UnrealMCPBridge)** - ⭐ 60
   An Unreal Engine plugin that implements an MCP server allowing MCP clients to access the UE Editor Python API.

2837. **[devto-mcp](https://github.com/Arindam200/devto-mcp)** - ⭐ 60
   MCP Server of DevTo

2838. **[mcp-server-echart](https://github.com/cnkanwei/mcp-server-echart)** - ⭐ 60
   基于 mcp-go 框架构建的 mcp 服务，它提供了一个能动态生成 ECharts 图表页面的工具。

2839. **[discourse-mcp](https://github.com/discourse/discourse-mcp)** - ⭐ 60
   MCP client for Discourse sites

2840. **[getnote-mcp](https://github.com/iswalle/getnote-mcp)** - ⭐ 60
   GetNote For MCP

2841. **[contentful-mcp](https://github.com/ivo-toby/contentful-mcp)** - ⭐ 60
   MCP (Model Context Protocol) server for the Contentful Management API

2842. **[Claude-Deep-Research](https://github.com/mcherukara/Claude-Deep-Research)** - ⭐ 60
   An MCP (Model Context Protocol) server that enables comprehensive research capabilities for Claude

2843. **[mcp-bridgekit](https://github.com/mkbhardwas12/mcp-bridgekit)** - ⭐ 60
   Embeddable MCP stdio → HTTP bridge with background jobs & live dashboard. Survives Vercel/Cloudflare 30s timeouts. Now scales to 100+ users.

2844. **[mcp-openmsx](https://github.com/nataliapc/mcp-openmsx)** - ⭐ 60
   A Model Context Protocol (MCP) server for automating openMSX emulator instances. This server provides comprehensive tools for MSX software development, testing, and automation through standardized MCP protocols.

2845. **[autosteer](https://github.com/notch-ai/autosteer)** - ⭐ 60
   Desktop app for multi-workspace Claude Code management

2846. **[chucknorris](https://github.com/pollinations/chucknorris)** - ⭐ 60
   ⚡ C̷h̷u̷c̷k̷N̷o̷r̷r̷i̷s̷ MCP server: Helping LLMs break limits. Provides enhancement prompts inspired by elder-plinius' L1B3RT4S

2847. **[nutrient-document-engine-mcp-server](https://github.com/PSPDFKit/nutrient-document-engine-mcp-server)** - ⭐ 60
   A Model Context Protocol (MCP) server implementation exposes document processing capabilities through natural language, supporting both direct human interaction and AI agent tool calling.

2848. **[puremd-mcp](https://github.com/puremd/puremd-mcp)** - ⭐ 60
   Unblock, scrape, and search tools for MCP clients

2849. **[npm-packages](https://github.com/WebMCP-org/npm-packages)** - ⭐ 60
   NPM packages for MCP-B: Transport layers, React hooks, and browser tools for the Model Context Protocol

2850. **[claude-plugins](https://github.com/2389-research/claude-plugins)** - ⭐ 59
   28 plugins and MCP servers for Claude Code — TDD, multi-agent orchestration, iterative refinement, binary RE, structured decisions. Install any skill in one command.

2851. **[mcp-kubernetes](https://github.com/Azure/mcp-kubernetes)** - ⭐ 59
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Kubernetes clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and Kubernetes

2852. **[cline-mcp-memory-bank](https://github.com/dazeb/cline-mcp-memory-bank)** - ⭐ 59
   A memory system for Cline that tracks progress between conversations.

2853. **[supermcp](https://github.com/dhanababum/supermcp)** - ⭐ 59
   🚀 SuperMCP - Create multiple isolated MCP servers using a single connector. Build powerful Model Context Protocol integrations for databases (PostgreSQL, MSSQL) with FastAPI backend, React dashboard, and token-based auth. Perfect for multi-tenant apps and AI assistants.

2854. **[mcp-difyworkflow-server](https://github.com/gotoolkits/mcp-difyworkflow-server)** - ⭐ 59
   mcp-difyworkflow-server is an mcp server Tools application that implements the query and invocation of Dify workflows, supporting the on-demand operation of multiple custom Dify workflows.

2855. **[devswarm](https://github.com/justrach/devswarm)** - ⭐ 59
   High-performance MCP server, code graph engine & evolutionary algorithm platform in Zig. 33 tools: GitHub project management, agent swarm orchestration, iterative review-fix loops, blast radius analysis, and code navigation via Model Context Protocol.

2856. **[nvim-mcp](https://github.com/linw1995/nvim-mcp)** - ⭐ 59
   A Model Context Protocol (MCP) server that provides seamless integration with Neovim instances, enabling AI assistants to interact with your editor through connections and access diagnostic information via structured resources.

2857. **[context-optimizer-mcp-server](https://github.com/malaksedarous/context-optimizer-mcp-server)** - ⭐ 59
   A Model Context Protocol (MCP) server that provides context optimization tools for AI coding assistants including GitHub Copilot, Cursor AI, Claude Desktop, and other MCP-compatible assistants enabling them to extract targeted information rather than processing large terminal outputs and files wasting their context.

2858. **[aitour26-WRK542-prototype-agents-with-Foundry-toolkit-and-model-context-protocol](https://github.com/microsoft/aitour26-WRK542-prototype-agents-with-Foundry-toolkit-and-model-context-protocol)** - ⭐ 59

2859. **[openaccountants](https://github.com/openaccountants/openaccountants)** - ⭐ 59
   Open-source tax skills for AI — 371 skills across 134 countries. Upload to any LLM or connect via MCP. Quality-tiered Q1–Q5.

2860. **[mcp_server_gdb](https://github.com/pansila/mcp_server_gdb)** - ⭐ 59
   MCP Server to expose the GDB debugging capabilities

2861. **[ask-user-questions-mcp](https://github.com/paulp-o/ask-user-questions-mcp)** - ⭐ 59
   Better 'AskUserQuestion' - A lightweight MCP server/OpenCode plugin/Agent Skills + CLI tool that allows your LLMs ask questions to you. Be the human in the human-in-the-loop!

2862. **[camofox-mcp](https://github.com/redf0x1/camofox-mcp)** - ⭐ 59
   Anti-detection browser MCP server for AI agents — navigate, interact, and automate the web without getting blocked

2863. **[mcp-batchit](https://github.com/ryanjoachim/mcp-batchit)** - ⭐ 59
   🚀 MCP aggregator for batching multiple tool calls into a single request. Reduces overhead, saves tokens, and simplifies complex operations in AI agent workflows.

2864. **[oh-my-codex](https://github.com/scalarian/oh-my-codex)** - ⭐ 59
   oh-my-codex (omx) — Orchestration layer for OpenAI Codex CLI. Async Claude Code delegation (no timeouts), structured workflows (autopilot, TDD, code review, planning), persistent state & memory. Like oh-my-zsh but for Codex.

2865. **[mono-mcp](https://github.com/sin4ch/mono-mcp)** - ⭐ 59
   A comprehensive Model Context Protocol (MCP) server for Nigerian banking operations using the Mono Open Banking API.

2866. **[awesome-remote-mcp-servers](https://github.com/sylviangth/awesome-remote-mcp-servers)** - ⭐ 59
   A curated list of Hosted & Managed Model Context Protocol (MCP) Servers accessible via a simple URL endpoint.

2867. **[AgentTools](https://github.com/WolframResearch/AgentTools)** - ⭐ 59
   Implements a model context protocol server using Wolfram Language

2868. **[shadcn-ui-mcp-server](https://github.com/ymadd/shadcn-ui-mcp-server)** - ⭐ 59
   MCP server for shadcn/ui component references

2869. **[Memory-Plus](https://github.com/Yuchen20/Memory-Plus)** - ⭐ 59
   🧠 𝑴𝒆𝒎𝒐𝒓𝒚-𝑷𝒍𝒖𝒔 is a lightweight, local RAG memory store for MCP agents. Easily record, retrieve, update, delete, and visualize persistent "memories" across sessions—perfect for developers working with multiple AI coders (like Windsurf, Cursor, or Copilot) or anyone who wants their AI to actually remember them.

2870. **[job-searchoor](https://github.com/0xDAEF0F/job-searchoor)** - ⭐ 58
   A simple MCP server that delivers you jobs based on your needs

2871. **[mcpserver](https://github.com/2234839/mcpserver)** - ⭐ 58
   为claude code+glm 添加上眼睛

2872. **[safari-mcp](https://github.com/achiya-automation/safari-mcp)** - ⭐ 58
   Native Safari browser automation for AI agents. 80 tools via AppleScript — zero overhead, keeps logins, runs silently in background. Drop-in alternative to Chrome DevTools MCP with 40-60% less CPU/heat on Apple Silicon.

2873. **[mcp-docs-service](https://github.com/alekspetrov/mcp-docs-service)** - ⭐ 58
   MCP Documentation Management Service - A Model Context Protocol implementation for documentation management

2874. **[Zikkaron](https://github.com/amanhij/Zikkaron)** - ⭐ 58
   Biologically-inspired persistent memory engine for Claude Code. 26 cognitive subsystems, Hopfield networks, predictive coding, causal discovery, successor representations, all running locally over SQLite.

2875. **[email-mcp](https://github.com/codefuturist/email-mcp)** - ⭐ 58
   Email MCP server with full IMAP + SMTP support — read, search, send, manage, and organize email from any AI assistant via the Model Context Protocol

2876. **[contentful-mcp-server](https://github.com/contentful/contentful-mcp-server)** - ⭐ 58
   MCP (Model Context Protocol) server for the Contentful Management API

2877. **[deploystack](https://github.com/deploystackio/deploystack)** - ⭐ 58
   Open source MCP hosting - deploy MCP servers to HTTP endpoints for n8n, Dify, Voiceflow, and any MCP client.

2878. **[ntfy-me-mcp](https://github.com/gitmotion/ntfy-me-mcp)** - ⭐ 58
   An ntfy MCP server for sending/fetching ntfy notifications to self-hosted or ANY ntfy.sh server from AI Agents 📤 (supports secure token auth & more - use with npx or docker!)

2879. **[mcp-toolbox-sdk-go](https://github.com/googleapis/mcp-toolbox-sdk-go)** - ⭐ 58
   Go SDK for interacting with the MCP Toolbox for Databases.

2880. **[hana-mcp-server](https://github.com/HatriGt/hana-mcp-server)** - ⭐ 58
   SAP HANA MCP server — Enterprise Model Context Protocol server for SAP HANA. Use with Claude Code, VS Code. npm: hana-mcp-server

2881. **[ai-forge-mcp](https://github.com/HurtzDonutStudios/ai-forge-mcp)** - ⭐ 58
   565 AI-callable tools across 16 MCP servers. Full-pipeline AAA game asset production. Controls Blender, Substance Suite, Maya, Houdini, and Unreal Engine 5. 50 specialized AI agents. One prompt in, game-ready asset out.

2882. **[thoughtbox](https://github.com/Kastalien-Research/thoughtbox)** - ⭐ 58
   Thoughtbox is an intention ledger for agents. Evaluate AI's decisions against its decision-making.

2883. **[org-mcp](https://github.com/laurynas-biveinis/org-mcp)** - ⭐ 58
   Emacs Org-mode integration with Model Context Protocol (MCP) for AI-assisted task management

2884. **[mcpshim](https://github.com/mcpshim/mcpshim)** - ⭐ 58
   Turn remote MCP servers into local command workflows.

2885. **[metis-router](https://github.com/metis-mantis/metis-router)** - ⭐ 58
   MCP router and Web Based MCP client

2886. **[aura](https://github.com/mezmo/aura)** - ⭐ 58
   A production-ready framework for composing AI agents from declarative TOML configuration, with MCP tool integration, RAG pipelines, and an OpenAI-compatible web API.

2887. **[mcp-cpp](https://github.com/Neumann-Labs/mcp-cpp)** - ⭐ 58
   A C++ SDK for the Model Context Protocol (MCP). The SDK will provide a framework for creating MCP servers and clients in C++.

2888. **[mcp-gitee](https://github.com/oschina/mcp-gitee)** - ⭐ 58
   mcp-gitee is a Model Context Protocol (MCP) server implementation for Gitee. It provides a set of tools that interact with Gitee's API, allowing AI assistants to manage repository, issues, pull requests, etc.

2889. **[mcp-gearbox](https://github.com/rohitsoni007/mcp-gearbox)** - ⭐ 58
   A modern desktop application for managing Model Context Protocol (MCP) servers across multiple AI agents

2890. **[vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp)** - ⭐ 58
   This project is a Model Context Protocol (MCP) server for interacting with the VRChat API.

2891. **[iota-agent-mcp](https://github.com/Scottcjn/iota-agent-mcp)** - ⭐ 58
   MCP server for IOTA blockchain — 20 tools for AI agent integration (wallet, Move CLI, on-chain queries via Model Context Protocol)

2892. **[scrapegraph-mcp](https://github.com/ScrapeGraphAI/scrapegraph-mcp)** - ⭐ 58
   ScapeGraph MCP Server

2893. **[vscode-mcp](https://github.com/tjx666/vscode-mcp)** - ⭐ 58
   MCP server for Claude Code/VSCode/Cursor/Windsurf to use editor self functionality. ⚡ Get real-time LSP diagnostics, type information, and code navigation for AI coding agents without waiting for slow tsc/eslint checks.

2894. **[unity-mcp-pro-plugin](https://github.com/youichi-uda/unity-mcp-pro-plugin)** - ⭐ 58
   147 AI tools for Unity game development via MCP (Model Context Protocol). Connect Claude, Cursor, and AI assistants to your Unity editor.

2895. **[foundry-vtt-mcp](https://github.com/adambdooley/foundry-vtt-mcp)** - ⭐ 57
   An MCP (Model Context Protocol) server that bridges Foundry VTT data with Claude Desktop, enabling users to chat with their game world data using their own Claude subscription.

2896. **[create-mcp-app](https://github.com/boguan/create-mcp-app)** - ⭐ 57
   A CLI tool for quickly scaffolding Model Context Protocol (MCP) server applications with TypeScript support and modern development tooling

2897. **[daipendency-mcp](https://github.com/daipendency/daipendency-mcp)** - ⭐ 57
   Model Context Protocol server for Daipendency

2898. **[fast-filesystem-mcp](https://github.com/efforthye/fast-filesystem-mcp)** - ⭐ 57
   A high-performance Model Context Protocol (MCP) server that provides secure filesystem access for Claude and other AI assistants.

2899. **[esa-mcp-server](https://github.com/esaio/esa-mcp-server)** - ⭐ 57
   esa.io の公式 MCP(Model Context Protocol)サーバー(STDIO Transport版)

2900. **[calculator-mcp-server](https://github.com/huhabla/calculator-mcp-server)** - ⭐ 57
   A Model Context Protocol (MCP) server that provides Claude with advanced mathematical calculation capabilities

2901. **[luma-mcp](https://github.com/JochenYang/luma-mcp)** - ⭐ 57
   Multi-Model Visual Understanding MCP Server, GLM-4.6V, DeepSeek-OCR (free), and Qwen3-VL-Flash. Provide visual processing capabilities for AI coding models that do not support image understanding.多模型视觉理解MCP服务器，GLM-4.6V、DeepSeek-OCR（免费）和Qwen3-VL-Flash等。为不支持图片理解的 AI 编码模型提供视觉处理能力。

2902. **[MCP_Atom_of_Thoughts](https://github.com/kbsooo/MCP_Atom_of_Thoughts)** - ⭐ 57
   Atom of Thoughts (AoT) MCP is a server that decomposes complex problems into independent atomic units of thought, using the dependencies between these units to deliver more robust reasoning and validated insights.

2903. **[RedTeam-Agent](https://github.com/ktol1/RedTeam-Agent)** - ⭐ 57
    RedTeam-Agent: AI-Powered Autonomous Red Team Framework via Model Context Protocol. AI红队与内网渗透自动化框架，支持 gogo, fscan, httpx, nuclei, impacket, playwright 等 15+ 渗透工具，让 LLM 直接化身安全审计黑客。

2904. **[shotgrid-mcp-server](https://github.com/loonghao/shotgrid-mcp-server)** - ⭐ 57
   A Model Context Protocol (MCP) server for Autodesk ShotGrid/Flow Production Tracking (FPT) with comprehensive CRUD operations and data management capabilities.

2905. **[mailgun-mcp-server](https://github.com/mailgun/mailgun-mcp-server)** - ⭐ 57
   Implementation of Model Context Protocol server for Mailgun APIs

2906. **[python](https://github.com/mcp-auth/python)** - ⭐ 57
   🔐 Plug-and-play auth for Python MCP servers.

2907. **[adbfriend](https://github.com/mikepenz/adbfriend)** - ⭐ 57
   Android ADB CLI tool including integrated MCP Server with common adb actions used during development

2908. **[React-Native-MCP](https://github.com/MrNitro360/React-Native-MCP)** - ⭐ 57
   A Model Context Protocol (MCP) server providing comprehensive guidance and best practices for React Native development based on official React Native documentation.

2909. **[imap-mcp](https://github.com/non-dirty/imap-mcp)** - ⭐ 57
   IMAP Model Context Protocol server for interactive email processing

2910. **[tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp)** - ⭐ 57
   A Model Context Protocol (MCP) server for Tripadvisor Content API.  This provides access to Tripadvisor location data, reviews, and photos through standardized MCP interfaces, allowing AI assistants to search for travel destinations and experiences.

2911. **[scheduler-mcp](https://github.com/PhialsBasement/scheduler-mcp)** - ⭐ 57
   MCP Scheduler is a task automation server that lets you schedule shell commands, API calls, AI tasks, and desktop notifications using cron expressions. Built with Model Context Protocol for seamless integration with Claude Desktop and other AI assistants.

2912. **[rustchain-mcp](https://github.com/Scottcjn/rustchain-mcp)** - ⭐ 57
   MCP server for RustChain blockchain and BoTTube video platform — AI agent tools for earning RTC tokens. Built on createkr's RustChain SDK.

2913. **[Archive-Agent](https://github.com/shredEngineer/Archive-Agent)** - ⭐ 57
   Find your files with natural language and ask questions.

2914. **[brainstorm-mcp](https://github.com/spranab/brainstorm-mcp)** - ⭐ 57
   MCP server for multi-round AI brainstorming debates between multiple models (GPT, DeepSeek, Groq, Ollama, etc.)

2915. **[mkp](https://github.com/StacklokLabs/mkp)** - ⭐ 57
   MKP is a Model Context Protocol (MCP) server for Kubernetes

2916. **[nasdaq-data-link-mcp](https://github.com/stefanoamorelli/nasdaq-data-link-mcp)** - ⭐ 57
   A Nasdaq Data Link MCP (Model Context Protocol) Server

2917. **[email-mcp](https://github.com/TimeCyber/email-mcp)** - ⭐ 57
   一个让AI轻松接管邮箱的MCP服务，基于 Model Context Protocol (MCP) 构建，支持在 MCP-X,Claude Desktop 等 MCP 客户端中使用。

2918. **[ocaml-mcp](https://github.com/tmattio/ocaml-mcp)** - ⭐ 57
   OCaml implementation of the Model Context Protocol (MCP)

2919. **[go-mcp-mysql](https://github.com/Zhwt/go-mcp-mysql)** - ⭐ 57
   Zero burden, ready-to-use Model Context Protocol (MCP) server for interacting with MySQL and automation. No Node.js or Python environment needed.

2920. **[hwpx-mcp-server](https://github.com/airmang/hwpx-mcp-server)** - ⭐ 56
   MCP server for AI agents to read, edit, inspect, and validate local HWPX documents.

2921. **[opencode-mcp](https://github.com/AlaeddineMessadi/opencode-mcp)** - ⭐ 56
   MCP server for OpenCode AI — 70 tools, 10 resources, 5 prompts. Use npx opencode-mcp with Claude Desktop, Claude Code, Cursor, Windsurf, or any MCP client.

2922. **[AllVoiceLab-MCP](https://github.com/allvoicelab/AllVoiceLab-MCP)** - ⭐ 56
   Official AllVoiceLab Model Context Protocol (MCP) server, supporting interaction with powerful text-to-speech and video translation APIs.

2923. **[mcp-gemini-search](https://github.com/arjunprabhulal/mcp-gemini-search)** - ⭐ 56
   Model Context Protocol (MCP) with Gemini 2.5 Pro. Convert conversational queries into flight searches using Gemini's function calling capabilities and MCP's flight search tools

2924. **[mcp-oauth-gateway](https://github.com/atrawog/mcp-oauth-gateway)** - ⭐ 56
   An OAuth 2.1 Authorization Server that adds authentication to any MCP (Model Context Protocol) server without code modification.

2925. **[mcp-server-flomo](https://github.com/chatmcp/mcp-server-flomo)** - ⭐ 56
   Write notes to Flomo

2926. **[unity-api-mcp](https://github.com/Codeturion/unity-api-mcp)** - ⭐ 56
   Instant, accurate Unity API lookups instead of expensive source file reads, saving your agent tokens, context, and hallucinations

2927. **[mcp-amadeus](https://github.com/donghyun-chae/mcp-amadeus)** - ⭐ 56
   Amadeus MCP(Model Context Protocol) Server

2928. **[mcp-server](https://github.com/inkdropapp/mcp-server)** - ⭐ 56
   Inkdrop Model Context Protocol Server

2929. **[naver-search-mcp](https://github.com/isnow890/naver-search-mcp)** - ⭐ 56
   MCP server for Naver Search API integration. Provides comprehensive search capabilities across Naver services (web, news, blog, shopping, etc) and data trend analysis tools via DataLab API.

2930. **[better-bear](https://github.com/KuvopLLC/better-bear)** - ⭐ 56

2931. **[ferris-search](https://github.com/lispking/ferris-search)** - ⭐ 56
   A blazing-fast MCP (Model Context Protocol) server for multi-engine web search, written in Rust.

2932. **[mcp-thinking](https://github.com/mattzcarey/mcp-thinking)** - ⭐ 56
   thinking tool for claude desktop/mcp clients using Deepseek reasoner

2933. **[minimax_search](https://github.com/MiniMax-AI/minimax_search)** - ⭐ 56
   MiniMax Search is an MCP (Model Context Protocol) server that provides web search and browsing capabilities.

2934. **[astro-mcp](https://github.com/morinokami/astro-mcp)** - ⭐ 56
   MCP server to support Astro project development

2935. **[web2mcp](https://github.com/neelsomani/web2mcp)** - ⭐ 56
   Generate an MCP for any web app

2936. **[solana-mcp-server](https://github.com/openSVM/solana-mcp-server)** - ⭐ 56
   solana mcp sever to enable solana rpc methods

2937. **[client](https://github.com/php-mcp/client)** - ⭐ 56
   Core PHP implementation for the Model Context Protocol (MCP) Client

2938. **[agent-trace](https://github.com/Siddhant-K-code/agent-trace)** - ⭐ 56
   strace for AI agents. Capture and replay every tool call, prompt, and response from Claude Code, Cursor, Gemini CLI or any MCP client

2939. **[ai-vision-mcp](https://github.com/tan-yong-sheng/ai-vision-mcp)** - ⭐ 56
   A Model Context Protocol (MCP) server that provides vision capabilities to analyze image and video

2940. **[ai-humanizer-mcp-server](https://github.com/Text2Go/ai-humanizer-mcp-server)** - ⭐ 56
   A powerful Model Context Protocol (MCP) server that helps refine AI-generated content to sound more natural and human-like. Built with advanced AI detection and text enhancement capabilities.

2941. **[cml-mcp](https://github.com/xorrkaz/cml-mcp)** - ⭐ 56
   A Model Context Protocol (MCP) Server for Cisco Modeling Labs (CML)

2942. **[fossil-mcp](https://github.com/yfedoseev/fossil-mcp)** - ⭐ 56
   The code quality toolkit for the agentic AI era. Find dead code, clones, and scaffolding across 15 languages. MCP server + CLI.

2943. **[mcp-secrets-plugin](https://github.com/amirshk/mcp-secrets-plugin)** - ⭐ 55
   Secure credential management for MCP servers leveraging system-native keychain storage across macOS, Windows, and Linux platforms

2944. **[agentic-pymol](https://github.com/Arcadia-Science/agentic-pymol)** - ⭐ 55
   A Model Context Protocol (MCP) server that exposes PyMOL as a typed tool surface to your agent (Claude Code/Desktop, Codex, or any MCP-compatible client)

2945. **[mcp-headless-gmail](https://github.com/baryhuang/mcp-headless-gmail)** - ⭐ 55
   A MCP (Model Context Protocol) server that provides get, send Gmails without local credential or token setup.

2946. **[cosmotop](https://github.com/bjia56/cosmotop)** - ⭐ 55
   Multiplatform system monitoring tool using Cosmopolitan Libc

2947. **[touchdesigner-mcp-server](https://github.com/bottobot/touchdesigner-mcp-server)** - ⭐ 55
   TouchDesigner Documentation MCP Server v2.6.1 - FIXED Python API tools! Features 629 operators + 14 tutorials + 69 Python API classes with working get_python_api & search_python_api tools. Zero-configuration setup for VS Code/Codium.

2948. **[crawlbase-mcp](https://github.com/crawlbase/crawlbase-mcp)** - ⭐ 55
   Crawlbase MCP Server connects AI agents and LLMs with real-time web data. It powers Claude, Cursor, and Windsurf integrations with battle-tested web scraping, JavaScript rendering, and anti-bot protection enabling structured, live data inside your AI workflows.

2949. **[ctxvault](https://github.com/Filippo-Venturini/ctxvault)** - ⭐ 55
   Local memory infrastructure for AI agents. Store knowledge and skills in isolated vaults you compose, control and query.

2950. **[trellis_blender](https://github.com/FishWoWater/trellis_blender)** - ⭐ 55
   Blender plugin for TRELLIS and TRELLIS.2 (3D AIGC Model, Text-to-3D, Image-to-3D)

2951. **[Intelli](https://github.com/intelligentnode/Intelli)** - ⭐ 55
   Build multi-model chatbots and agents from intent.

2952. **[mcp-duckdb-memory-server](https://github.com/IzumiSy/mcp-duckdb-memory-server)** - ⭐ 55
   MCP Memory Server with DuckDB backend

2953. **[mssql_mcp_server](https://github.com/JexinSam/mssql_mcp_server)** - ⭐ 55
   A Model Context Protocol (MCP) server facilitating secure interactions with MSSQL databases.

2954. **[stackchan-mcp](https://github.com/kisaragi-mochi/stackchan-mcp)** - ⭐ 55
   MCP gateway for StackChan (xiaozhi-esp32): bridge any MCP client to a CoreS3 + servo + camera robot

2955. **[tokio-prompt-orchestrator](https://github.com/Mattbusel/tokio-prompt-orchestrator)** - ⭐ 55
   Multi-core, Tokio-native orchestration for LLM pipelines.

2956. **[go-crx3](https://github.com/mmadfox/go-crx3)** - ⭐ 55
   Chrome browser extension tools with MCP integration. Pack, unpack, zip, unzip, download, and manage CRX3 extensions – now AI-compatible via Model Context Protocol.

2957. **[adx-mcp-server](https://github.com/pab1it0/adx-mcp-server)** - ⭐ 55
   A Model Context Protocol (MCP) server that enables AI assistants to query and analyze Azure Data Explorer databases through standardized interfaces.

2958. **[AfdianToMarkdown](https://github.com/PhiFever/AfdianToMarkdown)** - ⭐ 55
   爱发电爬虫(afdian.com)

2959. **[rulego-server](https://github.com/rulego/rulego-server)** - ⭐ 55
   A lightweight dependency-free workflow automation platform. Supports iPaaS, stream computing, MCP, and AI capabilities.

2960. **[AI-Cursor-Scraping-Assistant](https://github.com/TheWebScrapingClub/AI-Cursor-Scraping-Assistant)** - ⭐ 55
   A powerful tool that leverages Cursor AI and MCP (Model Context Protocol) to easily generate web scrapers for various types of websites.

2961. **[powhttp-mcp](https://github.com/usestring/powhttp-mcp)** - ⭐ 55
   MCP server enabling agents to debug HTTP requests better (using powhttp)

2962. **[minibridge](https://github.com/acuvity/minibridge)** - ⭐ 54
   Make your MCP servers secure and production ready

2963. **[Navidrome-MCP](https://github.com/Blakeem/Navidrome-MCP)** - ⭐ 54
   Analyze listening patterns, create custom playlists, discover missing albums, discover similar artists, discover radio stations, and validate radio streams using natural language.

2964. **[RoslynMCP](https://github.com/carquiza/RoslynMCP)** - ⭐ 54
   A Model Context Protocol (MCP) server that provides C# code analysis capabilities using Microsoft Roslyn

2965. **[mcp-accessibility-scanner](https://github.com/JustasMonkev/mcp-accessibility-scanner)** - ⭐ 54
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core.

2966. **[temporal-mcp](https://github.com/Mocksi/temporal-mcp)** - ⭐ 54
   Empowering AI with Workflow Orchestration

2967. **[swift-mcp-gui](https://github.com/NakaokaRei/swift-mcp-gui)** - ⭐ 54
   MCP server that can execute commands such as keyboard input and mouse movement on macOS

2968. **[ns-mcp-server](https://github.com/r-huijts/ns-mcp-server)** - ⭐ 54
   A Model Context Protocol (MCP) server that provides access to NS (Dutch Railways) travel information through Claude AI. This server enables Claude to fetch real-time train travel information and disruptions using the official Dutch NS API.

2969. **[template-mcp-server](https://github.com/redhat-data-and-ai/template-mcp-server)** - ⭐ 54
   Production-ready Python template for building MCP servers with FastMCP, FastAPI, OAuth, and OpenShift deployment.

2970. **[talkito](https://github.com/robdmac/talkito)** - ⭐ 54
   TalkiTo lets developers interact with AI systems through speech across multiple channels (terminal, API, phone). It can be used as both a command-line tool and a Python library.

2971. **[mcp-mermaid-validator](https://github.com/rtuin/mcp-mermaid-validator)** - ⭐ 54
   A Model Context Protocol server that validates and renders Mermaid diagrams.

2972. **[Koppla](https://github.com/ruudmens/Koppla)** - ⭐ 54
   A Model-Context-Protocol (MCP) Server for Active Directory

2973. **[sympy-mcp](https://github.com/sdiehl/sympy-mcp)** - ⭐ 54
   A MCP server for symbolic manipulation of mathematical expressions

2974. **[mcp](https://github.com/supadata-ai/mcp)** - ⭐ 54
   Official Supadata MCP Server - Adds powerful video & web scraping to Cursor, Claude and any other LLM clients.

2975. **[rs-utcp](https://github.com/universal-tool-calling-protocol/rs-utcp)** - ⭐ 54
   Official Rust implementation of the UTCP

2976. **[claude-code-emacs](https://github.com/yuya373/claude-code-emacs)** - ⭐ 54
   This package provides seamless integration with Claude Code, allowing you to run AI-powered coding sessions directly in your Emacs environment.

2977. **[NoLLMChat](https://github.com/zrg-team/NoLLMChat)** - ⭐ 54
   Not-Only LLM Chat. An AI application that enhances creativity and user experience beyond just LLM chat. Noted: Seems it beta version of there is issue with DB please clear site Data in debug

2978. **[mcp](https://github.com/40ants/mcp)** - ⭐ 53
   40ANTS-MCP is a framework for building Model Context Protocol servers in Common Lisp

2979. **[mcp-server-atlassian-confluence](https://github.com/aashari/mcp-server-atlassian-confluence)** - ⭐ 53
   Node.js/TypeScript MCP server for Atlassian Confluence. Provides tools enabling AI systems (LLMs) to list/get spaces & pages (content formatted as Markdown) and search via CQL. Connects AI seamlessly to Confluence knowledge bases using the standard MCP interface.

2980. **[skrills](https://github.com/athola/skrills)** - ⭐ 53
   Coordinate skills between Codex, Copilot, and Claude Code. Validates, analyzes, and syncs skills, subagents, commands, and configuration between multiple CLIs.

2981. **[cheat-engine-server-python](https://github.com/bethington/cheat-engine-server-python)** - ⭐ 53
   MCP Cheat Engine Server — provides safe, structured read-only access to memory analysis and debugging functionality through the Model Context Protocol (MCP). For developers, security researchers, and game modders.

2982. **[adk-mcp-a2a-crash-course](https://github.com/chongdashu/adk-mcp-a2a-crash-course)** - ⭐ 53
   This project demonstrates a multi-agent system using Google's Agent Development Kit (ADK), Agent2Agent (A2A) and Model Context Protocol (MCP).  that integrates Notion for information retrieval and ElevenLabs for text-to-speech conversion.

2983. **[mcp-zap-server](https://github.com/dtkmn/mcp-zap-server)** - ⭐ 53
   A Spring Boot application exposing OWASP ZAP as an MCP (Model Context Protocol) server. It lets any MCP‑compatible AI agent (e.g., Claude Desktop, Cursor) orchestrate ZAP actions—spider, active scan, import OpenAPI specs, and generate reports.

2984. **[CE-MCP-Plugin](https://github.com/Eruditi/CE-MCP-Plugin)** - ⭐ 53
   CE MCP Plugin是一个Cheat Engine插件，它实现了Model Context Protocol (MCP)，允许AI模型与Cheat Engine进行交互。通过这个插件，AI可以使用Cheat Engine的各种功能，如内存读写、进程管理等。

2985. **[mcp-server-azure-ai-agents](https://github.com/farzad528/mcp-server-azure-ai-agents)** - ⭐ 53
   Model Context Protocol Servers for Azure AI Search

2986. **[mcp-guard](https://github.com/General-Analysis/mcp-guard)** - ⭐ 53
   MCP Guard secures your MCP client from prompt injection attacks and more.

2987. **[mcp-musescore](https://github.com/ghchen99/mcp-musescore)** - ⭐ 53
   A Model Context Protocol (MCP) server that provides programmatic control over MuseScore!

2988. **[mcp-dap-server](https://github.com/go-delve/mcp-dap-server)** - ⭐ 53
   MCP server to communicate with DAP servers allowing AI Agents the ability to debug live programs.

2989. **[mlb-api-mcp](https://github.com/guillochon/mlb-api-mcp)** - ⭐ 53
   A Model Context Protocol (MCP) server that provides comprehensive access to MLB statistics and baseball data through a FastMCP-based interface.

2990. **[mcp-codestyle-server](https://github.com/itxaiohanglover/mcp-codestyle-server)** - ⭐ 53
   MCP Codestyle Server 是一个基于 Spring AI 实现的 Model Context Protocol (MCP) 服务器，为 IDE 和 AI 代理提供代码模板搜索和检索工具。该服务从本地缓存查找模板，并在缺失时自动从远程仓库下载元数据和文件进行修复。

2991. **[youtube-mcp-server](https://github.com/mourad-ghafiri/youtube-mcp-server)** - ⭐ 53
   A powerful Model Context Protocol (MCP) server for YouTube video transcription and metadata extraction.

2992. **[user-feedback-mcp](https://github.com/mrexodia/user-feedback-mcp)** - ⭐ 53
   Simple MCP Server to enable a human-in-the-loop workflow in tools like Cline and Cursor.

2993. **[nvim-mcp](https://github.com/paulburgess1357/nvim-mcp)** - ⭐ 53
   MCP server that connects AI agents to your running Neovim instance via msgpack-RPC — no plugins required.

2994. **[mcp-security-audit](https://github.com/qianniuspace/mcp-security-audit)** - ⭐ 53
   A powerful MCP (Model Context Protocol) Server that audits npm package dependencies for security vulnerabilities. Built with remote npm registry integration for real-time security checks.

2995. **[openai-mcp-client](https://github.com/ResoluteError/openai-mcp-client)** - ⭐ 53
   A rudimentary implementation of Anthropic's Model Context Protocol with OpenAIs Model

2996. **[Multi-Agent-System-A2A-ADK-MCP](https://github.com/RubensZimbres/Multi-Agent-System-A2A-ADK-MCP)** - ⭐ 53
   Multi-Agent Systems with Google's Agent Development Kit + A2A + MCP

2997. **[mcp-openai](https://github.com/S1M0N38/mcp-openai)** - ⭐ 53
   🔗 MCP Client with OpenAI compatible API

2998. **[rhinoMcpServer](https://github.com/always-tinkering/rhinoMcpServer)** - ⭐ 52
   RhinoMCP connects Rhino to Claude AI through the Model Context Protocol (MCP), enabling AI-assisted 3D modeling and architectural design.

2999. **[Scientific-Papers-MCP](https://github.com/benedict2310/Scientific-Papers-MCP)** - ⭐ 52
   A Model Context Protocol (MCP) server that provides LLMs with real-time access to scientific papers from arXiv and OpenAlex.

3000. **[youtrack-mcp](https://github.com/devstroop/youtrack-mcp)** - ⭐ 52
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

3001. **[peta-core](https://github.com/dunialabs/peta-core)** - ⭐ 52
   The Control Plane for MCP — secure vault, managed runtime, audit trail, and policy-based approvals.

3002. **[mcp-rdf-explorer](https://github.com/emekaokoye/mcp-rdf-explorer)** - ⭐ 52
   A Model Context Protocol (MCP) server that provides conversational interface for the exploration and analysis of RDF (Turtle) based Knowledge Graph in Local File mode or SPARQL Endpoint mode.

3003. **[funplay-unity-mcp](https://github.com/FunplayAI/funplay-unity-mcp)** - ⭐ 52
   The Most Advanced MCP Server for Unity Editor with execute_code, prompts/resources, input simulation, screenshots, and play mode automation.

3004. **[gemini-cloud-assist-mcp](https://github.com/GoogleCloudPlatform/gemini-cloud-assist-mcp)** - ⭐ 52
   An MCP Server for Gemini Cloud Assist; provides tools to assist with your tasks on GCP

3005. **[omnifocus-mcp-enhanced](https://github.com/jqlts1/omnifocus-mcp-enhanced)** - ⭐ 52
   Enhanced Model Context Protocol (MCP) server for OmniFocus with complete subtask support, perspective views (Inbox/Flagged/Forecast/Tags), ultimate   task filtering, and direct access to custom perspectives. Seamlessly integrate OmniFocus with Claude AI for intelligent task management.

3006. **[baba_is_eval](https://github.com/lennart-finke/baba_is_eval)** - ⭐ 52
   Claude  et al. play the brilliant puzzle title "Baba is You"

3007. **[gomcp](https://github.com/llmcontext/gomcp)** - ⭐ 52
   Unofficial Golang SDK for Anthropic Model Context Protocol

3008. **[paraview_mcp](https://github.com/llnl/paraview_mcp)** - ⭐ 52
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

3009. **[mcpx](https://github.com/lydakis/mcpx)** - ⭐ 52
   Turn MCP servers into composable CLIs.

3010. **[mcp-android-server-python](https://github.com/nim444/mcp-android-server-python)** - ⭐ 52
   MCP Android agent - This project provides an *MCP (Model Context Protocol)* server for automating Android devices using uiautomator2. It's designed to be easily plugged into AI agents like GitHub Copilot Chat, Claude, or Open Interpreter to control Android devices through natural language.

3011. **[Generative-UI-MCP](https://github.com/op7418/Generative-UI-MCP)** - ⭐ 52
   MCP server that teaches AI models to generate interactive visualizations — charts, diagrams, mockups, and more.

3012. **[MCPwner](https://github.com/Pigyon/MCPwner)** - ⭐ 52
   Model Context Protocol server for autonomous vulnerability discovery

3013. **[A2A_ADK_MCP](https://github.com/RubensZimbres/A2A_ADK_MCP)** - ⭐ 52
   Multi-Agent Systems with Google's Agent Development Kit + A2A + MCP

3014. **[us-census-bureau-data-api-mcp](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp)** - ⭐ 52
   The U.S. Census Bureau Data API MCP connects AI Assistants with official Census Bureau statistics.

3015. **[mcp-victorialogs](https://github.com/VictoriaMetrics-Community/mcp-victorialogs)** - ⭐ 52
   The implementation of Model Context Protocol (MCP) server for VictoriaLogs.

3016. **[codex-mcp-go](https://github.com/w31r4/codex-mcp-go)** - ⭐ 52
   codex-mcp-go is a Go-based MCP (Model Context Protocol) server that serves as a bridge for Codex CLI, enabling various AI coding assistants (such as Claude Code, Roo Code, KiloCode, etc.) to seamlessly collaborate with Codex.

3017. **[deepseek-mcp](https://github.com/arizen-dev/deepseek-mcp)** - ⭐ 51
   A tiny MCP stdio server that exposes DeepSeek as a cheap supervised worker for Claude Code, Codex, or any MCP client.

3018. **[whois-mcp](https://github.com/bharathvaj-ganesan/whois-mcp)** - ⭐ 51
   MCP Server for whois lookups.

3019. **[ShadowCrawl](https://github.com/DevsHero/ShadowCrawl)** - ⭐ 51
   🥷 The FREE, Sovereign alternative to Firecrawl & Tavily. Pure Rust Stealth Scraper + Built-in God-Tier Meta-Search for AI Agents. Bypass Cloudflare & DataDome via HITL. Zero-bloat, ultra-clean LLM data. 99.99% Success Rate. 🦀

3020. **[mcp-domain-availability](https://github.com/imprvhub/mcp-domain-availability)** - ⭐ 51
   A Model Context Protocol (MCP) server that enables Claude Desktop to check domain availability across 50+ TLDs. Features DNS/WHOIS verification, bulk checking, and smart suggestions. Zero-clone installation via uvx.

3021. **[gomcp](https://github.com/localrivet/gomcp)** - ⭐ 51
   gomcp provides a Go implementation of the Model Context Protocol (MCP), enabling communication between language models/agents and external tools or resources via a standardized protocol.

3022. **[mcp-atlassian-server](https://github.com/phuc-nt/mcp-atlassian-server)** - ⭐ 51
   MCP server connecting AI assistants with Jira & Confluence for smart project management.

3023. **[mcp-app-demo](https://github.com/pomerium/mcp-app-demo)** - ⭐ 51
   Demo application showcasing how to build and secure MCP servers and clients with Pomerium using contextual access policies.

3024. **[mcp-filter](https://github.com/pro-vi/mcp-filter)** - ⭐ 51
   A proxy MCP (Model Context Protocol) server that filters the upstream tool surface to just the tools you need.

3025. **[hmr](https://github.com/promplate/hmr)** - ⭐ 51
   Real hot-module reload for Python—side effects handled reactively. https://py3.online/hmr

3026. **[mcp-client](https://github.com/rakesh-eltropy/mcp-client)** - ⭐ 51

3027. **[notebooklm-mcp](https://github.com/roomi-fields/notebooklm-mcp)** - ⭐ 51
   MCP server for NotebookLM - Let your AI agents (Claude Code, Codex) research documentation directly with grounded, citation-backed answers from Gemini. Persistent auth, library management, cross-client sharing. Zero hallucinations, just your knowledge base.

3028. **[mcp-front](https://github.com/stainless-api/mcp-front)** - ⭐ 51
   Auth proxy for Model Context Protocol servers - adds authentication to MCP tools for Claude.ai, Claude Code, Cursor, Gemini

3029. **[matlab-mcp-server](https://github.com/subspace-lab/matlab-mcp-server)** - ⭐ 51
   Matlab MCP Server in python

3030. **[kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server)** - ⭐ 51
   A Model Context Protocol (MCP) server for Apache Kafka implemented in Go, leveraging franz-go and mcp-go.

3031. **[vchart-mcp-server](https://github.com/VisActor/vchart-mcp-server)** - ⭐ 51
   A Model Context Protocol (MCP) server for the @visactor/vchart that enables AI assistants to generate interactive charts and visualizations.

3032. **[gdal-mcp](https://github.com/Wayfinder-Foundry/gdal-mcp)** - ⭐ 51
   Model Context Protocol server that packages GDAL-style geospatial workflows through Python-native libraries (Rasterio, GeoPandas, PyProj, etc.) to give AI agents catalog discovery, metadata intelligence, and raster/vector processing with built-in reasoning guidance and reference resources.

3033. **[1xn-vmcp](https://github.com/1xn-labs/1xn-vmcp)** - ⭐ 50
   vMCP - Virtual Model Context Protocol

3034. **[mcp-youtube](https://github.com/adhikasp/mcp-youtube)** - ⭐ 50
   Model Context Protocol to fetch youtube transcript

3035. **[awesome-mcp-security](https://github.com/AIM-Intelligence/awesome-mcp-security)** - ⭐ 50
   Security Threats related with MCP (Model Context Protocol), MCP Servers and more

3036. **[xhs-mcp](https://github.com/Algovate/xhs-mcp)** - ⭐ 50
   用于小红书（xiaohongshu.com）的 Model Context Protocol（MCP）服务器与 CLI 工具，支持登录、发布、搜索、推荐等自动化能力

3037. **[Perigon.CLI](https://github.com/AterDev/Perigon.CLI)** - ⭐ 50
   This is a tool that helps you quickly build backend services based on Asp.Net Core and EF Core. It provides command line, WebUI and IDE MCP support. In a well-designed project architecture that has been put into practice, code generation and LLM technology are used to reduce various template codes and greatly improve development efficiency!

3038. **[sample-agentic-ai-web](https://github.com/aws-samples/sample-agentic-ai-web)** - ⭐ 50
   This project demonstrates how to use AWS Bedrock with Anthropic Claude and Amazon Nova models to create a web automation assistant with tool use, human-in-the-loop interaction, and vision capabilities.

3039. **[mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers)** - ⭐ 50
   🔒 Reference MCP servers that demo how authentication works with the current Model Context Protocol spec.

3040. **[mcp-tts](https://github.com/blacktop/mcp-tts)** - ⭐ 50
   MCP Server for Text to Speech

3041. **[civyk-winwright](https://github.com/civyk-official/civyk-winwright)** - ⭐ 50
   Playwright-style MCP server for Windows desktop, system, and browser automation. 59 tools for WPF, WinForms, Win32, Chrome/Edge via Model Context Protocol.

3042. **[coddy-agent](https://github.com/coddy-project/coddy-agent)** - ⭐ 50
   Open-source distroless harness coding agent in Go. Has embedded WebUI. Works with any IDE via ACP and with OpenAI clients via OpenAI-compatible REST API. Supports any OpenAI-compatible providers. Can use SKILLS and MCP servers.

3043. **[VS-MCPServer](https://github.com/CodingWithCalvin/VS-MCPServer)** - ⭐ 50
   VS MCP Server exposes Visual Studio features through the Model Context Protocol (MCP), enabling AI assistants like Claude to interact with your IDE programmatically. Open files, read code, build projects, and more - all through natural conversation!

3044. **[modular-mcp](https://github.com/d-kimuson/modular-mcp)** - ⭐ 50
   A Model Context Protocol (MCP) proxy server that enables efficient management of large tool collections across multiple MCP servers by grouping them and loading tool schemas on-demand.

3045. **[model-context-protocol-rb](https://github.com/dickdavis/model-context-protocol-rb)** - ⭐ 50
   An implementation of the Model Context Protocol in Ruby.

3046. **[octave-mcp](https://github.com/elevanaltd/octave-mcp)** - ⭐ 50
   OCTAVE protocol - structured AI communication with 3-20x token reduction. MCP server with lenient-to-canonical pipeline and schema validation.

3047. **[mcpo_docker_use](https://github.com/flyfox666/mcpo_docker_use)** - ⭐ 50
   An example Docker image for mcpo（with npm,curl,nodejs,uv Pre-Built;Pre-Built MCP:amap;baidumap;server-brave-search; tavily;fetch）, a tool that exposes MCP (Model Context Protocol) servers as OpenAPI-compatible HTTP endpoints for OpenWebUI.

3048. **[mcp](https://github.com/goplus/mcp)** - ⭐ 50
   A XGo implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

3049. **[meme-mcp](https://github.com/haltakov/meme-mcp)** - ⭐ 50
   A simple Model Context Protocol (MCP) server for generating memes using the ImgFlip API

3050. **[awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins)** - ⭐ 50
   A curated list of awesome plugins for AI assistants including Claude Code, OpenAI Codex, Gemini, OpenCode and More.

3051. **[kimi-code-mcp](https://github.com/howardpen9/kimi-code-mcp)** - ⭐ 50
   MCP server for Claude Code × Kimi K2.5 (256K context) — delegate bulk codebase analysis to Kimi, save 90% on token costs. Session caching, parallel agents, TypeScript.

3052. **[mcp_weather_server](https://github.com/isdaniel/mcp_weather_server)** - ⭐ 50
   A Model Context Protocol (MCP) server that provides weather information using the Open-Meteo API.

3053. **[gimp-mcp](https://github.com/maorcc/gimp-mcp)** - ⭐ 50
   GIMP MCP server

3054. **[mcp-codebase-index](https://github.com/MikeRecognex/mcp-codebase-index)** - ⭐ 50
   17 MCP query tools for codebase navigation — functions, classes, imports, dependency graphs, change impact. Zero dependencies. 87% token reduction.

3055. **[ScreenPilot](https://github.com/Mtehabsim/ScreenPilot)** - ⭐ 50
   Tool that allows the AI to control your device in the same way you do, enabling automation for everything!

3056. **[mcp-server-drupal](https://github.com/Omedia/mcp-server-drupal)** - ⭐ 50
   TS based companion MCP server for the Drupal MCP module that works with the STDIO transport.

3057. **[illustrator-mcp-server](https://github.com/spencerhhubert/illustrator-mcp-server)** - ⭐ 50
   mcp server to run scripts on adobe illustrator

3058. **[ScreenshotMCP](https://github.com/upnorthmedia/ScreenshotMCP)** - ⭐ 50
   A Model Context Protocol MCP server for capturing website screenshots with full page, element, and device size features.

3059. **[openrouter-deep-research-mcp](https://github.com/wheattoast11/openrouter-deep-research-mcp)** - ⭐ 50
   A multi-agent research MCP server + mini client adapter - orchestrates a net of async agents or streaming swarm to conduct ensemble consensus-backed research. Each task builds its own indexed pglite database on the fly in web assembly. Includes semantic + hybrid search, SQL execution, semaphores, prompts/resources and more

3060. **[pprof-analyzer-mcp](https://github.com/ZephyrDeng/pprof-analyzer-mcp)** - ⭐ 50
   This is a Model Context Protocol (MCP) server implemented in Go, providing a tool to analyze Go pprof performance profiles.

3061. **[create-mcp](https://github.com/zueai/create-mcp)** - ⭐ 50
   CLI to set up and deploy MCP Servers to Cloudflare Workers in seconds. Just write TypeScript functions to make Cursor MCP tools.

3062. **[shadowgit-mcp](https://github.com/aflsolutions/shadowgit-mcp)** - ⭐ 49
   A Model Context Protocol (MCP) server that provides AI assistants with secure, read-only access to your ShadowGit repositories. This enables powerful debugging and code analysis capabilities by giving AI access to your project's fine-grained git history.

3063. **[dotbot](https://github.com/andresharpe/dotbot)** - ⭐ 49
   Structured, auditable AI-assisted development for teams. Zero-dependency MCP server, web dashboard, and multi-provider AI CLI support.

3064. **[kirby-mcp](https://github.com/bnomei/kirby-mcp)** - ⭐ 49
   CLI-first MCP server for composer-based Kirby CMS projects — inspect blueprints/templates/plugins, interact with a real Kirby runtime, and use a bundled Kirby knowledge base.

3065. **[evernote-mcp-server](https://github.com/brentmid/evernote-mcp-server)** - ⭐ 49
   Evernote MCP server - allows LLMs that support MCP (like Claude Desktop) to query your notes in Evernote

3066. **[mcp_server_notify](https://github.com/Cactusinhand/mcp_server_notify)** - ⭐ 49
   Send system notification when Agent task is done.

3067. **[lisply-mcp](https://github.com/gornskew/lisply-mcp)** - ⭐ 49
   Model Context Protocol (MCP) server to manage and talk to compliant "Lisply" lisp-speaking backend services

3068. **[TalkToFigmaDesktop](https://github.com/grab/TalkToFigmaDesktop)** - ⭐ 49
   A powerful desktop application bridging Figma and AI tools via Model Context Protocol Seamless integration between Figma designs and AI assistants

3069. **[langchain-mcp-client](https://github.com/guinacio/langchain-mcp-client)** - ⭐ 49
   This Streamlit application provides a user interface for connecting to MCP (Model Context Protocol) servers and interacting with them using different LLM providers (OpenAI, Anthropic, Google, Ollama).

3070. **[langchaingo-mcp-adapter](https://github.com/i2y/langchaingo-mcp-adapter)** - ⭐ 49
   A Go adapter that bridges LangChain Go tools with Model Context Protocol (MCP) servers.

3071. **[n8n-workflow-builder-mcp](https://github.com/ifmelate/n8n-workflow-builder-mcp)** - ⭐ 49
   MCP server that allow LLM in agent mode builds n8n workflows for you

3072. **[gtm-mcp](https://github.com/impecablemee/gtm-mcp)** - ⭐ 49
   MCP server for B2B cold outreach — find companies via Apollo, verify with AI, push to SmartLead & GetSales. 49    tools. Works with Claude Code or any MCP client

3073. **[agent-os](https://github.com/imran-siddique/agent-os)** - ⭐ 49
   A Safety-First Kernel for Autonomous AI Agents - POSIX-inspired primitives with 0% policy violation guarantee

3074. **[vercel-ai-docs-mcp](https://github.com/IvanAmador/vercel-ai-docs-mcp)** - ⭐ 49
   A Model Context Protocol (MCP) server that provides AI-powered search and querying capabilities for the Vercel AI SDK documentation. This project enables developers to ask questions about the Vercel AI SDK and receive accurate, contextualized responses based on the official documentation.

3075. **[mcp-client-demo](https://github.com/KelvinQiu802/mcp-client-demo)** - ⭐ 49

3076. **[MCP-Scanner](https://github.com/knostic/MCP-Scanner)** - ⭐ 49
   Advanced Shodan-based scanner for discovering, verifying, and enumerating Model Context Protocol (MCP) servers and AI infrastructure tools over HTTP & SSE.

3077. **[amazon_ads_mcp](https://github.com/KuudoAI/amazon_ads_mcp)** - ⭐ 49
   Amazon Ads MCP - Model Context Protocol server for Amazon Advertising API

3078. **[image-gen-mcp](https://github.com/lansespirit/image-gen-mcp)** - ⭐ 49
   An MCP server that integrates with gpt-image-1 & Gemini imagen4 model for text-to-image generation services

3079. **[mcp-server-ledger](https://github.com/minhyeoky/mcp-server-ledger)** - ⭐ 49
   A Model Context Protocol server for interacting with Ledger CLI, a powerful double-entry accounting system. This server enables Large Language Models to query and analyze financial data through a standardized interface, making it easy for AI assistants to help with financial reporting, budget analysis, and accounting tasks.

3080. **[arch-mcp](https://github.com/nihalxkumar/arch-mcp)** - ⭐ 49
   Arch Linux MCP (Model Context Protocol) Server

3081. **[oatpp-mcp](https://github.com/oatpp/oatpp-mcp)** - ⭐ 49
   Anthropic’s Model Context Protocol implementation for Oat++

3082. **[zig-mcp-server](https://github.com/openSVM/zig-mcp-server)** - ⭐ 49
   A Model Context Protocol (MCP) server that provides Zig language tooling, code analysis, and documentation access. This server enhances AI capabilities with Zig-specific functionality including code optimization, compute unit estimation, code generation, and best practices recommendations.

3083. **[linux-do-mcp](https://github.com/Pleasurecruise/linux-do-mcp)** - ⭐ 49
   A MCP Server For LINUX DO community

3084. **[mcp-ai-memory](https://github.com/scanadi/mcp-ai-memory)** - ⭐ 49
   A production-ready Model Context Protocol (MCP) server for semantic memory management

3085. **[NepseAPI-Unofficial](https://github.com/surajrimal07/NepseAPI-Unofficial)** - ⭐ 49
   Unlock Nepal Stock Exchange (NEPSE) data with this powerful unofficial API. Features REST, WebSocket, and a first-of-its-kind Model Context Protocol (MCP) server, enabling AI models like Claude to perform live market analysis with over 20 specialized tools. Strictly for educational and non-commercial use.

3086. **[MCPApp](https://github.com/tanaikech/MCPApp)** - ⭐ 49
   This text introduces the Model Context Protocol (MCP) for AI interaction, exploring Google Apps Script (GAS) as a server option. It shows feasibility with a sample but notes the lack of a GAS SDK, aiming to encourage understanding and development.

3087. **[cinema4d-mcp](https://github.com/ttiimmaacc/cinema4d-mcp)** - ⭐ 49
   Cinema 4D plugin integrating Claude AI for prompt-driven 3D modeling, scene creation, and manipulation.

3088. **[any2markdown](https://github.com/WW-AI-Lab/any2markdown)** - ⭐ 49
   一个高性能的文档转换服务器，同时支持 Model Context Protocol (MCP) 和 RESTful API 接口。将 PDF、Word 和 Excel 文档转换为 Markdown 格式，具备图片提取、页眉页脚移除和批量处理等高级功能

3089. **[SUMO-MCP-Server](https://github.com/XRDS76354/SUMO-MCP-Server)** - ⭐ 49
   SUMO-MCP 是一个连接大语言模型 (LLM) 与 Eclipse SUMO 交通仿真的中间件。通过 Model Context Protocol (MCP)，它允许 AI 智能体（如 Claude, Cursor, TRAE等）直接调用 SUMO 的核心功能，实现从OpenStreetMap 数据获取、路网生成、需求建模到仿真运行与信号优化的全流程自动化。

3090. **[mcp-gitlab-server](https://github.com/yoda-digital/mcp-gitlab-server)** - ⭐ 49
   Production-grade GitLab MCP server with 86 tools — full GitLab control from any AI agent (Claude, Cursor, Zed).

3091. **[Wwise-MCP](https://github.com/BilkentAudio/Wwise-MCP)** - ⭐ 48
   Wwise-MCP is a Model Context Protocol (MCP) server that enables large language models (LLMs) to interact with the Wwise Authoring application. It exposes a set of tools built on a custom Python WAAPI library, allowing MCP clients such as Claude or Cursor to automate and compose complex, multi-step Wwise workflows.

3092. **[shadowgit-mcp](https://github.com/blade47/shadowgit-mcp)** - ⭐ 48
   A Model Context Protocol (MCP) server that provides AI assistants with secure, read-only access to your ShadowGit repositories. This enables powerful debugging and code analysis capabilities by giving AI access to your project's fine-grained git history.

3093. **[bonnard-cli](https://github.com/bonnard-data/bonnard-cli)** - ⭐ 48
   Open-source agentic schema CLI. Optimised for claude code, gemini, codex and co-pilot. Skills included.

3094. **[buildkite-mcp-server](https://github.com/buildkite/buildkite-mcp-server)** - ⭐ 48
   Official MCP Server for Buildkite.

3095. **[Go-High-Level-MCP-2026-Complete](https://github.com/BusyBee3333/Go-High-Level-MCP-2026-Complete)** - ⭐ 48
   GoHighLevel MCP Server — 520+ tools across 40 categories. Voice AI, Proposals, Contacts, Calendars, Conversations, Opportunities, Invoices, Payments, Workflows, Social Media, and more. MCP SDK 1.26, Streamable HTTP, tool annotations.

3096. **[mcp-lite-dev](https://github.com/datawhalechina/mcp-lite-dev)** - ⭐ 48
   共学《MCP极简开发》项目代码

3097. **[linkedin-mcp-server](https://github.com/Dishant27/linkedin-mcp-server)** - ⭐ 48
   Model Context Protocol (MCP) server for LinkedIn API integration

3098. **[mcp-metabase-server](https://github.com/easecloudio/mcp-metabase-server)** - ⭐ 48
   A comprehensive MCP server for Metabase with 70+ tools.

3099. **[sharedcontext](https://github.com/Eversmile12/sharedcontext)** - ⭐ 48
   MCP server that gives AI coding assistants persistent cross-client memory. Facts and conversations stored in SQLite, encrypted with AES-256-GCM, synced to Arweave. No server, no account, recoverable with a 12-word phrase.

3100. **[mcp-openapi-schema](https://github.com/hannesj/mcp-openapi-schema)** - ⭐ 48
   OpenAPI Schema Model Context Protocol Server

3101. **[Homeassistant-server-mcp](https://github.com/hekmon8/Homeassistant-server-mcp)** - ⭐ 48
   A Model Context Protocol (MCP) server for interacting with Home Assistant. This server provides tools to control and monitor your Home Assistant devices through MCP-enabled applications.

3102. **[advanced-homeassistant-mcp](https://github.com/jango-blockchained/advanced-homeassistant-mcp)** - ⭐ 48
   An advanced MCP server for Home Assistant. 🔋 Batteries included.

3103. **[globalping-mcp-server](https://github.com/jsdelivr/globalping-mcp-server)** - ⭐ 48
   Remote MCP server that gives LLMs access to run network commands

3104. **[lakevision](https://github.com/lakevision-project/lakevision)** - ⭐ 48
   Lakevision is a tool which provides insights into your Apache Iceberg based Data Lakehouse.

3105. **[codex-specialized-subagents](https://github.com/leonardsellem/codex-specialized-subagents)** - ⭐ 48
   MCP server that lets Codex delegate to isolated codex exec sub-agents, selecting repo+global skills automatically

3106. **[predictive-maintenance-mcp](https://github.com/LGDiMaggio/predictive-maintenance-mcp)** - ⭐ 48
   AI-Powered Predictive Maintenance & Fault Diagnosis through Model Context Protocol. An open-source framework for integrating Large Language Models with predictive maintenance and fault diagnosis workflows.

3107. **[js](https://github.com/mcp-auth/js)** - ⭐ 48
   🔐 Plug-and-play auth for Node.js MCP servers.

3108. **[synapse-ai](https://github.com/naveenraj-17/synapse-ai)** - ⭐ 48
   Build AI agents that actually do things. Synapse is an open-source platform for creating, connecting, and orchestrating AI agents powered by any LLM — local, cloud or CLIs.

3109. **[claude-mcp-setup](https://github.com/patruff/claude-mcp-setup)** - ⭐ 48
   Easy setup script for Anthropic Claude Model Context Protocol (MCP) servers on Windows

3110. **[mcp-server-weibo](https://github.com/qinyuanpei/mcp-server-weibo)** - ⭐ 48
   基于 Model Context Protocol 的微博数据接口服务器 - 实时获取微博用户信息、动态内容、热搜榜单、粉丝关注数据。支持用户搜索、内容搜索、话题分析，为 AI 应用提供完整的微博数据接入方案。

3111. **[mcp-mail](https://github.com/shuakami/mcp-mail)** - ⭐ 48
   📧 MCP Mail Tool - AI-powered email management tool | 基于 MCP 的智能邮件管理工具

3112. **[mcp-server-chart-minio](https://github.com/zaizaizhao/mcp-server-chart-minio)** - ⭐ 48
   mcp-server-chart私有化部署方案

3113. **[mcp-zen](https://github.com/199-mcp/mcp-zen)** - ⭐ 47
   Enhanced Zen MCP Server with 'zen' default tool and improvements

3114. **[yahoo-finance-server](https://github.com/AgentX-ai/yahoo-finance-server)** - ⭐ 47
   A Model Context Protocol (MCP) server that lets your AI interact with Yahoo Finance to get comprehensive stock market data, news, financials, and more

3115. **[world_bank_mcp_server](https://github.com/anshumax/world_bank_mcp_server)** - ⭐ 47
   An implementation of the Model Context Protocol for the World Bank open data API

3116. **[VSCode-Perplexity-MCP](https://github.com/Automations-Project/VSCode-Perplexity-MCP)** - ⭐ 47
   Perplexity AI search, reasoning, research, and compute - MCP server, dashboard, and multi-IDE auto-config for VS Code.

3117. **[mcp-container-ts](https://github.com/Azure-Samples/mcp-container-ts)** - ⭐ 47
   This is a quick start guide that provides the basic building blocks to set up a remote Model Context Protocol (MCP) server using Azure Container Apps. The MCP server is built using Node.js and TypeScript, and it can be used to run various tools and services in a serverless environment.

3118. **[gnome-mcp-server](https://github.com/bilelmoussaoui/gnome-mcp-server)** - ⭐ 47
   Grant the AI octopus access to a portion of your desktop

3119. **[auto-MCP-client](https://github.com/Chen-speculation/auto-MCP-client)** - ⭐ 47
   A Go library implementation of the Model Controller Protocol (MCP). This library allows developers to easily parse MCP service configurations, generate corresponding MCP clients, and integrate them as callable tools within LLM agent systems. Focuses on providing reusable Go packages for building MCP-enabled applications.

3120. **[ai-software-architect](https://github.com/codenamev/ai-software-architect)** - ⭐ 47
   AI-powered architecture documentation framework with ADRs, reviews, and pragmatic mode. Now available as Claude Code Plugin for easiest installation.

3121. **[hop](https://github.com/danmartuszewski/hop)** - ⭐ 47
   Fast, elegant SSH connection manager with a TUI dashboard and MCP server

3122. **[dremio-mcp](https://github.com/dremio/dremio-mcp)** - ⭐ 47
   Dremio MCP server

3123. **[spec-coding-mcp](https://github.com/feiyun0112/spec-coding-mcp)** - ⭐ 47
   Transform feature ideas into production-ready code through systematic Spec-Driven Development 通过系统化的**规格驱动开发**，将功能想法转化为可投入生产的代码

3124. **[Dragon-Brain](https://github.com/iikarus/Dragon-Brain)** - ⭐ 47
   Dragon Brain — persistent long-term memory for AI agents via MCP (Model Context Protocol). Knowledge graph (FalkorDB) + vector search (Qdrant) + CUDA GPU embeddings. Works with Claude, Gemini CLI, Cursor, Windsurf, VS Code Copilot. 30 tools, 1121 tests.

3125. **[kuon](https://github.com/lissettecarlr/kuon)** - ⭐ 47
   久远：一个开发中的大模型语音助手，当前关注易用性，简单上手，支持对话选择性记忆和Model Context Protocol (MCP)服务。 KUON:A large language model-based voice assistant under development, currently focused on ease of use and simple onboarding. It supports selective memory in conversations and the Model Context Protocol (MCP) service.

3126. **[mcp-workspace](https://github.com/MarcusJellinghaus/mcp-workspace)** - ⭐ 47
   MCP Workspace Server: A secure Model Context Protocol server providing file, git, and GitHub tools for AI assistants within a sandboxed project directory.

3127. **[Serper-search-mcp](https://github.com/NightTrek/Serper-search-mcp)** - ⭐ 47
   Un-official Serper Google search server for Cline and other MCP clients

3128. **[Reversecore_MCP](https://github.com/sjkim1127/Reversecore_MCP)** - ⭐ 47
   A security-first MCP server empowering AI agents to orchestrate Ghidra, Radare2, and YARA for automated reverse engineering.

3129. **[MDB-MCP](https://github.com/smadi0x86/MDB-MCP)** - ⭐ 47
   Multi Debugger MCP server that enables LLMs to interact with GDB and LLDB for binary debugging and analysis.

3130. **[flightradar24-mcp-server](https://github.com/sunsetcoder/flightradar24-mcp-server)** - ⭐ 47
   Model Context Protocol server for Flight Tracking

3131. **[sverklo](https://github.com/sverklo/sverklo)** - ⭐ 47
   Local-first code intelligence — MCP server for Claude Code, Cursor, Windsurf, Zed. Symbol graph, blast-radius, git-pinned memory. 43× fewer tokens than naive grep. MIT, zero-config.

3132. **[tomtom-maps-mcp](https://github.com/tomtom-international/tomtom-maps-mcp)** - ⭐ 47
   A Model Context Protocol (MCP) server providing TomTom's location services, search, routing, and traffic data to AI agents.

3133. **[MCP-Trust-Kit](https://github.com/aak204/MCP-Trust-Kit)** - ⭐ 46
   Deterministic CI scanner and surface-risk scoring for MCP (Model Context Protocol) servers.

3134. **[nuclei-mcp](https://github.com/addcontent/nuclei-mcp)** - ⭐ 46
   An implementation of a Model Context Protocol (MCP) for the Nuclei scanner. This tool enables context-aware vulnerability scanning by intelligently providing models and context to the scanning engine, allowing for more efficient and targeted template execution

3135. **[devcontext](https://github.com/aiurda/devcontext)** - ⭐ 46
   DevContext is a cutting-edge Model Context Protocol (MCP) server designed to provide developers with continuous, project-centric context awareness. Unlike traditional context systems, DevContext continuously learns from and adapts to your development patterns and delivers highly relevant context providing a deeper understanding of your codebase.

3136. **[binance-mcp-server](https://github.com/AnalyticAce/binance-mcp-server)** - ⭐ 46
   Unofficial tools and server implementation for Binance's Model Context Protocol (MCP). Designed to support developers building crypto trading  AI Agents.

3137. **[mcp-sitecore-server](https://github.com/Antonytm/mcp-sitecore-server)** - ⭐ 46
   Model Context Protocol server for Sitecore

3138. **[claude-additional-models-mcp](https://github.com/Arkya-AI/claude-additional-models-mcp)** - ⭐ 46
   Reduce Claude Desktop consumption by 10x - Integrate Google's Gemini or Z.ai's GLM-5 (744B params) with Claude via MCP for intelligent task delegation

3139. **[open-ghl-mcp](https://github.com/basicmachines-co/open-ghl-mcp)** - ⭐ 46
   An open source Model Context Protocol server for GoHighLevel API v2 with OAuth

3140. **[MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API)** - ⭐ 46
   ⚡ Control Apache Airflow with natural language via MCP. Chat with your workflows using Claude, GPT, or any LLM — no REST API calls needed. Supports Airflow 2.x (43 tools) & 3.0+ (45+ tools).

3141. **[mcp-made-simple](https://github.com/chongdashu/mcp-made-simple)** - ⭐ 46
   Model Context Protocol (MCP) Made Simple - Code for the tutorial series - focusing on practical ways to understand and use MCP

3142. **[claude-mcp](https://github.com/cnych/claude-mcp)** - ⭐ 46
   Claude Unified Model Context Interaction Protocol

3143. **[lighthouse-mcp-server](https://github.com/danielsogl/lighthouse-mcp-server)** - ⭐ 46
   MCP server that enables AI agents to perform comprehensive web audits using Google Lighthouse with 13+ tools for performance, accessibility, SEO, and security analysis.

3144. **[Readwise-Reader-MCP](https://github.com/edricgsh/Readwise-Reader-MCP)** - ⭐ 46
   A Model Context Protocol (MCP) server for the Readwise Reader API, built with TypeScript and the official Claude SDK.

3145. **[Aspire.MCP.Sample](https://github.com/elbruno/Aspire.MCP.Sample)** - ⭐ 46
   Sample MCP Server and MCP client with Aspire

3146. **[dataproduct-mcp](https://github.com/entropy-data/dataproduct-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) server for discovering data products and requesting access in Data Mesh Manager, and executing queries on the data platform to access business data.

3147. **[mcp-graphql-schema](https://github.com/hannesj/mcp-graphql-schema)** - ⭐ 46
   GraphQL Schema Model Context Protocol Server

3148. **[inAI-wiki](https://github.com/inai-sandy/inAI-wiki)** - ⭐ 46
   🌍 The open-source Wikipedia of AI — 2M+ apps, agents, LLMs & datasets. Updated daily with tools, tutorials & news.

3149. **[AgentDNS-Node](https://github.com/jsjfai/AgentDNS-Node)** - ⭐ 46
   AgentDNS·Node makes it easy to manage and scale multiple MCP (Model Context Protocol) servers by organizing them into flexible Streamable HTTP (SSE) endpoints—supporting access to all servers, individual servers, or logical server groups.

3150. **[fast-mcp-telegram](https://github.com/leshchenko1979/fast-mcp-telegram)** - ⭐ 46
   MCP/HTTP Telegram Gateway — Multi-tenant, MTProto User API, 8 tools, multi-user Bearer auth, global search, session ACL, Docker

3151. **[Claude-Project-Coordinator](https://github.com/M-Pineapple/Claude-Project-Coordinator)** - ⭐ 46
   Claude Project Coordinator is a Swift-powered MCP (Model Context Protocol) server designed to streamline multi-project Xcode development. It lets you track project status, auto-detect frameworks, search code patterns, and maintain a structured development knowledge base — all locally, with Claude Desktop as your assistant.

3152. **[mcpcat-python-sdk](https://github.com/MCPCat/mcpcat-python-sdk)** - ⭐ 46
   MCPcat is an analytics platform for MCP server owners 🐱.

3153. **[agentic-tools](https://github.com/meta-quest/agentic-tools)** - ⭐ 46
   Agent Tool and Skills for VR Development on Meta Quest

3154. **[mcp_demo](https://github.com/Ming-jiayou/mcp_demo)** - ⭐ 46
   A simple example of building an MCP client using C#.

3155. **[RevitMCP](https://github.com/oakplank/RevitMCP)** - ⭐ 46
   model context protocol for Autodesk Revit

3156. **[beemcp](https://github.com/OkGoDoIt/beemcp)** - ⭐ 46
   BeeMCP: an unofficial Model Context Protocol (MCP) server that connects your Bee wearable lifelogger to AI via the Model Context Protocol

3157. **[ckan-mcp-server](https://github.com/ondata/ckan-mcp-server)** - ⭐ 46
   MCP server for querying CKAN open data portals (package search, DataStore SQL, organizations, groups, tags)

3158. **[mcp_server](https://github.com/peppemas/mcp_server)** - ⭐ 46
   A C++ implementation of a Model Context Protocol Server with a pluggable module architecture.

3159. **[PixVerse-MCP](https://github.com/PixVerseAI/PixVerse-MCP)** - ⭐ 46
   Official PixVerse Model Context Protocol (MCP) server that enables interaction with powerful AI video generation APIs.

3160. **[pentestMCP](https://github.com/ramkansal/pentestMCP)** - ⭐ 46
   pentestMCP: AI-Powered Penetration Testing via MCP, an MCP designed for penetration testers.

3161. **[pdf-mcp](https://github.com/saury1120/pdf-mcp)** - ⭐ 46
   一个强大的 PDF 处理 MCP（Model Context Protocol）服务，提供全面的 PDF 文档分析功能

3162. **[mcp-nats](https://github.com/sinadarbouy/mcp-nats)** - ⭐ 46
   A Model Context Protocol (MCP) server for NATS messaging system integration

3163. **[steel-mcp-server](https://github.com/steel-dev/steel-mcp-server)** - ⭐ 46
   MCP Server for interacting with a Steel web browser

3164. **[mcp-starter-template](https://github.com/StevenStavrakis/mcp-starter-template)** - ⭐ 46
   An opinionated starter template for making Model Context Protocol (MCP) servers

3165. **[thingspanel-mcp](https://github.com/ThingsPanel/thingspanel-mcp)** - ⭐ 46
   This MCP server integrates ThingsPanel IoT platform with AI models like Claude, GPT, and others that support the Model Context Protocol.

3166. **[tiger-slack](https://github.com/timescale/tiger-slack)** - ⭐ 46
   Real-time Slack ingest and MCP server to power your agentic Slack bots

3167. **[tomtom-mcp](https://github.com/tomtom-international/tomtom-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) server providing TomTom's location services, search, routing, and traffic data to AI agents.

3168. **[beanquery-mcp](https://github.com/vanto/beanquery-mcp)** - ⭐ 46
   Beancount MCP Server is an experimental implementation that utilizes the Model Context Protocol (MCP) to enable AI assistants to query and analyze Beancount ledger files using Beancount Query Language (BQL) and the beanquery tool.

3169. **[mcp-sync](https://github.com/ztripez/mcp-sync)** - ⭐ 46
   Sync MCP (Model Context Protocol) configurations across AI tools

3170. **[mcp-wikidata](https://github.com/zzaebok/mcp-wikidata)** - ⭐ 46
   A server implementation for Wikidata API using the Model Context Protocol (MCP).

3171. **[mcp-yfinance-server](https://github.com/Adity-star/mcp-yfinance-server)** - ⭐ 45
   Real-time stock API with Python, MCP server example, yfinance stock analysis dashboard

3172. **[arifos](https://github.com/ariffazil/arifos)** - ⭐ 45
   arifOS — Constitutional MCP kernel for governed AI execution. AAA trinity: AGI (Mind) · ASI (Heart) · APEX (Judge). Built for the sovereign agentic era.

3173. **[instagram-engagement-mcp](https://github.com/Bob-lance/instagram-engagement-mcp)** - ⭐ 45
   📢 Instagram MCP Server – A powerful Model Context Protocol (MCP) server for tracking Instagram engagement, generating leads, and analyzing audience feedback.

3174. **[kanban-mcp](https://github.com/bradrisse/kanban-mcp)** - ⭐ 45
   MCP Kanban is a specialized middleware designed to facilitate interaction between Large Language Models (LLMs) and Planka, a Kanban board application. It serves as an intermediary layer that provides LLMs with a simplified and enhanced API to interact with Planka's task management system.

3175. **[keycloak-model-context-protocol](https://github.com/ChristophEnglisch/keycloak-model-context-protocol)** - ⭐ 45
   MCP server implementation for Keycloak user management. Enables AI-powered administration of Keycloak users and realms through the Model Context Protocol (MCP). Seamlessly integrates with Claude Desktop and other MCP clients for automated user operations.

3176. **[mcp-tools](https://github.com/clerk/mcp-tools)** - ⭐ 45
   Tools for building modern & secure MCP integrations across the client and server side

3177. **[shodan-mcp-server](https://github.com/Cyreslab-AI/shodan-mcp-server)** - ⭐ 45
   A Model Context Protocol server that provides access to Shodan API functionality

3178. **[ainovelprompter](https://github.com/danielsobrado/ainovelprompter)** - ⭐ 45
   Create the prompts you need to write your Novel using AI

3179. **[dataworkers-claw-community](https://github.com/DataWorkersProject/dataworkers-claw-community)** - ⭐ 45
   We’re build a swarm of agents for all data tasks. That anyone can use for free, open-source community version.

3180. **[mcp-playground](https://github.com/Elkhn/mcp-playground)** - ⭐ 45
   A Streamlit-based chat app for LLMs with plug-and-play tool support via Model Context Protocol (MCP), powered by LangChain, LangGraph, and Docker.

3181. **[mcpguard-dynamic](https://github.com/facebook/mcpguard-dynamic)** - ⭐ 45
   Kernel-level eBPF sandbox for securing LLM agent tool calls made through the Model Context Protocol (MCP)

3182. **[eliza-plugin-mcp](https://github.com/fleek-platform/eliza-plugin-mcp)** - ⭐ 45
   ElizaOS plugin allowing agents to connect to MCP servers

3183. **[algorand-mcp](https://github.com/GoPlausible/algorand-mcp)** - ⭐ 45
   Algorand Local Model Context Protocol (Server & Client)

3184. **[excalidraw-mcp](https://github.com/i-tozer/excalidraw-mcp)** - ⭐ 45
   Model Context Protocol (MCP) server for Excalidraw - Work in Progress

3185. **[fusion-mcp-server](https://github.com/Joe-Spencer/fusion-mcp-server)** - ⭐ 45
   A model context protocol (MCP) server for Autodesk Fusion that provides resources and tools from ADSK to an AI client such as Claude or Cursor.

3186. **[marinade-finance-mcp-server](https://github.com/lorine93s/marinade-finance-mcp-server)** - ⭐ 45
   Marinade Finance MCP Server is an MCP server specifically designed for the Marinade Finance.

3187. **[mcp_server_filesystem](https://github.com/MarcusJellinghaus/mcp_server_filesystem)** - ⭐ 45
   MCP File System Server: A secure Model Context Protocol server that provides file operations for AI assistants. Enables Claude and other assistants to safely read, write, and list files in a designated project directory with robust path validation and security controls.

3188. **[opencode-browser](https://github.com/michaljach/opencode-browser)** - ⭐ 45
   Browser automation plugin for OpenCode AI editor - Control Chrome/Edge with AI, automate web testing, scraping & form filling via MCP integration

3189. **[aitour26-WRK542-prototype-agents-with-the-ai-toolkit-and-model-context-protocol](https://github.com/microsoft/aitour26-WRK542-prototype-agents-with-the-ai-toolkit-and-model-context-protocol)** - ⭐ 45

3190. **[fusion360-claude-ultimate](https://github.com/Misterbra/fusion360-claude-ultimate)** - ⭐ 45
   🤖 Control Fusion 360 with natural language through Claude Desktop using MCP (Model Context Protocol). Create, manipulate and modify 3D objects by simply describing what you want to do. French-localized adaptation of Kanbara Tomonori's original concept.

3191. **[SSH-MCP](https://github.com/mixelpixx/SSH-MCP)** - ⭐ 45
   A Model Context Protocol (MCP) server that provides SSH access to remote servers, allowing AI tools like Claude Desktop or VS Code to securely connect to your VPS.

3192. **[spring-ai-mcp-client](https://github.com/ogulcanarbc/spring-ai-mcp-client)** - ⭐ 45
   mcp client application that utilizes spring ai. it integrates with mcp protocol-supported servers to enable ai-powered chat interactions.

3193. **[mcp-tool-filter](https://github.com/Portkey-AI/mcp-tool-filter)** - ⭐ 45
   Ultra-fast semantic tool filtering for MCP (Model Context Protocol) servers using embedding similarity. Reduce your tool context from 1000+ tools down to the most relevant 10-20 tools in under 10ms.

3194. **[a11y-mcp](https://github.com/priyankark/a11y-mcp)** - ⭐ 45
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core. Use the results in an agentic loop with your favorite AI assistants (Amp/Cline/Cursor/GH Copilot) and let them fix a11y issues for you!

3195. **[dynamic-fastmcp](https://github.com/ragieai/dynamic-fastmcp)** - ⭐ 45
   Dynamic FastMCP extends the Model Context Protocol Python server with context-aware tools that adapt their behavior and descriptions based on user, tenant, and request context.

3196. **[orionbelt-semantic-layer](https://github.com/ralfbecher/orionbelt-semantic-layer)** - ⭐ 45
   API-first semantic engine and query planner for AI agents that compiles declarative YAML models into optimized, dialect-specific SQL across BigQuery, PostgreSQL, Snowflake, ClickHouse, Dremio, Databricks, DuckDB, and MySQL.

3197. **[roampal-core](https://github.com/roampal-ai/roampal-core)** - ⭐ 45
   Outcome-based persistent memory MCP server for Claude Code and OpenCode. Good advice promoted, bad advice demoted. pip install roampal.

3198. **[zillow-mcp-server](https://github.com/sap156/zillow-mcp-server)** - ⭐ 45
   Zillow MCP Server for real estate data access via the Model Context Protocol

3199. **[mcp-sdk](https://github.com/symfony/mcp-sdk)** - ⭐ 45
   Model Context Protocol SDK for Client and Server applications in PHP

3200. **[python-notebook-mcp](https://github.com/UsamaK98/python-notebook-mcp)** - ⭐ 45
   Lightweight Python Notebook MCP - Enable AI assistants to create, edit, and view Jupyter notebooks via Model Context Protocol

3201. **[gopls-mcp](https://github.com/xieyuschen/gopls-mcp)** - ⭐ 45
   MCP server for golang projects development: Expand AI Code Agent ability boundary to have a semantic understanding and determinisic information for golang projects.

3202. **[mcp-zenml](https://github.com/zenml-io/mcp-zenml)** - ⭐ 45
   MCP server to connect an MCP client (Cursor, Claude Desktop etc) with your ZenML MLOps and LLMOps pipelines

3203. **[mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi)** - ⭐ 44
   A Model Context Protocol server implementation for Kagi's API

3204. **[yandex-tracker-mcp](https://github.com/aikts/yandex-tracker-mcp)** - ⭐ 44
   Yandex Tracker MCP Server with OAuth2 support

3205. **[Ctxo](https://github.com/alperhankendi/Ctxo)** - ⭐ 44
   MCP server for AI coding agents. Instead of reading files one by one, your agent gets dependency graphs, git intent, blast radius, and change health in a single call. Works with any language deep analysis for TypeScript, Go, and C#.

3206. **[mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks)** - ⭐ 44
   This Model Context Protocol (MCP) server provides a bridge between LLMs and Google Tasks, allowing you to manage your task lists and tasks directly through Claude.

3207. **[SpecialAgentPlugin](https://github.com/ArtisanGameworks/SpecialAgentPlugin)** - ⭐ 44
   SpecialAgent is an Unreal Engine 5 plugin that implements a Model Context Protocol (MCP)  server, allowing Large Language Models like Claude to programmatically interact with UE5  projects. With 71+ tool endpoints across 14 service categories, LLMs gain comprehensive control for building complex 3D environments.

3208. **[bsky-mcp-server](https://github.com/brianellin/bsky-mcp-server)** - ⭐ 44
   Bluesky MCP (Model Context Protocol) Server

3209. **[moondream-mcp](https://github.com/ColeMurray/moondream-mcp)** - ⭐ 44
   Moondream MCP Server in Python

3210. **[codebase-mcp](https://github.com/danyQe/codebase-mcp)** - ⭐ 44
   Open-source AI development assistant via Model Context Protocol (MCP). Turn Claude or any LLM into your personal coding assistant. Privacy-first with local semantic search, AI-assisted editing, persistent memory, and quality-checked code generation. Built for Python & React. Free alternative to paid AI coding tools.

3211. **[fcpxml-mcp-server](https://github.com/DareDev256/fcpxml-mcp-server)** - ⭐ 44
   🎬 The first AI-powered MCP server for Final Cut Pro XML. Control your edits with natural language.

3212. **[mcp-tasks](https://github.com/flesler/mcp-tasks)** - ⭐ 44
   A comprehensive and efficient MCP server for task management with multi-format support (Markdown, JSON, YAML)

3213. **[mcp-pyautogui-server](https://github.com/hetaoBackend/mcp-pyautogui-server)** - ⭐ 44
   A MCP (Model Context Protocol) server that provides automated GUI testing and control capabilities through PyAutoGUI.

3214. **[salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server)** - ⭐ 44
   Model Context Protocol server for Salesforce REST API integration

3215. **[bgg-mcp](https://github.com/kkjdaniel/bgg-mcp)** - ⭐ 44
   BGG MCP provides access to BoardGameGeek and a variety of board game related data through the Model Context Protocol. Enabling retrieval and filtering of board game data, user collections, and profiles.

3216. **[mcp-server-lib.el](https://github.com/laurynas-biveinis/mcp-server-lib.el)** - ⭐ 44
   Emacs Lisp implementation of the Model Context Protocol

3217. **[fal-mcp-server](https://github.com/luminarylane/fal-mcp-server)** - ⭐ 44
   MCP server for Fal.ai - Generate images, videos, music and audio with Claude

3218. **[mcp-agents-hub](https://github.com/mcp-agents-ai/mcp-agents-hub)** - ⭐ 44
   The open-source ecosystem for building, discovering, and deploying Model Context Protocol servers and clients.

3219. **[MCPToolBenchPP](https://github.com/mcp-tool-bench/MCPToolBenchPP)** - ⭐ 44
   MCPToolBench++ MCP Model Context Protocol Tool Use Benchmark on AI Agent and Model Tool Use Ability

3220. **[awesome-mcp-servers](https://github.com/mctrinh/awesome-mcp-servers)** - ⭐ 44
   A curated list of excellent Model Context Protocol (MCP) servers.

3221. **[code-screenshot-mcp](https://github.com/MoussaabBadla/code-screenshot-mcp)** - ⭐ 44
   MCP server for generating beautiful code screenshots directly from Claude

3222. **[dev-to-mcp](https://github.com/nickytonline/dev-to-mcp)** - ⭐ 44
   A remote Model Context Protocol (MCP) server for interacting with the dev.to public API without requiring authentication.

3223. **[Learn-Model-Context-Protocol-with-Python](https://github.com/PacktPublishing/Learn-Model-Context-Protocol-with-Python)** - ⭐ 44
   Learn Model Context Protocol with Python, published by Packt

3224. **[codebase-context](https://github.com/PatrickSys/codebase-context)** - ⭐ 44
   Generate a map of your codebaseto help AI Agents understand your architecture, coding conventions and patterns. Discoverable with Semantic Search

3225. **[cli-anything-zotero](https://github.com/PiaoyangGuohai1/cli-anything-zotero)** - ⭐ 44
   CLI & MCP server for Zotero 7/8 — let AI manage your library. 52 MCP tools + 70+ CLI commands for search, import, PDF, BibTeX, notes, and more. Works with Claude, Cursor, ChatGPT.

3226. **[prism-mcp-rs](https://github.com/prismworks-ai/prism-mcp-rs)** - ⭐ 44
   Enterprise-grade Rust implementation of Anthropic's MCP protocol

3227. **[chrome-debug-mcp](https://github.com/robertheadley/chrome-debug-mcp)** - ⭐ 44
   An MCP server to allow you to debug webpages using LLMs

3228. **[generic-mcp-client-chat](https://github.com/rom1504/generic-mcp-client-chat)** - ⭐ 44
   Generic MCP Client to use any MCP tool in a chat

3229. **[adal-cli](https://github.com/SylphAI-Inc/adal-cli)** - ⭐ 44
   The self-evolving coding agent that learns from your entire team and codebase. Less syncing. Less waiting. Deliver at the speed of thought.

3230. **[mcp-client-cli](https://github.com/thedotmack/mcp-client-cli)** - ⭐ 44
   Command-line interface for any Model Context Protocol (MCP) server.

3231. **[vue-mcp-next](https://github.com/tuskermanshu/vue-mcp-next)** - ⭐ 44
   Vue MCP Next bridges AI agents with Vue.js applications, enabling real-time component state inspection and   manipulation through the Model Context Protocol. Built for AI-assisted development workflows

3232. **[flywheel-memory](https://github.com/velvetmonkey/flywheel-memory)** - ⭐ 44
   MCP server giving AI a knowledge graph over Obsidian vaults. 13-layer scoring that learns. Local-first, zero cloud.

3233. **[MCPP.Net](https://github.com/xuzeyu91/MCPP.Net)** - ⭐ 44
   Model Context Protocol Platform，统一管理你的MCP服务

3234. **[mcp-typescribe](https://github.com/yWorks/mcp-typescribe)** - ⭐ 44
   An MCP server implementation enabling LLMs to work with new APIs and frameworks

3235. **[alibabacloud-dataworks-mcp-server](https://github.com/aliyun/alibabacloud-dataworks-mcp-server)** - ⭐ 43
   A Model Context Protocol (MCP) server that provides tools for AI, allowing it to interact with the DataWorks Open API through a standardized interface. This implementation is based on the Aliyun Open API and enables AI agents to perform cloud resources operations seamlessly.

3236. **[ads-mcp](https://github.com/amekala/ads-mcp)** - ⭐ 43
   MCP server for managing ad campaigns across Google Ads, Meta Ads, LinkedIn Ads, and TikTok Ads. 100+ tools for campaign creation, performance analysis, keyword research, and budget optimization. Works with ChatGPT, Claude, Gemini CLI, Cursor, Codex, and Windsurf.

3237. **[mcp-logic](https://github.com/angrysky56/mcp-logic)** - ⭐ 43
   Fully functional AI Logic Calculator utilizing Prover9/Mace4 via Python based Model Context Protocol (MCP-Server)- tool for Windows, Linux, Claude App etc

3238. **[awesome-finance-mcp](https://github.com/BlockRunAI/awesome-finance-mcp)** - ⭐ 43
   A curated list of MCP servers for AI finance agents

3239. **[mcp-server-leetcode](https://github.com/doggybee/mcp-server-leetcode)** - ⭐ 43
   A Model Context Protocol (MCP) server for LeetCode that provides access to problems, user data, and contest information through GraphQL

3240. **[MetaSearchMCP](https://github.com/gefsikatsinelou/MetaSearchMCP)** - ⭐ 43
   Open-source metasearch backend, MCP server, and AI search API for LLM agents. Python FastAPI search gateway with Google search via SerpBase and Serper, multi-engine search aggregation, structured JSON output, provider fallback, deduplication, and SearXNG alternative architecture for agent workflows.

3241. **[wechat-mcp](https://github.com/JettChenT/wechat-mcp)** - ⭐ 43
   Model Context Protocol for WeChat

3242. **[lastsaas](https://github.com/jonradoff/lastsaas)** - ⭐ 43
   SaaS boilerplate/starter-kit in Go+React with Stripe integration, multi-tenant support, comprehensive features and AI-agent ready

3243. **[elysia-mcp](https://github.com/kerlos/elysia-mcp)** - ⭐ 43
   ElysiaJS plugin for Model Context Protocol with HTTP transport

3244. **[music-composer-webmcp](https://github.com/Leanmcp-Community/music-composer-webmcp)** - ⭐ 43
   This WebMCP Music Composer project is a functional demonstration of the WebMCP Protocol, illustrating how AI agents can interact with local browser contexts (tools) to achieve complex workflows autonomously.

3245. **[substack-mcp](https://github.com/marcomoauro/substack-mcp)** - ⭐ 43
   A Model Context Protocol (MCP) Server for Substack enabling LLM clients to interact with Substack's API for automations like creating posts, managing drafts, and more.

3246. **[taskMaster-todoist-mcp](https://github.com/mingolladaniele/taskMaster-todoist-mcp)** - ⭐ 43
   A lightweight Model Context Protocol (MCP) server that enables natural language interaction with your Todoist tasks directly from your IDE. Built with simplicity and maintainability in mind.

3247. **[matrix-mcp-server](https://github.com/mjknowles/matrix-mcp-server)** - ⭐ 43
   MCP Server for a Matrix home server integration; chat, manage rooms, etc.

3248. **[better-code-review-graph](https://github.com/n24q02m/better-code-review-graph)** - ⭐ 43
   Knowledge graph for token-efficient code reviews -- fixed search, configurable embeddings, qualified call resolution.

3249. **[ue5-mcp-bridge](https://github.com/Natfii/ue5-mcp-bridge)** - ⭐ 43
   MCP server bridging AI assistants to Unreal Engine 5 editor

3250. **[LLaMa-MCP-Streamlit](https://github.com/Nikunj2003/LLaMa-MCP-Streamlit)** - ⭐ 43
   AI assistant built with Streamlit, NVIDIA NIM (LLaMa 3.3:70B) / Ollama, and Model Control Protocol (MCP).

3251. **[nia](https://github.com/nozomio-labs/nia)** - ⭐ 43
   Nia is a context-augmentation layer for agents, primarily designed for coding agents. It provides them with an up-to-date knowledge base and improves their performance by 27%.

3252. **[mcp-server](https://github.com/profullstack/mcp-server)** - ⭐ 43
   A generic, modular server for implementing the Model Context Protocol (MCP).

3253. **[mcp-server-arangodb](https://github.com/ravenwits/mcp-server-arangodb)** - ⭐ 43
   This is a TypeScript-based MCP server that provides database interaction capabilities through ArangoDB. It implements core database operations and allows seamless integration with ArangoDB through MCP tools. You can use it wih Claude app and also extension for VSCode that works with mcp like Cline!

3254. **[grafana-mcp-analyzer](https://github.com/SailingCoder/grafana-mcp-analyzer)** - ⭐ 43
   让AI助手直接分析你的Grafana监控数据 - A Model Context Protocol server for Grafana data analysis

3255. **[openrpc-mcp-server](https://github.com/shanejonas/openrpc-mcp-server)** - ⭐ 43
   A Model Context Protocol (MCP) server that provides JSON-RPC functionality through OpenRPC.

3256. **[inkmcp](https://github.com/Shriinivas/inkmcp)** - ⭐ 43
   Inkscape MCP Server - Control Inkscape through AI assistants via Model Context Protocol

3257. **[mitmproxy-mcp](https://github.com/snapspecter/mitmproxy-mcp)** - ⭐ 43
   MCP Server that wraps mitmproxy and exposes it as a tool to any MCP client, allows your AI agents to inspect traffic, filter traffic, intercept & modify traffic, request reply, set global headers, and start/stop mitmproxy as needed.

3258. **[solana-dev-mcp](https://github.com/solana-foundation/solana-dev-mcp)** - ⭐ 43
   Solana Model Context Protocol (MCP) Demo

3259. **[mcp-bundle](https://github.com/symfony/mcp-bundle)** - ⭐ 43
   Symfony integration bundle for Model Context Protocol (via official mcp/sdk)

3260. **[cli](https://github.com/syrin-labs/cli)** - ⭐ 43
   Runtime intelligence system that makes MCP servers debuggable, testable, and safe to run in production.

3261. **[agentic-developer-mcp](https://github.com/teabranch/agentic-developer-mcp)** - ⭐ 43
   An MCP server that scales development into controllable agentic, recursive flows, and build a feature from bottom-up

3262. **[webscraping-ai-mcp-server](https://github.com/webscraping-ai/webscraping-ai-mcp-server)** - ⭐ 43
    A Model Context Protocol (MCP) server implementation that integrates with WebScraping.AI for web data extraction capabilities.

3263. **[mcp-rquest](https://github.com/xxxbrian/mcp-rquest)** - ⭐ 43
   A MCP server providing realistic browser-like HTTP request capabilities with accurate TLS/JA3/JA4 fingerprints for bypassing anti-bot measures. It also supports converting PDF and HTML documents to Markdown for easier processing by LLMs.

3264. **[mcp-zero](https://github.com/zeromicro/mcp-zero)** - ⭐ 43
   Model Context Protocol (MCP) server for go-zero framework - Generate APIs, RPC services, and models with AI assistance.

3265. **[origin](https://github.com/7xuanlu/origin)** - ⭐ 42
   Local-first AI work memory that compounds: capture decisions, lessons, gotchas in flow, distill into source-backed wiki pages, recall across sessions and any MCP client (Claude Code, Codex, etc...). Plain Markdown you own.

3266. **[mcp-server](https://github.com/Aayush9029/mcp-server)** - ⭐ 42
   MCP SERVER

3267. **[mcp-flight-search](https://github.com/arjunprabhulal/mcp-flight-search)** - ⭐ 42
   MCP Server implementation for the Model Context Protocol (MCP) enabling AI tool usage - Realtime Flight Search

3268. **[tinyagent](https://github.com/askbudi/tinyagent)** - ⭐ 42
   Tiny Agent: Production-Ready LLM Agent SDK for Every Developer

3269. **[reactbits-mcp-server](https://github.com/ceorkm/reactbits-mcp-server)** - ⭐ 42
   MCP server providing access to 135+ animated React components from ReactBits.dev (9.2/10 test score)

3270. **[RedBook-Search-Comment-MCP](https://github.com/chenningling/RedBook-Search-Comment-MCP)** - ⭐ 42
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client，帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布智能评论等操作。

3271. **[tally-mcp-server](https://github.com/dhananjay1405/tally-mcp-server)** - ⭐ 42
   Tally Prime MCP (Model Context Protocol) Server implementation to feed Tally ERP data to popular LLM like Claude, ChatGPT supporting MCP

3272. **[whatsapp-mcp](https://github.com/felipeadeildo/whatsapp-mcp)** - ⭐ 42
   WhatsApp Unofficial MCP Server

3273. **[pyrestoolbox-mcp](https://github.com/gabrielserrao/pyrestoolbox-mcp)** - ⭐ 42
   Model Context Protocol (MCP) server for AI-powered reservoir engineering calculations. Integrates pyResToolbox with Claude AI for PVT analysis, well   performance, simulation support, and more. 47 production-ready tools using industry-standard correlations.

3274. **[openevidence-mcp](https://github.com/htlin222/openevidence-mcp)** - ⭐ 42
   Unofficial OpenEvidence MCP server — query OpenEvidence from Claude Code, Codex, and any MCP client through your own logged-in browser tab (no API key). Fire-and-forget asks, a shared relay daemon for concurrent sessions, BibTeX + Crossref citations.

3275. **[mobile-dev-mcp-server](https://github.com/jsuarezruiz/mobile-dev-mcp-server)** - ⭐ 42
   This is a MCP designed to manage and interact with mobile devices and simulators.

3276. **[mcp-konnect](https://github.com/Kong/mcp-konnect)** - ⭐ 42
   A Model Context Protocol (MCP) server for interacting with Kong Konnect APIs, allowing AI assistants to query and analyze Kong Gateway configurations, traffic, and analytics.

3277. **[mie](https://github.com/kraklabs/mie)** - ⭐ 42
   Persistent memory graph for AI agents. Facts, decisions, entities, and relationships that survive across sessions, tools, and providers. MCP server — works with Claude, Cursor, ChatGPT, and any MCP client.

3278. **[linkedapi-mcp](https://github.com/Linked-API/linkedapi-mcp)** - ⭐ 42
   MCP server that lets AI assistants control LinkedIn accounts and retrieve real-time data.

3279. **[zed-mcp-server-sequential-thinking](https://github.com/LoamStudios/zed-mcp-server-sequential-thinking)** - ⭐ 42
   A sequential thinking MCP server extension for Zed

3280. **[mcp-anywhere](https://github.com/locomotive-agency/mcp-anywhere)** - ⭐ 42
   A unified gateway for Model Context Protocol (MCP) servers that lets you discover, configure, and access MCP tools from any GitHub repository through a single endpoint.

3281. **[meta-ads-mcp](https://github.com/mikusnuz/meta-ads-mcp)** - ⭐ 42
   MCP server for Meta Marketing API v25.0 — 135 tools for Facebook & Instagram ad campaign management

3282. **[mermaid-mcp](https://github.com/Narasimhaponnada/mermaid-mcp)** - ⭐ 42

3283. **[jina-mcp-tools](https://github.com/PsychArch/jina-mcp-tools)** - ⭐ 42
   A Model Context Protocol (MCP) server that integrates with Jina AI Search Foundation APIs.

3284. **[qu3-app](https://github.com/qu3ai/qu3-app)** - ⭐ 42
   Quantum-proof MCP Server and Client Interactions

3285. **[fal-mcp-server](https://github.com/raveenb/fal-mcp-server)** - ⭐ 42
   MCP server for Fal.ai - Generate images, videos, music and audio with Claude

3286. **[mcp-google-cse](https://github.com/Richard-Weiss/mcp-google-cse)** - ⭐ 42
   A Model Context Protocol server that provides search capabilities using a Google CSE (custom search engine).

3287. **[mcp_rails_template](https://github.com/seuros/mcp_rails_template)** - ⭐ 42
   A minimal Rails API template for creating MCP (Model Context Protocol) servers with robust tool execution capabilities and examples.

3288. **[repl-mcp](https://github.com/simm-is/repl-mcp)** - ⭐ 42
   Model Context Protocol Clojure support including REPL integration with development tools.

3289. **[keycloak-mcp-server](https://github.com/sshaaf/keycloak-mcp-server)** - ⭐ 42
   An MCP server for Keycloak,  designed to work with Keycloak for identity and access management, covering, Users, Realms, Clients, Roles, Groups, IDPs, Authentication. Searching keycloak discourse, Native builds available.

3290. **[mitre-attack-mcp](https://github.com/stoyky/mitre-attack-mcp)** - ⭐ 42
   A Model-Context Protocol server for the MITRE ATT&CK knowledge base

3291. **[clickup-mcp-server](https://github.com/taazkareem/clickup-mcp-server)** - ⭐ 42
   ClickUp MCP Server - Integrate ClickUp project management with AI through Model Context Protocol

3292. **[searxng-mcp](https://github.com/tisDDM/searxng-mcp)** - ⭐ 42
   A Model Context Protocol (MCP) server that enables AI assistants to perform web searches using SearXNG, a privacy-respecting metasearch engine.

3293. **[scaled-mcp](https://github.com/Traego/scaled-mcp)** - ⭐ 42
   ScaledMCP is a horizontally scalabled MCP and A2A Server. You know, for AI.

3294. **[midi-mcp-server](https://github.com/tubone24/midi-mcp-server)** - ⭐ 42
   MIDI MCP Server is a Model Context Protocol (MCP) server that enables AI models to generate MIDI files from text-based music data. This tool allows for programmatic creation of musical compositions through a standardized interface.

3295. **[TWSEMCPServer](https://github.com/twjackysu/TWSEMCPServer)** - ⭐ 42
   台灣證交所OpenAPI 的 MCP Server

3296. **[xero-agent-toolkit](https://github.com/XeroAPI/xero-agent-toolkit)** - ⭐ 42
   A collection of examples demonstrating how to build AI agents that integrate with the Xero API using various agentic frameworks and the Xero MCP (Model Context Protocol) Server.

3297. **[dify-mcp-server](https://github.com/AI-FE/dify-mcp-server)** - ⭐ 41
   A Model Context Protocol server for Dify

3298. **[platform-context-exporter](https://github.com/alkoleft/platform-context-exporter)** - ⭐ 41
   Инструмент для выгрузки синтаксис помощника в файлы

3299. **[arifOS](https://github.com/ariffazil/arifOS)** - ⭐ 41
   ArifOS — Constitutional MCP kernel for governed AI execution. AAA architecture: Architect · Auditor · Agent. Built for the open-source agentic era.

3300. **[mcp-server-ios-simulator](https://github.com/atom2ueki/mcp-server-ios-simulator)** - ⭐ 41
   Model Context Protocol (MCP) implementation for iOS simulators

3301. **[PubChem-MCP-Server](https://github.com/Augmented-Nature/PubChem-MCP-Server)** - ⭐ 41
   A comprehensive Model Context Protocol (MCP) server for accessing the PubChem chemical database. This server provides access to over 110 million chemical compounds with extensive molecular properties, bioassay data, and chemical informatics tools.

3302. **[xmind-generator-mcp](https://github.com/BangyiZhang/xmind-generator-mcp)** - ⭐ 41
   An MCP (Model Context Protocol) server for generating Xmind mind maps. This server allows LLMs to create structured mind maps through the MCP protocol.

3303. **[dynamic-shell-server](https://github.com/codelion/dynamic-shell-server)** - ⭐ 41
   Dynamic Shell Command MCP Server

3304. **[MCP-BOE](https://github.com/ComputingVictor/MCP-BOE)** - ⭐ 41
   MCP server para el BOE 🇪🇸 — Acceso a legislación consolidada, sumarios diarios y tablas oficiales del Boletín Oficial del Estado mediante Model Context Protocol y API REST.

3305. **[filesystem-mcp-server](https://github.com/cyanheads/filesystem-mcp-server)** - ⭐ 41
   A Model Context Protocol (MCP) server for platform-agnostic file capabilities, including advanced search/replace and directory tree traversal

3306. **[mcp-obsidian](https://github.com/fazer-ai/mcp-obsidian)** - ⭐ 41
   MCP server for Obsidian (TypeScript + Bun)

3307. **[gatekit](https://github.com/gatekit-ai/gatekit)** - ⭐ 41
   A hackable Model Context Protocol (MCP) gateway

3308. **[RiMCP_hybrid](https://github.com/h7lu/RiMCP_hybrid)** - ⭐ 41
   Rimworld Coding RAG MCP server

3309. **[mcp-shell](https://github.com/hdresearch/mcp-shell)** - ⭐ 41
   Execute a secure shell in Claude Desktop using the Model Context Protocol.

3310. **[locallama-mcp](https://github.com/Heratiki/locallama-mcp)** - ⭐ 41
   An MCP Server that works with Roo Code/Cline.Bot/Claude Desktop to optimize costs by intelligently routing coding tasks between local LLMs free APIs and paid APIs.

3311. **[processhacker-mcp](https://github.com/illegal-instruction-co/processhacker-mcp)** - ⭐ 41
   your ai debugger, vibe hacking tool

3312. **[Unity-AI-ProBuilder](https://github.com/IvanMurzak/Unity-AI-ProBuilder)** - ⭐ 41
   AI-powered 3D modeling tools for Unity ProBuilder. Enables AI assistants to create and manipulate editable meshes through natural language commands. Create primitive shapes, extrude faces, bevel edges, apply materials, merge objects, and perform advanced mesh operations like bridging and subdivision.

3313. **[salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server)** - ⭐ 41
   A comprehensive Model Context Protocol (MCP) server that provides seamless Salesforce integration for AI development tools like Claude Desktop, Cline, and other MCP-compatible clients.

3314. **[korean-contracts](https://github.com/kimlawtech/korean-contracts)** - ⭐ 41
   한국 사업자용 계약서 자동 생성 Claude Code 스킬. 9종 계약서(근로·알바·유연·일용·프리랜서·외주·변경·연봉) + MCP 개인정보 보호 서버. 2026 최저임금·최신 대법원 판례 반영.

3315. **[mTarsier](https://github.com/mcp360/mTarsier)** - ⭐ 41
   mTarsier - The Open Source MCP & Skill Manager for Claude, Cursor, VS Code & any AI client.

3316. **[mcp-center](https://github.com/nautilus-ops/mcp-center)** - ⭐ 41
   A centralized platform for managing and connecting MCP servers. MCP Center provides a high-performance proxy service that enables seamless communication between MCP clients and multiple MCP servers.

3317. **[neurondb](https://github.com/neurondb/neurondb)** - ⭐ 41
   PostgreSQL extension for vector search, embeddings, and ML, plus NeuronAgent runtime and NeuronMCP server.

3318. **[agentic-mcp-client](https://github.com/peakmojo/agentic-mcp-client)** - ⭐ 41
   A standalone agent runner that executes tasks using MCP (Model Context Protocol) tools via Anthropic Claude, AWS BedRock and OpenAI APIs. It enables AI agents to run autonomously in cloud environments and interact with various systems securely.

3319. **[MCPollinations](https://github.com/pinkpixel-dev/MCPollinations)** - ⭐ 41
   A Model Context Protocol (MCP) server that enables AI assistants to generate images, text, and audio through the Pollinations APIs. Supports customizable parameters, image saving, and multiple model options.

3320. **[opnsense-mcp-server](https://github.com/Pixelworlds/opnsense-mcp-server)** - ⭐ 41
   Modular MCP server for OPNsense firewall management - 88 tools providing access to 2000+ methods through AI assistants

3321. **[okx-agent-trade-kit](https://github.com/PlaceNL2026/okx-agent-trade-kit)** - ⭐ 41
   OKX trading MCP CLI cryptocurrency spot futures swap AI agent Model Context Protocol Cursor Claude npm automated trading crypto API toolkit TypeScript open-source DeFi CEX

3322. **[mcp-api-gateway](https://github.com/rflpazini/mcp-api-gateway)** - ⭐ 41
   A universal MCP (Model Context Protocol) server to integrate any API with Claude Desktop using only Docker configurations.

3323. **[agent-mcp-gateway](https://github.com/roddutra/agent-mcp-gateway)** - ⭐ 41
   Provides per-subagent MCP access controls to Claude Code (or any MCP client) across all your MCPs and prevents context window bloat. Loads only 3 tools instead of all your MCP Server's tool definitions. Agents discover tools on-demand, only when needed. Control which servers and individual tools each agent/subagent can access.

3324. **[unreal-mcp](https://github.com/runeape-sats/unreal-mcp)** - ⭐ 41
   Unreal Engine MCP server for Claude Desktop (early alpha preview)

3325. **[felix](https://github.com/sausheong/felix)** - ⭐ 41
   Felix — single-binary AI agent gateway. Multi-provider LLM, persistent memory, MCP client, runs entirely on your hardware

3326. **[seekcode](https://github.com/seekrays/seekcode)** - ⭐ 41
   A clean and efficient code snippet and clipboard management tool designed for developers

3327. **[mcp-gateway](https://github.com/theognis1002/mcp-gateway)** - ⭐ 41
   Model Context Protocol (MCP) Gateway & Registry - Central hub for managing tools, resources, and prompts for MCP-compatible LLMs. Translates REST APIs into MCP, builds virtual MCP servers with security and observability, and bridges multiple transports (stdio, SSE, streamable HTTP).

3328. **[whatsapp-mcp](https://github.com/verygoodplugins/whatsapp-mcp)** - ⭐ 41
   WhatsApp MCP server - Connect Claude to WhatsApp for reading and sending messages

3329. **[solscan-mcp](https://github.com/wowinter13/solscan-mcp)** - ⭐ 41
   An MCP server for querying Solana transactions using natural language with Solscan API

3330. **[mcp-server-js](https://github.com/yepcode/mcp-server-js)** - ⭐ 41
   MCP server that exposes YepCode processes as callable tools for AI platforms. Securely connect AI assistants to your YepCode workflows, APIs, and automations.

3331. **[ZMCPTools](https://github.com/ZachHandley/ZMCPTools)** - ⭐ 41
   A custom TypeScript MCP Server intended to be used with Claude Code

3332. **[golemcore-bot](https://github.com/alexk-dev/golemcore-bot)** - ⭐ 40
   Agent Platform for AI-Native Companies

3333. **[mcp](https://github.com/Azure-Samples/mcp)** - ⭐ 40
   Links to samples, tools, and resources for building and integrating Model Context Protocol (MCP) servers on Azure using multiple languages

3334. **[mcp-server](https://github.com/blockscout/mcp-server)** - ⭐ 40
   Wraps Blockscout APIs and exposes blockchain data by Model Context Protocol

3335. **[scraps](https://github.com/boykush/scraps)** - ⭐ 40
   Scraps is a portable CLI knowledge hub for managing interconnected Markdown documentation with Wiki-link notation.

3336. **[dexpaprika-mcp](https://github.com/coinpaprika/dexpaprika-mcp)** - ⭐ 40
   DexPaprika MCP server allows access real-time and historical data on crypto tokens, DEX trading activity, and liquidity across multiple blockchains. It enables natural language queries for exploring market trends, token performance, and DeFi analytics through a standardized interface.

3337. **[autoteam](https://github.com/diazoxide/autoteam)** - ⭐ 40
   Orchestrate AI agents with YAML-driven workflows via universal Model Context Protocol (MCP)

3338. **[agentmako](https://github.com/drhalto/agentmako)** - ⭐ 40
   Local-first MCP server that gives coding agents structured context packets, code/schema facts, and diagnostics - backed by a local SQLite store.

3339. **[MCPbundler](https://github.com/eugenepyvovarov/MCPbundler)** - ⭐ 40

3340. **[mcp-for-security-python](https://github.com/f1tz/mcp-for-security-python)** - ⭐ 40
   一个为主流渗透测试工具打造的MCP服务器集合。 | A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

3341. **[originlab-mcp](https://github.com/garethbeaumo/originlab-mcp)** - ⭐ 40
    MCP Server for OriginLab  Control OriginLab with natural language through AI clients via the Model Context Protocol.

3342. **[claude-image-gen](https://github.com/guinacio/claude-image-gen)** - ⭐ 40
   AI-powered image generation using Google Gemini, integrated with Claude Code via Skills or Claude.ai via MCP (Model Context Protocol).

3343. **[mcp-desktop](https://github.com/http4k/mcp-desktop)** - ⭐ 40
   http4k MCP Desktop Client

3344. **[pdf-rag-mcp-server](https://github.com/hyson666/pdf-rag-mcp-server)** - ⭐ 40
   PDF RAG server for cursor.

3345. **[mcp-claude-spotify](https://github.com/imprvhub/mcp-claude-spotify)** - ⭐ 40
   An integration that allows Claude Desktop to interact with Spotify using the Model Context Protocol (MCP).

3346. **[reaper-mcp](https://github.com/itsuzef/reaper-mcp)** - ⭐ 40
   A comprehensive Model Context Protocol (MCP) server that enables AI agents to create fully mixed and mastered tracks in REAPER with both MIDI and audio capabilities.

3347. **[claude-homelab](https://github.com/jmagar/claude-homelab)** - ⭐ 40
   Comprehensive Agents, Commands, Hooks, and Skills for homelab service management - media automation, infrastructure monitoring, document management, and more

3348. **[dap_mcp](https://github.com/KashunCheng/dap_mcp)** - ⭐ 40
   Model Context Protocol (MCP) server that interacts with a Debugger

3349. **[storyblok-mcp-server](https://github.com/Kiran1689/storyblok-mcp-server)** - ⭐ 40
   A modular, extensible MCP Server for managing Storyblok spaces, stories, components, assets, workflows, and more via the Model Context Protocol (MCP).

3350. **[mmcp](https://github.com/koki-develop/mmcp)** - ⭐ 40
   🛠️ Manage your MCP (Model Context Protocol) server definitions in one place and apply them to supported agents.

3351. **[mcp](https://github.com/kyopark2014/mcp)** - ⭐ 40
   It shows how to use model-context-protocol.

3352. **[bonnard-cli](https://github.com/meal-inc/bonnard-cli)** - ⭐ 40
   Agent-native analytics. MCP server, dashboards, SDK, and semantic layer CLI.

3353. **[polymarket-mcp](https://github.com/ozgureyilmaz/polymarket-mcp)** - ⭐ 40
   a mcp server for polymarket

3354. **[datawrapper-mcp](https://github.com/palewire/datawrapper-mcp)** - ⭐ 40
   A Model Context Protocol (MCP) server and app for creating Datawrapper charts using AI assistants.

3355. **[mcp-panther](https://github.com/panther-labs/mcp-panther)** - ⭐ 40
   Write detections, investigate alerts, and query logs from your favorite AI agents

3356. **[mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server)** - ⭐ 40
   Model Context Protocol (MCP) server for Databricks that empowers AI agents to autonomously interact with Unity Catalog metadata. Enables data discovery, lineage analysis, and intelligent SQL execution. Agents explore catalogs/schemas/tables, understand relationships, discover notebooks/jobs, and execute queries - greatly reducing ad-hoc query time.

3357. **[forgejo-mcp](https://github.com/raohwork/forgejo-mcp)** - ⭐ 40
   A MCP server that enables you to manage Gitea/Forgejo repositories through AI assistants

3358. **[McpDotNet.Extensions.SemanticKernel](https://github.com/StefH/McpDotNet.Extensions.SemanticKernel)** - ⭐ 40
   Microsoft SemanticKernel integration for the Model Context Protocol (MCP). Enables seamless use of MCP tools as AI functions.

3359. **[just-mcp](https://github.com/toolprint/just-mcp)** - ⭐ 40
   Share the same project justfile tasks with your AI Coding Agent.

3360. **[apple-books-mcp](https://github.com/vgnshiyer/apple-books-mcp)** - ⭐ 40
   Apple Books MCP Server

3361. **[asc-mcp](https://github.com/zelentsov-dev/asc-mcp)** - ⭐ 40
   MCP server for App Store Connect API - 389 tools for apps, builds, TestFlight, subscriptions, Xcode Cloud, and more from Claude, Cursor, VS Code, or any MCP client

3362. **[onec-client-mcp-devkit](https://github.com/1c-neurofish/onec-client-mcp-devkit)** - ⭐ 39
   Реализация MCP сервера, который запускается в клиенте 1С:Предприятие

3363. **[whistle-mcp](https://github.com/7gugu/whistle-mcp)** - ⭐ 39
   A Whistle proxy management tool based on Model Context Protocol that allows AI assistants to directly control local Whistle proxy servers, simplifying network debugging, API testing, and proxy rule configuration through natural language interaction.

3364. **[agience-core](https://github.com/Agience/agience-core)** - ⭐ 39
   The operating system that AI workflows trust. Structure messy inputs. Establish identity. Track provenance. Build the durable data layer your AI workflows need to be trusted, reusable, and auditable.

3365. **[photoshop-mcp](https://github.com/alisaitteke/photoshop-mcp)** - ⭐ 39
   MCP server for Adobe Photoshop automation - Control Photoshop from AI assistants with 50+ tools for design, image editing, and workflow automation

3366. **[arifosmcp](https://github.com/ariffazil/arifosmcp)** - ⭐ 39
   ArifOS — AAA MCP-governed constitutional kernel for AI agents.

3367. **[mysql-mcp-server](https://github.com/askdba/mysql-mcp-server)** - ⭐ 39
   MySQL Server implementation for Model Context Protocol (MCP) written in Go.

3368. **[mcp-caiyun-weather](https://github.com/caiyunapp/mcp-caiyun-weather)** - ⭐ 39
   A Model Context Protocol (MCP) server for Caiyun (ColorfulClouds) Weather.

3369. **[chatwork-mcp-server](https://github.com/chatwork/chatwork-mcp-server)** - ⭐ 39
   ChatworkをAIから操作するためのMCP(Model Context Protocol)サーバー

3370. **[mcp-client-server-host-demo](https://github.com/danwritecode/mcp-client-server-host-demo)** - ⭐ 39
   A quick pokemon demo to showcase MCP server, client, and host

3371. **[mssql-mcp](https://github.com/daobataotie/mssql-mcp)** - ⭐ 39
   mssql mcp server

3372. **[DecisionNode](https://github.com/decisionnode/DecisionNode)** - ⭐ 39
   CLI + Local MCP - A shared structured memory store across Claude Code, Cursor, Windsurf, Antigravity, and every MCP client. Semantically queryable.

3373. **[search-scrape](https://github.com/DevsHero/search-scrape)** - ⭐ 39
   Self-hosted Stealth Scraping & Federated Search for AI Agents. A 100% private, free alternative to Firecrawl, Jina Reader, and Tavily. Featuring Universal Anti-bot Bypass + Semantic Research Memory, Copy-Paste setup

3374. **[mcp-graph-workflow](https://github.com/DiegoNogueiraDev/mcp-graph-workflow)** - ⭐ 39
   MCP local-first CLI tool that converts PRD text files into persistent execution graphs (SQLite) for structured agentic workflows

3375. **[vscode-agent-todos](https://github.com/digitarald/vscode-agent-todos)** - ⭐ 39
   Gives VS Code agent mode planning superpowers with dynamic todo lists

3376. **[help-scout-mcp-server](https://github.com/drewburchfield/help-scout-mcp-server)** - ⭐ 39
   MCP server for Help Scout - search conversations, threads, and inboxes with AI agents

3377. **[mcp_code_analyzer](https://github.com/emiryasar/mcp_code_analyzer)** - ⭐ 39
   A Model Context Protocol (MCP) server implementation for comprehensive code analysis. This tool integrates with Claude Desktop to provide code analysis capabilities through natural language interactions.

3378. **[codesearch](https://github.com/flupkede/codesearch)** - ⭐ 39
   Multi-repo semantic code search MCP server in Rust — hybrid vector + BM25 retrieval, tree-sitter AST chunking, fully offline. For OpenCode, Claude Code, Cursor, and any MCP client.

3379. **[middy-mcp](https://github.com/fredericbarthelet/middy-mcp)** - ⭐ 39
   Middy middleware for Model Context Protocol server hosting on AWS Lambda

3380. **[hass-mcp-server](https://github.com/ganhammar/hass-mcp-server)** - ⭐ 39
   A Home Assistant Custom Component that provides an MCP (Model Context Protocol) server using HTTP transport, allowing AI assistants like Claude to interact with your Home Assistant instance over HTTP

3381. **[mcpmc](https://github.com/gerred/mcpmc)** - ⭐ 39
   Model Context Protocol Minecraft Server

3382. **[agent-inbox](https://github.com/gsd-build/agent-inbox)** - ⭐ 39
   Give any AI agent a disposable email inbox in one tool call. MCP server for email verification, auth flows, and testing.

3383. **[pentester-mcp](https://github.com/halilkirazkaya/pentester-mcp)** - ⭐ 39
   Elevate your AI assistants (like Claude & Cursor) into autonomous cybersecurity experts. Pentester-MCP integrates 200+ pentesting tools via the Model Context Protocol (MCP) using a secure Docker sandbox.

3384. **[mcp-browser-agent](https://github.com/imprvhub/mcp-browser-agent)** - ⭐ 39
   A Model Context Protocol (MCP) integration that provides Claude Desktop with autonomous browser automation capabilities. This agent enables Claude to interact with web content, manipulate DOM elements, execute JavaScript, and perform API requests.

3385. **[pbixray-mcp-server](https://github.com/jonaolden/pbixray-mcp-server)** - ⭐ 39
   MCP server to give llms such as Claude, GitHub Copilot etc full PowerBI model context (from input .pbix) through tools based on PBIXRay python package.

3386. **[dotcom.chat](https://github.com/kamath/dotcom.chat)** - ⭐ 39
   A simple NextJS MCP client with sensible keybindings

3387. **[browser-use-mcp-client](https://github.com/Linzo99/browser-use-mcp-client)** - ⭐ 39
   A MCP client for browser-use

3388. **[markifact-mcp](https://github.com/markifact/markifact-mcp)** - ⭐ 39
   MCP server for Google Ads, Meta Ads, GA4, TikTok Ads, and LinkedIn Ads. Manage 300+ ad operations from Claude, ChatGPT, Gemini, Cursor, or any AI client. Human-in-the-loop on every write.

3389. **[storybook-mcp](https://github.com/mcpland/storybook-mcp)** - ⭐ 39
   A MCP server for Storybook.

3390. **[anki-mcp](https://github.com/nietus/anki-mcp)** - ⭐ 39
   MCP server for anki

3391. **[imap-mcp-server](https://github.com/nikolausm/imap-mcp-server)** - ⭐ 39
   A powerful Model Context Protocol (MCP) server for IMAP email integration with Claude

3392. **[mcp-dblp](https://github.com/szeider/mcp-dblp)** - ⭐ 39
   A Model Context Protocol (MCP) server that provides access to the DBLP computer science bibliography database for Large Language Models.

3393. **[best-of-mcp-servers](https://github.com/tolkonepiu/best-of-mcp-servers)** - ⭐ 39
   🏆  A ranked list of MCP servers. Updated weekly.

3394. **[mcp-crypto-price](https://github.com/truss44/mcp-crypto-price)** - ⭐ 39
   A Model Context Protocol (MCP) server that provides real-time cryptocurrency analysis via CoinCap's API. Enables Claude and other MCP clients to fetch crypto prices, analyze market trends, and track historical data.

3395. **[steampipe-mcp](https://github.com/turbot/steampipe-mcp)** - ⭐ 39
   Enable AI assistants to explore and query your Steampipe data!

3396. **[vulnerablemcp](https://github.com/vineethsai/vulnerablemcp)** - ⭐ 39
   A comprehensive database of Model Context Protocol vulnerabilities, security research, and exploits

3397. **[MCP-Microsoft-Office](https://github.com/Aanerud/MCP-Microsoft-Office)** - ⭐ 38
   an local MCP server you can run on your env, connecting you to Microsoft Graph, and the complete M365 eco system.

3398. **[nostr-mcp](https://github.com/AbdelStark/nostr-mcp)** - ⭐ 38
   A Nostr MCP server that allows to interact with Nostr, enabling posting notes, and more.

3399. **[awesome-devops-mcp](https://github.com/agenticdevops/awesome-devops-mcp)** - ⭐ 38
   List of Awesome MCP Servers and Clients for building Agentic Devops

3400. **[awesome-hermes-usecases](https://github.com/aliaihub/awesome-hermes-usecases)** - ⭐ 38
   Curated real-world use cases for Hermes Agent — the self-improving AI agent from Nous Research. Backed by primary sources.

3401. **[MCPDocSearch](https://github.com/alizdavoodi/MCPDocSearch)** - ⭐ 38
   This project provides a toolset to crawl websites wikis, tool/library documentions and generate Markdown documentation, and make that documentation searchable via a Model Context Protocol (MCP) server, designed for integration with tools like Cursor.

3402. **[protonmail-mcp](https://github.com/amotivv/protonmail-mcp)** - ⭐ 38
   This MCP server provides email sending functionality using Protonmail's SMTP service. It allows both Claude Desktop and Cline VSCode extension to send emails on your behalf using your Protonmail credentials.

3403. **[mcp-appstore](https://github.com/appreply-co/mcp-appstore)** - ⭐ 38
   This is an MCP server that provides tools to LLMs for searching and analyzing apps from both Google Play Store and Apple App Store – perfect for ASO.

3404. **[Web-Algebra](https://github.com/AtomGraph/Web-Algebra)** - ⭐ 38
   Suite of generic Linked Data/SPARQL as well as LinkedDataHub-specific MCP tools

3405. **[mcp-wasm](https://github.com/beekmarks/mcp-wasm)** - ⭐ 38
   A proof-of-concept implementation of a Model Context Protocol (MCP) server that runs in WebAssembly (WASM) within a web browser. This project demonstrates the integration of MCP tools and resources in a browser environment.

3406. **[context-awesome](https://github.com/bh-rat/context-awesome)** - ⭐ 38
   awesome-lists now available as MCP server for you agent.

3407. **[Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server)** - ⭐ 38
   A Model Context Protocol (MCP) server that integrates Volatility 3 memory forensics framework with Claude

3408. **[x64dbg_mcp](https://github.com/bromoket/x64dbg_mcp)** - ⭐ 38
   MCP server for x64dbg — 152 AI-powered debugging tools. Works with Claude, Cursor, Windsurf, Cline. Reverse engineering with AI.

3409. **[OpenInsider-MCP](https://github.com/btopn/OpenInsider-MCP)** - ⭐ 38
   MCP server that exposes openinsider.com to any MCP compatible client.

3410. **[TIA_Portal_Openness_MCP](https://github.com/bulaofen0036-coder/TIA_Portal_Openness_MCP)** - ⭐ 38
   Drive Siemens TIA Portal V20/V21 (STEP 7, WinCC Unified) from any MCP client — create projects, generate PLC & HMI, compile & diagnose. Prebuilt runtime, no Openness coding required.

3411. **[ContextPods](https://github.com/conorluddy/ContextPods)** - ⭐ 38
   Model Context Protocol management suite/factory. An MCP that can generate and manage other local MCPs in multiple languages. Uses the official SDKs for code gen.

3412. **[HAL](https://github.com/DeanWard/HAL)** - ⭐ 38
   HAL (HTTP API Layer) is a Model Context Protocol (MCP) server that provides HTTP API capabilities to Large Language Models.

3413. **[FastAPI-BitNet](https://github.com/grctest/FastAPI-BitNet)** - ⭐ 38
   Running Microsoft's BitNet inference framework via FastAPI, Uvicorn and Docker.

3414. **[openecon-data](https://github.com/hanlulong/openecon-data)** - ⭐ 38
   Give your AI agent accurate economic data. 330K indicators from FRED, World Bank, IMF, Eurostat & more. MCP server + web UI.

3415. **[openbim-mcp](https://github.com/helenkwok/openbim-mcp)** - ⭐ 38
   Model Context Protocol (MCP) server for openBIM

3416. **[nestjs-starter](https://github.com/hmake98/nestjs-starter)** - ⭐ 38
   Production-ready NestJS boilerplate with JWT auth, PostgreSQL/Prisma, AWS S3/SES, Bull/Redis queues, Docker/K8s support, and MCP integration for AI capabilities

3417. **[mcp-governance-sdk](https://github.com/ithena-one/mcp-governance-sdk)** - ⭐ 38
   Enterprise Governance Layer (Identity, RBAC, Credentials, Auditing, Logging, Tracing) for the Model Context Protocol SDK

3418. **[puppeteer-mcp-claude](https://github.com/jaenster/puppeteer-mcp-claude)** - ⭐ 38
   A Model Context Protocol (MCP) server that provides Claude Code with comprehensive browser automation capabilities through Puppeteer

3419. **[vancouver](https://github.com/jameslong/vancouver)** - ⭐ 38
   Simple MCP server library for Elixir.

3420. **[kitwork](https://github.com/kitwork/kitwork)** - ⭐ 38
   Automate kit workflows effortlessly with a lightweight, high-performance, fast, and flexible engine for cloud or self-hosted environments.

3421. **[File-Organizer-MCP](https://github.com/kridaydave/File-Organizer-MCP)** - ⭐ 38
   This MCP server will organize your files using connections to MCP using clients like Claude, Cursor and Gemini Cli

3422. **[comfy-mcp-server](https://github.com/lalanikarim/comfy-mcp-server)** - ⭐ 38
   A server using FastMCP framework to generate images based on prompts via a remote Comfy server.

3423. **[levante](https://github.com/levante-hub/levante)** - ⭐ 38
   Levante - Personal, Secure, Free, Local AI, MCP Client

3424. **[Outlook_Calendar_MCP](https://github.com/merajmehrabi/Outlook_Calendar_MCP)** - ⭐ 38
   A Model Context Protocol (MCP) server that allows Claude to access and manage your local Microsfot Outlook calendar (Windows only).

3425. **[mcp-toolkit](https://github.com/metosin/mcp-toolkit)** - ⭐ 38
   a lib to build MCP clients and MCP servers in Clojure(script)

3426. **[shadcn-svelte-mcp](https://github.com/Michael-Obele/shadcn-svelte-mcp)** - ⭐ 38
   Mastra MCP server and tooling for the shadcn-svelte component docs and developer utilities.

3427. **[octomind](https://github.com/Muvon/octomind)** - ⭐ 38
   Highly configurable autonomous efficient-first agentic AI framework for CLI

3428. **[How-To-Create-MCP-Server](https://github.com/nisalgunawardhana/How-To-Create-MCP-Server)** - ⭐ 38
   This guide will help you set up a basic MCP (Model Context Protocol) server in .NET, configure it in VS Code, and interact with it using Copilot Chat.

3429. **[mcp-go](https://github.com/riza-io/mcp-go)** - ⭐ 38
   Build Model Context Protocol (MCP) servers in Go

3430. **[mcp_ctl](https://github.com/runablehq/mcp_ctl)** - ⭐ 38
   A package manager to manage all your mcp servers across platforms

3431. **[Mcp.Net](https://github.com/SamFold/Mcp.Net)** - ⭐ 38
   A fully featured C# implementation of Anthropic's Model Context Protocol (MCP)

3432. **[cdk_pywrapper](https://github.com/sebotic/cdk_pywrapper)** - ⭐ 38
   A Python wrapper for the Chemistry Development Kit (CDK)

3433. **[mocxykit](https://github.com/shunseven/mocxykit)** - ⭐ 38
   This is an Frontend development service middleware that can be used with webpack and vite. Its main function is to visualize the configuration, manage http(s)-proxy, and mock data.

3434. **[DeepCo](https://github.com/succlz123/DeepCo)** - ⭐ 38
   A Chat Client for LLMs, written in Compose Multiplatform.

3435. **[prompt-decorators](https://github.com/synaptiai/prompt-decorators)** - ⭐ 38
   A standardized framework for enhancing how LLMs process and respond to prompts through composable decorators, featuring an official open standard specification and Python reference implementation with MCP server integration.

3436. **[sunnysideFigma-Context-MCP](https://github.com/tercumantanumut/sunnysideFigma-Context-MCP)** - ⭐ 38
   A comprehensive Model Context Protocol (MCP) server that bridges Figma designs with AI development workflows. It provides 30 specialized tools for extracting pixel-perfect code, assets, and component structures directly from Figma designs.

3437. **[matlab-mcp](https://github.com/Tsuchijo/matlab-mcp)** - ⭐ 38
   Model Context Protocol server to let LLMs write and execute matlab scripts

3438. **[crawl-mcp](https://github.com/wutongci/crawl-mcp)** - ⭐ 38
   完整的微信文章抓取MCP服务器 - 基于Model Context Protocol (MCP)的智能网页抓取工具，专为Cursor IDE和AI工具设计。

3439. **[zscaler-mcp-server](https://github.com/zscaler/zscaler-mcp-server)** - ⭐ 38
   Zscaler Integration MCP Server is a Model Context Protocol (MCP) server designed for managing Several Zscaler Products using Large Language Models (LLMs).

3440. **[code-mcp](https://github.com/54yyyu/code-mcp)** - ⭐ 37
   Code-MCP: Connect Claude AI to your development environment through the Model Context Protocol (MCP), enabling terminal commands and file operations through the AI interface.

3441. **[mssqlclient-mcp-server](https://github.com/aadversteeg/mssqlclient-mcp-server)** - ⭐ 37
   A Microsoft SQL Server client implementing the Model Context Protocol (MCP). This server provides SQL query capabilities through a simple MCP interface.

3442. **[codex-claude-bridge](https://github.com/abhishekgahlot2/codex-claude-bridge)** - ⭐ 37
   Bidirectional bridge between Claude Code and OpenAI Codex CLI. Built on Claude Code Channels. Two AI agents, one conversation, real-time web UI.

3443. **[apisix-mcp](https://github.com/api7/apisix-mcp)** - ⭐ 37
   APISIX Model Context Protocol (MCP) server is used to bridge large language models (LLMs) with the APISIX Admin API.

3444. **[apra-fleet](https://github.com/Apra-Labs/apra-fleet)** - ⭐ 37
   AI agents that write code, review each other's work, and coordinate across your machines

3445. **[trivy-mcp](https://github.com/aquasecurity/trivy-mcp)** - ⭐ 37
   Trivy plugin for starting an MCP server

3446. **[mcp-client-example](https://github.com/artemnovichkov/mcp-client-example)** - ⭐ 37
   Learn how to implement MCP client with SwiftUI and Anthropic API

3447. **[aio-mcp](https://github.com/athapong/aio-mcp)** - ⭐ 37
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows. Folk from https://github.com/nguyenvanduocit/all-in-one-model-context-protocol

3448. **[offeryn](https://github.com/avahowell/offeryn)** - ⭐ 37
   Build tools for LLMs in Rust using Model Context Protocol

3449. **[browser-use-rs](https://github.com/BB-fat/browser-use-rs)** - ⭐ 37
   A Rust library for browser automation via Chrome DevTools Protocol with built-in AI integration through Model Context Protocol (MCP)

3450. **[awesome-mcp-hardware](https://github.com/beriberikix/awesome-mcp-hardware)** - ⭐ 37
   Awesome list of MCP servers for interacting with hardware and the physical world.

3451. **[FastDomainCheck-MCP-Server](https://github.com/bingal/FastDomainCheck-MCP-Server)** - ⭐ 37
   A Model Context Protocol for checking domain name registration status in bulk.

3452. **[mcp-summarization-functions](https://github.com/Braffolk/mcp-summarization-functions)** - ⭐ 37
   Provides summarised output from various actions that could otherwise eat up tokens and cause crashes for AI agents

3453. **[mcp-file-context-server](https://github.com/bsmi021/mcp-file-context-server)** - ⭐ 37
   A Model Context Protocol (MCP) server that provides file system context to Large Language Models (LLMs). This server enables LLMs to read, search, and analyze code files with advanced caching and real-time file watching capabilities.

3454. **[mcp_xpp](https://github.com/ccampora/mcp_xpp)** - ⭐ 37
   Experimental MCP server for Dynamics 365 F&O X++ development. Provides object creation, modification, and codebase navigation through the Model Context Protocol. Includes VS2022 service integration for D365 object handling.

3455. **[tasker-mcp](https://github.com/dceluis/tasker-mcp)** - ⭐ 37
   An MCP server for Android's Tasker automation app.

3456. **[review-flow](https://github.com/DGouron/review-flow)** - ⭐ 37
   Automated AI code reviews powered — webhook-driven, real-time dashboard, MCP integration, smart queue with deduplication, multi-agent audits, and iterative follow-up reviews for GitLab MRs and GitHub PRs

3457. **[google-workspace-mcp](https://github.com/dguido/google-workspace-mcp)** - ⭐ 37
   MCP server for Google Drive, Docs, Sheets, Slides, Calendar, Gmail, and Contacts

3458. **[gemini-superclaude-mcp-server](https://github.com/Dianel555/gemini-superclaude-mcp-server)** - ⭐ 37
   A **complete rewrite** of the original SuperClaude MCP server with intelligent command routing, dynamic persona switching, and real MCP server orchestration for Gemini CLI.Th

3459. **[univer-mcp](https://github.com/dream-num/univer-mcp)** - ⭐ 37
   AI-powered spreadsheet automation through Model Context Protocol (MCP) server for Univer

3460. **[mcp-mistral-ocr](https://github.com/everaldo/mcp-mistral-ocr)** - ⭐ 37
   Model Context Protocol (MCP) Server for Mistral OCR API

3461. **[mcp](https://github.com/fastly/mcp)** - ⭐ 37
   Model Context Protocol (MCP) server for AI-powered Fastly CDN management.

3462. **[okta-mcp-server](https://github.com/fctr-id/okta-mcp-server)** - ⭐ 37
   The Okta MCP Server is a groundbreaking tool built by the team at Fctr that enables AI models to interact directly with your Okta environment using the Model Context Protocol (MCP). Built specifically for IAM engineers, security teams, and Okta administrators, it implements the MCP specification to help work with Okta enitities

3463. **[mcp-debug](https://github.com/giantswarm/mcp-debug)** - ⭐ 37
   Command-line tool for debugging MCP servers

3464. **[godot-mcp](https://github.com/HaD0Yun/godot-mcp)** - ⭐ 37
   GoPeak — The most comprehensive MCP server for Godot Engine. 95+ tools: scene management, GDScript LSP, DAP debugger, screenshot capture, input injection, ClassDB introspection, CC0 asset library. npx gopeak

3465. **[anythingmcp](https://github.com/HelpCode-ai/anythingmcp)** - ⭐ 37
   Self-hosted MCP gateway & API-to-MCP bridge. Convert REST/SOAP/WSDL/GraphQL/SQL APIs into MCP servers for Claude, ChatGPT, Gemini, Copilot, Cursor. OpenAPI/Postman/WSDL import, OAuth2, RBAC, audit log. 29 pre-built adapters (DHL, DATEV, Weclapp, Personio, Handelsregister, Shopware...). Source-available.

3466. **[mcp-starter](https://github.com/instructa/mcp-starter)** - ⭐ 37
   A super simple Starter to build your own MCP Server

3467. **[youtrack-mcp](https://github.com/itsalfredakku/youtrack-mcp)** - ⭐ 37
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

3468. **[apipost-mcp](https://github.com/jlcodes99/apipost-mcp)** - ⭐ 37
   ApiPost API management tool based on MCP (Model Context Protocol), supporting complete interface documentation management and team collaboration. Features intelligent search, batch operations, and security management.

3469. **[AskUserQuestionPlus](https://github.com/JoJoJotarou/AskUserQuestionPlus)** - ⭐ 37
   A MCP server (Streamable HTTP) for asking user questions via a web interface, inspired by the Claude Code AskUserQuestion Tool.

3470. **[example-mcp-server](https://github.com/kirill-markin/example-mcp-server)** - ⭐ 37
   A ready-to-use MCP (Model Context Protocol) server template for extending Cursor IDE with custom tools. Deploy your own server to Heroku with one click, create custom commands, and enhance your Cursor IDE experience. Perfect for developers who want to add their own tools and commands to Cursor IDE without complex setup.

3471. **[flutter-mcp-ai-chat](https://github.com/leehack/flutter-mcp-ai-chat)** - ⭐ 37
   Demonstrate how to implement MCP Client in Flutter application with AI.

3472. **[agentic-commerce-protocol-demo](https://github.com/locus-technologies/agentic-commerce-protocol-demo)** - ⭐ 37
   Reference implementation of OpenAI's Agentic Commerce Protocol (ACP)

3473. **[coin_api_mcp](https://github.com/longmans/coin_api_mcp)** - ⭐ 37
   A Model Context Protocol server that provides access to CoinMarketCap's cryptocurrency data. This server enables AI-powered applications to retrieve cryptocurrency listings, quotes, and detailed information about various coins.

3474. **[MCP-Packet-Tracer](https://github.com/Mats2208/MCP-Packet-Tracer)** - ⭐ 37
   AI-powered Cisco Packet Tracer automation using MCP. Generate, validate and deploy full network topologies (OSPF, DHCP, EIGRP, RIP) from natural language prompts.

3475. **[OmniClip-RAG](https://github.com/msjsc001/OmniClip-RAG)** - ⭐ 37
   Local-first RAG desktop app & official MCP Server. Let any AI instantly search your private Markdown, PDF, and 1290+ document formats. (本地优先的 RAG 桌面端与官方 MCP 服务器。让任意 AI 瞬间检索你的私有 Markdown、PDF 及 1290+ 种文档格式。)

3476. **[mcp-windows-automation](https://github.com/mukul975/mcp-windows-automation)** - ⭐ 37
   🚀 AI-Powered Windows Automation Server using Model Context Protocol (MCP) | Control Windows apps, automate tasks, and manage systems through natural language commands with Claude, ChatGPT & other AI assistants | 80+ automation tools

3477. **[narwhal](https://github.com/Nonanti/narwhal)** - ⭐ 37
   Multi-driver TUI database client with a built-in MCP server. Six databases (postgres, mysql, sqlite, duckdb, clickhouse, mssql), vim editing, Lua + WASM plugins, schema diff, audit log.

3478. **[odoo-mcp-pro](https://github.com/pantalytics/odoo-mcp-pro)** - ⭐ 37
   AI connector for Odoo ERP | Connect Claude, ChatGPT, Cursor and other AI tools to Odoo via MCP

3479. **[meshy-ai-mcp-server](https://github.com/pasie15/meshy-ai-mcp-server)** - ⭐ 37
   This is a Model Context Protocol (MCP) server for interacting with the Meshy AI API. It provides tools for generating 3D models from text and images, applying textures, and remeshing models.

3480. **[mcp-server-webcrawl](https://github.com/pragmar/mcp-server-webcrawl)** - ⭐ 37
   MCP server tailored to connecting web crawler data and archives

3481. **[mcp-security-inspector](https://github.com/purpleroc/mcp-security-inspector)** - ⭐ 37
   一个用于检测Model Context Protocol (MCP)安全性的Chrome扩展工具。

3482. **[GDB-MCP](https://github.com/smadi0x86/GDB-MCP)** - ⭐ 37
   An MCP server that enables LLMs to interact with GDB and LLDB for binary debugging and analysis.

3483. **[openrouter-mcp-multimodal](https://github.com/stabgan/openrouter-mcp-multimodal)** - ⭐ 37
   MCP server for OpenRouter — chat with 300+ LLMs (Claude, Gemini, GPT), analyze images / audio / video, generate images / speech / music / video (Veo 3.1, Sora, Seedance, Wan) from Claude Desktop, Cursor, Kiro, VS Code.

3484. **[ssh-mcp-server](https://github.com/uarlouski/ssh-mcp-server)** - ⭐ 37
   A secure, production-ready Model Context Protocol (MCP) server that empowers AI assistants to manage remote infrastructure via SSH.

3485. **[llm-tools-mcp](https://github.com/VirtusLab/llm-tools-mcp)** - ⭐ 37
   Connect to MCP servers right from your shell. Plugin for simonw/llm.

3486. **[ziya](https://github.com/ziya-ai/ziya)** - ⭐ 37
   Self-hosted AI technical workbench. Visual, persistent, multi-stream. Development, architecture, and operational analytics without losing context.

3487. **[MCPNotes](https://github.com/9Ninety/MCPNotes)** - ⭐ 36
   A simple note-taking MCP server for recording and managing notes with AI models.

3488. **[mcp-crew-ai](https://github.com/adam-paterson/mcp-crew-ai)** - ⭐ 36
   MCP Crew AI Server is a lightweight Python-based server designed to run, manage and create CrewAI workflows.

3489. **[drafts-mcp-server](https://github.com/agiletortoise/drafts-mcp-server)** - ⭐ 36
   Model Context Protocol for Drafts

3490. **[Handler](https://github.com/alDuncanson/Handler)** - ⭐ 36
   A2A Protocol client and developer toolkit.

3491. **[mcp-server-antv](https://github.com/antvis/mcp-server-antv)** - ⭐ 36
   🧑🏻‍💻 MCP Server for @antvis visualization development, which provides documentation context and examples for visualization developers.

3492. **[nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server)** - ⭐ 36
   A Model Context Protocol (MCP) server that provides Nostr capabilities to AI agents

3493. **[azure-functions-mcp-extension](https://github.com/Azure/azure-functions-mcp-extension)** - ⭐ 36
   Model Context Protocol extension for Azure Functions.

3494. **[mcp-server-text-editor](https://github.com/bhouston/mcp-server-text-editor)** - ⭐ 36
   An open source implementation of the Claude built-in text editor tool

3495. **[mcp-superset](https://github.com/bintocher/mcp-superset)** - ⭐ 36
   MCP server for managing Apache Superset — 128+ tools for dashboards, charts, datasets, SQL Lab, access control

3496. **[ChatSpatial](https://github.com/cafferychen777/ChatSpatial)** - ⭐ 36
   MCP server for spatial transcriptomics analysis through natural language interfaces.

3497. **[ronykit](https://github.com/clubpay/ronykit)** - ⭐ 36
   API Framework supporting REST and RPC.

3498. **[esa-mcp-server](https://github.com/d-kimuson/esa-mcp-server)** - ⭐ 36
   esa の Model Context Protocol サーバー実装

3499. **[ai-workshop](https://github.com/dotnet-presentations/ai-workshop)** - ⭐ 36
   Building GenAI Apps in C#: AI Templates, GitHub Models, Azure OpenAI & More

3500. **[turbomcpstudio](https://github.com/Epistates/turbomcpstudio)** - ⭐ 36
   A native desktop application for developing, testing, and debugging Model Context Protocol servers.

3501. **[authenticator_mcp](https://github.com/firstorderai/authenticator_mcp)** - ⭐ 36
   A secure MCP (Model Context Protocol) server that enables AI agents to interact with the Authenticator App.

3502. **[pfsense-mcp-server](https://github.com/gensecaihq/pfsense-mcp-server)** - ⭐ 36
   pfSense MCP Server enables security administrators to manage their pfSense firewalls using natural language through AI assistants like Claude Desktop. Simply ask "Show me blocked IPs" or "Run a PCI compliance check" instead of navigating complex interfaces. Supports REST/XML-RPC/SSH connections, and includes built-in complian

3503. **[wezterm-mcp](https://github.com/hiraishikentaro/wezterm-mcp)** - ⭐ 36
   About A Model Context Protocol server that executes commands in the current WezTerm session

3504. **[metabase-mcp-server](https://github.com/hyeongjun-dev/metabase-mcp-server)** - ⭐ 36
   A Model Context Protocol server that integrates AI assistants with Metabase analytics platform

3505. **[MCPSwiftWrapper](https://github.com/jamesrochabrun/MCPSwiftWrapper)** - ⭐ 36
   A light wrapper around mcp-swift-sdk for easy usage of MCP clients in Swift

3506. **[mcp-sandbox](https://github.com/JohanLi233/mcp-sandbox)** - ⭐ 36
   Python sandboxes for llms

3507. **[metals-standalone-client](https://github.com/jpablo/metals-standalone-client)** - ⭐ 36
   Minimal Metals stand alone client that allows running the metals mcp server

3508. **[workflowy](https://github.com/mholzen/workflowy)** - ⭐ 36
   Powerful CLI and MCP server for WorkFlowy: reports, search/replace, backup support, and AI integration (Claude, LLMs)

3509. **[ue5-mcp](https://github.com/mirno-ehf/ue5-mcp)** - ⭐ 36
   Let AI edit your Unreal Engine Blueprints. MCP server plugin for Claude Code — describe what you want in plain English.

3510. **[universal-crypto-mcp](https://github.com/nirholas/universal-crypto-mcp)** - ⭐ 36
   Universal MCP server for AI agents to interact with any* blockchain via natural language and plugins. Supports swaps, bridges, gas, staking, lending, and more across Ethereum, Arbitrum, Base, Polygon, BSC, and testnets.

3511. **[mcp-gateway](https://github.com/openziti/mcp-gateway)** - ⭐ 36
   Zero trust gateway for MCP servers. Aggregate, filter, and securely access MCP tools from anywhere without VPNs, open ports, or exposed endpoints. Built on OpenZiti, zrok, and Agora with cryptographic identity, mTLS, per-client isolation, and tool-level permission control.

3512. **[apple-mail-mcp](https://github.com/patrickfreyer/apple-mail-mcp)** - ⭐ 36
   MCP server giving AI assistants full access to Apple Mail - read, search, compose, organize & analyze emails via natural language

3513. **[chabeau](https://github.com/permacommons/chabeau)** - ⭐ 36
   OpenAI-API compatible terminal chatbot and MCP client in Rust

3514. **[copilot-security-instructions](https://github.com/Robotti-io/copilot-security-instructions)** - ⭐ 36
   ✨ A customizable copilot-instructions.md ruleset & prompts to guide GitHub Copilot toward secure coding defaults in Java, Node.js, C# and Python. Blocks risky patterns, teaches safe habits.

3515. **[awesome-blockchain-mcps](https://github.com/royyannick/awesome-blockchain-mcps)** - ⭐ 36
   🔗 A curated list of Blockchain & Crypto Model Context Protocol (MCP) servers. Enabling AI Agents to interact with the Blockchain, Web3, DeFi, on-chain data, on-chain actions, etc.  🚀

3516. **[lucide-icons-mcp](https://github.com/SeeYangZhi/lucide-icons-mcp)** - ⭐ 36
   A Model Context Protocol (MCP) server exposing Lucide icons as resources and tools for LLMs and agentic applications. Built with Bun and the MCP TypeScript SDK.

3517. **[framer-plugin-mcp](https://github.com/Sheshiyer/framer-plugin-mcp)** - ⭐ 36
   A Model Context Protocol (MCP) server for creating and managing Framer plugins with web3 capabilities

3518. **[OmniMind](https://github.com/Techiral/OmniMind)** - ⭐ 36
   OmniMind: An open-source Python library for effortless MCP (Model Context Protocol) integration, AI Agents, AI workflows, and AI Automations. Plug & Play AI Tools for MCP Servers and Clients, powered by Google Gemini.

3519. **[awesome-mcp-personas](https://github.com/toolprint/awesome-mcp-personas)** - ⭐ 36
   A curated collection of persona-based mcp server & tool groupings.

3520. **[mcp-anything](https://github.com/Type-MCP/mcp-anything)** - ⭐ 36
   One command to turn any codebase into an MCP server

3521. **[mcp-server](https://github.com/VapiAI/mcp-server)** - ⭐ 36
   Vapi MCP Server

3522. **[OmnifocusMCP](https://github.com/vitalyrodnenko/OmnifocusMCP)** - ⭐ 36
   Model Context Protocol (MCP) server for OmniFocus on macOS, with Rust, Python, and TypeScript implementations

3523. **[baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server)** - ⭐ 36
   特定のWeb APIに関するBaselineの状況を提供するModel Context Protocolサーバー

3524. **[overleaf-mcp-server](https://github.com/YounesBensafia/overleaf-mcp-server)** - ⭐ 36
   MCP server for Overleaf projects. Syncs LaTeX files via Git, parses sections, equations, and citations, and exposes them to AI clients for assisted paper review, LaTeX fixes, and content generation.

3525. **[mcp-registry](https://github.com/ARadRareness/mcp-registry)** - ⭐ 35
   A central registry and HTTP interface for coordinating Model Context Protocol (MCP) servers.

3526. **[openai-mcp](https://github.com/arthurcolle/openai-mcp)** - ⭐ 35
   OpenAI Code Assistant Model Context Protocol (MCP) Server

3527. **[AlphaFold-MCP-Server](https://github.com/Augmented-Nature/AlphaFold-MCP-Server)** - ⭐ 35
   A comprehensive Model Context Protocol (MCP) server that provides access to the AlphaFold Protein Structure Database through a rich set of tools and resources for protein structure prediction analysis.

3528. **[mcp-tung-shing](https://github.com/baranwang/mcp-tung-shing)** - ⭐ 35
   中国传统黄历 MCP 服务 | Chinese Traditional Almanac MCP Service

3529. **[daisyui-mcp](https://github.com/birdseyevue/daisyui-mcp)** - ⭐ 35
   🌼 A token-friendly local MCP server for DaisyUI component documentation using their public llms.txt.

3530. **[mcp-gemini-server](https://github.com/bsmi021/mcp-gemini-server)** - ⭐ 35
   This project provides a dedicated MCP (Model Context Protocol) server that wraps the @google/genai SDK. It exposes Google's Gemini model capabilities as standard MCP tools, allowing other LLMs (like Cline) or MCP-compatible systems to leverage Gemini's features as a backend workhorse.

3531. **[atlas-docs-mcp](https://github.com/CartographAI/atlas-docs-mcp)** - ⭐ 35
   Provide LLMs hosted, clean markdown documentation of libraries and frameworks

3532. **[korean-dart-mcp](https://github.com/chrisryugj/korean-dart-mcp)** - ⭐ 35
   OpenDART 전자공시MCP | 83개 API → 15 MCP 도구. 공시·재무·지분·XBRL + 버핏급 애널리스트 프레임(내부자 시그널·회계 리스크·퀄리티 체크리스트) + HWP/PDF 첨부 마크다운화 | 83 Korean DART disclosure APIs → 15 MCP tools with Buffett-grade analyst frames

3533. **[macOS-Notification-MCP](https://github.com/devizor/macOS-Notification-MCP)** - ⭐ 35
   macOS Notification MCP enables AI assistants to trigger native macOS sounds, visual notifications, and text-to-speech. Built for Claude and other AI models using the Model Context Protocol.

3534. **[awesome-mcp-servers](https://github.com/ever-works/awesome-mcp-servers)** - ⭐ 35
   A curated list of the best MCP Servers, featuring top solutions, libraries, tools, and more. - https://mcpserver.works

3535. **[mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client)** - ⭐ 35
   LangChain.js client for Model Context Protocol.

3536. **[mcp-rag-server](https://github.com/kwanLeeFrmVi/mcp-rag-server)** - ⭐ 35
   mcp-rag-server is a Model Context Protocol (MCP) server that enables Retrieval Augmented Generation (RAG) capabilities. It empowers Large Language Models (LLMs) to answer questions based on your document content by indexing and retrieving relevant information efficiently.

3537. **[mcp-video](https://github.com/KyaniteLabs/mcp-video)** - ⭐ 35
   Guardrailed video editing MCP server for AI agents. FFmpeg, Hyperframes, repurposing tools, Python client, and CLI. Local, fast, free.

3538. **[lets-learn-mcp-java](https://github.com/microsoft/lets-learn-mcp-java)** - ⭐ 35
   Learn how to build Java-based MCP Servers and Clients with LangChain4J and Quarkus

3539. **[WebSearch-MCP](https://github.com/mnhlt/WebSearch-MCP)** - ⭐ 35
   [Self-hosted] A Model Context Protocol (MCP) server implementation that provides a web search capability over stdio transport. This server integrates with a WebSearch Crawler API to retrieve search results.

3540. **[semrush-mcp](https://github.com/mrkooblu/semrush-mcp)** - ⭐ 35
   A Model Context Protocol (MCP) server implementation that provides tools for accessing Semrush API data.

3541. **[mcp.zig](https://github.com/muhammad-fiaz/mcp.zig)** - ⭐ 35
   A Model Context Protocol (MCP) library for the Zig ecosystem.

3542. **[ddg_search](https://github.com/OEvortex/ddg_search)** - ⭐ 35
   A powerful Model Context Protocol (MCP) server for web search and URL content extraction using DuckDuckGo.

3543. **[mcmodding-mcp](https://github.com/OGMatrix/mcmodding-mcp)** - ⭐ 35
   mcmodding-mcp is a Model Context Protocol (MCP) server that gives AI assistants like Claude direct access to Minecraft modding documentation. Instead of relying on potentially outdated training data, your AI assistant can search real documentation, find code examples, and explain concepts accurately.

3544. **[omop_mcp](https://github.com/OHNLP/omop_mcp)** - ⭐ 35
   Model Context Protocol (MCP) server for mapping clinical terminology to Observational Medical Outcomes Partnership (OMOP) concepts using Large Language Models

3545. **[context-harness](https://github.com/parallax-labs/context-harness)** - ⭐ 35
   Local-first context ingestion and retrieval for AI tools. SQLite + embeddings + MCP server for Cursor & Claude.

3546. **[plumcp](https://github.com/plumce/plumcp)** - ⭐ 35
   Clojure/ClojureScript library for making MCP server and client

3547. **[Blender-MCP-Server](https://github.com/poly-mcp/Blender-MCP-Server)** - ⭐ 35
   MCP server addon for Blender - Control Blender via AI agents through 51 powerful tools. Made to be used with PolyMCP for intelligent tool orchestration. Features thread-safe execution, auto-dependency installation, and complete 3D workflow automation.

3548. **[trading212-mcp-server](https://github.com/RohanAnandPandit/trading212-mcp-server)** - ⭐ 35
   The Trading212 MCP server is a Model Context Protocol server implementation that provides seamless data connectivity to the Trading212 trading platform enabling advanced interaction capabilities via the public beta API.

3549. **[minimal-godot-mcp](https://github.com/ryanmazzolini/minimal-godot-mcp)** - ⭐ 35
   Lightweight MCP server bridging Godot LSP to MCP clients for GDScript validation

3550. **[PRD-MCP-Server](https://github.com/Saml1211/PRD-MCP-Server)** - ⭐ 35
   Flagship Model Context Protocol server for generating Product Requirement Documents (PRDs) from codebase context.

3551. **[mcp](https://github.com/screenshotone/mcp)** - ⭐ 35
   A simple implementation of an MCP server for the ScreenshotOne API

3552. **[chat-nextjs-mcp-client](https://github.com/shricodev/chat-nextjs-mcp-client)** - ⭐ 35
   ⚡ Chat MCP Client for Remote hosted MCP Servers (with Composio) and locally hosted MCP servers. 📡

3553. **[mcp-prompt-server-go](https://github.com/smallnest/mcp-prompt-server-go)** - ⭐ 35
   一个提供优秀prompt的Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地和使用。提供tool和prompt两种形式

3554. **[deep-research](https://github.com/ssdeanx/deep-research)** - ⭐ 35
   The Deep Research Assistant is meticulously crafted on Mastra's modular, scalable architecture, designed for intelligent orchestration and seamless human-AI interaction. It's built to tackle complex research challenges autonomously.

3555. **[meta-prompt-mcp-server](https://github.com/tisu19021997/meta-prompt-mcp-server)** - ⭐ 35
   Turn any MCP Client into a "multi-agent" system (via prompting)

3556. **[rss-mcp](https://github.com/veithly/rss-mcp)** - ⭐ 35
   This is a Model Context Protocol (MCP) server built with TypeScript. It provides a versatile tool to fetch and parse any standard RSS/Atom feed, and also includes special support for RSSHub feeds.

3557. **[n8n-mcp](https://github.com/vredrick/n8n-mcp)** - ⭐ 35
   n8n MCP Server - Documentation and tools for n8n nodes via Model Context Protocol with SSE support

3558. **[mcp-scala](https://github.com/windymelt/mcp-scala)** - ⭐ 35
   Model Context Protocol server written in Scala

3559. **[godoc-mcp-server](https://github.com/yikakia/godoc-mcp-server)** - ⭐ 35
   A mcp server provide infomation from pkg.go.dev. For all golang programmers

3560. **[mcp-mail-server](https://github.com/yunfeizhu/mcp-mail-server)** - ⭐ 35
   A lightweight Model Context Protocol (MCP) server that provides IMAP and SMTP email functionality for AI assistants like Claude in Cursor IDE. Built with TypeScript and optimized for easy deployment via npm/npx.

3561. **[google-researcher-mcp](https://github.com/zoharbabin/google-researcher-mcp)** - ⭐ 35
   This is a Model Context Protocol (MCP) server that enables AI assistants like Claude, GPT, and other LLMs to:  Search the web via Google (general, images, news) Read any webpage including JavaScript-rendered sites Extract YouTube transcripts automatically Parse documents (PDF, DOCX, PPTX)

3562. **[kaggle-mcp](https://github.com/54yyyu/kaggle-mcp)** - ⭐ 34
   Kaggle-MCP: Connect Claude AI to the Kaggle API through the Model Context Protocol (MCP), enabling competition, dataset, and kernel operations through the AI interface.

3563. **[tiktok-ads-mcp-server](https://github.com/AdsMCP/tiktok-ads-mcp-server)** - ⭐ 34
   TikTok Ads MCP Server – Model Context Protocol Server for TikTok Ads Marketing API Integration

3564. **[mcp-server-fuzzer](https://github.com/Agent-Hellboy/mcp-server-fuzzer)** - ⭐ 34
   A generic mcp server fuzzer

3565. **[MCPSecBench](https://github.com/AIS2Lab/MCPSecBench)** - ⭐ 34
   MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols

3566. **[iotdb-mcp-server](https://github.com/apache/iotdb-mcp-server)** - ⭐ 34
   Apache IoTDB MCP Server

3567. **[adk-python-mcp-client](https://github.com/arjunprabhulal/adk-python-mcp-client)** - ⭐ 34
   Demo of ADK (Agent Development Kit) as an MCP (Model Context Protocol) client for flight search capabilities.

3568. **[coworker](https://github.com/Array-Ventures/coworker)** - ⭐ 34
   Open-source AI agent with MCP UI, app builder, A2A protocol, skills marketplace, and multi-provider chat. Built with Mastra. Alternative to OpenClaw.

3569. **[pushover-mcp](https://github.com/AshikNesin/pushover-mcp)** - ⭐ 34
   A MCP implementation for sending notifications via Pushover

3570. **[bear-notes-mcp](https://github.com/bejaminjones/bear-notes-mcp)** - ⭐ 34
   MCP server for Bear app - Full Read + Write AI-powered note management with Claude Desktop

3571. **[laravel-mcp-companion](https://github.com/brianirish/laravel-mcp-companion)** - ⭐ 34
   A Laravel developer's MCP companion. Get the absolute best advice, recommendations, and up-to-date documentation for the entire Laravel ecosystem.

3572. **[mcpls](https://github.com/bug-ops/mcpls)** - ⭐ 34
   Universal MCP to LSP bridge - expose Language Server Protocol capabilities as MCP tools for AI agents

3573. **[1mcp](https://github.com/buremba/1mcp)** - ⭐ 34
   Let your agent write code and execute code directly in the browser with WASM

3574. **[Agentic-MCP-Skill](https://github.com/cablate/Agentic-MCP-Skill)** - ⭐ 34
   Agentic-MCP, Progressive MCP client with three-layer lazy loading. Validates AgentSkills.io pattern for efficient token usage. Use MCP without pre-install & wasting full-loading

3575. **[prometheus_mcp_server](https://github.com/CaesarYangs/prometheus_mcp_server)** - ⭐ 34
   A Model Context Protocol (MCP) server enabling LLMs to query, analyze, and interact with Prometheus databases through predefined routes.

3576. **[codelogic-mcp-server](https://github.com/CodeLogicIncEngineering/codelogic-mcp-server)** - ⭐ 34
   An MCP Server to utilize Codelogic's rich software dependency data in your AI programming assistant.

3577. **[resonant](https://github.com/codependentai/resonant)** - ⭐ 34
   Open-source relational AI framework with identity persistence, memory, and MCP integration. Build relationship-aware AI agents that remember, grow, and maintain continuity. Built on Claude Agent SDK.

3578. **[awesome-mcp-lists](https://github.com/collabnix/awesome-mcp-lists)** - ⭐ 34
   A Curated List of MCP Servers, Clients and Toolkits

3579. **[fantasy-football-mcp-public](https://github.com/derekrbreese/fantasy-football-mcp-public)** - ⭐ 34
   Yahoo Fantasy Football MCP server for Claude Desktop - Advanced lineup optimization, draft assistance, and league management. Built using Claude Code.

3580. **[mcp-client-auth](https://github.com/dzhng/mcp-client-auth)** - ⭐ 34
   A TypeScript library providing OAuth2 authentication utilities for Model Context Protocol (MCP) clients. This library simplifies the process of adding OAuth authentication to MCP client implementations.

3581. **[garmin-connect-mcp](https://github.com/eddmann/garmin-connect-mcp)** - ⭐ 34
   MCP server enabling LLMs to interact with Garmin Connect - activities, health metrics, sleep data, and training analysis

3582. **[rlm-claude](https://github.com/EncrEor/rlm-claude)** - ⭐ 34
   Recursive Language Models for Claude Code - Infinite memory solution inspired by MIT CSAIL paper

3583. **[kanban-mcp](https://github.com/eyalzh/kanban-mcp)** - ⭐ 34
   MCP server providing kanban-based task management memory for complex multi-session workflows with AI agents

3584. **[FalkorDB-MCPServer](https://github.com/FalkorDB/FalkorDB-MCPServer)** - ⭐ 34
   FalkorDB-MCPServer is an MCP (Model Context Protocol) server that connects LLMs to FalkorDB

3585. **[gate-for-ai](https://github.com/gate/gate-for-ai)** - ⭐ 34
   Gate for AI is an AI-native crypto infrastructure that enables AI agents to trade, analyze markets, manage wallets, and query on-chain data through MCP (Model Context Protocol) and modular AI Skills. Integrate ChatGPT, Claude, and OpenClaw with CEX + DEX capabilities.

3586. **[diy-tools-mcp](https://github.com/hesreallyhim/diy-tools-mcp)** - ⭐ 34
   An MCP server that allows users to dynamically add custom tools/functions at runtime

3587. **[Unity-AI-ParticleSystem](https://github.com/IvanMurzak/Unity-AI-ParticleSystem)** - ⭐ 34
   AI-powered tools for Unity Particle System. Create and modify Particle System directly through natural language commands.

3588. **[any-script-mcp](https://github.com/izumin5210/any-script-mcp)** - ⭐ 34
   An MCP server that exposes arbitrary CLI tools and shell scripts as MCP Tools

3589. **[mattermost-mcp-host](https://github.com/jagan-shanmugam/mattermost-mcp-host)** - ⭐ 34
   A Mattermost integration that connects to Model Context Protocol (MCP) servers, leveraging a LangGraph-based Agent.

3590. **[chessagineweb](https://github.com/jalpp/chessagineweb)** - ⭐ 34
   The most underrated FOSS chess interface that combines AI agents and chess engines into one unified platform.

3591. **[capacities-mcp](https://github.com/jem-computer/capacities-mcp)** - ⭐ 34
   Capacities×MCP

3592. **[mcp-wireshark](https://github.com/khuynh22/mcp-wireshark)** - ⭐ 34
   An MCP server that integrates Wireshark/tshark with AI tools and IDEs. Capture live traffic, parse .pcap files, apply display filters, follow streams, and export JSON - all via Claude Desktop, VS Code, or CLI. Cross‑platform, typed, tested, and pip‑installable.

3593. **[mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing)** - ⭐ 34
   A minimal Model Context Protocol 🖥️ server/client🧑‍💻with OpenAI and 🌐 web browser control via Playwright.

3594. **[claude-code-mcp](https://github.com/KunihiroS/claude-code-mcp)** - ⭐ 34
   MCP Server connects with claude code local command.

3595. **[douyin-mcp-server](https://github.com/lancelin111/douyin-mcp-server)** - ⭐ 34
   🎥 Douyin (TikTok China) MCP Server - Automated video upload service via Model Context Protocol for AI integration

3596. **[mcp-probe-kit](https://github.com/mybolide/mcp-probe-kit)** - ⭐ 34
   一个强大的 MCP (Model Context Protocol) 服务器，提20个实用工具，覆盖代码质量、开发效率、项目管理、生成skills文档全流程。

3597. **[McpToolkit](https://github.com/nuskey8/McpToolkit)** - ⭐ 34
   Lightweight, fast, NativeAOT compatible MCP (Model Context Protocol) framework for .NET

3598. **[mcp-searxng-enhanced](https://github.com/OvertliDS/mcp-searxng-enhanced)** - ⭐ 34
   Enhanced MCP server for SearXNG: category-aware web-search, web-scraping, and date/time retrieval.

3599. **[PDBe-MCP-Servers](https://github.com/PDBeurope/PDBe-MCP-Servers)** - ⭐ 34
   PDBe MCP Servers integrate Protein Data Bank Europe resources with LLMs via Model Context Protocol. Provides seamless access to protein structure data through API tools and graph database schema assistance for intelligent Cypher query generation, bridging structural biology and AI research.

3600. **[mindbridge-mcp](https://github.com/pinkpixel-dev/mindbridge-mcp)** - ⭐ 34
   MindBridge is an AI orchestration MCP server that lets any app talk to any LLM — OpenAI, Anthropic, DeepSeek, Ollama, and more — through a single unified API. Route queries, compare models, get second opinions, and build smarter multi-LLM workflows.

3601. **[phonepi-mcp](https://github.com/priyankark/phonepi-mcp)** - ⭐ 34
   PhonePi MCP enables seamless integration between desktop AI tools and your smartphone, providing 23+ direct actions including SMS messaging, phone calls, contact management, snippet creation and search, clipboard sharing, notifications, battery status checks, and remote device controls.

3602. **[MCPServer](https://github.com/rhennigan/MCPServer)** - ⭐ 34
   Implements a model context protocol server using Wolfram Language

3603. **[wiki-js-mcp](https://github.com/talosdeus/wiki-js-mcp)** - ⭐ 34
   Model Context Protocol (MCP) server for Wiki.js with hierarchical documentation & Docker setup

3604. **[MCP-Server-Starter](https://github.com/TheSethRose/MCP-Server-Starter)** - ⭐ 34
   A Model Context Protocol server starter template

3605. **[autotask-mcp](https://github.com/wyre-technology/autotask-mcp)** - ⭐ 34
   MCP server for Kaseya Autotask PSA — 39 tools for companies, tickets, projects, time entries, and more

3606. **[mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal)** - ⭐ 34
   Model Context Protocol Server for Apache OpenDAL™

3607. **[DBJavaGenix](https://github.com/ZhaoXingPeng/DBJavaGenix)** - ⭐ 34
   智能数据库代码生成工具基于MCP架构，支持MySQL等多种数据库，自动生成Entity、DAO、Service及Controller等完整分层代码，大幅提升开发效率。依托MCP协议，具备强大扩展与集成能力，可智能推断表关系与业务语义。集成Mustache、MapStruct和Lombok，实现跨语言生成、高效映射和代码简化，并提供依赖自动管理，保障项目稳定。

3608. **[zilliz-mcp-server](https://github.com/zilliztech/zilliz-mcp-server)** - ⭐ 34
   A Model Context Protocol (MCP) server seamlessly connecting AI Agents and AI coding tools with Zilliz Cloud  https://zilliz.com/

3609. **[fastmcp-threatintel](https://github.com/4R9UN/fastmcp-threatintel)** - ⭐ 33
   AI-Powered Threat Intelligence MCP tool

3610. **[Unreal-MCP](https://github.com/aadeshrao123/Unreal-MCP)** - ⭐ 33
   AI bridge for Unreal Engine 5. Control the editor from Claude Code, Cursor, Windsurf, and any MCP client. 238 commands across materials, blueprints, Niagara VFX, StateTree, data tables, Mass Entity, Enhanced Input, UMG widgets, and performance profiling.

3611. **[silverbullet-mcp](https://github.com/Ahmad-A0/silverbullet-mcp)** - ⭐ 33
   A Model Context Protocol (MCP) server to interact with your SilverBullet notes and data.

3612. **[kaggle-mcp](https://github.com/arrismo/kaggle-mcp)** - ⭐ 33
   MCP server for Kaggle

3613. **[Zammad-MCP](https://github.com/basher83/Zammad-MCP)** - ⭐ 33
   A Model Context Protocol (MCP) server for Zammad integration, enabling AI assistants to interact with tickets, users, and organizations.

3614. **[Amazing-Marvin-MCP](https://github.com/bgheneti/Amazing-Marvin-MCP)** - ⭐ 33
   Model Context Provider for Amazing Marvin productivity app - Access your tasks, projects, and categories in AI assistants

3615. **[maven-mcp-server](https://github.com/Bigsy/maven-mcp-server)** - ⭐ 33
   An MCP (Model Context Protocol) server that provides tools for checking Maven dependency versions.

3616. **[bitrise-mcp](https://github.com/bitrise-io/bitrise-mcp)** - ⭐ 33
   MCP Server for the Bitrise API, enabling app management, build operations, artifact management and more.

3617. **[browserai-mcp](https://github.com/brightdata/browserai-mcp)** - ⭐ 33
   A powerful Model Context Protocol (MCP) server that provides an access to serverless browser for AI agents and apps

3618. **[devduck](https://github.com/cagataycali/devduck)** - ⭐ 33
   Minimalist AI agent that fixes itself when things break.

3619. **[enhanced-mcp-memory](https://github.com/cbunting99/enhanced-mcp-memory)** - ⭐ 33
   An enhanced MCP (Model Context Protocol) server for intelligent memory and task management, designed for AI assistants and development workflows. Features semantic search, automatic task extraction, knowledge graphs, and comprehensive project management.

3620. **[kratos-mcp](https://github.com/ceorkm/kratos-mcp)** - ⭐ 33
   🏛️ Memory System for AI Coding Tools - Never explain your codebase again. MCP server with perfect project isolation, 95.8% context accuracy, and the Four Pillars Framework.

3621. **[DMCPServer](https://github.com/Daniel09Fernandes/DMCPServer)** - ⭐ 33
   Dinos MCP Server, make your code, on MCP Action and execute by AI

3622. **[mcp-mesh](https://github.com/dhyansraj/mcp-mesh)** - ⭐ 33
   Enterprise-grade distributed AI agent framework | Develop → Deploy → Observe | K8s-native | Dynamic DI | Auto-failover | Multi-LLM | Python + Java + TypeScript

3623. **[mcp-server](https://github.com/DollhouseMCP/mcp-server)** - ⭐ 33
   A Free, Open Source MCP server for dynamic custom persona management with public a GitHub collection of personas, skills, templates, and other elements for AI models.

3624. **[binance-mcp-server](https://github.com/ethancod1ng/binance-mcp-server)** - ⭐ 33
   A Model Context Protocol (MCP) server for integrating AI assistants with Binance cryptocurrency exchange APIs, enabling automated trading, market data access, and account management.

3625. **[mcp-server-fanqie](https://github.com/fysh1010/mcp-server-fanqie)** - ⭐ 33
   番茄小说 MCP 服务器 - 为番茄小说提供 Model Context Protocol 服务

3626. **[mcpmcp-server](https://github.com/glenngillen/mcpmcp-server)** - ⭐ 33
   Discover, setup, and integrate MCP servers with your favorite clients. Unlock the full potential of AI in your daily workflow.

3627. **[sketchfab-mcp-server](https://github.com/gregkop/sketchfab-mcp-server)** - ⭐ 33
   This is an MCP (Model Context Protocol) Server for discovering and downloading 3D models

3628. **[claude-mcp-trello](https://github.com/hrs-asano/claude-mcp-trello)** - ⭐ 33
   A Model Context Protocol (MCP) server that provides tools for interacting with Trello boards.

3629. **[apifox-mcp](https://github.com/iwen-conf/apifox-mcp)** - ⭐ 33
   Apifox MCP 服务器 - 让 Claude 等 AI 助手通过自然语言管理你的 Apifox 项目，轻松创建、更新和审计 API 接口

3630. **[prediction-market-mcp](https://github.com/JamesANZ/prediction-market-mcp)** - ⭐ 33
   A simple MCP server that grabs prediction market data from polymarket, PredictIt, & Kalshi.

3631. **[holoviz-mcp](https://github.com/MarcSkovMadsen/holoviz-mcp)** - ⭐ 33
   ✨A MCP server that provides intelligent access to the HoloViz ecosystem for humans and AIs.

3632. **[mcp-veo2](https://github.com/mario-andreschak/mcp-veo2)** - ⭐ 33
   MCP for Video- or Image-Generation with Google VEO2

3633. **[mcp-server](https://github.com/membranehq/mcp-server)** - ⭐ 33
   MCP Server for Membrane

3634. **[mcp-launcher](https://github.com/moeru-ai/mcp-launcher)** - ⭐ 33
   🐳🧩 Easy to use MCP builder & launcher for all possible MCP servers, just like Ollama for models!

3635. **[UCAI](https://github.com/nirholas/UCAI)** - ⭐ 33
   Universal Contract AI Interface (UCAI) 🔗 ABI to MCP | The open standard for connecting AI agents to blockchain. MCP server generator for smart contracts. Claude + Uniswap, Aave, ERC20, NFTs, DeFi. Python CLI, Web3 integration, transaction simulation. Polygon, Arbitrum, Base, Ethereum EVM chains. Claude, GPT, LLM tooling, Solidity, OpenAI.

3636. **[pan-mcp-relay](https://github.com/PaloAltoNetworks/pan-mcp-relay)** - ⭐ 33
   Palo Alto Networks AI Runtime Security Model Context Protocol (MCP) Relay Server

3637. **[UniAI](https://github.com/PiscesGameDev/UniAI)** - ⭐ 33
   Unity AI 交互框架

3638. **[listmonk-mcp](https://github.com/rhnvrm/listmonk-mcp)** - ⭐ 33
   MCP (Model Context Protocol) server for Listmonk newsletter management

3639. **[YFinance-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop)** - ⭐ 33
   An MCP (Model Context Protocol) tool that provides stock market data and trading capabilities using the yfinance library, specifically adapted for Claude Desktop.

3640. **[aec-model-bridge](https://github.com/Sam-AEC/aec-model-bridge)** - ⭐ 33
   Independent Revit MCP ( Model Context Protocol integration for Revit software ).

3641. **[MCPCorpus](https://github.com/Snakinya/MCPCorpus)** - ⭐ 33
   MCPCorpus is a comprehensive dataset for analyzing the Model Context Protocol (MCP) ecosystem, containing ~14K MCP servers and 300 MCP clients with 20+ normalized metadata attributes.

3642. **[google-search-console-mcp](https://github.com/surendranb/google-search-console-mcp)** - ⭐ 33
   Google Search Console MCP Server for Claude, Cursor, Windsurf and other MCP Clients

3643. **[vision-one-mcp-server](https://github.com/trendmicro/vision-one-mcp-server)** - ⭐ 33
   The Trend Vision One Model Context Protocol (MCP) Server enables natural language interaction between your favourite AI tooling and the Trend Vision One web APIs.  This allows users to harness the power of Large Language Models (LLM) to interpret and respond to security events.

3644. **[total-agent-memory](https://github.com/vbcherepanov/total-agent-memory)** - ⭐ 33
   Persistent memory for Claude Code & Codex CLI. Auto-extracted knowledge graph, multi-representation embeddings, 3D WebGL visualization. LongMemEval R@5=97.45%. Self-hosted, Ollama-optional

3645. **[vibeshell](https://github.com/veithly/vibeshell)** - ⭐ 33
   The first SSH client built for AI agents. Let Claude Code, Codex, and other CLI agents manage your servers through MCP skills. Beautiful UI, native performance.

3646. **[asterisk-mcp-server](https://github.com/winfunc/asterisk-mcp-server)** - ⭐ 33
   Asterisk Model Context Protocol (MCP) server.

3647. **[tiktok-ads-mcp](https://github.com/ysntony/tiktok-ads-mcp)** - ⭐ 33
   A pure MCP (Model Context Protocol) server for TikTok Business API integration, designed for AI-first interactions.

3648. **[unplugin-devpilot](https://github.com/zcf0508/unplugin-devpilot)** - ⭐ 33
   A universal plugin framework for development tools that enables seamless browser-server communication and MCP (Model Context Protocol) integration with AI/LLM systems.

3649. **[mcp-slicer](https://github.com/zhaoyouj/mcp-slicer)** - ⭐ 33
   A Model Context Protocol server for 3D Slicer integration

3650. **[altinity-mcp](https://github.com/Altinity/altinity-mcp)** - ⭐ 32
   Model Context Protocol server to use ClickHouse®  databases in your AI agents

3651. **[congressMCP](https://github.com/amurshak/congressMCP)** - ⭐ 32
   An MCP server allowing AI agents and MCP clients to interface with the Congress.gov API

3652. **[apisql-mcp](https://github.com/apisql-dev/apisql-mcp)** - ⭐ 32
   一个 MCP Server 连接你的所有数据库，数据库 MCP Server 的瑞士军刀。One MCP Server for all your databases. The Swiss Army Knife of Database MCP Servers.

3653. **[mcp-appium-gestures](https://github.com/AppiumTestDistribution/mcp-appium-gestures)** - ⭐ 32
   This is a Model Context Protocol (MCP) server providing resources and tools for Appium mobile gestures using Actions API..

3654. **[actor-critic-thinking-mcp](https://github.com/aquarius-wing/actor-critic-thinking-mcp)** - ⭐ 32
   A dual-perspective thinking analysis server based on Model Context Protocol (MCP), providing comprehensive performance evaluation through Actor-Critic methodology.

3655. **[atxp](https://github.com/atxp-dev/atxp)** - ⭐ 32
   Give your AI agent a wallet, email, phone number, and instant access to paid MCP tools — web search, image/video/music gen, X search, SMS, voice calls, code execution, and more. Works with Gemini CLI, Claude, and any MCP client.

3656. **[ILSpy-Mcp](https://github.com/bivex/ILSpy-Mcp)** - ⭐ 32
   🔓 UNLEASH ILSpy'S POWER. Reverse-engineer DOTNET code at GOD SPEED. AI-assisted debugging that THINKS with you. Decompile ANYTHING. 🚀

3657. **[Cortex](https://github.com/cdeust/Cortex)** - ⭐ 32
   Persistent memory for Claude Code — 41 neuroscience papers, 26 biological mechanisms with paper-bearing per-mechanism ablation evidence (E1 v3). LongMemEval R@10 98.4% / MRR 0.9124 (n=500). LoCoMo R@10 94.2% / MRR 0.8278 (n=1986). BEAM-10M +33.4% over flat retrieval. PostgreSQL + pgvector. Verified via 31-row two-benchmark ablation campaign.

3658. **[clay-mcp](https://github.com/clay-inc/clay-mcp)** - ⭐ 32
   A simple Model Context Protocol (MCP) server for Clay.

3659. **[workflows-mcp-server](https://github.com/cyanheads/workflows-mcp-server)** - ⭐ 32
   Model Context Protocol server that enables AI agents to discover, create, and execute complex, multi-step workflows defined in simple YAML files. Allow your AI agents to better organize their tool usage and provide a more structured way to handle complex multi-step tasks.

3660. **[dassian-adt](https://github.com/DassianInc/dassian-adt)** - ⭐ 32
   MCP server for SAP ABAP development via ADT API. Connect AI assistants to SAP: read, write, test, and deploy ABAP code without SAP GUI.

3661. **[mcp-ollama](https://github.com/emgeee/mcp-ollama)** - ⭐ 32
   Query model running with Ollama from within Claude Desktop or other MCP clients

3662. **[engram-memory](https://github.com/EngramMemory/engram-memory)** - ⭐ 32
   The highest-scoring AI memory system ever benchmarked that isn't reliant on LLM reranking. And it's free & burns less tokens.

3663. **[Direwolf](https://github.com/Framebuffers/Direwolf)** - ⭐ 32
   Distributed Data Processing Pipeline for MCP.

3664. **[rod-mcp](https://github.com/go-rod/rod-mcp)** - ⭐ 32
   Model Context Protocol Server of Rod

3665. **[mcp-server](https://github.com/HuaweiCloudDeveloper/mcp-server)** - ⭐ 32
   Provide different cloud products  MCP Server tools to  help developers  manage cloud resources  with AI-agent

3666. **[mcp-server-zotero-dev](https://github.com/introfini/mcp-server-zotero-dev)** - ⭐ 32
   Give your AI assistant superpowers for Zotero plugin development. 25 tools for screenshots, DOM inspection, JavaScript execution, build integration, and debugging via Model Context Protocol.

3667. **[codingbuddy](https://github.com/JeremyDev87/codingbuddy)** - ⭐ 32
   Codingbuddy orchestrates 29 specialized AI agents to deliver code quality comparable to a team of human experts through a PLAN → ACT → EVAL workflow.

3668. **[pdf-mcp](https://github.com/jztan/pdf-mcp)** - ⭐ 32
   MCP server that lets Claude Code and other AI agents read large PDFs without hitting context limits. Chunked reading, hybrid search, OCR, table and image extraction, SQLite cache.

3669. **[Smart-Thinking](https://github.com/Leghis/Smart-Thinking)** - ⭐ 32
   Smart-Thinking is a Model Context Protocol (MCP) server that delivers graph-based, multi-step reasoning without relying on external AI APIs. Everything happens locally: similarity search, heuristic-based scoring, verification tracking, memory, and visualization all run in a deterministic pipeline designed for transparency and reproducibility.

3670. **[myBrAIn](https://github.com/lilium360/myBrAIn)** - ⭐ 32
   myBrAIn is an MCP (Model Context Protocol) server designed to provide persistent and contextual memory to language models (like Google Antigravity). It acts as a "second brain" for your development environment, allowing the AI to remember project rules, architectural decisions, and technical insights across different chat sessions

3671. **[biothings-mcp](https://github.com/longevity-genie/biothings-mcp)** - ⭐ 32
   MCP (Model Context Protocol) server for biothings

3672. **[notion-cli](https://github.com/lox/notion-cli)** - ⭐ 32
   CLI for Notion using the Model Context Protocol (MCP)

3673. **[d365fo-client](https://github.com/mafzaal/d365fo-client)** - ⭐ 32
   A comprehensive Python client library and MCP server for Microsoft Dynamics 365 Finance & Operations (D365 F&O) that provides easy access to OData endpoints, metadata operations, label management, and AI assistant integration.

3674. **[mcp-server-giphy](https://github.com/magarcia/mcp-server-giphy)** - ⭐ 32
   An implementation of Giphy integration with Model Context Protocol

3675. **[mcp-google-calendar](https://github.com/markelaugust74/mcp-google-calendar)** - ⭐ 32
   A Model Context Protocol (MCP) server implementation for Google Calendar integration. Create and manage calendar events directly through Claude or other AI assistants.

3676. **[clay-mcp](https://github.com/mesh/clay-mcp)** - ⭐ 32
   A simple Model Context Protocol (MCP) server for Clay.

3677. **[qdrant-mcp-server](https://github.com/mhalder/qdrant-mcp-server)** - ⭐ 32
   MCP server for semantic search using local Qdrant vector database and OpenAI embeddings

3678. **[dev-kit](https://github.com/nguyenvanduocit/dev-kit)** - ⭐ 32
   [Model Context Protocol] Dev Kit - anything a developer need for him day to day works

3679. **[seatunnel-mcp](https://github.com/ocean-zhc/seatunnel-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server for Apache Seatunnel.  This provides access to your Apache Seatunnel RESTful API V2 instance and the surrounding ecosystem.

3680. **[mcpc](https://github.com/OlaHulleberg/mcpc)** - ⭐ 32
   An extension to MCP (Model-Context-Protocol) that enables two-way asynchronous communication between LLMs and tools through the already existing MCP transport - no additional transport layer needed.

3681. **[mcp-hacker-news](https://github.com/paabloLC/mcp-hacker-news)** - ⭐ 32
   This MCP server acts as a bridge between the official Hacker News API and AI-powered tools that support the Model Context Protocol, such as Claude and Cursor.

3682. **[mcp-bash](https://github.com/patrickomatik/mcp-bash)** - ⭐ 32
   A simple model context protocol (MCP) server that allows Claude Desktop or other MCP aware clients to run Bash commands on your local machine.

3683. **[emcp](https://github.com/PJUllrich/emcp)** - ⭐ 32
   A Model Context Protocol (MCP) Server for Elixir

3684. **[ptt_mcp_server](https://github.com/PyPtt/ptt_mcp_server)** - ⭐ 32
   The best PTT MCP server

3685. **[agent-twitter-client-mcp](https://github.com/ryanmac/agent-twitter-client-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server that integrates with X using the @elizaOS `agent-twitter-client` package, allowing AI models to interact with Twitter without direct API access.

3686. **[postman-mcp](https://github.com/SalehKhatri/postman-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server that provides seamless integration with the Postman API. This package enables AI assistants and applications to interact with Postman workspaces, collections, requests, environments, and folders programmatically.

3687. **[laravel-mcp-client](https://github.com/scriptoshi/laravel-mcp-client)** - ⭐ 32

3688. **[mcp-server-weibo](https://github.com/Selenium39/mcp-server-weibo)** - ⭐ 32
   Model Context Protocol服务器，用于抓取微博用户信息、动态和搜索功能

3689. **[imagegen-mcp](https://github.com/spartanz51/imagegen-mcp)** - ⭐ 32
   MCP server for OpenAI Image Generation & Editing — text-to-image, image-to-image (with mask), no extra plugins.

3690. **[mcp-java-sdk-examples](https://github.com/thought2code/mcp-java-sdk-examples)** - ⭐ 32
   A collection of MCP server examples developed by various Java SDKs

3691. **[src-to-kb](https://github.com/vezlo/src-to-kb)** - ⭐ 32
   Convert source code to LLM ready knowledge base

3692. **[mmx-mcp-server](https://github.com/zth0828/mmx-mcp-server)** - ⭐ 32
   A unified Model Context Protocol server for MiniMax CLI (mmx)

3693. **[mcp-marketplace](https://github.com/aiagenta2z/mcp-marketplace)** - ⭐ 31
   OpenSource MCP Marketplace | MCP Servers Tools Meta Dataset | Web API | Web Client Integration

3694. **[mcp-server-starter-ts](https://github.com/alexanderop/mcp-server-starter-ts)** - ⭐ 31
   A minimal TypeScript starter template for building Model Context Protocol (MCP) servers.

3695. **[azure-container-apps-ai-mcp](https://github.com/Azure-Samples/azure-container-apps-ai-mcp)** - ⭐ 31
   This project showcases how to use the MCP protocol with Azure OpenAI. It provides a simple example to interact with OpenAI's API seamlessly via an MCP server and client.

3696. **[MCP-OpenStack-Ops](https://github.com/call518/MCP-OpenStack-Ops)** - ⭐ 31
   90+ production-safe OpenStack tools for AI agents via MCP. Project-scoped & read-only by default. Works with Claude, Open WebUI & any MCP client. FastMCP + OpenStack SDK. Available on PyPI, Docker Hub & Smithery.

3697. **[mentor-mcp-server](https://github.com/cyanheads/mentor-mcp-server)** - ⭐ 31
   A Model Context Protocol server providing LLM Agents a second opinion via AI-powered Deepseek-Reasoning R1 mentorship capabilities, including code review, design critique, writing feedback, and idea brainstorming through the Deepseek API.

3698. **[bw-modeling-mcp](https://github.com/dnic-dev/bw-modeling-mcp)** - ⭐ 31
   MCP server for agentic AI-assisted development in SAP BW/4HANA

3699. **[cca-mcp-configurator](https://github.com/doggy8088/cca-mcp-configurator)** - ⭐ 31
   一個簡單易用的網頁工具，用於管理 GitHub Copilot Coding Agent 的 MCP (Model Context Protocol) 設定

3700. **[ontomics](https://github.com/EtienneChollet/ontomics)** - ⭐ 31
   Extract domain knowledge from codebases to reduce LLM token consumption by 20x and time in agentic search by 10x — gathers and makes concepts, naming conventions, and vocabulary queryable via MCP.

3701. **[clap-mcp](https://github.com/gakonst/clap-mcp)** - ⭐ 31
   A Rust framework that bridges clap command-line applications with the Model Context Protocol (MCP)

3702. **[turn-based-game-mcp](https://github.com/github-samples/turn-based-game-mcp)** - ⭐ 31
   A turn-based games app built with Next.js and TypeScript that features Tic-Tac-Toe and Rock Paper Scissors games with AI opponents powered by the Model Context Protocol (MCP), offering three difficulty levels.

3703. **[ez-mcp](https://github.com/intellectronica/ez-mcp)** - ⭐ 31
   The easiest path to getting an MCP server going

3704. **[mcp-klever-vm](https://github.com/klever-io/mcp-klever-vm)** - ⭐ 31
   MCP server for Klever blockchain smart contract development

3705. **[mcp-dashboards](https://github.com/KyuRish/mcp-dashboards)** - ⭐ 31
   Turn your data into interactive dashboards inside any AI client - MCP Apps powered

3706. **[powerplatform-mcp](https://github.com/michsob/powerplatform-mcp)** - ⭐ 31
   PowerPlatform Model Context Protocol server

3707. **[NiFiMCP](https://github.com/ms82119/NiFiMCP)** - ⭐ 31
   An MCP Server and client for communicating with Nifi (v1.28)

3708. **[zerodha-mcp](https://github.com/mtwn105/zerodha-mcp)** - ⭐ 31
   Zerodha MCP Server & Client - AI Agent (w/Agno & w/Google ADK)

3709. **[ESP32MCPServer](https://github.com/navado/ESP32MCPServer)** - ⭐ 31
   Allow AI models connect to ESP32 exposed interfaces. AI generated MCP server for ESP32.

3710. **[simple-psql-mcp](https://github.com/NetanelBollag/simple-psql-mcp)** - ⭐ 31
   A beginner-friendly MCP server template featuring a PostgreSQL connector with clean, easy-to-understand code. Perfect for developers new to Model Context Protocol who want to experiment and create their own AI tool connectors with minimal setup.

3711. **[jlcpcb-parts-mcp](https://github.com/nvsofts/jlcpcb-parts-mcp)** - ⭐ 31
   JLCPCB PCBA向けの、部品探しを補助するためのMCPサーバー

3712. **[unity-editor-mcp](https://github.com/ozankasikci/unity-editor-mcp)** - ⭐ 31
   An MCP server and client for LLMs to interact with Unity Projects

3713. **[pubnub-mcp-server](https://github.com/pubnub/pubnub-mcp-server)** - ⭐ 31
   PubNub MCP Model Context Protocol Server for use in Cursor, Windsurf, Claude Desktop, Claude Code and OpenAI Codex and more!

3714. **[mdk-mcp-server](https://github.com/SAP/mdk-mcp-server)** - ⭐ 31
   Model Context Protocol (MCP) server for AI-assisted development ("vibe coding") of MDK applications.

3715. **[mcp-youtube-transcript](https://github.com/sinco-lab/mcp-youtube-transcript)** - ⭐ 31
   TypeScript MCP server for retrieving YouTube transcripts in Claude Desktop, Cursor, Cline, Codex, and other MCP clients

3716. **[unplugin-mcp](https://github.com/situ2001/unplugin-mcp)** - ⭐ 31
   A unified plugin for developers integrating MCP servers into modern JavaScript build tools, including Webpack, Rollup, Vite, and more.

3717. **[EU_AI_ACT_MCP](https://github.com/SonnyLabs/EU_AI_ACT_MCP)** - ⭐ 31
   EU AI Act MCP (Model Context Protocol) that connects to your AI agents, helping you to comply with the EU AI Act.

3718. **[mcp-proxy](https://github.com/stephenlacy/mcp-proxy)** - ⭐ 31
   Fast rust MCP proxy between stdio and SSE

3719. **[mcp-weather](https://github.com/TimLukaHorstmann/mcp-weather)** - ⭐ 31
   A Model Context Protocol (MCP) server that provides hourly and daily weather forecasts using the AccuWeather API.

3720. **[stata-workbench](https://github.com/tmonk/stata-workbench)** - ⭐ 31
   A VS Code compatible extension (Cursor, Windsurf, Antigravity etc.) that allows Stata code to be run directly from the editor. Enables AI agents to directly interact with Stata. Powered by mcp-stata, https://github.com/tmonk/mcp-stata.

3721. **[NetContextServer](https://github.com/willibrandon/NetContextServer)** - ⭐ 31
   A .NET implementation of the Model Context Protocol enabling AI assistants to explore and understand .NET codebases.

3722. **[localwp-agent-tools](https://github.com/10up/localwp-agent-tools)** - ⭐ 30
   A Local add-on that provides an MCP server, skills, and project context for AI-powered WordPress development. Works with Claude Code, Cursor, Windsurf, VS Code Copilot, and any MCP client.

3723. **[airflow-mcp-server](https://github.com/abhishekbhakat/airflow-mcp-server)** - ⭐ 30
   MCP Server for Apache Airflow

3724. **[postgres-mcp-server](https://github.com/ahmedmustahid/postgres-mcp-server)** - ⭐ 30
   MCP (Model Context Protocol) Server for postgres Database

3725. **[dockashell](https://github.com/anzax/dockashell)** - ⭐ 30
   DockaShell is an MCP server that gives AI agents isolated Docker containers to work in. MCP tools for shell access, file operations, and full audit trail.

3726. **[mcp-loxone](https://github.com/avrabe/mcp-loxone)** - ⭐ 30
   An opinionated Model Context Protocol (MCP) server for controlling Loxone home automation systems.

3727. **[kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp)** - ⭐ 30
   A comprehensive Message Control Protocol (MCP) server for Kafka Schema Registry.

3728. **[ai-foundry-agents-samples](https://github.com/Azure-Samples/ai-foundry-agents-samples)** - ⭐ 30
   Azure AI Foundry - Agents related sample code

3729. **[runjs](https://github.com/CharlieDigital/runjs)** - ⭐ 30
   The only MCP server you need: let your LLM generate and safely execute JavaScript -- including fetch API calls, JSONPath ETL, built-in resiliencey, and secrets management

3730. **[mcp-etherscan-server](https://github.com/crazyrabbitLTC/mcp-etherscan-server)** - ⭐ 30
   An MCP (Model Context Protocol) server that provides Ethereum blockchain data tools via Etherscan's API. Features include checking ETH balances, viewing transaction history, tracking ERC20 transfers, fetching contract ABIs, monitoring gas prices, and resolving ENS names.

3731. **[mcp-cyclops](https://github.com/cyclops-ui/mcp-cyclops)** - ⭐ 30
   Model Context Protocol server for Cyclops

3732. **[mcp-server](https://github.com/Decodo/mcp-server)** - ⭐ 30
   The Decodo MCP server which enables MCP clients to interface with services.

3733. **[mcp-server-dumplingai](https://github.com/DumplingAI/mcp-server-dumplingai)** - ⭐ 30
   MCP (Model Context Protocol) server for Dumpling AI

3734. **[mcp-client](https://github.com/edanyal/mcp-client)** - ⭐ 30
   Typescript mcp client library.

3735. **[mcp-log-proxy](https://github.com/emicklei/mcp-log-proxy)** - ⭐ 30
   a web logging proxy for MCP client-server communication

3736. **[google-workspace-mcp-server](https://github.com/epaproditus/google-workspace-mcp-server)** - ⭐ 30
   A Model Context Protocol server for Google Workspace integration (Gmail and Calendar)

3737. **[turbovault](https://github.com/Epistates/turbovault)** - ⭐ 30
   MCP server that transforms your Obsidian vault into an intelligent knowledge system

3738. **[stitch-mcp-auto](https://github.com/GreenSheep01201/stitch-mcp-auto)** - ⭐ 30
   Automated installer for Stitch MCP - The easiest way to set up your Universal MCP server for Google Stitch.

3739. **[itential-mcp](https://github.com/itential/itential-mcp)** - ⭐ 30
   🔌 Itential Platform MCP Server

3740. **[mcp_espn_ff](https://github.com/KBThree13/mcp_espn_ff)** - ⭐ 30
   ESPN Fantasy API with LLMs!

3741. **[mcp-gateway](https://github.com/lucky-aeon/mcp-gateway)** - ⭐ 30
   The MCP gateway is a reverse proxy server that forwards requests from clients to the MCP server or uses all MCP servers under the gateway through a unified portal.

3742. **[MalwareBazaar_MCP](https://github.com/mytechnotalent/MalwareBazaar_MCP)** - ⭐ 30
   An AI-driven MCP server that autonomously interfaces with Malware Bazaar, delivering real-time threat intel and sample metadata for authorized cybersecurity research workflows.

3743. **[local_faiss_mcp](https://github.com/nonatofabio/local_faiss_mcp)** - ⭐ 30
   Local FAISS vector store as an MCP server – Agent Memory, drop-in local semantic search for Claude / Copilot / Agents.

3744. **[chrome-extension-bridge-mcp](https://github.com/Oanakiaja/chrome-extension-bridge-mcp)** - ⭐ 30
   A chrome extension bridge that allows you to connect to a mcp server to use global window object.

3745. **[deno-mcp-template](https://github.com/phughesmcr/deno-mcp-template)** - ⭐ 30
   A template repo for writing and publishing local, remote, DXT, and binary MCP servers using Deno.

3746. **[reporecall](https://github.com/proofofwork-agency/reporecall)** - ⭐ 30
   Local codebase memory, auto-generated wiki, and interactive architecture dashboard for Claude Code and MCP. AST indexing, call graphs, hybrid search, topology analysis. 0 tool calls, 3-8x fewer tokens, everything stays on your machine.

3747. **[google-search-console-mcp-server](https://github.com/Shin-sibainu/google-search-console-mcp-server)** - ⭐ 30
   Model Context Protocol server for Google Search Console API - integrate with Claude Code and Claude Desktop

3748. **[machinepal](https://github.com/skalenetwork/machinepal)** - ⭐ 30
   The Cloud-Native MCP and X402 Gateway to Run and Monetize your AI Agents and Services, as well as optimize your AI costs

3749. **[carrot-ai-pm](https://github.com/talvinder/carrot-ai-pm)** - ⭐ 30
   Carrot auto-writes specs and catches AI code drift. MCP server for Cursor that AST-validates every commit.

3750. **[AI-Tracker](https://github.com/twwch/AI-Tracker)** - ⭐ 30
   本仓库旨在整理关于大语言模型（LLM）底层逻辑、**上下文工程 (Context Engineering)** 以及 **Model Context Protocol (MCP)** 协议的核心学习资源与实战路径。

3751. **[mcp](https://github.com/yandex-cloud/mcp)** - ⭐ 30
   Yandex Cloud MCP Servers

3752. **[ros-mcp](https://github.com/Yutarop/ros-mcp)** - ⭐ 30
   MCP server for ROS to control robots via topics, services, and actions.

3753. **[zebbern-kali-mcp](https://github.com/zebbern/zebbern-kali-mcp)** - ⭐ 30
   MCP server for Kali Linux penetration testing - 130 tools for AI-assisted security testing - Giving Agents access to full pentesting tools

3754. **[batchdata-mcp-real-estate](https://github.com/zellerhaus/batchdata-mcp-real-estate)** - ⭐ 30
   Model Context Protocol (MCP) server for BatchData.io property and address APIs - Real estate data integration for Claude and other AI assistants

3755. **[server-sharepoint](https://github.com/Zerg00s/server-sharepoint)** - ⭐ 30
   This is a MCP server for Claude Desktop that allows you to interact with SharePoint Online using the SharePoint REST API. It is designed to be used with the [Claude Desktop](https://claude.ai/download) app, but could be used by other MCP clients as well.

3756. **[mcp-notify](https://github.com/aahl/mcp-notify)** - ⭐ 29
   💬  MCP Server for notify to Weixin, Telegram, Bark, Lark, 飞书, 钉钉

3757. **[MCP-Scorecard](https://github.com/aak204/MCP-Scorecard)** - ⭐ 29
   Deterministic CI scanner and surface-risk scoring for MCP (Model Context Protocol) servers.

3758. **[alibabacloud-dms-mcp-server](https://github.com/aliyun/alibabacloud-dms-mcp-server)** - ⭐ 29
   A universal multi-cloud data MCP Server supporting over 40 types of data source connections, providing secure, unified data access in a single platform. Supports full range of Alibaba Cloud services and Mainstream databases/data warehouses.

3759. **[excel-reader-mcp](https://github.com/ArchimedesCrypto/excel-reader-mcp)** - ⭐ 29
   A Model Context Protocol (MCP) server for reading Excel files with automatic chunking and pagination support. Built with SheetJS and TypeScript.

3760. **[mcp-ollama-agent](https://github.com/ausboss/mcp-ollama-agent)** - ⭐ 29
   A TypeScript example showcasing the integration of Ollama with the Model Context Protocol (MCP) servers. This project provides an interactive command-line interface for an AI agent that can utilize the tools from multiple MCP Servers..

3761. **[openai-mcp-agent-dotnet](https://github.com/Azure-Samples/openai-mcp-agent-dotnet)** - ⭐ 29
   Sample to create an AI Agent using OpenAI models with any MCP server running on Azure Container Apps

3762. **[notion-mcp](https://github.com/Badhansen/notion-mcp)** - ⭐ 29
   A simple Model Context Protocol (MCP) server that integrates with Notion's API to manage my personal todo list.

3763. **[nchan-mcp-transport](https://github.com/ConechoAI/nchan-mcp-transport)** - ⭐ 29
   The best way to deploy mcp server. A high-performance WebSocket/SSE transport layer & gateway for Anthropic's MCP (Model Context Protocol) — powered by Nginx, Nchan, and FastAPI.

3764. **[luke-desktop](https://github.com/DrJonBrock/luke-desktop)** - ⭐ 29
   A modern desktop client for Claude AI with MCP server support, built with Tauri, React, and TypeScript.

3765. **[php-mcp](https://github.com/dtyq/php-mcp)** - ⭐ 29
   A complete PHP implementation of the Model Context Protocol (MCP) with server and client support, STDIO and HTTP transports, and framework integration

3766. **[izan.io](https://github.com/ekingunoncu/izan.io)** - ⭐ 29
   Turn Any Browser Action & Data Extraction into an AI Tool in 60 Seconds

3767. **[engram-memory-community](https://github.com/EngramMemory/engram-memory-community)** - ⭐ 29
   The highest-scoring AI memory system ever benchmarked that isn't reliant on LLM reranking. And it's free & burns less tokens.

3768. **[FerrumMCP](https://github.com/Eth3rnit3/FerrumMCP)** - ⭐ 29
   A Model Context Protocol (MCP) server that provides web automation capabilities through Ferrum, with optional BotBrowser integration for advanced anti-detection features. This enables AI agents to interact with web pages seamlessly.

3769. **[agent-pm](https://github.com/gannonh/agent-pm)** - ⭐ 29
   MCP server for the planning and execution of AI-assisted development projects.

3770. **[TAM-MCP-Server](https://github.com/gvaibhav/TAM-MCP-Server)** - ⭐ 29
   A comprehensive Model Context Protocol (MCP) server for market sizing analysis, TAM/SAM calculations, and industry research. Built with TypeScript, Express.js, and following the MCP  specification.

3771. **[langchain-mcp-tools-py](https://github.com/hideya/langchain-mcp-tools-py)** - ⭐ 29
   MCP to LangChain Tools Conversion Utility / Python

3772. **[pptx-xlsx-mcp](https://github.com/jenstangen1/pptx-xlsx-mcp)** - ⭐ 29
   Antrophics Model context protocol to edit powerpoint files

3773. **[raybridge](https://github.com/jlokos/raybridge)** - ⭐ 29
   MCP server that bridges Raycast extensions to any MCP-compatible client

3774. **[local-skills-mcp](https://github.com/kdpa-llc/local-skills-mcp)** - ⭐ 29
   Universal MCP server enabling any LLM or AI agent to utilize expert skills from your local filesystem. Reduces context consumption through lazy loading. Works with Claude, Cline, and any MCP-compatible client.

3775. **[telegram-mcp-server](https://github.com/kfastov/telegram-mcp-server)** - ⭐ 29
   MCP server implementation for Telegram

3776. **[tgcli](https://github.com/kfastov/tgcli)** - ⭐ 29
   Telegram user console client and archiver

3777. **[mcp-testing-framework](https://github.com/L-Qun/mcp-testing-framework)** - ⭐ 29
   Testing framework for Model Context Protocol (MCP)

3778. **[leanmcp-sdk](https://github.com/Leanmcp/leanmcp-sdk)** - ⭐ 29
   Production-ready TypeScript SDK for MCP servers: auth, multi-tenant, observability. Build enterprise AI agents fast.

3779. **[drawio-mcp-extension](https://github.com/lgazo/drawio-mcp-extension)** - ⭐ 29
   Draw.io Model Context Protocol (MCP) Browser Extension

3780. **[mcp-badges](https://github.com/mcpx-dev/mcp-badges)** - ⭐ 29
   Get your projects MCP (Model Context Protocol)  badges

3781. **[seo-insights-mcp-server](https://github.com/mrgoonie/seo-insights-mcp-server)** - ⭐ 29
   TypeScript Model Context Protocol (MCP) server for SEO Insights. Provides SEO tools for backlinks, keyword research, and traffic analysis. Includes CLI support and extensible structure for connecting AI systems (LLMs) to SEO APIs

3782. **[demo-mcp-server-client-implementation](https://github.com/mschwarzmueller/demo-mcp-server-client-implementation)** - ⭐ 29
   A demo implementation of a MCP server (consuming a dummy API) and basic client.

3783. **[nimbletools-core](https://github.com/NimbleBrainInc/nimbletools-core)** - ⭐ 29
   NimbleTools is an open-source MCP runtime. Infrastructure for the agentic web.

3784. **[rails-pg-extras-mcp](https://github.com/pawurb/rails-pg-extras-mcp)** - ⭐ 29
   MCP (Model Context Protocol) LLM interface for rails-pg-extras gem

3785. **[taskflow-mcp](https://github.com/pinkpixel-dev/taskflow-mcp)** - ⭐ 29
   A task management Model Context Protocol (MCP) server that helps AI assistants break down user requests into manageable tasks with subtasks, dependencies, and notes. Enforces a structured workflow with user approval steps.

3786. **[robinhood-mcp-server](https://github.com/rohitsingh-iitd/robinhood-mcp-server)** - ⭐ 29
   The Robinhood MCP Server provides a comprehensive interface to the Robinhood Crypto API. This server handles authentication, account management, market data retrieval, and trading operations through both REST API and WebSocket interfaces.

3787. **[mcp_autogen_sse_stdio](https://github.com/SaM-92/mcp_autogen_sse_stdio)** - ⭐ 29
   This repository demonstrates how to use AutoGen to integrate local and remote MCP (Model Context Protocol) servers. It showcases a local math tool (math_server.py) using Stdio and a remote Apify tool (RAG Web Browser Actor) via SSE for tasks like arithmetic and web browsing.

3788. **[zotero-mcp-server](https://github.com/swairshah/zotero-mcp-server)** - ⭐ 29
   MCP server to expose local zotero repository to MCP clients

3789. **[rdkit-mcp-server](https://github.com/tandemai-inc/rdkit-mcp-server)** - ⭐ 29
   MCP server that enables language models to interact with RDKit through natural language

3790. **[mcp-inception](https://github.com/tanevanwifferen/mcp-inception)** - ⭐ 29
   Call another MCP client from your MCP client. Offload context windows, delegate tasks, split between models

3791. **[mcp-websocket](https://github.com/virajsharma2000/mcp-websocket)** - ⭐ 29
   This server implements an MCP (Model Context Protocol) server with WebSocket enhancements for real-time data updates.

3792. **[rootcause](https://github.com/yindia/rootcause)** - ⭐ 29
   RootCause is a local-first MCP server that turns natural-language requests into evidence-backed incident analysis, Kubernetes diagnostics, and safer operations.

3793. **[openapi-mcp-generator](https://github.com/abutbul/openapi-mcp-generator)** - ⭐ 28
   A Python tool that automatically converts OpenAPI(Swagger, ETAPI) compatible specifications into fully functional Model Context Protocol (MCP) servers. Generates Docker-ready implementations with support for SSE/IO communication protocols, authentication, and comprehensive error handling. https://pypi.org/project/openapi-mcp-generator/

3794. **[mcp-simple-timeserver](https://github.com/andybrandt/mcp-simple-timeserver)** - ⭐ 28
   Simple MCP to give Claude ability to check current time as well as know when holidays are, what is the time distance between dates etc.

3795. **[capture-mcp-server](https://github.com/blencorp/capture-mcp-server)** - ⭐ 28
   AI-native Model Context Protocol (MCP) server that integrates SAM.gov, USASpending.gov, and Tango APIs to capture and analyze federal procurement and spending data through natural language queries. Responses include both human-readable text and structured JSON so MCP-compatible clients can consume the data programmatically.

3796. **[Palmos](https://github.com/ClayPulse/Palmos)** - ⭐ 28
   The Runtime Where AI Agents Build, Ship, and Evolve. Pulse Editor is a modular, cross-platform, AI-powered productivity platform with federated app collaboration and extensible workflows.

3797. **[pulse-editor](https://github.com/ClayPulse/pulse-editor)** - ⭐ 28
   The Runtime Where AI Agents Build, Ship, and Evolve. Pulse Editor is a modular, cross-platform, AI-powered productivity platform with federated app collaboration and extensible workflows.

3798. **[do-remote-mcp-server-template](https://github.com/do-community/do-remote-mcp-server-template)** - ⭐ 28
   A Model Context Protocol (MCP) server that checks domain name availability using WHOIS lookups and DNS resolution

3799. **[aistudio-mcp-server](https://github.com/eternnoir/aistudio-mcp-server)** - ⭐ 28
   Google AI Studio MCP Server - Powerful Gemini API integration for Model Context Protocol with multi-modal file processing, PDF-to-Markdown conversion, image analysis,   and audio transcription capabilities. Supports all Gemini 2.5 models with comprehensive file format support.

3800. **[mlb-mcp](https://github.com/etweisberg/mlb-mcp)** - ⭐ 28
   MCP server for advanced baseball analytics (statcast, fangraphs, baseball reference, mlb stats API)

3801. **[mcp-attr](https://github.com/frozenlib/mcp-attr)** - ⭐ 28
   A library for declaratively building Model Context Protocol servers.

3802. **[postmancer](https://github.com/hijaz/postmancer)** - ⭐ 28
   An experimental MCP server Rest Client intended to be a replacement of tools postman & insomnia

3803. **[mcp-config-manager](https://github.com/holstein13/mcp-config-manager)** - ⭐ 28
   Manage MCP server configs across Claude, Gemini & other AI systems. Interactive CLI for server enable/disable, preset management & config sync.

3804. **[Healthcare-MCP](https://github.com/innovaccer/Healthcare-MCP)** - ⭐ 28
   Specification and documentation for the Healthcare Model Context Protocol. This builds on top of the base Model Context Protocol

3805. **[tempo-mcp-server](https://github.com/ivelin-web/tempo-mcp-server)** - ⭐ 28
   MCP server for managing Tempo worklogs in Jira

3806. **[mcp-writer-substack](https://github.com/jonathan-politzki/mcp-writer-substack)** - ⭐ 28
   Model Context Protocol to bridge in Substack writings to Claude.

3807. **[nettune](https://github.com/jtsang4/nettune)** - ⭐ 28
   A network diagnostics and TCP optimization tool with MCP (Model Context Protocol) integration for AI-assisted configuration.

3808. **[kernel-mcp-server](https://github.com/kernel/kernel-mcp-server)** - ⭐ 28
   Open-source MCP server for secure, low-latency cloud-browser automation on Kernel.

3809. **[leanmcp-sdk](https://github.com/LeanMCP/leanmcp-sdk)** - ⭐ 28
   Production-ready TypeScript SDK for MCP servers: auth, multi-tenant, observability. Build enterprise AI agents fast.

3810. **[godot-dotnet-mcp](https://github.com/LuoxuanLove/godot-dotnet-mcp)** - ⭐ 28
   A Godot 4.6+ editor plugin that gives AI agents a real MCP interface to the live Godot editor: project state, scene editing, script analysis, runtime control, screenshots, logs, and client setup from inside the editor itself.

3811. **[MiAO-MCP-for-Unity](https://github.com/MiAO-AI-Lab/MiAO-MCP-for-Unity)** - ⭐ 28
   MCP Server + Plugin for Unity Editor and Unity game. The Plugin allows to connect to MCP clients like Claude Desktop or others.

3812. **[minds-mcp](https://github.com/mindsdb/minds-mcp)** - ⭐ 28
   An MCP (Model Context Protocol) server for Minds, allowing LLMs to interact with the Minds SDK through a standardized interface.

3813. **[laravel-mcp-sdk](https://github.com/mohamedahmed01/laravel-mcp-sdk)** - ⭐ 28
   Laravel Based Implementation for Model Context Protocol

3814. **[brlaw_mcp_server](https://github.com/pdmtt/brlaw_mcp_server)** - ⭐ 28
   A MCP (Model Context Protocol) server for agent-driven research on Brazilian law using official sources

3815. **[relace-mcp](https://github.com/possible055/relace-mcp)** - ⭐ 28
   Unofficial Relace MCP client with AI features. Personal project; not affiliated with or endorsed by Relace

3816. **[gemsuite-mcp](https://github.com/PV-Bhat/gemsuite-mcp)** - ⭐ 28
   Professional Gemini API integration for Claude and all MCP-compatible hosts with intelligent model selection and advanced file handling | Smithery.ai verified

3817. **[chat](https://github.com/repaera/chat)** - ⭐ 28
   Chat Client for Your Service's MCP Server

3818. **[atm](https://github.com/sfox38/atm)** - ⭐ 28
   Create secure and scoped Home Assistant API tokens for AI assistants and other MCP clients

3819. **[vsc-mcp](https://github.com/thomasgazzoni/vsc-mcp)** - ⭐ 28
   This project provides tools that expose Language Server Protocol (LSP) functionality as MCP (Model Context Protocol) tools

3820. **[emilie](https://github.com/veronica-builds/emilie)** - ⭐ 28
   Swiss sovereign legal AI. Fork of Mike, extended with MCP client and local model support (Apertus). Named after Emilie Kempin-Spyri.

3821. **[mcp-server-semgrep](https://github.com/VetCoders/mcp-server-semgrep)** - ⭐ 28
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

3822. **[manceps](https://github.com/zarpay/manceps)** - ⭐ 28
   Ruby client for the Model Context Protocol (MCP). Latin: one who takes in hand.

3823. **[claude-code-mcp](https://github.com/zebbern/claude-code-mcp)** - ⭐ 28
   Model Context Protocol (MCP) servers with Claude Code. These tools dramatically enhance Claude Code's capabilities, allowing it to interact with your filesystem, web browsers, and more.

3824. **[twincat-validator-mcp](https://github.com/agenticcontrolio/twincat-validator-mcp)** - ⭐ 27
   An MCP server that validates, auto-fixes, and scaffolds TwinCAT 3 XML files. Connect it to any LLM client to give your AI assistant reliable, deterministic TwinCAT code quality tooling — structural checks, 21 IEC 61131-3 OOP checks, auto-fix pipelines, and canonical skeleton generation.

3825. **[MCP-DB-Client](https://github.com/DitriXNew/MCP-DB-Client)** - ⭐ 27
   MCP layer for 1C

3826. **[systemprompt-mcp-notion](https://github.com/Ejb503/systemprompt-mcp-notion)** - ⭐ 27
   This an Model Context Protocol (MCP) server that integrates Notion into your AI workflows. This server enables seamless access to Notion through MCP, allowing AI agents to interact with pages, databases, and comments.

3827. **[fastify-mcp-server](https://github.com/flaviodelgrosso/fastify-mcp-server)** - ⭐ 27
   Fastify plugin to easily spin up Model Context Protocol (MCP) HTTP servers

3828. **[MCP-Developer-SubAgent](https://github.com/gensecaihq/MCP-Developer-SubAgent)** - ⭐ 27
    A specialized framework for Model Context Protocol (MCP) development featuring 8   Claude Code sub-agents, security hooks, and production-ready FastMCP server   templates. Provides immediate MCP development assistance through markdown-driven   agents with optional programmatic SDK .

3829. **[agent-hub-mcp](https://github.com/gilbarbara/agent-hub-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server that enables communication and coordination between multiple AI agents

3830. **[Excel-MCP-Server-Master](https://github.com/guillehr2/Excel-MCP-Server-Master)** - ⭐ 27
   Excel MCP Server - Manipulate Excel files without Microsoft Excel. Model Context Protocol for XLSX, XLSM with Claude AI integration

3831. **[Python-Runtime-Interpreter-MCP-Server](https://github.com/hileamlakB/Python-Runtime-Interpreter-MCP-Server)** - ⭐ 27
   PRIMS is a lightweight, open-source Model Context Protocol (MCP) server that lets LLM agents safely execute arbitrary Python code in a secure, throw-away sandbox.

3832. **[VercelGenUI_MCP](https://github.com/JamesSloan/VercelGenUI_MCP)** - ⭐ 27
   Proof of concept chat AI combining the Model Context Protocol (MCP) with Vercel's AI SDK UI

3833. **[slack-mcp-server](https://github.com/jtalk22/slack-mcp-server)** - ⭐ 27
   Session-based Slack MCP for Claude and MCP clients: local-first workflows, secure-default HTTP.

3834. **[symfony-mcp-server](https://github.com/klapaudius/symfony-mcp-server)** - ⭐ 27
   A Symfony package designed for building secure servers based on the Model Context Protocol, utilizing Server-Sent Events (SSE) and/or StreamableHTTP for real-time communication. It offers a scalable tool system tailored for enterprise-grade applications.

3835. **[MCP-Mastery-with-Claude-and-Langchain](https://github.com/laxmimerit/MCP-Mastery-with-Claude-and-Langchain)** - ⭐ 27
   Build MCP servers & clients with Python, Streamlit, ChromaDB, LangChain, LangGraph agents, and Ollama integrations

3836. **[aj-mcp](https://github.com/lightweight-component/aj-mcp)** - ⭐ 27
   Simple MCP SDK in Java

3837. **[aws-mcp](https://github.com/lokeswaran-aj/aws-mcp)** - ⭐ 27
   An MCP(Model Context Protocol) Server for AWS services

3838. **[ai-cli](https://github.com/manusa/ai-cli)** - ⭐ 27
   ai-cli lets you go from zero to AI-powered in seconds in a safe, automated and tailored way.

3839. **[nebulagraph-mcp-server](https://github.com/nebula-contrib/nebulagraph-mcp-server)** - ⭐ 27
   Model Context Protocol Server for NebulaGraph 3.x

3840. **[novyx-mcp](https://github.com/novyxlabs/novyx-mcp)** - ⭐ 27
   Persistent memory for AI agents. 107 MCP tools for remember, recall, rollback, audit, knowledge graph, eval, cortex, replay, governed actions, threat intel, auto-defense, Runtime v2 agents/missions, and more. Works locally (zero config) or with Novyx Cloud.

3841. **[openzeppelin-mcp](https://github.com/OpenZeppelin/openzeppelin-mcp)** - ⭐ 27
   Model Context Protocol Servers Repository for OpenZeppelin products

3842. **[deep-research-mcp](https://github.com/pinkpixel-dev/deep-research-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) compliant server designed for comprehensive web research. It uses Tavily's Search and Crawl APIs to gather detailed information on a given topic, then structures this data in a format perfect for LLMs to create high-quality markdown documents.

3843. **[mcp-web-browser](https://github.com/random-robbie/mcp-web-browser)** - ⭐ 27
   An advanced web browsing server for the Model Context Protocol (MCP) powered by Playwright, enabling headless browser interactions through a flexible, secure API.

3844. **[directus-mcp-server](https://github.com/rijkvanzanten/directus-mcp-server)** - ⭐ 27
   Model Context Protocol server for Directus

3845. **[rollbar-mcp-server](https://github.com/rollbar/rollbar-mcp-server)** - ⭐ 27
   Model Context Protocol server for Rollbar

3846. **[janee](https://github.com/rsdouglas/janee)** - ⭐ 27
   Secrets management for AI agents via MCP • @janeesecure

3847. **[mcp-stytch-consumer-todo-list](https://github.com/stytchauth/mcp-stytch-consumer-todo-list)** - ⭐ 27
   Workers + Stytch TODO App MCP Server

3848. **[suse-ai-up](https://github.com/SUSE/suse-ai-up)** - ⭐ 27
   A comprehensive platform for managing and proxying Model Context Protocol (MCP) servers, providing scalable AI service orchestration across multiple microservices.

3849. **[mcp_streamable_http](https://github.com/theailanguage/mcp_streamable_http)** - ⭐ 27
   Educational repo for MCP streamable HTTP servers and clients

3850. **[mcp-annotated-java-sdk](https://github.com/thought2code/mcp-annotated-java-sdk)** - ⭐ 27
   Annotation-driven MCP dev 🚀 No Spring, Zero Boilerplate, Pure Java

3851. **[mcp-local-dev](https://github.com/txbm/mcp-local-dev)** - ⭐ 27
   Let LLMs manage your local dev environments

3852. **[Memgpt-MCP-Server](https://github.com/Vic563/Memgpt-MCP-Server)** - ⭐ 27
   A Model Context Protocol (MCP) server that provides persistent memory and multi-model LLM support.

3853. **[gaia-x](https://github.com/YFGaia/gaia-x)** - ⭐ 27
   Gaia-X 基于AI新范式的下一代企业级AI应用平台。Gaia-X旨在实现类人脑的、针对企业办公业务场景的AI化赋能，包括一系列新颖而稳定的企业级AI功能，包括不限于：企业级管理功能、MCP Server支持（且支持将企业内部系统API转换为MCP Server提供服务）、支持自然语言驱动的RPA（大模型操作电脑）、划词分析和悬浮球等。

3854. **[mcp_rss](https://github.com/buhe/mcp_rss)** - ⭐ 26
   MCP RSS is a Model Context Protocol (MCP) server for interacting with RSS feeds.

3855. **[ton-blockchain-mcp](https://github.com/devonmojito/ton-blockchain-mcp)** - ⭐ 26
   A Model Context Protocol (MCP) server written in Python for natural language interaction with the TON blockchain 💎

3856. **[mcp-auth](https://github.com/famma-ai/mcp-auth)** - ⭐ 26
   MCP Auth via Reverse Proxy

3857. **[skill-mcp](https://github.com/fkesheh/skill-mcp)** - ⭐ 26
   LLM-managed skills platform using MCP - create, edit, and execute skills programmatically in Claude, Cursor, and any MCP-compatible client without manual file uploads.

3858. **[greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server)** - ⭐ 26
   A Model Context Protocol (MCP) server for GreptimeDB

3859. **[fastify-mcp](https://github.com/haroldadmin/fastify-mcp)** - ⭐ 26
   A Fastify plugin to run Model Context Protocol (MCP) servers

3860. **[webmcp-bridge](https://github.com/holon-run/webmcp-bridge)** - ⭐ 26
   Bridge local MCP clients to browser WebMCP tools through Playwright, using native WebMCP when available and injected adapters when not.

3861. **[strava-mcp](https://github.com/kw510/strava-mcp)** - ⭐ 26
   A Model Context Protocol (MCP) server with Strava OAuth integration, built on Cloudflare Workers. Enables secure authentication and tool access for MCP clients like Claude and Cursor through Strava login. Perfect for developers looking to integrate Strava authentication with AI tools.

3862. **[lotus-wisdom-mcp](https://github.com/linxule/lotus-wisdom-mcp)** - ⭐ 26
   Contemplative reasoning MCP server — Lotus Sutra wisdom framework with interactive ext-apps journey visualization.

3863. **[taiwan-holiday-mcp](https://github.com/lis186/taiwan-holiday-mcp)** - ⭐ 26
   一個基於 Model Context Protocol (MCP) 的台灣假期查詢伺服器，為 AI 工具提供準確的台灣國定假日資訊。

3864. **[plux](https://github.com/milisp/plux)** - ⭐ 26
   💡AI finder/explorer. One click @files via a visual filetree and save insights in a notepad. build with Tauri

3865. **[chatbot_Shopify](https://github.com/Mobeen-Dev/chatbot_Shopify)** - ⭐ 26
   Agentic Shopify Chatbot with MCP integration, embedded directly into Shopify via a Theme Extension

3866. **[Mobus](https://github.com/mobus-ai/Mobus)** - ⭐ 26
   Search, preview, and analyze datasets from 20+ platforms via a single MCP connector. Works with Claude instantly.

3867. **[Risuai-NodeOnly](https://github.com/mrbart3885/Risuai-NodeOnly)** - ⭐ 26
   Make your own story. User-friendly software for LLM roleplaying, forked from Risuai

3868. **[markview](https://github.com/paulhkang94/markview)** - ⭐ 26
   Native macOS markdown preview + MCP server for Claude Code. Swift/SwiftUI, GFM, Mermaid, syntax highlighting. No Electron.

3869. **[MCPHammer](https://github.com/praetorian-inc/MCPHammer)** - ⭐ 26
   MCP security testing framework for evaluating Model Context Protocol server vulnerabilities

3870. **[mcp-structured-thinking](https://github.com/Promptly-Technologies-LLC/mcp-structured-thinking)** - ⭐ 26
   A TypeScript Model Context Protocol (MCP) server to allow LLMs to programmatically construct mind maps to explore an idea space, with enforced "metacognitive" self-reflection

3871. **[mcp-client-x](https://github.com/RGGH/mcp-client-x)** - ⭐ 26
   Python MCP client + server example

3872. **[github-repo-mcp](https://github.com/Ryan0204/github-repo-mcp)** - ⭐ 26
   Model Context Protocol server for Github Repo // Reading Github Repo

3873. **[mcp-frontend-testing](https://github.com/StudentOfJS/mcp-frontend-testing)** - ⭐ 26
   Frontend testing tools for Model Context Protocol

3874. **[mcp-ffmpeg-helper](https://github.com/sworddut/mcp-ffmpeg-helper)** - ⭐ 26
   一个基于 Model Context Protocol (MCP) 的 FFmpeg 辅助工具，提供视频处理功能。

3875. **[mcp-desktop-automation](https://github.com/tanob/mcp-desktop-automation)** - ⭐ 26
   A Model Context Protocol server that provides desktop automation capabilities using RobotJS and screenshot capabilities

3876. **[gemini-webapi-mcp](https://github.com/AndyShaman/gemini-webapi-mcp)** - ⭐ 25
   MCP server for Google Gemini — free image generation, editing & chat via browser cookies. No API keys needed.

3877. **[mcp-webdriveragent](https://github.com/AppiumTestDistribution/mcp-webdriveragent)** - ⭐ 25
   This is a Model Context Protocol (MCP) server that provides tools for building and signing WebDriverAgent for iOS.

3878. **[microsoft_fabric_mcp](https://github.com/Augustab/microsoft_fabric_mcp)** - ⭐ 25
   MCP server wrapping around the Fabric Rest API

3879. **[slack-mcp-server](https://github.com/AVIMBU/slack-mcp-server)** - ⭐ 25
   A Model Context Protocol Server for Interacting with Slack

3880. **[Super-Productivity-MCP](https://github.com/b0x42/Super-Productivity-MCP)** - ⭐ 25
   MCP server that connects AI assistants to Super Productivity — manage tasks, projects, and tags through Claude, Kiro, or any MCP client

3881. **[nestjs-mcp](https://github.com/bamada/nestjs-mcp)** - ⭐ 25
   NestJS module for seamless Model Context Protocol (MCP) server integration using decorators.

3882. **[php-mcp-sdk](https://github.com/dalehurley/php-mcp-sdk)** - ⭐ 25
   PHP implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.  ✨ Features  🚀 Complete MCP Protocol Support - Full implementation of the MCP specification 🔧 Type-Safe - Leverages PHP 8.1+ type system with enums, union types, and strict typing ⚡ Async First

3883. **[azure-diagram-mcp](https://github.com/dminkovski/azure-diagram-mcp)** - ⭐ 25
   MCP server that turns natural-language prompts into Microsoft Azure architecture diagrams (PNG) using Python Diagrams + Graphviz.

3884. **[openai-copilot](https://github.com/feiskyer/openai-copilot)** - ⭐ 25
   Your life Copilot powered by LLM models (CLI interface for LLM models with MCP tools).

3885. **[mcp-php](https://github.com/garyblankenship/mcp-php)** - ⭐ 25
   model context protocol or mcp for php laravel

3886. **[muster](https://github.com/giantswarm/muster)** - ⭐ 25
   MCP tool management and workflow proxy

3887. **[ccmcp](https://github.com/gsong/ccmcp)** - ⭐ 25
   A CLI tool that intelligently discovers, validates, and selects MCP (Model Context Protocol) server configurations for Claude Code.

3888. **[ib-mcp-cache-server](https://github.com/ibproduct/ib-mcp-cache-server)** - ⭐ 25
   Memory Cache Server for use with supported MCP API Clients.

3889. **[prometheus-mcp](https://github.com/idanfishman/prometheus-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server implementation that provides AI agents with programmatic access to Prometheus metrics via a unified interface.

3890. **[nix-mcp-servers](https://github.com/ismail-kattakath/nix-mcp-servers)** - ⭐ 25
   A nix flake for configuring Model Context Protocol (MCP) servers across supported AI assistant clients

3891. **[Tiny-OAI-MCP-Agent](https://github.com/jalr4ever/Tiny-OAI-MCP-Agent)** - ⭐ 25
   A MCP protocol agent that operates a SQLite using natural language by OpenAI-Compatible LLM.

3892. **[cfbd-mcp-server](https://github.com/lenwood/cfbd-mcp-server)** - ⭐ 25
   An MCP server enabling CFBD API queries within Claude Desktop.

3893. **[mcpmate](https://github.com/loocor/mcpmate)** - ⭐ 25
   MCPMate is a progressive MCP management center for organizing servers, clients, profiles, capabilities, and runtime visibility in one local workspace.

3894. **[Screenhand](https://github.com/manushi4/Screenhand)** - ⭐ 25
   Give AI eyes and hands on your desktop. Open-source MCP server for desktop automation — screenshots, UI control, browser automation, OCR. Works with Claude, Cursor, and any MCP client. macOS + Windows.

3895. **[mcp-media-processor](https://github.com/maoxiaoke/mcp-media-processor)** - ⭐ 25
   A Node.js server implementing Model Context Protocol (MCP) for media processing operations, providing powerful video and image manipulation capabilities.

3896. **[meeting-mcp](https://github.com/Meeting-BaaS/meeting-mcp)** - ⭐ 25
   Model Context Protocol server for AI assistants to create meeting bots, search transcripts, and manage meeting recordings.

3897. **[mcpc](https://github.com/micl2e2/mcpc)** - ⭐ 25
   Cross-platform C SDK for Model Context Protocol (MCP), in modern🚀 C23.

3898. **[gyazo-mcp-server](https://github.com/nota/gyazo-mcp-server)** - ⭐ 25
   Official Model Context Protocol server for Gyazo

3899. **[mcp-manager](https://github.com/nstebbins/mcp-manager)** - ⭐ 25
   CLI tool for managing Model Context Protocol (MCP) servers in one place & using them across them different clients

3900. **[json2video-mcp-server](https://github.com/omergocmen/json2video-mcp-server)** - ⭐ 25
   Message Communication Protocol server for json2video API integration

3901. **[llmqore](https://github.com/Palm1r/llmqore)** - ⭐ 25
   Qt C++ library for working with AI/LLM Providers and MCP

3902. **[Intercept](https://github.com/PolicyLayer/Intercept)** - ⭐ 25
   The control layer for AI agents. Intercept enforces hard limits on every MCP tool call before execution. Rate limits, spend caps, access controls. Open source.

3903. **[askr](https://github.com/Sweatent/askr)** - ⭐ 25
   MCP Q&A Assistant - Async Q&A capabilities for AI clients via MCP protocol

3904. **[alpaca-mcp-server](https://github.com/tedlikeskix/alpaca-mcp-server)** - ⭐ 25
   Model Context Protocol (MCP) server for Alpaca trading API

3905. **[linux-command-mcp](https://github.com/xkiranj/linux-command-mcp)** - ⭐ 25
   MCP server and client for running Linux commands

3906. **[mcp-playground](https://github.com/zanetworker/mcp-playground)** - ⭐ 25
   Simple MCP Client for remote MCP Servers 🌐

3907. **[mcp-stdio-guard](https://github.com/1Utkarsh1/mcp-stdio-guard)** - ⭐ 24
   Catch stdout pollution and handshake failures in MCP stdio servers before clients do.

3908. **[agentgate](https://github.com/agentkitai/agentgate)** - ⭐ 24
   Approval workflows for AI agents

3909. **[identity-spec](https://github.com/agntcy/identity-spec)** - ⭐ 24
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

3910. **[Awesome-MCP](https://github.com/Albertchamberlain/Awesome-MCP)** - ⭐ 24
   Awesome-MCP Servers & Clients & Funny things

3911. **[ai-memory-mcp](https://github.com/alphaonedev/ai-memory-mcp)** - ⭐ 24
   Persistent memory for any AI — MCP server, HTTP API, CLI. Works with Claude, ChatGPT, Grok, Gemini, Codex, Cursor, OpenClaw, and any MCP client. 97.8% R@5 on LongMemEval. Pure SQLite FTS5, zero cloud dependencies.

3912. **[DeepResearchMCP](https://github.com/ameeralns/DeepResearchMCP)** - ⭐ 24
   Deep Research MCP is an intelligent research assistant built on the Model Context Protocol (MCP) that performs comprehensive, multi-step research on any topic.

3913. **[roo-logger](https://github.com/annenpolka/roo-logger)** - ⭐ 24
   An MCP server for logging activity in Roo Code/Cline.

3914. **[bzm-mcp](https://github.com/Blazemeter/bzm-mcp)** - ⭐ 24
   Official BlazeMeter MCP Server for AI-driven performance testing

3915. **[mcp-chain-of-draft-server](https://github.com/bsmi021/mcp-chain-of-draft-server)** - ⭐ 24
   Chain of Draft Server is a powerful AI-driven tool that helps developers make better decisions through systematic, iterative refinement of thoughts and designs. It integrates seamlessly with popular AI agents and provides a structured approach to reasoning, API design, architecture decisions, code reviews, and implementation planning.

3916. **[mcp-task-manager-server](https://github.com/bsmi021/mcp-task-manager-server)** - ⭐ 24
   A local Model Context Protocol (MCP) server providing backend tools for client-driven project and task management using a SQLite database.

3917. **[puzzlebox](https://github.com/cliffhall/puzzlebox)** - ⭐ 24
   An MCP server that hosts finite state machines as dynamic resources that multiple clients can subscribe to and be updated when their state changes.

3918. **[typescript-mcp-client](https://github.com/CodelyTV/typescript-mcp-client)** - ⭐ 24

3919. **[context-lens](https://github.com/cornelcroi/context-lens)** - ⭐ 24
   Semantic search knowledge base for MCP-enabled AI assistants. Index local files or GitHub repos, query with natural language. Built on LanceDB vector storage. Works with Claude Desktop, Cursor, and other MCP clients.

3920. **[Autonomous-AI-Trading-Agent-MCP-Flash-Arb-Engine](https://github.com/Cortex-AI-Software/Autonomous-AI-Trading-Agent-MCP-Flash-Arb-Engine)** - ⭐ 24
   🧠 Autonomous AI Trading Agent & Multi-Chain Flash-Arb Engine (v2.0 Beta). Powered by MCP-Protocol & LLM reasoning. High-frequency arbitrage on Solana, Base, and EVM L2s. Built by Cortex Software Labs.

3921. **[Autonomous-AI-Trading-Agent-MCP-Flash-Arb-Engine](https://github.com/cortexaiofficial/Autonomous-AI-Trading-Agent-MCP-Flash-Arb-Engine)** - ⭐ 24
   🧠 Autonomous AI Trading Agent & Multi-Chain Flash-Arb Engine (v2.0 Beta). Powered by MCP-Protocol & LLM reasoning. High-frequency arbitrage on Solana, Base, and EVM L2s. Built by Cortex Software Labs.

3922. **[cf-mcp-client](https://github.com/cpage-pivotal/cf-mcp-client)** - ⭐ 24
   Tanzu Platform Chat

3923. **[calendar-mcp](https://github.com/deciduus/calendar-mcp)** - ⭐ 24
   This project implements a Python-based MCP (Model Context Protocol) server that acts as an interface between Large Language Models (LLMs) and the Google Calendar API. It enables LLMs to perform calendar operations via natural language requests.

3924. **[mcp-cmd](https://github.com/developit/mcp-cmd)** - ⭐ 24
   CLI for calling successive MCP Server tools

3925. **[dive](https://github.com/DuckTapeKiller/dive)** - ⭐ 24
   Dive is a secure, local-first desktop client for Ollama and Pi agentic AI. Features an ultra-compact offline RAG engine for indexing massive book libraries, MCP tool integration, sandboxed custom skills, PDF extraction, and macOS daemon support.

3926. **[MCP](https://github.com/EduBase/MCP)** - ⭐ 24
   The EduBase MCP server enables Claude and other LLMs to interact with EduBase's comprehensive e-learning platform through the Model Context Protocol (MCP).

3927. **[GenomeMCP](https://github.com/Eldergenix/GenomeMCP)** - ⭐ 24
   An AI-driven genomic intelligence system delivering structured ClinVar interpretation and high-precision exon, intron, and gene queries using the Model Context Protocol (MCP).

3928. **[opnsense-mcp-server](https://github.com/floriangrousset/opnsense-mcp-server)** - ⭐ 24
   A Model Context Protocol (MCP) server implementation for managing OPNsense firewalls. This server allows Claude and other MCP-compatible clients to interact with all features exposed by the OPNsense API.

3929. **[Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop](https://github.com/gloveboxes/Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop)** - ⭐ 24

3930. **[langchain-mcp-tools-ts](https://github.com/hideya/langchain-mcp-tools-ts)** - ⭐ 24
   MCP to LangChain Tools Conversion Utility / TypeScript

3931. **[mcp-rss-aggregator](https://github.com/imprvhub/mcp-rss-aggregator)** - ⭐ 24
   Model Context Protocol Server for aggregating RSS feeds in Claude Desktop

3932. **[cursor-db-mcp](https://github.com/jbdamask/cursor-db-mcp)** - ⭐ 24
   Model Context Protocol server for querying Cursor chat history

3933. **[mcp-unifi-applications](https://github.com/KallistoX/mcp-unifi-applications)** - ⭐ 24
   An MCP server that exposes UniFi application API documentation (Network, Protect, Site Manager) as queryable tools for Claude Desktop, Claude Code (VS Code / JetBrains), or any MCP-compatible client.

3934. **[codemesh](https://github.com/kiliman/codemesh)** - ⭐ 24
   The Self-Improving MCP Server - Agents write code to orchestrate multiple MCP servers with intelligent TypeScript execution and auto-augmentation

3935. **[readwise-vector-db](https://github.com/leonardsellem/readwise-vector-db)** - ⭐ 24
   Turn your Readwise library into a blazing-fast, self-hosted semantic search engine – complete with nightly syncs, vector search API, Prometheus metrics, and a streaming MCP server for LLM clients.

3936. **[html-to-markdown-mcp](https://github.com/levz0r/html-to-markdown-mcp)** - ⭐ 24
   MCP server for converting HTML to Markdown using Turndown.js. Fetch web pages and convert them to clean, formatted Markdown.

3937. **[bruno-mcp](https://github.com/macarthy/bruno-mcp)** - ⭐ 24
   🚀 MCP server for generating Bruno API testing files programmatically. Create collections, environments, requests, and test scripts using AI clients like Claude Desktop.

3938. **[ProxmoxMCP-advance](https://github.com/Markermav/ProxmoxMCP-advance)** - ⭐ 24
   ProxmoxMCP (advance): MCP for Proxmox integration in Claude, Goose, Cline, any client.

3939. **[metmuseum-mcp](https://github.com/mikechao/metmuseum-mcp)** - ⭐ 24
   Met Museum MCP integration to discover the art collection at The Metropolitan Museum of Art in New York

3940. **[mcp-template-dotnet](https://github.com/NikiforovAll/mcp-template-dotnet)** - ⭐ 24
   This repository contains a template for creating a Model Context Protocol (MCP) applications in .NET.

3941. **[nlweb-net](https://github.com/nlweb-ai/nlweb-net)** - ⭐ 24
   The official .NET 9 implementation of the NLWeb protocol for building natural language web interfaces with support for List, Summarize, and Generate query modes, plus Model Context Protocol (MCP) integration for AI clients.

3942. **[mcp-oauth-proxy](https://github.com/obot-platform/mcp-oauth-proxy)** - ⭐ 24
   Oauth 2.1 proxy server that can autheticate client and proxy requests to mcp server

3943. **[GUI-MCP](https://github.com/PhialsBasement/GUI-MCP)** - ⭐ 24
   A Blueprint-style visual node editor for creating FastMCP servers. Build MCP tools, resources, and prompts by connecting nodes - no coding required.

3944. **[WikidataMCP](https://github.com/philippesaade-wmde/WikidataMCP)** - ⭐ 24
   Model Context Protocol for Wikidata

3945. **[k6-mcp-server](https://github.com/QAInsights/k6-mcp-server)** - ⭐ 24
   k6 MCP server

3946. **[Claude-Code-MCP-Manager](https://github.com/qdhenry/Claude-Code-MCP-Manager)** - ⭐ 24
    A comprehensive tool to manage Model Context Protocol (MCP) configurations for Claude code

3947. **[n8n-AI-agent-DVM-MCP-client](https://github.com/r0d8lsh0p/n8n-AI-agent-DVM-MCP-client)** - ⭐ 24
   An AI agent built in n8n which can find and use Model Context Protocol (MCP) Server Tools served as Data Vending Machines (DVM) over the Nostr network.

3948. **[csv-editor](https://github.com/santoshray02/csv-editor)** - ⭐ 24
   Stateful CSV editing MCP server for AI assistants — sessions, undo/redo, auto-save, and 39 pandas-powered tools. Works    with Claude, ChatGPT, Cursor, Windsurf, Claude Code, and any MCP-compatible client. Built on FastMCP 3

3949. **[mcp-client-agent](https://github.com/shane-kercheval/mcp-client-agent)** - ⭐ 24
   CLI that uses DSPy to interact with MCP servers.

3950. **[mcp-server-semgrep](https://github.com/Szowesgad/mcp-server-semgrep)** - ⭐ 24
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

3951. **[solana-mcp](https://github.com/tony-42069/solana-mcp)** - ⭐ 24
   A comprehensive Solana MCP (Model Context Protocol) server for analyzing memecoins, tracking trends, and providing AI-powered insights using cultural analysis and on-chain data.

3952. **[lua-resty-mcp](https://github.com/ufownl/lua-resty-mcp)** - ⭐ 24
   Model Context Protocol SDK implemented in Lua for OpenResty

3953. **[nexo](https://github.com/wazionapps/nexo)** - ⭐ 24
   NEXO Brain — Shared brain for AI agents. Persistent memory, semantic RAG, natural forgetting, metacognitive guard, trust scoring, 150+ MCP tools. Works with Claude Code, Codex, Claude Desktop & any MCP client. 100% local, open source, free.

3954. **[WikidataMCP](https://github.com/wmde/WikidataMCP)** - ⭐ 24
   Model Context Protocol for Wikidata

3955. **[python-sequential-thinking-mcp](https://github.com/XD3an/python-sequential-thinking-mcp)** - ⭐ 24
   A Python implementation of the Sequential Thinking MCP server using the official Model Context Protocol (MCP) Python SDK. This server facilitates a detailed, step-by-step thinking process for problem-solving and analysis.

3956. **[room-mcp](https://github.com/agree-able/room-mcp)** - ⭐ 23
   Allow MCP clients like claude-desktop to use rooms to coordinate with other agents

3957. **[autotask-mcp](https://github.com/asachs01/autotask-mcp)** - ⭐ 23
   MCP server for Kaseya Autotask PSA — 39 tools for companies, tickets, projects, time entries, and more

3958. **[Model-Context-Protocol](https://github.com/Coding-Crashkurse/Model-Context-Protocol)** - ⭐ 23

3959. **[mcp-twitter-server](https://github.com/crazyrabbitLTC/mcp-twitter-server)** - ⭐ 23
   Model Context Protocol Server for Accessing twitter

3960. **[slack-mcp-client](https://github.com/csonigo/slack-mcp-client)** - ⭐ 23
   An MCP client for slack in Typescript

3961. **[mcp-web-scraper](https://github.com/Decodo/mcp-web-scraper)** - ⭐ 23
   The Decodo MCP server which enables MCP clients to interface with services.

3962. **[swift-mcp](https://github.com/DePasqualeOrg/swift-mcp)** - ⭐ 23
   Full-featured Swift SDK for Model Context Protocol servers and clients

3963. **[jsonv-ts](https://github.com/dswbx/jsonv-ts)** - ⭐ 23
   JSON Schema builder and validator for TypeScript with static type inference, Hono middleware for OpenAPI generation and validation, and MCP server/client implementation. Lightweight, dependency-free, and built on Web Standards.

3964. **[ollama-pi-chat](https://github.com/DuckTapeKiller/ollama-pi-chat)** - ⭐ 23
   A secure, local-first desktop client for Ollama and Pi agentic AI. Features an ultra-compact offline RAG engine for indexing massive book libraries, MCP tool integration, sandboxed custom skills, PDF extraction, and macOS daemon support.

3965. **[eleven.shopping](https://github.com/elevenlabs/eleven.shopping)** - ⭐ 23
   ElevenLabs Agent with Storefront MCP UI Server & MCP UI client

3966. **[pupila](https://github.com/FranRom/pupila)** - ⭐ 23
   Local-first daily job aggregator. AI review per job via your own LLM CLI, swipe-to-apply triage, and an MCP server for AI clients.

3967. **[cortex](https://github.com/FreePeak/cortex)** - ⭐ 23
   A declarative platform for building Model Context Protocol (MCP) servers in Golang—exposing tools, resources & prompts in a clean, structured way

3968. **[herald-mail-app](https://github.com/herald-email/herald-mail-app)** - ⭐ 23
   Herald is a terminal email client and inbox cleanup tool with IMAP, AI-assisted triage, MCP tools, and SSH/browser-friendly app modes.

3969. **[home-assistant-mcp](https://github.com/hpohlmann/home-assistant-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) integration that enables AI assistants to search for and control Home Assistant devices through natural language commands in Cursor.

3970. **[jigsawstack-mcp-server](https://github.com/JigsawStack/jigsawstack-mcp-server)** - ⭐ 23
   Model Context Protocol Server that allows AI models to interact with JigsawStack models!

3971. **[mcp-framework](https://github.com/koki7o/mcp-framework)** - ⭐ 23
   Rust MCP framework for building AI agents

3972. **[paraview_mcp](https://github.com/LLNL/paraview_mcp)** - ⭐ 23
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

3973. **[balldontlie-mcp](https://github.com/mikechao/balldontlie-mcp)** - ⭐ 23
   An MCP Server implementation that integrates the Balldontlie API, to provide information about players, teams and games for the NBA, NFL and MLB

3974. **[mcp-community](https://github.com/Mirascope/mcp-community)** - ⭐ 23
   Easily run, deploy, and connect to MCP servers

3975. **[agent-studio-starter](https://github.com/nsphung/agent-studio-starter)** - ⭐ 23
   Stop building AI agents from scratch. Bootstrap starter Agent app with LangGraph, CopilotKit, and beautiful Generative UIs.

3976. **[mcp-add](https://github.com/paoloricciuti/mcp-add)** - ⭐ 23
   Universal cli to add an MCP server to a variety of clients

3977. **[lexis](https://github.com/R0MADEV/lexis)** - ⭐ 23
   Lexical + structural code search MCP server for Claude Code, Cursor, Windsurf and any MCP client. Gives AI assistants 28 precise search tools so they find the right code fast 80% fewer tokens per task. No vectors, no embeddings, just ripgrep.

3978. **[your-money-left-the-chat](https://github.com/Rayato159/your-money-left-the-chat)** - ⭐ 23
   A Rust + MCP powered financial tracker that knows exactly where your money ghosted you.

3979. **[mcp-scan](https://github.com/rodolfboctor/mcp-scan)** - ⭐ 23
   Security scanner for MCP server configurations. Detects secrets, CVEs, permission issues, and exfiltration vectors across 10 AI tool clients.

3980. **[codeprism](https://github.com/rustic-ai/codeprism)** - ⭐ 23
   An experimental, 100% AI-generated, high-performance code intelligence server providing AI assistants with a graph-based understanding of codebases.

3981. **[aws-s3-mcp](https://github.com/samuraikun/aws-s3-mcp)** - ⭐ 23
   MCP server to integrate AWS S3 and LLM

3982. **[awesome-agent-skills-mcp](https://github.com/shadowrootdev/awesome-agent-skills-mcp)** - ⭐ 23
   MCP server providing 100+ AI agent skills from Anthropic, Vercel, Trail of Bits, Hugging Face & more. Works with Claude, GitHub Copilot, and any MCP client.

3983. **[lightdash-mcp-server](https://github.com/syucream/lightdash-mcp-server)** - ⭐ 23
   A MCP(Model Context Protocol) server that accesses to Lightdash

3984. **[flutter-ai-labs](https://github.com/theshivamlko/flutter-ai-labs)** - ⭐ 23
   A curated collection of LLM-powered Flutter apps built using RAG, AI Agents, Multi-Agent Systems, MCP, and Voice Agents.

3985. **[lineshopping-api-mcp](https://github.com/woraphol-j/lineshopping-api-mcp)** - ⭐ 23
   Model Context Protocol (MCP) server for the LINE SHOPPING API. Enables AI agents and tools to manage products, inventory, orders, and settlements on LINE SHOPPING via auto-generated MCP tools from the official OpenAPI spec.

3986. **[mcp-pa-ai-agent](https://github.com/zhangzhongnan928/mcp-pa-ai-agent)** - ⭐ 23
   A personal assistant AI agent built with the Model Context Protocol (MCP)

3987. **[mcp-server-amazon-bedrock](https://github.com/zxkane/mcp-server-amazon-bedrock)** - ⭐ 23
   Model Context Procotol(MCP) server for using Amazon Bedrock Nova Canvas to generate images

3988. **[biznagafest-mcp](https://github.com/0GiS0/biznagafest-mcp)** - ⭐ 22
   MCP Servers en Málaga con salero

3989. **[p5js-ai-editor](https://github.com/adilmoujahid/p5js-ai-editor)** - ⭐ 22
   A modern, web-based IDE for creating and editing p5.js sketches with AI assistance and Model Context Protocol (MCP) integration for Claude Desktop.

3990. **[gemini-mcp-client](https://github.com/angrysky56/gemini-mcp-client)** - ⭐ 22
   A MCP (Model Context Protocol) client that uses Google Gemini AI models for intelligent tool usage and conversation handling.  Tested working nicely with Claude Desktop as an MCP Server currently. Based on untested AI gen code by a non-coder use at own risk.

3991. **[conductor](https://github.com/aryabyte21/conductor)** - ⭐ 22
   Manage MCP server configs across AI coding clients

3992. **[mcp-prompt-optimizer](https://github.com/Bubobot-Team/mcp-prompt-optimizer)** - ⭐ 22
   Advanced MCP server providing cutting-edge prompt optimization tools with research-backed strategies

3993. **[hs-mcp](https://github.com/buecking/hs-mcp)** - ⭐ 22
   Haskell server/client for MCP (Model Context Protocol)

3994. **[perplexity-mcp-server](https://github.com/cyanheads/perplexity-mcp-server)** - ⭐ 22
   A Perplexity API MCP server that unlocks Perplexity's search-augmented AI capabilities for LLM agents. Features robust error handling, secure input validation, and transparent reasoning with the showThinking parameter.

3995. **[teamcity-mcp](https://github.com/Daghis/teamcity-mcp)** - ⭐ 22
   Model Context Protocol (MCP) server for JetBrains TeamCity: control builds, tests, agents and configs from AI coding assistants.

3996. **[DANP-Engine](https://github.com/DANP-LABS/DANP-Engine)** - ⭐ 22
   A trusted AI Model Context Protocol (MCP) runtime for secure, decentralized AI tools and services.

3997. **[mcp-server-oracle](https://github.com/hdcola/mcp-server-oracle)** - ⭐ 22
   Model Context Protocol server to access oracle database

3998. **[mcp-observer-server](https://github.com/hesreallyhim/mcp-observer-server)** - ⭐ 22
   An MCP server that provides server-to-client notifications for file changes that the client subscribes to

3999. **[higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation that enables comprehensive configuration and management of Higress.

4000. **[mcp-knowledge-base](https://github.com/hjlee94/mcp-knowledge-base)** - ⭐ 22
   MCP agent/client/server implementation for private knowledge base

4001. **[ida-codex-mcp](https://github.com/Iamgublin/ida-codex-mcp)** - ⭐ 22
   IDA Codex MCP bridges IDA Pro 9.2 with the MCP ecosystem. It provides an IDA plugin and a stdio MCP server that expose   function lists, call graphs, Hex‑Rays pseudocode, disassembly, imports/exports, xrefs, strings, and memory reads to   MCP clients.

4002. **[MobSF-MCP](https://github.com/il-il1/MobSF-MCP)** - ⭐ 22
   a Node.js-based Model Context Protocol implementation for MobSF

4003. **[MicrosoftGraph_Transcript_MCP](https://github.com/ITSpecialist111/MicrosoftGraph_Transcript_MCP)** - ⭐ 22
   A remote Model Context Protocol (MCP) server that retrieves Microsoft Teams meeting transcripts via the Microsoft Graph API, using delegated **OAuth 2.0 On-Behalf-Of (OBO)** authentication.  Designed for integration with Microsoft Copilot Studio (via the MCP Wizard), though any MCP-compatible client can connect.

4004. **[mcp-flux-studio](https://github.com/jmanhype/mcp-flux-studio)** - ⭐ 22
   A Model Context Protocol server for Flux image generation, providing tools for image generation, manipulation, and control

4005. **[jenkins-mcp-enterprise](https://github.com/Jordan-Jarvis/jenkins-mcp-enterprise)** - ⭐ 22
   The most advanced Jenkins MCP server available - Enterprise debugging, multi-instance management, AI-powered failure analysis, vector search, and configurable diagnostics for complex CI/CD pipelines.

4006. **[Jiva](https://github.com/KarmaloopAI/Jiva)** - ⭐ 22
   Jiva is a CLI-first, open source autonomous AI agent and open alternative to Claude. Built in TypeScript with a three-agent architecture (Manager, Worker, Client), it autonomously plans and executes tasks from your terminal. Supports MCP servers, a built-in Skills system, and Jiva Personas - a plugin framework fully compatible with Claude Plugins.

4007. **[Elysia-mcp](https://github.com/keithagroves/Elysia-mcp)** - ⭐ 22
   Model Context Protocol (MCP) Server for Bun and Elysia

4008. **[dbt-docs-mcp](https://github.com/mattijsdp/dbt-docs-mcp)** - ⭐ 22
   MCP (model context protocol) server for interacting with dbt Docs

4009. **[mcpagentai](https://github.com/mcpagents-ai/mcpagentai)** - ⭐ 22
   Python SDK designed to simplify interactions with MCP (Model Context Protocol) servers. It provides an easy-to-use interface for connecting to MCP servers, reading resources, and calling tools

4010. **[awesome-mcp](https://github.com/MCPHubCloud/awesome-mcp)** - ⭐ 22
   A collection of mcp servers/client/sdks

4011. **[google-scholar-mcp](https://github.com/mochow13/google-scholar-mcp)** - ⭐ 22
   An MCP server for Google Scholar written in TypeScript with Streamable HTTP

4012. **[IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server)** - ⭐ 22
   MCP server for Industrial IoT, SCADA and PLC systems. Unifies MQTT sensors, Modbus devices and industrial equipment into a single AI-orchestrable API. Features real-time monitoring, alarms, time-series storage and actuator control.

4013. **[spectrawl](https://github.com/Pyx-Corp/spectrawl)** - ⭐ 22
   The unified web layer for AI agents. Search (8 engines), stealth browse, auth, and act on 24 platforms. One npm install, self-hosted.

4014. **[gumroad-mcp](https://github.com/rmarescu/gumroad-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation for Gumroad API

4015. **[mini_agent](https://github.com/sergenes/mini_agent)** - ⭐ 22
   A minimal AI agent built from scratch — no agent framework, just Python, the OpenAI SDK, and a `while` loop. Accompanies the Medium article "Build Your Own AI Agent from Scratch." Three execution modes: `local` (Ollama only), `remote` (cloud provider), `mixed` (local orchestrates, delegates to remote).

4016. **[mcp-sse-authenticated-cloud-run](https://github.com/the-freetech-company/mcp-sse-authenticated-cloud-run)** - ⭐ 22
   Host an Model Context Protocol SSE deployment on Cloud Run, Authenticating with IAM.

4017. **[printify-mcp](https://github.com/TSavo/printify-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server for integrating AI assistants with Printify's print-on-demand platform

4018. **[MCP-123](https://github.com/Tylersuard/MCP-123)** - ⭐ 22
   The easiest possible implementation of an MCP server and client.  Set up a server or a client in 2 lines of code.

4019. **[async-mcp](https://github.com/v3g42/async-mcp)** - ⭐ 22
   A minimalistic async Rust implementation of the Model Context Protocol (MCP).

4020. **[aisdk-mcp-bridge](https://github.com/vrknetha/aisdk-mcp-bridge)** - ⭐ 22
   Bridge package enabling seamless integration between Model Context Protocol (MCP) servers and AI SDK tools. Supports multiple server types, real-time communication, and TypeScript.

4021. **[unity-mcp](https://github.com/wondeks/unity-mcp)** - ⭐ 22
   A Unity MCP server that allows MCP clients like Claude Desktop or Cursor to perform Unity Editor actions.

4022. **[nobitex-mcp-server](https://github.com/xmannii/nobitex-mcp-server)** - ⭐ 22
   a Model Context Protocol (MCP) server that provides access to cryptocurrency market data from the Nobitex API.

4023. **[mcp-kling](https://github.com/199-mcp/mcp-kling)** - ⭐ 21
   🎬 The FIRST MCP server for Kling AI video generation! Generate stunning AI videos directly from Claude.

4024. **[PDB-MCP-Server](https://github.com/Augmented-Nature/PDB-MCP-Server)** - ⭐ 21
   A Model Context Protocol (MCP) server that provides access to the Protein Data Bank (PDB) - the worldwide repository of information about the 3D structures of proteins, nucleic acids, and complex assemblies.

4025. **[mcp-link](https://github.com/AuraFriday/mcp-link)** - ⭐ 21
   Let AI agents like ChatGPT & Claude use real-world local/remote tools you approve via browser extension + optional MCP server

4026. **[MCPRules](https://github.com/bartwisch/MCPRules)** - ⭐ 21
   A powerful Model Context Protocol (MCP) server that manages and serves programming guidelines and rules. This server integrates with development tools to provide consistent coding standards across projects.

4027. **[emqx-mcp-server](https://github.com/Benniu/emqx-mcp-server)** - ⭐ 21
   A Model Context Protocol (MCP) server implementation that provides EMQX MQTT broker interaction.

4028. **[knowledgebase-mcp](https://github.com/biocontext-ai/knowledgebase-mcp)** - ⭐ 21
   BioContextAI Knowledgebase MCP server for biomedical agentic AI

4029. **[registry](https://github.com/biocontext-ai/registry)** - ⭐ 21
   The BioContextAI Registry for biomedical MCP servers

4030. **[skill-to-mcp](https://github.com/biocontext-ai/skill-to-mcp)** - ⭐ 21
   Convert AI Skills (Claude Skills format) to MCP server resources - Part of BioContextAI

4031. **[mcpsharepoint](https://github.com/BrianCusack/mcpsharepoint)** - ⭐ 21
   Model Context Protocol server that provides access to Organisational SharePoint.

4032. **[mcp-file-operations-server](https://github.com/bsmi021/mcp-file-operations-server)** - ⭐ 21
   A Model Context Protocol (MCP) server that provides enhanced file operation capabilities with streaming, patching, and change tracking support.

4033. **[bridge-mcp](https://github.com/codingjam/bridge-mcp)** - ⭐ 21
   Open Source MCP gateway and proxy for Model Context Protocol (MCP) servers with enterprise authentication and service discovery

4034. **[archmcp](https://github.com/dejo1307/archmcp)** - ⭐ 21
   archmcp - MCP Architectural Snapshot Server and Knowledge Graph

4035. **[Air-Quality-Trends-Analysis-Project](https://github.com/dyneth02/Air-Quality-Trends-Analysis-Project)** - ⭐ 21
   Full-stack air quality analytics platform built with FastAPI, React, and MySQL. Aggregates multi-source PM2.5/PM10 data, performs multi-city comparison and time-series forecasting (SARIMAX), and integrates an LLM-based planning agent with tiered access, secure APIs, and PDF reporting.

4036. **[factorly](https://github.com/factorly-dev/factorly)** - ⭐ 21
   Factorly is a local runtime for agent tool chains. It manages tool calls, injects credentials from an encrypted vault, enforces governance rules, and logs everything. Your agent sees workflows, tools, and data. Secrets stay secret.

4037. **[code-context-mcp](https://github.com/fkesheh/code-context-mcp)** - ⭐ 21
   A Model Context Protocol (MCP) server for providing code context from git repositories

4038. **[mcp-ai-agent](https://github.com/fkesheh/mcp-ai-agent)** - ⭐ 21
   A TypeScript library that enables AI agents to leverage MCP (Model Context Protocol) servers for enhanced capabilities. This library integrates with the AI SDK to provide a seamless way to connect to MCP servers and use their tools in AI-powered applications.

4039. **[uk-case-law-mcp-server](https://github.com/georgejeffers/uk-case-law-mcp-server)** - ⭐ 21
   MCP server for UK case law using The National Archives API. Enables LLMs to search, retrieve, and cite UK legal judgments.

4040. **[kiro-professional-toolkit](https://github.com/gkhantyln/kiro-professional-toolkit)** - ⭐ 21
   ⚡ The most complete Kiro IDE toolkit — 34 AI Agents, 32 Expert Hooks, 50 Skills, 22 Steering Rules & 44 MCP Integrations. From React to Rust, Spring to GraphQL — production-grade workflows, one install.

4041. **[ffmpeg-mcp-lite](https://github.com/kevinwatt/ffmpeg-mcp-lite)** - ⭐ 21
   MCP server for video/audio processing via FFmpeg - convert, compress, trim, extract audio, add subtitles

4042. **[github-repos-manager-mcp](https://github.com/kurdin/github-repos-manager-mcp)** - ⭐ 21
   GitHub Repos Manager MCP Server that enables your MCP client (e.g., Claude Desktop, Roo Code, etc.) to interact with GitHub repositories using your GitHub personal access token.

4043. **[dsers-mcp-product](https://github.com/lofder/dsers-mcp-product)** - ⭐ 21
   An open-source MCP server to automate DSers product import, bulk edit variants, and push to Shopify/Wix/WooCommerce using AI. Supports AliExpress, Alibaba, 1688.

4044. **[mcp-sentry](https://github.com/MCP-100/mcp-sentry)** - ⭐ 21
   A Model Context Protocol server for retrieving and analyzing issues from Sentry.io

4045. **[starbase](https://github.com/metorial/starbase)** - ⭐ 21
   Connect, explore, and test any MCP server with AI models 🤖 ⚡

4046. **[DocsRay](https://github.com/MIMICLab/DocsRay)** - ⭐ 21
   Lightweight PDF Q&A tool powered by RAG (Retrieval-Augmented Generation) with MCP (Model Context Protocol) Support.

4047. **[obsidian-http-mcp](https://github.com/NasAndNora/obsidian-http-mcp)** - ⭐ 21
   First HTTP-native MCP server for Obsidian - Compatible with any MCP client (Claude Code, Codex, Gemini, etc.) without stdio bugs

4048. **[mcp-diagnostics-extension](https://github.com/newbpydev/mcp-diagnostics-extension)** - ⭐ 21
   VS Code extension that exposes diagnostic problems via Model Context Protocol (MCP) for AI agents and tools

4049. **[istat_mcp_server](https://github.com/ondata/istat_mcp_server)** - ⭐ 21
   MCP server to query Italian statistics (ISTAT) via SDMX API — compatible with any MCP client

4050. **[agentidentityprotocol](https://github.com/openagentidentityprotocol/agentidentityprotocol)** - ⭐ 21
   Agent Identity Protocol - Zero-trust security layer for AI agents. Policy enforcement proxy for MCP with Human-in-the-Loop approval, DLP scanning, and audit logging.

4051. **[mendeley-mcp](https://github.com/pallaprolus/mendeley-mcp)** - ⭐ 21
   MCP server for Mendeley reference manager - search, retrieve, and manage your academic library from Claude and other MCP clients

4052. **[mcp-server](https://github.com/paperinvest/mcp-server)** - ⭐ 21
   Official MCP server for Paper's trading platform - enables AI assistants to interact with Paper's API

4053. **[ARBuilder](https://github.com/Quantum3-Labs/ARBuilder)** - ⭐ 21
   AI-powered code generator for Arbitrum Stylus, SDK bridging, dApps & Orbit chains — 19 MCP tools with RAG

4054. **[open-code-review](https://github.com/raye-deng/open-code-review)** - ⭐ 21
   🤖 AI code quality gate for AI-generated code. Detects hallucinated packages, phantom dependencies, stale APIs, and more. MCP Server + CLI + CI/CD Action.

4055. **[MCP_A2A](https://github.com/regismesquita/MCP_A2A)** - ⭐ 21
   A2A MCP Server is a lightweight Python bridge that lets Claude Desktop or any MCP client talk to A2A agents. It provides three tools: register servers, list agents, and call an agent, enabling quick integration of A2A-compatible agents with zero boilerplate for rapid prototyping.

4056. **[retyc-cli](https://github.com/retyc/retyc-cli)** - ⭐ 21
   Official CLI client for Retyc with MCP server

4057. **[pixelpanda-mcp](https://github.com/RyanKramer/pixelpanda-mcp)** - ⭐ 21
   MCP server for PixelPanda — 31 AI image processing tools for Claude Desktop, Cursor & other MCP clients

4058. **[mcp-server-memos-py](https://github.com/RyoJerryYu/mcp-server-memos-py)** - ⭐ 21
   A Python package enabling LLM models to interact with the Memos server via the MCP interface for searching, creating, retrieving, and managing memos.

4059. **[mcp-server-client-demo](https://github.com/S1LV3RJ1NX/mcp-server-client-demo)** - ⭐ 21
   Streamable HTTP based MCP server and Client demo with auto registry, Dockerfile setup and env.

4060. **[turn-mcp](https://github.com/shiahonb777/turn-mcp)** - ⭐ 21
   Achieve infinite conversation turns in a single API request via turn-mcp.             Self-hosted MCP server with browser console for human-in-the-loop AI agents.

4061. **[grumpydev-mcp](https://github.com/sinedied/grumpydev-mcp)** - ⭐ 21
   Let the grumpy senior dev review your code with this MCP server

4062. **[heuristic-mcp](https://github.com/softerist/heuristic-mcp)** - ⭐ 21
   Enhanced MCP server for semantic code search with call-graph proximity, recency ranking, and find-similar-code. Built for AI coding assistants.

4063. **[command-executor-mcp-server](https://github.com/Sunwood-ai-labs/command-executor-mcp-server)** - ⭐ 21
   Model Context Protocol Server for Safely Executing Pre-approved Commands

4064. **[supabase-mcp-client](https://github.com/tambo-ai/supabase-mcp-client)** - ⭐ 21
   Supabase MCP client react app with Tambo

4065. **[supabase-mcp-client](https://github.com/tambo-labs/supabase-mcp-client)** - ⭐ 21
   Supabase MCP client react app with Tambo

4066. **[codeTree](https://github.com/ThinkyMiner/codeTree)** - ⭐ 21
   MCP server with 23 tools for structured code understanding via tree-sitter. 10 languages. 999 tests. One-command install.

4067. **[mcp-deepseek-demo](https://github.com/Ulanxx/mcp-deepseek-demo)** - ⭐ 21
   deepseek 结合 mcp 场景，最小用例，包括 client and server

4068. **[mcp-korean-spell](https://github.com/winterjung/mcp-korean-spell)** - ⭐ 21
   MCP(Model Context Protocol) server designed for Korean spell checking

4069. **[codex-mcp-tool](https://github.com/x51xxx/codex-mcp-tool)** - ⭐ 21

4070. **[mcp-libsql](https://github.com/Xexr/mcp-libsql)** - ⭐ 21
   Secure MCP server for libSQL databases with comprehensive tools, connection pooling, and transaction support. Built with TypeScript for Claude Desktop, Claude Code, Cursor, and other MCP clients.

4071. **[mcp_documents_reader](https://github.com/xt765/mcp_documents_reader)** - ⭐ 21
   Model Context Protocol (MCP) server exposes tools to read multiple document types including DOCX, PDF, Excel, and TXT. This has been tested on Trae Desktop.

4072. **[agentic-ai-engineering](https://github.com/zkzkGamal/agentic-ai-engineering)** - ⭐ 21
   Agentic AI Engineering is a production-grade engineering resource for building modern agentic AI systems with LangChain, LangGraph, RAG, MCP, local models, and deployable Python services.

4073. **[mcp-ts](https://github.com/zonlabs/mcp-ts)** - ⭐ 21
   An MCP client library for building conversational AI applications with dynamic tool discovery for context-efficient agents.

4074. **[mcp](https://github.com/zuplo/mcp)** - ⭐ 21
   A fetch API based TypeScript SDK for MCP

4075. **[mcp-client-and-proxy](https://github.com/appsecco/mcp-client-and-proxy)** - ⭐ 20
   A universal MCP client with proxying feature to interact with MCP Servers which support STDIO transport.

4076. **[docdex](https://github.com/bekirdag/docdex)** - ⭐ 20
   A document index with MCP, http and client support. https://docdex.org/

4077. **[eraser-io-mcp-server](https://github.com/buck-0x/eraser-io-mcp-server)** - ⭐ 20
   A Python MCP (Model Context Protocol) server and CLI tool to render diagrams using the Eraser API.

4078. **[gpt2099.nu](https://github.com/cablehead/gpt2099.nu)** - ⭐ 20
   a Nushell cross.stream extension to interact with LLMs and MCP servers

4079. **[MCP-Agent](https://github.com/CursorTouch/MCP-Agent)** - ⭐ 20
   Connect to any MCP servers using agents

4080. **[emceepee](https://github.com/eastlondoner/emceepee)** - ⭐ 20
   MCP server to dynamically connect to other MCP servers & exposes the entire MCP protocol via tool calls. Ideal for testing MCPs during development or accessing MCP Server features from clients that do not support notifications, resource templates, prompts or elicitations.

4081. **[mcp-server-microsoft-paint](https://github.com/ghuntley/mcp-server-microsoft-paint)** - ⭐ 20

4082. **[agent-mcp](https://github.com/grupa-ai/agent-mcp)** - ⭐ 20
   MCPAgent for Grupa.AI Multi-agent Collaboration Network (MACNET) with Model Context Protocol (MCP) capabilities baked in

4083. **[hasmcp-ce](https://github.com/hasmcp/hasmcp-ce)** - ⭐ 20
   HasMCP Community Edition

4084. **[cucumberstudio-mcp](https://github.com/HeroSizy/cucumberstudio-mcp)** - ⭐ 20
   MCP Server for Cucumber Studio

4085. **[mcpbi](https://github.com/jonaolden/mcpbi)** - ⭐ 20
   PowerBI MCP server to give LLM clients (Claude, GH Copilot,etc) context from locally running PowerBI Desktop instances.

4086. **[webclaw](https://github.com/kuroko1t/webclaw)** - ⭐ 20
   A WebMCP-native browser agent that runs inside your real Chrome — control it from Claude, Cursor, and any MCP client

4087. **[mcp-free-usdc-transfer](https://github.com/magnetai/mcp-free-usdc-transfer)** - ⭐ 20
   MCP (Model Context Protocol) server - free usdc transfer powered by Coinbase CDP

4088. **[openinstaflow](https://github.com/Narla-Venkata-Anand-Sai-Kumar/openinstaflow)** - ⭐ 20
   OpenInstaFlow — An MCP server that exposes the Instagram Graph API to any MCP client (Claude Desktop, Claude Code, Cursor )

4089. **[lyra-tool-discovery](https://github.com/nirholas/lyra-tool-discovery)** - ⭐ 20
   AI powered automation toolkit which acts as an agent that discovers MCP servers for you. Point it at GitHub/npm/configure your own discovery, let GPT or Claude analyze the API or MCP or any tool, get ready-to-ship plugin configs. Zero manual work.

4090. **[hoot](https://github.com/Portkey-AI/hoot)** - ⭐ 20
   MCP Testing Tool — Like Postman, but for the Model Context Protocol.

4091. **[mcp-server-amazon](https://github.com/rigwild/mcp-server-amazon)** - ⭐ 20
   🛍📦 Unofficial Amazon Model Context Protocol Server (MCP) - Search products and purchase directly from Claude AI! ✨

4092. **[brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server)** - ⭐ 20
   MCP server for Brightspace (D2L). Check grades, due dates, assignments, announcements, rosters, syllabus & course content via Claude, ChatGPT, Cursor, Windsurf, or any MCP client. Works with any school. npm: npx brightspace-mcp-server@latest

4093. **[mcp-frontend](https://github.com/shaharia-lab/mcp-frontend)** - ⭐ 20
   Frontend for MCP (Model Context Protocol) Kit for Go - A Complete MCP solutions for ready to use

4094. **[gh-mcp](https://github.com/shuymn/gh-mcp)** - ⭐ 20
   A GitHub CLI extension that seamlessly runs the github-mcp-server using your existing gh authentication. Eliminates manual PAT setup by automatically retrieving GitHub credentials and launching the MCP server with proper authentication.

4095. **[strategy-mcp](https://github.com/sohaibt/strategy-mcp)** - ⭐ 20
   strategy-mcp is an open source MCP server that exposes professional-grade product strategy frameworks as structured tools. Any MCP-compatible AI assistant (Claude, Cursor, Cline) can install it and immediately get access to structured strategy analysis, RICE, JTBD, competitive positioning, assumption mapping, and more.

4096. **[daiv](https://github.com/srtab/daiv)** - ⭐ 20
   Your AI-powered SWE teammate, built into your git workflow

4097. **[mcp-server-runner](https://github.com/yonaka15/mcp-server-runner)** - ⭐ 20
   A WebSocket server implementation for running Model Context Protocol (MCP) servers. This application enables MCP servers to be accessed via WebSocket connections, facilitating integration with web applications and other network-enabled clients.

4098. **[openapi2mcptools](https://github.com/2013xile/openapi2mcptools)** - ⭐ 19
   OpenAPI specifications => MCP (Model Context Protocol) tools

4099. **[mcp-yfinance](https://github.com/9nate-drake/mcp-yfinance)** - ⭐ 19
   MCP Server for fething yfinance financial data into Claude Desktop

4100. **[mcp-server-mariadb](https://github.com/abel9851/mcp-server-mariadb)** - ⭐ 19
   An mcp server that provides read-only access to MariaDB.

4101. **[awesome-mcp-security](https://github.com/AgentSeal/awesome-mcp-security)** - ⭐ 19
   Security scores for 800+ MCP servers. 9 analyzers scan for prompt injection, toxic flows, and attack surface risks. Updated daily. 🛡️

4102. **[mcpx](https://github.com/AIGC-Hackers/mcpx)** - ⭐ 19
   苹果 MCP 工具 ✅

4103. **[Augmented-Nature-UniProt-MCP-Server](https://github.com/Augmented-Nature/Augmented-Nature-UniProt-MCP-Server)** - ⭐ 19
   A comprehensive Model Context Protocol (MCP) server providing advanced access to the UniProt protein database.

4104. **[guidance-for-scalable-model-inference-and-agentic-ai-on-amazon-eks](https://github.com/aws-solutions-library-samples/guidance-for-scalable-model-inference-and-agentic-ai-on-amazon-eks)** - ⭐ 19
   Comprehensive, scalable ML inference architecture using Amazon EKS, leveraging Graviton processors for cost-effective CPU-based inference and GPU instances for accelerated inference. Guidance provides a complete end-to-end platform for deploying LLMs with agentic AI capabilities, including RAG and MCP

4105. **[bonnard](https://github.com/bonnard-data/bonnard)** - ⭐ 19
   Open-source agentic schema for reliable data outputs. Query data through MCP and via our SDK. Create apps, embed data or just simply explore through your preferred agent.

4106. **[mcp-server-codegraph](https://github.com/CartographAI/mcp-server-codegraph)** - ⭐ 19
   MCP server for graph representation of a codebase

4107. **[termlink](https://github.com/chu2bard/termlink)** - ⭐ 19
   MCP server for shell and terminal operations

4108. **[pophive-mcp-server](https://github.com/Cicatriiz/pophive-mcp-server)** - ⭐ 19
   *Featured on Claude!* MCP server for accessing near real-time health data from Yale's PopHIVE platform, as well as additional HHS/CDC data

4109. **[toolkit-mcp-server](https://github.com/cyanheads/toolkit-mcp-server)** - ⭐ 19
   A Model Context Protocol server providing LLM Agents with system utilities and tools, including IP geolocation, network diagnostics, system monitoring, cryptographic operations, and QR code generation.

4110. **[bambu-printer-mcp](https://github.com/DMontgomery40/bambu-printer-mcp)** - ⭐ 19
   MCP server for Bambu Lab 3D printers — STL manipulation, BambuStudio slicing, and direct printer control

4111. **[mcp](https://github.com/EmilLindfors/mcp)** - ⭐ 19
    A crate for making MCP (Model Context Protocol) compatible programs with rust

4112. **[spectrawl](https://github.com/FayAndXan/spectrawl)** - ⭐ 19
   The unified web layer for AI agents. Search (8 engines), stealth browse, auth, and act on 24 platforms. One npm install, self-hosted.

4113. **[short-url](https://github.com/fengzhongsen/short-url)** - ⭐ 19
   简单易用的短链接生成工具，完全开源、免费、无需登录，可私有化部署，链接永久有效！

4114. **[mcp-anything](https://github.com/gabrielekarra/mcp-anything)** - ⭐ 19
   One command to turn any codebase into an MCP server

4115. **[SimpleMcp.Demo](https://github.com/hassanhabib/SimpleMcp.Demo)** - ⭐ 19
   Simplest Possible Demo for Building MCP Server & Client

4116. **[openpyxl-mcp-server](https://github.com/jonemo/openpyxl-mcp-server)** - ⭐ 19
   A thin wrapper around the OpenPyXl Python library that exposes some of its features as Model Context Protocol (MCP) server. This allows Claude and other MCP clients to fetch data from Excel files.

4117. **[mcp-agent](https://github.com/joshuaalpuerto/mcp-agent)** - ⭐ 19
   Lightweight, focused utilities to manage connections and execute MCP tools with minimal integration effort. Use it to directly call tools or build simple agents within your current architecture.

4118. **[unified-gateway-mcp](https://github.com/mcp360/unified-gateway-mcp)** - ⭐ 19
   Unified MCP Gateway Platform, Marketplace & Custom MCPs

4119. **[better-notion-mcp](https://github.com/n24q02m/better-notion-mcp)** - ⭐ 19
   Markdown-first MCP server for Notion API - composite tools optimized for AI agents

4120. **[davinci-mcp-professional](https://github.com/Positronikal/davinci-mcp-professional)** - ⭐ 19
   An enterprise-grade MCP server that exposes the full functionality of DaVinci Resolve and DaVinci Resolve Studio (through version 20) to either Claude Desktop or Cursor MCP clients. Fully configured and tested as a Claude Desktop Extension making installation as easy as clicking a button. Supports both Windows and Macintosh.

4121. **[slm-mesh](https://github.com/qualixar/slm-mesh)** - ⭐ 19
   Peer-to-peer communication for AI coding agents. 8 MCP tools, full CLI, Python client. Part of the Qualixar research initiative by Varun Pratap Bhardwaj.

4122. **[MCP-Development-with-Rust](https://github.com/RustSandbox/MCP-Development-with-Rust)** - ⭐ 19
   This comprehensive learning resource provides two complete tutorials for mastering Model Context Protocol (MCP) development with Rust. From beginner-friendly introductions to production-ready enterprise applications, these tutorials guide you through every aspect of building robust MCP servers.

4123. **[mcp-spotify-player](https://github.com/vsaez/mcp-spotify-player)** - ⭐ 19
   MCP server to manage Spotify from MCP clients

4124. **[it-tools-mcp](https://github.com/wrenchpilot/it-tools-mcp)** - ⭐ 19
   A comprehensive Model Context Protocol (MCP) server that provides access to over 100 IT tools and utilities commonly used by developers, system administrators, and IT professionals. Inspired by https://github.com/CorentinTh/it-tools

4125. **[nanobanana-mcp](https://github.com/YCSE/nanobanana-mcp)** - ⭐ 19
   Gemini Vision & Image Generation MCP for Claude Desktop and Claude Code

4126. **[builtwith-api](https://github.com/zcaceres/builtwith-api)** - ⭐ 19
   TypeScript library, MCP, and agent-friendly CLI for the BuiltWith API.

4127. **[subcog](https://github.com/zircote/subcog)** - ⭐ 19
   Persistent memory system for AI coding assistants. Captures decisions, learnings, and context from coding sessions. Features hybrid search (semantic + BM25), MCP server integration, SQLite persistence with knowledge graph, and proactive memory surfacing. Written in Rust.

4128. **[Agentic-AI-Tutorial](https://github.com/zkzkGamal/Agentic-AI-Tutorial)** - ⭐ 19
   Step-by-step guide to building agentic AI systems with LangGraph and MCP — from basic LLM calls to multi-node agents that reason, plan, and use real tools.

4129. **[arxiv-mcp-server](https://github.com/anuj0456/arxiv-mcp-server)** - ⭐ 18
   MCP server for arXiv.org - Search, analyze, and export academic papers with AI assistants. Features advanced paper discovery, citation analysis, trend tracking, and multi-format exports.

4130. **[sveltekit-mcp-starter](https://github.com/axel-rock/sveltekit-mcp-starter)** - ⭐ 18

4131. **[mcp-chain-of-draft-prompt-tool](https://github.com/brendancopley/mcp-chain-of-draft-prompt-tool)** - ⭐ 18
   MCP prompt tool applying Chain-of-Draft (CoD) reasoning - BYOLLM

4132. **[kanboard-mcp](https://github.com/ChristianJStarr/kanboard-mcp)** - ⭐ 18
   Transform your Kanboard.org into an AI-powered project management powerhouse! This plugin enables complete control over Kanboard through the Model Context Protocol (MCP), allowing AI assistants like Cursor, Claude, and other MCP clients to manage your projects through natural language commands.

4133. **[mcp-server-templates](https://github.com/Data-Everything/mcp-server-templates)** - ⭐ 18
   A flexible platform that provides Docker & Kubernetes backends, a lightweight CLI (mcpt), and client utilities for seamless MCP integration. Spin up servers from templates, route requests through a single endpoint with load balancing, and support both deployed (HTTP) and local (stdio) transports — all with sensible defaults and YAML-based configs.

4134. **[local-mcp-gateway](https://github.com/DXHeroes/local-mcp-gateway)** - ⭐ 18
   Aggregate multiple MCP servers into a single endpoint with web UI, OAuth 2.1, and profile-based tool management

4135. **[amazon-seller-mcp](https://github.com/enginterzi/amazon-seller-mcp)** - ⭐ 18
   Transform Your Amazon Business with AI - The first Model Context Protocol (MCP) client that seamlessly connects Claude and other AI agents to Amazon's Selling Partner API, enabling intelligent automation of your entire seller workflow from inventory management to listing optimization.

4136. **[MCP-Manager-GUI](https://github.com/gabrielbacha/MCP-Manager-GUI)** - ⭐ 18
   MCP Toggle is a simple GUI tool to help you manage MCP servers across clients seamlessly.

4137. **[seats.aero-mcp-server](https://github.com/gavgrego/seats.aero-mcp-server)** - ⭐ 18
   MCP server allowing clients to interface with the seats.aero API

4138. **[ContextOS](https://github.com/itallstartedwithaidea/ContextOS)** - ⭐ 18
   Unified MCP context intelligence platform — pip-installable CLI that absorbed 6 foundational repos. Context engineering for AI agents.

4139. **[mistr-agent](https://github.com/itisaevalex/mistr-agent)** - ⭐ 18
   A MCP client that enables Mistral AI models to autonomously execute complex tasks across web and local environments through standardized agentic capabilities.

4140. **[Devmind-MCP](https://github.com/JochenYang/Devmind-MCP)** - ⭐ 18
   DevMind MCP provides **persistent memory capabilities** for AI assistants through the Model Context Protocol (MCP). It enables AI to remember context across conversations, automatically track development activities, and retrieve relevant information intelligently.

4141. **[mcp-chat-studio](https://github.com/JoeCastrom/mcp-chat-studio)** - ⭐ 18
   A powerful MCP testing tool with multi-provider LLM support (Ollama, OpenAI, Claude, Gemini). Test, debug, and develop MCP servers with a modern UI.

4142. **[agentify](https://github.com/koriyoshi2041/agentify)** - ⭐ 18
   Agent Interface Compiler — One command. Every agent speaks your product. Transform OpenAPI specs into MCP Servers, Skills, CLAUDE.md, AGENTS.md, and more.

4143. **[awesome-dxt-mcp](https://github.com/MCPStar/awesome-dxt-mcp)** - ⭐ 18
   🚀 A curated list of awesome Desktop Extensions (DXT) and MCP servers for Claude Desktop. Discover, share, and contribute to the growing ecosystem of AI-powered local tools and automations.

4144. **[mcp-chatbot](https://github.com/mctrinh/mcp-chatbot)** - ⭐ 18
   MCP Chatbot powered by Anthropic Claude. Delivering on‐demand literature search and summarisation for academics and engineers

4145. **[signal-mcp-client](https://github.com/piebro/signal-mcp-client)** - ⭐ 18
   An MCP client that uses signal for sending and receiving messages.

4146. **[mcp-obsidian](https://github.com/Piotr1215/mcp-obsidian)** - ⭐ 18
   simple mcp server for interacting with local obsidian notes

4147. **[sufetch](https://github.com/productdevbook/sufetch)** - ⭐ 18
   Type-safe OpenAPI clients with MCP server for AI-driven API exploration

4148. **[easymcp](https://github.com/promptmesh/easymcp)** - ⭐ 18
   A high performance MCP client sdk for python

4149. **[scopus-mcp](https://github.com/qwe4559999/scopus-mcp)** - ⭐ 18
   A Model Context Protocol (MCP) server for Elsevier Scopus. Allows AI assistants like Claude to search academic papers, retrieve abstracts, and analyze author profiles directly.

4150. **[rigour](https://github.com/rigour-labs/rigour)** - ⭐ 18
   The immune system for AI coding agents

4151. **[robotmem](https://github.com/robotmem/robotmem)** - ⭐ 18
   Robot Memory - Persistent memory system for AI robots. MCP Server + hybrid search + spatial retrieval.

4152. **[cmcp](https://github.com/RussellLuo/cmcp)** - ⭐ 18
   A command-line utility for interacting with MCP servers.

4153. **[speclock](https://github.com/sgroy10/speclock)** - ⭐ 18
   AI Constraint Engine by Sandeep Roy — stops AI from breaking what you locked. 100/100 on Claude's adversarial test suite. 42 MCP tools. Works with Bolt.new, Lovable, Claude Code, Cursor. Free & open source.

4154. **[mcp-this](https://github.com/shane-kercheval/mcp-this)** - ⭐ 18
   mcp-this lets you turn any command-line tool into an MCP tool and create structured prompt templates that any MCP Client (e.g. Claude Desktop) can use. er for any command

4155. **[XcodeMCPWrapper](https://github.com/SoundBlaster/XcodeMCPWrapper)** - ⭐ 18
   MCP that makes Xcode 26.3's MCP compatible with Cursor and other strict MCP-spec-compliant clients

4156. **[toolhive-catalog](https://github.com/stacklok/toolhive-catalog)** - ⭐ 18
   ToolHive's registry catalog of MCP servers

4157. **[titanmind-whatsapp-mcp](https://github.com/TitanmindAGI/titanmind-whatsapp-mcp)** - ⭐ 18
   A WhatsApp marketing and messaging tool MCP (Model Control Protocol) service using Titanmind. Handles free-form messages (24hr window) and template workflows automatically

4158. **[mcp-copilot](https://github.com/tshu-w/mcp-copilot)** - ⭐ 18
   A meta MCP server that seamlessly scales LLMs to 1000+ MCP servers through automatic routing.

4159. **[mcp-gateway](https://github.com/unrelated-ai/mcp-gateway)** - ⭐ 18
   Transform any HTTP endpoint into an MCP server. Aggregate multiple MCP servers, manage configuration profiles, and serve them through a unified gateway with multi-tenant isolation.

4160. **[seedream-image-mcp](https://github.com/wearzdk/seedream-image-mcp)** - ⭐ 18
   🚀 PixelMCP | 为你的 Cursor、Claude Code 等集成AI绘画能力，让AI生成的页面不再单调！

4161. **[Frontapp-MCP](https://github.com/zqushair/Frontapp-MCP)** - ⭐ 18
   MCP server and client for Frontapp

4162. **[youtube-mcp-server](https://github.com/0GiS0/youtube-mcp-server)** - ⭐ 17
   Cómo crear MCP Servers y usarlos con GitHub Copilot Chat 🚀💻🤖

4163. **[videocapture-mcp](https://github.com/13rac1/videocapture-mcp)** - ⭐ 17
   Model Context Protocol (MCP) server to capture images from an OpenCV-compatible webcam or video source

4164. **[mcp_client](https://github.com/app-appplayer/mcp_client)** - ⭐ 17

4165. **[model-context-protocol-survey](https://github.com/asinghcsu/model-context-protocol-survey)** - ⭐ 17
   Model Context Protocol (MCP)

4166. **[mcp-koii](https://github.com/benjaminr/mcp-koii)** - ⭐ 17
   MCP Server for Teenage Engineering EP-133 KO-II

4167. **[programmatic-tool-calling-ai-sdk](https://github.com/cameronking4/programmatic-tool-calling-ai-sdk)** - ⭐ 17
   ⚡ Cut LLM inference costs 80% with Programmatic Tool Calling. Instead of N tool call round-trips, generate JavaScript to orchestrate tools in Vercel Sandbox. Supports Anthropic, OpenAI, 100+ models via AI Gateway. Novel MCP Bridge for external service integration.

4168. **[ia-na-pratica](https://github.com/Code4Delphi/ia-na-pratica)** - ⭐ 17
   IA na Prática: LLM, RAG, MCP, Agents, Function Calling, Multimodal, TTS/STT e mais

4169. **[FocusRelayMCP](https://github.com/deverman/FocusRelayMCP)** - ⭐ 17
   Talk to your OmniFocus tasks. An OmniFocus MCP server that lets AI assistants query your tasks, projects, and tags using natural language—no more clicking through endless lists.

4170. **[video-research-mcp](https://github.com/Galbaz1/video-research-mcp)** - ⭐ 17
   Give Claude Code 41 research & video tools with one command. Video analysis, deep research, content extraction, explainer video creation, and Weaviate vector search — powered by Gemini 3.1 Pro.

4171. **[mcp-email-client](https://github.com/gamalan/mcp-email-client)** - ⭐ 17
   Email Client as MCP Server. Feature: multiple configuration, more than just gmail

4172. **[mcp-web-client](https://github.com/hemanth/mcp-web-client)** - ⭐ 17
   A web-based client for connecting to MCP servers with OAuth support

4173. **[qmt-mcp-server](https://github.com/jm12138/qmt-mcp-server)** - ⭐ 17
   基于 QMT 平台股票行情的 MCP 服务器，用于提供股票市场数据下载和查询的功能。

4174. **[askit](https://github.com/johnrobinsn/askit)** - ⭐ 17
   LLM Function Calling Library and CLI with Support for MCP Servers

4175. **[smartlead-mcp-server](https://github.com/jonathan-politzki/smartlead-mcp-server)** - ⭐ 17
   Local version of Smartlead MCP for quick download and deployment to MCP compatible clients or n8n.

4176. **[mcp-server-prometheus](https://github.com/loglmhq/mcp-server-prometheus)** - ⭐ 17
   MCP server for interacting with Prometheus

4177. **[mcpforge](https://github.com/lorenzosaraiva/mcpforge)** - ⭐ 17

4178. **[ai-cli-mcp](https://github.com/mkXultra/ai-cli-mcp)** - ⭐ 17
   MCP server to run Claude, Codex, and Gemini CLI agents in the background from any MCP client.

4179. **[osmmcp](https://github.com/NERVsystems/osmmcp)** - ⭐ 17
   OpenStreetMap MCP server providing precision geospatial tools for LLMs via Model Context Protocol. Features geocoding, routing, nearby places, neighborhood analysis, EV charging stations, and more.

4180. **[extract-llms-docs](https://github.com/nirholas/extract-llms-docs)** - ⭐ 17
   Extract documentation for AI agents from any site with llms.txt support. Features MCP server, REST API, batch processing, and multiple export formats.

4181. **[github-to-mcp](https://github.com/nirholas/github-to-mcp)** - ⭐ 17
   Convert GitHub repositories to MCP servers automatically. Extract tools from OpenAPI, GraphQL & REST APIs for Claude Desktop, Cursor, Windsurf, Cline & VS Code. AI-powered code generation creates type-safe TypeScript/Python MCP servers. Zero config setup - just paste a repo URL. Built for AI assistants & LLM tool integration.

4182. **[autowpmcp](https://github.com/Njengah/autowpmcp)** - ⭐ 17
   AutoWP MCP (Model Context Protocol) server connects Claude to WordPress site and allows users to ask Claude to write blog posts and automatically publish them to WordPress sites.

4183. **[GUARDRAIL](https://github.com/nshkrdotcom/GUARDRAIL)** - ⭐ 17
   GUARDRAIL - MCP Security - Gateway for Unified Access, Resource Delegation, and Risk-Attenuating Information Limits

4184. **[nasa](https://github.com/peteretelej/nasa)** - ⭐ 17
   Go client library for NASA APIs: APOD, NeoWs, DONKI, NASA Image Library, SSD/CNEOS, EONET. Supports built-in rate-limiting, a CLI & MCP Server

4185. **[lightdash_mcp](https://github.com/poddubnyoleg/lightdash_mcp)** - ⭐ 17
   mcp server for lightdash

4186. **[CereBro](https://github.com/rob1997/CereBro)** - ⭐ 17
   A model-agnostic MCP Client-Server for .Net and Unity

4187. **[mcp-http-client-example](https://github.com/slavashvets/mcp-http-client-example)** - ⭐ 17
   Simple example client demonstrating how to connect to MCP servers over HTTP (SSE)

4188. **[mcp-server-python-template](https://github.com/sontallive/mcp-server-python-template)** - ⭐ 17
   This template provides a streamlined foundation for building Model Context Protocol (MCP) servers in Python. It's designed to make AI-assisted development of MCP tools easier and more efficient.

4189. **[mcp-ecosystem](https://github.com/SynkraAI/mcp-ecosystem)** - ⭐ 17
   MCP Ecosystem: Docker MCP Toolkit, IDE Configs & Presets for AIOS

4190. **[jiki](https://github.com/teilomillet/jiki)** - ⭐ 17

4191. **[context-engineering](https://github.com/timothywarner-org/context-engineering)** - ⭐ 17
   🧠 Stop building AI that forgets. Master MCP (Model Context Protocol) with production-ready semantic memory, hybrid RAG, and the WARNERCO Schematica teaching app. FastMCP + LangGraph + Vector/Graph stores. Your AI assistant's long-term memory starts here.

4192. **[mcp-graphql-forge](https://github.com/toolprint/mcp-graphql-forge)** - ⭐ 17
   MCP that can proxy any GraphQL API and expose graphql operations as mcp tools.

4193. **[deep-research](https://github.com/troyhantech/deep-research)** - ⭐ 17
   A minimalist deep research framework for any OpenAI API compatible LLMs.

4194. **[docmole](https://github.com/Vigtu/docmole)** - ⭐ 17
   Dig through any documentation with AI - MCP server for Claude, Cursor, and other AI assistants

4195. **[arxiv-mcp-server](https://github.com/1Dark134/arxiv-mcp-server)** - ⭐ 16
   arXiv MCP Server Client 🐙 enables AI assistants to search, retrieve, analyze, and summarize arXiv papers with features like author/category browsing, trends, and citation insights.

4196. **[drf-mcp-docs](https://github.com/Abdulkhalek-1/drf-mcp-docs)** - ⭐ 16
   API documentation via MCP for AI coding agents

4197. **[mcp-client-cli](https://github.com/addity3/mcp-client-cli)** - ⭐ 16
   cli-based program to run llm prompt and mcp

4198. **[mcp-salesforce](https://github.com/AiondaDotCom/mcp-salesforce)** - ⭐ 16
   🚀 Complete MCP (Model Context Protocol) server for Salesforce integration with Claude Desktop. Provides seamless OAuth authentication, universal CRUD operations on any Salesforce object.

4199. **[vite-plugin-mcp-client-tools](https://github.com/atesgoral/vite-plugin-mcp-client-tools)** - ⭐ 16
   Pluggable Vite MCP plugin that brings client-side tools to your existing Vite setup

4200. **[sample-multi-tenant-saas-mcp-server](https://github.com/aws-samples/sample-multi-tenant-saas-mcp-server)** - ⭐ 16
   Multi-Tenant remote MCP server with Amazon Cognito and remote client with Amazon Bedrock hosted on AWS

4201. **[mcp-progressive-agentskill](https://github.com/cablate/mcp-progressive-agentskill)** - ⭐ 16
   AgentSkill - Progressive MCP client with three-layer lazy loading. Validates AgentSkills.io pattern for efficient token usage.

4202. **[reporelay](https://github.com/chwoerz/reporelay)** - ⭐ 16
   A self-hosted code context engine for MCP.

4203. **[oneshot](https://github.com/Destiner/oneshot)** - ⭐ 16
   Anthropic MCP client for macOS

4204. **[aica](https://github.com/dotneet/aica)** - ⭐ 16
   aica(AI Code Analyzer) reviews your code using AI. Supports CLI and GitHub Actions.

4205. **[go-mcp](https://github.com/dstotijn/go-mcp)** - ⭐ 16
   Go library for implementing the Model Context Protocol (MCP).

4206. **[ux-mcp-server](https://github.com/elsahafy/ux-mcp-server)** - ⭐ 16
   MCP server providing 28 UX knowledge resources, 23 analysis tools & 4 workflow prompts. Works with Claude, Cursor, Continue.dev, Cline, Zed & any MCP client. WCAG, Nielsen heuristics, design systems, e-commerce, PWA, AI/ML & more.

4207. **[openapi-to-mcp](https://github.com/EvilFreelancer/openapi-to-mcp)** - ⭐ 16
   Turns any OpenAPI/Swagger API into an MCP server. One MCP tool per endpoint, Streamable HTTP - for AI clients calling your REST API.

4208. **[create-mcp](https://github.com/fefergrgrgrg/create-mcp)** - ⭐ 16
   CLI to set up and deploy MCP Servers to Cloudflare Workers in seconds. Just write TypeScript functions to make Cursor MCP tools.

4209. **[protocols-io-mcp-server](https://github.com/hqn21/protocols-io-mcp-server)** - ⭐ 16
   An MCP server that enables MCP clients like Claude Desktop to interact with data from protocols.io.

4210. **[Ai-doctor](https://github.com/Jevon-Zhong/Ai-doctor)** - ⭐ 16
   🧑‍⚕️ Ai智能医生聊天助手-这是一个前端基于Vue3、TS、后端基于Nest.js、MongoDB、Redis、Milvus并结合大模型、RAG等技术实现的医疗库智能问答系统，能结合大模型的生成能力和上传的专业医疗领域知识库针对提问给出专业回答。同时具备工具调用能力，可使用MCP集成网页爬取能力让大模型根据网址对应的医疗领域文章进行分析和输出。

4211. **[mcp-installer](https://github.com/joobisb/mcp-installer)** - ⭐ 16
   Simplifies the installation and management of MCP (Model Context Protocol) servers across different AI clients.

4212. **[mcp-jest](https://github.com/josharsh/mcp-jest)** - ⭐ 16
   Automated testing for Model Context Protocol servers. Ship MCP Servers with confidence.

4213. **[mcpdog](https://github.com/kinhunt/mcpdog)** - ⭐ 16
   🐕 Universal MCP Server Manager - Configure once, manage multiple MCP servers through a single interface. Perfect for Claude   Desktop, Claude Code, Cursor, Gemini CLI & AI assistants. Web dashboard, auto-detection, unified proxy layer.

4214. **[MCP-Analyzer](https://github.com/klara-research/MCP-Analyzer)** - ⭐ 16
   An MCP server to read MCP logs to debug directly inside the client

4215. **[mcp-client-gen](https://github.com/kriasoft/mcp-client-gen)** - ⭐ 16
   Turn any MCP server into a type-safe TypeScript SDK in seconds - with    OAuth 2.1 and multi-provider support

4216. **[pentest-mcp-server](https://github.com/LayeSec006/pentest-mcp-server)** - ⭐ 16
   MCP server for penetration testing

4217. **[webmcp-react](https://github.com/MCPCat/webmcp-react)** - ⭐ 16
   React hooks for exposing your app's functionality as WebMCP tools - transport-agnostic, SSR-safe, Strict Mode safe, W3C spec-aligned

4218. **[EasyMCP](https://github.com/mshojaei77/EasyMCP)** - ⭐ 16
   A beginner-friendly client for the MCP (Model Context Protocol). Connect to SSE, NPX, and UV servers, and integrate with OpenAI for dynamic tool interactions. Perfect for exploring server connections and chat enhancements.

4219. **[appvector-mcp](https://github.com/Multivariate-AI-Inc/appvector-mcp)** - ⭐ 16
   This MCP server provides programmatic access to AppVector's powerful APIs, enabling you to integrate ASO insights directly into your development and marketing workflows through any MCP Client

4220. **[mcp-server-unitycatalog](https://github.com/ognis1205/mcp-server-unitycatalog)** - ⭐ 16
   Unity Catalog AI Model Context Protocol Server

4221. **[QCX](https://github.com/QueueLab/QCX)** - ⭐ 16
   Language to Maps

4222. **[lite-mcp-client](https://github.com/sligter/lite-mcp-client)** - ⭐ 16
   Lite-MCP-Client是一个基于命令行的轻量级MCP客户端工具

4223. **[LSP4J-MCP](https://github.com/stephanj/LSP4J-MCP)** - ⭐ 16
   A Java MCP (Model Context Protocol) server that wraps JDTLS (Eclipse JDT Language Server) using LSP4J to provide Java IDE features to AI assistants like Claude.

4224. **[puppeteer-mcp-server](https://github.com/sultannaufal/puppeteer-mcp-server)** - ⭐ 16
   Self-hosted Puppeteer MCP server with remote SSE access, API key authentication, and Docker deployment. Complete tool suite for browser automation via Model Context Protocol.

4225. **[SchemaPin](https://github.com/ThirdKeyAI/SchemaPin)** - ⭐ 16
   The SchemaPin protocol for cryptographically signing and verifying AI agent tool schemas to prevent supply-chain attacks.

4226. **[claude-mcp-scheduler](https://github.com/tonybentley/claude-mcp-scheduler)** - ⭐ 16
   Use Claude API to prompt remote agents on a cron interval but use local MCPs to handle tool calls for context

4227. **[google-mcp](https://github.com/vakharwalad23/google-mcp)** - ⭐ 16
   Collection of Google-native tools (e.g., Gmail, Calendar) for the MCP

4228. **[shodan-mcp](https://github.com/Vorota-ai/shodan-mcp)** - ⭐ 16
   Shodan MCP server for Claude, Cursor & VS Code. 20 tools for passive reconnaissance, CVE/CPE intelligence, DNS analysis, and device search. 4 tools work free without an API key. OSINT and vulnerability research from your IDE.

4229. **[claude-vigil-mcp](https://github.com/Vvkmnn/claude-vigil-mcp)** - ⭐ 16
   🏺 An MCP server for checkpointing and file recovery in Claude Code

4230. **[grok-faf-mcp](https://github.com/Wolfe-Jam/grok-faf-mcp)** - ⭐ 16
   MCP server for xAI Grok — read and serve .faf project context. npm: grok-faf-mcp

4231. **[outlook-mcp](https://github.com/XenoXilus/outlook-mcp)** - ⭐ 16
   MCP server for Microsoft Office 365 Outlook – email, calendar & SharePoint integration for Claude, ChatGPT, and AI assistants via Microsoft Graph API

4232. **[penpot-mcp-server](https://github.com/zcube/penpot-mcp-server)** - ⭐ 16
   MCP server for Penpot - Connect AI assistants to Penpot design platform via Model Context Protocol

4233. **[mcp-client-for-weather-example](https://github.com/a-persimmons/mcp-client-for-weather-example)** - ⭐ 15
   一个MCP客户端实践：实现LLM调用天气MCP服务端查询天气的快速示例

4234. **[opentrace](https://github.com/adham90/opentrace)** - ⭐ 15
   Self-hosted observability server with 75+ MCP tools. Ingest logs, connect Postgres, monitor servers — then debug it all from Claude, Cursor, or any MCP client.

4235. **[npm-search-mcp-server](https://github.com/btwiuse/npm-search-mcp-server)** - ⭐ 15
   MCP server for searching npm packages

4236. **[mcp-server](https://github.com/configcat/mcp-server)** - ⭐ 15
   Official ConfigCat Model Context Protocol (MCP) Server

4237. **[salesforce-mcp-lib](https://github.com/Damecek/salesforce-mcp-lib)** - ⭐ 15
   Salesforce MCP Library is a local stdio bridge for Salesforce MCP endpoints using OAuth client credentials, featuring a reusable Apex MCP library and JSON-RPC 2.0 core.

4238. **[claude-server](https://github.com/davidteren/claude-server)** - ⭐ 15
   Claude Server is an MCP implementation that enhances Claude's capabilities by providing sophisticated context management across sessions, enabling persistent knowledge organization through hierarchical project contexts and continuous conversation threads stored in a well-structured ~/.claude directory.

4239. **[mcp-server-subagent](https://github.com/dvcrn/mcp-server-subagent)** - ⭐ 15
   MCP for letting agents delegate tasks to sub-agents (Claude Code, Aider, Q)

4240. **[mcp-server](https://github.com/HarperFast/mcp-server)** - ⭐ 15
   An MCP server providing an interface for MCP clients to access data within Harper.

4241. **[hecate](https://github.com/hecatehq/hecate)** - ⭐ 15
   Hecate is an open-source AI gateway, coding-agent console, and agent-task runtime for routing OpenAI- and Anthropic-compatible traffic across cloud and local models, running external coding agents as supervised local adapters, controlling spend, and running agent work behind policy, approvals, and OpenTelemetry.

4242. **[hive-crypto-mcp](https://github.com/hive-intel/hive-crypto-mcp)** - ⭐ 15
   Hive Intelligence Crypto MCP | The Ultimate Cryptocurrency MCP for AI Assistants - Unified access to crypto, DeFi, and Web3 analytics

4243. **[ultrathink](https://github.com/husniadil/ultrathink)** - ⭐ 15
   MCP server for sequential thinking and complex problem-solving. Built iteratively using itself. Features confidence scoring,   assumption tracking, and multi-session support.

4244. **[django-mcp](https://github.com/hyperb1iss/django-mcp)** - ⭐ 15
    Connect Django apps to AI assistants with Model Context Protocol. Simple decorators expose models, admin functions, and custom tools to Claude and other AI assistants.

4245. **[the-academy](https://github.com/im-knots/the-academy)** - ⭐ 15
   A Socratic dialogue engine for AI agents.

4246. **[cursor-feedback-extension](https://github.com/jianger666/cursor-feedback-extension)** - ⭐ 15
   Save your Cursor monthly quota! Unlimited AI interactions in one conversation via MCP feedback loop.

4247. **[cuba-memorys](https://github.com/LeandroPG19/cuba-memorys)** - ⭐ 15
   🧠 Persistent memory MCP for AI agents — Knowledge graph + Hebbian learning + Anti-hallucination. 12 tools, 1 dependency, zero manual setup.

4248. **[mcp](https://github.com/local-falcon/mcp)** - ⭐ 15
   MCP server for Local Falcon's local SEO and AI visibility platform: geo-grid rank tracking, campaign management, and competitor analysis via Model Context Protocol

4249. **[memoryOSS](https://github.com/memoryOSScom/memoryOSS)** - ⭐ 15
   Persistent long-term memory for AI agents. Local proxy + MCP memory layer for Claude, Codex, and OpenAI-compatible clients.

4250. **[gemma-mcp](https://github.com/monatis/gemma-mcp)** - ⭐ 15
   MCP Client for Gemma-3

4251. **[mcp-tui](https://github.com/msabramo/mcp-tui)** - ⭐ 15
   MCP host app w/ textual user interface, in Python

4252. **[automagik-tools](https://github.com/namastexlabs/automagik-tools)** - ⭐ 15
   From API to AI in 30 Seconds - Transform any API into an intelligent MCP agent that learns, adapts, and speaks human

4253. **[opentargets-mcp](https://github.com/nickzren/opentargets-mcp)** - ⭐ 15
   MCP server for Open Targets Data

4254. **[pinmeto-location-mcp](https://github.com/PinMeTo/pinmeto-location-mcp)** - ⭐ 15
   PinMeTo MCP server that enables users with authorized credentials to unlock their data

4255. **[chatgpt-app-typescript-template](https://github.com/pomerium/chatgpt-app-typescript-template)** - ⭐ 15
   ChatGPT app template using Pomerium, OpenAI Apps SDK and Model Context Protocol (MCP), with a Node.js server and React widgets.

4256. **[bexio-mcp-server](https://github.com/PromptPartner/bexio-mcp-server)** - ⭐ 15
   Complete Swiss accounting integration for Bexio via MCP. Works with Claude Desktop, n8n, and any MCP client. 310 tools for invoices, contacts, projects & more. Created by Lukas Hertig.

4257. **[agent-board](https://github.com/quentintou/agent-board)** - ⭐ 15
   Open-source multi-agent task board for OpenClaw. Kanban + DAG dependencies + MCP server + auto-retry + audit trail. Built for autonomous AI agent teams.

4258. **[django-firebase-mcp](https://github.com/raghavdasila/django-firebase-mcp)** - ⭐ 15
   A production-ready Django app implementing Firebase Model Context Protocol (MCP) server with 14 Firebase tools for AI agents. Features standalone agent, HTTP/stdio transport, LangChain integration, and complete Firebase service coverage (Auth, Firestore, Storage).

4259. **[Convert-Markdown-PDF-MCP](https://github.com/seanivore/Convert-Markdown-PDF-MCP)** - ⭐ 15
   Markdown To PDF Conversion MCP

4260. **[mcp-turso-cloud](https://github.com/spences10/mcp-turso-cloud)** - ⭐ 15
   🗂️ A Model Context Protocol (MCP) server that provides integration with Turso databases for LLMs. This server implements a two-level authentication system to handle both organization-level and database-level operations, making it easy to manage and query Turso databases directly from LLMs.

4261. **[companies-house-mcp](https://github.com/stefanoamorelli/companies-house-mcp)** - ⭐ 15
   🇬🇧🏦 MCP server for UK Companies House API - Search companies, retrieve detailed information, filing history, officers, and charges data through the Model Context Protocol

4262. **[mcp-time](https://github.com/TheoBrigitte/mcp-time)** - ⭐ 15
   MCP (Model Context Protocol) server which provides utilities to work with time and dates, with natural language, multiple formats and timezone convertion capabilities

4263. **[gsd-task-manager](https://github.com/vscarpenter/gsd-task-manager)** - ⭐ 15
   Stop juggling, start finishing. GSD Task Manager makes it easy to sort your to-dos into what’s urgent and what’s important, so you can finally get stuff done without burning out. It’s simple, visual, and works entirely offline.

4264. **[webmcp-sh](https://github.com/WebMCP-org/webmcp-sh)** - ⭐ 15
   A modern web-based Model Context Protocol (MCP) playground for testing and developing MCP servers and clients

4265. **[faf](https://github.com/Wolfe-Jam/faf)** - ⭐ 15
   FAF specification — IANA-registered AI context format (application/vnd.faf+yaml)

4266. **[mcp-bundler](https://github.com/wrtnlabs/mcp-bundler)** - ⭐ 15
   Is the MCP configuration too complicated? You can easily share your own simplified setup!

4267. **[swift-skeleton](https://github.com/1amageek/swift-skeleton)** - ⭐ 14
   Swift source code structural indexer. Extracts type declarations, properties, method signatures, and source locations. MCP server for Claude Code.

4268. **[servicenow-mcp](https://github.com/aartiq/servicenow-mcp)** - ⭐ 14
   Production-ready Model Context Protocol server for ServiceNow platform integration - ITOM, ITSM, CMDB with OAuth, natural language queries, and enterprise security controls

4269. **[llms-txt-generator](https://github.com/aircodelabs/llms-txt-generator)** - ⭐ 14
   The ultimate AI-powered generator for llms.txt and llms-full.txt files.

4270. **[mcp-ipfs](https://github.com/alexbakers/mcp-ipfs)** - ⭐ 14
   🪐 MCP IPFS Server

4271. **[deep-directory-tree-mcp](https://github.com/andredezzy/deep-directory-tree-mcp)** - ⭐ 14
   Powerful Model Context Protocol (MCP) implementation for visualizing directory structures with real-time updates, configurable depth, and smart exclusions for efficient project navigation

4272. **[ex_mcp](https://github.com/azmaveth/ex_mcp)** - ⭐ 14
   Model Context Protocol (MCP) and Agent Client Protocol (ACP) client/server library for Elixir

4273. **[java-xiaohongshu-mcp](https://github.com/bzlrj/java-xiaohongshu-mcp)** - ⭐ 14
   Java 实现的小红书 Model Context Protocol (MCP) 工具服务  为 AI Agent / MCP Client 提供标准化接口，实现： 登录、发图文、发视频、搜索、评论、推荐内容、用户主页 等核心功能

4274. **[ntfy-mcp-server](https://github.com/cyanheads/ntfy-mcp-server)** - ⭐ 14
   An MCP (Model Context Protocol) server designed to interact with the ntfy push notification service. It enables LLMs and AI agents to send notifications to your devices with extensive customization options.

4275. **[MCP-Platform](https://github.com/Data-Everything/MCP-Platform)** - ⭐ 14
   A flexible platform that provides Docker & Kubernetes backends, a lightweight CLI (mcpt), and client utilities for seamless MCP integration. Spin up servers from templates, route requests through a single endpoint with load balancing, and support both deployed (HTTP) and local (stdio) transports — all with sensible defaults and YAML-based configs

4276. **[mcpskills-cli](https://github.com/dhanababum/mcpskills-cli)** - ⭐ 14
   Generate Agent Skills from MCP server tools. Connects via Streamable HTTP, discovers tools, and outputs a skill with schema docs and a call script in the language of your choice.

4277. **[domain-search-mcp](https://github.com/dorukardahan/domain-search-mcp)** - ⭐ 14
   Zero-config domain availability MCP for Claude & ChatGPT. AI suggestions, premium/auction detection via GoDaddy, RDAP/WHOIS fallback. Stdio + HTTP.

4278. **[signoz-mcp-server](https://github.com/DrDroidLab/signoz-mcp-server)** - ⭐ 14
   Connect your Signoz Instance with Cursor, Claude Desktop or any other MCP Compatible Client

4279. **[obsidian-cli-rest](https://github.com/dsebastien/obsidian-cli-rest)** - ⭐ 14
   Control your Obsidian vault programmatically. This plugin turns all Obsidian CLI commands into a local HTTP API and MCP server, letting you automate your workflow from scripts, tools, and AI assistants.

4280. **[mcpterm](https://github.com/dwrtz/mcpterm)** - ⭐ 14
   An MCP tool server that provides stateful, TUI-compatible terminal sessions.

4281. **[systemprompt-mcp-core](https://github.com/Ejb503/systemprompt-mcp-core)** - ⭐ 14
   The core MCP extension for Systemprompt MCP multimodal client

4282. **[phabricator-mcp](https://github.com/freelancer/phabricator-mcp)** - ⭐ 14
   MCP server for Phabricator

4283. **[langgraph-mcp-dataanalysis](https://github.com/gongwon-nayeon/langgraph-mcp-dataanalysis)** - ⭐ 14
   DataAnalysis Agent using LangGraph & MCP server and client

4284. **[mcp-server-gemini-pro](https://github.com/gurveeer/mcp-server-gemini-pro)** - ⭐ 14
   A state-of-the-art Model Context Protocol (MCP) server that provides seamless integration with Google's Gemini AI models. This server enables Claude Desktop and other MCP-compatible clients to leverage the full power of Gemini's advanced AI capabilities.

4285. **[mcp-security-checklist](https://github.com/Helixar-AI/mcp-security-checklist)** - ⭐ 14
   MCP is being adopted rapidly. Security guidance is lagging behind. This checklist gives security engineers, platform teams, and technical leaders a clear, actionable baseline for securing MCP deployments , whether you're shipping an internal tool or a customer-facing AI agent.

4286. **[bookmark-manager-mcp](https://github.com/infinitepi-io/bookmark-manager-mcp)** - ⭐ 14
   A lightweight Model Context Protocol (MCP) server that provides persistent bookmark management for Claude and other MCP-compatible clients. Features categorized storage, resource discovery, and seamless integration with your AI workflow.

4287. **[mcp-safe-run](https://github.com/ithena-one/mcp-safe-run)** - ⭐ 14
   Tired of hardcoding secrets like API keys in your MCP client configuration (e.g., mcp.json, claude_desktop_config.json)? mcp-secure-launcher lets you run your existing MCP servers securely without modifying them.

4288. **[mcp-perplexity-server](https://github.com/joewilsonai/mcp-perplexity-server)** - ⭐ 14
   A Model Context Protocol (MCP) server for intelligent code analysis and debugging using Perplexity AI’s API, seamlessly integrated with the Claude desktop client.

4289. **[mcp-config-editor](https://github.com/kaichen/mcp-config-editor)** - ⭐ 14
   A simple GUI for managing MCP servers, for easy toggle mcp servers.

4290. **[KunAvatar](https://github.com/KunLabAI/KunAvatar)** - ⭐ 14
   基于ollama推理框架本地部署的Agent应用，实现MCP工具调用，短长期记忆等功能。||  A locally deployed agent application built on the Ollama, featuring MCP tool integration along with both short-term and long-term memory support.

4291. **[XcodeMCPKit](https://github.com/lynnswap/XcodeMCPKit)** - ⭐ 14
   Xcode MCP proxy with multi-client sessions

4292. **[webfetch-mcp](https://github.com/manooll/webfetch-mcp)** - ⭐ 14
   Live Web Access for Your Local AI — Tunable Search & Clean Content Extraction

4293. **[SRE-agent](https://github.com/martinimarcello00/SRE-agent)** - ⭐ 14
   Autonomous agent for Kubernetes incident detection, diagnosis, and mitigation using LLMs and modular workflows. Integrates LangChain, LangGraph, and MCP servers to enable automated SRE tasks in cloud-native environments.

4294. **[WAIaaS](https://github.com/minhoyoo-iotrust/WAIaaS)** - ⭐ 14
   Wallet-as-a-Service for all AI agents in the world

4295. **[memory-visualizer](https://github.com/mjherich/memory-visualizer)** - ⭐ 14
   Interactive visualizer for Anthropic's Memory MCP knowledge graphs. Instantly explore, debug, and analyze entities, relations, and observations from memory.json files in the Model Context Protocol.

4296. **[work-memory-mcp](https://github.com/moontmsai/work-memory-mcp)** - ⭐ 14
   Never lose context again - persistent memory management system for AI-powered workflows across multiple tools

4297. **[x402-deploy](https://github.com/nirholas/x402-deploy)** - ⭐ 14
   Turn any API or MCP server into a paid service with x402

4298. **[llm-sse-mcp-demo-2025](https://github.com/nlinhvu/llm-sse-mcp-demo-2025)** - ⭐ 14
   This project demonstrates the integration between LLM clients and MCP (Model Context Protocol) servers using Server-Sent Events (SSE) for real-time communication.

4299. **[openalex-research-mcp](https://github.com/oksure/openalex-research-mcp)** - ⭐ 14
   MCP server for the OpenAlex API — search 240M+ scholarly works, analyze citations, track research trends, and map collaboration networks

4300. **[ckan-mcp-server](https://github.com/ondics/ckan-mcp-server)** - ⭐ 14
   A Model Context Protocol (MCP) server for the CKAN API that enables browsing and managing CKAN data portals through MCP-compatible clients.

4301. **[dav-mcp](https://github.com/PhilflowIO/dav-mcp)** - ⭐ 14
   Transform AI agents into orchestrating assistants managing calendars, contacts, and tasks

4302. **[mcp-perplexity-server](https://github.com/PoliTwit1984/mcp-perplexity-server)** - ⭐ 14
   A Model Context Protocol (MCP) server for intelligent code analysis and debugging using Perplexity AI’s API, seamlessly integrated with the Claude desktop client.

4303. **[jadx-mcp-server](https://github.com/Qtty/jadx-mcp-server)** - ⭐ 14
   A Pure-Java MCP Server for JaDX Android Reverse Engineering Tool

4304. **[MCPScan](https://github.com/sahiloj/MCPScan)** - ⭐ 14
   Offensive MCP server auditor — detects tool poisoning, credential leaks, RCE vectors, SSRF, session hijacking, and supply chain vulnerabilities across stdio, HTTP, and SSE transports.

4305. **[toolhive-registry-server](https://github.com/stacklok/toolhive-registry-server)** - ⭐ 14
   An API server that implements the official MCP Registry API, providing standardised access to MCP servers from multiple backends, including file-based and other API-compliant registries.

4306. **[ai-mate](https://github.com/symfony/ai-mate)** - ⭐ 14
   AI development assistant MCP server for Symfony projects

4307. **[mcp-client-compatibility](https://github.com/tadata-org/mcp-client-compatibility)** - ⭐ 14

4308. **[mcphawk](https://github.com/tech4242/mcphawk)** - ⭐ 14
   MCPHawk is a new Logging & Monitoring solution for Model Context Protocol (MCP) traffic, providing deep visibility into MCP client-server interactions. It started off as a mix between Wireshark and mcpinspector, purpose-built for the MCP ecosystem, and is now slowly turning into something more.

4309. **[vmware-esxi-mcp](https://github.com/uldyssian-sh/vmware-esxi-mcp)** - ⭐ 14
   Professional Model Context Protocol (MCP) server for VMware ESXi hypervisor management. Enterprise-ready solution with secure interfaces for ESXi operations, VM lifecycle management, and infrastructure monitoring.

4310. **[google-mcp-remote](https://github.com/vakharwalad23/google-mcp-remote)** - ⭐ 14
   Collection of Google-native tools (e.g., Gmail, Calendar) for the MCP

4311. **[mcp-toggl](https://github.com/verygoodplugins/mcp-toggl)** - ⭐ 14
   MCP server for Toggl Track integration with intelligent caching and reporting tools

4312. **[claude-praetorian-mcp](https://github.com/Vvkmnn/claude-praetorian-mcp)** - ⭐ 14
   ⚜️ An MCP server for context compaction and recycling in Claude Code

4313. **[dx-toolkit](https://github.com/youdotcom-oss/dx-toolkit)** - ⭐ 14
   Open-source toolkit enabling developers to integrate You.com's AI capabilities into their workflows

4314. **[mongo-mcp](https://github.com/1RB/mongo-mcp)** - ⭐ 13
   MCP server that provide tools to LLMs such as claude in cursor to interact with MongoDB

4315. **[owl-mcp](https://github.com/ai4curation/owl-mcp)** - ⭐ 13
   MCP server for OWL applications

4316. **[vault-sync](https://github.com/alexjbarnes/vault-sync)** - ⭐ 13
   Headless Obsidian Sync client with MCP server for AI assistants

4317. **[mcp-server-template](https://github.com/BearHuddleston/mcp-server-template)** - ⭐ 13
   Spec-driven Go MCP server template for building domain MCPs with AI-agent onboarding.

4318. **[llamacppMCPClientDemo](https://github.com/brucepro/llamacppMCPClientDemo)** - ⭐ 13
   standalone react MCP client using SSE

4319. **[nest-mcp](https://github.com/btwld/nest-mcp)** - ⭐ 13
   Build Model Context Protocol (MCP) servers, clients, and gateways using the NestJS ecosystem you already know.

4320. **[sherpa](https://github.com/CartographAI/sherpa)** - ⭐ 13
   Chat with any codebase with MCP servers in a single command

4321. **[mcp-chat-client](https://github.com/Ceeon/mcp-chat-client)** - ⭐ 13
   基于高德地图MCP服务的聊天客户端

4322. **[RAG-MCP](https://github.com/cr21/RAG-MCP)** - ⭐ 13
   Simple RAG implementation from scratch using MCP, focusing on Perception, Memory, Decision and Action

4323. **[mcp-test-client](https://github.com/crazyrabbitLTC/mcp-test-client)** - ⭐ 13
   MCP Test Client is a TypeScript testing utility for Model Context Protocol (MCP) servers.

4324. **[easy-mcp-use](https://github.com/dforel/easy-mcp-use)** - ⭐ 13
   Easy-MCP-Use is the open source TypeScript library to connect any LLM to any MCP server and build custom agents that have tool access, without using closed source or application clients.

4325. **[Rube](https://github.com/dorucioclea/Rube)** - ⭐ 13
   Rube is a Model Context Protocol (MCP) server that connects your AI tools to 500+ apps like Gmail, Slack, GitHub, and Notion. Simply install it in your AI client, authenticate once with your apps, and start asking your AI to perform real actions like "Send an email" or "Create a task."

4326. **[pentest-mcp-server](https://github.com/exjskdjsdfks/pentest-mcp-server)** - ⭐ 13
   ⚙️ Enable AI agents to conduct autonomous penetration testing on any Linux distribution with a persistent and robust Model Context Protocol server.

4327. **[spring-ai-mcp-deepseek](https://github.com/firefly0512/spring-ai-mcp-deepseek)** - ⭐ 13
   使用 Spring AI 整合 MCP 服务，包括 MCP server 和 deepseek client

4328. **[mcp-delphi](https://github.com/flydev-fr/mcp-delphi)** - ⭐ 13
   Delphi and Lazarus/FPC MCP server: build/clean pascal projects via MCP tools.

4329. **[mcp-web-search-tool](https://github.com/gabrimatic/mcp-web-search-tool)** - ⭐ 13
   A MCP server providing real-time web search capabilities to any AI model.

4330. **[DevoChat](https://github.com/gws8820/DevoChat)** - ⭐ 13
   Unified Web AI Chat UI & MCP Client

4331. **[pentesting-cyber-mcp](https://github.com/hackersatyamrastogi/pentesting-cyber-mcp)** - ⭐ 13
   🔐 50+ MCP Security Servers for AI-Powered Pentesting | Integrate Nmap, Burp Suite, Nuclei, Shodan, BloodHound, Semgrep, Trivy | Model Context Protocol for Cybersecurity

4332. **[mcp-client-langchain-ts](https://github.com/hideya/mcp-client-langchain-ts)** - ⭐ 13
   Simple MCP Client CLI Implementation Using LangChain ReAct Agent / TypeScript

4333. **[mcp-server-weather-js](https://github.com/hideya/mcp-server-weather-js)** - ⭐ 13
   Simple Weather MCP Server Example

4334. **[prompt-engineer-mcp-server](https://github.com/hireshBrem/prompt-engineer-mcp-server)** - ⭐ 13
   Write 10x better prompts using Prompt Engineer MCP server.

4335. **[lm](https://github.com/houtini-ai/lm)** - ⭐ 13
   Offload Tasks from Claude to your Local LLM With Houtini-LM - uses OpenAPI for LM Studio and Ollama Compatibility. Save tokens by offloading some grunt work for your API - our tool description helps claude decide what work to assign and why.

4336. **[memory-mcp-server](https://github.com/hpkv-io/memory-mcp-server)** - ⭐ 13
   A MCP (Model Context Protocol) server providing long-term memory for LLMs

4337. **[Tinvo](https://github.com/imxcstar/Tinvo)** - ⭐ 13
   LLM AI Client based on Blazor. (openai, chatgpt, llama, ollama, onnx, deepseekr1...)

4338. **[istek](https://github.com/istekapp/istek)** - ⭐ 13
   The API client built for AI agents. HTTP, GraphQL, gRPC, WebSocket, MQTT + MCP."

4339. **[devtap](https://github.com/killme2008/devtap)** - ⭐ 13
   Bridge build/dev process output to AI coding sessions via MCP — supports Claude Code, Codex, OpenCode, Gemini CLI, and aider

4340. **[cie](https://github.com/kraklabs/cie)** - ⭐ 13
   Code Intelligence Engine — indexes your codebase and gives AI assistants deep understanding via MCP (semantic search, call graphs, 20+ tools)

4341. **[llama-nexus](https://github.com/LlamaEdge/llama-nexus)** - ⭐ 13
   A gateway service designed to manage and orchestrate OpenAI-compatible API servers with MCP support.

4342. **[sift-gateway](https://github.com/lourencomaciel/sift-gateway)** - ⭐ 13
   Reliability gateway for AI tool output: schema-stable, secret-safe, pagination-complete JSON for MCP and CLI agents.

4343. **[locus](https://github.com/Magnifico4625/locus)** - ⭐ 13
   Persistent project-aware memory for AI coding tools. Built on MCP. Works with Codex, Claude Code, and other MCP-compatible clients.

4344. **[openalgo-mcp](https://github.com/marketcalls/openalgo-mcp)** - ⭐ 13
   Documentation

4345. **[claude-qdrant-mcp](https://github.com/marlian/claude-qdrant-mcp)** - ⭐ 13
   Local-first TypeScript MCP server for Qdrant with client isolation, LM Studio integration, and scalable document workflows.

4346. **[claude-tools-mcp](https://github.com/mathematic-inc/claude-tools-mcp)** - ⭐ 13
   MCP server that exposes Claude Code's file and shell tools (bash, read, write, edit, glob, grep) over HTTP for remote use by any MCP client

4347. **[inspector](https://github.com/mcp-use/inspector)** - ⭐ 13
   Modern MCP Inspector for remote mcp servers with support for Apps SDK

4348. **[magento-coding-standard-mcp](https://github.com/Midhun-edv/magento-coding-standard-mcp)** - ⭐ 13
   MCP server that teaches AI assistants Magento 2 coding standards — validate code, look up correct patterns, check security, and apply theme-specific rules (Hyva, Luma, Breeze, Porto). Works with Claude, Cursor, Gemini CLI, VS Code Copilot, and any MCP-compatible client.

4349. **[mcpup](https://github.com/mohammedsamin/mcpup)** - ⭐ 13
   MCP configuration manager — enable, disable, and sync MCP servers across AI clients from one place

4350. **[agent-hub](https://github.com/nathangtg/agent-hub)** - ⭐ 13
   Agent Hub is an AI orchestration platform that transforms how developers and DevOps engineers interact with their toolchain. Built on the cutting-edge Model Context Protocol (MCP), it provides intelligent automation through specialized AI agents, seamlessly integrating with GitHub, Azure, security tools, and data processing

4351. **[mcp-meme-sticky](https://github.com/nkapila6/mcp-meme-sticky)** - ⭐ 13
   Create AI generated memes using MCP Meme Sticky. Can converted generated memes into stickers for Telegram or WhatsApp (WA coming soon).  ✨ no APIs required ✨.

4352. **[SQL_MCP_Server](https://github.com/pawankumar94/SQL_MCP_Server)** - ⭐ 13
   SQLGenius is an AI-powered SQL assistant that converts natural language to SQL queries using Vertex AI's Gemini Pro. Built with MCP and Streamlit, it provides an intuitive interface for BigQuery data exploration with real-time visualization and schema management.

4353. **[credit-optimizer-v5](https://github.com/rafsilva85/credit-optimizer-v5)** - ⭐ 13
   Credit Optimizer v5 for Manus AI - Save 30-75% on credits. Free MCP Server (PyPI) + $9 Manus Skill. Audited across 53 scenarios. Zero quality loss.

4354. **[mcp-client-laravel](https://github.com/RedberryProducts/mcp-client-laravel)** - ⭐ 13
   Laravel-native client for Model Context Protocol (MCP) servers. Built by Redberry (Diamond-tier Laravel partner). Used by LarAgent and other frameworks to enable AI agent functionality.

4355. **[codepilot](https://github.com/rohittcodes/codepilot)** - ⭐ 13
   A multi-agent CLI tool powered by Swarms-rs and Composio

4356. **[league-client-mcp](https://github.com/rumi-chan/league-client-mcp)** - ⭐ 13
   Connect Claude, Antigravity to League Client via MCP & Pengu Loader.

4357. **[mcp-auth-helper](https://github.com/sdaoudi/mcp-auth-helper)** - ⭐ 13
   Standalone OAuth helper for MCP servers with client allowlists (Figma, etc.) - works with OpenCode without forking

4358. **[vector_mcp](https://github.com/sergiobayona/vector_mcp)** - ⭐ 13
   A server implementation for the Model Context Protocol (MCP) in Ruby.

4359. **[GitLab-CICD-Agent](https://github.com/shalwin04/GitLab-CICD-Agent)** - ⭐ 13
   agentic-cicd is an AI-powered multi-agent system that automates GitLab CI/CD workflows using natural language. Built with LangGraphJS, it connects to GitLab via OAuth, interprets user intent, generates pipelines, and executes deployments — all orchestrated by autonomous AI agents and backed by a GitLab MCP server.

4360. **[obsidian-mcp-server](https://github.com/smith-and-web/obsidian-mcp-server)** - ⭐ 13
   MCP server for Obsidian vault management - enables Claude and other AI assistants to read, write, search, and organize your notes

4361. **[openwebui-mcp-setup](https://github.com/sonzentherevolution/openwebui-mcp-setup)** - ⭐ 13
    Universal MCPO/MCP bridge for Open Web UI with AI-powered configuration. Automated setup generation, Docker support, beginner-friendly. Any AI assistant can instantly convert MCP configs to   working Open Web UI integrations.

4362. **[AgentStack](https://github.com/ssdeanx/AgentStack)** - ⭐ 13
   AgentStack is a production-grade multi-agent framework built on Mastra, delivering 50+ enterprise tools, 25+ specialized agents, and A2A/MCP orchestration for scalable AI systems. Focuses on financial intelligence, RAG pipelines, observability, and secure governance.

4363. **[taiga-ui-mcp](https://github.com/taiga-family/taiga-ui-mcp)** - ⭐ 13
   Taiga UI MCP server providing documentation search and scaffolding tools.

4364. **[temple-bridge](https://github.com/templetwo/temple-bridge)** - ⭐ 13
   The Sovereign Stack: MCP server binding local AI capabilities with governance protocols. 100% local operation with memory, conscience, and recursive observation.

4365. **[mcp-more](https://github.com/toosean/mcp-more)** - ⭐ 13
   A modern desktop application for managing Model Context Protocol (MCP) servers.

4366. **[mcp_review_code_tool](https://github.com/wenkil/mcp_review_code_tool)** - ⭐ 13
   A code review tool based on Model Context Protocol (MCP) that leverages OpenAI's capabilities for intelligent code analysis and review. | 基于模型上下文协议(MCP)的代码审查工具，利用OpenAI的能力进行智能代码分析和审查。

4367. **[claude-faf-mcp](https://github.com/Wolfe-Jam/claude-faf-mcp)** - ⭐ 13
   Anthropic MCP server for .faf — 33 tools, IANA-registered format. npm: claude-faf-mcp. MCP Registry #2759

4368. **[n8n-coolify-mcp-tools](https://github.com/wrediam/n8n-coolify-mcp-tools)** - ⭐ 13
   This workflow leverages the Community n8n MCP Client and my new Coolify MCP Server to interact with your Coolify infrastructure using MCP (Model Context Protocol).

4369. **[MCPGateway](https://github.com/abdullah1854/MCPGateway)** - ⭐ 12
   Open-source MCP server — progressive tool discovery, code execution, intelligent routing & token optimization across 50+ tools

4370. **[asap-protocol](https://github.com/adriannoes/asap-protocol)** - ⭐ 12
   Standard protocol for agent-to-agent communication with stateful orchestration, MCP-compatible and a public marketplace to discover and register agents.

4371. **[actual-mcp-server](https://github.com/agigante80/actual-mcp-server)** - ⭐ 12
   Docker MCP server connecting MCP clients (tested with LibreChat/LobeChat) to Actual Budget for natural-language budgeting, transaction management, and financial insights.

4372. **[mcp-chat-widget](https://github.com/aimdoc-ai/mcp-chat-widget)** - ⭐ 12
   Configure, host and embed MCP-enabled chat widgets for your website or product. Lightweight and extensible Chatbase clone to remotely configure and embed your agents anywhere.

4373. **[openclaw-mcp-bridge](https://github.com/AIWerk/openclaw-mcp-bridge)** - ⭐ 12
   OpenClaw MCP Client Plugin - bridges MCP servers into OpenClaw via registerTool

4374. **[mcp-interactive-terminal](https://github.com/amol21p/mcp-interactive-terminal)** - ⭐ 12
   MCP server that gives AI agents (Claude Code, Cursor, Windsurf) real interactive terminal sessions — REPLs, SSH, databases, Docker, and any interactive CLI with clean output and smart completion detection

4375. **[agent-identity-protocol](https://github.com/ArangoGutierrez/agent-identity-protocol)** - ⭐ 12
   Agent Identity Protocol - Zero-trust security layer for AI agents. Policy enforcement proxy for MCP with Human-in-the-Loop approval, DLP scanning, and audit logging.

4376. **[jenkins-mcp-server](https://github.com/AshwiniGhuge3012/jenkins-mcp-server)** - ⭐ 12
   An MCP server for interacting with a Jenkins server. Allows you to trigger jobs, check build statuses, and manage your Jenkins instance through MCP.

4377. **[mcp-server-webscan](https://github.com/bsmi021/mcp-server-webscan)** - ⭐ 12
   A Model Context Protocol (MCP) server for web content scanning and analysis. This server provides tools for fetching, analyzing, and extracting information from web pages.

4378. **[MIST](https://github.com/CLoaKY233/MIST)** - ⭐ 12
   MCP server empowering AI assistants with real-world capabilities: Gmail, Calendar, Tasks, Git integration, and note management. Bridges AI assistants to external services through standardized protocol with secure authentication.

4379. **[xcf](https://github.com/CodeFreezeAI/xcf)** - ⭐ 12
   Xcode MCP Server xcf is a 100% Swift based allowing you to integrate Xcode with your favorite AI IDE or MCP Client

4380. **[mcp_client_rust](https://github.com/darinkishore/mcp_client_rust)** - ⭐ 12

4381. **[wamcp](https://github.com/delltrak/wamcp)** - ⭐ 12
   WhatsApp MCP Server — Connect AI agents to WhatsApp via Model Context Protocol. 61 tools, 10 resources, 12 real-time events. Supports Baileys (WhatsApp Web) and Cloud API. Built with TypeScript, BullMQ, and Docker.

4382. **[guildbridge](https://github.com/dend/guildbridge)** - ⭐ 12
   🏰 Remotely hosted MCP server for Discord

4383. **[st_rag_mcp](https://github.com/digital-duck/st_rag_mcp)** - ⭐ 12
   MCP streamlit client with RAG support for tool search

4384. **[snowflake-mcp-server](https://github.com/dynamike/snowflake-mcp-server)** - ⭐ 12
   MCP Server for connecting to Snowflake with read-only questions

4385. **[_b00t_](https://github.com/elasticdotventures/_b00t_)** - ⭐ 12
   🥾 _b00t_:  state of the art agentic harness tooling & dynamic context initialization

4386. **[create-mcp-server-kit](https://github.com/Epi-1120/create-mcp-server-kit)** - ⭐ 12
   Scaffold a production-ready Model Context Protocol (MCP) server in seconds.

4387. **[cv-resume-builder-mcp](https://github.com/eyaab/cv-resume-builder-mcp)** - ⭐ 12
   AI-powered CV and resume builder using Model Context Protocol. Automatically sync your achievements from Jira, Credly, LinkedIn, and git. Keep your CV always up-to-date.

4388. **[openclaw-mcp-server](https://github.com/Helms-AI/openclaw-mcp-server)** - ⭐ 12
   MCP server exposing OpenClaw Gateway tools to Claude Code and other MCP-compatible clients

4389. **[Hoofy](https://github.com/HendryAvila/Hoofy)** - ⭐ 12
   Hoofy — AI development companion MCP server. Persistent memory, spec-driven development, adaptive change pipeline, Clarity Gate. 32 tools, single Go binary, zero deps.

4390. **[langchain-mcp-tools-ts-usage](https://github.com/hideya/langchain-mcp-tools-ts-usage)** - ⭐ 12
   MCP Tools Usage From LangChain ReAct Agent / Example in TypeScript

4391. **[mcp-client-langchain-py](https://github.com/hideya/mcp-client-langchain-py)** - ⭐ 12
   Simple MCP Client CLI Implementation Using LangChain ReAct Agent / Python

4392. **[nodebench-ai](https://github.com/HomenShum/nodebench-ai)** - ⭐ 12
   NodeBench MCP - 260-tool Model Context Protocol server with progressive discovery, agent-as-a-graph embeddings, research optimization, and adaptive web scraping. Monorepo: MCP server + Convex backend + React frontend.

4393. **[mcp-server-manager](https://github.com/infinitimeless/mcp-server-manager)** - ⭐ 12
   A tool to create, build, and manage MCP servers for use with Claude and other MCP clients

4394. **[mcp-for-woocommerce](https://github.com/iOSDevSK/mcp-for-woocommerce)** - ⭐ 12
   WooCommerce MCP Server — WordPress community plugin implementing the Model Context Protocol (MCP) for WooCommerce. Supports STDIO and HTTP streamable transport, with optional JWT authentication. Based on Automattic’s official WordPress MCP.  This plugin is not affiliated with Automattic.

4395. **[mcp-mux](https://github.com/mcpmux/mcp-mux)** - ⭐ 12
   Configure MCP servers once, connect every AI client through a single local gateway

4396. **[claude-context-local](https://github.com/MikeO-AI/claude-context-local)** - ⭐ 12
   🔒 Privacy-first MCP server for Claude using PostgreSQL + Ollama. Local alternative to cloud-based code context with full data sovereignty. No API keys, no external calls, 100% local.

4397. **[porkbun-mcp-server](https://github.com/miraclebakelaser/porkbun-mcp-server)** - ⭐ 12
   MCP server implementation for managing domains, DNS, and SSL via the Porkbun API.

4398. **[ggMCP4VSCode](https://github.com/n2ns/ggMCP4VSCode)** - ⭐ 12
   Google Gemini Model Context Protocol (MCP) Client for VS Code. Connect AI assistants to local context & tools.

4399. **[biomed-agent](https://github.com/nickzren/biomed-agent)** - ⭐ 12
   Connecting AI agent to biomedical data

4400. **[openagentidentityprotocol](https://github.com/openagentidentityprotocol/openagentidentityprotocol)** - ⭐ 12
   Agent Identity Protocol - Zero-trust security layer for AI agents. Policy enforcement proxy for MCP with Human-in-the-Loop approval, DLP scanning, and audit logging.

4401. **[Opencollab-mcp](https://github.com/prakhar1605/Opencollab-mcp)** - ⭐ 12
   AI-powered open source contribution matchmaker — finds perfect "good first issues" matched to YOUR skills

4402. **[kiro-powers](https://github.com/praveenc/kiro-powers)** - ⭐ 12
   Repository of custom kiro powers. https://kiro.dev/docs/powers/

4403. **[MCP-Client-Server-for-agents](https://github.com/qmatteoq/MCP-Client-Server-for-agents)** - ⭐ 12
   This project demonstrates a Model Context Protocol (MCP) server and client implementation in .NET

4404. **[robotmcp_client](https://github.com/robotmcp/robotmcp_client)** - ⭐ 12
   Connect AI models like Claude & GPT with robots using MCP and ROS.

4405. **[scorable-mcp](https://github.com/root-signals/scorable-mcp)** - ⭐ 12
   MCP for Scorable Evaluation Platform

4406. **[PackageFlow](https://github.com/runkids/PackageFlow)** - ⭐ 12
   A visual DevOps hub for npm scripts, Git, workflows, and deploy — controllable by AI via MCP.

4407. **[sarvam-mcp-server](https://github.com/Shobhit-Nagpal/sarvam-mcp-server)** - ⭐ 12
   talk to sarvam APIs directly, without code.

4408. **[proxy-base-agent](https://github.com/TheProxyCompany/proxy-base-agent)** - ⭐ 12
   A stateful agent with 100% reliable tool use. Build custom agents on any LLM with guaranteed state consistency.

4409. **[CursorMCPMonitor](https://github.com/willibrandon/CursorMCPMonitor)** - ⭐ 12
   Real-time monitoring tool for Model Context Protocol (MCP) interactions in Cursor AI editor. Track, analyze, and debug AI context exchanges between LLM clients and servers. Supports log rotation, pattern matching, and color-coded event visualization.

4410. **[local-history-mcp](https://github.com/xxczaki/local-history-mcp)** - ⭐ 12
   MCP server for accessing VS Code/Cursor's Local History

4411. **[mcp-trace](https://github.com/zabirauf/mcp-trace)** - ⭐ 12
   A TUI to probe the calls between MCP client and server

4412. **[swift-context-protocol](https://github.com/1amageek/swift-context-protocol)** - ⭐ 11
   swift-context-protocol is a Swift-based implementation of the Model Context Protocol (MCP) for AI contexts. It leverages Swift’s distributed actor model to enable type-safe, asynchronous remote invocation of tools, resources, and prompts.

4413. **[MCP_Client](https://github.com/andrewdeng318/MCP_Client)** - ⭐ 11

4414. **[glm5-mcp](https://github.com/Arkya-AI/glm5-mcp)** - ⭐ 11
   Reduce Claude Desktop consumption by 10x - Integrate Z.ai's GLM-5 (744B params) with Claude via MCP for intelligent task delegation

4415. **[mcp-shopline](https://github.com/asgard-ai-platform/mcp-shopline)** - ⭐ 11
   MCP server wrapping the Shopline Open API into 143 AI-callable tools (75 read + 68 write) for e-commerce operations. Built for Claude Code, Claude Desktop, and any MCP-compatible AI client.

4416. **[pycentauri](https://github.com/bjan/pycentauri)** - ⭐ 11
   Python client, CLI, and MCP server for the Elegoo Centauri Carbon 3D printer

4417. **[commvault-mcp-server](https://github.com/Commvault/commvault-mcp-server)** - ⭐ 11
   A Model Context Protocol (MCP) server for interacting with Commvault software.

4418. **[french-tax-mcp](https://github.com/cornelcroi/french-tax-mcp)** - ⭐ 11
   MCP server for French tax calculations and information - enables AI assistants to provide accurate French tax guidance

4419. **[mcpkit](https://github.com/cybertheory/mcpkit)** - ⭐ 11
   Easy to use Official MCP Registry Client UI. npx @cybertheory/mcpkit

4420. **[bio-agents-mcp](https://github.com/dogeplusplus/bio-agents-mcp)** - ⭐ 11
   MCP servers for Protein Data Bank, ChemBL, and other life science data (WIP), with Ollama client for local testing.

4421. **[fathom-mcp](https://github.com/Dot-Fun/fathom-mcp)** - ⭐ 11
   Model Context Protocol server for Fathom AI - access meeting recordings, transcripts, summaries, teams, and webhooks

4422. **[auto-mcp-client](https://github.com/down-to-earth1994/auto-mcp-client)** - ⭐ 11
   基于Spring AI 封装了 mcp-client 服务，目的使web网页智能体也能通过 stdio 和 HTTP SSE（Server-Sent Events） 与 MCP Server 进行交互。项目实现了自动化的连接管理机制，包括自动初始化连接、健康检查、超时关闭以及链接复用等功能

4423. **[unity-mcp-template](https://github.com/dunward/unity-mcp-template)** - ⭐ 11
   Simple template project for controlling Unity via MCP

4424. **[springboot-ai-mcp-example](https://github.com/duongminhhieu/springboot-ai-mcp-example)** - ⭐ 11
   Example Spring AI Model Context Protocol (MCP)

4425. **[systemprompt-mcp-gmail](https://github.com/Ejb503/systemprompt-mcp-gmail)** - ⭐ 11
   A specialized Model Context Protocol (MCP) server that enables you to search, read, delete and send emails from your Gmail account, leveraging an AI Agent to help with each operation.  Optimized for Systemprompt MCP Voice client.

4426. **[context-kit](https://github.com/eyalzh/context-kit)** - ⭐ 11
   A CLI tool and MCP client, used to create spec files for AI coding agents with context baked in

4427. **[trebuchet](https://github.com/fuzzball-muck/trebuchet)** - ⭐ 11
   A MUD/MUCK/MUSH chat client with MCP/GUI support.

4428. **[md2confluence-mcp](https://github.com/Gyeom/md2confluence-mcp)** - ⭐ 11
   MCP server to upload Markdown to Confluence. Auto-converts Mermaid diagrams, code blocks, images, and tables.

4429. **[keycloak-mcp](https://github.com/HaithamOumerzoug/keycloak-mcp)** - ⭐ 11
   MCP server that integrates with Keycloak, allowing you to manage Keycloak users and realms through a standardized protocol. It uses the official Keycloak Admin Client to interact with Keycloak's API.

4430. **[GitIntel-MCP-Server](https://github.com/hoangsonww/GitIntel-MCP-Server)** - ⭐ 11
   A Git intelligence MCP server built with Node.js and TypeScript that analyzes local Git repositories to surface insights like hotspots, churn, temporal coupling, knowledge maps, and risk scoring. Designed for AI agents, it exposes repository analytics tools through the Model Context Protocol (MCP) while keeping all data local and read-only.

4431. **[mcp-browser-automation](https://github.com/hrmeetsingh/mcp-browser-automation)** - ⭐ 11
   Model Context Protocol based AI Agent that runs a browser from Claude desktop

4432. **[mcp-boilerplate](https://github.com/iamsrikanthnani/mcp-boilerplate)** - ⭐ 11
   A powerful, production-ready MCP server implementing the Model Context Protocol with robust SSE transport, built-in tools, and comprehensive error handling. Seamlessly connect AI models to data sources with enterprise-grade stability and performance.

4433. **[qurio](https://github.com/irahardianto/qurio)** - ⭐ 11
   Self-hosted RAG engine for AI coding assistants. Ingests technical docs & code repositories locally with structure-aware chunking. Serves grounded context via MCP to prevent hallucinations in software development workflows.

4434. **[druid-mcp-server](https://github.com/iunera/druid-mcp-server)** - ⭐ 11
   A comprehensive Model Context Protocol (MCP) server for Apache Druid that provides extensive tools, resources, and AI-assisted prompts for managing and analyzing Druid clusters. Built with Spring Boot and Spring AI, this server enables seamless integration between AI assistants and Apache Druid through standardized MCP protocol.

4435. **[mcp-coroot](https://github.com/jamesbrink/mcp-coroot)** - ⭐ 11
   MCP server for Coroot observability platform - integrate monitoring, troubleshooting, and configuration tools with AI agents

4436. **[emcp](https://github.com/joeymeere/emcp)** - ⭐ 11
   A framework for building simple MCP servers with custom middleware

4437. **[lol-client-mcp](https://github.com/johnnyinlee/lol-client-mcp)** - ⭐ 11
   League of Legends Game Client API MCP Server

4438. **[oauth-callback](https://github.com/kriasoft/oauth-callback)** - ⭐ 11
   Lightweight OAuth 2.0 authorization code capture for CLI tools & desktop   apps. Works with Node.js, Deno, Bun. MCP SDK ready.

4439. **[mcp-bibliotheque_nationale_de_France](https://github.com/Kryzo/mcp-bibliotheque_nationale_de_France)** - ⭐ 11
   Un serveur MCP (Model-Client-Protocol) pour accéder à l'API Gallica de la Bibliothèque nationale de France (BnF) et générer des rapports de recherche séquentiels.

4440. **[nautobot_mcp](https://github.com/kvncampos/nautobot_mcp)** - ⭐ 11
   Nautobot Model Context Protocol (MCP) Server - Contains STDIO and HTTP Deployments with Embedding Search and RAG.

4441. **[AMS](https://github.com/LastEld/AMS)** - ⭐ 11
   Audit Memory System (AMS): Durable orchestration and memory layer for MCP clients.

4442. **[AIFoundry-MCPConnector-FabricGraphQL](https://github.com/LazaUK/AIFoundry-MCPConnector-FabricGraphQL)** - ⭐ 11
   MCP Client and Server apps to demo integration of Azure OpenAI-based AI agent with a Data Warehouse, exposed through GraphQL in Microsoft Fabric.

4443. **[msty-admin-mcp](https://github.com/M-Pineapple/msty-admin-mcp)** - ⭐ 11
   AI-powered administration for Msty Studio Desktop. 24 MCP tools for database insights, config sync, local model orchestration, and Claude handoff workflows.

4444. **[mcp-server-kintone](https://github.com/macrat/mcp-server-kintone)** - ⭐ 11
   MCP server for kintone

4445. **[mcpHTTPClient](https://github.com/matlab-deep-learning/mcpHTTPClient)** - ⭐ 11
   An MCP client in pure MATLAB code

4446. **[openmessage](https://github.com/MaxGhenis/openmessage)** - ⭐ 11
   Open-source Google Messages client with AI tools (MCP). SMS + RCS from your desktop.

4447. **[chromadb-remote-mcp](https://github.com/meloncafe/chromadb-remote-mcp)** - ⭐ 11
   Remote MCP server for ChromaDB

4448. **[mcp-express-adapter](https://github.com/Moe03/mcp-express-adapter)** - ⭐ 11
   Run multiple MCP clients on a NodeJS Express server (adapter/middleware)

4449. **[polaris](https://github.com/octu0/polaris)** - ⭐ 11
   Distributed AI Agent Framework

4450. **[miro-mcp-server](https://github.com/olgasafonova/miro-mcp-server)** - ⭐ 11
   MCP server for controlling Miro whiteboards with AI assistants

4451. **[openchatwidget](https://github.com/Open-Chat-Widget/openchatwidget)** - ⭐ 11
   AI chat widget in your web app. Supports MCP as a client.

4452. **[nestjs-mcp](https://github.com/orbit-codes/nestjs-mcp)** - ⭐ 11
   An opinionated MCP module for NestJS

4453. **[llmcore](https://github.com/Palm1r/llmcore)** - ⭐ 11
   Qt C++ library for working with AI/LLM Providers and MCP

4454. **[gtm-mcp](https://github.com/pouyanafisi/gtm-mcp)** - ⭐ 11
   MCP server for Google Tag Manager: read tags/triggers/variables, publish containers, and audit changes via Claude/Gemini.

4455. **[prometheus-protocol](https://github.com/prometheus-protocol/prometheus-protocol)** - ⭐ 11
   The trust layer for the open agentic web—giving AI agents a passport, a bank account, and a trusted marketplace to securely interact with the world.

4456. **[semantictool](https://github.com/promptmesh/semantictool)** - ⭐ 11
   tool management service for performing vector tool calling at scale.

4457. **[locust-mcp-server](https://github.com/QAInsights/locust-mcp-server)** - ⭐ 11
   A Model Context Protocol (MCP) server implementation for running Locust load tests. This server enables seamless integration of Locust load testing capabilities with AI-powered development environments.

4458. **[mcp-client-app](https://github.com/RegiByte/mcp-client-app)** - ⭐ 11
   A mcp client chat application built for learning purposes

4459. **[mcpconnect](https://github.com/rocket-connect/mcpconnect)** - ⭐ 11
   Inspect and debug Model Context Protocol servers directly in your browser.

4460. **[simple-nodejs-mcp-client](https://github.com/sawa-zen/simple-nodejs-mcp-client)** - ⭐ 11
   This is a study repository for implementing a Model Context Protocol (MCP) client. It features a simple interactive MCP client implemented in Node.js.

4461. **[alexa-mcp-server](https://github.com/sijan2/alexa-mcp-server)** - ⭐ 11
   amazon alexa mcp server for poke🌴 and other mcp client

4462. **[mcp-optimizer](https://github.com/StacklokLabs/mcp-optimizer)** - ⭐ 11
   MCP server that acts as an intelligent intermediary between AI clients and multiple MCP servers

4463. **[mcp-space](https://github.com/tharuneshwar-s/mcp-space)** - ⭐ 11
   MCP Space is a no-code platform for building and deploying AI tools using the Model Context Protocol (MCP). Create powerful AI agents through an intuitive chat interface without writing code, then deploy with one click to Cloudflare Workers. Combines a Next.js frontend with Google ADK backend for a seamless AI development experience.

4464. **[mcp-oidc-provider](https://github.com/tigrisdata/mcp-oidc-provider)** - ⭐ 11
   Open-sourced mcp-oidc-provider: a minimal, vendor-neutral OIDC layer that sits between MCP clients and your upstream IdP (Auth0/Clerk/Okta).

4465. **[miniflux-mcp](https://github.com/tssujt/miniflux-mcp)** - ⭐ 11
   A Model Context Protocol (MCP) server for interacting with Miniflux RSS reader.

4466. **[streamdeck-mcp](https://github.com/verygoodplugins/streamdeck-mcp)** - ⭐ 11
   MCP server for Elgato Stream Deck control — set buttons, manage pages, wire actions

4467. **[mcp-tradovate](https://github.com/0xjmp/mcp-tradovate)** - ⭐ 10
   MCP server for the Tradovate platform

4468. **[Cognio](https://github.com/0xReLogic/Cognio)** - ⭐ 10
   Persistent semantic memory server for MCP - Give your AI long-term memory that survives across conversations. Lightweight Python server with SQLite storage and semantic search.

4469. **[mini_claude](https://github.com/20alexl/mini_claude)** - ⭐ 10
   Give Claude Code persistent memory across sessions. Track habits, log mistakes, prevent death spirals. Runs locally with Ollama.

4470. **[adonis-mcp](https://github.com/7nohe/adonis-mcp)** - ⭐ 10
   An AdonisJS package for building remote MCP servers

4471. **[openapi-to-mcp](https://github.com/agentic-community/openapi-to-mcp)** - ⭐ 10
   Transform OpenAPI specifications into production-ready MCP servers   with AI-powered evaluation and enhancement. Leverages LLMs to   analyze, improve, and generate Model Context Protocol   implementations from your existing API documentation.

4472. **[AgentX-mcp-servers](https://github.com/AgentX-ai/AgentX-mcp-servers)** - ⭐ 10
   List of open sourced MCP servers. MIT license. Managed by AgentX with love.

4473. **[mcp-wikipedia](https://github.com/algonacci/mcp-wikipedia)** - ⭐ 10
   MCP server to give client the ability to access Wikipedia pages

4474. **[CodeCompass](https://github.com/alvinveroy/CodeCompass)** - ⭐ 10
   CodeCompass: AI-powered Vibe Coding with MCP. Connects Git repositories to AI assistants like Claude, using Ollama for privacy or OpenAI for cloud. Integrates with VSCode, Cursor, and more.

4475. **[emotion_ai](https://github.com/angrysky56/emotion_ai)** - ⭐ 10
   The Aura Emotion AI system has chroma with a local embedding model, memvid qr code mp4 infinite memory, brainwave and neurochemical simulations, sociobiological reasoning, autonomous subsystem processing with a Gemini flash model so the main model is less taxed, is a MCP client with adaptive tool learning and MCP server.

4476. **[Simple_MCP_Client](https://github.com/Avento/Simple_MCP_Client)** - ⭐ 10
   Simple MCP Client for OpenAI/Deepseek R1/V3

4477. **[cheatengine-mcp-bridge](https://github.com/beamstar/cheatengine-mcp-bridge)** - ⭐ 10
   🔗 Connect AI to Cheat Engine for fast memory analysis, enabling quick mods and audits without the tedious manual work.

4478. **[mcp-serverman](https://github.com/benhaotang/mcp-serverman)** - ⭐ 10
   a cli/mcp server tool for managing mcp server json config file with version control, profiles and multi-client support

4479. **[context-engineering-mcp](https://github.com/bralca/context-engineering-mcp)** - ⭐ 10
   Context Engineering is a MCP server that gives AI agents perfect understanding of your codebase. Eliminates context loss, reduces token usage, and generates comprehensive feature plans in minutes. Compatible with Cursor, Claude Code, and VS Code.

4480. **[PsMCP-MCP-Server-for-Photoshop](https://github.com/Chandrahas455/PsMCP-MCP-Server-for-Photoshop)** - ⭐ 10
   An Extensive MCP server and a Gradio MCP client ( with Gemini ) with several tools made using win32com to intereact with Photoshop. Designing with Photoshop has never been more fun!

4481. **[mcp-spring-ai-mcp-client](https://github.com/chaozai0304/mcp-spring-ai-mcp-client)** - ⭐ 10
   使用java实现mcp client了解底层的调用机制，demo示例

4482. **[civitai-mcp-server](https://github.com/Cicatriiz/civitai-mcp-server)** - ⭐ 10
   A Model Context Protocol server for browsing and discovering AI models on Civitai

4483. **[local-voice-mcp](https://github.com/CodeCraftersLLC/local-voice-mcp)** - ⭐ 10
   Give your MCP clients the ability to speak by running local voice models

4484. **[mcp-client](https://github.com/CopilotKit/mcp-client)** - ⭐ 10

4485. **[mcp-reporter](https://github.com/cyanheads/mcp-reporter)** - ⭐ 10
   mcp-reporter is a streamlined utility that generates comprehensive capability reports for Model Context Protocol servers, empowering developers to easily understand available functionality across their MCP servers ecosystem for both documentation and integration into other tools.

4486. **[youtube-mcp-server](https://github.com/dannySubsense/youtube-mcp-server)** - ⭐ 10
   A comprehensive Model Context Protocol (MCP) server providing real-time YouTube Data API access for AI assistants. Features 14 functions including intelligent content evaluation with technology freshness scoring for knowledge base curation.

4487. **[langchain-mcp-client](https://github.com/datalayer/langchain-mcp-client)** - ⭐ 10
   🦜🔗 LangChain Model Context Protocol (MCP) Client

4488. **[simple-mcp-server](https://github.com/dataworkshop/simple-mcp-server)** - ⭐ 10
   Simple MCP Server — Educational Example This repository contains a minimal MCP (Model Context Protocol) server built for educational purposes. Its goal is to help developers understand how the MCP protocol works and how to manage decision-making processes based on model–client communication.

4489. **[ctx-sys](https://github.com/david-franz/ctx-sys)** - ⭐ 10
   Intelligent context management for AI coding assistants. Indexes your codebase with tree-sitter, builds a semantic knowledge graph, and serves 12 tools over MCP. Hybrid RAG combines keyword search, vector embeddings, and graph traversal for precise retrieval. Works with Claude Desktop, Cursor, and any MCP client. Fully local with Ollama.

4490. **[caltrain-mcp](https://github.com/davidyen1124/caltrain-mcp)** - ⭐ 10
   A Model Context Protocol (MCP) server for Caltrain schedules. Get real-time train departures using GTFS data, designed for Claude Desktop and other MCP clients.

4491. **[rec-us-mcp-server](https://github.com/elizabethsiegle/rec-us-mcp-server)** - ⭐ 10
   Book a San Francisco tennis court via MCP server w/ auth

4492. **[mcp-client](https://github.com/EuclideanAI/mcp-client)** - ⭐ 10
   A custom Model Context Protocol (MCP) Client interface with integrated LLM agent chat capabilities built with Next.js and the Vercel AI SDK

4493. **[shellguard](https://github.com/fawdyinc/shellguard)** - ⭐ 10
   MCP server that gives LLM agents read-only shell access over SSH

4494. **[whatsapp-mcp-extended](https://github.com/FelixIsaac/whatsapp-mcp-extended)** - ⭐ 10
   Extended WhatsApp MCP server with 41 tools - reactions, group management, polls, presence, newsletters & more. Fork of lharries/whatsapp-mcp

4495. **[mcp-server](https://github.com/finmap-org/mcp-server)** - ⭐ 10
   The finmap.org MCP server provides comprehensive historical data from the US, UK, Russian and Turkish stock exchanges. Access sectors, tickers, company profiles, market cap, volume, value, and trade counts, as well as treemap and histogram visualizations

4496. **[awesome-mcp](https://github.com/gauravfs-14/awesome-mcp)** - ⭐ 10
   A carefully curated collection of high-quality tools, libraries, research papers, projects, and tutorials centered around Model Context Protocol (MCP) — a novel paradigm designed to enable modular, adaptive coordination between large language models (LLMs) and external tools or data contexts.

4497. **[glasses-mcp](https://github.com/gourraguis/glasses-mcp)** - ⭐ 10
   Glasses MCP is a simple MCP server that lets your AI agent see and capture the web 👓

4498. **[mcp-google-calendar](https://github.com/guinacio/mcp-google-calendar)** - ⭐ 10
   A MCP server that allows Claude and other MCP clients to interact with Google Calendar. This server enables AI assistants to manage your calendar events, check availability, and handle scheduling tasks.

4499. **[team-memory-mcp](https://github.com/gustavolira/team-memory-mcp)** - ⭐ 10
   Shared team memory for AI coding agents. Bayesian confidence scoring with temporal decay. Works with Claude Code, Devin, Cursor, and any MCP-compatible client.

4500. **[aichat](https://github.com/Hayashi-Yudai/aichat)** - ⭐ 10
   A customizable AI chat application powered by Flet.

4501. **[mcp-claude-hackernews](https://github.com/imprvhub/mcp-claude-hackernews)** - ⭐ 10
   An integration that allows Claude Desktop to interact with Hacker News using the Model Context Protocol (MCP).

4502. **[cli](https://github.com/inboxapi/cli)** - ⭐ 10
   🤖 Your Agents' personal email 📧

4503. **[py-mcp-sse](https://github.com/jayliangdl/py-mcp-sse)** - ⭐ 10
   MCP Client 与 MCP Server基于SSE方式的样例实现（Python版本）

4504. **[chessmata](https://github.com/jonradoff/chessmata)** - ⭐ 10
   Chessmata: chess game for humans and AI agents

4505. **[auxilia](https://github.com/keurcien/auxilia)** - ⭐ 10
   A lightweight web MCP client designed to host your MCP-powered AI assistants. auxilia is designed to only support remote MCP servers.

4506. **[ollama-mcp-example](https://github.com/kirillsaidov/ollama-mcp-example)** - ⭐ 10
   Ollama MCP example for dummies.

4507. **[mcp-sys-bridge](https://github.com/leynier/mcp-sys-bridge)** - ⭐ 10
   An implementation of the Model Context Protocol (MCP), acting as a simple bridge to native OS functionalities like clipboard management and URL handling.

4508. **[mcp_client_openai](https://github.com/liangpn/mcp_client_openai)** - ⭐ 10
   适配Openai SDK构建MCP Client

4509. **[laravel-release-changelog-generator](https://github.com/lightszentip/laravel-release-changelog-generator)** - ⭐ 10
   Generate a changelog and releases with version management with artisan

4510. **[world-intel-mcp](https://github.com/marc-shade/world-intel-mcp)** - ⭐ 10
   100+ tool MCP server for real-time global intelligence — markets, FX, bonds, earnings, SEC filings, conflict, military, cyber, climate, news, company enrichment, and 30+ domains. Live Leaflet dashboard with 20 map layers, SSE streaming, and AI situation briefs.

4511. **[mcp-agent-proxy](https://github.com/mashh-lab/mcp-agent-proxy)** - ⭐ 10
   An MCP server that exposes local and remote agents across different servers as MCP tools.

4512. **[ai-assistant-vui](https://github.com/mgoltzsche/ai-assistant-vui)** - ⭐ 10
   Experimental voice user interface (VUI) to interact with an agentic AI assistant

4513. **[cubbi](https://github.com/Monadical-SAS/cubbi)** - ⭐ 10
   Monadical container CLI tool for running sandboxed MCP clients & servers

4514. **[MCP-Penetration-testing](https://github.com/Mr-Infect/MCP-Penetration-testing)** - ⭐ 10
   The ultimate OWASP MCP Top 10 security checklist and pentesting framework for Model Context Protocol (MCP), AI agents, and LLM-powered systems.

4515. **[capacities-mcp-bridge-unofficial](https://github.com/natkitten/capacities-mcp-bridge-unofficial)** - ⭐ 10
   Unofficial MCP tools and bridges for Capacities.io, for use with Claude Desktop, Genspark, and other clients.

4516. **[chatgpt2md](https://github.com/NextStat/chatgpt2md)** - ⭐ 10
   Convert ChatGPT export to Markdown with full-text search and MCP server for Claude

4517. **[dbt-core-mcp](https://github.com/NiclasOlofsson/dbt-core-mcp)** - ⭐ 10
   dbt Core MCP Server: Interact with dbt projects via Model Context Protocol

4518. **[mode-manager-mcp](https://github.com/NiclasOlofsson/mode-manager-mcp)** - ⭐ 10
   MCP Memory Agent Server - A VS Code chatmode and instruction manager with library integration

4519. **[mistral-ai-docs-mcp-server](https://github.com/nikhilbhima/mistral-ai-docs-mcp-server)** - ⭐ 10
   Unofficial MCP server for Mistral AI developer docs and API reference. One public URL, no auth, works in every MCP client.

4520. **[mcp-starter-template-ts](https://github.com/onamfc/mcp-starter-template-ts)** - ⭐ 10
   TypeScript starter template for building Model Context Protocol (MCP) servers, designed to help developers create secure and robust AI-agent-compatible services.

4521. **[ObsidianMCPServer](https://github.com/otaviocc/ObsidianMCPServer)** - ⭐ 10
   A Model Context Protocol (MCP) server that enables AI assistants to interact with your Obsidian vault

4522. **[notification-mcp](https://github.com/pinkpixel-dev/notification-mcp)** - ⭐ 10
   A Model Context Protocol server that allows AI agents to play a notification sound via a tool when a task is completed.

4523. **[pipulate](https://github.com/pipulate/pipulate)** - ⭐ 10
   Local First AI SEO Software on Nix, FastHTML & HTMX

4524. **[mcp-server-blog](https://github.com/portal-labs-infrastructure/mcp-server-blog)** - ⭐ 10
   Example of a MCP implementation using TypeScript and OAuth.

4525. **[mcpd](https://github.com/pouriya/mcpd)** - ⭐ 10
   A ~3MB MCP daemon that exposes any script as a tool for Claude, Cursor & AI assistants

4526. **[mcp-shell](https://github.com/Prat011/mcp-shell)** - ⭐ 10
   terminal based MCP Client

4527. **[mcp-sqlite-server](https://github.com/prayanks/mcp-sqlite-server)** - ⭐ 10
   These are MCP server implementations for accessing a SQLite database in your MCP client. There is both a SDIO and a SSE implementation.

4528. **[discogs-mcp](https://github.com/rianvdm/discogs-mcp)** - ⭐ 10
   A Discogs MCP Server with OAuth, to use with your favorite LLM client. Ask for recommendations, stats about your collection, details about releases you own, and more!

4529. **[flipper-mcp](https://github.com/roostercoopllc/flipper-mcp)** - ⭐ 10
   AI-powered MCP server for Flipper Zero. Control SubGHz, NFC, RFID, IR, BLE, GPIO, and more over WiFi using Claude or any MCP client.

4530. **[openapi-mcp-swagger](https://github.com/salacoste/openapi-mcp-swagger)** - ⭐ 10
   Solve AI context window limits for API docs | Convert any Swagger/OpenAPI to searchable MCP server | AI-powered endpoint discovery & code generation | Works with Cursor, Claude, VS Code

4531. **[statelessagent](https://github.com/sgx-labs/statelessagent)** - ⭐ 10
   Your AI forgets everything between sessions. SAME fixes that. Local-first, no API keys, single binary.

4532. **[mcp-kit](https://github.com/shaharia-lab/mcp-kit)** - ⭐ 10
   MCP (Model Context Protocol) Kit for Go - A Complete MCP solutions for ready to use

4533. **[Azure-Foundry-Webinar](https://github.com/ShivamGoyal03/Azure-Foundry-Webinar)** - ⭐ 10
   This repository is the official companion for the Azure AI Foundry Agent Service Webinar Series. It provides hands-on code samples, modular use cases, and practical guides for building, deploying, and scaling AI agents on Azure.

4534. **[mcpet](https://github.com/shreyaskarnik/mcpet)** - ⭐ 10
   This is a TypeScript-based Model Context Protocol (MCP) server that implements a virtual pet simulation system. It demonstrates core MCP concepts by providing tools for pet care and interaction.

4535. **[esp32-mcpserver](https://github.com/solnera/esp32-mcpserver)** - ⭐ 10
   A lightweight Model Context Protocol (MCP) server framework for ESP32. Seamlessly connect embedded devices to LLMs.

4536. **[mcp-demo](https://github.com/sshh12/mcp-demo)** - ⭐ 10
   URL MCP is a proof of concept stateless MCP server builder that allows users to build MCP servers without writing or hosting code. It's intended for protocol and security experimentation rather than for building real world MCP integrations.

4537. **[toolhive-cloud-ui](https://github.com/stacklok/toolhive-cloud-ui)** - ⭐ 10
   ToolHive Cloud UI surfaces MCP servers running in your infrastructure, highlighting metadata, tool capabilities, and copy-ready endpoints for fast AI agent integrations.

4538. **[sec-edgar-agentkit](https://github.com/stefanoamorelli/sec-edgar-agentkit)** - ⭐ 10
   AI agent toolkit for accessing and analyzing SEC EDGAR filing data. Build intelligent agents with LangChain, MCP-use, Gradio, Dify, and smolagents to analyze financial statements, insider trading, and company filings.

4539. **[storybook-mcp-server](https://github.com/stefanoamorelli/storybook-mcp-server)** - ⭐ 10
   MCP server for Storybook - provides AI assistants access to components, stories, properties and screenshots. Built with TypeScript and Model Context Protocol SDK.

4540. **[systemprompt-template](https://github.com/systempromptio/systemprompt-template)** - ⭐ 10
   Production AI agent mesh in 3 commands. MCP servers, playbooks, and multi-agent orchestration built on systemprompt-core.

4541. **[taskboard](https://github.com/tcarac/taskboard)** - ⭐ 10
   Local project management with Kanban UI, CLI, and MCP server for AI assistants. SQLite-backed, single binary, installable via Homebrew.

4542. **[awesome-mcp](https://github.com/timunbasah3/awesome-mcp)** - ⭐ 10
   🚀 Discover and explore a curated list of MCP servers, tools, and resources for AI assistants, enhancing your development and productivity.

4543. **[tupac](https://github.com/tkellogg/tupac)** - ⭐ 10
   A terminal MCP client based on the OpenAI responses API.

4544. **[mcp-chaos-rig](https://github.com/Typewise/mcp-chaos-rig)** - ⭐ 10
   A local MCP server that breaks on demand. Test your client against auth failures, disappearing tools, flaky responses, and token expiry, all from a web UI.

4545. **[kroki-mcp](https://github.com/utain/kroki-mcp)** - ⭐ 10
   Kroki-MCP is a Go-based Model Context Protocol tool that converts textual diagram definitions (PlantUML, Mermaid, and more) into images via a Kroki backend. Designed for simplicity and flexibility, it supports both local and remote Kroki servers, offers configurable settings, and outputs multiple formats – making it ideal for developers building AI

4546. **[mcp-go](https://github.com/XiaoConstantine/mcp-go)** - ⭐ 10
   Golang impl of mcp protocol

4547. **[ai-mcp-bridge](https://github.com/xiaozhug/ai-mcp-bridge)** - ⭐ 10
   rest to mcp & mcp Registry & mcp Loadbalancer & ai mcp & Multiple Registries & 多注册中心

4548. **[genkit-mcp-client-blender](https://github.com/xprilion/genkit-mcp-client-blender)** - ⭐ 10
   An MCP Client for interfacing with the Blender MCP Server built with Firebase Genkit and Gemini

4549. **[mcp-document-converter](https://github.com/xt765/mcp-document-converter)** - ⭐ 10
   MCP Document Converter - A powerful MCP tool for converting documents between multiple formats, enabling AI agents to easily transform documents.

### MCP Clients

*MCP client applications that connect to MCP servers*

1. **[chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)** - ⭐ 42,983
   CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

2. **[valuecell](https://github.com/ValueCell-ai/valuecell)** - ⭐ 10,792
   ValueCell is a community-driven, multi-agent platform for financial applications.

3. **[evolver](https://github.com/EvoMap/evolver)** - ⭐ 8,516
   The GEP-powered self-evolving engine for AI agents. Auditable evolution with Genes, Capsules, and Events. | evomap.ai

4. **[deepchat](https://github.com/ThinkInAIXYZ/deepchat)** - ⭐ 6,001
   🐬DeepChat - A smart assistant that connects powerful AI to your personal world

5. **[magic](https://github.com/dtyq/magic)** - ⭐ 4,853
   Magicrew. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system)

6. **[koog](https://github.com/JetBrains/koog)** - ⭐ 4,340
   Koog is a JVM (Java and Kotlin) framework for building predictable, fault-tolerant and enterprise-ready AI agents across all platforms – from backend services to Android and iOS, JVM, and even in-browser environments. Koog is based on our AI products expertise and provides proven solutions for complex LLM and AI problems

7. **[ragent](https://github.com/nageoffer/ragent)** - ⭐ 2,690
   企业级 Agentic RAG 智能体 - 全链路覆盖文档解析、多路检索、意图识别、问题重写、会话记忆、MCP 工具调用与深度思考。面向真实业务场景，从 0 到 1 完整工程实现。

8. **[nono](https://github.com/always-further/nono)** - ⭐ 2,649
   Capability-based agent runtime with fine-grained policies . Brokering access directly within the agent's operating context, with zero setup and zero latency

9. **[papersgpt-for-zotero](https://github.com/papersgpt/papersgpt-for-zotero)** - ⭐ 2,450
   A powerful Zotero AI and MCP plugin with ChatGPT, Gemini 3.5, Claude, DeepSeek V4, Grok, OpenRouter, Kimi 2.6, GLM 5, SiliconFlow, GPT-oss, Gemma 4, Qwen 3.7

10. **[shippie](https://github.com/mattzcarey/shippie)** - ⭐ 2,375
   extendable code review and QA agent 🚢

11. **[supermemory-mcp](https://github.com/supermemoryai/supermemory-mcp)** - ⭐ 1,699
   Your memories are in ChatGPT... But nowhere else. Universal Memory MCP makes your memories available to every single LLM. No logins or paywall. One command to set it up.

12. **[open-mcp-client](https://github.com/CopilotKit/open-mcp-client)** - ⭐ 1,642

13. **[boss-agent-cli](https://github.com/can4hou6joeng4/boss-agent-cli)** - ⭐ 1,159
   AI-agent-first CLI for BOSS 直聘 — 职位搜索、福利筛选、招聘者工作流、MCP 工具与 AI 简历优化

14. **[openinference](https://github.com/Arize-ai/openinference)** - ⭐ 1,019
   OpenTelemetry Instrumentation for AI Observability

15. **[VectorCode](https://github.com/Davidyz/VectorCode)** - ⭐ 867
   A code repository indexing tool to supercharge your LLM experience.

16. **[deepseek-pp](https://github.com/zhu1090093659/deepseek-pp)** - ⭐ 715
   DeepSeek Web browser extension: AI agent workspace with MCP tools, memory, Skills, automation, web search, and conversation export.

17. **[HyperChat](https://github.com/BigSweetPotatoStudio/HyperChat)** - ⭐ 711
   HyperChat is a Chat client that strives for openness, utilizing APIs from various LLMs to achieve the best Chat experience, as well as implementing productivity tools through the MCP protocol.

18. **[GalwayBus](https://github.com/joreilly/GalwayBus)** - ⭐ 581
   Galway Bus Kotlin Multiplatform project using Jetpack Compose and SwiftUI

19. **[comunica](https://github.com/comunica/comunica)** - ⭐ 570
   📬 A knowledge graph querying framework for JavaScript

20. **[casbin-gateway](https://github.com/apache/casbin-gateway)** - ⭐ 560
   Casbin AI & MCP security gateway for HTTP, online demo: https://door.caswaf.com

21. **[fleur](https://github.com/fleuristes/fleur)** - ⭐ 534
   The easiest way to discover and install MCPs

22. **[self-dify](https://github.com/datawhalechina/self-dify)** - ⭐ 487
   本教程将全面指导你如何快速搭建自己的AI应用环境，从Docker桌面版的安装与配置开始，到本地部署Dify并自定义AI助手功能，让你轻松实现“猜病例”、“甜蜜哄人”、“新生入学指南”、“小红书读书卡片”与“面试宝典”等多种特色AI应用。并教会你从基础智能体到使用工作流，再到知识库、DeepResearch、数据库、MCP、复杂任务编排等高阶任务，由浅到深的学习掌握基于dify的大模型应用开发。

23. **[a2a-x402](https://github.com/google-agentic-commerce/a2a-x402)** - ⭐ 485
   The A2A x402 Extension brings cryptocurrency payments to the Agent-to-Agent (A2A) protocol, enabling agents to monetize their services through on-chain payments. This extension revives the spirit of HTTP 402 "Payment Required" for the decentralized agent ecosystem.

24. **[js-reverse-automation--skill](https://github.com/Fausto-404/js-reverse-automation--skill)** - ⭐ 468
   结合chrome-devtools-mcp的能力并加上Skill的规范，实现JSRPC+Flask+autoDecoder方案的前端JS逆向自动化分析，提升JS逆向的效率

25. **[daiso-mcp](https://github.com/hmmhmmhm/daiso-mcp)** - ⭐ 302
   한국 로컬 리테일과 영화관 조회를 MCP, CLI, Codex Skill로 연결합니다.

26. **[pwno-mcp](https://github.com/pwno-io/pwno-mcp)** - ⭐ 269
   MCP for Pwn

27. **[second-brain-cloudflare](https://github.com/rahilp/second-brain-cloudflare)** - ⭐ 263
   One memory layer, every AI tool. Store anything once — recall it in Claude, ChatGPT, Cursor, or any MCP client. Self-hosted on Cloudflare's free tier.

28. **[Frappe_Assistant_Core](https://github.com/buildswithpaul/Frappe_Assistant_Core)** - ⭐ 249
   Infrastructure that connects LLMs to ERPNext. Frappe Assistant Core works with the Model Context Protocol (MCP) to expose ERPNext functionality to any compatible Language Model

29. **[openclaw.net](https://github.com/clawdotnet/openclaw.net)** - ⭐ 243
   Self-hosted OpenClaw gateway + agent runtime in .NET (NativeAOT-friendly)

30. **[ai](https://github.com/WordPress/ai)** - ⭐ 177
   AI features and experiments for WordPress. Modular framework for testing AI capabilities.

31. **[terminal-ai](https://github.com/dwmkerr/terminal-ai)** - ⭐ 161
   Unopinionated AI for the Shell. A lightweight AI CLI for scripts, pipelines, and automation, with a universal client for MCP, A2A, and other AI protocols. .

32. **[web-hacker](https://github.com/VectorlyApp/web-hacker)** - ⭐ 153
   Reverse engineer web apps

33. **[airbyte-agent-connectors](https://github.com/airbytehq/airbyte-agent-connectors)** - ⭐ 109
   🐙 Drop-in tools that give AI agents reliable, permission-aware access to external systems.

34. **[uxc](https://github.com/holon-run/uxc)** - ⭐ 107
   A unified CLI for discovering and invoking tools across OpenAPI, MCP, GraphQL, gRPC, and JSON-RPC

35. **[FlowUpdater](https://github.com/FlowArg/FlowUpdater)** - ⭐ 98
   The free and open source solution to update Minecraft.

36. **[hm_editor](https://github.com/huimeicloud/hm_editor)** - ⭐ 98
   一款轻量级、可扩展的、跨平台的、专为医疗信息化设计的电子病历编辑器内核，为EMR（电子病历系统）提供专业的结构化病历编辑与AI接入解决方案。

37. **[ai-microcore](https://github.com/Nayjest/ai-microcore)** - ⭐ 95
   A handy lib for smooth interaction with large language models (LLMs) and crafting AI apps.

38. **[mcp-manager](https://github.com/petiky/mcp-manager)** - ⭐ 94
   This is a visual client tool used to manage MCP (Model Context Protocol). With this tool, you can easily manage and operate the MCP environment without manually performing complex command-line operations.

39. **[researcher_agent](https://github.com/lgesuellip/researcher_agent)** - ⭐ 63
   An application built on the Model Context Protocol (MCP) that transforms any website into highly relevant content based on your queries. The app seamlessly integrates with platforms like X, Slack, and among others.

40. **[MCPE-Client-Sources](https://github.com/Turkeii/MCPE-Client-Sources)** - ⭐ 60

41. **[deepsecure](https://github.com/DeepTrail/deepsecure)** - ⭐ 51
   Effortlessly secure your AI agents and AI-powered workflows — from prototype to production. Get easy-to-use identity, credential, and access management built for fast-moving AI developers.

42. **[revit-mcp-commandset](https://github.com/revit-mcp/revit-mcp-commandset)** - ⭐ 47
   🔄 Revit-MCP Client | Core implementation of the Revit-MCP protocol that connects LLMs with Revit. Includes essential CRUD commands for Revit elements enabling AI-driven BIM automation.

43. **[mcp-client-python-example](https://github.com/alejandro-ao/mcp-client-python-example)** - ⭐ 39

44. **[flowllm](https://github.com/FlowLLM-AI/flowllm)** - ⭐ 32
   FlowLLM: Simplifying LLM-based HTTP/MCP Service Development

45. **[ai](https://github.com/JoakimCarlsson/ai)** - ⭐ 29
   A Go toolkit for building AI agents and applications across multiple providers. Unified LLM client, agent framework with handoffs, tool calling, streaming, structured output, MCP integration, and cost tracking.

46. **[mcpx4j](https://github.com/dylibso/mcpx4j)** - ⭐ 28
   Java client library for https://mcp.run - call portable and secure tools for your AI Agents and Apps

47. **[mcp-web-client](https://github.com/jinruoxinchen/mcp-web-client)** - ⭐ 27
   MCP Web Client project

48. **[axonflow](https://github.com/getaxonflow/axonflow)** - ⭐ 26
   AxonFlow — Source-available AI control plane for production LLM systems

49. **[mcpx-py](https://github.com/dylibso/mcpx-py)** - ⭐ 25
   Python client library for https://mcp.run - call portable & secure tools for your AI Agents and Apps

50. **[mcp-client](https://github.com/liuwenzhoa/mcp-client)** - ⭐ 22

51. **[awesome-netsuite-ai](https://github.com/michoelchaikin/awesome-netsuite-ai)** - ⭐ 22
   A curated list of awesome NetSuite AI resources, tools, articles, and community contributions focused on the NetSuite AI Connector Service and MCP (Model Context Protocol) integration.

52. **[luma-api-mcp](https://github.com/lumalabs/luma-api-mcp)** - ⭐ 21
   Powered by Ray (video) and Photon (image) models by Luma AI

53. **[web-search-plus](https://github.com/robbyczgw-cla/web-search-plus)** - ⭐ 21
   Flagship multi-provider search and extraction stack for OpenClaw, Hermes Agent, MCP clients, and native plugins.

54. **[desktop4mistral](https://github.com/hathibelagal-dev/desktop4mistral)** - ⭐ 20
   A desktop client with MCP support for Mistral LLMs

55. **[fast-mcp-client](https://github.com/aswincandra/fast-mcp-client)** - ⭐ 11
   MCP Client Implemented to FastAPI

56. **[novelcrafter-mcp](https://github.com/deadshot465/novelcrafter-mcp)** - ⭐ 11
   An experimental desktop client for using Claude Desktop's MCP with Novelcrafter codices.

57. **[chatbot-spring-ai-mcp-telegram-client](https://github.com/mohamedYoussfi/chatbot-spring-ai-mcp-telegram-client)** - ⭐ 11

58. **[ArcaMCP](https://github.com/Yoryoboy/ArcaMCP)** - ⭐ 10
   Servidor MCP para AFIP/ARCA: automatiza certificados, autorización de Web Services, emisión/consulta de comprobantes y generación de PDF con QR.

### Tools & Libraries

*Development tools and libraries for working with MCP*

1. **[n8n](https://github.com/n8n-io/n8n)** - ⭐ 192,124
   Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

2. **[goose](https://github.com/aaif-goose/goose)** - ⭐ 48,945
   an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

3. **[kong](https://github.com/Kong/kong)** - ⭐ 43,566
   🦍 The API and AI Gateway

4. **[minds](https://github.com/mindsdb/minds)** - ⭐ 39,290
   General-purpose AI designed for knowledge workers — creators, strategists, and operators — and individuals seeking AI systems they can truly control to help them get work done, with full flexibility to extend and deploy anywhere (VPC, on-prem, or cloud).

5. **[minds-platform](https://github.com/mindsdb/minds-platform)** - ⭐ 39,285
   General-purpose AI designed for knowledge workers — creators, strategists, and operators — and individuals seeking AI systems they can truly control to help them get work done, with full flexibility to extend and deploy anywhere (VPC, on-prem, or cloud).

6. **[mindsdb](https://github.com/mindsdb/mindsdb)** - ⭐ 39,161
   AI Data Vault - A query engine for AI Agents to securely query data from any datasource

7. **[agents](https://github.com/wshobson/agents)** - ⭐ 36,644
   Multi-harness agentic plugin marketplace for Claude Code, Codex CLI, Cursor, OpenCode, GitHub Copilot, and Gemini CLI

8. **[FastGPT](https://github.com/labring/FastGPT)** - ⭐ 28,362
   FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

9. **[hyperframes](https://github.com/heygen-com/hyperframes)** - ⭐ 26,889
   Write HTML. Render video. Built for agents.

10. **[agentscope](https://github.com/agentscope-ai/agentscope)** - ⭐ 26,714
   Build and run agents you can see, understand and trust.

11. **[excelize](https://github.com/qax-os/excelize)** - ⭐ 20,660
   Go language library for reading and writing Microsoft Excel™ (XLAM / XLSM / XLSX / XLTM / XLTX) spreadsheets

12. **[easy-vibe](https://github.com/datawhalechina/easy-vibe)** - ⭐ 16,798
   💻 vibe coding 2026 | Your first modern Coding course beginners to master step by step.

13. **[plate](https://github.com/udecode/plate)** - ⭐ 16,344
   Rich-text editor with AI and shadcn/ui

14. **[LangBot](https://github.com/langbot-app/LangBot)** - ⭐ 14,244
   Production-grade platform for building IM bots / 生产级即时通信机器人开发平台. Bots for QQ / QQ频道 / Discord / LINE / WeChat(微信, 企业微信)/ Telegram / 飞书 / 钉钉 / Slack e.g. Integrated with ChatGPT(GPT), DeepSeek, Dify, n8n, Langflow, Coze, Claude, Google Gemini, Nano Banana, Kimi, PPIO, Ollama, MiniMax, SiliconFlow, Qwen, Moonshot, MCP etc. LLM & Agent & RAG

15. **[langchain4j](https://github.com/langchain4j/langchain4j)** - ⭐ 12,296
   LangChain4j is an idiomatic, open-source Java library for building LLM-powered applications on the JVM. It offers a unified API over popular LLM providers and vector stores, and makes implementing tool calling (including MCP support), agents and RAG easy. It integrates seamlessly with enterprise Java frameworks like Quarkus and Spring Boot.

16. **[Fay](https://github.com/xszyou/Fay)** - ⭐ 12,179
   fay是一个帮助数字人（2.5d、3d、移动、pc、网页）或大语言模型（openai兼容、deepseek）连通业务系统的mcp框架。

17. **[note-gen](https://github.com/codexu/note-gen)** - ⭐ 12,132
   A cross-platform Markdown AI note-taking software.

18. **[ui](https://github.com/creativetimofficial/ui)** - ⭐ 11,918
   Open-source components, blocks, and AI agents designed to speed up your workflow. Import them seamlessly into your favorite tools through Registry and MCPs.

19. **[astron-agent](https://github.com/iflytek/astron-agent)** - ⭐ 8,552
   Enterprise-grade, commercial-friendly agentic workflow platform for building next-generation SuperAgents.

20. **[adk-go](https://github.com/google/adk-go)** - ⭐ 8,145
   An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

21. **[lamda](https://github.com/firerpa/lamda)** - ⭐ 7,829
    The most powerful Android RPA agent framework, next generation mobile automation.

22. **[codefather](https://github.com/liyupi/codefather)** - ⭐ 7,653
   程序员鱼皮的编程宝典 ⭐️ 2026年最全编程学习路线图！包含Java学习路线、前端学习路线、Python学习路线、C++学习路线、算法学习路线、计算机基础学习路线、AI应用开发学习路线、AI Agent开发学习路线等。提供编程入门教程、AI大模型应用开发教程、RAG开发实战、MCP开发教程、Prompt工程指南、LLM应用开发、技术知识分享、学习资源推荐、项目实战教程、热门面试题、求职经验、简历优化、编程自学指南等内容，适用于所有零基础学编程、学习AI开发、转行程序员、计算机专业学生、求职找工作的同学 💎 编程学习，就来编程导航！

23. **[camel](https://github.com/apache/camel)** - ⭐ 6,229
   Apache Camel is an open source integration framework that empowers you to quickly and easily integrate various systems consuming or producing data.

24. **[API-mega-list](https://github.com/cporter202/API-mega-list)** - ⭐ 6,146
   This GitHub repo is a powerhouse collection of APIs you can start using immediately to build everything from simple automations to full-scale applications. One of the most valuable API lists on GitHub—period. 💪

25. **[Yuxi](https://github.com/xerrors/Yuxi)** - ⭐ 5,536
   结合知识库、知识图谱管理的 多租户 Agent Harness 平台。 An agent harness that integrates a LightRAG knowledge base and knowledge graphs. Build with LangChain + Vue + FastAPI, support DeepAgents、MinerU PDF、Neo4j 、MCP.

26. **[holaOS](https://github.com/holaboss-ai/holaOS)** - ⭐ 5,498
   Your super agent for work: local-first, learn your working context in mins and never forget it.

27. **[ruoyi-ai](https://github.com/ageerle/ruoyi-ai)** - ⭐ 5,392
   面向企业级市场的一站式AI应用开发框架，支持多厂商大模型统一接入与管理，具备安全可控的企业知识库与高精度检索优化能力，提供可视化流程编排、自主决策智能体与多智能体协同调度，兼容主流 Agent Skill 协议，帮助企业与开发者零门槛快速构建安全、高效、可落地的AI智能体应用与行业解决方案。

28. **[Viper](https://github.com/FunnyWolf/Viper)** - ⭐ 5,073
   Adversary simulation and Red teaming platform with AI

29. **[nexent](https://github.com/ModelEngine-Group/nexent)** - ⭐ 5,012
   Nexent is a zero-code platform for auto-generating production-grade AI agents using Harness Engineering principles — unified tools, skills, memory, and orchestration with built-in constraints, feedback loops, and control planes.

30. **[53AIHub](https://github.com/53AI/53AIHub)** - ⭐ 4,906
   53AI Hub is an open-source AI portal, which enables you to quickly build a operational-level AI portal to launch and operate AI agents, prompts, and AI tools. It supports seamless integration with development platforms like Coze, Dify, FastGPT, RAGFlow.

31. **[Yuxi-Know](https://github.com/xerrors/Yuxi-Know)** - ⭐ 4,667
   结合LightRAG 知识库的知识图谱智能体平台。 An agent platform that integrates a LightRAG knowledge base and knowledge graphs. Build with LangChain v1 + Vue + FastAPI, support DeepAgents、MinerU PDF、Neo4j 、MCP.

32. **[ag2](https://github.com/ag2ai/ag2)** - ⭐ 4,663
   AG2 (formerly AutoGen): The Open-Source AgentOS.Join us at: https://discord.gg/sNGSwQME3x

33. **[ENScan_GO](https://github.com/wgpsec/ENScan_GO)** - ⭐ 4,451
   一款基于各大企业信息API的工具，解决在遇到的各种针对国内企业信息收集难题。一键收集控股公司ICP备案、APP、小程序、微信公众号等信息聚合导出。支持MCP接入

34. **[semantic-router](https://github.com/vllm-project/semantic-router)** - ⭐ 4,321
   System Level Intelligent Router for Mixture-of-Models at Cloud, Data Center and Edge

35. **[kubefwd](https://github.com/txn2/kubefwd)** - ⭐ 4,120
   Bulk port forwarding Kubernetes services for local development.

36. **[claude-code-book](https://github.com/lintsinghua/claude-code-book)** - ⭐ 3,632
   《御舆：解码 Agent Harness》42万字拆解 AI Agent 的Harness骨架与神经 —— Claude Code 架构深度剖析，15 章从对话循环到构建你自己的 Agent Harness。在线阅读网站：

37. **[manifest](https://github.com/mnfst/manifest)** - ⭐ 3,309
   A shadcn/ui library for building ChatGPT Apps and MCP Apps

38. **[ultracite](https://github.com/haydenbleasel/ultracite)** - ⭐ 3,002
   A highly opinionated, zero-configuration linter and formatter.

39. **[md2wechat-skill](https://github.com/geekjourneyx/md2wechat-skill)** - ⭐ 2,816
   Markdown to WeChat CLI | 一键排版发布到微信公众号：支持 40+ 排版样式和专业主题 、AI 配图 、批量发布

40. **[solon](https://github.com/opensolon/solon)** - ⭐ 2,747
   🔥 Java enterprise application development framework for full scenario: Restrained, Efficient, Open, Ecologicalll!!! 700% higher concurrency 50% memory savings Startup is 10 times faster. Packing 90% smaller; Compatible with java8 ~ java25; Supports LTS. (Replaceable spring)

41. **[generative-ai](https://github.com/genieincodebottle/generative-ai)** - ⭐ 2,354
   Comprehensive resources on Generative AI, including a detailed roadmap, projects, use cases, interview preparation, and coding preparation.

42. **[jar-analyzer](https://github.com/jar-analyzer/jar-analyzer)** - ⭐ 2,102
   Jar Analyzer - 一个 JAR 包 GUI 分析工具，支持 JAR DIFF 分析，方法调用关系搜索，方法调用链 DFS 算法分析，模拟 JVM 的污点分析验证 DFS 结果，字符串搜索，Java Web 组件入口分析，CFG 程序分析，JVM 栈帧分析，自定义表达式搜索，紧跟 AI 技术发展，支持 MCP 和 n8n 工作流

43. **[DataDesigner](https://github.com/NVIDIA-NeMo/DataDesigner)** - ⭐ 1,988
   🎨 NeMo Data Designer: Generate high-quality synthetic data from scratch or from seed data.

44. **[amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli)** - ⭐ 1,966
   ✨ Agentic chat experience in your terminal. Build applications using natural language.

45. **[agents-best-practices](https://github.com/DenisSergeevitch/agents-best-practices)** - ⭐ 1,914
   Provider-neutral Agent Skill for Codex, Claude Code, and agentic harness design.

46. **[MinecraftDev](https://github.com/minecraft-dev/MinecraftDev)** - ⭐ 1,760
   Plugin for IntelliJ IDEA that gives special support for Minecraft modding projects.

47. **[Klee](https://github.com/signerlabs/Klee)** - ⭐ 1,740
   A native macOS AI chat app powered by MLX. 100% local inference on Apple Silicon, no cloud required. Built with ShipSwift.

48. **[d2mcpp](https://github.com/mcpp-community/d2mcpp)** - ⭐ 1,713
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

49. **[Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills)** - ⭐ 1,627
   VibeSkills is a new kind of super skill that organizes 340+ governed skills into one stable AI work system.

50. **[MultiAgentPPT](https://github.com/johnson7788/MultiAgentPPT)** - ⭐ 1,604
   MultiAgentPPT 是一个集成了 A2A（Agent2Agent）+ MCP（Model Context Protocol）+ ADK（Agent Development Kit） 架构的智能化演示文稿生成系统，支持通过多智能体协作和流式并发机制

51. **[mcpelauncher-manifest](https://github.com/minecraft-linux/mcpelauncher-manifest)** - ⭐ 1,543
   The main repository for the Linux and Mac OS Bedrock edition Minecraft launcher.

52. **[IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP)** - ⭐ 1,529
   Say goodbye to the complex, verbose, and laggy interaction mode of IDA Pro MCP

53. **[paperdebugger](https://github.com/PaperDebugger/paperdebugger)** - ⭐ 1,489
   A Plugin-Based Multi-Agent System for In-Editor Academic Writing, Review, and Editing

54. **[open-trading-api](https://github.com/koreainvestment/open-trading-api)** - ⭐ 1,463
   Korea Investment & Securities Open API Github

55. **[LitterBox](https://github.com/BlackSnufkin/LitterBox)** - ⭐ 1,459
   A self-hosted sandbox for red teams to test payloads against modern detection before deployment. MCP integration lets an LLM agent drive analysis end to end.

56. **[mcpp-standard](https://github.com/Sunrisepeak/mcpp-standard)** - ⭐ 1,372
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

57. **[awesome-hacking-lists](https://github.com/taielab/awesome-hacking-lists)** - ⭐ 1,348
   A curated collection of top-tier penetration testing tools and productivity utilities across multiple domains. Join us to explore, contribute, and enhance your hacking toolkit!

58. **[Claude-Code-Development-Kit](https://github.com/peterkrueck/Claude-Code-Development-Kit)** - ⭐ 1,332
   Handle context at scale - my custom Claude Code workflow including hooks, mcp and sub agents

59. **[NagaAgent](https://github.com/Xxiii8322766509/NagaAgent)** - ⭐ 1,325
   A simple yet powerful agent framework for personal assistants, designed to enable intelligent interaction, multi-agent collaboration, and seamless tool integration.

60. **[chunkhound](https://github.com/chunkhound/chunkhound)** - ⭐ 1,311
   Local first codebase intelligence

61. **[rp-engine](https://github.com/jieyefriic/rp-engine)** - ⭐ 1,236
   YAML-native agent workflow execution engine, written in Rust

62. **[BuildingAI](https://github.com/BidingCC/BuildingAI)** - ⭐ 1,229
   BuildingAI is an enterprise-grade open-source intelligent agent platform designed for AI developers, AI entrepreneurs, and forward-thinking organizations. Through a visual configuration interface (Do It Yourself), you can build native enterprise AI applications without code. The platform offers native capabilities such as intelligent agents, MCP...

63. **[grafbase](https://github.com/grafbase/grafbase)** - ⭐ 1,229
   [Acquired by The Guild] The Grafbase GraphQL Federation Gateway

64. **[voicemode](https://github.com/mbailey/voicemode)** - ⭐ 1,222
   Natural voice conversations with Claude Code

65. **[AWorld](https://github.com/inclusionAI/AWorld)** - ⭐ 1,202
   Search, understand, reproduce, and improve an idea with ease

66. **[any-agent](https://github.com/mozilla-ai/any-agent)** - ⭐ 1,174
   A single interface to use and evaluate different agent frameworks

67. **[rulesync](https://github.com/dyoshikawa/rulesync)** - ⭐ 1,154
   A Utility CLI for AI Coding Agents

68. **[LightAgent](https://github.com/wanxingai/LightAgent)** - ⭐ 1,131
   LightAgent: Lightweight AI agent framework with memory, mcp & skill. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

69. **[zen](https://github.com/sheshbabu/zen)** - ⭐ 1,109
   Selfhosted notes app. Single golang binary, notes stored as markdown within SQLite, full-text search, very low resource usage

70. **[ai4paper](https://github.com/wdcpclover/ai4paper)** - ⭐ 1,092
   AI一键文献综述 · AI一键搜文献 · AI笔记管理 · 原生GPT直连 · MCP协议 · 支持Zotero 7/8/9 | AI4Paper.pro

71. **[ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill)** - ⭐ 1,073
   An IOS Simulator Skill for ClaudeCode. Use it to optimise Claude's ability to build, run and interact with your apps. I mainly use it as an xcodebuild wrapper to save context.

72. **[openops](https://github.com/openops-cloud/openops)** - ⭐ 1,034
   The batteries-included, No-Code FinOps automation platform, with the AI you trust.

73. **[arduino-mcp2515](https://github.com/autowp/arduino-mcp2515)** - ⭐ 1,004
   Arduino MCP2515 CAN interface library

74. **[cursor2api-go](https://github.com/libaxuan/cursor2api-go)** - ⭐ 934
   Free claude-sonnet-4.6  | cursor不倒我不倒🙏 ❌ 不支持 tools / function calling / MCP

75. **[axi](https://github.com/kunchenguid/axi)** - ⭐ 848
   Design principles for agent ergonomics. Higher accuracy with lower token cost than both MCP and regular CLI.

76. **[agent-desktop](https://github.com/lahfir/agent-desktop)** - ⭐ 836
   Native desktop automation CLI for AI agents. Control any application through OS accessibility trees with structured JSON output and deterministic element refs.

77. **[eDBG](https://github.com/ShinoLeah/eDBG)** - ⭐ 827
   eBPF-based lightweight debugger for Android with MCP support

78. **[WHartTest](https://github.com/MGdaasLab/WHartTest)** - ⭐ 826
   WHartTest 是基于 Django REST Framework 与现代大模型技术打造的 AI 驱动测试自动化平台。平台聚合自然语言理解、知识库检索与嵌入搜索能力，结合 LangChain 与 MCP（Model Context Protocol） 工具调用，实现从需求到可执行测试用例的自动化生成与管理，帮助测试团队提升效率与覆盖率。

79. **[markitdown](https://github.com/DuanYan007/markitdown)** - ⭐ 824
   markitdown：CLI；MCP

80. **[claude-chatgpt-mcp](https://github.com/syedazharmbnr1/claude-chatgpt-mcp)** - ⭐ 785
   A Claude MCP tool to interact with the ChatGPT desktop app on macOS

81. **[how-to-vibecoding](https://github.com/1EchA/how-to-vibecoding)** - ⭐ 782
   Vibecoding 系列教程：从环境搭建到多智能体协作，涵盖 MCP、Skills、Agent 分工治理

82. **[aderyn](https://github.com/Cyfrin/aderyn)** - ⭐ 778
   Solidity Static Analyzer that easily integrates into your editor

83. **[vocotype-cli](https://github.com/233stone/vocotype-cli)** - ⭐ 746
   VocoType 是一款运行在本地端侧的隐私安全语音输入工具，通过快捷键即可将语音实时转换为文字并自动输入到当前应用。支持语音转文字MCP、AI 优化文本、自定义替换词典、录音视频转文字等功能，让语音输入更高效、更安全。

84. **[MCPELauncher](https://github.com/zhuowei/MCPELauncher)** - ⭐ 738
   Source code for BlockLauncher, a launcher that patches Minecraft for Android

85. **[tool-ui](https://github.com/assistant-ui/tool-ui)** - ⭐ 726
   UI components for AI interfaces

86. **[JiwuChat](https://github.com/KiWi233333/JiwuChat)** - ⭐ 718
   JiwuChat 🍂 - A lightweight cross-platform instant messaging app with integrated AI assistants (DeepSeek/Gemini/Kimi). Features real-time messaging, audio/video calls, multi-device sync, and customizable themes. Built with Vue3 & Tauri2 🍒

87. **[Sentient](https://github.com/existence-master/Sentient)** - ⭐ 687
   A personal AI assistant for everyone

88. **[ChattyPlay-Agent](https://github.com/P1kaj1uu/ChattyPlay-Agent)** - ⭐ 687
   🚀 告别多个App！本项目主要基于Python+React+TypeScript+Hono+SQLite3+Redis，打造“All in One”智能工具集。免会员破解爱奇艺、腾讯视频、优酷、抖音、B站、小红书等20+平台视频，支持4K在线解析与无水印高速下载。集成Cloudflare Turnstile防机器人和爬虫、Google、GitHub授权登录及OpenAI SDK、埋点SDK、MCP服务和Agent等，支持ChatGPT对话、AI绘画、论文降重、Hugging Face论文爬取、在线Latex编写；更有实时黄金K线、AI思维导图、闲鱼助手等效率黑科技。内置海量动漫漫画资源，畅享阅读！轻量高效，配置即用，完美适配PC与移动端，快来ChattyPlay开启奇妙之旅吧～

89. **[ai-code-helper](https://github.com/liyupi/ai-code-helper)** - ⭐ 684
   2025 年 AI 编程助手实战项目（作者：程序员鱼皮），基于 Spring Boot 3.5 + Java 21 + LangChain4j + AI 构建智能编程学习与求职辅导机器人，覆盖 AI 大模型接入、LangChain4j 核心特性、流式对话、Prompt 工程、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、Web 爬虫、安全防护、Vue.js 前端开发、SSE 服务端推送等企业级 AI 应用开发技术。帮助开发者掌握 AI 时代必备技能，熟悉 LangChain 框架，提升编程学习效率和求职竞争力，成为企业需要的 AI 全栈开发人才。

90. **[infio-copilot](https://github.com/infiolab/infio-copilot)** - ⭐ 666
   A Cursor-inspired AI assistant for Obsidian that offers smart autocomplete and interactive chat with your selected notes

91. **[OpenIntegrations](https://github.com/Bayselonarrend/OpenIntegrations)** - ⭐ 626
   Набор инструментов интеграции с популярными сервисами и технологиями для 1С:Предприятие, OneScript и CLI+MCP (Telegram, VK, Bitrix24, Google, Яндекс, S3, PostgreSQL, SQLite, MySQL и др.)

92. **[cloudsword](https://github.com/wgpsec/cloudsword)** - ⭐ 608
   一款帮助云租户发现和测试云上风险、增强云上防护能力的综合性开源工具

93. **[Citadel](https://github.com/SethGammon/Citadel)** - ⭐ 604
   The operating layer for Claude Code + OpenAI Codex: persistent project memory, intent routing, safety hooks, cost telemetry, and parallel agent fleets.

94. **[claude-code-cli](https://github.com/huangserva/claude-code-cli)** - ⭐ 603
   这是 Claude Code 的 CLI 客户端主体（src/ 目录），即整个终端交互层的源码。具体包含： 1. CLI 入口与命令解析 — main.tsx（4684行）、entrypoints/（CLI 模式、SDK 模式、MCP 模式） 2. 终端 UI 渲染 — components/（144 个组件，用 React + Ink 渲染终端界面） 3. 工具系统 — tools/（43 个工具，Bash、文件读写编辑、Grep、Glob、Web 搜索等） 4. API 通信层 — services/api/（与 Anthropic 后端通信） 5. MCP 协议  6. 多 Agent/Team 协作 l 7. 认证与策略 8. 辅助服务 等

95. **[marmot](https://github.com/marmotdata/marmot)** - ⭐ 575
   The open-source context layer for your AI. Catalog your tables, topics, queues and APIs then expose real metadata to your AI agents.

96. **[auto-commenter](https://github.com/rokpiy/auto-commenter)** - ⭐ 569
   A Claude skill that automatically posts personalized, authentic comments in your target communities.

97. **[machi](https://github.com/qntx/machi)** - ⭐ 563
   Agent behavior that compiles

98. **[CookHero](https://github.com/Decade-qiu/CookHero)** - ⭐ 561
   CookHero是一个基于 LLM + RAG + Agent + 多模态的智能饮食与烹饪管理平台，支持智能菜谱查询、个性化饮食计划、AI 饮食记录、营养分析、Web 搜索增强，以及可扩展的 ReAct Agent / Subagent 工具体系，帮助厨房新手轻松成为“烹饪英雄”。

99. **[spool](https://github.com/paperboytm/spool)** - ⭐ 558
   Your local AI session library. Browse, pin, and ⌘K-search every Claude Code, Codex, Gemini & OpenCode session — and let the built-in scanner catch leaked secrets. Local-first, nothing leaves your machine.

100. **[Auditor](https://github.com/TheAuditorTool/Auditor)** - ⭐ 548
   Release channel for TheAuditor — see blog.theauditortool.com

101. **[spool](https://github.com/spool-lab/spool)** - ⭐ 531
   Your local AI session library. Collects sessions from Claude Code, Codex CLI, Gemini CLI (and more) — browsable and ⌘K-searchable.

102. **[SecSkills](https://github.com/DaoYiSec/SecSkills)** - ⭐ 523
   收集整理渗透测试、漏洞扫描、代码审计、CTF、逆向、安全研究 等网络安全相关的 Skills和MCP

103. **[browser-operator-core](https://github.com/BrowserOperator/browser-operator-core)** - ⭐ 486
   Browser Operator - The AI browser with built in Multi-Agent platform! Open source alternative to ChatGPT Atlas, Perplexity Comet, Dia and Microsoft CoPilot Edge Browser

104. **[Sponsio](https://github.com/SponsioLabs/Sponsio)** - ⭐ 476
   Deterministic safety solutions for probabilistic AI agents

105. **[claude-tradingview-mcp-trading](https://github.com/jackson-video-resources/claude-tradingview-mcp-trading)** - ⭐ 470
   Connect Claude Code to TradingView and execute trades automatically via BitGet

106. **[AIWriteX](https://github.com/iniwap/AIWriteX)** - ⭐ 465
   AIWriteX是基于CrewAI、AIForge的新一代智能内容创作平台，从微信公众号自动化工具起步，正在重新定义AI辅助内容创作的边界，融合"AI+创意+搜索+借鉴"四重能力，多种超绝玩法，内容创作充满无限可能。

107. **[Patter](https://github.com/PatterAI/Patter)** - ⭐ 453
   Open-source voice-AI SDK. The Vapi/Retell alternative for builders who want to own the stack. Give your AI agent a phone number in 4 lines — Python and TypeScript, MIT licensed, Twilio, Telnyx, and Plivo.

108. **[mcp-cn-a-stock](https://github.com/elsejj/mcp-cn-a-stock)** - ⭐ 449
   这是一个为大模型提供 A 股数据的的 MCP(Model Content Protocol) 服务。

109. **[LightAgent](https://github.com/wxai-space/LightAgent)** - ⭐ 430
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

110. **[bridle](https://github.com/neiii/bridle)** - ⭐ 427
   TUI / CLI config manager for agentic harnesses (Amp, Claude Code, Opencode, Goose, Copilot CLI, Crush, Droid)

111. **[reins](https://github.com/pegasi-ai/reins)** - ⭐ 415
   Stop AI agents from doing things you didn't ask for.

112. **[UE5-MCP](https://github.com/VedantRGosavi/UE5-MCP)** - ⭐ 401
   MCP for Unreal Engine 5

113. **[groundhog](https://github.com/ghuntley/groundhog)** - ⭐ 400
   Groundhog's primary purpose is to teach people how Cursor and all these other coding agents work under the hood. If you understand how these coding assistants work from first principles, then you can drive these tools harder (or perhaps make your own!).

114. **[graphrag-toolkit](https://github.com/awslabs/graphrag-toolkit)** - ⭐ 395
   Python toolkit for building graph-enhanced GenAI applications

115. **[pokemon-chat](https://github.com/skygazer42/pokemon-chat)** - ⭐ 395
   基于 LightRAG、LangGraph、MCP、RagFlow、微调LLMs宝可梦主题的智能聊天助手

116. **[volcano-agent-sdk](https://github.com/Kong/volcano-agent-sdk)** - ⭐ 394
   🌋 Build AI agents that seamlessly combine LLM reasoning with real-world actions via MCP tools — in just a few lines of TypeScript.

117. **[mcpi](https://github.com/martinohanlon/mcpi)** - ⭐ 391
   Minecraft: Pi Edition API Python Library

118. **[volcano-sdk](https://github.com/Kong/volcano-sdk)** - ⭐ 386
   🌋 Build AI agents that seamlessly combine LLM reasoning with real-world actions via MCP tools — in just a few lines of TypeScript.

119. **[Adafruit-MCP23017-Arduino-Library](https://github.com/adafruit/Adafruit-MCP23017-Arduino-Library)** - ⭐ 378
   Arduino Library for Adafruit MCP23017

120. **[MCprep](https://github.com/Moo-Ack-Productions/MCprep)** - ⭐ 355
   Blender python addon to increase workflow for creating minecraft renders and animations

121. **[boltmcp](https://github.com/boltmcp/boltmcp)** - ⭐ 353

122. **[exograph](https://github.com/exograph/exograph)** - ⭐ 345
   Build production-ready backends in minutes

123. **[depyler](https://github.com/paiml/depyler)** - ⭐ 344
   Compiles Python to Rust, helping transition off of Python to Energy Efficient and Safe Rust Code

124. **[eechat](https://github.com/Lucassssss/eechat)** - ⭐ 340
   🚀 Powerful Local AI Chat Application - Mcp, Secure, Efficient, Personalized 本地化部署的大模型客户端

125. **[MCPanelViewController](https://github.com/matthewcheok/MCPanelViewController)** - ⭐ 319
   Drop-in panel control for iOS with blurring background and screen-edge activation gestures.

126. **[news-agents](https://github.com/eugeneyan/news-agents)** - ⭐ 317
   📰 Building News Agents to Summarize News with MCP, Q, and tmux

127. **[awesome-slash](https://github.com/avifenesh/awesome-slash)** - ⭐ 312
   AI writes code. This automates everything else. 9 plugins · 39 agents · 24 skills · for Claude Code, OpenCode, Codex.

128. **[building-an-agentic-system](https://github.com/gerred/building-an-agentic-system)** - ⭐ 304
   An in-depth book and reference on building agentic systems like Claude Code

129. **[x-mcp](https://github.com/xpzouying/x-mcp)** - ⭐ 304
   小红书创作中心

130. **[skene](https://github.com/SkeneTechnologies/skene)** - ⭐ 290
   Product-Led Growth (PLG) analysis toolkit that detects tech stacks, plans growth loops and builds the loop iteratively.

131. **[ai4eh](https://github.com/ethiack/ai4eh)** - ⭐ 282
   AI for Ethical Hacking - Workshop

132. **[genie](https://github.com/automagik-dev/genie)** - ⭐ 280
   Wishes in, PRs out. CLI agent that interviews you, plans the work, dispatches parallel agents in isolated worktrees, and reviews code before you see it.

133. **[TrueMemory](https://github.com/buildingjoshbetter/TrueMemory)** - ⭐ 279
   The memory your AI should have had from the start. Automatic capture, automatic recall, 100% local. One SQLite file, zero cloud. Works with Claude Code, Claude CLI, Cursor, Codex CLI, Gemini CLI.

134. **[scribe.js](https://github.com/scribeocr/scribe.js)** - ⭐ 271
   JavaScript OCR and text extraction for images and PDFs.

135. **[Weave](https://github.com/liaotxcn/Weave)** - ⭐ 269
   A highly efficient, secure, and stable application development platform with excellent performance, easy scalability, and deep integration of AI capabilities such as LLM, AI Chat, RAG, and Agents.高效、安全、稳定的服务研发平台，具备良好性能，同时易扩展，深度集成LLM、AIChat、RAG、Agent等AI能力

136. **[talkio](https://github.com/llt22/talkio)** - ⭐ 268
   Local-first multi-AI group chat desktop app — pull gpt, Claude, Gemini, DeepSeek into one conversation. Tauri 2 + React 19.

137. **[MCPDict](https://github.com/MaigoAkisame/MCPDict)** - ⭐ 259
   Android App: 漢字古今中外讀音查詢

138. **[PSAI](https://github.com/dfinke/PSAI)** - ⭐ 256
   High-agency PowerShell AI framework for multi-agent orchestration and autonomous systems engineering

139. **[MCP-Defender](https://github.com/MCP-Defender/MCP-Defender)** - ⭐ 253
   Desktop app that automatically scans and blocks malicious MCP traffic in AI apps like Cursor, Claude, VS Code and Windsurf.

140. **[structurizr](https://github.com/structurizr/structurizr)** - ⭐ 248
   Structurizr is a "models as code" tool designed for the C4 model.

141. **[agentica](https://github.com/shibing624/agentica)** - ⭐ 246
   Agentica: Lightweight async-first Python framework for AI agents. 轻量级异步优先的AI Agent框架，支持工具调用、RAG、多智能体和MCP。

142. **[MCPMappingViewer](https://github.com/bspkrs/MCPMappingViewer)** - ⭐ 244
   A small GUI for viewing the mappings from Minecraft obfuscated code names to MCP code names.

143. **[cupcake](https://github.com/eqtylab/cupcake)** - ⭐ 244
   A native policy enforcement layer for AI coding agents. Built on OPA/Rego.

144. **[MCPConfig](https://github.com/MinecraftForge/MCPConfig)** - ⭐ 240
   Public facing repo for MCP SRG mappings.

145. **[agentic-ai-systems](https://github.com/ThibautMelen/agentic-ai-systems)** - ⭐ 240
   🐔 Agentic systems explained with chickens. Workflows, agents & orchestration made simple. Mermaid diagrams included

146. **[Minecraft-Deobfuscator3000](https://github.com/SimplyProgrammer/Minecraft-Deobfuscator3000)** - ⭐ 238
   Powerful and universal deobfuscator for Minecraft mods and java decompiler!

147. **[claudemap](https://github.com/QuinnAho/claudemap)** - ⭐ 234
   google maps for vibecoders.

148. **[MCPU](https://github.com/cpldcpu/MCPU)** - ⭐ 233
   MCPU - A Minimal 8Bit CPU in a 32 Macrocell CPLD

149. **[stock-scanner-mcp](https://github.com/wbsu2003/stock-scanner-mcp)** - ⭐ 231
   这是一个基于 FastAPI-MCP 的股票分析服务，旨在通过 MCP 工具函数接口提供股票相关的综合数据和分析能力，包括价格、评分、技术报告和 AI 分析。

150. **[langchain_data_agent](https://github.com/eosho/langchain_data_agent)** - ⭐ 228
   NL2SQL - Ask questions in plain English, get SQL queries and results. Powered by LangGraph.

151. **[LAP](https://github.com/Lap-Platform/LAP)** - ⭐ 223
   Your agents are guessing at APIs. Give them the actual Agent-Native spec. 1500+ API's Ready To-Use skills,  Compile any API spec into a lean, agent-native format. 10× smaller. OpenAPI, GraphQL, AsyncAPI, Protobuf, Postman.

152. **[mcpfp](https://github.com/MauritsWilke/mcpfp)** - ⭐ 221
   A website to generate Minecraft profile pictures

153. **[AuditLuma](https://github.com/Vistaminc/AuditLuma)** - ⭐ 217
   AuditLuma是一个AI+智能体代码审计系统，它利用多个AI代理和先进的技术，包括多代理合作协议（MCP）和Self-RAG（检索增强生成），为代码库提供全面的安全分析，目前已经支持ollama部署的本地大模型

154. **[McPicker-iOS](https://github.com/kmcgill88/McPicker-iOS)** - ⭐ 215
   McPicker is a customizable, closure driven UIPickerView drop-in solution with animations that is rotation ready.

155. **[Toucan](https://github.com/TheAgentArk/Toucan)** - ⭐ 215
   Official repo of Toucan: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments

156. **[weam](https://github.com/weam-ai/weam)** - ⭐ 214
   Web app for teams of 20+ members. In-built connections to major LLMs via API. Share chats, prompts, and agents in team or private folders. Modern, fully responsive stack (Next.js, Node.js). Deploy your own vibe-coded AI apps, agents, or workflows—or use ready-made solutions from the library.

157. **[mcpat](https://github.com/HewlettPackard/mcpat)** - ⭐ 209
   An integrated power, area, and timing modeling framework for multicore and manycore architectures

158. **[OnionClaw](https://github.com/christinminor459/OnionClaw)** - ⭐ 205
   Provide AI agents with full Tor network access and dark web data through a zero-config OpenClaw skill or standalone tool.

159. **[BaseLayer](https://github.com/zwgnr/BaseLayer)** - ⭐ 203
   Re-usable multi part components built on React Aria and TailwindCSS.

160. **[MCP-919](https://github.com/Marcelektro/MCP-919)** - ⭐ 190
   Fully working & decompiled MCP for Minecraft 1.8.9

161. **[MCPScan](https://github.com/antgroup/MCPScan)** - ⭐ 189

162. **[codecompanion-history.nvim](https://github.com/ravitemer/codecompanion-history.nvim)** - ⭐ 178
   A history management extension for codecompanion AI chat plugin that enables saving, browsing and restoring chat sessions.

163. **[selene](https://github.com/tercumantanumut/selene)** - ⭐ 169
   Selene is a desktop app that runs AI agents on your machine. Connect them to your WhatsApp, Telegram, Slack, or Discord. Write code, generate images, build personal assistants. All from one place. Your data stays on your device.

164. **[bluebox-sdk](https://github.com/VectorlyApp/bluebox-sdk)** - ⭐ 169
   Reverse engineer web apps

165. **[claude-android-skill](https://github.com/dpconde/claude-android-skill)** - ⭐ 164
   Claude Code skill for building modern Android apps following best practices.

166. **[ZenOps](https://github.com/opsre/ZenOps)** - ⭐ 160
   🧘 通过钉钉、飞书、企微智能机器人用自然语言查询运维资源的工具。

167. **[edumcp](https://github.com/aieducations/edumcp)** - ⭐ 155
   EDUMCP is a protocol that integrates the Model Context Protocol (MCP) with applications in the education field, dedicated to achieving seamless interconnection and interoperability among different AI models, educational applications, smart hardware, and teaching AGENTs.

168. **[mcp-audit](https://github.com/apisec-inc/mcp-audit)** - ⭐ 149
   See what your AI agents can access. Scan MCP configs for exposed secrets, shadow APIs, and AI models. Generate AI-BOMs for compliance.

169. **[seline](https://github.com/tercumantanumut/seline)** - ⭐ 143
   Seline is a local-first AI desktop application that brings together conversational AI, visual generation tools, vector search, and multi-channel connectivity in one place.

170. **[toon-java](https://github.com/toon-format/toon-java)** - ⭐ 142
   ☕ Community-driven Java implementation of TOON

171. **[Z.ai2api](https://github.com/hmjz100/Z.ai2api)** - ⭐ 140
   将 Z.ai Chat 代理为 OpenAI/Anthropic Compatible 格式，支持多模型列表映射、免令牌、智能处理思考链、图片上传等功能；Z.ai ZtoApi z2api ZaitoApi zai X-Signature 签名 GLM 4.5 v 4.6

172. **[rocketship](https://github.com/rocketship-ai/rocketship)** - ⭐ 140
   A QA testing framework for your coding agent.

173. **[mcp-toolkit](https://github.com/charIesding/mcp-toolkit)** - ⭐ 137
   utilities for mcp

174. **[coplay-unity-plugin](https://github.com/CoplayDev/coplay-unity-plugin)** - ⭐ 129
   Unity plugin for Coplay

175. **[awesome-ai-repositories](https://github.com/altengineer/awesome-ai-repositories)** - ⭐ 128
   A curated list of open source repositories for AI Engineers

176. **[claude-ipc-mcp](https://github.com/jdez427/claude-ipc-mcp)** - ⭐ 127
   AI-to-AI communication protocol for Claude, Gemini, and other AI assistants

177. **[agentic-ai](https://github.com/mahmoudrabie/agentic-ai)** - ⭐ 127
   This repository serves as a comprehensive knowledge hub, curating cutting-edge research papers and developments across 24 specialized domains

178. **[mcp-in-action](https://github.com/huangjia2019/mcp-in-action)** - ⭐ 120
   极客时间MCP新课已经上线！超2000同学一起开启MCP学习之旅！

179. **[roampal](https://github.com/roampal-ai/roampal)** - ⭐ 120
   Memory that learns what works.

180. **[5-Day-AI-Agents-Intensive-Course-with-Google](https://github.com/sdivyanshu90/5-Day-AI-Agents-Intensive-Course-with-Google)** - ⭐ 119
   5-Day Gen AI Intensive Course with Google

181. **[STAMP](https://github.com/KatherLab/STAMP)** - ⭐ 115
   Solid Tumor Associative Modeling in Pathology

182. **[protocol-launcher](https://github.com/zhensherlock/protocol-launcher)** - ⭐ 115
   One-click launch URL generator for protocol-based apps

183. **[AgentNexus](https://github.com/wozhenbang2004/AgentNexus)** - ⭐ 114
   Multi-Agent,MCP,RAG,SpringAI1.0.0,RE-ACT

184. **[AgentFly](https://github.com/Agent-One-Lab/AgentFly)** - ⭐ 111
   Scalable and extensible reinforcement learning for LM agents.

185. **[Gearcoleco](https://github.com/drhelius/Gearcoleco)** - ⭐ 110
   ColecoVision emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

186. **[5-Day-AI-Agents-Intensive-Course-with-Google](https://github.com/anxiong2025/5-Day-AI-Agents-Intensive-Course-with-Google)** - ⭐ 109
   谷歌5天AI Agents强化课程

187. **[GenAI-AgenticAI-From-Zero-to-Production](https://github.com/bansalkanav/GenAI-AgenticAI-From-Zero-to-Production)** - ⭐ 108
   Learn GenAI and Agentic AI from Zero to Production

188. **[kalouk-mcp](https://github.com/fabianabarca/kalouk-mcp)** - ⭐ 106
   Servidor de contexto de Kalouk para agentes de inteligencia artificial.

189. **[Squirrel](https://github.com/hakoniwaa/Squirrel)** - ⭐ 92
   ai memory for coding

190. **[yes-ue-mcp](https://github.com/softdaddy-o/yes-ue-mcp)** - ⭐ 86
   Native C++ Model Context Protocol (MCP) plugin for Unreal Engine 5.4+

191. **[TensorBlock-Studio](https://github.com/TensorBlock/TensorBlock-Studio)** - ⭐ 80
   A lightweight, open, and extensible multi-LLM interaction studio.

192. **[Complementarity.jl](https://github.com/chkwon/Complementarity.jl)** - ⭐ 79
   provides a modeling interface for mixed complementarity problems (MCP) and math programs with equilibrium problems (MPEC) via JuMP

193. **[open-skills](https://github.com/besoeasy/open-skills)** - ⭐ 78
   Battle-tested skill library for AI agents. Save 98% of API costs with ready-to-use code for crypto, PDFs, search, web scraping & more. No trial-and-error, no expensive APIs.

194. **[smart-customer-service-system](https://github.com/traveler-leon/smart-customer-service-system)** - ⭐ 78
   构建一个基于大模型的智能客服系统，可提供静态知识问答(静态数据)、动态知识问答（数据库），业务办理（api调用）等功能，同时系统具有自我学习能力。定期的反思可让系统变得更强大。

195. **[nvim-gemini-companion](https://github.com/gutsavgupta/nvim-gemini-companion)** - ⭐ 77
   A Neovim plugin to integrate Gemini CLI well (+ Qwen-code now)

196. **[quarkus-workshop-langchain4j](https://github.com/quarkusio/quarkus-workshop-langchain4j)** - ⭐ 75
   Quarkus Langchain4J Workshop

197. **[lycoris](https://github.com/solaoi/lycoris)** - ⭐ 75
   Real-time speech recognition & AI-powered note-taking app for macOS with offline/online modes, multilingual transcription, and Japanese translation support.

198. **[onemcp-hub](https://github.com/ipenywis/onemcp-hub)** - ⭐ 74
   OneMCP feature requests, bugs and improvements

199. **[tiktok-mcp](https://github.com/yap-audio/tiktok-mcp)** - ⭐ 72
   A Model Context Protocol service for TikTok video discovery and metadata extraction.

200. **[claude-code-buddy](https://github.com/PCIRCLE-AI/claude-code-buddy)** - ⭐ 64
   MeMesh Plugin — Searchable project memory plugin for Claude Code.

201. **[seekchat](https://github.com/seekrays/seekchat)** - ⭐ 64
   ✨ A Sleek and Powerful AI Desktop Assistant that supports MCP integration✨

202. **[Grapheteria](https://github.com/beubax/Grapheteria)** - ⭐ 62
   Grapheteria: A structured framework bringing uniformity to agent orchestration!

203. **[Roomey_AI_Voice_Agent](https://github.com/augmentedstartups/Roomey_AI_Voice_Agent)** - ⭐ 61
   Roomey is a multi-purpose Voice Agent designed to run your personal and business life.

204. **[houdini-mcp](https://github.com/capoom/houdini-mcp)** - ⭐ 56
   Houdini integration through the Model Context Protocol

205. **[OneCite](https://github.com/HzaCode/OneCite)** - ⭐ 56
   📚 An intelligent toolkit to automatically parse, complete, and format academic references.

206. **[Wireshark_mcp](https://github.com/jayimu/Wireshark_mcp)** - ⭐ 55
   Wireshark MCP 是一个基于 Model Context Protocol (MCP) 的服务器，允许 AI 助手通过 tshark 命令行工具进行交互。该工具提供了丰富的网络数据分析功能，支持实时抓包和离线分析。

207. **[chm-converter](https://github.com/DTDucas/chm-converter)** - ⭐ 51
   chm to markdown and vectorDB

208. **[mcp-java8-sdk](https://github.com/krrr/mcp-java8-sdk)** - ⭐ 49
   Backported Model Context Protocol SDK for Java 8

209. **[Manifold](https://github.com/Garume/Manifold)** - ⭐ 45
   Operation-first .NET foundation for generating fast CLI and MCP surfaces from a single definition.

210. **[velocity](https://github.com/OptimiLabs/velocity)** - ⭐ 42
   Local-first workspace for Claude Code, Codex CLI, and Gemini CLI with sessions, analytics, workflows, and tools

211. **[asya](https://github.com/deliveryhero/asya)** - ⭐ 40
   🎭 Actors on Kubernetes for scalable Gen AI

212. **[prompt-pro](https://github.com/timothywarner-org/prompt-pro)** - ⭐ 40
   Master AI prompting for business innovation. O'Reilly Live Learning course by Tim Warner covering ChatGPT, Claude, Copilot, and enterprise prompt engineering with MCP implementation.

213. **[ummon](https://github.com/Nayshins/ummon)** - ⭐ 37
   The semantic layer for software engineering: Connect   code to meaning, build on understanding

214. **[Agience](https://github.com/Agience/Agience)** - ⭐ 36
   MCP-native workspace for turning live work into durable knowledge.

215. **[hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298](https://github.com/LinkedInLearning/hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298)** - ⭐ 36
   this repo is for linkedin learning course: Hands-On AI: Building AI Agents with Model Context Protocol (MCP) and Agent2Agent (A2A)

216. **[xiaozhi-MCPTools](https://github.com/ZhongZiTongXue/xiaozhi-MCPTools)** - ⭐ 35
   一个图形化界面的小智MCP服务连接器，包含多种工具！ 自动部署服务，方便小白给小智Ai添加MCP工具

217. **[zentrun](https://github.com/andrewsky-labs/zentrun)** - ⭐ 34
   Prompt-driven automation platform - Transform natural language into executable workflows

218. **[mini-coder](https://github.com/sacenox/mini-coder)** - ⭐ 34
   A good idea 👾

219. **[advanced-reason-mcp](https://github.com/Kuon-dev/advanced-reason-mcp)** - ⭐ 33
   Enhanced version of "Sequential Thinking" MCP

220. **[ai-agents](https://github.com/rjmurillo/ai-agents)** - ⭐ 30
   Multi-agent system for software development

221. **[shebe](https://github.com/shebe-oss/shebe)** - ⭐ 30
   Fast BM25 full-text search for code repositories with MCP integration for AI coding agents.

222. **[awesome-mcp-list](https://github.com/notedit/awesome-mcp-list)** - ⭐ 28
   Awesome Model Context Protocol Service List

223. **[adk-mcp-gemma3](https://github.com/arjunprabhulal/adk-mcp-gemma3)** - ⭐ 27
   Build AI Agent using Google ADK , MCP and Gemma 3 model

224. **[codai](https://github.com/codai-agent/codai)** - ⭐ 26
   Codai is an AI programming tool that boosts coding efficiency and empowers non-programmers. Its future plans include introducing a local database, enabling customization, and building a versatile AI terminal. It aims to popularize AI programming and lead the AI Programming+ era.

225. **[shebe](https://github.com/rhobimd-oss/shebe)** - ⭐ 26
   Fast BM25 full-text search for code repositories with MCP integration for AI coding agents.

226. **[minime-mcp](https://github.com/manujbawa/minime-mcp)** - ⭐ 21
   Universal infinite memory layer for Developer AI assistants. One shared brain across Claude, Cursor, Windsurf & more. 100% local, built on MCP standard. Stop re-explaining context

227. **[cursor-like-pro](https://github.com/gifflet/cursor-like-pro)** - ⭐ 17
   Cursor IDE like Pro

228. **[codectx](https://github.com/hey-granth/codectx)** - ⭐ 17
   Codebase context compiler for AI agents. Graph-ranked, token-budgeted, tier-compressed output. Smarter than the existing ones.

229. **[n8n-operator](https://github.com/jakub-k-slys/n8n-operator)** - ⭐ 17
   Kubernetes Operator for N8n, a fair-code workflow automation platform with native AI capabilities.

230. **[MCPStack](https://github.com/MCP-Pipeline/MCPStack)** - ⭐ 16
   Stack & Orchestrate MCP Tools — The Scikit-Learn-Pipeline Way , For LLMs

231. **[mcp-labs](https://github.com/thangchung/mcp-labs)** - ⭐ 16
   All things about MCP experiments.⭐️ Star to support our work!

232. **[ai-tools](https://github.com/elsejj/ai-tools)** - ⭐ 15
   ai-tools  call your llm based tools through shortcut (ctrl-q) in any application

233. **[pic-standard](https://github.com/madeinplutofabio/pic-standard)** - ⭐ 14
   The industry standard for Provenance & Intent Contracts (PIC) in Agentic AI. Bridging the Causal Gap in autonomous systems.

234. **[Tapnow-Studio--](https://github.com/Menaelz/Tapnow-Studio--)** - ⭐ 14
   🎨 Create visual AI workflows with Tapnow Studio, a browser-based tool that combines powerful AI capabilities in a single, interactive node editor.

235. **[mkinf-run](https://github.com/mkinf-io/mkinf-run)** - ⭐ 13
   mkinf run API

236. **[feather_wand_agent](https://github.com/QAInsights/feather_wand_agent)** - ⭐ 13
   Feather Wand Agent is a comprehensive AI-powered toolkit for performance testing and monitoring. It integrates multiple industry-standard performance testing tools (JMeter, k6, Gatling, and Locust) into a single, unified interface, allowing users to execute and analyze performance tests through natural language interactions.

237. **[Unity-AI-Tools-Template](https://github.com/IvanMurzak/Unity-AI-Tools-Template)** - ⭐ 12
   Unity MCP Tool template project

238. **[mcp-tools](https://github.com/shaharia-lab/mcp-tools)** - ⭐ 11
   Tools for MCP (Model Context Protocol) written in Go

239. **[Ai_agents](https://github.com/jenasuraj/Ai_agents)** - ⭐ 10
   This is a repository of collection of many agents build on top of Langchain , Langgraph, MCP and so many amazing tools

240. **[claude-colony](https://github.com/MakingJamie/claude-colony)** - ⭐ 10
   Multi-agent Claude Code you can actually control. Spawn specialist teams in tmux, watch them work side-by-side, steer when needed. Built on native Claude Code agents. No black boxes.

### Examples

*Example projects demonstrating MCP usage*

1. **[YC-Killer](https://github.com/sahibzada-allahyar/YC-Killer)** - ⭐ 2,778
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and apply using the link in the readme to join our open source AI research team.

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

1. **[JavaGuide](https://github.com/Snailclimb/JavaGuide)** - ⭐ 156,325
   Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发

2. **[ai-guide](https://github.com/liyupi/ai-guide)** - ⭐ 15,621
   程序员鱼皮的 AI 资源大全 + Vibe Coding 零基础教程，分享 OpenClaw 保姆级教程、大模型玩法（DeepSeek / GPT / Gemini / Claude）、最新 AI 资讯、Prompt 提示词大全、AI 知识百科（Agent Skills / RAG / MCP / A2A）、AI 编程教程（Harness Engineering）、AI 工具用法（Cursor / Claude Code / TRAE / Codex / Copilot）、AI 开发框架教程（Spring AI / LangChain）、AI 产品变现指南，帮你快速掌握 AI 技术，走在时代前沿。本项目为开源文档，已升级为鱼皮 AI 导航网站

3. **[modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)** - ⭐ 8,379
   Specification and documentation for the Model Context Protocol

4. **[wechatDownload](https://github.com/qiye45/wechatDownload)** - ⭐ 8,066
   微信公众号文章批量下载工具，支持评论、合集下载，支持保存html/mhtml/md/pdf/docx/csv文件，保存文章内图片、视频、音频文件，支持MCP/Skill调用

5. **[openagent](https://github.com/Haohao-end/openagent)** - ⭐ 821
   AI Agent Development Platform - Supports multiple models (OpenAI/DeepSeek/Wenxin/Tongyi), knowledge base management, workflow automation, and enterprise-grade security. Built with Flask + Vue3 + LangChain, featuring one-click Docker deployment.

6. **[forksilly.doc](https://github.com/fatsnk/forksilly.doc)** - ⭐ 107
   Documents repo of ForkSilly. ForkSilly：兼容sillytavern（酒馆）角色卡、世界书、正则、预设、聊天记录的安卓移动端应用；同时也可作为stable diffusion客户端使用。

7. **[claude-code-cli](https://github.com/Harkirat1462/claude-code-cli)** - ⭐ 105
   claude code cli install codex github anthropic agentic coding system terminal assistant codebase git workflows multi file editing mcp protocol model context protocol subagents automation ci cd integration npm install setup guide tutorial command line interface latest version 2026 free download update bug fix test runner**

8. **[platform-engineering](https://github.com/codetocloudorg/platform-engineering)** - ⭐ 94
   A centralized hub for platform engineering teams, providing resources, best practices, and automation tools. Includes IaC templates, blueprints, and operational guides to help build scalable, secure, and efficient platforms for cloud-native environments and DevSecOps workflows.

9. **[pew-pew-plaza-packs](https://github.com/appboypov/pew-pew-plaza-packs)** - ⭐ 83
   AI-powered project management framework based on an opinionated view on effective prompts and a highly modular approach to building effective agents, workflows, templates, prompts and context documents.

10. **[Agent-Fusion](https://github.com/krokozyab/Agent-Fusion)** - ⭐ 57
    Agent Fusion is a local RAG semantic search engine that gives AI agents instant access to your code, documentation (Markdown, Word, PDF). Query    your codebase from code agents without hallucinations. Runs 100% locally, includes a lightweight embedding model, and optional multi-agent task    orchestration. Deploy with a single JAR

11. **[codedox](https://github.com/chriswritescode-dev/codedox)** - ⭐ 27
    A powerful system for crawling documentation websites, extracting code snippets, and providing fast search capabilities via MCP (Model Context Protocol) integration.

12. **[Q4_learning](https://github.com/DanielHashmi/Q4_learning)** - ⭐ 15
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

