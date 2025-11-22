# Contributing to Awesome MCP

感谢您对 Awesome MCP 项目的关注！我们欢迎各种形式的贡献。

## 如何贡献

### 报告问题

如果您发现：
- 某个项目链接失效
- 项目分类错误
- 缺失的优秀项目
- 其他问题

请[提交 Issue](https://github.com/Rodert/awesome-mcp/issues/new)。

### 提交项目

如果您想添加新的 MCP 项目：

1. **手动提交（推荐）**
   - Fork 本仓库
   - 编辑 `data/projects.json` 文件，添加项目信息
   - 提交 Pull Request

2. **通过自动化**
   - 项目会自动通过 GitHub Actions 定期收集
   - 如果项目满足条件（≥10 stars，有 README），会自动出现在列表中

### 项目添加标准

- ⭐ Stars 数量 ≥ 10
- 📝 必须有 README 文件
- 🔗 项目必须与 MCP（Model Context Protocol）相关
- ✅ 项目必须未被归档（archived）

## 本地开发

### 环境要求

- Python 3.11+
- Node.js 18+
- npm 或 yarn

### 设置步骤

1. **克隆仓库**
   ```bash
   git clone https://github.com/Rodert/awesome-mcp.git
   cd awesome-mcp
   ```

2. **安装 Python 依赖**
   ```bash
   cd scripts
   pip install -r requirements.txt
   ```

3. **安装 Node.js 依赖**
   ```bash
   npm install
   ```

4. **设置 GitHub Token**
   ```bash
   export GITHUB_TOKEN=your_github_token_here
   ```

5. **运行采集脚本**
   ```bash
   python scripts/collect_projects.py
   python scripts/generate_markdown.py
   python scripts/translate_content.py  # 可选，翻译可能需要较长时间
   ```

6. **本地预览网站**
   ```bash
   npm run dev
   ```

7. **构建网站**
   ```bash
   npm run build
   ```

## 代码规范

- Python 代码遵循 PEP 8 规范
- JavaScript 代码使用 ES6+ 语法
- Markdown 文件使用标准 Markdown 格式

## 许可证

贡献即表示您同意您的代码将遵循本项目使用的 Apache License 2.0 许可证。

## 问题反馈

如有任何问题，请随时[提交 Issue](https://github.com/Rodert/awesome-mcp/issues)。

感谢您的贡献！🎉

