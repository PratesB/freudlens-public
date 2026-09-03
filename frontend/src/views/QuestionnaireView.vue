<template>
  <div class="bg-[#020617] min-h-screen text-slate-100 overflow-x-hidden selection:bg-blue-500/30 pt-12 pb-12 relative z-0">
    <!-- Background Gradients to match HomeHero -->
    <div class="fixed inset-0 pointer-events-none z-[-1]">
      <div class="absolute top-1/4 left-1/4 w-[500px] h-[500px] bg-blue-600/10 rounded-full blur-[120px]"></div>
      <div class="absolute bottom-1/4 right-1/4 w-[400px] h-[400px] bg-blue-400/5 rounded-full blur-[100px]"></div>
    </div>
    
    <main class="container mx-auto px-4 max-w-4xl relative z-10">
      <!-- Back to Home Link -->
      <div class="mb-12">
        <router-link to="/" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-[#020617] border border-blue-900/50 text-blue-400 hover:bg-blue-900/30 hover:text-blue-300 hover:border-blue-500 transition-all shadow-[0_0_20px_rgba(0,0,0,0.5)] font-medium text-sm">
          <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
          </svg>
          Back to Home
        </router-link>
      </div>

      <!-- State 1: API Key Validation -->
      <Transition name="fade" mode="out-in">
        <ApiKeyStep 
          v-if="currentStep === 1" 
          @validated="handleApiKeyValidated" 
        />
        
        <!-- Placeholders for future phases -->
        <div v-else-if="currentStep === 2" class="text-center py-20">
          <h2 class="text-2xl font-bold">Phase 2: Choose Psychoanalyst and Language</h2>
          <p class="text-slate-500 mt-2">Your API Key is validated. Coming soon...</p>
        </div>
      </Transition>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ApiKeyStep from '../components/questionnaire/ApiKeyStep.vue'

// State
const currentStep = ref(1)
const sessionData = ref({
  apiKey: null,
  model: null,
  language: null,
  answers: []
})

// Handlers
const handleApiKeyValidated = (key) => {
  sessionData.value.apiKey = key
  // Advance to Phase 2 (Config)
  currentStep.value = 2
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
