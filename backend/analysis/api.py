from ninja import Router
from http import HTTPStatus
from .schemas import AnalyzeInSchema, ReportOutSchema, ValidateKeyInSchema, ValidateKeyOutSchema
from .gemini import call_gemini, validate_gemini_key



analysis_router = Router()



@analysis_router.post('/validate', response=ValidateKeyOutSchema)
async def validate_key(request, payload: ValidateKeyInSchema):
    is_valid = await validate_gemini_key(payload.api_key)
    return {"is_valid": is_valid}



@analysis_router.post('/', response={
    HTTPStatus.OK: ReportOutSchema,
    HTTPStatus.INTERNAL_SERVER_ERROR: dict
})
async def generate_analysis(request, payload: AnalyzeInSchema):
    
    all_models = ['gemini-3.7-flash', 'gemini-3.6-flash', 'gemini-3.5-flash']
    
    models_to_try = [payload.model_name.value]

    for model in all_models:
        if model not in models_to_try:
            models_to_try.append(model)
            
    last_error = None
    
    for current_model in models_to_try:
        try:
            print(f"Attempting analysis with model: {current_model}...")
            analysis_data = await call_gemini(
                api_key=payload.api_key, 
                model_name=current_model,
                language=payload.language.value,
                answers=payload.answers
            )
            print(f"Success with {current_model}!")
            return HTTPStatus.OK, analysis_data
            
        except Exception as e:
            print(f"Fallback triggered: {current_model} failed due to | {e}")
            last_error = e
            continue
            
  
    print("All fallback models failed.")
    return HTTPStatus.INTERNAL_SERVER_ERROR, {"detail": f"Failed to generate analysis. All models failed. Check your API Key or Quota. Last error: {last_error}"}