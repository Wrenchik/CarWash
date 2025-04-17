from django.shortcuts import render, redirect
from .forms import BookingForm

def booking_page(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('main_page')
    else:
        form = BookingForm()
    return render(request, 'booking/booking.html', {'form': form})