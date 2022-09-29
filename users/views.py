from .forms import RegisterUserForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib.messages.views import SuccessMessageMixin


Users = get_user_model()
# Create your views here.

def RegisterUser(request):
    form = RegisterUserForm
    users = Users.objects.all()
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid:
            form.save()
            return redirect("users:RUF")
    return render(request, "users/register/register.html", context={
        'form':form,
        'object_list':users
    })

class RegisterUser(LoginRequiredMixin, CreateView, SuccessMessageMixin):
    login_url = ''
    login_redirect_field = reverse_lazy("users:LG")
    model = Users
    form_class = RegisterUserForm
    template_name = "users/register/register.html"
    success_url = reverse_lazy("users:RUF")
    success_message = 'Yangi Foydalanuvchi muaffaqiyatli qo\'shildi'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Users.objects.all().order_by('-joined_date')
        return super().get_context_data(**kwargs)

def LOGIN(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("H")
    form = AuthenticationForm
    return render(request, "users/login/login.html", {
        "form":form
    })

def LOGOUT(request):
    logout(request)
    messages.info(request, "Akkountdan chiqildi!")
    return redirect("users:LG")