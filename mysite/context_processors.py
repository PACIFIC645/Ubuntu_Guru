# mysite/context_processors.py

from django.conf import settings
from polls.models import Question

def latest_poll_question_id(request):
    latest_question = Question.objects.order_by('-pub_date').first()
    return {'latest_poll_question_id': latest_question.id if latest_question else None}