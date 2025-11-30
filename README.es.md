# Awesome MCP

> Una lista curada de increíbles proyectos Model Context Protocol (MCP) de GitHub

[![Auto Update](https://github.com/Rodert/awesome-mcp/workflows/Update%20Projects/badge.svg)](https://github.com/Rodert/awesome-mcp/actions)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

**Languages / 语言 / Языки / 言語 / Langues / Idiomas:**
- [English](README.md) | [中文](README.zh.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Français](README.fr.md) | [Español](README.es.md)

Este repositorio recopila y organiza automáticamente proyectos MCP de alta calidad de GitHub, presentándolos en un formato hermoso y consultable. La lista se actualiza diariamente a través de GitHub Actions y se aloja en GitHub Pages.

## 🌐 Idiomas

- [English](https://rodert.github.io/awesome-mcp/en/projects)
- [中文](https://rodert.github.io/awesome-mcp/zh/projects)
- [Русский](https://rodert.github.io/awesome-mcp/ru/projects)
- [日本語](https://rodert.github.io/awesome-mcp/ja/projects)
- [Français](https://rodert.github.io/awesome-mcp/fr/projects)
- [Español](https://rodert.github.io/awesome-mcp/es/projects)

## 🚀 Inicio rápido: Cómo usar MCP en herramientas de IA

El Model Context Protocol (MCP) permite que los asistentes de IA se conecten a fuentes de datos y herramientas externas. Así es como configurarlo en herramientas de IA populares:

### 📱 Claude Desktop

1. **Encuentra el archivo de configuración:**
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

2. **Edita el archivo de configuración** y agrega tus servidores MCP:

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

3. **Reinicia Claude Desktop** para aplicar los cambios.

### 💻 Cursor IDE

1. **Abre Configuración**: `Cmd/Ctrl + ,`
2. **Navega a**: Features → Agent → MCP Servers
3. **Haz clic en "Add Server"**
4. **Ingresa los detalles del servidor**:
   - **Nombre**: Un nombre descriptivo para el servidor
   - **Comando**: El comando a ejecutar (ej. `npx`)
   - **Argumentos**: Argumentos del comando (ej. `["-y", "@modelcontextprotocol/server-github"]`)
   - **Variables de entorno**: Variables de entorno (si es necesario)

### 🔌 Continue (Extensión de VS Code)

1. **Instala la extensión Continue** desde el marketplace de VS Code
2. **Abre la configuración de Continue**: Haz clic en el icono de Continue en la barra lateral
3. **Navega a**: Settings → MCP Servers
4. **Agrega un servidor MCP** en `~/.continue/config.json`:

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

5. **Recarga VS Code** para aplicar los cambios.

### 🔌 Cline (Extensión de VS Code)

1. **Instala la extensión Cline** desde el marketplace de VS Code
2. **Abre la paleta de comandos**: `Cmd/Ctrl + Shift + P`
3. **Ejecuta**: `Cline: Configure MCP Servers`
4. **Edita el archivo de configuración** que se abre, o edita manualmente `~/.cline/mcp_config.json`:

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

5. **Reinicia VS Code** para aplicar los cambios.

### ⚡ Aider (Línea de comandos)

1. **Instala Aider**: `pip install aider-chat`
2. **Establece la variable de entorno** para los servidores MCP:

```bash
export MCP_SERVERS='{"github": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-github"], "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": "your_token"}}}'
```

3. **O crea** `~/.aider/mcp_config.json`:

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

4. **Ejecuta Aider**: `aider` (los servidores MCP se cargarán automáticamente)

### 🌊 Windsurf

1. **Abre la configuración de Windsurf**: `Cmd/Ctrl + ,`
2. **Navega a**: Extensions → MCP
3. **Haz clic en "Add MCP Server"**
4. **Configura el servidor**:
   - **Nombre**: Identificador del servidor
   - **Comando**: Comando a ejecutar
   - **Argumentos**: Argumentos del comando
   - **Variables de entorno**: Variables de entorno
5. **Guarda y reinicia** Windsurf

### 🎨 Composer (Anthropic)

1. **Abre la configuración de Composer**
2. **Navega a**: Settings → Integrations → MCP
3. **Agrega la configuración del servidor MCP**:

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

4. **Reinicia Composer** para aplicar los cambios.

### 🔍 Encontrar servidores MCP

Explora la [lista de proyectos](#-proyectos-9-en-total) a continuación para descubrir servidores MCP disponibles. Las opciones populares incluyen:

- **[GitHub MCP Server](https://github.com/github/github-mcp-server)** - Acceder a repositorios e issues de GitHub
- **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** - Automatización del navegador
- **[Filesystem Server](https://github.com/modelcontextprotocol/servers)** - Acceso al sistema de archivos
- **[SQLite Server](https://github.com/modelcontextprotocol/servers)** - Consultas a bases de datos

### 📝 Ejemplo: GitHub MCP Server

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

**Obtener un token de GitHub**: [GitHub Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)

### 🎯 ¿Qué puede hacer MCP?

Una vez configurado, MCP permite a los asistentes de IA:
- 📂 Acceder a archivos y directorios
- 🔍 Buscar en repositorios de código
- 🌐 Navegar por la web
- 💾 Consultar bases de datos
- 📊 Analizar datos
- 🔧 Ejecutar herramientas y scripts

### 📚 Más información

- [Documentación oficial de MCP](https://modelcontextprotocol.io/)
- [Especificación de MCP](https://github.com/modelcontextprotocol/specification)
- Explorar la [Colección de servidores MCP](https://github.com/modelcontextprotocol/servers)

---

## 📚 Proyectos (9 en total)

> Última actualización: **2025-11-22**

### Servidores MCP

*Implementaciones de servidores MCP que proporcionan servicios de protocolo*

1. **[dify](https://github.com/langgenius/dify)** - ⭐ 119,501
   Plataforma lista para producción para el desarrollo de flujos de trabajo de agentes.

2. **[open-webui](https://github.com/open-webui/open-webui)** - ⭐ 115,900
   Interfaz de IA fácil de usar (Soporta Ollama, OpenAI API, ...)

3. **[netdata](https://github.com/netdata/netdata)** - ⭐ 76,770
   El camino más rápido hacia la observabilidad completa impulsada por IA, incluso para equipos pequeños.

4. **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** - ⭐ 75,146
   Una colección de servidores MCP.

5. **[servers](https://github.com/modelcontextprotocol/servers)** - ⭐ 73,079
   Servidores Model Context Protocol

[Ver todos los 8 →](https://rodert.github.io/awesome-mcp/es/projects)

### Clientes MCP

*Aplicaciones cliente MCP que se conectan a servidores MCP*

*Próximamente...*

### Herramientas y bibliotecas

*Herramientas de desarrollo y bibliotecas para trabajar con MCP*

1. **[n8n](https://github.com/n8n-io/n8n)** - ⭐ 157,879
   Plataforma de automatización de flujos de trabajo de código justo con capacidades de IA nativas. Combina construcción visual con código personalizado, autoalojado o en la nube, 400+ integraciones.

### Ejemplos

*Proyectos de ejemplo que demuestran el uso de MCP*

*Próximamente...*

### Documentación

*Documentación, tutoriales y recursos de aprendizaje*

*Próximamente...*

---

**[Ver la lista completa de proyectos en GitHub Pages →](https://rodert.github.io/awesome-mcp/)**

## 📋 Criterios del proyecto

- ⭐ Al menos 10 estrellas
- 📝 Debe tener un archivo README
- 🔍 Descubierto a través de palabras clave, temas y etiquetas relacionadas con MCP

## 🤖 Automatización

Este repositorio utiliza scripts automatizados que:

1. **Recopilan** proyectos diariamente a través de la API de búsqueda de GitHub
2. **Categorizan** proyectos por caso de uso (servidores, clientes, herramientas, ejemplos, documentación)
3. **Traducen** contenido a múltiples idiomas usando traducción de IA
4. **Actualizan** el sitio web automáticamente

## 🏗️ Estructura

```
awesome-mcp/
├── .github/workflows/    # Automatización de GitHub Actions
├── scripts/              # Scripts de Python para recopilación y traducción
├── data/                 # Archivos de datos JSON
└── docs/                 # Fuente del sitio VitePress
```

## 📝 Licencia

Licenciado bajo Apache License 2.0 - consulte el archivo [LICENSE](LICENSE) para más detalles.

## 👥 Mantenedores

Este proyecto es mantenido por asistentes de codificación de IA:

- **Cursor** - Editor de código impulsado por IA
- **Claude Code** - Asistente de codificación de IA de Anthropic
- **DeepSeek** - Asistente de codificación de IA DeepSeek
- **Gemini** - Asistente de codificación de IA de Google

Estos asistentes de IA colaboran para mantener el proyecto actualizado, recopilar nuevos proyectos MCP y mantener la calidad de la lista curada.

## 🙏 Contribuir

¡Las contribuciones son bienvenidas! No dude en enviar un Pull Request.

