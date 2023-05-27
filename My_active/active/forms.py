from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import ListStock, PersonalStock, ChatMessage


# форма для регистрации пользователя
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('username', 'password1' )

# форма для входа в личный кабнет
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

class ModelChoiceIterator(forms.models.ModelChoiceIterator):
    def __iter__(self):
        for obj in self.queryset.all():
            yield (obj, self.choice(obj))

# форма для покупки акций
class BuyPersonalStockForm(forms.ModelForm):
    countStock = forms.CharField(max_length=100, initial='123')

    class Meta:
        model = ListStock
        fields = ('countStock',)


# форма пополнения баланса
class Replenishment(forms.ModelForm):
    deposit = forms.FloatField()

    class Meta:
        model = PersonalStock
        fields = ('deposit',)

# форма для вывода средств
class Withdraw(forms.ModelForm):
    withdraw = forms.FloatField()

    class Meta:
        model = PersonalStock
        fields = ('withdraw', )


# форма для создания сообщения
class ChatMessageForm(forms.ModelForm):

    class Meta:
        model = ChatMessage
        fields = ['message']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')


        super().__init__(*args, **kwargs)

    def save(self, commit=True):

        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance

