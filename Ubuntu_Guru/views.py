# Ubuntu_Guru/views.py

from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.views import generic
from .models import Article
from polls.models import Question


class SignUpView(SuccessMessageMixin, CreateView):
    """
    Handles user registration with a custom user creation form.
    Redirects to the login page upon successful registration and displays a success message.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('Ubuntu_Guru:login')
    template_name = 'Ubuntu_Guru/signup.html'
    success_message = "Your account was created successfully. Please log in."

    def form_invalid(self, form):
        """
        Overrides the form_invalid method to handle form validation errors by displaying them to the user.
        """
        for _, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

class CustomLoginView(LoginView):
    template_name = 'Ubuntu_Guru/login.html'  
    
    def get_success_url(self):
        return reverse_lazy('Ubuntu_Guru:home')   

def article_list(request):
    articles = Article.objects.all() # Retrieve all articles
    if not articles:
        # Handle the case where no articles are found
        context = {'message': "No articles found."}
    else:
        context = {'articles': articles}
    return render(request, 'Ubuntu_Guru/article_list.html', context)

def about(request):
    return render(request, 'Ubuntu_Guru/about.html')

def contact(request):
    return render(request, 'Ubuntu_Guru/contact.html')

def home_view(request):
    context = {}
    latest_articles = Article.objects.all()[:3] 
    latest_questions = Question.objects.order_by('-pub_date')[:3]
    
    context['latest_articles'] = latest_articles
    context['latest_questions'] = latest_questions
    
    # Add more context variables as needed
    return render(request, 'Ubuntu_Guru/home.html', context)

def profile(request):
    return render(request, 'Ubuntu_Guru/profile.html')

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    print("Latest questions:", latest_question_list) 
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def view_polls(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:3]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'Ubuntu_Guru/polls_list.html', context)  


