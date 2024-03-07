from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def index(request): 
    return render(request, 'form.html')

def result(request):

    if 'check' not in request.POST:
        return redirect(reverse('index'))
    
    else:
        context = {
            'name': request.POST["name"],
            'dojoLocation': request.POST["dojoLocation"],
            'faveLang': request.POST["faveLang"],
            'comment': request.POST["comment"],
        }
        return render(request, 'results.html', context)
