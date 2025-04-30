from django.shortcuts import render
from .models import Service, Review


def get_main_page(request):
    template_name = 'main/main.html'

    services = Service.objects.all()
    reviews = Review.objects.filter(is_published=True).order_by('-date')[:5]

    return render(request, template_name,  {'services': services})