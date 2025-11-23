<template>
  <div class="project-search">
    <!-- 搜索和筛选栏 -->
    <div class="search-section">
      <div class="search-bar-wrapper">
        <div class="search-input-wrapper" :class="{ 'search-focused': isSearchFocused }">
          <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8"></circle>
            <path d="m21 21-4.35-4.35"></path>
          </svg>
          <input
            v-model="searchQuery"
            type="text"
            :placeholder="t('searchPlaceholder')"
            class="search-input"
            @input="handleSearch"
            @focus="isSearchFocused = true"
            @blur="isSearchFocused = false"
          />
          <button v-if="searchQuery" @click="clearSearch" class="clear-search">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>
      </div>
      
      <div class="filters-wrapper">
        <div class="filter-group">
          <select v-model="selectedCategory" @change="handleFilter" class="filter-select">
            <option value="">{{ t('allCategories') }}</option>
            <option value="servers">{{ t('servers') }}</option>
            <option value="clients">{{ t('clients') }}</option>
            <option value="tools">{{ t('tools') }}</option>
            <option value="examples">{{ t('examples') }}</option>
            <option value="documentation">{{ t('documentation') }}</option>
          </select>
        </div>
        
        <div class="filter-group">
          <select v-model="selectedLanguage" @change="handleFilter" class="filter-select">
            <option value="">{{ t('allLanguages') }}</option>
            <option v-for="lang in availableLanguages" :key="lang" :value="lang">
              {{ lang }}
            </option>
          </select>
        </div>
        
        <div class="filter-group">
          <select v-model="sortBy" @change="handleSort" class="filter-select">
            <option value="stars">{{ t('sortByStars') }}</option>
            <option value="updated">{{ t('sortByUpdated') }}</option>
            <option value="name">{{ t('sortByName') }}</option>
          </select>
        </div>
      </div>
    </div>

    <!-- 统计信息和活动筛选标签 -->
    <div class="stats-section">
      <div class="stats-info">
        <span class="stats-text">
          <span class="stats-highlight">{{ filteredProjects.length }}</span>
          / {{ totalProjects }} {{ t('projects') }}
        </span>
        <span v-if="selectedTag" class="active-tag">
          {{ t('filteredByTag') }}: <strong>{{ selectedTag }}</strong>
          <button @click="clearTagFilter" class="tag-close">×</button>
        </span>
      </div>
    </div>

    <!-- 加载状态 -->
    <div v-if="loading" class="loading-container">
      <div class="loading-spinner"></div>
      <p>{{ t('loading') }}</p>
    </div>

    <!-- 项目列表 -->
    <transition-group 
      v-else-if="filteredProjects.length > 0" 
      name="project-list" 
      tag="div" 
      class="projects-grid"
    >
      <div
        v-for="(project, index) in filteredProjects"
        :key="project.full_name"
        class="project-card"
        :style="{ 'animation-delay': `${index * 0.05}s` }"
      >
        <div class="card-gradient"></div>
        <div class="card-content">
          <div class="project-header">
            <div class="project-title-wrapper">
              <h3 class="project-name">
                <a :href="project.url" target="_blank" rel="noopener noreferrer">
                  {{ project.name }}
                  <svg class="external-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                    <polyline points="15 3 21 3 21 9"></polyline>
                    <line x1="10" y1="14" x2="21" y2="3"></line>
                  </svg>
                </a>
              </h3>
              <span class="project-owner">{{ project.owner }}</span>
            </div>
            <div class="project-meta">
              <span class="stars-badge">
                <svg class="star-icon" viewBox="0 0 24 24" fill="currentColor">
                  <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                </svg>
                {{ formatNumber(project.stars) }}
              </span>
              <span class="language-badge" :style="{ '--lang-color': getLanguageColor(project.language) }">
                {{ project.language || 'N/A' }}
              </span>
            </div>
          </div>
          
          <p class="project-description">{{ project.description }}</p>
          
          <div class="project-tags">
            <span
              v-for="tag in project.topics?.slice(0, 10)"
              :key="tag"
              class="tag"
              @click="filterByTag(tag)"
              :class="{ 'tag-active': selectedTag === tag }"
            >
              {{ tag }}
            </span>
          </div>
          
          <div class="project-footer">
            <span class="category-badge">{{ getCategoryName(project.category) }}</span>
            <span class="updated-text">{{ formatDate(project.updated_at) }}</span>
          </div>
        </div>
      </div>
    </transition-group>

    <!-- 无结果 -->
    <div v-else-if="!loading" class="no-results">
      <div class="no-results-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <circle cx="11" cy="11" r="8"></circle>
          <path d="m21 21-4.35-4.35"></path>
        </svg>
      </div>
      <p class="no-results-text">{{ t('noResults') }}</p>
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
    clearFilters: 'Clear all filters',
    loading: 'Loading projects...'
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
    clearFilters: '清除所有筛选',
    loading: '正在加载项目...'
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
    clearFilters: 'Очистить все фильтры',
    loading: 'Загрузка проектов...'
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
    clearFilters: 'すべてのフィルタをクリア',
    loading: 'プロジェクトを読み込み中...'
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
    clearFilters: 'Effacer tous les filtres',
    loading: 'Chargement des projets...'
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
    clearFilters: 'Limpiar todos los filtros',
    loading: 'Cargando proyectos...'
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
const loading = ref(true)
const isSearchFocused = ref(false)

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
  loading.value = true
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
          // 添加小延迟让加载动画更流畅
          await new Promise(resolve => setTimeout(resolve, 300))
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
  } finally {
    loading.value = false
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

const clearSearch = () => {
  searchQuery.value = ''
}

const clearFilters = () => {
  searchQuery.value = ''
  selectedCategory.value = ''
  selectedLanguage.value = ''
  selectedTag.value = ''
}

const getLanguageColor = (language) => {
  const colors = {
    'TypeScript': '#3178c6',
    'JavaScript': '#f7df1e',
    'Python': '#3776ab',
    'Java': '#ed8b00',
    'Go': '#00add8',
    'C': '#a8b9cc',
    'C++': '#00599c',
    'Rust': '#000000',
    'Ruby': '#cc342d',
    'PHP': '#777bb4',
    'Swift': '#fa7343',
    'Kotlin': '#7f52ff',
    'Dart': '#0175c2',
    'Lua': '#000080',
    'N/A': '#6b7280'
  }
  return colors[language] || '#6b7280'
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
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
}

/* 搜索区域 */
.search-section {
  margin-bottom: 2rem;
}

.search-bar-wrapper {
  margin-bottom: 1.5rem;
}

.search-input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  background: var(--vp-c-bg-soft);
  border: 2px solid var(--vp-c-divider);
  border-radius: 16px;
  padding: 0.75rem 1rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.search-input-wrapper.search-focused {
  border-color: var(--vp-c-brand);
  box-shadow: 0 4px 20px rgba(82, 159, 255, 0.15);
  background: var(--vp-c-bg);
}

.search-icon {
  width: 20px;
  height: 20px;
  color: var(--vp-c-text-2);
  margin-right: 0.75rem;
  flex-shrink: 0;
  transition: color 0.3s;
}

.search-input-wrapper.search-focused .search-icon {
  color: var(--vp-c-brand);
}

.search-input {
  flex: 1;
  border: none;
  outline: none;
  background: transparent;
  font-size: 1rem;
  color: var(--vp-c-text-1);
  padding: 0;
}

.search-input::placeholder {
  color: var(--vp-c-text-3);
}

.clear-search {
  background: none;
  border: none;
  padding: 0.25rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--vp-c-text-3);
  transition: all 0.2s;
  border-radius: 4px;
  margin-left: 0.5rem;
}

.clear-search:hover {
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg-alt);
}

.clear-search svg {
  width: 16px;
  height: 16px;
}

.filters-wrapper {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.filter-group {
  flex: 1;
  min-width: 150px;
}

.filter-select {
  width: 100%;
  padding: 0.625rem 1rem;
  border: 1.5px solid var(--vp-c-divider);
  border-radius: 10px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.2s;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%23666' d='M6 9L1 4h10z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 0.75rem center;
  padding-right: 2.5rem;
}

.filter-select:hover {
  border-color: var(--vp-c-brand-light);
  background: var(--vp-c-bg);
}

.filter-select:focus {
  outline: none;
  border-color: var(--vp-c-brand);
  box-shadow: 0 0 0 3px rgba(82, 159, 255, 0.1);
}

/* 统计区域 */
.stats-section {
  margin-bottom: 2rem;
}

.stats-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.stats-text {
  font-size: 0.95rem;
  color: var(--vp-c-text-2);
}

.stats-highlight {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--vp-c-brand);
}

.active-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: linear-gradient(135deg, var(--vp-c-brand-soft), var(--vp-c-brand-soft));
  border-radius: 20px;
  font-size: 0.85rem;
  color: var(--vp-c-text-1);
  animation: tagSlideIn 0.3s ease-out;
}

@keyframes tagSlideIn {
  from {
    opacity: 0;
    transform: translateX(-10px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.tag-close {
  background: none;
  border: none;
  font-size: 1.25rem;
  line-height: 1;
  cursor: pointer;
  color: var(--vp-c-text-2);
  padding: 0;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: all 0.2s;
}

.tag-close:hover {
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
}

/* 加载动画 */
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  gap: 1rem;
}

.loading-spinner {
  width: 48px;
  height: 48px;
  border: 4px solid var(--vp-c-divider);
  border-top-color: var(--vp-c-brand);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* 项目网格 */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
  gap: 1.75rem;
}

/* 项目卡片 */
.project-card {
  position: relative;
  background: var(--vp-c-bg);
  border: 1.5px solid var(--vp-c-divider);
  border-radius: 16px;
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  animation: cardFadeIn 0.5s ease-out backwards;
  cursor: pointer;
}

@keyframes cardFadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.project-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--vp-c-brand), var(--vp-c-brand-light));
  opacity: 0;
  transition: opacity 0.3s;
}

.project-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
  border-color: var(--vp-c-brand-light);
}

.project-card:hover::before {
  opacity: 1;
}

.card-gradient {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(135deg, rgba(82, 159, 255, 0.05), rgba(82, 159, 255, 0.02));
  opacity: 0;
  transition: opacity 0.3s;
  pointer-events: none;
}

.project-card:hover .card-gradient {
  opacity: 1;
}

.card-content {
  position: relative;
  padding: 1.75rem;
  z-index: 1;
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
  gap: 1rem;
}

.project-title-wrapper {
  flex: 1;
  min-width: 0;
}

.project-name {
  margin: 0 0 0.25rem 0;
  font-size: 1.25rem;
  font-weight: 700;
  line-height: 1.4;
}

.project-name a {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--vp-c-text-1);
  text-decoration: none;
  transition: color 0.2s;
}

.project-name a:hover {
  color: var(--vp-c-brand);
}

.external-icon {
  width: 14px;
  height: 14px;
  opacity: 0.5;
  transition: all 0.2s;
}

.project-name a:hover .external-icon {
  opacity: 1;
  transform: translate(2px, -2px);
}

.project-owner {
  font-size: 0.85rem;
  color: var(--vp-c-text-3);
  font-weight: 500;
}

.project-meta {
  display: flex;
  gap: 0.75rem;
  flex-shrink: 0;
  align-items: center;
}

.stars-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  padding: 0.375rem 0.75rem;
  background: var(--vp-c-bg-soft);
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
}

.star-icon {
  width: 14px;
  height: 14px;
  color: #fbbf24;
  fill: currentColor;
}

.language-badge {
  padding: 0.375rem 0.75rem;
  background: var(--vp-c-bg-soft);
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
  border-left: 3px solid var(--lang-color);
}

.project-description {
  color: var(--vp-c-text-2);
  line-height: 1.7;
  margin-bottom: 1.25rem;
  font-size: 0.95rem;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.25rem;
}

.tag {
  padding: 0.375rem 0.875rem;
  background: var(--vp-c-bg-soft);
  border-radius: 8px;
  font-size: 0.8rem;
  color: var(--vp-c-text-2);
  cursor: pointer;
  transition: all 0.2s;
  border: 1px solid transparent;
  font-weight: 500;
}

.tag:hover {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand);
  border-color: var(--vp-c-brand-light);
  transform: translateY(-1px);
}

.tag-active {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand);
  border-color: var(--vp-c-brand);
  font-weight: 600;
}

.project-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 1rem;
  border-top: 1px solid var(--vp-c-divider);
  gap: 1rem;
}

.category-badge {
  padding: 0.375rem 0.875rem;
  background: var(--vp-c-bg-soft);
  border-radius: 8px;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--vp-c-text-2);
}

.updated-text {
  font-size: 0.8rem;
  color: var(--vp-c-text-3);
  white-space: nowrap;
}

/* 列表过渡动画 */
.project-list-enter-active,
.project-list-leave-active {
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.project-list-enter-from {
  opacity: 0;
  transform: translateY(30px) scale(0.95);
}

.project-list-leave-to {
  opacity: 0;
  transform: translateY(-30px) scale(0.95);
}

.project-list-move {
  transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

/* 无结果 */
.no-results {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  text-align: center;
}

.no-results-icon {
  width: 80px;
  height: 80px;
  margin-bottom: 1.5rem;
  color: var(--vp-c-text-3);
  opacity: 0.5;
}

.no-results-icon svg {
  width: 100%;
  height: 100%;
}

.no-results-text {
  font-size: 1.1rem;
  color: var(--vp-c-text-2);
  margin-bottom: 1.5rem;
}

.clear-filters-btn {
  padding: 0.75rem 2rem;
  background: linear-gradient(135deg, var(--vp-c-brand), var(--vp-c-brand-light, #529fff));
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-size: 0.95rem;
  font-weight: 600;
  transition: all 0.3s;
  box-shadow: 0 4px 12px rgba(82, 159, 255, 0.3);
}

.clear-filters-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(82, 159, 255, 0.4);
}

.clear-filters-btn:active {
  transform: translateY(0);
}

/* 响应式设计 */
@media (max-width: 960px) {
  .projects-grid {
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 1.5rem;
  }
}

@media (max-width: 768px) {
  .project-search {
    padding: 1.5rem 1rem;
  }

  .projects-grid {
    grid-template-columns: 1fr;
    gap: 1.25rem;
  }

  .filters-wrapper {
    flex-direction: column;
  }

  .filter-group {
    width: 100%;
  }

  .search-input-wrapper {
    padding: 0.625rem 0.875rem;
  }

  .card-content {
    padding: 1.5rem;
  }

  .project-header {
    flex-direction: column;
    gap: 0.75rem;
  }

  .project-meta {
    width: 100%;
    justify-content: flex-start;
  }
}

@media (max-width: 480px) {
  .project-name {
    font-size: 1.1rem;
  }

  .project-description {
    font-size: 0.9rem;
  }
}
</style>

