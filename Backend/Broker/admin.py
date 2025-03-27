from django.contrib import admin

# Register your models here.
from .models import SymbolData, DefaultSecurities

admin.site.register(SymbolData)
admin.site.register(DefaultSecurities)