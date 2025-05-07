from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from .formulario import produtoForm
from .models import Productos

def home(request):
  return render(request,'home.html')
  
def cadastro(request):
 
  if request.method =='GET':
    return render(request, 'registro.html',{
    'form':UserCreationForm
  })
  
  else:
    if request.POST['password1']==request.POST['password2']:
      try:
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
        user.save()
        login(request,user)
        return redirect('productos')
        
      except IntegrityError:
        return render(request, 'login.html',{
    'form':UserCreationForm,
    "error": 'usuário já existe'
  })
        
  return render(request, 'registro.html',{
    'form':UserCreationForm,
    "error": 'As palavras passes não combinam'
  })
  
def produto(request):
  todosProd = Productos.objects.all()
  return render(request, 'produtos.html',{
    'produto':todosProd
  })
  
def insertProduto(request):
  if request.method == 'GET':
    return render(request, 'insert_producto.html',{
    'form':produtoForm
   })
  else:
     try:
       form = produtoForm(request.POST)
       novoProd = form.save(commit=False)
       novoProd.user = request.user
       novoProd.save()
       print(novoProd)
       return redirect('productos')
     except ValueError:
       return render(request, 'insert_producto.html',{
    'form':produtoForm,
       'erro':'Por favor! insira dados válidos'
   })
  
def Logout(request):
  logout(request)
  return redirect(home)
def entrar(request):
  if request.method == "GET":
    return render(request, 'entrar.html', {
      'form':AuthenticationForm
    })
  else:
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
      return render(request, 'entrar.html',
      {
      'form':AuthenticationForm,
      'erro':'dados incorrectos'
    })
    else:
      login(request,user)
      return redirect('productos')
  
  

