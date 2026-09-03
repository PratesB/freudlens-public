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
          A clinical approach to analyzing your code. The entire session happens locally in your browser. Swipe or use the buttons to proceed.
        </p>
      </div>

      <!-- The Carousel -->
      <div class="relative w-full max-w-md md:max-w-4xl mx-auto reveal-on-scroll">
        
        <!-- Controls (Desktop/Buttons) -->
        <div class="absolute top-1/2 -left-4 md:-left-16 -translate-y-1/2 z-20 hidden md:block">
          <button @click="scrollPrev" class="w-12 h-12 rounded-full bg-[#020617] border border-blue-900/50 flex items-center justify-center text-blue-400 hover:bg-blue-900/30 hover:border-blue-500 transition-all shadow-[0_0_20px_rgba(0,0,0,0.5)] cursor-pointer">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" /></svg>
          </button>
        </div>
        <div class="absolute top-1/2 -right-4 md:-right-16 -translate-y-1/2 z-20 hidden md:block">
          <button @click="scrollNext" class="w-12 h-12 rounded-full bg-[#020617] border border-blue-900/50 flex items-center justify-center text-blue-400 hover:bg-blue-900/30 hover:border-blue-500 transition-all shadow-[0_0_20px_rgba(0,0,0,0.5)] cursor-pointer">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
          </button>
        </div>

        <!-- Cards Container -->
        <div 
          ref="carouselRef" 
          class="flex overflow-x-auto snap-x snap-mandatory gap-6 pb-12 hide-scrollbar scroll-smooth"
          @scroll="handleScroll"
        >
          
          <!-- Card 1 -->
          <div class="snap-center shrink-0 w-full md:w-[calc(50%-12px)] lg:w-[calc(33.333%-16px)] bg-[#020617]/40 backdrop-blur-md border border-slate-800/80 rounded-[2rem] p-8 shadow-2xl flex flex-col group hover:border-blue-500/50 transition-colors duration-500">
            <div class="w-12 h-12 rounded-full border-2 border-blue-500/30 bg-blue-950/30 flex items-center justify-center text-blue-400 font-mono text-sm mb-6 relative">
              01
              <div class="absolute inset-0 bg-blue-500/20 rounded-full blur-md opacity-0 group-hover:opacity-100 transition-opacity"></div>
            </div>
            <h3 class="text-xl font-serif italic text-white/90 mb-2">"Provide the key to your subconscious."</h3>
            <h4 class="text-lg font-bold text-blue-400 mb-3 tracking-wide">The Key</h4>
            <p class="text-slate-400 text-sm leading-relaxed mb-6 flex-grow">
              You must supply your own Google Gemini API Key. <strong class="text-slate-300">This is a BYOK platform.</strong> Your key runs strictly locally and is never sent to our servers.
            </p>
            <a href="https://aistudio.google.com/app/apikey" target="_blank" class="inline-flex items-center justify-center gap-1.5 text-xs text-blue-400 hover:text-white font-medium transition-colors bg-blue-950/30 px-4 py-2.5 rounded-lg border border-blue-900/50 hover:border-blue-500 mt-auto">
              Get a Free API Key
              <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            </a>
          </div>

          <!-- Card 2 -->
          <div class="snap-center shrink-0 w-full md:w-[calc(50%-12px)] lg:w-[calc(33.333%-16px)] bg-[#020617]/40 backdrop-blur-md border border-slate-800/80 rounded-[2rem] p-8 shadow-2xl flex flex-col group hover:border-emerald-500/50 transition-colors duration-500">
            <div class="w-12 h-12 rounded-full border-2 border-emerald-500/30 bg-emerald-950/30 flex items-center justify-center text-emerald-400 font-mono text-sm mb-6 relative">
              02
              <div class="absolute inset-0 bg-emerald-500/20 rounded-full blur-md opacity-0 group-hover:opacity-100 transition-opacity"></div>
            </div>
            <h3 class="text-xl font-serif italic text-white/90 mb-2">"Establishing a secure dialogue."</h3>
            <h4 class="text-lg font-bold text-emerald-500 mb-3 tracking-wide">The Handshake</h4>
            <p class="text-slate-400 text-sm leading-relaxed flex-grow">
              The framework instantly validates your API key locally. Once verified, the connection to the engine is established and the session begins seamlessly.
            </p>
          </div>

          <!-- Card 3 -->
          <div class="snap-center shrink-0 w-full md:w-[calc(50%-12px)] lg:w-[calc(33.333%-16px)] bg-[#020617]/40 backdrop-blur-md border border-slate-800/80 rounded-[2rem] p-8 shadow-2xl flex flex-col group hover:border-indigo-500/50 transition-colors duration-500">
            <div class="w-12 h-12 rounded-full border-2 border-indigo-500/30 bg-indigo-950/30 flex items-center justify-center text-indigo-400 font-mono text-sm mb-6 relative">
              03
              <div class="absolute inset-0 bg-indigo-500/20 rounded-full blur-md opacity-0 group-hover:opacity-100 transition-opacity"></div>
            </div>
            <h3 class="text-xl font-serif italic text-white/90 mb-2">"Answer with your first instinct."</h3>
            <h4 class="text-lg font-bold text-indigo-400 mb-3 tracking-wide">The Assessment</h4>
            <p class="text-slate-400 text-sm leading-relaxed flex-grow">
              You will face <strong class="text-slate-300">21 multiple-choice questions</strong> designed to probe your development habits, mathematically distributed across psychoanalytical domains.
            </p>
          </div>

          <!-- Card 4 -->
          <div class="snap-center shrink-0 w-full md:w-[calc(50%-12px)] lg:w-[calc(33.333%-16px)] bg-[#020617]/40 backdrop-blur-md border border-slate-800/80 rounded-[2rem] p-8 shadow-2xl flex flex-col group hover:border-purple-500/50 transition-colors duration-500">
            <div class="w-12 h-12 rounded-full border-2 border-purple-500/30 bg-purple-950/30 flex items-center justify-center text-purple-400 font-mono text-sm mb-6 relative">
              04
              <div class="absolute inset-0 bg-purple-500/20 rounded-full blur-md opacity-0 group-hover:opacity-100 transition-opacity"></div>
            </div>
            <h3 class="text-xl font-serif italic text-white/90 mb-2">"Confront your hidden patterns."</h3>
            <h4 class="text-lg font-bold text-purple-400 mb-3 tracking-wide">The Core Dump</h4>
            <p class="text-slate-400 text-sm leading-relaxed flex-grow">
              At the end of the questions, the engine processes your choices and outputs a brutally honest, deeply personal psychological profile of you as a developer.
            </p>
          </div>

        </div>

        <!-- Pagination Dots -->
        <div class="flex justify-center gap-2 mt-4 md:hidden">
          <button 
            v-for="index in 4" :key="index"
            @click="scrollToCard(index - 1)"
            class="w-2.5 h-2.5 rounded-full transition-colors duration-300"
            :class="activeIndex === (index - 1) ? 'bg-blue-500' : 'bg-slate-800'"
          ></button>
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
        <div class="mt-6 max-w-3xl text-center px-4">
          <p class="text-slate-600 text-[10px] md:text-[11px] leading-relaxed font-mono uppercase tracking-widest opacity-60">
            <strong class="text-slate-500">Disclaimer:</strong> FreudLens is an experimental platform designed to test AI agent technologies. It does not provide medical advice, psychiatric diagnosis, or treatment. This experience is strictly for entertainment and technological evaluation purposes and should never substitute professional psychological consultation.
          </p>
        </div>
      </div>

    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const carouselRef = ref(null)
const activeIndex = ref(0)

const start = () => {
  router.push('/questionnaire')
}

const scrollNext = () => {
  if (carouselRef.value) {
    const cardWidth = carouselRef.value.offsetWidth
    carouselRef.value.scrollBy({ left: cardWidth, behavior: 'smooth' })
  }
}

const scrollPrev = () => {
  if (carouselRef.value) {
    const cardWidth = carouselRef.value.offsetWidth
    carouselRef.value.scrollBy({ left: -cardWidth, behavior: 'smooth' })
  }
}

const scrollToCard = (index) => {
  if (carouselRef.value) {
    const cardWidth = carouselRef.value.offsetWidth
    carouselRef.value.scrollTo({ left: cardWidth * index, behavior: 'smooth' })
  }
}

const handleScroll = () => {
  if (carouselRef.value) {
    const scrollLeft = carouselRef.value.scrollLeft
    const cardWidth = carouselRef.value.offsetWidth
    activeIndex.value = Math.round(scrollLeft / cardWidth)
  }
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
