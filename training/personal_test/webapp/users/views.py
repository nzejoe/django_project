from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from . forms import CustomUserCreationForm


class SignUpView(SuccessMessageMixin, generic.edit.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        self.success_message = f'Account successfully created for {username}! You can login below.'
        return super().form_valid(form)