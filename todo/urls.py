"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pendiente.views import signupuser,currenttodos,logoutuser,index,loginuser,crearpendiente,verpendiente,completado,borrar,completados

urlpatterns = [
    path('admin/', admin.site.urls),

    # Autenticacion
    path('signup/',signupuser,name='signupuser'),
    path('logout/',logoutuser,name='logoutuser'),
    path('login/',loginuser,name='loginuser'),

    #Pendientes
    path('current/',currenttodos,name='currenttodos'),
    path('',index,name='index'),
    path('create/',crearpendiente,name='crearpendiente'),
    path('completed/',completados,name='completed'),

    path('pendiente/<int:pendiente_pk>',verpendiente,name='verpendiente'),
    path('pendiente/<int:pendiente_pk>/completados',completado,name='completado'),
    path('pendiente/<int:pendiente_pk>/borrado',borrar,name='borrado'),


]
