from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .models import Booking
from .forms import BookingForm

def get_available_slots(date, selected_services, existing_bookings):
    work_start = time(11, 0)
    work_end = time(21, 0)

    total_duration = sum(service.duration for service in selected_services)
    delta = timedelta(minutes=60)

    slots = []
    current_time = datetime.combine(date, work_start)
    end_of_day = datetime.combine(date, work_end)

    while current_time + timedelta(minutes=total_duration) <= end_of_day:
        current_end = current_time + timedelta(minutes=total_duration)
        overlap = False
        for booking in existing_bookings:
            booked_start = datetime.combine(booking.date, booking.start_time)
            booked_end = datetime.combine(booking.date, booking.end_time)
            if booked_start < current_end and current_time < booked_end:
                overlap = True
                break
        if not overlap:
            slots.append(current_time.time())
        current_time += delta

    return slots

class CreateBookingView(View):
    def post(self, request):
        data = request.POST
        user = request.user
        service_ids = data.getlist('services[]')
        date = parse_date(data.get('date'))
        start_time = parse_time(data.get('start_time'))
        comment = data.get('comment', '')
        payment_method = data.get('payment_method', 'cash')

        services = Service.objects.filter(id__in=service_ids)
        bookings = Booking.objects.filter(date=date)

        slots = get_available_slots(date, services, bookings)
        if start_time not in slots:
            return JsonResponse({'error': 'Выбранный слот уже занят'}, status=400)

        booking = Booking.objects.create(
            user=user,
            date=date,
            start_time=start_time,
            comment=comment,
            payment_method=payment_method
        )
        booking.services.set(services)
        booking.save()
        return JsonResponse({'message': 'Бронирование создано'})

class AvailableSlotsView(View):
    def get(self, request):
        date_str = request.GET.get('date')
        service_ids = request.GET.getlist('services[]')

        if not date_str or not service_ids:
            return JsonResponse({'error': 'Недостаточно данных'}, status=400)

        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            services = Service.objects.filter(id__in=service_ids)
            bookings = Booking.objects.filter(date=date)

            available_slots = get_available_slots(date, services, bookings)
            return JsonResponse({'available_slots': [t.strftime('%H:%M') for t in available_slots]})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
