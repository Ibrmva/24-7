from django.shortcuts import render


def index(request):
    data = {
        'title': 'Home',
        'values': ['Check out latest news of AIU and add new articles!', 'Press the blue button on the left side to add your own articles!']
    }
    return render(request, "main/index.html", data)

def about(request):
    return render(request, 'main/about.html')
# Create your views here.

def contacts(request):
    return render(request, 'main/contacts.html')
# Create your views here.
