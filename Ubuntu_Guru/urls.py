# Ubuntu_Guru/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, SignUpView
from .views import CustomLoginView

app_name = 'Ubuntu_Guru'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', views.home_view, name='home'),
    path('articles/', views.article_list, name='article_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('view-polls/', views.view_polls, name='view_polls'),
    # Login path.
    path('login/', CustomLoginView.as_view(), name='login'),  # Use your custom login view
    # Logout path redirects to the namespaced 'home' URL.
    path('logout/', auth_views.LogoutView.as_view(next_page='Ubuntu_Guru:home'), name='logout'),
]


