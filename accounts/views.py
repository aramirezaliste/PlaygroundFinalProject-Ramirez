from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render

from .forms import CustomAuthenticationForm, CustomUserCreationForm

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