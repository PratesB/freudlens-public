import { ref, onMounted, onUnmounted } from 'vue'

export function useButtonSpotlight(btnRef) {
  const mouseX = ref(0)
  const mouseY = ref(0)

  const handleMouseMove = (e) => {
    if (!btnRef.value) return
    const rect = btnRef.value.getBoundingClientRect()
    mouseX.value = e.clientX - rect.left
    mouseY.value = e.clientY - rect.top
  }

  return {
    mouseX,
    mouseY,
    handleMouseMove
  }
}
