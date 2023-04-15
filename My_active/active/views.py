from django.shortcuts import render
from .models import Stock

def index(request):
    stock_list = Stock.objects.all()
    context = {'stock_list': stock_list, }
    return render(
        request,
        'index.html',
        context=context
    )

def action_list(request):
    stock_list = Stock.objects.all()
    context = {'stock_list': stock_list, }
    return render(
        request,
        'active/action_list.html',
        context=context
         )

def registration(request):
    return render(
        request,
        'active/registration.html'
    )

from django.views import generic


class StockListView(generic.ListView):
    model = Stock
    # paginate_by = 1

