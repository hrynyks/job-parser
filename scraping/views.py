from django.shortcuts import render
from .models import Vacancy
from .forms import FindForm


def home_view(request):
    print(request.GET)
    form = FindForm()
    city = request.GET.get('city')
    programming_language = request.GET.get('programming_language')
    qs = []
    if city or programming_language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if programming_language:
            _filter['programming_language__slug'] = programming_language

        qs = Vacancy.objects.filter(**_filter)
    # qs = Vacancy.objects.all()
    return render(request, 'scraping/home.html', {'objects_list': qs, 'form': form})
