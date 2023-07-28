from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import RegisterForm, TaikhoanForm, LoginForm, PostForm, CoursesForm
from django.contrib.auth import login, authenticate


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def courses(request):
    return render(request, 'pages/courses.html')


def about(request):
    return render(request, 'pages/about.html')


def blog(request):
    return render(request, 'pages/blog.html')


def blog_details(request):
    return render(request, 'pages/blog_details.html')


def elements(request):
    return render(request, 'pages/elements.html')


def contact(request):
    return render(request, 'pages/contact.html')


def login(request):
    return render(request, 'pages/login.html')


def register(request):
    return render(request, 'pages/register.html')


def new(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        tk = TaikhoanForm(request.POST)
        if form.is_valid() and tk.is_valid():
            try:
                form.save()
                tk.save()
                return redirect('/index')
            except:
                pass
    else:
        form = RegisterForm()
    return render(request, 'pages/register.html', {"form": form})


def loginacc(request):
    # if request.method == "POST":
    #     form = TaikhoanForm(request.POST)
    #     if form.is_valid():
    #         Email = form.cleaned_data.get('Email')
    #         Matkhau = form.cleaned_data.get('MatKhau')
    #         user = authenticate(username=Email, password=Matkhau)
    #         if user is not None:
    #             login(request, user)
    #             messages.info(request, f"You are now logged in as {Email}.")
    #             return redirect("/index")
    # form = TaikhoanForm()
    return render(request, 'pages/index.html')


def savepost(request):
    if request.method == "POST":
        form = PostForm(request, data=request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/blog_details")
            except:
                pass
    else:
        form = PostForm()
    return render(request, 'pages/blog_details.html', {"form": form})


def pay(request):
    return render(request, 'pages/pay.html')

def service(request):
    return render(request, 'pages/service.html')
