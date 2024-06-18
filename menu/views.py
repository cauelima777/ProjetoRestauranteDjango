# menu/views.py
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from menu.serializers import MenuItemSerializer, PedidoSerializer
from .models import MenuItem, Pedido




#Listar itens do cardápio / Gerência
def menu_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu/menu_list.html', {'menu_items': menu_items})

#Criar Itens para o cardápio / Gerência
def menu_create(request):
    if request.method == 'POST':
        MenuItem.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            price=request.POST['price']
        )
        return redirect('menu_list')
    return render(request, 'menu/menu_create.html')



#Editar itens para o cardápio / Gerência
def menu_edit(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.price = request.POST['price']
        item.save()
        return redirect('menu_list')
    return render(request, 'menu/menu_edit.html', {'item': item})


#Deletar itens para o cardápio / Gerência
def menu_delete(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('menu_list')
    return render(request, 'menu/menu_delete.html', {'item': item})

#Listar o itens diponíveis no cardápio para o cliente pedir
def cliente_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu/cliente_list.html', {'menu_items': menu_items})



#Fazer pedido / Cliente
def make_order(request):
    if request.method == 'POST':
        quantidade = request.POST.get('quantidade')
        item_id = request.POST.get('menu_item')
        mesa = request.POST.get('mesa')
        item = get_object_or_404(MenuItem, pk=item_id)
        Pedido.objects.create(menu_item=item, quantidade=quantidade, mesa=mesa)
        return redirect('cliente_list')
    else:
        menu_items = MenuItem.objects.all()
        return render(request, 'menu/make_order.html', {'menu_items': menu_items})
    

#Listar pedido / Comanda - Funcionários
def order_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'menu/order_list.html', {'pedidos': pedidos})


#Deletar itens da comanda / Funcionário
def delete_order(request, order_id):
    pedido = get_object_or_404(Pedido, pk=order_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('order_list')
    return render(request, 'menu/order_list.html', {'pedido': pedido})


#Detalhes do pedido / Comanda
def order_detail(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    return render(request, 'menu/order_detail.html', {'pedido': pedido})


#Mostrar todas as navegações
def index(request):
    return render(request, 'menu/index.html')



#Marcar como Concluída os itens da comanda
def marcar_como_concluido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    pedido.concluido = True
    pedido.save()
    return redirect('order_list')

#Desfazer a conlusão quando for necessário
def desfazer_conclusao(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.concluido = False
    pedido.save()
    return redirect('order_list')





# API's
class MenuItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class PedidoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer