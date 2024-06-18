# serializers.py
from rest_framework import serializers
from .models import MenuItem, Pedido

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
     class Meta:
        model = Pedido
        fields = '__all__'