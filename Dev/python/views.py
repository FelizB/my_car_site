from django.shortcuts import render, redirect
from Dev.forms import ReviewForm
from django.urls import reverse

app_name= 'python'

# Create your views here.
def css(request):
    if request.method == 'POST':
        form= ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect(reverse('python:css'))
    else:
        form= ReviewForm()

    return render(request,'python/css.html', context={'form':form})


def html(request):
    return render(request, 'python/html.html')