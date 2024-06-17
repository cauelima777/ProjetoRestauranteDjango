# menu/views.py
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics

from menu.serializers import MenuItemSerializer
from .models import MenuItem, Pedido

def menu_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu/menu_list.html', {'menu_items': menu_items})

def menu_create(request):
    if request.method == 'POST':
        MenuItem.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            price=request.POST['price']
        )
        return redirect('menu_list')
    return render(request, 'menu/menu_create.html')

def menu_edit(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.price = request.POST['price']
        item.save()
        return redirect('menu_list')
    return render(request, 'menu/menu_edit.html', {'item': item})

def menu_delete(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('menu_list')
    return render(request, 'menu/menu_delete.html', {'item': item})

def cliente_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu/cliente_list.html', {'menu_items': menu_items})

def make_order(request):
    if request.method == 'POST':
        item_id = request.POST.get('menu_item')
        mesa = request.POST.get('mesa')
        quantidade = request.POST.get('quantidade')
        item = get_object_or_404(MenuItem, pk=item_id)
        Pedido.objects.create(menu_item=item, mesa=mesa)
        return redirect('cliente_list')
    else:
        menu_items = MenuItem.objects.all()
        return render(request, 'menu/make_order.html', {'menu_items': menu_items})

def order_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'menu/order_list.html', {'pedidos': pedidos})


def delete_order(request, order_id):
    pedido = get_object_or_404(Pedido, pk=order_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('order_list')
    return render(request, 'menu/order_list.html', {'pedido': pedido})



def order_detail(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    return render(request, 'menu/order_detail.html', {'pedido': pedido})



def index(request):
    return render(request, 'menu/index.html')



class MenuItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
