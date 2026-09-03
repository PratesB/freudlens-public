import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import QuestionnaireView from '../views/QuestionnaireView.vue'
//import AnalysisView from '../views/AnalysisView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/questionnaire',
      name: 'questionnaire',
      component: QuestionnaireView
    },
    // {
    //   path: '/analysis',
    //   name: 'analysis',
    //   component: AnalysisView
    // }
  ]
})

export default router
