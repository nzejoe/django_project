from django.views import generic
from . forms import CustomUserCreationForm
from django.urls import reverse_lazy


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')