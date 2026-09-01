from ninja import Router
from http import HTTPStatus
from django.http import Http404
from .schemas import AnswerItemSchema, AnalyzeInSchema, ReportOutSchema



analysis_router = Router()




@analysis_router.post('/', response={HTTPStatus.OK: ReportOutSchema})
async def generate_analysis_mock(request, payload: AnalyzeInSchema):
    
    print(f"API Key received: {payload.api_key}")
    print(f"Number of answers received: {len(payload.answers)}")

    
    return HTTPStatus.OK, {
        "summary": "The user presents clear traits of internal conflict (Test Data).",
        "defense_mechanisms": ["Repression", "Projection", "Rationalization"],
        "dynamics": "The Superego is exercising too much pressure on the Ego.",
        "past_influence": "Strong oral fixation identified.",
        "conclusion": "This is just a test. The route is working and the Schemas are correct!"
    }