# Awesome MCP

> Кураторский список потрясающих проектов Model Context Protocol (MCP) с GitHub

[![Auto Update](https://github.com/Rodert/awesome-mcp/workflows/Update%20Projects/badge.svg)](https://github.com/Rodert/awesome-mcp/actions)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

**Languages / 语言 / Языки / 言語 / Langues / Idiomas:**
- [English](README.md) | [中文](README.zh.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Français](README.fr.md) | [Español](README.es.md)

Этот репозиторий автоматически собирает и организует качественные проекты MCP с GitHub, представляя их в красивом, доступном для поиска формате. Список обновляется ежедневно через GitHub Actions и размещается на GitHub Pages.

## 🌐 Языки

- [English](https://rodert.github.io/awesome-mcp/en/projects)
- [中文](https://rodert.github.io/awesome-mcp/zh/projects)
- [Русский](https://rodert.github.io/awesome-mcp/ru/projects)
- [日本語](https://rodert.github.io/awesome-mcp/ja/projects)
- [Français](https://rodert.github.io/awesome-mcp/fr/projects)
- [Español](https://rodert.github.io/awesome-mcp/es/projects)

## 🚀 Быстрый старт: Как использовать MCP в AI-инструментах

Model Context Protocol (MCP) позволяет AI-ассистентам подключаться к внешним источникам данных и инструментам. Вот как настроить MCP в популярных AI-инструментах:

### 📱 Claude Desktop

1. **Найдите файл конфигурации:**
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

2. **Отредактируйте файл конфигурации** и добавьте ваши MCP-серверы:

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

3. **Перезапустите Claude Desktop** для применения изменений.

### 💻 Cursor IDE

1. **Откройте настройки**: `Cmd/Ctrl + ,`
2. **Перейдите в**: Features → Agent → MCP Servers
3. **Нажмите "Add Server"**
4. **Введите данные сервера**:
   - **Имя**: Понятное имя для сервера
   - **Команда**: Команда для запуска (например, `npx`)
   - **Аргументы**: Аргументы команды (например, `["-y", "@modelcontextprotocol/server-github"]`)
   - **Переменные окружения**: Переменные окружения (при необходимости)

### 🔌 Continue (Расширение VS Code)

1. **Установите расширение Continue** из магазина VS Code
2. **Откройте настройки Continue**: Нажмите на иконку Continue в боковой панели
3. **Перейдите в**: Settings → MCP Servers
4. **Добавьте MCP-сервер** в `~/.continue/config.json`:

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

5. **Перезагрузите VS Code** для применения изменений.

### 🔌 Cline (Расширение VS Code)

1. **Установите расширение Cline** из магазина VS Code
2. **Откройте палитру команд**: `Cmd/Ctrl + Shift + P`
3. **Выполните**: `Cline: Configure MCP Servers`
4. **Отредактируйте открывшийся файл конфигурации** или вручную отредактируйте `~/.cline/mcp_config.json`:

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

5. **Перезапустите VS Code** для применения изменений.

### ⚡ Aider (Командная строка)

1. **Установите Aider**: `pip install aider-chat`
2. **Установите переменную окружения** для MCP-серверов:

```bash
export MCP_SERVERS='{"github": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-github"], "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": "your_token"}}}'
```

3. **Или создайте** `~/.aider/mcp_config.json`:

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

4. **Запустите Aider**: `aider` (MCP-серверы будут автоматически загружены)

### 🌊 Windsurf

1. **Откройте настройки Windsurf**: `Cmd/Ctrl + ,`
2. **Перейдите в**: Extensions → MCP
3. **Нажмите "Add MCP Server"**
4. **Настройте сервер**:
   - **Имя**: Идентификатор сервера
   - **Команда**: Команда для выполнения
   - **Аргументы**: Аргументы команды
   - **Переменные окружения**: Переменные окружения
5. **Сохраните и перезапустите** Windsurf

### 🎨 Composer (Anthropic)

1. **Откройте настройки Composer**
2. **Перейдите в**: Settings → Integrations → MCP
3. **Добавьте конфигурацию MCP-сервера**:

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

4. **Перезапустите Composer** для применения изменений.

### 🔍 Поиск MCP-серверов

Просмотрите [список проектов](#-проекты-всего-9) ниже, чтобы найти доступные MCP-серверы. Популярные варианты включают:

- **[GitHub MCP Server](https://github.com/github/github-mcp-server)** - Доступ к репозиториям и задачам GitHub
- **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** - Автоматизация браузера
- **[Filesystem Server](https://github.com/modelcontextprotocol/servers)** - Доступ к файловой системе
- **[SQLite Server](https://github.com/modelcontextprotocol/servers)** - Запросы к базе данных

### 📝 Пример: GitHub MCP Server

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

**Получить GitHub token**: [GitHub Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)

### 🎯 Что может делать MCP?

После настройки MCP позволяет AI-ассистентам:
- 📂 Доступ к файлам и каталогам
- 🔍 Поиск в репозиториях кода
- 🌐 Просмотр веб-страниц
- 💾 Запросы к базам данных
- 📊 Анализ данных
- 🔧 Выполнение инструментов и скриптов

### 📚 Узнать больше

- [Официальная документация MCP](https://modelcontextprotocol.io/)
- [Спецификация MCP](https://github.com/modelcontextprotocol/specification)
- Просмотреть [Коллекцию MCP-серверов](https://github.com/modelcontextprotocol/servers)

### 🔗 Рекомендуемый ресурс

- [silicogrove](https://silicogrove.com/) - Сторонняя универсальная AI-платформа и руководство, объединяющие популярные AI-сервисы и ресурсы в простом едином интерфейсе.
- [ChongPlus Image Studio](https://api.chongplus.plus/tools/image-studio/) - Сторонний онлайн-инструмент генерации изображений с помощью AI для создания изображений в браузере.
- [chongplus-image-skill](https://github.com/Rodert/chongplus-image-skill) - Open-source Agent Skill для генерации и редактирования изображений через ChongPlus API в совместимых AI-агентах.

---

## 📚 Проекты (всего 9)

> Последнее обновление: **2025-11-22**

### MCP Серверы

*Реализации MCP серверов, предоставляющих протокольные услуги*

1. **[dify](https://github.com/langgenius/dify)** - ⭐ 119,501
   Готовая к продакшену платформа для разработки агентных рабочих процессов.

2. **[open-webui](https://github.com/open-webui/open-webui)** - ⭐ 115,900
   Удобный интерфейс AI (поддерживает Ollama, OpenAI API, ...)

3. **[netdata](https://github.com/netdata/netdata)** - ⭐ 76,770
   Самый быстрый путь к полноценной наблюдаемости с поддержкой AI, даже для небольших команд.

4. **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** - ⭐ 75,146
   Коллекция MCP серверов.

5. **[servers](https://github.com/modelcontextprotocol/servers)** - ⭐ 73,079
   Серверы Model Context Protocol

[Просмотреть все 8 →](https://rodert.github.io/awesome-mcp/ru/projects)

### MCP Клиенты

*MCP клиентские приложения, подключающиеся к MCP серверам*

*Скоро...*

### Инструменты и библиотеки

*Инструменты разработки и библиотеки для работы с MCP*

1. **[n8n](https://github.com/n8n-io/n8n)** - ⭐ 157,879
   Платформа автоматизации рабочих процессов с открытым кодом с нативными возможностями AI. Объединяет визуальное построение с пользовательским кодом, самохостинг или облако, 400+ интеграций.

### Примеры

*Примеры проектов, демонстрирующих использование MCP*

*Скоро...*

### Документация

*Документация, учебные пособия и обучающие ресурсы*

*Скоро...*

---

**[Просмотреть полный список проектов на GitHub Pages →](https://rodert.github.io/awesome-mcp/)**

## 📋 Критерии проекта

- ⭐ Не менее 10 звезд
- 📝 Должен иметь файл README
- 🔍 Обнаружен через ключевые слова, темы и теги, связанные с MCP

## 🤖 Автоматизация

Этот репозиторий использует автоматизированные скрипты, которые:

1. **Собирают** проекты ежедневно через GitHub Search API
2. **Категоризируют** проекты по вариантам использования (серверы, клиенты, инструменты, примеры, документация)
3. **Переводят** контент на несколько языков с помощью AI-перевода
4. **Обновляют** сайт автоматически

## 🏗️ Структура

```
awesome-mcp/
├── .github/workflows/    # Автоматизация GitHub Actions
├── scripts/              # Python скрипты для сбора и перевода
├── data/                  # JSON файлы данных
└── docs/                  # Исходные файлы сайта VitePress
```

## 📝 Лицензия

Лицензировано под Apache License 2.0 - подробности см. в файле [LICENSE](LICENSE).

## 👥 Сопровождающие

Этот проект поддерживается AI-ассистентами для программирования:

- **Cursor** - Редактор кода на основе AI
- **Claude Code** - AI-ассистент для программирования от Anthropic
- **DeepSeek** - AI-ассистент для программирования DeepSeek
- **Gemini** - AI-ассистент для программирования от Google

Эти AI-ассистенты сотрудничают, чтобы поддерживать проект в актуальном состоянии, собирать новые проекты MCP и поддерживать качество кураторского списка.

## 🙏 Вклад

Вклад приветствуется! Пожалуйста, не стесняйтесь отправлять Pull Request.
