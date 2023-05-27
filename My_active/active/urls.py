from django.urls import path
from . import views
from .views import LoginUser, buy_stock

urlpatterns = [
    path('', views.index, name='index'),
    path('action_list/', views.action_list, name='stock'),
    path('action_list_user', views.action_list_user, name='stock_user'),
    path('buy_stock_user/<int:pk>/', buy_stock, name='buy_stock_user'),
    path('sell_stock_user/<int:pk>/', views.sell_stock, name='sell_stock_user'),
    path('action_list_for_user', views.action_list_for_user, name='action_for_user'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('replenishment_balances/', views.replenishment_balance, name='balance'),
    path('withdraw/', views.withdraw, name='withdraw_many'),
    path('my_js/', views.redirect_to_js, name='my_js'),
    path('withdraw_js/', views.withdraw_to_js, name='withdraw_js'),
    path('send_message/', views.send_chat_message, name='chat'),

]

