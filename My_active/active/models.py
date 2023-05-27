from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Stock(models.Model):
    name = models.CharField(max_length=100, default=None)
    data_open = models.DateField(null=True, blank=True, default=None)
    price = models.FloatField(null=True, default=0)
    image = models.ImageField(null=True, upload_to='stock/images/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('action-detail', args=[str(self.id)])


class PersonalStock(models.Model):
    PersonalStockNameUser = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    deposit = models.FloatField(default=0)
    currentMany = models.FloatField(default=0)
    fixPrice = models.FloatField(null=True, default=0)

    totalCountAPLE = models.IntegerField(default=0)
    totalCountAMZN = models.IntegerField(default=0)
    totalCountTSLA = models.IntegerField(default=0)
    totalCountMSFT = models.IntegerField(default=0)
    totalCountAMD = models.IntegerField(default=0)

    def __str__(self):
        return self.PersonalStockNameUser.username


class ListStock(models.Model):
    pers = models.ForeignKey('PersonalStock', null=True, default=None, on_delete=models.CASCADE)
    idStock = models.ForeignKey('Stock', null=True, default=None, on_delete=models.CASCADE)
    userListName = models.CharField(max_length=100, blank=True, null=True)
    userListPrice = models.FloatField(null=True, default=0)
    countStock = models.CharField(max_length=100, null=True, default='0')

    # def __str__(self):
    #     return self.idStock.name

    def get_absolute_url(self):
        return reverse('buy_stocks', args=[str(self.id)])

    def update_stock(self):
        self.userListPrice = self.idStock.price
        self.userListName = self.idStock.name
        return self.userListName, self.userListPrice


class ChatMessage(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return '{}: {}'.format(self.user.username, self.message)

