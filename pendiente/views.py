from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import PendienteForm
from .models import Pendiente
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'pendiente/index.html')

def signupuser(request):

    if request.method=="GET":
        return render(request, 'pendiente/signupuser.html',{'form':UserCreationForm()})
    
    else:
        #crear nuevo usuario
        if request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('currenttodos')

            except IntegrityError:
                return render(request, 'pendiente/signupuser.html',{'form':UserCreationForm(),'error':'Ese usuario ya existe'})
        else:
            # si las contraseñas no coinciden
            return render(request, 'pendiente/signupuser.html',{'form':UserCreationForm(),'error':'Las contraseñas no coinciden'})
            
@login_required
def currenttodos(request):
    pendientes=Pendiente.objects.filter(created_by=request.user,datecompleted__isnull=True)
    return render(request, 'pendiente/currenttodos.html',{'pendientes':pendientes})

@login_required
def logoutuser(request):
    if request.method=="POST":
        logout(request)
    return redirect('index')

def loginuser(request):
    if request.method=="GET":
        return render(request, 'pendiente/loginuser.html',{'form':AuthenticationForm()})
    
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'pendiente/loginuser.html',{'form':AuthenticationForm(),'error':'Usuario y contraseña no coincidieron'})
        else:
            login(request,user)
            return redirect('currenttodos')

@login_required
def crearpendiente(request):
    if request.method=='GET':
        return render(request, 'pendiente/crearpendiente.html',{'form':PendienteForm()})
    else:
        try:
            form = PendienteForm(request.POST)
            nuevopendiente=form.save(commit=False)
            nuevopendiente.created_by=request.user
            nuevopendiente.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request,'pendiente/crearpendiente.html',{'form':PendienteForm(), 'error':"No edites el html :)"})

@login_required
def verpendiente(request,pendiente_pk):
    
    pendiente=get_object_or_404(Pendiente,pk=pendiente_pk,created_by=request.user)

    form = PendienteForm(instance=pendiente)

    context_dict={
        'pendiente':pendiente,

    }

    if request.method=='GET':
        form = PendienteForm(instance=pendiente)
        context_dict.update({'form':form})
        return render(request, 'pendiente/verpendiente.html',context_dict)
    else:
        try:
            form = PendienteForm(request.POST,instance=pendiente)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            context_dict.update({'error':'Mala data pasada'})

@login_required
def completado(request,pendiente_pk):
    
    pendiente=get_object_or_404(Pendiente,pk=pendiente_pk,created_by=request.user)

    if request.method=="POST":
        pendiente.datecompleted= timezone.now()
        pendiente.save()
        return redirect('currenttodos')

@login_required
def borrar(request,pendiente_pk):
    
    pendiente=get_object_or_404(Pendiente,pk=pendiente_pk,created_by=request.user)

    if request.method=="POST":
        pendiente.delete()
        return redirect('currenttodos')

@login_required
def completados(request):
    pendientes=Pendiente.objects.filter(created_by=request.user,datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'pendiente/completados.html',{'pendientes':pendientes})





        



