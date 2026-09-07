<template>
  <section id="software" class="py-24 lg:py-32 bg-[#020617] relative border-t border-blue-900/20 overflow-hidden">
    <!-- Diagnostic Background -->
    <div class="absolute inset-0 pointer-events-none">
      <!-- Grid overlay -->
      <div class="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.03)_1px,transparent_1px)] bg-[size:40px_40px] [mask-image:radial-gradient(ellipse_at_center,black,transparent_70%)]"></div>
      <!-- Core Glow -->
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-blue-600/10 rounded-full blur-[120px]"></div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      
      <!-- Grand Intro -->
      <div class="mb-16 lg:mb-24 reveal-on-scroll text-center px-4 md:px-12">
        <div class="relative inline-block max-w-4xl mx-auto">
          <svg class="absolute -top-10 -left-6 md:-left-12 w-20 h-20 text-blue-900/30 transform -rotate-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h3.983v10h-9.983z"/></svg>
          <p class="text-3xl md:text-4xl lg:text-5xl font-serif italic text-white leading-[1.4] md:leading-[1.4] relative z-10">
            "If you think about it, software is an extension of our cognition. <strong class="text-blue-400 not-italic font-black">Software Engineering</strong> and <strong class="text-blue-400 not-italic font-black">Psychoanalysis</strong> offer surprisingly faithful, and fascinating, parallels."
          </p>
        </div>
      </div>

      <!-- Diagnostic Scanner Interface -->
      <div class="max-w-5xl mx-auto reveal-on-scroll">
        <div 
          class="bg-[#050b14]/90 backdrop-blur-2xl rounded-2xl border border-blue-500/20 shadow-[0_0_50px_rgba(0,0,0,0.8),inset_0_0_20px_rgba(59,130,246,0.05)] overflow-hidden flex flex-col md:flex-row min-h-[600px] md:min-h-[500px]"
          @touchstart="handleTouchStart"
          @touchend="handleTouchEnd"
        >
          
          <!-- Sidebar Navigation -->
          <div class="w-full md:w-1/3 bg-black/40 border-b md:border-b-0 md:border-r border-blue-500/10 p-6 flex flex-col">
            <div class="mb-8 hidden md:block">
              <div class="text-[10px] uppercase tracking-[0.3em] text-blue-500/70 font-mono mb-2 flex items-center gap-2">
                <span class="w-2 h-2 bg-blue-500 rounded-full animate-pulse"></span>
                System Diagnostic
              </div>
              <div class="text-xs text-slate-500 font-mono">Target: Developer Psyche</div>
            </div>

            <!-- Layer Buttons -->
            <div 
              class="flex md:flex-col overflow-x-auto md:overflow-visible gap-2 md:gap-4 pb-4 md:pb-0 hide-scrollbar" 
              ref="layerButtonsContainer"
            >
              <button 
                v-for="(layer, index) in layers" :key="index"
                :ref="el => buttonRefs[index] = el"
                @click="goToLayer(index)"
                :aria-selected="currentLayer === index"
                class="flex-shrink-0 text-left px-4 py-4 rounded-lg font-mono text-sm transition-all duration-300 relative overflow-hidden group border cursor-pointer"
                :class="currentLayer === index ? 'bg-blue-900/20 border-blue-500/50 text-blue-300 shadow-[inset_0_0_15px_rgba(59,130,246,0.2)]' : 'bg-transparent border-transparent text-slate-500 hover:text-slate-300 hover:bg-white/5'"
              >
                <!-- Active Indicator Line -->
                <div 
                  class="absolute left-0 top-0 bottom-0 w-1 bg-blue-500 transition-transform duration-300 hidden md:block"
                  :class="currentLayer === index ? 'translate-y-0' : '-translate-y-full'"
                ></div>
                <!-- Mobile active indicator (bottom line) -->
                <div 
                  class="absolute left-0 bottom-0 right-0 h-1 bg-blue-500 transition-transform duration-300 md:hidden"
                  :class="currentLayer === index ? 'translate-x-0' : '-translate-x-full'"
                ></div>
                
                <div class="flex items-center gap-3">
                  <span class="opacity-50 text-xs">L-0{{ index + 1 }}</span>
                  <span class="font-bold tracking-wide uppercase">{{ layer.title }}</span>
                </div>
              </button>
            </div>
            
            <div class="mt-auto hidden md:block pt-8 border-t border-white/5 text-[10px] text-slate-600 font-mono">
              STATUS: <span class="text-blue-400">ANALYZING...</span><br>
              DEPTH: 0{{ currentLayer + 1 }} / 04
            </div>
          </div>

          <!-- Main Diagnostic Content -->
          <div class="w-full md:w-2/3 p-8 md:p-12 relative flex flex-col bg-[radial-gradient(ellipse_at_top_right,rgba(59,130,246,0.05),transparent_50%)]">
            
            <!-- Scanning Laser Line (purely visual) -->
            <div class="absolute top-0 left-0 w-full h-0.5 bg-blue-500/50 shadow-[0_0_10px_rgba(59,130,246,1)] animate-[scan_4s_ease-in-out_infinite] z-20 pointer-events-none"></div>

            <div class="flex-grow relative z-10 flex flex-col justify-center">
              <transition :name="transitionName" mode="out-in">
                
                <!-- CONTENT BLOCKS -->
                
                <!-- Layer 1 -->
                <div v-if="currentLayer === 0" :key="0" class="w-full">
                  <h3 class="text-2xl md:text-3xl font-mono text-white mb-8 pb-4 border-b border-white/10">
                    <span class="text-blue-500">></span> The Developer's Psyche
                  </h3>
                  <div class="space-y-8 font-serif text-slate-300 text-lg leading-relaxed">
                    <p>
                      <strong class="font-sans font-bold text-white tracking-wide">The Id (The Coder):</strong><br>
                      Driven by the pleasure principle, seeking immediate satisfaction. <em class="text-slate-400">"Just make it work! We can worry about the architecture later."</em>
                    </p>
                    <p>
                      <strong class="font-sans font-bold text-white tracking-wide">The Superego (The Architect):</strong><br>
                      Our internalized technical ideals, prohibitions, and strict standards. <em class="text-slate-400">"You cannot push this without 100% test coverage and perfect SOLID principles."</em>
                    </p>
                    <p>
                      <strong class="font-sans font-bold text-blue-300">The Ego (The Engineer):</strong><br>
                      The reality principle. The pragmatic developer sweating in the middle, trying to mediate between the Coder's impulses and the Architect's rigid demands.
                    </p>
                  </div>
                </div>

                <!-- Layer 2 -->
                <div v-else-if="currentLayer === 1" :key="1" class="w-full">
                  <h3 class="text-2xl md:text-3xl font-mono text-white mb-8 pb-4 border-b border-white/10">
                    <span class="text-blue-500">></span> Legacy Code = The Unconscious
                  </h3>
                  <div class="space-y-6 font-serif text-slate-300 text-lg leading-relaxed">
                    <p>
                      The <strong class="text-white">Conscious Mind</strong> is your shiny new Frontend: polished, modern, and exactly what the user sees and understands.
                    </p>
                    <p>
                      The <strong class="text-blue-300">Unconscious</strong> is that undocumented 5-year-old legacy backend. It is not just a repository of tech debt, it's a complex layer that remains out of daily awareness but continuously influences the system's behavior.
                    </p>
                    <div class="mt-8 p-4 bg-blue-900/10 border-l-2 border-blue-500 font-mono text-sm text-blue-200/80">
                      [WARNING]: Legacy systems, much like unconscious contents, operate behind the scenes. When unmanaged, they produce systemic neuroses (inexplicable crashes).
                    </div>
                  </div>
                </div>

                <!-- Layer 3 -->
                <div v-else-if="currentLayer === 2" :key="2" class="w-full">
                  <h3 class="text-2xl md:text-3xl font-mono text-white mb-8 pb-4 border-b border-white/10">
                    <span class="text-blue-500">></span> Defense Mechanisms
                  </h3>
                  <div class="space-y-8 font-serif text-slate-300 text-lg leading-relaxed">
                    <div>
                      <strong class="font-sans font-bold text-white tracking-wide text-xl">Denial:</strong><br>
                      <em class="text-blue-200">"It works on my machine."</em><br>
                      <span class="text-sm text-slate-500 font-mono mt-1 block">Refusing to accept the objective reality of a failing system.</span>
                    </div>
                    <div>
                      <strong class="font-sans font-bold text-white tracking-wide text-xl">Projection:</strong><br>
                      <em class="text-blue-200">"It's not my code's fault, this open-source library is just bad."</em><br>
                      <span class="text-sm text-slate-500 font-mono mt-1 block">Attributing your own logical errors to external dependencies.</span>
                    </div>
                    <div>
                      <strong class="font-sans font-bold text-white tracking-wide text-xl">Rationalization:</strong><br>
                      <em class="text-blue-200">"I didn't write tests because the deadline was too tight."</em><br>
                      <span class="text-sm text-slate-500 font-mono mt-1 block">Constructing a seemingly logical explanation to justify a decision whose true motivation is different.</span>
                    </div>
                  </div>
                </div>

                <!-- Layer 4 -->
                <div v-else-if="currentLayer === 3" :key="3" class="w-full">
                  <h3 class="text-2xl md:text-3xl font-mono text-white mb-8 pb-4 border-b border-white/10">
                    <span class="text-blue-500">></span> Therapy is Just Debugging
                  </h3>
                  <div class="space-y-8 font-serif text-slate-300 text-lg leading-relaxed">
                    <p>
                      <strong class="text-white">Psychoanalysis</strong> seeks to understand the underlying processes that produce symptoms, rather than just treating the surface.
                    </p>
                    <p>
                      Similarly, when we look at a <strong class="text-blue-300">Stack Trace</strong>, we use it as a metaphor to move beyond the observable error and investigate the deeper processes that produced it.
                    </p>
                    <div class="mt-12 p-6 border border-blue-500/20 bg-blue-900/10 rounded-lg text-center shadow-[inset_0_0_20px_rgba(59,130,246,0.1)]">
                      <div class="text-blue-400 font-mono text-sm mb-4">FINAL DIAGNOSIS</div>
                      <div class="text-xl md:text-2xl text-white italic font-serif">
                        "To debug is to psychoanalyze the machine."
                      </div>
                    </div>
                  </div>
                </div>

              </transition>
            </div>
            

          </div>
        </div>
      </div>
      
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const currentLayer = ref(0)
const transitionName = ref('scan-up') // Initial transition
const buttonRefs = ref([])
const layerButtonsContainer = ref(null)

const layers = [
  { title: 'The Psyche' },
  { title: 'The Unconscious' },
  { title: 'Defenses' },
  { title: 'Resolution' }
]

const goToLayer = (index) => {
  if (index === currentLayer.value) return;
  // If moving down the list (e.g. 0 to 1), text scans UP to reveal what's below
  transitionName.value = index > currentLayer.value ? 'scan-up' : 'scan-down'
  currentLayer.value = index

  // Scroll button into view safely without shifting the whole page
  if (buttonRefs.value[index] && layerButtonsContainer.value) {
    const btn = buttonRefs.value[index]
    const container = layerButtonsContainer.value
    
    // Only scroll horizontally if on mobile (container can scroll)
    if (window.innerWidth < 768) {
      const scrollPos = btn.offsetLeft - (container.offsetWidth / 2) + (btn.offsetWidth / 2)
      container.scrollTo({
        left: scrollPos,
        behavior: 'smooth'
      })
    }
  }
}

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
    if (currentLayer.value < layers.length - 1) goToLayer(currentLayer.value + 1)
  }
  if (touchEndX.value > touchStartX.value + swipeThreshold) {
    if (currentLayer.value > 0) goToLayer(currentLayer.value - 1)
  }
}
</script>

<style scoped>
/* Scan Up (Moving deeper, text comes from below) */
.scan-up-enter-active,
.scan-up-leave-active {
  transition: opacity 0.5s ease, transform 0.5s ease;
}
.scan-up-enter-from {
  opacity: 0;
  transform: translateY(20px);
}
.scan-up-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

/* Scan Down (Moving shallower, text comes from above) */
.scan-down-enter-active,
.scan-down-leave-active {
  transition: opacity 0.5s ease, transform 0.5s ease;
}
.scan-down-enter-from {
  opacity: 0;
  transform: translateY(-20px);
}
.scan-down-leave-to {
  opacity: 0;
  transform: translateY(20px);
}

/* Visual Laser Scan Effect */
@keyframes scan {
  0% { top: 0%; opacity: 0; }
  10% { opacity: 1; }
  90% { opacity: 1; }
  100% { top: 100%; opacity: 0; }
}

/* Hide scrollbar for the mobile horizontal nav */
.hide-scrollbar::-webkit-scrollbar {
  display: none;
}
.hide-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>
