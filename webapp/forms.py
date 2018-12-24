from django import forms
from webapp.models import Food, Order, OrderFood


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = []


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = []


class OrderCourierForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'courier']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].choices = [('on_way', 'В пути'),
                                         ('delivered', 'Доставлен'), ]


class OrderFoodForm(forms.ModelForm):
    class Meta:
        model = OrderFood
        exclude = ['order']
