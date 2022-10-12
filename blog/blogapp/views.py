from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import *
from .models import *

# Create your views here.
def index(request):

    records = post.objects.all().order_by('-id')[1:]
    last_post = post.objects.all().order_by('-id')[0]

    return render(request, 'index.html' , {'rec' : records , 'last': last_post})


def create_post(request):
    if request.method == 'POST':
        form = post_form(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = post_form()

    return render(request, 'post.html' , {'form' : form})


def selected_post(request , d):
    n = post.objects.get(id = d)
    return render(request, 'selected_post.html' , {'n':n})

def delete(request , d):
    n = post.objects.get(id = d)
    n.delete()

    return redirect('/')