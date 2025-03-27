from django.contrib import admin

# Register your models here.
from .models import SymbolData, DefaultSecurity

admin.site.register(SymbolData)
admin.site.register(DefaultSecurity)