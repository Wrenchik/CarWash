from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserRegisterForm

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('main_page')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)
        activation_link = self.request.build_absolute_uri(
            reverse('activate', kwargs={'uidb64': uid, 'token': token})
        )

        send_mail(
            'Подтверждение регистрации',
            f'Здравствуйте, {user.username}!\nПерейдите по ссылке для активации: {activation_link}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

        messages.info(self.request, "Письмо с подтверждением отправлено на вашу почту.")
        return redirect('main_page')

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        messages.success(self.request, f"Добро пожаловать, {form.get_user().username}!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Неверные имя пользователя или пароль")
        return super().form_invalid(form)

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('main_page')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Вы успешно вышли из системы")

        return super().dispatch(request, *args, **kwargs)

class ActivateAccount(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Аккаунт успешно активирован! Теперь вы можете войти.")
            return redirect('login')
        else:
            messages.error(request, "Ссылка недействительна или устарела.")
            return redirect('main_page')