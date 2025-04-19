from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')  # После успешной регистрации — перенаправление на логин

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'login'  # После логаута — обратно на страницу логина

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/create.html'
    success_url = reverse_lazy('booking_success')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
