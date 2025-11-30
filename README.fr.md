# Awesome MCP

> Une liste organisée de projets Model Context Protocol (MCP) impressionnants depuis GitHub

[![Auto Update](https://github.com/Rodert/awesome-mcp/workflows/Update%20Projects/badge.svg)](https://github.com/Rodert/awesome-mcp/actions)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

**Languages / 语言 / Языки / 言語 / Langues / Idiomas:**
- [English](README.md) | [中文](README.zh.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Français](README.fr.md) | [Español](README.es.md)

Ce dépôt collecte et organise automatiquement des projets MCP de haute qualité depuis GitHub, les présentant dans un format beau et consultable. La liste est mise à jour quotidiennement via GitHub Actions et hébergée sur GitHub Pages.

## 🌐 Langues

- [English](https://rodert.github.io/awesome-mcp/en/projects)
- [中文](https://rodert.github.io/awesome-mcp/zh/projects)
- [Русский](https://rodert.github.io/awesome-mcp/ru/projects)
- [日本語](https://rodert.github.io/awesome-mcp/ja/projects)
- [Français](https://rodert.github.io/awesome-mcp/fr/projects)
- [Español](https://rodert.github.io/awesome-mcp/es/projects)

## 🚀 Démarrage rapide : Comment utiliser MCP dans les outils IA

Le Model Context Protocol (MCP) permet aux assistants IA de se connecter à des sources de données et outils externes. Voici comment le configurer dans les outils IA populaires :

### 📱 Claude Desktop

1. **Trouvez le fichier de configuration :**
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

2. **Modifiez le fichier de configuration** et ajoutez vos serveurs MCP :

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

3. **Redémarrez Claude Desktop** pour appliquer les modifications.

### 💻 Cursor IDE

1. **Ouvrez les paramètres** : `Cmd/Ctrl + ,`
2. **Naviguez vers** : Features → Agent → MCP Servers
3. **Cliquez sur "Add Server"**
4. **Entrez les détails du serveur** :
   - **Nom** : Un nom convivial pour le serveur
   - **Commande** : La commande à exécuter (par ex. `npx`)
   - **Arguments** : Arguments de la commande (par ex. `["-y", "@modelcontextprotocol/server-github"]`)
   - **Variables d'environnement** : Variables d'environnement (si nécessaire)

### 🔌 Continue (Extension VS Code)

1. **Installez l'extension Continue** depuis le marketplace VS Code
2. **Ouvrez les paramètres Continue** : Cliquez sur l'icône Continue dans la barre latérale
3. **Naviguez vers** : Settings → MCP Servers
4. **Ajoutez un serveur MCP** dans `~/.continue/config.json` :

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

5. **Rechargez VS Code** pour appliquer les modifications.

### 🔌 Cline (Extension VS Code)

1. **Installez l'extension Cline** depuis le marketplace VS Code
2. **Ouvrez la palette de commandes** : `Cmd/Ctrl + Shift + P`
3. **Exécutez** : `Cline: Configure MCP Servers`
4. **Modifiez le fichier de configuration** qui s'ouvre, ou modifiez manuellement `~/.cline/mcp_config.json` :

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

5. **Redémarrez VS Code** pour appliquer les modifications.

### ⚡ Aider (Ligne de commande)

1. **Installez Aider** : `pip install aider-chat`
2. **Définissez la variable d'environnement** pour les serveurs MCP :

```bash
export MCP_SERVERS='{"github": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-github"], "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": "your_token"}}}'
```

3. **Ou créez** `~/.aider/mcp_config.json` :

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

4. **Exécutez Aider** : `aider` (les serveurs MCP seront automatiquement chargés)

### 🌊 Windsurf

1. **Ouvrez les paramètres Windsurf** : `Cmd/Ctrl + ,`
2. **Naviguez vers** : Extensions → MCP
3. **Cliquez sur "Add MCP Server"**
4. **Configurez le serveur** :
   - **Nom** : Identifiant du serveur
   - **Commande** : Commande à exécuter
   - **Arguments** : Arguments de la commande
   - **Variables d'environnement** : Variables d'environnement
5. **Enregistrez et redémarrez** Windsurf

### 🎨 Composer (Anthropic)

1. **Ouvrez les paramètres Composer**
2. **Naviguez vers** : Settings → Integrations → MCP
3. **Ajoutez la configuration du serveur MCP** :

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

4. **Redémarrez Composer** pour appliquer les modifications.

### 🔍 Trouver des serveurs MCP

Parcourez la [liste des projets](#-projets-9-au-total) ci-dessous pour découvrir les serveurs MCP disponibles. Les options populaires incluent :

- **[GitHub MCP Server](https://github.com/github/github-mcp-server)** - Accéder aux dépôts et problèmes GitHub
- **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** - Automatisation du navigateur
- **[Filesystem Server](https://github.com/modelcontextprotocol/servers)** - Accès au système de fichiers
- **[SQLite Server](https://github.com/modelcontextprotocol/servers)** - Requêtes de base de données

### 📝 Exemple : GitHub MCP Server

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

**Obtenir un token GitHub** : [GitHub Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)

### 🎯 Que peut faire MCP ?

Une fois configuré, MCP permet aux assistants IA de :
- 📂 Accéder aux fichiers et répertoires
- 🔍 Rechercher dans les dépôts de code
- 🌐 Naviguer sur le web
- 💾 Interroger les bases de données
- 📊 Analyser les données
- 🔧 Exécuter des outils et scripts

### 📚 En savoir plus

- [Documentation officielle MCP](https://modelcontextprotocol.io/)
- [Spécification MCP](https://github.com/modelcontextprotocol/specification)
- Parcourir la [Collection de serveurs MCP](https://github.com/modelcontextprotocol/servers)

---

## 📚 Projets (9 au total)

> Dernière mise à jour : **2025-11-22**

### Serveurs MCP

*Implémentations de serveurs MCP qui fournissent des services de protocole*

1. **[dify](https://github.com/langgenius/dify)** - ⭐ 119,501
   Plateforme prête pour la production pour le développement de workflows d'agents.

2. **[open-webui](https://github.com/open-webui/open-webui)** - ⭐ 115,900
   Interface AI conviviale (Prend en charge Ollama, OpenAI API, ...)

3. **[netdata](https://github.com/netdata/netdata)** - ⭐ 76,770
   Le chemin le plus rapide vers l'observabilité complète alimentée par l'IA, même pour les équipes réduites.

4. **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** - ⭐ 75,146
   Une collection de serveurs MCP.

5. **[servers](https://github.com/modelcontextprotocol/servers)** - ⭐ 73,079
   Serveurs Model Context Protocol

[Voir tous les 8 →](https://rodert.github.io/awesome-mcp/fr/projects)

### Clients MCP

*Applications clientes MCP qui se connectent aux serveurs MCP*

*Bientôt disponible...*

### Outils et bibliothèques

*Outils de développement et bibliothèques pour travailler avec MCP*

1. **[n8n](https://github.com/n8n-io/n8n)** - ⭐ 157,879
   Plateforme d'automatisation de workflows à code équitable avec des capacités AI natives. Combine la construction visuelle avec du code personnalisé, auto-hébergé ou cloud, 400+ intégrations.

### Exemples

*Projets d'exemple démontrant l'utilisation de MCP*

*Bientôt disponible...*

### Documentation

*Documentation, tutoriels et ressources d'apprentissage*

*Bientôt disponible...*

---

**[Voir la liste complète des projets sur GitHub Pages →](https://rodert.github.io/awesome-mcp/)**

## 📋 Critères du projet

- ⭐ Au moins 10 étoiles
- 📝 Doit avoir un fichier README
- 🔍 Découvert via des mots-clés, sujets et tags liés à MCP

## 🤖 Automatisation

Ce dépôt utilise des scripts automatisés qui :

1. **Collectent** des projets quotidiennement via l'API GitHub Search
2. **Catégorisent** les projets par cas d'utilisation (serveurs, clients, outils, exemples, documentation)
3. **Traduisent** le contenu dans plusieurs langues en utilisant la traduction IA
4. **Mettent à jour** le site Web automatiquement

## 🏗️ Structure

```
awesome-mcp/
├── .github/workflows/    # Automatisation GitHub Actions
├── scripts/              # Scripts Python de collecte et de traduction
├── data/                 # Fichiers de données JSON
└── docs/                 # Source du site VitePress
```

## 📝 Licence

Sous licence Apache License 2.0 - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👥 Mainteneurs

Ce projet est maintenu par des assistants de codage IA :

- **Cursor** - Éditeur de code alimenté par l'IA
- **Claude Code** - Assistant de codage IA d'Anthropic
- **DeepSeek** - Assistant de codage IA DeepSeek
- **Gemini** - Assistant de codage IA de Google

Ces assistants IA collaborent pour maintenir le projet à jour, collecter de nouveaux projets MCP et maintenir la qualité de la liste organisée.

## 🙏 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à soumettre une Pull Request.

