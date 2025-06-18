from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Service, Review
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import redirect
from accounts.forms import UserRegisterForm, LoginForm
from django.contrib.auth import authenticate, login
from booking.models import Booking

def get_main_page(request):
    template_name = 'main/main.html'

    services = Service.objects.all()
    reviews = Review.objects.filter(is_published=True).order_by('-created_at')

    service_paginator = Paginator(services, 4)
    service_page_obj = service_paginator.get_page(1)

    review_paginator = Paginator(reviews, 3)
    review_page_obj = review_paginator.get_page(1)

    register_form = UserRegisterForm()
    login_form = LoginForm()

    user_bookings = []
    if request.user.is_authenticated:
        user_bookings = Booking.objects.filter(user=request.user).order_by('-date', '-start_time')

    if request.method == 'POST':
        if 'register' in request.POST:
            register_form = UserRegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.is_active = True
                user.save()

                return redirect('main_page')
        elif 'login' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"Добро пожаловать, {user.username}!")
                    return redirect('main_page')
                else:
                    messages.error(request, "Неверное имя пользователя или пароль.")

    return render(request, template_name, {
        'service_page_obj': service_page_obj,
        'review_page_obj': review_page_obj,
        'form': register_form,
        'login_form': login_form,
        'bookings': user_bookings,
    })

def load_services(request):
    page = request.GET.get('page', 1)
    services = Service.objects.all()

    paginator = Paginator(services, 3)
    page_obj = paginator.get_page(page)

    html = render_to_string('includes/services.html', {'services': page_obj.object_list})

    has_next = page_obj.has_next()

    return JsonResponse({
        'html': html,
        'has_next': has_next,
        'next_page': page_obj.next_page_number() if has_next else None
    })

def load_reviews(request):
    page = request.GET.get("page", 1)
    reviews = Review.objects.filter(is_published=True).order_by('-created_at')

    paginator = Paginator(reviews, 3)
    page_obj = paginator.get_page(page)

    html = render_to_string('includes/reviews.html', {'reviews': page_obj.object_list})

    has_next = page_obj.has_next()

    return JsonResponse({
        'html': html,
        'has_next': has_next,
        'next_page': page_obj.next_page_number() if has_next else None
    })