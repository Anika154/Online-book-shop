from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login


# Create your views here.
def Contact(request):
    return render(request, 'process/contact.html')


def review(request):
    if request.method == 'GET':
        return render(request, 'process/review.html')
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        review = Review(title=title, body=body)
        review.save()
        return redirect('new')


def New(request):
    all_review = Review.objects.all()
    context = {
        "reviews": all_review
    }
    return render(request, 'process/new.html', context)


def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'process/index.html')


def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')
    d = {'error': error}
    return render(request, 'process/login.html', d)


@login_required
def dashboard(request):
    return render(request, 'process/index.html')


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


def Biography(request):
    bk = Book.objects.all()
    b = {
        "book": bk
    }
    return render(request, 'process/biography.html', b)


def Fiction(request):
    fic = Book.objects.all()
    c = {
        "book": fic
    }
    return render(request, 'process/fiction.html', c)


def Thriller(request):
    thril = Book.objects.all()
    d = {
        "book": thril
    }
    return render(request, 'process/thriller.html', d)


def Romance(request):
    rom = Book.objects.all()
    e = {
        "book": rom
    }
    return render(request, 'process/romance.html', e)


def order(request):
    if request.method == 'GET':
        books=Book.objects.all()
        context= {
            "book": books
        }
        return render(request, 'process/order.html', context)

    return redirect('review')
