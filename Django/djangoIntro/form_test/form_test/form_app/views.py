from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_user(request):
    context = {
        "name" : request.POST['name'],
        "email" : request.POST['email']
    }
    return redirect('/success')

def success(request):
    return render(request, "success.html")