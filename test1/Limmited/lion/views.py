from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def review(request):
    return render(request, 'lion/review.html')

def thanks(request):
    return render(request, 'lion/thanks.html')
