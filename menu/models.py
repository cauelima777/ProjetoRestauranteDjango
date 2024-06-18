# menu/models.py
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Pedido(models.Model):
    mesa = models.IntegerField()
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    quantidade = models.IntegerField(default=1)
    concluido = models.BooleanField(default=False)
    def __str__(self):
        return f"Pedido de {self.menu_item.name} em {self.created_at}"
