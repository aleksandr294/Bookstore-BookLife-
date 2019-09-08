from django.shortcuts import render

# Create your views here.
def index(request):
    
    count=load_count()
    count=count+1
    save_count(str(count))
  
    return render(request, 'mainPage/MainPage.html', locals())

def save_count(count):
    with open('mainPage\some.txt', 'w+') as the_file:
        the_file.write(count)

def load_count():
    my_file = open("mainPage\some.txt")
    count = my_file.read()
    my_file.close()
    return int(count)