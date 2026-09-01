from ninja import NinjaAPI
from questions.api import questions_router
from analysis.api import analysis_router

api = NinjaAPI()



api.add_router('questions/', questions_router)
api.add_router('analysis/', analysis_router)
