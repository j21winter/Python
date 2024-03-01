from django.shortcuts import render
from datetime import datetime
from tzlocal import get_localzone

# Create your views here.
def index(request): 

    data = datetime.now(get_localzone())


    context = {
        "date": data.strftime("%a, %w %B"),
        "time": data.strftime("%I : %M %p")
    }
    return render(request, 'index.html', context)