from ninja import Schema
from enum import Enum



class SupportedModel(str, Enum):
    FLASH_3_5 = "gemini-3.5-flash"
    FLASH_3_6 = "gemini-3.6-flash"
    FLASH_3_7 = "gemini-3.7-flash"

    

class SupportedLanguage(str, Enum):
    PT = "Português"
    EN = "English"
    ES = "Español"
    DE = "Deutsch"
    FR = "Français"
    IT = "Italiano"
    FI = "Suomi"
    SV = "Svenska"
    NO = "Norsk"




class ValidateKeyInSchema(Schema):
    api_key: str




class ValidateKeyOutSchema(Schema):
    is_valid: bool



class AnswerItemSchema(Schema):
    question_id: int
    text: str



class AnalyzeInSchema(Schema):
    api_key: str
    model_name: SupportedModel
    language: SupportedLanguage
    answers: list[AnswerItemSchema]



class ReportOutSchema(Schema):
    summary: str
    defense_mechanisms: list[str]
    dynamics: str
    past_influence: str
    conclusion: str

