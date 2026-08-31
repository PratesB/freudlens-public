from ninja import Schema



class OutQuestionSchema(Schema):
    id: int
    subject: str
    text: str
    order: int



class ErrorSchema(Schema):
    detail:str