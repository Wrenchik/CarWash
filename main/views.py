from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Service, Review
from django.http import JsonResponse
from django.template.loader import render_to_string

def get_main_page(request):
    template_name = 'main/main.html'

    services = Service.objects.all()
    reviews = Review.objects.filter(is_published=True).order_by('-created_at')

    service_paginator = Paginator(services, 4)
    service_page_obj = service_paginator.get_page(1)

    review_paginator = Paginator(reviews, 4)
    review_page_obj = review_paginator.get_page(1)

    return render(request, template_name, {
        'service_page_obj': service_page_obj,
        'review_page_obj': review_page_obj
    })

def load_services(request):
    page = request.GET.get('page', 1)
    services = Service.objects.all()

    paginator = Paginator(services, 4)
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
