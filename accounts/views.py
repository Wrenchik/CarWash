from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserRegisterForm

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()         # <-- вот здесь пользователь сохраняется в БД
            login(request, user)       # <-- сразу залогинить (необязательно)
            messages.success(request, "Вы успешно зарегистрированы")
            return redirect('main_page')  # <-- возвращаемся на главную
        else:
            # чтобы видеть ошибки в шаблоне
            messages.error(request, "Пожалуйста, исправьте ошибки в форме")
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})