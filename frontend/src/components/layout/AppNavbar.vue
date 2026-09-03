<template>
  <div 
    class="fixed left-0 w-full z-50 flex flex-col items-center px-4 md:px-6 pointer-events-none transition-all duration-500 ease-in-out gap-4"
    :class="isVisible ? 'top-6 translate-y-0 opacity-100' : '-top-20 -translate-y-full opacity-0'"
  >
    <nav class="pointer-events-auto w-full max-w-6xl relative bg-[#050b1a]/40 backdrop-blur-2xl border border-blue-500/20 rounded-full px-6 py-3 flex items-center justify-between shadow-[0_20px_40px_rgba(0,0,0,0.5)] transition-all duration-500">
      <!-- Logo -->
      <div class="flex items-center">
        <span class="font-bold text-lg text-white tracking-wide">FreudLens<sup class="text-[10px] font-normal text-blue-400 ml-0.5">®</sup></span>
      </div>
      
      <!-- Links (Desktop) -->
      <div class="hidden md:flex items-center gap-6 lg:gap-8 text-sm font-medium text-slate-300">
        <a href="#history" class="hover:text-blue-400 transition-colors">Who was Freud</a>
        <a href="#legacy" class="hover:text-blue-400 transition-colors">The Freudian Legacy</a>
        <a href="#software" class="hover:text-blue-400 transition-colors">Psychoanalysis of Code</a>
        <a href="#benefits" class="hover:text-blue-400 transition-colors">Value</a>
        <a href="#how-it-works" class="hover:text-blue-400 transition-colors">How it Works</a>
      </div>

      <!-- CTA & Mobile Menu Toggle -->
      <div class="flex items-center gap-3">
        <button @click="start" class="group relative overflow-hidden cursor-pointer text-[10px] sm:text-xs uppercase tracking-[0.15em] bg-[#03091e] hover:bg-[#051033] text-white font-medium py-2.5 px-6 rounded-full transition-all duration-500 border border-blue-500/30 hover:border-blue-400/60 shadow-[0_0_15px_rgba(59,130,246,0.1)] hover:shadow-[0_0_25px_rgba(59,130,246,0.4)]">
          <span class="relative z-10 flex items-center gap-2">
            Begin Session
            <svg class="w-3.5 h-3.5 text-blue-400 group-hover:translate-x-1 transition-transform duration-300" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
          </span>
          <!-- Subtle inner glow -->
          <div class="absolute inset-0 bg-blue-500/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500 blur-md pointer-events-none"></div>
        </button>
        
        <!-- Hamburger Button -->
        <button @click="isMobileMenuOpen = !isMobileMenuOpen" class="cursor-pointer md:hidden text-slate-300 hover:text-white p-1 transition-colors outline-none focus:outline-none">
          <svg v-if="!isMobileMenuOpen" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
          <svg v-else xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>
    </nav>
    
    <!-- Mobile Menu Dropdown -->
    <div 
      class="md:hidden w-full max-w-6xl pointer-events-auto bg-[#050b1a]/90 backdrop-blur-3xl border border-blue-500/20 rounded-3xl shadow-[0_20px_40px_rgba(0,0,0,0.5)] transition-all duration-300 overflow-hidden"
      :class="isMobileMenuOpen ? 'max-h-[400px] opacity-100 border-opacity-100' : 'max-h-0 opacity-0 border-opacity-0 !border-0'"
    >
      <div class="flex flex-col p-6 gap-6 text-base font-medium text-slate-300">
        <a href="#history" @click="isMobileMenuOpen = false" class="hover:text-blue-400 transition-colors w-full border-b border-blue-900/30 pb-2">Who was Freud</a>
        <a href="#legacy" @click="isMobileMenuOpen = false" class="hover:text-blue-400 transition-colors w-full border-b border-blue-900/30 pb-2">The Freudian Legacy</a>
        <a href="#software" @click="isMobileMenuOpen = false" class="hover:text-blue-400 transition-colors w-full border-b border-blue-900/30 pb-2">Psychoanalysis of Code</a>
        <a href="#benefits" @click="isMobileMenuOpen = false" class="hover:text-blue-400 transition-colors w-full border-b border-blue-900/30 pb-2">Value</a>
        <a href="#how-it-works" @click="isMobileMenuOpen = false" class="hover:text-blue-400 transition-colors w-full pb-2">How it Works</a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const isVisible = ref(true)
const isMobileMenuOpen = ref(false)
let lastScrollY = 0

const handleScroll = () => {
  const currentScrollY = window.scrollY
  
  if (currentScrollY > 100) {
    // Hide if scrolling down, show if scrolling up
    isVisible.value = currentScrollY < lastScrollY
  } else {
    // Always show at the very top
    isVisible.value = true
  }
  
  // Hide navbar on scroll to menu mobile close
  if (!isVisible.value) {
    isMobileMenuOpen.value = false
  }
  
  lastScrollY = currentScrollY
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

const start = () => {
  isMobileMenuOpen.value = false
  router.push('/questionnaire')
}
</script>
