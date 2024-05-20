from django.shortcuts import render

# Create your views here.

def card_index(request):
    return render(request, "cards/index.html")