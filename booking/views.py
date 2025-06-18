import json
from datetime import datetime, time, timedelta
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking
from main.models import Service
from .forms import BookingForm

STEP_MINUTES = 30
WORK_START = time(11, 0)
WORK_END   = time(21, 0)

def get_available_slots(date, selected_services, existing_bookings):
    total_minutes = sum(s.duration for s in selected_services)
    day_start = datetime.combine(date, WORK_START)
    day_end   = datetime.combine(date, WORK_END)
    step = timedelta(minutes=STEP_MINUTES)

    slots = []
    cursor = day_start
    while cursor + timedelta(minutes=total_minutes) <= day_end:
        slot_start = cursor.time()
        slot_end_dt = cursor + timedelta(minutes=total_minutes)
        slot_end = slot_end_dt.time()

        # проверяем пересечение
        conflict = False
        for b in existing_bookings:
            b_start = datetime.combine(b.date, b.start_time)
            b_end   = datetime.combine(b.date, b.calculate_end_time())
            if not (slot_end <= b_start.time() or slot_start >= b_end.time()):
                conflict = True
                break
        if not conflict:
            slots.append(slot_start.strftime('%H:%M'))
        cursor += step

    return slots

class BookingPageView(LoginRequiredMixin, TemplateView):
    template_name = 'booking/booking.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['services'] = Service.objects.all()
        return ctx

class AvailableSlotsView(LoginRequiredMixin, View):
    def get(self, request):
        date_str = request.GET.get('date')
        service_ids = request.GET.getlist('services')
        if not date_str or not service_ids:
            return JsonResponse({'error': 'Недостаточно данных'}, status=400)

        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        services = Service.objects.filter(id__in=service_ids)
        bookings = Booking.objects.filter(date=date)

        slots = get_available_slots(date, services, bookings)
        return JsonResponse({'slots': slots})

class CreateBookingView(LoginRequiredMixin, View):
    def post(self, request):
        form = BookingForm(request.POST)
        if not form.is_valid():
            return JsonResponse({'errors': form.errors}, status=400)

        booking = form.save(commit=False)
        booking.user = request.user
        booking.save()
        form.save_m2m()

        if booking.payment_method == 'cash':
            return render(request, 'booking/success_cash.html', {'booking': booking})
        else:
            phone = "+79999999999"
            return render(request, 'booking/success_payment.html', {
                'booking': booking, 'phone': phone
            })
