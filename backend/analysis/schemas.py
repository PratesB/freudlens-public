from ninja import Schema




class AnswerItemSchema(Schema):
    question_id: int
    text: str



class AnalyzeInSchema(Schema):
    api_key: str
    answers: list[AnswerItemSchema]



class ReportOutSchema(Schema):
    summary: str
    defense_mechanisms: list[str]
    dynamics: str
    past_influence: str
    conclusion: str

