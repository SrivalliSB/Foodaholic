from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
def signup(request):
    print(request.method)
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]

        print(username)
        print(fname)

        user = User.objects.create_user(
            first_name=fname,
            last_name=lname,
            email=email,
            username=username,
            password=password,
        )
       
        login(request, user)
        return redirect("/")

    return render(request, "signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

        else:
            return HttpResponse("Invalid Credentials. <a href='/signin'>Login again here</a>")

    return render(request, "signin.html")


def signout(request):
    logout(request)
    return redirect("/")
