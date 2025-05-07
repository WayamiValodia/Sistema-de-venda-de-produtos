from django.contrib import admin
from .models import Productos

class ProdAdmin(admin.ModelAdmin):
  readonly_fields = ("created", )
  
admin.site.register(Productos)