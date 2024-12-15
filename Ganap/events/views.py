from django.shortcuts import render
from .models import Event

def home(request):
    events = Event.objects.all()[:3] 
    return render(request, 'events/index.html', {'events': events})
