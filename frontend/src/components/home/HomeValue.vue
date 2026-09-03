<template>
  <section id="benefits" class="py-32 lg:py-48 relative overflow-hidden bg-[#020617] border-t border-blue-900/20 flex flex-col items-center justify-center min-h-[80vh]">
    <!-- The FreudLens Effect (Giant Glowing Iris/Portal) -->
    <div class="absolute inset-0 flex items-center justify-center pointer-events-none overflow-hidden">
      <!-- Core glow -->
      <div class="absolute w-[60vw] h-[60vw] md:w-[40vw] md:h-[40vw] rounded-full bg-blue-600/10 blur-[100px] animate-[pulse_4s_ease-in-out_infinite]"></div>
      <!-- Lens rings -->
      <div class="absolute w-[30vw] h-[30vw] md:w-[20vw] md:h-[20vw] rounded-full border border-blue-500/20 opacity-50"></div>
      <div class="absolute w-[45vw] h-[45vw] md:w-[30vw] md:h-[30vw] rounded-full border border-blue-500/10 opacity-30"></div>
      <div class="absolute w-[70vw] h-[70vw] md:w-[50vw] md:h-[50vw] rounded-full border border-blue-900/10 opacity-20"></div>
      <!-- Scanline inside the lens -->
      <div class="absolute w-full h-[1px] bg-blue-500/30 top-1/2 -translate-y-1/2 blur-[2px]"></div>
    </div>

    <div class="max-w-6xl mx-auto px-6 text-center relative z-10">
      <span class="text-blue-400 text-xs font-bold tracking-[0.3em] uppercase block mb-10 reveal-on-scroll">
        The Value of Analysis
      </span>
      
      <!-- The Kinetic Assembly Manifesto -->
      <div class="mb-20 min-h-[250px] flex flex-wrap items-center justify-center content-center gap-x-2 gap-y-3 md:gap-y-4 text-2xl md:text-3xl lg:text-4xl font-bold text-white leading-relaxed md:leading-relaxed tracking-normal font-serif italic" ref="manifestoRef">
        <span 
          v-for="(word, index) in words" 
          :key="index"
          class="word inline-block transition-all duration-[2000ms] ease-[cubic-bezier(0.16,1,0.3,1)]"
          :class="isAssembled ? 'opacity-100 blur-0 translate-x-0 translate-y-0 rotate-0 scale-100' : 'opacity-0 blur-xl pointer-events-none'"
          :style="isAssembled ? { transitionDelay: `${index * 30}ms` } : { transform: `translate(${randomValues[index].x}px, ${randomValues[index].y}px) rotate(${randomValues[index].rot}deg) scale(${randomValues[index].scale})` }"
        >
          {{ word }}
        </span>
      </div>

      <div class="mt-8 text-center" :class="{ 'opacity-100 transition-opacity duration-1000 delay-[1500ms]': isAssembled, 'opacity-0': !isAssembled }">
        <!-- Action Container with Spinning Border -->
        <div class="group/button relative inline-block rounded-full p-[2px] overflow-hidden shadow-[0_10px_40px_rgba(0,0,0,0.8)] hover:shadow-[0_10px_40px_rgba(59,130,246,0.2)] transition-shadow duration-500 cursor-pointer">
          <!-- Spinning light border -->
          <div class="absolute top-1/2 left-1/2 w-[400%] aspect-square -translate-x-1/2 -translate-y-1/2 animate-[spin_3s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,transparent_0%,#3b82f6_50%,transparent_100%)] opacity-30 group-hover/button:opacity-100 transition-opacity duration-500 pointer-events-none"></div>

          <button 
            @click="start"
            class="cursor-pointer group relative overflow-hidden px-10 py-5 w-full h-full rounded-full bg-[#03091e] transition-colors duration-500 flex items-center justify-center gap-3 font-medium text-lg text-white font-sans not-italic"
          >
            <!-- Idle scanning light -->
            <div class="absolute pointer-events-none rounded-full bg-blue-500/40 blur-[30px] w-32 h-full top-0 animate-[sweep_2s_ease-in-out_infinite] transition-opacity duration-500"></div>

            <span class="relative z-10 whitespace-nowrap">Uncover My Patterns</span>
            <svg class="relative z-10 w-5 h-5 transition-transform duration-300 group-hover:translate-x-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M14 5l7 7m0 0l-7 7m7-7H3" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const manifestoRef = ref(null)

const start = () => {
  router.push('/questionnaire')
}

const finalText = "Freud didn't map the human mind for textbooks. He mapped it so we could break free from our own invisible patterns. Self-sabotage, burnout, the pursuit of perfection. That's your unconscious taking control. Stop reacting on autopilot. Start shaping your life and your state of mind with intention."

const words = finalText.split(' ')

// Pre-calculate random spread values for each word so they don't jump around on reactivity updates
const randomValues = words.map(() => ({
  x: (Math.random() - 0.5) * 600, // Spread between -300px and +300px
  y: (Math.random() - 0.5) * 600,
  rot: (Math.random() - 0.5) * 90, // Random rotation between -45 and 45 deg
  scale: 1 + Math.random() * 2 // Random scale between 1 and 3
}))

const isAssembled = ref(false)
let observer = null

onMounted(() => {
  observer = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      setTimeout(() => {
        isAssembled.value = true
      }, 100) // Small delay
      observer.disconnect()
    }
  }, { threshold: 0.4 }) // triggers when 40% of the element is visible

  if (manifestoRef.value) {
    observer.observe(manifestoRef.value)
  }
})

onBeforeUnmount(() => {
  if (observer) {
    observer.disconnect()
  }
})
</script>

<style scoped>
@keyframes sweep {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}
</style>
