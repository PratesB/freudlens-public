<template>
  <div class="flex flex-col items-center justify-center min-h-[70vh] px-4 w-full pb-32">
    <!-- Loading State -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center space-y-4">
      <div class="w-12 h-12 rounded-full border-2 border-slate-700 border-t-blue-500 animate-spin"></div>
      <p class="text-slate-400 font-light tracking-widest text-sm uppercase">Preparing the couch...</p>
    </div>

    <!-- Main Container -->
    <div v-else-if="themes.length > 0" class="w-full max-w-4xl relative">
      
      <!-- Progress Bar Area -->
      <div class="mb-8">
        <div class="flex justify-between items-end mb-2">
          <span class="text-slate-400 text-xs font-light uppercase tracking-wider">Progress</span>
          <span class="font-medium text-sm transition-colors duration-500" :class="currentPalette.textPrimary">{{ currentThemeIndex + 1 }} / {{ themes.length }}</span>
        </div>
        <div class="w-full h-1 bg-slate-800 rounded-full overflow-hidden">
          <div 
            class="h-full transition-all duration-500 ease-out bg-gradient-to-r"
            :class="currentPalette.progress"
            :style="{ width: `${((currentThemeIndex + 1) / themes.length) * 100}%` }"
          ></div>
        </div>
      </div>

      <!-- Content Card -->
      <div 
        class="w-full p-8 md:p-10 backdrop-blur-xl bg-[#03091e]/80 border rounded-2xl shadow-[0_10px_40px_rgba(0,0,0,0.8)] relative overflow-hidden transition-all duration-500"
        :class="currentPalette.border"
      >
        <!-- Subtle top glow -->
        <div 
          class="absolute top-0 left-1/4 w-1/2 h-[1px] bg-gradient-to-r from-transparent to-transparent transition-all duration-500"
          :class="currentPalette.glow"
        ></div>

        <div class="mb-8">
          <h2 
            class="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r mb-3 drop-shadow-md transition-all duration-500"
            :class="currentPalette.textGradient"
          >
            {{ currentTheme.subject }}
          </h2>
          <p class="text-slate-400 text-sm font-light leading-relaxed">
            Take your time. Answer honestly and spontaneously.
          </p>
        </div>

        <div class="space-y-8">
          <div v-for="(q, index) in currentTheme.questions" :key="q.id" class="group">
            <label 
              :for="`q-${q.id}`" 
              class="block text-slate-200 text-lg mb-4 leading-relaxed font-medium transition-colors duration-500"
              :class="currentPalette.hoverText"
            >
              {{ q.text }}
            </label>
            <div class="relative">
              <textarea
                :id="`q-${q.id}`"
                v-model="answersMap[q.id]"
                rows="4"
                class="w-full bg-[#020617]/50 border border-slate-700/50 text-slate-100 rounded-xl px-5 pt-4 pb-10 transition-all duration-500 outline-none shadow-inner placeholder:text-slate-600 resize-none font-light leading-relaxed focus:ring-2"
                :class="currentPalette.focus"
                placeholder="Write your thoughts here..."
              ></textarea>
              
              <!-- Integrated Word Counter -->
              <div class="absolute bottom-3 right-5 flex items-center pointer-events-none">
                <span class="text-[10px] uppercase tracking-widest font-medium transition-colors duration-500" 
                      :class="getWordCount(answersMap[q.id]) >= 20 ? currentPalette.textPrimary : 'text-slate-500'">
                  {{ getWordCount(answersMap[q.id]) }} <span class="text-[9px] opacity-70">words</span>
                  <span v-if="getWordCount(answersMap[q.id]) < 20" class="lowercase tracking-wide font-normal ml-1 opacity-50">(aim for 20+)</span>
                  <span v-else class="ml-1 opacity-90">- Optimal Depth</span>
                </span>
              </div>
              
              <!-- Subtle Progress Bar overlaying the bottom inside the textarea -->
              <div class="absolute bottom-[1px] left-[1px] right-[1px] h-[3px] rounded-b-xl overflow-hidden pointer-events-none z-10">
                 <div class="h-full transition-all duration-500 ease-out bg-gradient-to-r opacity-80" 
                      :class="currentPalette.progress"
                      :style="{ width: `${Math.min((getWordCount(answersMap[q.id]) / 20) * 100, 100)}%` }">
                 </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Validation Error Message -->
        <div v-if="showError" class="mt-6 text-red-400 text-sm font-medium animate-pulse text-center">
          Please answer all questions before proceeding.
        </div>

        <!-- Navigation Buttons -->
        <div class="mt-10 flex justify-between items-center pt-6 border-t border-slate-800/50">
          <button 
            type="button"
            @click="prevTheme"
            :class="currentThemeIndex === 0 ? 'invisible' : 'visible'"
            class="px-6 py-3 text-slate-400 hover:text-slate-200 transition-colors text-sm uppercase tracking-widest font-medium cursor-pointer"
          >
            Previous
          </button>

          <button 
            v-if="!isLastTheme"
            type="button"
            @click="handleNext"
            class="relative py-3.5 px-8 bg-[#03091e] hover:bg-slate-900/80 text-slate-100 font-medium tracking-[0.15em] uppercase text-sm rounded-xl transition-all duration-500 border group flex items-center gap-3 overflow-hidden shadow-lg cursor-pointer"
            :class="[currentPalette.buttonBorder, currentPalette.buttonShadow]"
          >
            <!-- Background hover gradient -->
            <div class="absolute inset-0 bg-gradient-to-r opacity-0 group-hover:opacity-10 transition-opacity duration-300" :class="currentPalette.progress"></div>
            
            <span class="relative z-10">Next</span>
            <svg class="relative z-10 w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" :class="currentPalette.textPrimary" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
          </button>

          <!-- Grand Submit Button (HomeHero style) -->
          <div v-else class="group/button relative rounded-full p-[2px] overflow-hidden shadow-[0_10px_40px_rgba(0,0,0,0.8)] hover:shadow-[0_10px_40px_rgba(59,130,246,0.2)] transition-shadow duration-500 cursor-pointer">
            <!-- Spinning light border -->
            <div class="absolute top-1/2 left-1/2 w-[400%] aspect-square -translate-x-1/2 -translate-y-1/2 animate-[spin_3s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,transparent_0%,#3b82f6_50%,transparent_100%)] opacity-30 group-hover/button:opacity-80 transition-opacity duration-500 pointer-events-none"></div>

            <button 
              type="button"
              @click="handleNext"
              class="cursor-pointer group relative overflow-hidden px-10 py-4 w-full h-full rounded-full bg-[#03091e] transition-colors duration-500 flex items-center justify-center"
            >
              <!-- Idle scanning light -->
              <div class="absolute pointer-events-none rounded-full bg-blue-500/40 blur-[30px] w-32 h-full top-0 animate-idle-scan group-hover:opacity-0 transition-opacity duration-500"></div>
              
              <!-- Button Text -->
              <span class="relative z-10 text-white font-light tracking-[0.25em] uppercase text-sm flex items-center gap-4 drop-shadow-md">
                Submit Analysis
                <svg class="transition-transform duration-500 group-hover:scale-110 text-blue-400" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="m9 11 3 3L22 4"/></svg>
              </span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { apiService } from '../../services/api'

const emit = defineEmits(['completed'])

const isLoading = ref(true)
const themes = ref([])
const currentThemeIndex = ref(0)
const answersMap = ref({}) // map of questionId -> answer text
const showError = ref(false)

// Palettes for different themes to give visual feedback on progress
const themePalettes = [
  // 1. Structure of Personality (Blue)
  { textPrimary: 'text-blue-400', textGradient: 'from-blue-300 to-blue-600', border: 'border-blue-500/20', focus: 'focus:ring-blue-500/50 focus:border-blue-500/50', progress: 'from-blue-600 to-blue-400', glow: 'via-blue-500/50', hoverText: 'group-hover:text-blue-300', buttonBorder: 'border-blue-500/30 hover:border-blue-500', buttonShadow: 'shadow-[0_0_20px_rgba(59,130,246,0.1)] hover:shadow-[0_0_30px_rgba(59,130,246,0.2)]' },
  // 2. Psychosexual Development (Rose)
  { textPrimary: 'text-rose-400', textGradient: 'from-rose-300 to-rose-600', border: 'border-rose-500/20', focus: 'focus:ring-rose-500/50 focus:border-rose-500/50', progress: 'from-rose-600 to-rose-400', glow: 'via-rose-500/50', hoverText: 'group-hover:text-rose-300', buttonBorder: 'border-rose-500/30 hover:border-rose-500', buttonShadow: 'shadow-[0_0_20px_rgba(244,63,94,0.1)] hover:shadow-[0_0_30px_rgba(244,63,94,0.2)]' },
  // 3. Defense Mechanisms (Emerald)
  { textPrimary: 'text-emerald-400', textGradient: 'from-emerald-300 to-emerald-600', border: 'border-emerald-500/20', focus: 'focus:ring-emerald-500/50 focus:border-emerald-500/50', progress: 'from-emerald-600 to-emerald-400', glow: 'via-emerald-500/50', hoverText: 'group-hover:text-emerald-300', buttonBorder: 'border-emerald-500/30 hover:border-emerald-500', buttonShadow: 'shadow-[0_0_20px_rgba(16,185,129,0.1)] hover:shadow-[0_0_30px_rgba(16,185,129,0.2)]' },
  // 4. Unconscious and Dreams (Indigo)
  { textPrimary: 'text-indigo-400', textGradient: 'from-indigo-300 to-indigo-600', border: 'border-indigo-500/20', focus: 'focus:ring-indigo-500/50 focus:border-indigo-500/50', progress: 'from-indigo-600 to-indigo-400', glow: 'via-indigo-500/50', hoverText: 'group-hover:text-indigo-300', buttonBorder: 'border-indigo-500/30 hover:border-indigo-500', buttonShadow: 'shadow-[0_0_20px_rgba(99,102,241,0.1)] hover:shadow-[0_0_30px_rgba(99,102,241,0.2)]' },
  // 5. Repression and Trauma (Amber)
  { textPrimary: 'text-amber-400', textGradient: 'from-amber-300 to-amber-600', border: 'border-amber-500/20', focus: 'focus:ring-amber-500/50 focus:border-amber-500/50', progress: 'from-amber-600 to-amber-400', glow: 'via-amber-500/50', hoverText: 'group-hover:text-amber-300', buttonBorder: 'border-amber-500/30 hover:border-amber-500', buttonShadow: 'shadow-[0_0_20px_rgba(245,158,11,0.1)] hover:shadow-[0_0_30px_rgba(245,158,11,0.2)]' },
  // 6. Sexuality and Desire (Fuchsia)
  { textPrimary: 'text-fuchsia-400', textGradient: 'from-fuchsia-300 to-fuchsia-600', border: 'border-fuchsia-500/20', focus: 'focus:ring-fuchsia-500/50 focus:border-fuchsia-500/50', progress: 'from-fuchsia-600 to-fuchsia-400', glow: 'via-fuchsia-500/50', hoverText: 'group-hover:text-fuchsia-300', buttonBorder: 'border-fuchsia-500/30 hover:border-fuchsia-500', buttonShadow: 'shadow-[0_0_20px_rgba(217,70,239,0.1)] hover:shadow-[0_0_30px_rgba(217,70,239,0.2)]' },
  // 7. Complexes and Relationships (Teal)
  { textPrimary: 'text-teal-400', textGradient: 'from-teal-300 to-teal-600', border: 'border-teal-500/20', focus: 'focus:ring-teal-500/50 focus:border-teal-500/50', progress: 'from-teal-600 to-teal-400', glow: 'via-teal-500/50', hoverText: 'group-hover:text-teal-300', buttonBorder: 'border-teal-500/30 hover:border-teal-500', buttonShadow: 'shadow-[0_0_20px_rgba(20,184,166,0.1)] hover:shadow-[0_0_30px_rgba(20,184,166,0.2)]' }
]

const currentPalette = computed(() => {
  return themePalettes[currentThemeIndex.value % themePalettes.length]
})

const currentTheme = computed(() => {
  return themes.value[currentThemeIndex.value] || { subject: '', questions: [] }
})

const isLastTheme = computed(() => {
  return currentThemeIndex.value === themes.value.length - 1
})

const getWordCount = (text) => {
  if (!text) return 0
  // Split by spaces and filter out "words" that don't have at least one letter or number
  // The regex includes standard letters, numbers, and common Latin accented characters (for Portuguese, Spanish, etc.)
  return text.trim().split(/\s+/).filter(word => /[A-Za-z0-9\u00C0-\u024F]/.test(word)).length
}

onMounted(async () => {
  try {
    const rawQuestions = await apiService.fetchQuestions()
    
    // Group questions by subject
    const grouped = {}
    rawQuestions.forEach(q => {
      if (!grouped[q.subject]) {
        grouped[q.subject] = {
          subject: q.subject,
          questions: []
        }
      }
      grouped[q.subject].questions.push(q)
      
      // Initialize answer map with empty strings
      answersMap.value[q.id] = ''
    })
    
    themes.value = Object.values(grouped)
  } catch (error) {
    console.error("Failed to load questions", error)
  } finally {
    isLoading.value = false
  }
})

const validateCurrentTheme = () => {
  // Check if all questions in the current theme have a non-empty answer (ignoring whitespace)
  const isComplete = currentTheme.value.questions.every(q => {
    return answersMap.value[q.id] && answersMap.value[q.id].trim().length > 0
  })
  showError.value = !isComplete
  return isComplete
}

const prevTheme = () => {
  if (currentThemeIndex.value > 0) {
    currentThemeIndex.value--
    showError.value = false
  }
}

const handleNext = () => {
  if (!validateCurrentTheme()) {
    return
  }

  showError.value = false

  if (isLastTheme.value) {
    // Format answers to match backend schema: { question_id, text }
    const finalAnswers = Object.entries(answersMap.value).map(([id, text]) => ({
      question_id: parseInt(id),
      text: text.trim()
    }))
    emit('completed', finalAnswers)
  } else {
    currentThemeIndex.value++
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}

// Expose internal navigation to parent
defineExpose({
  canGoBack: computed(() => currentThemeIndex.value > 0),
  goBack: prevTheme
})
</script>


