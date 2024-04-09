# polls/views.py

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from .models import Question, BlogPost


@login_required
def index(request):
    """
    Redirect to view_polls (live) which lists all polls and allows voting.
    """
    return redirect('polls:view_polls')  # Adjust 'polls:view_polls' as necessary based on your URL name for view_polls


def vote(request, question_id):
    """
    Processes a vote for a specific poll question identified by `question_id`.

    Args:
        request (HttpRequest): The request object used to pass states through the system.
        question_id (int): The primary key of the poll question being voted on.

    Returns:
        HttpResponseRedirect: Redirects to the voting results page if the vote is successful.
        HttpResponse: Renders the polling detail page with an error message if an invalid choice is made.

    Raises:
        KeyError: If no choice is selected in the POST request data.
        Choice.DoesNotExist: If the selected choice does not exist in the database.
    """
    if not request.user.is_authenticated:
        # Redirect to login page if the user is not authenticated
        return HttpResponseRedirect(reverse('Ubuntu_Guru:login') + "?next=" + request.path)
    
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    """
    Viewing poll results.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

@login_required
def manage_polls_view(request):
    # Logic for managing 
    return render(request, 'polls/manage_polls.html', {})

@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def redirect_to_latest_poll(request):
    latest_question = Question.objects.order_by('-pub_date').first()
    if not latest_question:
        raise Http404("The anticipation is palpable, but no polls are currently available.")
    return redirect('polls:detail', question_id=latest_question.id)

def poll_tracker_season(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    recent_blog_posts = BlogPost.objects.order_by('-created_on')[:3]  # Get the three most recent blog posts
    context = {
        'latest_questions': latest_questions,
        'recent_blog_posts': recent_blog_posts,
    }
    return render(request, 'polls/home.html', context)

def view_polls(request):
    questions = Question.objects.all()  # Fetch all questions
    return render(request, 'polls/all_polls.html', {'questions': questions})

def view_all_polls(request):
    questions = Question.objects.all()
    return render(request, 'polls/all_polls.html', {'questions': questions})

def view_polls_live(request):
    """
    Redirect to the poll_tracker_season view.
    """
    return redirect('polls:poll_tracker_season') 
 