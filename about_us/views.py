from django.shortcuts import render
from .forms import UserForm
# Create your views here.

# Create your views here.
def about_us(request):
    userform = UserForm(request.POST or None)
    if request.method =="POST" and userform.is_valid():
        price = request.POST.get("order_price")
        if int(price)>=500 and int(price)<1000:
            skid='Ваша скидка составляет '
            discount=int(price)*0.25
            skid=skid+str(discount)+' грн'
        elif int(price)<500:
            skid='У вас нет скидки'
        else:
            skid='Ваша скидка составляет '
            discount=int(price)*0.35
            skid=skid+str(discount)+' грн'
    return render(request, 'about_us/usBlock.html',locals())