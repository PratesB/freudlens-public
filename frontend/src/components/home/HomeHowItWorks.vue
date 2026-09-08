<template>
  <section id="how-it-works" class="pt-24 pb-12 lg:pt-32 lg:pb-16 bg-[#050b1a] border-t border-blue-900/20 relative overflow-hidden">
    
    <!-- Background Ambient Glow -->
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[1000px] h-[500px] bg-blue-900/10 rounded-full blur-[120px] pointer-events-none"></div>

    <div class="max-w-6xl mx-auto px-6 relative z-10">
      
      <!-- Header -->
      <div class="text-center mb-16 reveal-on-scroll">
        <span class="text-blue-400 text-xs font-bold tracking-[0.3em] uppercase block mb-4">
          The Procedure
        </span>
        <h2 class="text-4xl lg:text-6xl font-black text-white tracking-tight drop-shadow-md">
          How FreudLens works
        </h2>
        <p class="text-slate-400 mt-6 text-lg max-w-2xl mx-auto font-light">
          A clinical approach to understanding your mind. The entire session happens locally and privately in your browser.
        </p>
      </div>

      <!-- The Grid -->
      <div class="w-full max-w-[90rem] mx-auto reveal-on-scroll">
        
        <!-- Cards Container -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 xl:gap-8" style="perspective: 2000px;">
          
          <div 
            v-for="(card, index) in procedureCards" :key="index"
            @mousemove="handleMouseMove($event, index)"
            @mouseleave="handleMouseLeave(index)"
            :style="{ transform: cardTransforms[index] }"
            class="relative bg-gradient-to-b from-white/[0.04] to-transparent backdrop-blur-xl border border-white/[0.05] border-t-white/[0.15] rounded-[2rem] p-8 xl:p-10 shadow-[0_10px_40px_rgba(0,0,0,0.5)] flex flex-col group transition-transform duration-200 ease-out overflow-hidden"
            style="transform-style: preserve-3d; will-change: transform;"
          >
            <!-- Spotlight / Glow -->
            <div 
              class="absolute inset-0 z-0 pointer-events-none transition-opacity duration-300"
              :style="spotlightStyles[index]"
            ></div>

            <!-- Ghost Number -->
            <div 
              class="absolute -right-4 -top-8 text-[180px] font-black text-white/[0.02] font-mono leading-none pointer-events-none select-none transition-all duration-700 group-hover:-translate-y-2"
              :class="card.ghostHoverClass"
            >
              {{ card.number }}
            </div>
            
            <div class="relative z-10 flex flex-col h-full pointer-events-none" style="transform: translateZ(30px);">
              <h3 class="text-xl font-serif italic text-white/90 mb-6 mt-4">"{{ card.quote }}"</h3>
              <h4 class="text-sm font-bold mb-3 tracking-widest uppercase" :class="card.titleClass">{{ card.title }}</h4>
              <p class="text-slate-400 text-sm leading-relaxed mb-8 flex-grow">
                <template v-for="(segment, i) in card.description" :key="i">
                  <strong v-if="segment.bold" class="text-slate-300">{{ segment.text }}</strong>
                  <template v-else>{{ segment.text }}</template>
                </template>
              </p>
              
              <a v-if="card.action" :href="card.action.url" target="_blank" class="pointer-events-auto inline-flex items-center justify-center gap-1.5 text-xs hover:text-white font-medium transition-colors bg-white/5 px-4 py-2.5 rounded-lg border border-white/10 hover:border-white/30 mt-auto w-fit" :class="card.actionTextClass">
                {{ card.action.text }}
                <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
              </a>
            </div>
          </div>

        </div>
      </div>

      <!-- Start Diagnostics Action Area & Security Note -->
      <div class="flex flex-col items-center justify-center mb-8 reveal-on-scroll mt-16">
        <!-- Action Container with Spinning Border -->
        <div class="group/button relative rounded-full p-[2px] overflow-hidden shadow-[0_10px_40px_rgba(0,0,0,0.8)] hover:shadow-[0_10px_40px_rgba(59,130,246,0.2)] transition-shadow duration-500 cursor-pointer mb-6">
          <div class="absolute top-1/2 left-1/2 w-[400%] aspect-square -translate-x-1/2 -translate-y-1/2 animate-[spin_3s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,transparent_0%,#3b82f6_50%,transparent_100%)] opacity-30 group-hover/button:opacity-80 transition-opacity duration-500 pointer-events-none"></div>

          <button 
            @click="start"
            class="cursor-pointer group relative overflow-hidden px-8 py-4 md:px-12 md:py-5 w-full h-full rounded-full bg-[#03091e] transition-colors duration-500 flex items-center gap-3 font-medium text-lg text-white"
          >
            <div class="absolute pointer-events-none rounded-full bg-blue-500/40 blur-[30px] w-32 h-full top-0 animate-[sweep_2s_ease-in-out_infinite] transition-opacity duration-500"></div>
            <span class="relative z-10 whitespace-nowrap">Take your seat</span>
            <svg class="relative z-10 w-5 h-5 transition-transform duration-300 group-hover:translate-x-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M14 5l7 7m0 0l-7 7m7-7H3" />
            </svg>
          </button>
        </div>

        <!-- Security / Privacy Note (Minimalist) -->
        <div class="mt-2">
          <p class="text-slate-500 text-xs md:text-sm max-w-xl text-center leading-relaxed">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="inline-block text-blue-500/70 mr-1.5 -mt-0.5"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
            <strong class="text-slate-400 font-semibold">Zero Data Retention:</strong> FreudLens runs exclusively in your browser. API keys and profiles are <span class="text-slate-400 underline decoration-blue-900/50 underline-offset-2">never saved</span>.
          </p>
        </div>

        <!-- Medical & Technical Disclaimer -->
        <div class="mt-8 max-w-4xl text-center px-4">
          <div class="text-slate-500/80 text-[10px] md:text-[11px] leading-relaxed font-sans text-justify md:text-center opacity-70">
            <strong class="text-slate-400 uppercase tracking-widest font-semibold mr-1">Disclaimer of Liability:</strong> 
            FreudLens is an experimental software project created as part of a professional portfolio to demonstrate advanced skills in software engineering, system architecture, and the practical integration of artificial intelligence and large language models. All content generated by this application is fully automated, simulated, and fictional. It does not constitute professional medical advice, psychological evaluation, psychiatric diagnosis, therapy, counseling, or any form of clinical treatment. The creator(s) expressly disclaim any and all liability for decisions, actions, or consequences arising from the use of or reliance upon this output. By accessing or using FreudLens, you acknowledge that this is a technical demonstration only and possesses no medical, clinical, therapeutic, or scientific validity. If you are experiencing psychological distress or mental health concerns, please seek immediate assistance from a licensed healthcare professional.
          </div>
        </div>
      </div>

    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const procedureCards = [
  {
    number: '01',
    ghostHoverClass: 'group-hover:text-blue-500/[0.05]',
    titleClass: 'text-blue-400',
    actionTextClass: 'text-blue-400',
    spotlightColor: 'rgba(59, 130, 246, 0.15)',
    quote: 'Provide the key to your subconscious.',
    title: 'The Key',
    description: [
      { text: 'You must supply your own Google Gemini API Key. ' },
      { text: 'This is a BYOK platform.', bold: true },
      { text: ' Your key runs strictly locally and is never sent to our servers.' }
    ],
    action: { text: 'Get a Free API Key', url: 'https://aistudio.google.com/app/apikey' }
  },
  {
    number: '02',
    ghostHoverClass: 'group-hover:text-emerald-500/[0.05]',
    titleClass: 'text-emerald-500',
    actionTextClass: 'text-emerald-500',
    spotlightColor: 'rgba(16, 185, 129, 0.15)',
    quote: 'Establishing a secure dialogue.',
    title: 'The Handshake',
    description: [
      { text: 'The framework instantly validates your API key locally. Once verified, the connection to the engine is established and the session begins seamlessly.' }
    ],
    action: null
  },
  {
    number: '03',
    ghostHoverClass: 'group-hover:text-indigo-500/[0.05]',
    titleClass: 'text-indigo-400',
    actionTextClass: 'text-indigo-400',
    spotlightColor: 'rgba(99, 102, 241, 0.15)',
    quote: 'Answer with your first instinct.',
    title: 'The Assessment',
    description: [
      { text: 'You will face ' },
      { text: '21 multiple-choice questions', bold: true },
      { text: ' designed to probe your development habits, mathematically distributed across psychoanalytical domains.' }
    ],
    action: null
  },
  {
    number: '04',
    ghostHoverClass: 'group-hover:text-purple-500/[0.05]',
    titleClass: 'text-purple-400',
    actionTextClass: 'text-purple-400',
    spotlightColor: 'rgba(168, 85, 247, 0.15)',
    quote: 'Confront your hidden patterns.',
    title: 'The Core Dump',
    description: [
      { text: 'At the end of the questions, the engine processes your choices and outputs a brutally honest, deeply personal psychological profile of you as a developer.' }
    ],
    action: null
  }
]

const cardTransforms = ref([
  'rotateX(0deg) rotateY(0deg)',
  'rotateX(0deg) rotateY(0deg)',
  'rotateX(0deg) rotateY(0deg)',
  'rotateX(0deg) rotateY(0deg)'
])

const spotlightStyles = ref([
  { opacity: 0, background: '' },
  { opacity: 0, background: '' },
  { opacity: 0, background: '' },
  { opacity: 0, background: '' }
])

const handleMouseMove = (event, index) => {
  const card = event.currentTarget
  const rect = card.getBoundingClientRect()
  const x = event.clientX - rect.left
  const y = event.clientY - rect.top

  const centerX = rect.width / 2
  const centerY = rect.height / 2
  
  // Calculate rotation angles (max 10 degrees)
  const rotateX = ((y - centerY) / centerY) * -10
  const rotateY = ((x - centerX) / centerX) * 10
  
  cardTransforms.value[index] = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`
  
  spotlightStyles.value[index] = {
    opacity: 1,
    background: `radial-gradient(circle 350px at ${x}px ${y}px, ${procedureCards[index].spotlightColor}, transparent 70%)`
  }
}

const handleMouseLeave = (index) => {
  cardTransforms.value[index] = 'rotateX(0deg) rotateY(0deg)'
  spotlightStyles.value[index].opacity = 0
}

const start = () => {
  router.push('/questionnaire')
}
</script>

<style scoped>
@keyframes sweep {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}

.hide-scrollbar::-webkit-scrollbar {
  display: none;
}
.hide-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>
