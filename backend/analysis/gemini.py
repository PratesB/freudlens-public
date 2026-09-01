import json
from google import genai
from google.genai import types
from .prompt import get_system_prompt
from .schemas import ReportOutSchema




async def validate_gemini_key(api_key: str) -> bool:

    client = genai.Client(api_key=api_key)

    try:
        await client.aio.models.get(model="gemini-3.5-flash")
        return True
        
    except Exception as e:
        print(f"API Key validation failed: {e}")
        return False



async def call_gemini(api_key: str, model_name: str, language: str, answers: list) -> dict:

    client = genai.Client(api_key=api_key)

    formatted_answers = "\n".join([f"Question {ans.question_id}: {ans.text}" for ans in answers])
    user_message = f"Here are the user's answers:\n{formatted_answers}"
    
    
    response = await client.aio.models.generate_content(
        model=model_name,
        contents=user_message,
        config=types.GenerateContentConfig(
            system_instruction=get_system_prompt(language),
            response_mime_type="application/json",
            response_schema=ReportOutSchema,
            temperature=0.7,
            max_output_tokens=2500,
        ),
    )
    

    return json.loads(response.text)
