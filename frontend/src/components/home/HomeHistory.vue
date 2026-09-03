<template>
  <section id="history" class="py-24 bg-[#020617] scroll-mt-10">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-8 items-center reveal-on-scroll">
      
      <!-- Left: Image -->
      <div class="lg:col-span-5 relative rounded-3xl overflow-hidden shadow-[0_20px_50px_rgba(0,0,0,0.5)] border border-blue-900/20 group h-full min-h-[500px]">
        <!-- Image -->
        <img src="/freud-portrait.jpg" alt="Sigmund Freud" class="w-full h-full object-cover absolute inset-0 transition-transform duration-700 group-hover:scale-105" />
        <!-- Dark blue overlay to match UI -->
        <div class="absolute inset-0 bg-[#050b1a]/30 mix-blend-multiply"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-[#020617] via-[#020617]/40 to-transparent"></div>
        
        <!-- Archive Badge -->
        <div class="absolute bottom-6 left-6 right-6 p-5 rounded-xl bg-[#0a1128]/80 backdrop-blur-md border border-blue-900/40">
          <div class="flex items-center justify-between text-[10px] font-bold text-blue-400 tracking-wider uppercase mb-2">
            <span>Archive Ref: SF-1856-1939</span>
            <span>Vienna, Austria</span>
          </div>
          <h4 class="text-white font-semibold text-lg">Sigmund Freud, M.D.</h4>
          <p class="text-slate-400 text-xs mt-1">Pioneer of Free Association & The Architecture of the Unconscious.</p>
        </div>
      </div>

      <!-- Right: Content -->
      <div class="lg:col-span-7 flex flex-col justify-center space-y-10 lg:pl-10">
        
        <!-- Headers -->
        <div>
          <span class="text-blue-400 text-xs font-bold tracking-[0.2em] uppercase mb-3 block">The Origins</span>
          <h2 class="text-4xl lg:text-5xl font-bold text-white tracking-tight">The Father of Psychoanalysis</h2>
        </div>

        <!-- Paragraph -->
        <div class="space-y-6 text-lg text-slate-300 leading-relaxed font-light">
          <p>
            <strong class="text-white font-medium">Sigmund Freud (1856–1939)</strong> was an Austrian neurologist who revolutionized how humanity understands itself. Before him, humans were believed to be driven solely by conscious reason. Freud revealed that a vast hidden ocean lies within us: <span class="text-blue-400 font-semibold">the Unconscious</span>.
          </p>
          <p>
            He pioneered Psychoanalysis, a clinical framework for exploring psychopathology through dialogue, demonstrating that our repressed desires, fears, and childhood impressions sculpt who we become today.
          </p>
        </div>

        <!-- Legacy Timeline Cards -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-4">
          
          <div class="bg-[#0a1128]/50 p-5 rounded-xl border border-blue-900/30 hover:border-blue-700/50 transition-colors">
            <span class="text-blue-400 font-mono text-sm font-bold block mb-2">1895</span>
            <h4 class="text-white font-semibold text-sm mb-2">The Couch & Association</h4>
            <p class="text-slate-400 text-xs leading-relaxed">
              Invention of the talking cure, stripping away conscious defenses through uncensored speech.
            </p>
          </div>

          <div class="bg-[#0a1128]/50 p-5 rounded-xl border border-blue-900/30 hover:border-blue-700/50 transition-colors">
            <span class="text-blue-400 font-mono text-sm font-bold block mb-2">1899</span>
            <h4 class="text-white font-semibold text-sm mb-2">Interpretation of Dreams</h4>
            <p class="text-slate-400 text-xs leading-relaxed">
              Unveiling dreams as the "royal road" to latent desires, displacement, and condensation.
            </p>
          </div>

          <div class="bg-[#0a1128]/50 p-5 rounded-xl border border-blue-900/30 hover:border-blue-700/50 transition-colors">
            <span class="text-blue-400 font-mono text-sm font-bold block mb-2">1923</span>
            <h4 class="text-white font-semibold text-sm mb-2">The Structural Model</h4>
            <p class="text-slate-400 text-xs leading-relaxed">
              Formalizing the human psyche into three interacting forces: Id, Ego, and Superego.
            </p>
          </div>

        </div>
      </div>
      
    </div>
  </section>
</template>

<script setup>
</script>
