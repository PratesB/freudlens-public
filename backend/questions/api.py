from ninja import Router
from http import HTTPStatus
from django.shortcuts import get_object_or_404
from django.http import Http404
from .schemas import OutQuestionSchema, ErrorSchema
from .models import Question



questions_router = Router()



@questions_router.get('/', response={
    HTTPStatus.OK: list[OutQuestionSchema]
})
def list_questions(request):
    questions = Question.objects.all().order_by('order')
    return HTTPStatus.OK, questions




@questions_router.get('/{question_id}', response={
    HTTPStatus.OK: OutQuestionSchema, 
    HTTPStatus.NOT_FOUND: ErrorSchema
})
def get_question(request, question_id: int):
    try:
        question = get_object_or_404(Question, id=question_id)
        return HTTPStatus.OK, question
        
    except Http404:
        return HTTPStatus.NOT_FOUND, ErrorSchema(detail='Question not found')
