from django.shortcuts import render
from .forms import AppForm

def index(request):
    #get user data from the form
    if request.method == "POST":
        form = AppForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

    return render(request,"index.html")
