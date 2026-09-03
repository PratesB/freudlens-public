<template>
  <div class="min-h-screen bg-[#020617] text-slate-300 font-sans selection:bg-blue-500/30 overflow-x-clip">
    
    <AppNavbar />
    
    <HomeHero />
    
    <HomeHistory />
    
    <HomeLegacy />
    
    <HomeComparison />
    
    <HomeValue />
    
    <HomeHowItWorks />
    
    <AppFooter />

  </div>
</template>

<script setup>
import { useScrollReveal } from '../composables/useScrollReveal'

// Import Layout Components
import AppNavbar from '../components/layout/AppNavbar.vue'
import AppFooter from '../components/layout/AppFooter.vue'

// Import Home Components
import HomeHero from '../components/home/HomeHero.vue'
import HomeHistory from '../components/home/HomeHistory.vue'
import HomeLegacy from '../components/home/HomeLegacy.vue'
import HomeComparison from '../components/home/HomeComparison.vue'
import HomeValue from '../components/home/HomeValue.vue'
import HomeHowItWorks from '../components/home/HomeHowItWorks.vue'

// Initialize global scroll animations
useScrollReveal()
</script>
