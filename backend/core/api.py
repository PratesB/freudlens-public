from ninja import NinjaAPI
from questions.api import questions_router


api = NinjaAPI()



api.add_router('questions/', questions_router)


