import { reactive, readonly } from 'vue'

const state = reactive({
  apiKey: '',
  isValidated: false,
  answers: {},
  analysisText: ''
})

export function useAppState() {
  const setApiKey = (key) => {
    state.apiKey = key
  }

  const setValidated = (status) => {
    state.isValidated = status
  }

  const saveAnswer = (questionId, answerText) => {
    state.answers[questionId] = answerText
  }
  
  const setAnalysis = (text) => {
    state.analysisText = text
  }

  const clearData = () => {
    state.apiKey = ''
    state.isValidated = false
    state.answers = {}
    state.analysisText = ''
  }

  return {
    state: readonly(state),
    setApiKey,
    setValidated,
    saveAnswer,
    setAnalysis,
    clearData
  }
}
