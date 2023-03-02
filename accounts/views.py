from .forms import AccountForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse

# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect(reverse("home"))
    else:
        form = AccountForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)
