<template>
  <div class="bg-[#020617] min-h-screen flex flex-col text-slate-100 overflow-x-hidden selection:bg-blue-500/30 relative z-0">
    <!-- Background Gradients to match HomeHero -->
    <div class="fixed inset-0 pointer-events-none z-[-1]">
      <div class="absolute top-1/4 left-1/4 w-[500px] h-[500px] bg-blue-600/10 rounded-full blur-[120px]"></div>
      <div class="absolute bottom-1/4 right-1/4 w-[400px] h-[400px] bg-blue-400/5 rounded-full blur-[100px]"></div>
    </div>
    

    
    <main class="container mx-auto px-4 max-w-4xl relative z-10 flex-grow pt-6 sm:pt-12 pb-24">
      
      <!-- Top Navigation Controls (In document flow, prevents overlap) -->
      <div class="w-full flex justify-between items-center mb-6 sm:mb-8 print:hidden min-h-[40px]">
        
        <!-- Left Side: Back Button -->
        <div>
          <button 
            v-if="currentStep > 1 && currentStep < 4" 
            @click="handleBack" 
            class="flex items-center gap-2 px-5 py-2.5 rounded-full bg-[#020617] border border-blue-900/50 text-blue-400 hover:bg-blue-900/30 hover:text-blue-300 hover:border-blue-500 transition-all shadow-[0_0_20px_rgba(0,0,0,0.5)] font-medium text-sm group cursor-pointer"
          >
            <svg class="w-4 h-4 group-hover:-translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
            Previous Step
          </button>
        </div>

        <!-- Right Side: Exit Button -->
        <div>
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
        </div>
      </div>

      <!-- State 1: API Key Validation -->
      <Transition name="fade" mode="out-in">
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
import { ref } from 'vue'
import ApiKeyStep from '../components/questionnaire/ApiKeyStep.vue'
import ConfigStep from '../components/questionnaire/ConfigStep.vue'
import QuestionsStep from '../components/questionnaire/QuestionsStep.vue'
import ReportStep from '../components/questionnaire/ReportStep.vue'
import AppFooter from '../components/layout/AppFooter.vue'

// State
const currentStep = ref(1)
const questionsStepRef = ref(null)
const sessionData = ref({
  apiKey: null,
  model: null,
  language: null,
  answers: []
})

// Handlers
const handleBack = () => {
  if (currentStep.value === 3 && questionsStepRef.value && questionsStepRef.value.canGoBack) {
    questionsStepRef.value.goBack()
  } else {
    currentStep.value--
  }
}

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

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>
