from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from accounts.forms import LoginForm, CustomUserCreationForm, UserChangeForm, PasswordChangeForm


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            messages.error(request, "Некорректные данные")
            return redirect('index')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.warning(request, "Пользователь не найден")
            return redirect('index')
        login(request, user)
        messages.success(request, 'Добро пожаловать')
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'


class UserChangeView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})


class PasswordChangeView(UpdateView):
    model = get_user_model()
    template_name = 'change_password.html'
    form_class = PasswordChangeForm



    def get_success_url(self):
        return reverse('index')
