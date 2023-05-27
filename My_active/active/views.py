import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Stock, PersonalStock, ListStock, ChatMessage
from django.contrib.auth.models import User

def index(request):

    stock_list = Stock.objects.all()
    context = {'stock_list': stock_list, }
    return render(
        request,
        'index.html',
        context=context
    )

# список акций зарегистрированные в приложении
def action_list(request):
    stock_list = Stock.objects.all()
    context = {'stock_list': stock_list, }
    return render(
        request,
        'active/action_list.html',
        context=context
         )

# функция для обновления базы данных пользователя
def update_db():

    #################################################################

    # выбираем всех пользователей
    persn = PersonalStock.objects.all()

    # считаем все купленные акции пользователя и заносим общее число в базу данных пользователя
    # и обновляем общую текущую и балансовую стоимость активов
    for per in persn:  # перебираем пользователей
        per.fixPrice = 0
        totalMany = 0
        totalFixMany = 0
        objPer = ListStock.objects.all().filter(pers=per)

        for st in Stock.objects.all().order_by('id'):  # перебираем зарегистрированные акции
            sum = 0

            for obj in objPer:  # перебираем объекты пользователя,
                # принадлежащие текущей акции в цикле

                if obj.userListName == st.name:
                    sum += int(obj.countStock)
                    totalFixMany += obj.userListPrice * int(obj.countStock)

            per.fixPrice = round(totalFixMany, 2)
            if st.id == 1:
                per.totalCountAPLE = sum
                totalMany += st.price * sum
            elif st.id == 2:
                per.totalCountAMZN = sum
                totalMany += st.price * sum
            elif st.id == 3:
                per.totalCountTSLA = sum
                totalMany += st.price * sum
            elif st.id == 4:
                per.totalCountMSFT = sum
                totalMany += st.price * sum
            elif st.id == 5:
                per.totalCountAMD = sum
                totalMany += st.price * sum
            per.currentMany = round(totalMany, 2)
            per.save()


# функция представления для всех акций у пользователя
def action_list_user(request):

    # текущий пользователь
    stock_user_list_id = PersonalStock.objects.filter(PersonalStockNameUser=request.user)
    stock_user_list_id = stock_user_list_id[0]

    context = {}

    # список всех зарегистрированных акций
    stocks = Stock.objects.all()


    # если количество купленных акций не ноль, то работаем с этой акцией
    if stock_user_list_id.totalCountAPLE:
        update_db()

        # цена при которой мы купили эту акцию
        sumFixPrice = 0

        # название акции
        context['APLE'] = [stocks[0].name]

        # количество всех этих акций
        context['APLE'].append(stock_user_list_id.totalCountAPLE)

        # текущая цена этих акций
        context['APLE'].append(stocks[0].price * stock_user_list_id.totalCountAPLE)

        # округляем эту цену до двух знаков после запятой
        context['APLE'][2] = round(context['APLE'][2], 2)

        # цикл по всем объектам принадлежащие текущему пользователю и рассматриеваемой акции
        for i in ListStock.objects.filter(pers__PersonalStockNameUser=request.user).filter(userListName='APLE'):

            # считаем цену при которой купили эту акцию
            sumFixPrice += i.userListPrice * int(i.countStock)

        # разница мужду текущей ценой этой акции и при которой мы эти акции купили
        context['APLE'].append(context['APLE'][2] - sumFixPrice)

        # округляем до двух знаков после запятой
        context['APLE'][3] = round(context['APLE'][3], 2)

        context['APLE'].append(stocks[0].pk)


    if stock_user_list_id.totalCountAMZN:

        update_db()

        sumFixPrice = 0
        context['AMZN'] = [stocks[1].name]
        context['AMZN'].append(stock_user_list_id.totalCountAMZN)
        context['AMZN'].append(stocks[1].price * stock_user_list_id.totalCountAMZN)
        context['AMZN'][2] = round(context['AMZN'][2], 2)
        for i in ListStock.objects.filter(pers__PersonalStockNameUser=request.user).filter(userListName='AMZN'):
            sumFixPrice += i.userListPrice * int(i.countStock)
        context['AMZN'].append(context['AMZN'][2] - sumFixPrice)
        context['AMZN'][3] = round(context['AMZN'][3], 2)
        context['AMZN'].append(stocks[1].pk)

    if stock_user_list_id.totalCountTSLA:

        update_db()

        sumFixPrice = 0
        context['TSLA'] = [stocks[2].name]
        context['TSLA'].append(stock_user_list_id.totalCountTSLA)
        context['TSLA'].append(stocks[2].price * stock_user_list_id.totalCountTSLA)
        context['TSLA'][2] = round(context['TSLA'][2], 2)
        for i in ListStock.objects.filter(pers__PersonalStockNameUser=request.user).filter(userListName='TSLA'):
            sumFixPrice += i.userListPrice * int(i.countStock)
        context['TSLA'].append(context['TSLA'][2] - sumFixPrice)
        context['TSLA'][3] = round(context['TSLA'][3], 2)
        context['TSLA'].append(stocks[2].pk)

    if stock_user_list_id.totalCountMSFT:

        update_db()

        sumFixPrice = 0
        context['MSFT'] = [stocks[3].name]
        context['MSFT'].append(stock_user_list_id.totalCountMSFT)
        context['MSFT'].append(stocks[3].price * stock_user_list_id.totalCountMSFT)
        context['MSFT'][2] = round(context['MSFT'][2], 2)
        for i in ListStock.objects.filter(pers__PersonalStockNameUser=request.user).filter(userListName='MSFT'):
            sumFixPrice += i.userListPrice * int(i.countStock)
        context['MSFT'].append(context['MSFT'][2] - sumFixPrice)
        context['MSFT'][3] = round(context['MSFT'][3], 2)
        context['MSFT'].append(stocks[3].pk)

    if stock_user_list_id.totalCountAMD:

        update_db()

        sumFixPrice = 0
        context['AMD'] = [stocks[4].name]
        context['AMD'].append(stock_user_list_id.totalCountAMD)
        context['AMD'].append(stocks[4].price * stock_user_list_id.totalCountAMD)
        context['AMD'][2] = round(context['AMD'][2], 2)
        for i in ListStock.objects.filter(pers__PersonalStockNameUser=request.user).filter(userListName='AMD'):
            sumFixPrice += i.userListPrice * int(i.countStock)
        context['AMD'].append(context['AMD'][2] - sumFixPrice)
        context['AMD'][3] = round(context['AMD'][3], 2)
        context['AMD'].append(stocks[4].pk)

    # разница между текущей ценой всех акций и ценой всех акций при которой мы их купили
    profit = round(stock_user_list_id.currentMany - stock_user_list_id.fixPrice, 2)

    # вычитаем из баланса пользователя цену купленных акций
    deposit = stock_user_list_id.deposit - stock_user_list_id.fixPrice
    deposit = round(deposit, 2)



    return render(
        request,
        'active/action_list_user.html',
        {'context': context, 'profit': profit, 'deposit': deposit }
    )

# функция представления для всех акций авторизованного пользователя
def action_list_for_user(request):


    stock_list = Stock.objects.all()
    context = {'stock_list': stock_list, }

    return render(
        request,
        'active/action_list_for_user.html',
        context=context
    )


from .forms import SignUpForm, LoginUserForm, BuyPersonalStockForm, Replenishment, Withdraw, ChatMessageForm


def registration(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print(form)
            user = form.save()
            new_pers = PersonalStock()
            new_pers.PersonalStockNameUser = user
            new_pers.save()


            login(request, user)
            return redirect('stock_user')
        else:
            print("Форма не прошла валидацию!")
    else:
        form = SignUpForm()
    return render(request, 'active/signup.html', {'form': form})


# функция представления для js файла
def redirect_to_js(request):
    with open('C://Django//My_active//My_active//active//static//js//showWindow.js', encoding='utf-8') as f:
        js_code = f.read()
    return HttpResponse(js_code, content_type='application/javascript')


# функция представления для js файла для вывода ошибки в выводе средств
def withdraw_to_js(request):
    with open('C://Django//My_active//My_active//active//static//js//withdraw.js', encoding='utf-8') as f:
        js_code = f.read()
        print(js_code)
    return HttpResponse(js_code, content_type='application/javascript')



# функция формы для покупки акций
def buy_stock(request, pk):

    user = request.user
    print('покупка акций')
    # текущий объект пользователя
    persnl = PersonalStock.objects.filter(PersonalStockNameUser=user)

    # объект выбранной зарегистрированной акции
    your_model_obj = Stock.objects.get(pk=pk)

    # форма для покупки акции
    form = BuyPersonalStockForm(request.POST)

    if request.method == 'POST':
        print("метод POST")
        if form.is_valid():
            countStock_new = form.cleaned_data
            print(countStock_new)
            countStock_new = countStock_new['countStock']
            if persnl[0].deposit - int(countStock_new) * your_model_obj.price < 0:
                print('Недостаточно средств!')

                return render(request, 'active/buy_stock.html', {'countStock': 'NoMany'},)

            print('форма прошла валидацию!')
            form.save()

            # список всех объектов купленных акций
            for i in ListStock.objects.all():
                print(i)
            persn = ListStock.objects.all().order_by('-id')[0]

            print(persn, ' - последний элемент')

            # выбираем последний элемент у всех купленных акций и присваиваем к этому объекту объект текущего пользователя
            persn.pers = persnl[0]

            # присваиваем последнему объекту имя имя выбранной акции
            persn.userListName = your_model_obj.name

            # присваиваем последнему объекту цену выбранной акции
            persn.userListPrice = your_model_obj.price

            persn.save()

            update_db()
            return redirect('stock_user')
        else:
            form = BuyPersonalStockForm()
    return render(request, 'active/buy_stock.html', {'form': form, 'your_model_obj': your_model_obj})



# функция для продажи акций пользователя
def sell_stock(request, pk):
    context = []
    stock_user_list_id = PersonalStock.objects.filter(PersonalStockNameUser=request.user)
    stock_user_list_id = stock_user_list_id[0]
    profit = round(stock_user_list_id.currentMany - stock_user_list_id.fixPrice, 2)
    your_model_obj = Stock.objects.get(pk=pk)
    stocks = Stock.objects.all()

    if your_model_obj.name == 'APLE':

        sumFixPrice = 0
        # название выбранной пользователем акции на продажу
        context.append(stocks[0].name)

        # количество выбранных акций
        context.append(stock_user_list_id.totalCountAPLE)

        # текущая цена на продажу этих акций
        context.append(stocks[0].price * stock_user_list_id.totalCountAPLE)

        # округляем до дух чисел после запятой
        context[2] = round(context[2], 2)

        # считаем цену при которой купили эти акции
        for i in ListStock.objects.filter(pers__PersonalStockNameUser=request.user).filter(userListName='APLE'):
            sumFixPrice += i.userListPrice * int(i.countStock)

        # вычисляем разницу при которой купили и потом продали эти акции
        context.append(context[2] - sumFixPrice)

        # округляем разницу до двух чисел после запятой
        context[3] = round(context[3], 2)
        print(context[3])

        context.append(stocks[0].pk)


    if your_model_obj.name == 'AMZN':
        sumFixPrice = 0
        context.append(stocks[1].name)
        context.append(stock_user_list_id.totalCountAMZN)
        context.append(stocks[1].price * stock_user_list_id.totalCountAMZN)
        context[2] = round(context[2], 2)
        for i in ListStock.objects.filter(pers__PersonalStockNameUser=request.user).filter(userListName='AMZN'):
            sumFixPrice += i.userListPrice * int(i.countStock)
        context.append(context[2] - sumFixPrice)
        context[3] = round(context[3], 2)
        print(context[3])

        context.append(stocks[1].pk)

    if your_model_obj.name == 'TSLA':
        sumFixPrice = 0
        context.append(stocks[2].name)
        context.append(stock_user_list_id.totalCountTSLA)
        context.append(stocks[2].price * stock_user_list_id.totalCountTSLA)
        context[2] = round(context[2], 2)
        for i in ListStock.objects.filter(pers__PersonalStockNameUser=request.user).filter(userListName='TSLA'):
            sumFixPrice += i.userListPrice * int(i.countStock)
        context.append(context[2] - sumFixPrice)
        context[3] = round(context[3], 2)
        print(context[3])

        context.append(stocks[2].pk)

    if your_model_obj.name == 'MSFT':
        sumFixPrice = 0
        context.append(stocks[3].name)
        context.append(stock_user_list_id.totalCountMSFT)
        context.append(stocks[3].price * stock_user_list_id.totalCountMSFT)
        context[2] = round(context[2], 2)
        for i in ListStock.objects.filter(pers__PersonalStockNameUser=request.user).filter(userListName='MSFT'):
            sumFixPrice += i.userListPrice * int(i.countStock)
        context.append(context[2] - sumFixPrice)
        context[3] = round(context[3], 2)
        print(context[3])

        context.append(stocks[3].pk)

    if your_model_obj.name == 'AMD':
        sumFixPrice = 0
        context.append(stocks[4].name)
        context.append(stock_user_list_id.totalCountAMD)
        context.append(stocks[4].price * stock_user_list_id.totalCountAMD)
        context[2] = round(context[2], 2)
        for i in ListStock.objects.filter(pers__PersonalStockNameUser=request.user).filter(userListName='AMD'):
            sumFixPrice += i.userListPrice * int(i.countStock)
        context.append(context[2] - sumFixPrice)
        context[3] = round(context[3], 2)
        print(context[3])
        context.append(stocks[4].pk)

    if request.method == 'POST':

        print(stock_user_list_id.deposit)
        print('привет!')
        stock_user_list_id.deposit += context[3]
        print(context[3])
        stock_user_list_id.save()
        stock_user_list = ListStock.objects.filter(pers__PersonalStockNameUser=request.user).filter(userListName=context[0])
        print(stock_user_list)
        stock_user_list.delete()

        update_db()
        return redirect('stock_user')

    return render(
        request, 'active/sell_stock.html', {'context': context}
    )

# пополнение баланса
def replenishment_balance(request):

    user = request.user

    persnl = PersonalStock.objects.filter(PersonalStockNameUser=user)
    form = Replenishment(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print("форма прошла валидацию")
            balance = form.cleaned_data.get('deposit')
            persnl = persnl[0]
            persnl.deposit += balance
            persnl.save()

            return redirect('stock_user')
        else:
            form = Replenishment()
        print("форма не прошла валидацию")

    return render(request, 'active/replenishment_balance.html' )

# вывод средств
def withdraw(request):

    user = request.user

    persnl = PersonalStock.objects.filter(PersonalStockNameUser=user)
    form = Withdraw(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            print("форма прошла валидацию")
            withdraw = form.cleaned_data.get('withdraw')

            stock_user_list = ListStock.objects.filter(pers__PersonalStockNameUser=request.user)
            sumMany = 0

            # считаем сколько денег вложено в акции
            for i in stock_user_list:
                sumMany += i.userListPrice

            # если сумма для вывода больше, то вызываем окно с ошибкой
            if persnl[0].deposit - sumMany - withdraw < 0:

                print('Недостаточно средств!')

                return render(request, 'active/withdraw_many.html', {'withdraw': 'NoMany'},)

            persnl = persnl[0]
            persnl.deposit -= withdraw
            persnl.save()
            print(withdraw)
            print(persnl.deposit)
            print(persnl.deposit - withdraw)

            # update_db()



            return redirect('stock_user')
        else:
            form = Withdraw()
        print("форма не прошла валидацию")

    return render(request, 'active/withdraw_many.html')

from django.views import generic
from django.shortcuts import get_object_or_404

class BuyStockListView(generic.ListView):
    model = ListStock


class BuyStockDetailView(generic.DetailView):
    model = ListStock
    template_name = 'active/buy_stock.html'
    context_object_name = "st_user"




class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('stock_user')


def logout_user(request):
    logout(request)
    return redirect('/')




from django.views.generic import ListView
# from .models import ChatMessage



class StockListView(generic.ListView):
    model = Stock
    # paginate_by = 1


def send_chat_message(request):

    if request.method == 'POST':
        form = ChatMessageForm(request.POST, user=request.user)

        if form.is_valid():
            form.save()

            return redirect('chat')
    else:
        form = ChatMessageForm(user=request.user)

    messages = ChatMessage.objects.all().order_by('-id')[:10][::-1]
    user = str(request.user)
    context = {'form': form, 'messages': messages, 'user': user}


    return render(request, 'active/chat.html', context)
