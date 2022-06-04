from django.shortcuts import render, redirect

from new_app.forms import PersonForm

from new_app.models import Person


def index(request):
    form = PersonForm()
    persons = Person.objects.all()
    context = {'persons': persons}
    # context = {'form': form}
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {'form': form}
            return render(request, 'index.html', context)
    return render(request, 'index.html', context)

def form_save(request):
    return render(request, 'index.html', context)