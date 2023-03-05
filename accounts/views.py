from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic

from .forms import UserCreateForm


class RegisterView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('job:home')