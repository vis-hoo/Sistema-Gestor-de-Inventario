from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Empleado

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def home(request):
    return render(request, "home.html")

@login_required
def employees_list(request):
    empleados = Empleado.objects.all()
    data = { 'empleados': empleados }
    return render(request, "employees_control/employees_list.html", data)