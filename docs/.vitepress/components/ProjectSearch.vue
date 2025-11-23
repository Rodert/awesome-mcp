<template>
  <div class="project-search">
    <!-- 搜索和筛选栏 -->
    <div class="search-bar">
      <div class="search-input-wrapper">
        <input
          v-model="searchQuery"
          type="text"
          :placeholder="t('searchPlaceholder')"
          class="search-input"
          @input="handleSearch"
        />
        <span class="search-icon">🔍</span>
      </div>
      
      <div class="filters">
        <select v-model="selectedCategory" @change="handleFilter" class="filter-select">
          <option value="">{{ t('allCategories') }}</option>
          <option value="servers">{{ t('servers') }}</option>
          <option value="clients">{{ t('clients') }}</option>
          <option value="tools">{{ t('tools') }}</option>
          <option value="examples">{{ t('examples') }}</option>
          <option value="documentation">{{ t('documentation') }}</option>
        </select>
        
        <select v-model="selectedLanguage" @change="handleFilter" class="filter-select">
          <option value="">{{ t('allLanguages') }}</option>
          <option v-for="lang in availableLanguages" :key="lang" :value="lang">
            {{ lang }}
          </option>
        </select>
        
        <select v-model="sortBy" @change="handleSort" class="filter-select">
          <option value="stars">{{ t('sortByStars') }}</option>
          <option value="updated">{{ t('sortByUpdated') }}</option>
          <option value="name">{{ t('sortByName') }}</option>
        </select>
      </div>
    </div>

    <!-- 统计信息 -->
    <div class="stats">
      <span>{{ t('showing') }} {{ filteredProjects.length }} / {{ totalProjects }} {{ t('projects') }}</span>
      <span v-if="selectedTag" class="tag-filter">
        {{ t('filteredByTag') }}: <strong>{{ selectedTag }}</strong>
        <button @click="clearTagFilter" class="clear-tag">×</button>
      </span>
    </div>

    <!-- 项目列表 -->
    <div v-if="filteredProjects.length > 0" class="projects-grid">
      <div
        v-for="project in filteredProjects"
        :key="project.full_name"
        class="project-card"
      >
        <div class="project-header">
          <h3 class="project-name">
            <a :href="project.url" target="_blank" rel="noopener noreferrer">
              {{ project.name }}
            </a>
          </h3>
          <div class="project-meta">
            <span class="stars">⭐ {{ formatNumber(project.stars) }}</span>
            <span class="language">{{ project.language || 'N/A' }}</span>
          </div>
        </div>
        
        <p class="project-description">{{ project.description }}</p>
        
        <div class="project-tags">
          <span
            v-for="tag in project.topics?.slice(0, 8)"
            :key="tag"
            class="tag"
            @click="filterByTag(tag)"
          >
            {{ tag }}
          </span>
        </div>
        
        <div class="project-footer">
          <span class="category">{{ getCategoryName(project.category) }}</span>
          <span class="updated">{{ formatDate(project.updated_at) }}</span>
        </div>
      </div>
    </div>

    <!-- 无结果 -->
    <div v-else class="no-results">
      <p>{{ t('noResults') }}</p>
      <button @click="clearFilters" class="clear-filters-btn">{{ t('clearFilters') }}</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const props = defineProps({
  lang: {
    type: String,
    default: 'en'
  }
})

// 翻译文本
const translations = {
  en: {
    searchPlaceholder: 'Search projects by name, description, or tags...',
    allCategories: 'All Categories',
    servers: 'MCP Servers',
    clients: 'MCP Clients',
    tools: 'Tools & Libraries',
    examples: 'Examples',
    documentation: 'Documentation',
    allLanguages: 'All Languages',
    sortByStars: 'Sort by Stars',
    sortByUpdated: 'Sort by Updated',
    sortByName: 'Sort by Name',
    showing: 'Showing',
    projects: 'projects',
    filteredByTag: 'Filtered by tag',
    noResults: 'No projects found matching your criteria.',
    clearFilters: 'Clear all filters'
  },
  zh: {
    searchPlaceholder: '按名称、描述或标签搜索项目...',
    allCategories: '所有分类',
    servers: 'MCP 服务器',
    clients: 'MCP 客户端',
    tools: '工具和库',
    examples: '示例',
    documentation: '文档',
    allLanguages: '所有语言',
    sortByStars: '按星标排序',
    sortByUpdated: '按更新排序',
    sortByName: '按名称排序',
    showing: '显示',
    projects: '个项目',
    filteredByTag: '按标签筛选',
    noResults: '未找到匹配的项目。',
    clearFilters: '清除所有筛选'
  },
  ru: {
    searchPlaceholder: 'Поиск проектов по названию, описанию или тегам...',
    allCategories: 'Все категории',
    servers: 'MCP Серверы',
    clients: 'MCP Клиенты',
    tools: 'Инструменты и библиотеки',
    examples: 'Примеры',
    documentation: 'Документация',
    allLanguages: 'Все языки',
    sortByStars: 'Сортировать по звездам',
    sortByUpdated: 'Сортировать по обновлению',
    sortByName: 'Сортировать по имени',
    showing: 'Показано',
    projects: 'проектов',
    filteredByTag: 'Отфильтровано по тегу',
    noResults: 'Проекты не найдены.',
    clearFilters: 'Очистить все фильтры'
  },
  ja: {
    searchPlaceholder: '名前、説明、またはタグでプロジェクトを検索...',
    allCategories: 'すべてのカテゴリ',
    servers: 'MCP サーバー',
    clients: 'MCP クライアント',
    tools: 'ツールとライブラリ',
    examples: '例',
    documentation: 'ドキュメント',
    allLanguages: 'すべての言語',
    sortByStars: 'スターで並べ替え',
    sortByUpdated: '更新で並べ替え',
    sortByName: '名前で並べ替え',
    showing: '表示中',
    projects: 'プロジェクト',
    filteredByTag: 'タグでフィルタ',
    noResults: '一致するプロジェクトが見つかりません。',
    clearFilters: 'すべてのフィルタをクリア'
  },
  fr: {
    searchPlaceholder: 'Rechercher des projets par nom, description ou tags...',
    allCategories: 'Toutes les catégories',
    servers: 'Serveurs MCP',
    clients: 'Clients MCP',
    tools: 'Outils et bibliothèques',
    examples: 'Exemples',
    documentation: 'Documentation',
    allLanguages: 'Toutes les langues',
    sortByStars: 'Trier par étoiles',
    sortByUpdated: 'Trier par mise à jour',
    sortByName: 'Trier par nom',
    showing: 'Affichage',
    projects: 'projets',
    filteredByTag: 'Filtré par tag',
    noResults: 'Aucun projet trouvé.',
    clearFilters: 'Effacer tous les filtres'
  },
  es: {
    searchPlaceholder: 'Buscar proyectos por nombre, descripción o etiquetas...',
    allCategories: 'Todas las categorías',
    servers: 'Servidores MCP',
    clients: 'Clientes MCP',
    tools: 'Herramientas y bibliotecas',
    examples: 'Ejemplos',
    documentation: 'Documentación',
    allLanguages: 'Todos los idiomas',
    sortByStars: 'Ordenar por estrellas',
    sortByUpdated: 'Ordenar por actualización',
    sortByName: 'Ordenar por nombre',
    showing: 'Mostrando',
    projects: 'proyectos',
    filteredByTag: 'Filtrado por etiqueta',
    noResults: 'No se encontraron proyectos.',
    clearFilters: 'Limpiar todos los filtros'
  }
}

const t = (key) => translations[props.lang]?.[key] || translations.en[key]

// 数据
const projects = ref([])
const searchQuery = ref('')
const selectedCategory = ref('')
const selectedLanguage = ref('')
const selectedTag = ref('')
const sortBy = ref('stars')

// 计算属性
const totalProjects = computed(() => projects.value.length)

const availableLanguages = computed(() => {
  const langs = new Set()
  projects.value.forEach(p => {
    if (p.language && p.language !== 'N/A') {
      langs.add(p.language)
    }
  })
  return Array.from(langs).sort()
})

const filteredProjects = computed(() => {
  let result = [...projects.value]

  // 搜索过滤
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    result = result.filter(p => {
      return (
        p.name.toLowerCase().includes(query) ||
        p.description.toLowerCase().includes(query) ||
        p.full_name.toLowerCase().includes(query) ||
        (p.topics && p.topics.some(t => t.toLowerCase().includes(query)))
      )
    })
  }

  // 分类过滤
  if (selectedCategory.value) {
    result = result.filter(p => p.category === selectedCategory.value)
  }

  // 语言过滤
  if (selectedLanguage.value) {
    result = result.filter(p => p.language === selectedLanguage.value)
  }

  // 标签过滤
  if (selectedTag.value) {
    result = result.filter(p => 
      p.topics && p.topics.some(t => t.toLowerCase() === selectedTag.value.toLowerCase())
    )
  }

  // 排序
  result.sort((a, b) => {
    if (sortBy.value === 'stars') {
      return b.stars - a.stars
    } else if (sortBy.value === 'updated') {
      return new Date(b.updated_at) - new Date(a.updated_at)
    } else if (sortBy.value === 'name') {
      return a.name.localeCompare(b.name)
    }
    return 0
  })

  return result
})

// 方法
const loadProjects = async () => {
  try {
    // 根据当前路径确定数据文件位置
    const basePath = import.meta.env.BASE_URL || '/awesome-mcp/'
    const possiblePaths = [
      `${basePath}data/projects.json`,
      '/awesome-mcp/data/projects.json',
      './data/projects.json',
      '../data/projects.json',
      '/data/projects.json'
    ]
    
    let loaded = false
    for (const path of possiblePaths) {
      try {
        const response = await fetch(path)
        if (response.ok) {
          const data = await response.json()
          projects.value = data.projects || []
          loaded = true
          console.log(`✓ Loaded ${projects.value.length} projects from ${path}`)
          break
        }
      } catch (e) {
        // 继续尝试下一个路径
        continue
      }
    }
    
    if (!loaded) {
      console.error('Failed to load projects from all paths:', possiblePaths)
    }
  } catch (error) {
    console.error('Failed to load projects:', error)
  }
}

const handleSearch = () => {
  // 搜索是响应式的，不需要额外处理
}

const handleFilter = () => {
  // 过滤是响应式的，不需要额外处理
}

const handleSort = () => {
  // 排序是响应式的，不需要额外处理
}

const filterByTag = (tag) => {
  selectedTag.value = tag
  searchQuery.value = ''
}

const clearTagFilter = () => {
  selectedTag.value = ''
}

const clearFilters = () => {
  searchQuery.value = ''
  selectedCategory.value = ''
  selectedLanguage.value = ''
  selectedTag.value = ''
}

const formatNumber = (num) => {
  return num.toLocaleString()
}

const formatDate = (dateStr) => {
  try {
    const date = new Date(dateStr)
    return date.toLocaleDateString(props.lang === 'zh' ? 'zh-CN' : 'en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    })
  } catch {
    return dateStr
  }
}

const getCategoryName = (category) => {
  const names = {
    servers: t('servers'),
    clients: t('clients'),
    tools: t('tools'),
    examples: t('examples'),
    documentation: t('documentation')
  }
  return names[category] || category
}

onMounted(() => {
  loadProjects()
})
</script>

<style scoped>
.project-search {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.search-bar {
  margin-bottom: 2rem;
}

.search-input-wrapper {
  position: relative;
  margin-bottom: 1rem;
}

.search-input {
  width: 100%;
  padding: 1rem 3rem 1rem 1rem;
  font-size: 1.1rem;
  border: 2px solid var(--vp-c-divider);
  border-radius: 8px;
  transition: border-color 0.3s;
}

.search-input:focus {
  outline: none;
  border-color: var(--vp-c-brand);
}

.search-icon {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  font-size: 1.2rem;
}

.filters {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.filter-select {
  padding: 0.5rem 1rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  cursor: pointer;
  font-size: 0.9rem;
}

.stats {
  margin-bottom: 1.5rem;
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.tag-filter {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.25rem 0.75rem;
  background: var(--vp-c-brand-soft);
  border-radius: 4px;
}

.clear-tag {
  background: none;
  border: none;
  font-size: 1.2rem;
  cursor: pointer;
  color: var(--vp-c-text-2);
  padding: 0;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.clear-tag:hover {
  color: var(--vp-c-text-1);
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem;
}

.project-card {
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 1.5rem;
  transition: transform 0.2s, box-shadow 0.2s;
  background: var(--vp-c-bg);
}

.project-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
  gap: 1rem;
}

.project-name {
  margin: 0;
  font-size: 1.2rem;
  flex: 1;
}

.project-name a {
  color: var(--vp-c-brand);
  text-decoration: none;
}

.project-name a:hover {
  text-decoration: underline;
}

.project-meta {
  display: flex;
  gap: 0.75rem;
  font-size: 0.9rem;
  color: var(--vp-c-text-2);
  white-space: nowrap;
}

.stars {
  font-weight: 600;
}

.project-description {
  color: var(--vp-c-text-2);
  line-height: 1.6;
  margin-bottom: 1rem;
  font-size: 0.95rem;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.tag {
  padding: 0.25rem 0.75rem;
  background: var(--vp-c-bg-soft);
  border-radius: 4px;
  font-size: 0.85rem;
  color: var(--vp-c-text-2);
  cursor: pointer;
  transition: background 0.2s;
}

.tag:hover {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand);
}

.project-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
  color: var(--vp-c-text-3);
  padding-top: 1rem;
  border-top: 1px solid var(--vp-c-divider);
}

.category {
  font-weight: 500;
}

.no-results {
  text-align: center;
  padding: 3rem;
  color: var(--vp-c-text-2);
}

.clear-filters-btn {
  margin-top: 1rem;
  padding: 0.5rem 1.5rem;
  background: var(--vp-c-brand);
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: background 0.2s;
}

.clear-filters-btn:hover {
  background: var(--vp-c-brand-dark);
}

@media (max-width: 768px) {
  .projects-grid {
    grid-template-columns: 1fr;
  }
  
  .filters {
    flex-direction: column;
  }
  
  .filter-select {
    width: 100%;
  }
}
</style>

