from django.shortcuts import render, HttpResponse
from datetime import datetime
from . import models
from .models import Querys

# Create your views here.
def index(requests):
    return render(requests, 'index.html')
def result(requests):
    if requests.method == "POST":
        text = requests.POST.get('text')
        date = datetime.today()
        context = {
            'text': text,
            'date': date,
        }
        qwerty = models.Querys(text=text, date=date)
        qwerty.save()
        return render(requests, "result.html", context)

def notes(requests):
    allNotes = Querys.objects.all()
    a = []
    for i in allNotes:
        a.append(i)
        print(i)
    context = {
    'noteshtml': a
    }
    return render(requests, "notes.html",  context)
