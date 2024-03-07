from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
        request.session['custom_count'] += 1
    else: 
        request.session['count'] = 1
        request.session['custom_count'] = 1

    return render(request, 'index.html' )

def delete(request):
    if 'count' in request.session:
        del request.session['count']
    
    if 'custom_count' in request.session:
        del request.session['custom_count']

    return redirect('/')

def double(request):
    if 'custom_count' in request.session:
        request.session['custom_count'] += 1
    else: 
        request.session['custom_count'] = 1

    return redirect('/')

def custom(request):
    print(request.POST)
    num = int(request.POST['num'])

    if 'custom_count' in request.session:
        request.session['custom_count'] += num -1 
    else: 
        request.session['custom_count'] = num -1 
    return redirect('/')