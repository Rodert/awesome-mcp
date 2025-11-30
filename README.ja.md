# Awesome MCP

> GitHub からの素晴らしい Model Context Protocol (MCP) プロジェクトのキュレーションリスト

[![Auto Update](https://github.com/Rodert/awesome-mcp/workflows/Update%20Projects/badge.svg)](https://github.com/Rodert/awesome-mcp/actions)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

**Languages / 语言 / Языки / 言語 / Langues / Idiomas:**
- [English](README.md) | [中文](README.zh.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Français](README.fr.md) | [Español](README.es.md)

このリポジトリは、GitHub から高品質な MCP プロジェクトを自動的に収集し、整理し、美しく検索可能な形式で提示します。リストは GitHub Actions を通じて毎日更新され、GitHub Pages でホストされています。

## 🌐 言語

- [English](https://rodert.github.io/awesome-mcp/en/projects)
- [中文](https://rodert.github.io/awesome-mcp/zh/projects)
- [Русский](https://rodert.github.io/awesome-mcp/ru/projects)
- [日本語](https://rodert.github.io/awesome-mcp/ja/projects)
- [Français](https://rodert.github.io/awesome-mcp/fr/projects)
- [Español](https://rodert.github.io/awesome-mcp/es/projects)

## 🚀 クイックスタート：AIツールでMCPを使用する方法

Model Context Protocol (MCP) により、AIアシスタントは外部データソースやツールに接続できます。人気のあるAIツールでMCPを設定する方法は以下の通りです：

### 📱 Claude Desktop

1. **設定ファイルを見つける：**
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

2. **設定ファイルを編集**してMCPサーバーを追加：

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

3. **Claude Desktopを再起動**して変更を適用。

### 💻 Cursor IDE

1. **設定を開く**：`Cmd/Ctrl + ,`
2. **移動**：Features → Agent → MCP Servers
3. **"Add Server"をクリック**
4. **サーバーの詳細を入力**：
   - **名前**：サーバーのわかりやすい名前
   - **コマンド**：実行するコマンド（例：`npx`）
   - **引数**：コマンド引数（例：`["-y", "@modelcontextprotocol/server-github"]`）
   - **環境変数**：環境変数（必要に応じて）

### 🔌 Continue (VS Code拡張機能)

1. **Continue拡張機能をインストール**：VS Codeマーケットプレイスから
2. **Continue設定を開く**：サイドバーのContinueアイコンをクリック
3. **移動**：Settings → MCP Servers
4. **`~/.continue/config.json`にMCPサーバーを追加**：

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

5. **VS Codeを再読み込み**して変更を適用。

### 🔌 Cline (VS Code拡張機能)

1. **Cline拡張機能をインストール**：VS Codeマーケットプレイスから
2. **コマンドパレットを開く**：`Cmd/Ctrl + Shift + P`
3. **実行**：`Cline: Configure MCP Servers`
4. **開いた設定ファイルを編集**するか、手動で`~/.cline/mcp_config.json`を編集：

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

5. **VS Codeを再起動**して変更を適用。

### ⚡ Aider (コマンドライン)

1. **Aiderをインストール**：`pip install aider-chat`
2. **MCPサーバー用の環境変数を設定**：

```bash
export MCP_SERVERS='{"github": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-github"], "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": "your_token"}}}'
```

3. **または`~/.aider/mcp_config.json`を作成**：

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

4. **Aiderを実行**：`aider`（MCPサーバーが自動的に読み込まれます）

### 🌊 Windsurf

1. **Windsurf設定を開く**：`Cmd/Ctrl + ,`
2. **移動**：Extensions → MCP
3. **"Add MCP Server"をクリック**
4. **サーバーを設定**：
   - **名前**：サーバー識別子
   - **コマンド**：実行するコマンド
   - **引数**：コマンド引数
   - **環境変数**：環境変数
5. **保存してWindsurfを再起動**

### 🎨 Composer (Anthropic)

1. **Composer設定を開く**
2. **移動**：Settings → Integrations → MCP
3. **MCPサーバー設定を追加**：

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

4. **Composerを再起動**して変更を適用。

### 🔍 MCPサーバーの検索

以下の[プロジェクトリスト](#-プロジェクト合計-9)を閲覧して、利用可能なMCPサーバーを見つけます。人気のあるオプションには以下が含まれます：

- **[GitHub MCP Server](https://github.com/github/github-mcp-server)** - GitHubリポジトリとイシューにアクセス
- **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** - ブラウザ自動化
- **[Filesystem Server](https://github.com/modelcontextprotocol/servers)** - ファイルシステムアクセス
- **[SQLite Server](https://github.com/modelcontextprotocol/servers)** - データベースクエリ

### 📝 例：GitHub MCP Server

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

**GitHubトークンを取得**：[GitHub Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)

### 🎯 MCPでできること

設定後、MCPはAIアシスタントに以下を可能にします：
- 📂 ファイルとディレクトリへのアクセス
- 🔍 コードリポジトリの検索
- 🌐 ウェブの閲覧
- 💾 データベースのクエリ
- 📊 データの分析
- 🔧 ツールとスクリプトの実行

### 📚 詳細情報

- [公式MCPドキュメント](https://modelcontextprotocol.io/)
- [MCP仕様](https://github.com/modelcontextprotocol/specification)
- [MCPサーバーコレクション](https://github.com/modelcontextprotocol/servers)を閲覧

---

## 📚 プロジェクト（合計 9）

> 最終更新：**2025-11-22**

### MCP サーバー

*プロトコルサービスを提供する MCP サーバーの実装*

1. **[dify](https://github.com/langgenius/dify)** - ⭐ 119,501
   エージェントワークフロー開発のための本番対応プラットフォーム。

2. **[open-webui](https://github.com/open-webui/open-webui)** - ⭐ 115,900
   ユーザーフレンドリーな AI インターフェース（Ollama、OpenAI API などをサポート）

3. **[netdata](https://github.com/netdata/netdata)** - ⭐ 76,770
   AI を活用したフルスタック可観測性への最短パス。小規模チームでも利用可能。

4. **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** - ⭐ 75,146
   MCP サーバーのコレクション。

5. **[servers](https://github.com/modelcontextprotocol/servers)** - ⭐ 73,079
   Model Context Protocol サーバー

[すべての 8 件を表示 →](https://rodert.github.io/awesome-mcp/ja/projects)

### MCP クライアント

*MCP サーバーに接続する MCP クライアントアプリケーション*

*近日公開...*

### ツールとライブラリ

*MCP を扱うための開発ツールとライブラリ*

1. **[n8n](https://github.com/n8n-io/n8n)** - ⭐ 157,879
   ネイティブ AI 機能を備えたフェアコードワークフロー自動化プラットフォーム。ビジュアル構築とカスタムコードを組み合わせ、セルフホストまたはクラウド、400+ の統合。

### 例

*MCP の使用を実演するサンプルプロジェクト*

*近日公開...*

### ドキュメント

*ドキュメント、チュートリアル、学習リソース*

*近日公開...*

---

**[GitHub Pages で完全なプロジェクトリストを表示 →](https://rodert.github.io/awesome-mcp/)**

## 📋 プロジェクト基準

- ⭐ 少なくとも 10 スター
- 📝 README ファイルが必要
- 🔍 MCP 関連のキーワード、トピック、タグを通じて発見

## 🤖 自動化

このリポジトリは、以下の自動化スクリプトを使用します：

1. **収集** - GitHub Search API を通じて毎日プロジェクトを収集
2. **分類** - ユースケース別にプロジェクトを分類（サーバー、クライアント、ツール、例、ドキュメント）
3. **翻訳** - AI 翻訳を使用してコンテンツを複数の言語に翻訳
4. **更新** - ウェブサイトを自動的に更新

## 🏗️ 構造

```
awesome-mcp/
├── .github/workflows/    # GitHub Actions 自動化
├── scripts/              # Python 収集および翻訳スクリプト
├── data/                 # JSON データファイル
└── docs/                 # VitePress サイトソース
```

## 📝 ライセンス

Apache License 2.0 の下でライセンスされています - 詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 👥 メンテナー

このプロジェクトは、以下の AI コーディングアシスタントによってメンテナンスされています：

- **Cursor** - AI を活用したコードエディタ
- **Claude Code** - Anthropic の AI コーディングアシスタント
- **DeepSeek** - DeepSeek AI コーディングアシスタント
- **Gemini** - Google の AI コーディングアシスタント

これらの AI アシスタントは協力して、プロジェクトを最新の状態に保ち、新しい MCP プロジェクトを収集し、キュレーションリストの品質を維持します。

## 🙏 貢献

貢献を歓迎します！お気軽に Pull Request を送信してください。

