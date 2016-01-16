from __future__ import absolute_import

from django.views import generic
from django.contrib.auth import authenticate , login , logout 
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from .forms import RegisterationForm
from .forms import LoginForm

class HomePageView(generic.TemplateView):
	template_name = 'home.html'


class SignUpView (generic.CreateView):
	form_class = RegisterationForm
	model = User
	template_name = 'accounts/signup.html'


class LoginForm(generic.FormView):
	form_class = LoginForm
	success_url = reverse_lazy('home')
	template_name = 'accounts/login.html'

	