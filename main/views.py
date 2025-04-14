from django.shortcuts import render


def get_main_page(request):
    template_name = 'base.html'

    context = {
        'page_title': 'Главная страница',
    }

    return render(request, template_name, context)