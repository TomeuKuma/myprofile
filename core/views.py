from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):

    context = {}
    return render(request, 'index.html', context)
