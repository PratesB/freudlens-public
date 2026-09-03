<template>
  <section id="software" class="py-24 lg:py-32 bg-[#020617] relative border-t border-blue-900/20">
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_top,_var(--tw-gradient-stops))] from-blue-900/5 via-[#020617] to-[#020617] pointer-events-none"></div>

    <div class="max-w-6xl mx-auto px-6 relative z-10">
      
      <!-- Grand Intro Statement -->
      <div class="mb-16 lg:mb-24 reveal-on-scroll text-center px-4 md:px-12">
        <div class="relative inline-block max-w-4xl mx-auto">
          <svg class="absolute -top-10 -left-6 md:-left-12 w-20 h-20 text-blue-900/30 transform -rotate-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h3.983v10h-9.983z"/></svg>
          <p class="text-3xl md:text-4xl lg:text-5xl font-serif italic text-white leading-[1.4] md:leading-[1.4] relative z-10">
            "If you think about it, software is an extension of our cognition. <strong class="text-blue-400 not-italic font-black">Software Engineering</strong> and <strong class="text-blue-400 not-italic font-black">Psychoanalysis</strong> share some surprisingly real, and fascinating, parallels."
          </p>
        </div>
      </div>

          <!-- Clinical Notebook (Midnight Slate Version) -->
      <div class="max-w-2xl mx-auto reveal-on-scroll perspective-1000">
        
        <div 
          class="relative bg-[#0b1021] rounded-r-3xl rounded-l-sm shadow-[0_20px_60px_rgba(0,0,0,0.8),inset_2px_0_10px_rgba(255,255,255,0.02)] border-l-[24px] border-[#04060d] min-h-[600px] overflow-hidden flex flex-col transform-gpu rotate-y-2 select-none"
          @touchstart="handleTouchStart"
          @touchend="handleTouchEnd"
        >
          
          <!-- Leather Spine Highlight -->
          <div class="absolute top-0 bottom-0 left-0 w-2 bg-gradient-to-r from-white/10 to-transparent z-20 pointer-events-none"></div>
          
          <!-- Subtle Paper Texture Overlay -->
          <div class="absolute inset-0 opacity-[0.03] pointer-events-none mix-blend-screen" style="background-image: url('data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noiseFilter%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%220.8%22 numOctaves=%224%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noiseFilter)%22/%3E%3C/svg%3E');"></div>
          
          <!-- Ruled Lines Background -->
          <div class="absolute inset-0 top-[60px] bg-[linear-gradient(transparent_95%,rgba(255,255,255,0.03)_95%)] bg-[length:100%_2rem] pointer-events-none z-0"></div>

          <!-- Vertical Margin Line (Subtle Cyan/Blue instead of Red to harmonize) -->
          <div class="absolute top-0 bottom-0 left-12 w-px bg-blue-500/20 z-0 pointer-events-none hidden md:block"></div>

          <!-- Notebook Header -->
          <div class="border-b border-white/5 px-6 md:px-16 py-4 flex justify-between items-center text-slate-500 font-mono text-xs md:text-sm relative z-10 bg-[#0b1021]">
            <span>Subject: Dev Analysis</span>
            <span>Date: {{ new Date().toLocaleDateString() }}</span>
            <span>Page: 0{{ currentPage + 1 }}/04</span>
          </div>

          <!-- Notebook Body (Pages) -->
          <div class="flex-grow relative z-10 px-6 md:px-16 py-8 pb-28">
            
            <transition :name="transitionDirection" mode="out-in">
              
              <!-- PAGE 1 -->
              <div v-if="currentPage === 0" :key="0" class="h-full pt-2">
                <div class="text-blue-400 font-serif italic text-2xl md:text-3xl font-bold mb-8 border-b border-white/10 inline-block pb-1">
                  1. The Developer's Psyche
                </div>
                <div class="space-y-8 font-serif text-slate-300 text-lg leading-relaxed">
                  <p>
                    <strong class="font-bold text-slate-100">The Id (The Hacker):</strong> The impulsive voice screaming <em>"Deploy to prod now! Ignore the architecture, I want results!"</em>
                  </p>
                  <p>
                    <strong class="font-bold text-slate-100">The Superego (The Architect):</strong> The strict technical morality. <em>"You cannot push this without 100% test coverage and perfect SOLID principles."</em>
                  </p>
                  <p>
                    <strong class="font-bold text-slate-100">The Ego (You):</strong> The pragmatic developer sweating in the middle, trying to write acceptable code that pleases the Architect while meeting the Hacker's Sprint deadline.
                  </p>
                </div>
              </div>

              <!-- PAGE 2 -->
              <div v-else-if="currentPage === 1" :key="1" class="h-full pt-2">
                <div class="text-blue-400 font-serif italic text-2xl md:text-3xl font-bold mb-8 border-b border-white/10 inline-block pb-1">
                  2. Legacy Code = The Unconscious
                </div>
                <div class="space-y-8 font-serif text-slate-300 text-lg leading-relaxed">
                  <p>
                    The <strong class="text-slate-100">Conscious Mind</strong> is your shiny new Frontend: polished, modern, and exactly what the user sees and understands.
                  </p>
                  <p>
                    The <strong class="text-slate-100">Unconscious</strong> is that undocumented 5-year-old backend full of technical debt. Nobody wants to look at it, the team represses its existence, but when it fails, it brings the entire system down inexplicably.
                  </p>
                  <div class="mt-8 p-4 bg-slate-900/50 border-l-2 border-blue-500/50 rounded-r font-mono text-sm text-slate-400">
                    > Observation: Repressing tech debt leads to system-wide neurosis (crashes).
                  </div>
                </div>
              </div>

              <!-- PAGE 3 -->
              <div v-else-if="currentPage === 2" :key="2" class="h-full pt-2">
                <div class="text-blue-400 font-serif italic text-2xl md:text-3xl font-bold mb-8 border-b border-white/10 inline-block pb-1">
                  3. Defense Mechanisms
                </div>
                <div class="space-y-8 font-serif text-slate-300 text-lg leading-relaxed">
                  <div>
                    <strong class="font-bold text-blue-300">Denial:</strong><br>
                    <em class="text-slate-100">"It works on my machine."</em><br>
                    <span class="text-sm text-slate-500">Refusing to accept the objective reality of a failing system.</span>
                  </div>
                  <div>
                    <strong class="font-bold text-blue-300">Projection:</strong><br>
                    <em class="text-slate-100">"It's not my code's fault, this open-source library is just bad."</em><br>
                    <span class="text-sm text-slate-500">Attributing your own logical errors to external dependencies.</span>
                  </div>
                  <div>
                    <strong class="font-bold text-blue-300">Rationalization:</strong><br>
                    <em class="text-slate-100">"I didn't write tests because the deadline was too tight."</em><br>
                    <span class="text-sm text-slate-500">Creating logical, seemingly valid excuses for poor technical behavior.</span>
                  </div>
                </div>
              </div>

              <!-- PAGE 4 -->
              <div v-else-if="currentPage === 3" :key="3" class="h-full pt-2">
                <div class="text-blue-400 font-serif italic text-2xl md:text-3xl font-bold mb-8 border-b border-white/10 inline-block pb-1">
                  4. Therapy is Just Debugging
                </div>
                <div class="space-y-8 font-serif text-slate-300 text-lg leading-relaxed">
                  <p>
                    Psychoanalysis consists of pulling the thread of a symptom until you find the original trauma, the <strong class="text-slate-100">Root Cause</strong>.
                  </p>
                  <p>
                    This is exactly what we do when looking at a Stack Trace. We traverse the layers of code until we find the deeply buried bug in the logic.
                  </p>
                  <div class="mt-16 text-center text-slate-500 italic font-serif">
                    "To debug is to psychoanalyze the machine."
                  </div>
                </div>
              </div>

            </transition>
          </div>

          <!-- Navigation Controls (Desktop) -->
          <div class="absolute bottom-6 left-0 w-full hidden md:flex justify-between items-center px-6 md:px-16 z-20">
            <button 
              @click="prevPage" 
              :class="currentPage === 0 ? 'opacity-0 pointer-events-none' : 'opacity-100 hover:text-blue-400 cursor-pointer'"
              class="flex items-center gap-2 text-slate-500 font-mono text-xs uppercase tracking-wider transition-all"
            >
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" /></svg>
              Turn Back
            </button>
            <div class="flex gap-2">
              <button 
                v-for="n in 4" :key="n"
                @click="goToPage(n - 1)"
                class="w-1.5 h-1.5 rounded-full transition-colors cursor-pointer"
                :class="currentPage === (n - 1) ? 'bg-blue-500 shadow-[0_0_8px_rgba(59,130,246,0.8)]' : 'bg-slate-700'"
              ></button>
            </div>
            <button 
              @click="nextPage" 
              :class="currentPage === 3 ? 'opacity-0 pointer-events-none' : 'opacity-100 hover:text-blue-400 cursor-pointer'"
              class="flex items-center gap-2 text-slate-500 font-mono text-xs uppercase tracking-wider transition-all"
            >
              Turn Page
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
            </button>
          </div>

          <!-- Mobile Swipe Indicator -->
          <div class="absolute bottom-6 left-0 w-full flex flex-col md:hidden justify-center items-center gap-3 z-20 pointer-events-none">
            <div class="flex items-center gap-2 text-slate-500 font-mono text-[10px] uppercase tracking-widest" v-if="currentPage < 3">
              Swipe to turn page 
              <svg class="w-3 h-3 animate-[swipeHint_2s_infinite]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
            </div>
            <div class="flex justify-center items-center gap-2">
              <div 
                v-for="n in 4" :key="'m'+n"
                class="w-1.5 h-1.5 rounded-full transition-colors"
                :class="currentPage === (n - 1) ? 'bg-blue-500 shadow-[0_0_8px_rgba(59,130,246,0.8)]' : 'bg-slate-700'"
              ></div>
            </div>
          </div>
          
        </div>
      </div>
      
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const currentPage = ref(0)
const transitionDirection = ref('slide-left')

// Swipe logic
const touchStartX = ref(0)
const touchEndX = ref(0)

const handleTouchStart = (e) => {
  touchStartX.value = e.changedTouches[0].screenX
}

const handleTouchEnd = (e) => {
  touchEndX.value = e.changedTouches[0].screenX
  handleSwipe()
}

const handleSwipe = () => {
  const swipeThreshold = 50 // minimum distance to be considered a swipe
  if (touchEndX.value < touchStartX.value - swipeThreshold) {
    nextPage()
  }
  if (touchEndX.value > touchStartX.value + swipeThreshold) {
    prevPage()
  }
}

const nextPage = () => {
  if (currentPage.value < 3) {
    transitionDirection.value = 'slide-left'
    currentPage.value++
  }
}

const prevPage = () => {
  if (currentPage.value > 0) {
    transitionDirection.value = 'slide-right'
    currentPage.value--
  }
}

const goToPage = (index) => {
  transitionDirection.value = index > currentPage.value ? 'slide-left' : 'slide-right'
  currentPage.value = index
}
</script>

<style scoped>
/* Slide Left (Next) */
.slide-left-enter-active,
.slide-left-leave-active {
  transition: opacity 0.4s ease, transform 0.4s ease;
}
.slide-left-enter-from {
  opacity: 0;
  transform: translateX(15px);
}
.slide-left-leave-to {
  opacity: 0;
  transform: translateX(-15px);
}

/* Slide Right (Prev) */
.slide-right-enter-active,
.slide-right-leave-active {
  transition: opacity 0.4s ease, transform 0.4s ease;
}
.slide-right-enter-from {
  opacity: 0;
  transform: translateX(-15px);
}
.slide-right-leave-to {
  opacity: 0;
  transform: translateX(15px);
}

@keyframes swipeHint {
  0%, 100% { transform: translateX(0); opacity: 0.3; }
  50% { transform: translateX(4px); opacity: 1; }
}
</style>
