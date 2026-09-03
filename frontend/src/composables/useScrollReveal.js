import { onMounted } from 'vue'

export function useScrollReveal() {
  onMounted(() => {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible')
        }
      })
    }, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' })

    document.querySelectorAll('.reveal-on-scroll').forEach(el => revealObserver.observe(el))
  })
}
