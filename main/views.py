from django.shortcuts import render
from .models import Service


def get_main_page(request):
    template_name = 'main/main.html'

    services = Service.objects.all()

    return render(request, template_name,  {'services': services})