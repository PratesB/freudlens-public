<template>
  <div class="flex flex-col items-center justify-center min-h-[70vh] px-4 w-full pb-32">
    <!-- Main Container -->
    <div class="w-full max-w-4xl p-8 backdrop-blur-xl bg-[#03091e]/80 border border-blue-500/20 rounded-2xl shadow-[0_10px_40px_rgba(0,0,0,0.8)] relative">
      
      <!-- Subtle top glow -->
      <div class="absolute top-0 left-1/4 w-1/2 h-[1px] bg-gradient-to-r from-transparent via-blue-500/50 to-transparent"></div>

      <div class="text-center mb-10 mt-2">
        <h2 class="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-300 to-blue-600 mb-3 drop-shadow-md">
          Choose Your Analyst
        </h2>
        <p class="text-slate-400 text-sm font-light leading-relaxed max-w-xl mx-auto">
          Select the psychoanalytic lens for your assessment. Choose to be analyzed by the Founder himself or through the expanded Freudian frameworks of his legendary successors.
        </p>
      </div>

      <form @submit.prevent="handleSubmit" class="space-y-10 relative z-10">
        
        <!-- Analyst Selection Cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div 
            v-for="analyst in analysts" 
            :key="analyst.id"
            @click="selectedAnalyst = analyst.id"
            class="relative cursor-pointer rounded-xl p-6 transition-all duration-500 flex flex-col h-full border group min-h-[420px]"
            :class="selectedAnalyst === analyst.id 
              ? 'border-blue-500 shadow-[0_0_30px_rgba(59,130,246,0.3)]' 
              : 'border-slate-700/50 hover:border-blue-500/50'"
          >
            <!-- Background Image -->
            <div 
              class="absolute inset-0 bg-cover bg-top rounded-xl opacity-50 group-hover:opacity-70 transition-opacity duration-500 pointer-events-none"
              :style="{ backgroundImage: `url(${analyst.image})` }"
            ></div>
            <!-- Dark Gradient overlay so text is readable at the bottom -->
            <div class="absolute inset-0 bg-gradient-to-t from-[#020617] from-10% via-[#020617]/80 via-60% to-transparent rounded-xl pointer-events-none"></div>

            <!-- Selected Glow Effect inside card -->
            <div 
              class="absolute inset-0 bg-gradient-to-br from-blue-500/20 to-transparent rounded-xl opacity-0 transition-opacity duration-500 pointer-events-none"
              :class="selectedAnalyst === analyst.id ? 'opacity-100' : 'group-hover:opacity-30'"
            ></div>

            <div class="flex justify-end mb-4 relative z-20">
              <!-- Tooltip for Model Info -->
              <div class="group/tooltip relative">
                <svg class="w-5 h-5 text-slate-400 hover:text-blue-400 transition-colors cursor-help drop-shadow-md" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
                <!-- Tooltip Popup -->
                <div class="absolute bottom-full right-0 mb-2 w-max max-w-[200px] p-2 bg-[#020617] border border-slate-600 rounded-lg shadow-2xl opacity-0 invisible group-hover/tooltip:opacity-100 group-hover/tooltip:visible transition-all duration-300 z-50 text-xs text-slate-200 text-center">
                  Powered by <span class="text-blue-400 font-mono">{{ analyst.id }}</span>
                </div>
              </div>
            </div>

            <!-- Push text to the bottom to reveal the face -->
            <div class="mt-auto relative z-10 pt-20">
              <h3 
                class="text-xl font-bold mb-2 transition-colors duration-500"
                :class="selectedAnalyst === analyst.id ? 'text-white' : 'text-slate-200'"
              >
                {{ analyst.name }}
              </h3>
              
              <p 
                class="text-sm font-light leading-relaxed transition-colors duration-500"
                :class="selectedAnalyst === analyst.id ? 'text-blue-100/80' : 'text-slate-400'"
              >
                {{ analyst.description }}
              </p>

              <!-- Selection Indicator -->
              <div 
                class="mt-4 flex items-center justify-end transition-opacity duration-500"
                :class="selectedAnalyst === analyst.id ? 'opacity-100' : 'opacity-0'"
              >
                <div class="w-5 h-5 rounded-full bg-blue-500 flex items-center justify-center">
                  <svg class="w-3 h-3 text-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Language Selection (Custom Dropdown) -->
        <div class="max-w-md mx-auto relative">
          <label class="block text-sm font-medium text-slate-300 mb-2 tracking-wide text-center">
            Session Language
          </label>
          <div class="relative">
            <!-- Transparent Overlay to close dropdown -->
            <div 
              v-if="isDropdownOpen" 
              @click="isDropdownOpen = false" 
              class="fixed inset-0 z-40"
            ></div>

            <!-- Selected Value Button -->
            <button 
              type="button"
              @click="isDropdownOpen = !isDropdownOpen"
              class="w-full flex items-center justify-between px-4 py-3 rounded-xl bg-[#020617]/80 border border-slate-700/50 text-slate-100 hover:border-blue-500/50 transition-all outline-none shadow-inner cursor-pointer relative z-50"
            >
              <div class="flex items-center gap-3">
                <img :src="`https://flagcdn.com/w20/${selectedLanguageObj.code}.png`" :alt="selectedLanguageObj.name" class="w-5 rounded-[2px]" />
                <span>{{ selectedLanguageObj.name }}</span>
              </div>
              <svg class="w-4 h-4 text-slate-400 transition-transform duration-300" :class="{ 'rotate-180': isDropdownOpen }" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
            </button>

            <!-- Dropdown List -->
            <transition name="fade">
              <ul 
                v-if="isDropdownOpen"
                class="absolute z-50 w-full mt-2 py-2 bg-[#020617] border border-slate-700 rounded-xl shadow-[0_10px_40px_rgba(0,0,0,0.8)] max-h-60 overflow-y-auto"
              >
                <li 
                  v-for="lang in languages" 
                  :key="lang.name"
                  @click="selectLanguage(lang)"
                  class="px-4 py-2.5 flex items-center gap-3 cursor-pointer hover:bg-blue-900/40 transition-colors"
                  :class="{ 'bg-blue-900/20': selectedLanguage === lang.name }"
                >
                  <img :src="`https://flagcdn.com/w20/${lang.code}.png`" :alt="lang.name" class="w-5 rounded-[2px]" />
                  <span class="text-slate-200">{{ lang.name }}</span>
                </li>
              </ul>
            </transition>
          </div>
        </div>

        <!-- Submit Button -->
        <div class="max-w-md mx-auto mb-8">
          <div class="group/button relative rounded-xl p-[1px] overflow-hidden shadow-[0_0_20px_rgba(59,130,246,0.1)] mt-4">
            <!-- Spinning light border on hover -->
            <div class="absolute top-1/2 left-1/2 w-[200%] aspect-square -translate-x-1/2 -translate-y-1/2 animate-[spin_3s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,transparent_0%,#3b82f6_50%,transparent_100%)] opacity-0 group-hover/button:opacity-100 transition-opacity duration-500 pointer-events-none"></div>

            <button 
              type="submit"
              class="relative w-full py-3.5 px-4 bg-[#03091e] group-hover/button:bg-blue-950/40 text-blue-100 font-medium tracking-[0.15em] uppercase text-sm rounded-xl transition-all duration-300 cursor-pointer flex justify-center items-center overflow-hidden"
            >
              <!-- Idle glow -->
              <div class="absolute inset-0 bg-gradient-to-r from-blue-600/10 to-blue-400/10 opacity-0 group-hover/button:opacity-100 transition-opacity duration-300"></div>
              
              <span class="relative z-10 flex items-center gap-3">
                Proceed to Couch
                <svg class="w-4 h-4 text-blue-400 transition-transform duration-300 group-hover/button:translate-x-1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
              </span>
            </button>
          </div>
        </div>

        <!-- Medical Disclaimer -->
        <div class="max-w-3xl mx-auto text-[9px] sm:text-[10px] text-slate-500/80 leading-relaxed font-sans text-justify md:text-center mt-12 pt-6 border-t border-slate-800/60 transition-opacity hover:opacity-100 opacity-70">
          <strong class="text-slate-400 uppercase tracking-widest font-semibold mr-1">Disclaimer of Liability:</strong> 
          FreudLens is an experimental software portfolio project developed solely to demonstrate artificial intelligence and large language model integration. 
          The content generated herein is entirely automated, simulated, and fictional. IT DOES NOT CONSTITUTE professional medical advice, psychological evaluation, 
          psychiatric diagnosis, therapy, or treatment. The creator(s) expressly disclaim any and all liability for decisions or actions taken based on this output. 
          By using this application, you acknowledge that this is a technical demonstration with absolutely no medical, clinical, or scientific validity. 
          If you are experiencing psychological distress, seek assistance from a licensed healthcare professional immediately.
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const emit = defineEmits(['configured'])

const analysts = [
  {
    id: 'gemini-3.7-flash',
    name: 'Sigmund Freud',
    description: 'The Founder. Fast, instinctive analysis. Focuses purely on your repressed drives and immediate subconscious reactions.',
    image: '/freud-portrait.jpg'
  },
  {
    id: 'gemini-3.6-flash',
    name: 'Carl Jung',
    description: 'Freud’s famous disciple. Expands the Freudian foundation with a deep dive into the archetypes and collective unconscious of your psyche.',
    image: '/carl-jung-portrait.png'
  },
  {
    id: 'gemini-3.5-flash',
    name: 'Jacques Lacan',
    description: 'The intellectual heir. A "Return to Freud" approach. Complexly deconstructs the language and symbolic order of your discourse.',
    image: 'jacques-lacan-portrait.png'
  }
]

const languages = [
  { name: 'Deutsch', code: 'de' },
  { name: 'English', code: 'us' },
  { name: 'Español', code: 'es' },
  { name: 'Français', code: 'fr' },
  { name: 'Italiano', code: 'it' },
  { name: 'Norsk', code: 'no' },
  { name: 'Português', code: 'br' },
  { name: 'Suomi', code: 'fi' },
  { name: 'Svenska', code: 'se' }
]

// Defaults per user request
const selectedAnalyst = ref('gemini-3.7-flash')
const selectedLanguage = ref('English')
const isDropdownOpen = ref(false)

const selectedLanguageObj = computed(() => {
  return languages.find(l => l.name === selectedLanguage.value) || languages.find(l => l.name === 'English')
})

const selectLanguage = (lang) => {
  selectedLanguage.value = lang.name
  isDropdownOpen.value = false
}

const handleSubmit = () => {
  emit('configured', {
    modelName: selectedAnalyst.value,
    language: selectedLanguage.value
  })
}
</script>
