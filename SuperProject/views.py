from django.shortcuts import render
from .models import Droid


def get_droids(request):
    droids = Droid.objects.all()
    print(request.POST)
    if request.method == 'POST':
        droid = Droid.objects.filter(name=request.POST.get('droid'))
        print(droid)
        if droid:
            context = {'droid': droid}
            return render(request, 'droids.html', context)
        else:
            context = {'error': 'Поиск не дал'}
            return render(request, 'droids.html', context)
    context = {'droids': droids}
    return render(request, 'droids.html', context)


def main_page(request):
    return render(request, 'main_page.html')
