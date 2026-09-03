// Base URL for the Django Ninja API
const API_BASE_URL = 'http://localhost:8000/api'

export const apiService = {
  async validateApiKey(apiKey) {
    try {
      const response = await fetch(`${API_BASE_URL}/analysis/validate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ api_key: apiKey })
      });
      
      if (!response.ok) {
        return false;
      }
      
      const data = await response.json();
      return data.is_valid;
    } catch (error) {
      console.error("Error validating key", error)
      return false
    }
  },

  async fetchQuestions() {
    try {
      const response = await fetch(`${API_BASE_URL}/questions/`);
      if (!response.ok) {
        throw new Error('Failed to fetch questions');
      }
      return await response.json();
    } catch (error) {
      console.error("Error fetching questions", error)
      return []
    }
  },

  async generateAnalysis(apiKey, answers) {
    try {
      // Temporary mock
      return {
        report: "Analysis will be here"
      }
    } catch (error) {
      console.error("Error generating analysis", error)
      throw error
    }
  }
}
