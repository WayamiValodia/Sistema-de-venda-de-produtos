from django.forms import ModelForm
from .models import Productos

class produtoForm(ModelForm):
  class Meta:
    model=Productos
    fields=['nome','categoria','descricao']