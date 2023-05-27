import psycopg2
from django.contrib import admin
from psycopg2 import OperationalError
from .models import Stock, PersonalStock, ListStock, ChatMessage


# проверка соединения с БД
def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to MySQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):

    import requests
    from datetime import date, timedelta


    # список зарегистрированных акций
    list_stock = ['APLE', 'AMZN', 'TSLA', 'MSFT', 'AMD']

    # дата в которой делаем Api запрос
    date_now = str(date.today() - timedelta(days=2))

    # список для добавления в базу данных
    lst_data = []


    # делаем запрос Api для каждой акции
    for ind, i in enumerate(list_stock):
        lst_data_intr = []
        api_key = f'https://api.polygon.io/v1/open-close/{i}/{date_now}?adjusted=true&apiKey=7rhXA8XJzBJa6rtQOFzNL2efEy_LV4MI'
        BASE_URL = api_key
        response = requests.get(f"{BASE_URL}")
        res = response.json()

        # сохраняем нужные нам значения из запроса
        lst_data_intr.append(res['symbol'])
        lst_data_intr.append(res['from'])
        lst_data_intr.append(res['high'])
        lst_data.append(lst_data_intr)
        # print(lst_data_intr)
    # получаем все наши объекты, то есть зарегистрированные акции
    posts = Stock.objects.all()

    # наше соединение с БД
    connection = create_connection("active", "postgres", "admin", "127.0.0.1", "5432")

    for i in range(len(posts)):

        # переменная для моего курсора
        mycursor = connection.cursor()

        # меняем значения наших зарегистрированных акций
        update_val = f"""
        UPDATE active_stock SET data_open = '{lst_data[i][1]}', price = {lst_data[i][2]} WHERE name = '{lst_data[i][0]}'
        """

        # вставляем новый объект для наших акций
        insert_val = f"""
        INSERT INTO active_stock (name, data_open, price, image)
        VALUES ('{lst_data[i][0]}', '{lst_data[i][1]}', {lst_data[i][2]}, null);
        """

        # смотрим все наши зарегистрированные акции
        select_all = f"""
            SELECT * from active_stock;
        """

        # удаляем все наши акции
        delete_all = f"""DELETE FROM active_stock;"""


        mycursor.execute(update_val)    # делаем запрос
        connection.commit()             # делаем сохраниние запроса


        mycursor.execute(select_all)
        connection.commit()

        myresult = mycursor.fetchall()
        for j in myresult:
            print(j)


    list_display = ('id', 'name', 'data_open', 'price')


@admin.register(PersonalStock)
class PersonalStockAdmin(admin.ModelAdmin):
    list_display = ('PersonalStockNameUser', 'fixPrice', 'deposit', 'currentMany', 'totalCountAPLE', 'totalCountAMZN', 'totalCountTSLA', 'totalCountMSFT', 'totalCountAMD', )



@admin.register(ListStock)
class ListStockAdmin(admin.ModelAdmin):
    list_display = ('pers', 'userListName', 'countStock' )


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'create_date', )
#
# @admin.register(ChatMessageListView)
# class ChatMessageListViewAdmin(admin.ModelAdmin):
#     list_display = ('user', 'message', 'create_date', )
#
