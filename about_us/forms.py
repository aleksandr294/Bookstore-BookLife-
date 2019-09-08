from django import forms
 
class UserForm(forms.Form):
    order_price = forms.CharField(label='Сумма заказа')