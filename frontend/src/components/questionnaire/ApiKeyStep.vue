<template>
  <div class="flex flex-col items-center justify-center min-h-[70vh] px-4">
    <!-- Main Card -->
    <div class="w-full max-w-md p-8 backdrop-blur-xl bg-[#03091e]/80 border border-blue-500/20 rounded-2xl shadow-[0_10px_40px_rgba(0,0,0,0.8)] hover:shadow-[0_10px_40px_rgba(59,130,246,0.15)] transition-shadow duration-500 relative overflow-hidden">
      
      <!-- Subtle top glow -->
      <div class="absolute top-0 left-1/4 w-1/2 h-[1px] bg-gradient-to-r from-transparent via-blue-500/50 to-transparent"></div>

      <div class="text-center mb-10 mt-2">
        <h2 class="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-300 to-blue-600 mb-3 drop-shadow-md">
          Your Gemini Key
        </h2>
        <p class="text-slate-400 text-sm font-light leading-relaxed">
          To begin your psychoanalytic analysis, enter your Google Gemini API Key.
        </p>
      </div>

      <!-- Input Section -->
      <form @submit.prevent="handleValidate" class="space-y-6 relative z-10">
        <div>
          <div class="flex items-center justify-between mb-2">
            <label for="apiKey" class="block text-sm font-medium text-slate-300 tracking-wide">
              API Key
            </label>
            <div class="flex items-center gap-3">
              <button type="button" @click="showTutorial = !showTutorial" class="text-xs text-slate-400 hover:text-blue-300 transition-colors underline decoration-slate-600 hover:decoration-blue-400 underline-offset-2">
                Need help?
              </button>
              <a href="https://aistudio.google.com/app/apikey" target="_blank" class="inline-flex items-center justify-center gap-1.5 text-xs text-blue-400 hover:text-white font-medium transition-colors bg-blue-950/30 px-3 py-1.5 rounded-lg border border-blue-900/50 hover:border-blue-500">
                Get a Free API Key
                <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
              </a>
            </div>
          </div>
          <div class="relative">
            <input 
              id="apiKey"
              v-model="apiKey"
              type="password"
              required
              placeholder="AIzaSy..."
              class="w-full px-4 py-3 rounded-xl bg-[#020617]/80 border border-slate-700/50 text-slate-100 placeholder-slate-600 focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500/50 transition-all outline-none shadow-inner"
              :disabled="isLoading"
            />
          </div>

          <!-- Tutorial Box -->
          <Transition name="fade">
            <div v-if="showTutorial" class="mt-4 p-5 rounded-xl bg-[#020617]/60 border border-blue-500/30 text-sm text-slate-300 shadow-inner backdrop-blur-sm">
              <h4 class="font-semibold text-blue-400 mb-3 flex items-center gap-2">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                How to get your API Key:
              </h4>
              <ol class="list-decimal list-inside space-y-2 text-[13px] leading-relaxed">
                <li>Click the <strong class="text-white">Get a Free API Key</strong> button above.</li>
                <li>Sign in with your Google account.</li>
                <li>Click on the <strong class="text-white">"Create API key"</strong> button.</li>
                <li>Copy the generated key (<code class="bg-black/50 px-1.5 py-0.5 rounded text-blue-300 font-mono text-xs">AIzaSy...</code>).</li>
                <li>Paste it here! It's completely free and takes 1 minute.</li>
              </ol>
            </div>
          </Transition>
        </div>

        <!-- Error Message -->
        <p v-if="error" class="text-rose-400 text-sm text-center font-medium bg-rose-500/10 border border-rose-500/20 py-2 px-3 rounded-lg">
          {{ error }}
        </p>

        <!-- Submit Button -->
        <div class="group/button relative rounded-xl p-[1px] overflow-hidden shadow-[0_0_20px_rgba(59,130,246,0.1)] mt-8">
          <!-- Spinning light border on hover/active -->
          <div v-if="!isLoading && apiKey" class="absolute top-1/2 left-1/2 w-[200%] aspect-square -translate-x-1/2 -translate-y-1/2 animate-[spin_3s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,transparent_0%,#3b82f6_50%,transparent_100%)] opacity-0 group-hover/button:opacity-100 transition-opacity duration-500 pointer-events-none"></div>

          <button 
            type="submit"
            :disabled="isLoading || !apiKey"
            class="relative w-full py-3.5 px-4 bg-[#03091e] group-hover/button:bg-blue-950/40 text-blue-100 font-medium tracking-[0.15em] uppercase text-sm rounded-xl transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed cursor-pointer flex justify-center items-center overflow-hidden"
          >
            <!-- Idle glow -->
            <div class="absolute inset-0 bg-gradient-to-r from-blue-600/10 to-blue-400/10 opacity-0 group-hover/button:opacity-100 transition-opacity duration-300"></div>
            
            <span class="relative z-10 flex items-center gap-3">
              {{ isLoading ? 'Validating...' : 'Start Analysis' }}
              <svg v-if="isLoading" class="animate-spin h-4 w-4 text-blue-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            </span>
          </button>
        </div>
      </form>

      <!-- Security Notice (Emerald style matching HomeHero) -->
      <div class="mt-8 flex flex-col items-center gap-3 pt-6 border-t border-white/5">
        <div class="inline-flex items-center justify-center gap-2 px-4 py-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/20 shadow-[0_0_15px_rgba(16,185,129,0.1)]">
          <svg class="text-emerald-400" xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          <span class="text-xs font-semibold tracking-[0.1em] uppercase text-emerald-50">100% Private. <span class="text-emerald-200/80 font-medium">No data stored.</span></span>
        </div>
        <p class="text-[11px] text-slate-400/80 font-medium tracking-wide text-center leading-relaxed max-w-sm mt-1">
          Your API Key and answers are processed strictly locally in your browser. We have zero data retention. Nothing is ever sent to or stored on our servers. As a fully transparent open-source project, you can verify this yourself:
          <br><br>
          <a href="https://github.com/PratesB/freudlens-public" target="_blank" class="text-blue-400 hover:text-blue-300 transition-colors inline-flex items-center underline decoration-blue-500/30 underline-offset-2">
            Inspect the Code on GitHub
            <svg class="w-3 h-3 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
            </svg>
          </a>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { apiService } from '../../services/api'

const emit = defineEmits(['validated'])

const apiKey = ref('')
const isLoading = ref(false)
const error = ref('')
const showTutorial = ref(false)

const handleValidate = async () => {
  if (!apiKey.value.trim()) return
  
  error.value = ''
  isLoading.value = true
  
  try {
    const isValid = await apiService.validateApiKey(apiKey.value)
    
    if (isValid) {
      emit('validated', apiKey.value)
    } else {
      error.value = 'Invalid API key. Please check and try again.'
    }
  } catch (err) {
    error.value = 'An error occurred while connecting to the server.'
  } finally {
    isLoading.value = false
  }
}
</script>
