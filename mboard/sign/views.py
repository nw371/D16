from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm

# class LoginView(TemplateView):
#     template_name = 'sign/login.html'

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'