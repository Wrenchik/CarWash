from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('main_page')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        # Отправка email
        send_mail(
            subject='Новая регистрация',
            message=f'Пользователь {user.username} зарегистрировался с почтой {user.email} и телефоном {user.phone}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['cleanlabekb@gmail.com'],
        )

        messages.success(self.request, "Вы успешно зарегистрированы!")
        return redirect(self.success_url)

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'login'

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/create.html'
    success_url = reverse_lazy('booking_success')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
