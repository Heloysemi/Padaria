"""
URL configuration for projeto_barbearia project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from loja import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # '' significa que essa sera a pagina inicial, views esta importando do app.nome da função  
    path('', views.home2, name='home'),
    # # 'nome/' seta o que vem depois da barra do enderenço inicial, para ser buscado , name serve para indentificar a pagina
    # path('home2/', views.home2, name='home2'),
    # path('home3/', views.home3, name='home3'),
    
]