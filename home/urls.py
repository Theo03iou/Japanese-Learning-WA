from django.urls import path
from . import views
from .forms import LoginForm
from django.contrib.auth import 


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]
