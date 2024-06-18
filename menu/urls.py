# menu/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gerencia/', views.menu_list, name='menu_list'),
    path('menu_criar/', views.menu_create, name='menu_create'),
    path('menu_editar/<int:item_id>/', views.menu_edit, name='menu_edit'),
    path('menu_deletar/<int:item_id>/', views.menu_delete, name='menu_delete'),
    path('cliente/', views.cliente_list, name='cliente_list'), 
    path('pedido/', views.make_order, name='make_order'),
    path('deletar/<int:order_id>/', views.delete_order, name='delete_order'),
    path('visualizar/<int:pedido_id>/', views.order_detail, name='order_detail'), 
    
    
    
    #Apis
    
    path('api/menuitems/', views.MenuItemListCreateAPIView.as_view(), name='api_menuitem_list_create'),
    path('api/menuitems/<int:pk>/', views.MenuItemRetrieveUpdateDestroyAPIView.as_view(), name='api_menuitem_detail'),



    #Comandas

    path('comandas/', views.order_list, name='order_list'),  

    path('marcar_como_concluido/<int:pk>/', views.marcar_como_concluido, name='marcar_como_concluido'),
    path('comandas/desfazer_conclusao/<int:pedido_id>/', views.desfazer_conclusao, name='desfazer_conclusao'),

]
