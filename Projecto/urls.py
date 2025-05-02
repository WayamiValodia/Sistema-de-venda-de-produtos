from django.contrib import admin
from django.urls import path
from sistema import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('productos/',views.produto, name='productos'),
    path('logout/', views.Logout, name='logout'),
    path('entrar/', views.entrar, name='entrar'),
    
]
