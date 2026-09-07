<template>
  <div class="flex flex-col items-center justify-center min-h-[70vh] px-4 w-full pb-32">
    
    <!-- Loading State -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center space-y-6 w-full max-w-md text-center">
      <div class="relative w-24 h-24">
        <!-- Outer spinning ring -->
        <div class="absolute inset-0 rounded-full border-2 border-slate-800 border-t-blue-500 animate-spin"></div>
        <!-- Inner pulsing core -->
        <div class="absolute inset-4 rounded-full bg-blue-500/20 blur-sm animate-pulse"></div>
        <svg class="absolute inset-0 m-auto w-8 h-8 text-blue-400 animate-pulse" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 4 4 0 0 0 .556 6.588A4 4 0 1 0 12 18Z"/>
          <path d="M12 5a3 3 0 1 1 5.997.125 4 4 0 0 1 2.526 5.77 4 4 0 0 1-.556 6.588A4 4 0 1 1 12 18Z"/>
          <path d="M15 13a4.5 4.5 0 0 1-3-4 4.5 4.5 0 0 1-3 4"/>
          <path d="M17.599 6.5a3 3 0 0 0 .399-1.375"/>
          <path d="M6.002 6.5A3 3 0 0 1 5.603 5.125"/>
          <path d="M11.588 15.5a3 3 0 0 1-.598 3.125"/>
          <path d="M12.412 15.5a3 3 0 0 0 .598 3.125"/>
        </svg>
      </div>
      <h3 class="text-xl font-medium text-slate-200 tracking-wide">The Analyst is Reviewing...</h3>
      <p class="text-slate-400 font-light text-sm leading-relaxed">
        Processing your responses to generate the analytical profile. This may take a moment.
      </p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="flex flex-col items-center justify-center space-y-6 w-full max-w-lg text-center p-8 backdrop-blur-xl bg-red-950/20 border border-red-500/30 rounded-2xl">
      <svg class="w-12 h-12 text-red-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
      <h3 class="text-xl font-bold text-red-400">Analysis Failed</h3>
      <p class="text-slate-300 font-light text-sm">{{ error }}</p>
      <button @click="emit('restart')" class="mt-4 px-6 py-2 bg-slate-800 hover:bg-slate-700 text-white rounded-lg transition-colors text-sm">Return to Start</button>
    </div>

    <!-- Success State: The Report -->
    <div v-else-if="report" class="w-full max-w-4xl flex flex-col items-center print:max-w-none print:w-full print:block">
      
      <!-- Actions Bar (Hidden on Print) -->
      <div class="w-full flex justify-end mb-6 print:hidden">
        <button 
          @click="printReport"
          class="group relative overflow-hidden cursor-pointer text-xs uppercase tracking-[0.15em] bg-[#03091e] hover:bg-[#051033] text-white font-medium py-3 px-8 rounded-full transition-all duration-500 border border-blue-500/30 hover:border-blue-400/60 shadow-[0_0_15px_rgba(59,130,246,0.1)] hover:shadow-[0_0_25px_rgba(59,130,246,0.4)]"
        >
          <span class="relative z-10 flex items-center gap-2">
            <svg class="w-4 h-4 text-blue-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9V2h12v7"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><path d="M6 14h12v8H6z"/></svg>
            Print / Save PDF
          </span>
          <!-- Subtle inner glow -->
          <div class="absolute inset-0 bg-blue-500/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500 blur-md pointer-events-none"></div>
        </button>
      </div>

      <!-- The Paper -->
      <div class="report-paper w-full bg-[#fdfbf7] text-slate-900 p-10 md:p-16 rounded-sm shadow-[0_20px_60px_rgba(0,0,0,0.5)] print:shadow-none print:p-0 print:bg-white relative overflow-hidden">
        
        <!-- Subtle paper texture overlay (simulated with CSS gradient) -->
        <div class="absolute inset-0 pointer-events-none opacity-4 bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0IiBoZWlnaHQ9IjQiPgo8cmVjdCB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSIjZmZmIi8+CjxyZWN0IHdpZHRoPSIxIiBoZWlnaHQ9IjEiIGZpbGw9IiMwMDAiLz4KPC9zdmc+')]"></div>

        <!-- Header -->
        <div class="border-b-2 border-slate-800 pb-6 mb-10 flex flex-col md:flex-row print:flex-row justify-between items-start md:items-end print:items-end gap-4 relative z-10">
          <div>
            <h1 class="font-serif text-3xl md:text-4xl font-bold tracking-tight text-slate-900 mb-1">FreudLens System</h1>
            <p class="font-sans text-xs text-slate-500 uppercase tracking-widest font-semibold">Psychodynamic Profile</p>
          </div>
          <div class="font-sans text-xs text-slate-600 text-left md:text-right print:text-right space-y-1">
            <p><span class="font-bold text-slate-800">Date:</span> {{ currentDate }}</p>
            <p><span class="font-bold text-slate-800">Time:</span> {{ currentTime }}</p>
            <p><span class="font-bold text-slate-800">Patient ID:</span> {{ patientId }}</p>
            <p><span class="font-bold text-slate-800">Analyst:</span> {{ sessionData.model }}</p>
          </div>
        </div>

        <!-- Body -->
        <div class="font-serif space-y-10 relative z-10 leading-relaxed text-slate-800 text-justify">
          
          <!-- Summary -->
          <section>
            <h2 class="text-left text-xl font-bold border-b border-slate-300 pb-2 mb-4 uppercase tracking-wider font-sans text-sm text-slate-900">I. Clinical Summary</h2>
            <p class="whitespace-pre-line text-[1.05rem]">{{ report.summary }}</p>
          </section>

          <!-- Defense Mechanisms -->
          <section>
            <h2 class="text-left text-xl font-bold border-b border-slate-300 pb-2 mb-4 uppercase tracking-wider font-sans text-sm text-slate-900">II. Observed Defense Mechanisms</h2>
            <ul class="list-disc pl-6 space-y-2 text-[1.05rem]">
              <li v-for="(mech, idx) in report.defense_mechanisms" :key="idx" class="pl-2">
                {{ mech }}
              </li>
            </ul>
          </section>

          <!-- Dynamics -->
          <section>
            <h2 class="text-left text-xl font-bold border-b border-slate-300 pb-2 mb-4 uppercase tracking-wider font-sans text-sm text-slate-900">III. Psychological Dynamics</h2>
            <p class="whitespace-pre-line text-[1.05rem]">{{ report.dynamics }}</p>
          </section>

          <!-- Past Influence -->
          <section>
            <h2 class="text-left text-xl font-bold border-b border-slate-300 pb-2 mb-4 uppercase tracking-wider font-sans text-sm text-slate-900">IV. Influence of the Past</h2>
            <p class="whitespace-pre-line text-[1.05rem]">{{ report.past_influence }}</p>
          </section>

          <!-- Conclusion -->
          <section>
            <h2 class="text-left text-xl font-bold border-b border-slate-300 pb-2 mb-4 uppercase tracking-wider font-sans text-sm text-slate-900">V. Diagnostic Conclusion</h2>
            <p class="whitespace-pre-line text-[1.05rem] italic font-medium">{{ report.conclusion }}</p>
          </section>

        </div>

        <!-- Footer -->
        <div class="mt-24 relative z-10">
          
          <!-- Signature Block -->
          <div class="flex justify-center mb-12">
            <div class="text-center w-64 shrink-0">
              <div class="h-16 border-b border-slate-800 mb-2 relative">
                <!-- Fake signature -->
                <div class="absolute bottom-0 left-0 w-full font-['Brush_Script_MT',cursive] text-4xl text-slate-800 opacity-80 -rotate-3 select-none">
                  {{ sessionData.model }}
                </div>
              </div>
              <p class="font-sans text-xs uppercase tracking-widest text-slate-600 font-bold">Simulated Analyst Persona</p>
              <p class="font-sans text-[10px] text-slate-500 mt-1">Generated by FreudLens AI</p>
            </div>
          </div>

          <!-- Disclaimer (Full width fine print) -->
          <div class="w-full text-[9px] sm:text-[10px] text-slate-500 leading-relaxed font-sans text-justify pt-3 border-t border-slate-300">
            <strong class="text-slate-700">DISCLAIMER OF LIABILITY:</strong> 
            FreudLens is an experimental software portfolio project developed solely to demonstrate artificial intelligence and large language model integration. 
            The content generated herein is entirely automated, simulated, and fictional. IT DOES NOT CONSTITUTE professional medical advice, psychological evaluation, 
            psychiatric diagnosis, therapy, or treatment. The creator(s) expressly disclaim any and all liability for decisions or actions taken based on this output. 
            By using this application, you acknowledge that this is a technical demonstration with absolutely no medical, clinical, or scientific validity. 
            If you are experiencing psychological distress, seek assistance from a licensed healthcare professional immediately.
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { apiService } from '../../services/api'

const props = defineProps({
  sessionData: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['restart'])

const isLoading = ref(true)
const error = ref(null)
const report = ref(null)

// For the document header
const now = new Date()
const currentDate = now.toLocaleDateString()
const currentTime = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
const patientId = 'FL-' + Math.random().toString(36).substring(2, 8).toUpperCase()

onMounted(async () => {
  try {
    const { apiKey, model, language, answers } = props.sessionData
    
    // Call the backend endpoint
    const response = await apiService.generateAnalysis(apiKey, model, language, answers)
    report.value = response
  } catch (e) {
    error.value = e.message || 'An unexpected error occurred.'
  } finally {
    isLoading.value = false
  }
})

const printReport = () => {
  window.print()
}
</script>
