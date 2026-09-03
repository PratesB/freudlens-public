<template>
  <div>
    <!-- The Freudian Legacy -->
    <section id="legacy" class="py-24 lg:py-32 bg-[#050b1a] relative overflow-hidden scroll-mt-10 border-t border-blue-900/20">
      
      <!-- Background Ambient Glow -->
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-blue-900/10 rounded-full blur-[150px] pointer-events-none"></div>

      <div class="max-w-7xl mx-auto px-6 relative z-10 flex flex-col items-center reveal-on-scroll">
        
        <div class="text-center max-w-3xl mb-20 space-y-4">
          <span class="text-blue-400 text-xs font-bold tracking-[0.3em] uppercase block">The Freudian Legacy</span>
          <h2 class="text-4xl lg:text-5xl font-bold text-white tracking-tight drop-shadow-md">His Contributions to the World</h2>
          <p class="text-slate-400 font-light text-lg md:text-xl leading-relaxed">
            He didn't just map the mind; he gave humanity the vocabulary to understand it. These three discoveries permanently altered the course of human thought.
          </p>
        </div>

        <!-- 3-Column Glass Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 w-full">
          
          <!-- Concept 1 -->
          <div class="relative rounded-[2rem] p-8 md:p-10 backdrop-blur-3xl shadow-[0_20px_40px_rgba(0,0,0,0.4),inset_0_1px_1px_rgba(255,255,255,0.1)] border border-white/5 bg-gradient-to-br from-[#020617]/90 to-blue-900/10 hover:-translate-y-2 transition-transform duration-500 group overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-tr from-transparent via-white/[0.04] to-transparent pointer-events-none opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
            
            <div class="relative z-10">
              <h4 class="text-2xl font-bold text-white mb-4 tracking-tight">The Unconscious</h4>
              <div class="w-12 h-px bg-gradient-to-r from-blue-500 to-transparent mb-6"></div>
              <p class="text-base text-slate-300 leading-relaxed font-light">
                The realization that our conscious choices are merely the tip of the iceberg. Beneath the surface lies a vast repository of drives, fears, and memories that secretly govern our behavior.
              </p>
            </div>
          </div>

          <!-- Concept 2 -->
          <div class="relative rounded-[2rem] p-8 md:p-10 backdrop-blur-3xl shadow-[0_20px_40px_rgba(0,0,0,0.4),inset_0_1px_1px_rgba(255,255,255,0.1)] border border-white/5 bg-gradient-to-b from-[#020617]/90 to-blue-900/10 hover:-translate-y-2 transition-transform duration-500 group overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-tr from-transparent via-white/[0.04] to-transparent pointer-events-none opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
            
            <div class="relative z-10">
              <h4 class="text-2xl font-bold text-white mb-4 tracking-tight">Defense Mechanisms</h4>
              <div class="w-12 h-px bg-gradient-to-r from-blue-500 to-transparent mb-6"></div>
              <p class="text-base text-slate-300 leading-relaxed font-light">
                Concepts like <em class="text-white font-medium">Denial</em>, <em class="text-white font-medium">Repression</em>, and <em class="text-white font-medium">Projection</em> were identified by Freud as the mind's automatic software to protect the Ego from unbearable anxiety and emotional pain.
              </p>
            </div>
          </div>

          <!-- Concept 3 -->
          <div class="relative rounded-[2rem] p-8 md:p-10 backdrop-blur-3xl shadow-[0_20px_40px_rgba(0,0,0,0.4),inset_0_1px_1px_rgba(255,255,255,0.1)] border border-white/5 bg-gradient-to-bl from-[#020617]/90 to-blue-900/10 hover:-translate-y-2 transition-transform duration-500 group overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-tr from-transparent via-white/[0.04] to-transparent pointer-events-none opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
            
            <div class="relative z-10">
              <h4 class="text-2xl font-bold text-white mb-4 tracking-tight">The Talking Cure</h4>
              <div class="w-12 h-px bg-gradient-to-r from-blue-500 to-transparent mb-6"></div>
              <p class="text-base text-slate-300 leading-relaxed font-light">
                He proved that psychological wounds cannot be treated with scalpels, but with words. Bringing hidden traumas into conscious dialogue is the ultimate path to mental liberation.
              </p>
            </div>
          </div>

        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
</script>
