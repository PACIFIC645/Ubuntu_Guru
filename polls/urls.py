# polls/urls

from django.urls import path
from . import views
from .views import poll_tracker_season
from .views import view_polls

app_name = 'polls'   # Namespace for app-specific URLs

urlpatterns = [
    path('', views.index, name='index'),  # Main page for polls
    path('poll-tracker-season/', views.poll_tracker_season, name='poll_tracker_season'),
    path('<int:question_id>/', views.detail, name='detail'),  # Detailed view for a specific question
    path('<int:question_id>/results/', views.results, name='results'),  # Results view for specific questions
    path('<int:question_id>/vote/', views.vote, name='vote'),  # Voting action for a specific question
    path('manage/', views.manage_polls_view, name='manage_polls'), # Manage Polls view
    path('view-polls/', view_polls, name='view_polls'),
    path('view-polls-live/', views.view_polls_live, name='view_polls_live'),
]
