from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    context = {
        'all_dojos' : Dojo.objects.all()
    }
    return render(request, "index.html", context)

def create_dojo(request):
    Dojo.objects.create(name = request.POST['name'], city = request.POST['city'], state = request.POST['state'])
    return redirect('/')

def destroy_dojo(request):
    dojo = Dojo.objects.get( id = request.POST['dojo_id'])
    dojo.delete()
    return redirect('/')

def create_ninja(request):
    dojo = Dojo.objects.get(id = request.POST['dojo_id'])
    Ninja.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], dojo_id = dojo)

    return redirect('/')

def destroy_ninja(request):
    ninja = Ninja.objects.get( id = request.POST['ninja_id'])
    ninja.delete()
    return redirect('/')