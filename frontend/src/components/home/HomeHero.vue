<template>
  <section class="relative pt-40 pb-32 px-6 lg:pt-56 lg:pb-48 flex items-center justify-center overflow-hidden min-h-[90vh]">
    <!-- Video Background -->
    <div class="absolute inset-0 z-0">
      <video 
        src="/freudlens-video.mp4" 
        autoplay 
        loop 
        muted 
        playsinline 
        class="w-full h-full object-cover object-center scale-105"
      ></video>
      <!-- Gradients to blend video into the dark background and make text readable -->
      <div class="absolute inset-0 bg-[#020617]/70 backdrop-blur-[2px]"></div>
      <div class="absolute inset-0 bg-gradient-to-t from-[#020617] via-transparent to-[#020617]/50"></div>
      <div class="absolute inset-0 bg-gradient-to-r from-[#020617]/80 via-transparent to-[#020617]/80"></div>
    </div>
    
    <!-- Content -->
    <div class="max-w-5xl mx-auto relative z-10 text-center flex flex-col items-center">
      <h1 class="text-6xl md:text-7xl lg:text-[5.5rem] font-bold tracking-tight text-white leading-[1.05] drop-shadow-2xl mb-8">
        Discover the <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-300 to-blue-600">Mysteries</span><br class="hidden md:block"/> of Your Own Mind
      </h1>
      
      <p class="text-xl md:text-2xl text-slate-300 font-light leading-relaxed max-w-2xl mb-12 drop-shadow-lg">
        Your conscious mind is just the tip of the iceberg. Unveil the hidden patterns that shape your behavior, guided by the timeless principles of Sigmund Freud.
      </p>

      <!-- Action Area: Custom Mouse-Tracking Lens Button -->
      <div class="mt-10 flex flex-col items-center gap-6 w-full">
        
        <!-- Action Container with Spinning Border -->
        <div class="group/button relative rounded-full p-[2px] overflow-hidden shadow-[0_10px_40px_rgba(0,0,0,0.8)] hover:shadow-[0_10px_40px_rgba(59,130,246,0.2)] transition-shadow duration-500 cursor-pointer">
          <!-- Spinning light border -->
          <div class="absolute top-1/2 left-1/2 w-[400%] aspect-square -translate-x-1/2 -translate-y-1/2 animate-[spin_3s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,transparent_0%,#3b82f6_50%,transparent_100%)] opacity-30 group-hover/button:opacity-80 transition-opacity duration-500 pointer-events-none"></div>

          <button 
            ref="btnRef"
            @mousemove="handleMouseMove"
            @click="start"
            class="cursor-pointer group relative overflow-hidden px-12 py-5 w-full h-full rounded-full bg-[#03091e] transition-colors duration-500"
          >
            <!-- Idle scanning light (fades out on hover) -->
            <div class="absolute pointer-events-none rounded-full bg-blue-500/40 blur-[30px] w-32 h-full top-0 animate-idle-scan group-hover:opacity-0 transition-opacity duration-500"></div>

            <!-- Spotlight / Lens that follows the mouse -->
            <div 
              class="absolute pointer-events-none rounded-full bg-blue-500/40 blur-[25px] w-40 h-40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 transform -translate-x-1/2 -translate-y-1/2"
              :style="{ left: mouseX + 'px', top: mouseY + 'px' }"
            ></div>
            
            <!-- Button Text -->
            <span class="relative z-10 text-white font-light tracking-[0.25em] uppercase text-sm flex items-center justify-center gap-4 drop-shadow-md">
              Debug My Brain
              <svg class="transition-transform duration-500 group-hover:translate-x-3 group-hover:scale-110 text-blue-400" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
            </span>
          </button>
        </div>
        
        <!-- Security Badge & Explanation -->
        <div class="flex flex-col items-center gap-2 mt-5">
          <div class="inline-flex items-center justify-center gap-2 px-4 py-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/20 shadow-[0_0_15px_rgba(16,185,129,0.15)]">
            <svg class="text-emerald-400" xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <span class="text-xs font-semibold tracking-[0.1em] uppercase text-emerald-50">100% Private. <span class="text-emerald-200/80 font-medium">No data stored.</span></span>
          </div>
          <p class="text-[11px] text-slate-400/80 font-medium tracking-wide max-w-xs text-center leading-relaxed">
            Your API Key and answers never leave your device. Everything is processed locally in your browser.
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useButtonSpotlight } from '../../composables/useButtonSpotlight'

const router = useRouter()
const btnRef = ref(null)

const { mouseX, mouseY, handleMouseMove } = useButtonSpotlight(btnRef)

const start = () => {
  router.push('/questionnaire')
}
</script>

<style scoped>
@keyframes idleScan {
  0%, 100% { left: -50%; }
  50% { left: 150%; }
}
.animate-idle-scan {
  animation: idleScan 4s ease-in-out infinite;
}
</style>
