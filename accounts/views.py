from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render

from .forms import CustomAuthenticationForm, CustomUserCreationForm, UserModificationForm

# Create your views here.
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "accounts/login.html"

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("blog:index")
    else:  # if request.method == "GET":
        form = CustomUserCreationForm()
        context = {
            'form': form
        }
    return render(request, "accounts/register.html", context )

def profile(request):
   return render(request, "accounts/profile.html", {} )

def profile_edit(request):
    if request.method == 'POST':
        form = UserModificationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect("accounts:profile")
    if request.method == "GET":
        form = UserModificationForm(instance=request.user)
        context = {
            'form': form
        }
        return render(request, "accounts/profile_edit.html", context )