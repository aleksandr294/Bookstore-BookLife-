from django.db import models

# Create your models here.
class Subscribers(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=128)
    password=models.CharField(max_length=50)
    

    def __str__(self):
        return 'Пользователь %s '% (self.name)
