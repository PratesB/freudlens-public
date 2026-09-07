<template>
  <div class="bg-[#020617] min-h-screen flex flex-col text-slate-100 overflow-x-hidden selection:bg-blue-500/30 relative z-0">
    <!-- Background Gradients to match HomeHero -->
    <div class="fixed inset-0 pointer-events-none z-[-1]">
      <div class="absolute top-1/4 left-1/4 w-[500px] h-[500px] bg-blue-600/10 rounded-full blur-[120px]"></div>
      <div class="absolute bottom-1/4 right-1/4 w-[400px] h-[400px] bg-blue-400/5 rounded-full blur-[100px]"></div>
    </div>
    

    <!-- Hidden Audio Player -->
    <audio ref="audioPlayerRef" src="/ambient-music.mp3" loop></audio>

    <main class="container mx-auto px-4 max-w-4xl relative z-10 flex-grow pt-6 sm:pt-12 pb-24">
      
      <!-- Top Navigation Controls (In document flow, prevents overlap) -->
      <div class="w-full flex justify-end items-center mb-6 sm:mb-8 print:hidden min-h-[40px] gap-4">
        
        <!-- Audio Control -->
        <button 
          v-if="currentStep === 3"
          @click="toggleAudio"
          class="flex items-center gap-2 px-4 py-2 rounded-full border transition-all shadow-[0_0_20px_rgba(0,0,0,0.5)] cursor-pointer text-[10px] sm:text-xs uppercase tracking-[0.2em] font-medium group"
          :class="isAudioPlaying ? 'bg-emerald-950/30 border-emerald-900/50 text-emerald-400 hover:bg-emerald-900/40 hover:text-emerald-300' : 'bg-[#020617] border-slate-800 text-slate-500 hover:bg-slate-800/50 hover:text-slate-400'"
          title="Toggle Background Music"
        >
          <svg v-if="isAudioPlaying" class="w-4 h-4 animate-pulse" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>
          <svg v-else class="w-4 h-4 opacity-70" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
          <span class="hidden sm:inline pt-[1px]">{{ isAudioPlaying ? 'Music: ON' : 'Music: OFF' }}</span>
        </button>
        <!-- Exit / Back Button (X) -->
        <router-link 
          v-if="currentStep === 1" 
          to="/" 
          class="flex items-center justify-center w-10 h-10 rounded-full bg-[#020617] border border-blue-900/50 text-blue-400 hover:bg-blue-900/30 hover:text-blue-300 hover:border-blue-500 transition-all shadow-[0_0_20px_rgba(0,0,0,0.5)] cursor-pointer"
          title="Exit Session"
        >
          <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </router-link>

        <button 
          v-else-if="currentStep === 2" 
          @click="currentStep = 1"
          class="flex items-center justify-center w-10 h-10 rounded-full bg-[#020617] border border-blue-900/50 text-blue-400 hover:bg-blue-900/30 hover:text-blue-300 hover:border-blue-500 transition-all shadow-[0_0_20px_rgba(0,0,0,0.5)] cursor-pointer"
          title="Back to API Key"
        >
          <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- State 1: API Key Validation -->
      <Transition 
        enter-active-class="transition-all duration-300 ease-out"
        leave-active-class="transition-all duration-300 ease-in"
        enter-from-class="opacity-0 translate-y-2"
        enter-to-class="opacity-100 translate-y-0"
        leave-from-class="opacity-100 translate-y-0"
        leave-to-class="opacity-0 translate-y-2"
        mode="out-in"
      >
        <ApiKeyStep 
          v-if="currentStep === 1" 
          @validated="handleApiKeyValidated" 
        />
        
        <!-- State 2: Configuration -->
        <ConfigStep 
          v-else-if="currentStep === 2" 
          @configured="handleConfigured" 
        />

        <!-- State 3: The Questions -->
        <QuestionsStep 
          v-else-if="currentStep === 3" 
          ref="questionsStepRef"
          @completed="handleQuestionsCompleted" 
          @back="currentStep = 2"
        />

        <!-- State 4: The Final Report -->
        <ReportStep 
          v-else-if="currentStep === 4" 
          :sessionData="sessionData"
          @restart="currentStep = 1"
        />
      </Transition>
    </main>

    <!-- Global Footer (Hidden on Print) -->
    <div class="print:hidden mt-auto w-full">
      <AppFooter />
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import ApiKeyStep from '../components/questionnaire/ApiKeyStep.vue'
import ConfigStep from '../components/questionnaire/ConfigStep.vue'
import QuestionsStep from '../components/questionnaire/QuestionsStep.vue'
import ReportStep from '../components/questionnaire/ReportStep.vue'
import AppFooter from '../components/layout/AppFooter.vue'

// State
const currentStep = ref(1)
const questionsStepRef = ref(null)
const audioPlayerRef = ref(null)
const isAudioPlaying = ref(false)
const sessionData = ref({
  apiKey: null,
  model: null,
  language: null,
  answers: []
})

// Audio Toggle Logic
const toggleAudio = () => {
  if (!audioPlayerRef.value) return
  
  if (isAudioPlaying.value) {
    audioPlayerRef.value.pause()
    isAudioPlaying.value = false
  } else {
    audioPlayerRef.value.play()
    isAudioPlaying.value = true
  }
}

// Automatically stop audio when leaving Questions Mode
watch(currentStep, (newStep) => {
  if (newStep !== 3 && isAudioPlaying.value && audioPlayerRef.value) {
    audioPlayerRef.value.pause()
    isAudioPlaying.value = false
  }
})

// Navigation is now handled by components emitting events or local state

const handleApiKeyValidated = (key) => {
  sessionData.value.apiKey = key
  // Advance to Phase 2 (Config)
  currentStep.value = 2
}

const handleConfigured = (config) => {
  sessionData.value.model = config.modelName
  sessionData.value.language = config.language
  
  // Advance to Phase 3 (Questions)
  currentStep.value = 3
}

const handleQuestionsCompleted = (answers) => {
  sessionData.value.answers = answers
  
  // Advance to Phase 4 (Submit/Report)
  currentStep.value = 4
}
</script>

