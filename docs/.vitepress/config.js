import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Awesome MCP',
  description: 'A curated list of awesome Model Context Protocol (MCP) projects from GitHub',
  
  base: '/awesome-mcp/',  // GitHub Pages base path
  
  markdown: {
    links: {
      externalLinkIcon: true
    }
  },
  
  ignoreDeadLinks: true,
  
  // 确保静态资源可以被访问
  vite: {
    publicDir: 'public'
  },
  
  head: [
    ['link', { rel: 'icon', href: '/awesome-mcp/favicon.ico' }],
    ['meta', { name: 'keywords', content: 'MCP, Model Context Protocol, awesome, awesome-list' }]
  ],
  
  themeConfig: {
    // logo: '/awesome-mcp/logo.svg',  // 可以添加 logo
    
    nav: [
      { 
        text: '🌐 Languages', 
        items: [
          { text: 'English', link: '/awesome-mcp/en/projects' },
          { text: '中文', link: '/awesome-mcp/zh/projects' },
          { text: 'Русский', link: '/awesome-mcp/ru/projects' },
          { text: '日本語', link: '/awesome-mcp/ja/projects' },
          { text: 'Français', link: '/awesome-mcp/fr/projects' },
          { text: 'Español', link: '/awesome-mcp/es/projects' }
        ]
      },
      { text: 'GitHub', link: 'https://github.com/Rodert/awesome-mcp' }
    ],
    
    sidebar: {
      '/en/': [
        {
          text: 'Projects',
          link: '/en/projects'
        }
      ],
      '/zh/': [
        {
          text: '项目',
          link: '/zh/projects'
        }
      ],
      '/ru/': [
        {
          text: 'Проекты',
          link: '/ru/projects'
        }
      ],
      '/ja/': [
        {
          text: 'プロジェクト',
          link: '/ja/projects'
        }
      ],
      '/fr/': [
        {
          text: 'Projets',
          link: '/fr/projects'
        }
      ],
      '/es/': [
        {
          text: 'Proyectos',
          link: '/es/projects'
        }
      ]
    },
    
    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: 'Search',
            buttonAriaLabel: 'Search'
          },
          modal: {
            noResultsText: 'No results found',
            resetButtonTitle: 'Reset search',
            footer: {
              selectText: 'to select',
              navigateText: 'to navigate',
              closeText: 'to close'
            }
          }
        }
      }
    },
    
    socialLinks: [
      { icon: 'github', link: 'https://github.com/Rodert/awesome-mcp' }
    ],
    
    footer: {
      message: 'Made with ❤️ for the MCP community',
      copyright: 'Copyright © 2024 Awesome MCP Contributors'
    },
    
    editLink: {
      pattern: 'https://github.com/Rodert/awesome-mcp/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    },
    
    lastUpdated: {
      text: 'Last updated'
    }
  }
})

