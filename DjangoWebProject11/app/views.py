from django.shortcuts import render
def index(request):
    return render(request, 'app/index.html')

def news(request):
    return render(request, 'app/news.html')

def management(request):
    return render(request, 'app/management.html')

def about(request):
    return render(request, 'app/about.html')

def contacts(request):
    return render(request, 'app/contacts.html')
