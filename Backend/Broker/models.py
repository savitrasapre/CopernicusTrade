from django.db import models

class SymbolData(models.Model):
    id = models.AutoField(primary_key=True)
    market_data = models.JSONField(null=True, blank=True)
    broker_name = models.CharField(max_length=500)
    symbol_name = models.CharField(max_length=500)
    updated_at = models.DateTimeField(auto_now=True)