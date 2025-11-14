from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Empleado
from .form import EmpleadoRegistroForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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



@login_required
def employees_registration(request):
    form = EmpleadoRegistroForm()
    
    # Solo se ejecuta cuando se apreta registrar
    if request.method == 'POST':
        form = EmpleadoRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('employees_list'))                  

    data = {'form' : form,
            'titulo': 'Registrar Empleado',
            'txtBoton':'Registrar'}
    return render(request, 'employees_control/employees_register.html' ,data)