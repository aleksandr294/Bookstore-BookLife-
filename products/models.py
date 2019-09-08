from django.db import models

class Product(models.Model):
    image=models.ImageField(upload_to='BookLife\static\css/')
    name_book=models.CharField(max_length=64, blank=True, null=True, default=None)
    author=models.CharField(max_length=30, blank=True, null=True, default=None)
    publishing=models.CharField(max_length=30, blank=True, null=True, default=None)
    book_series=models.CharField(max_length=20, blank=True, null=True, default=None)
    language=models.CharField(max_length=20, blank=True, null=True, default=None)
    year=models.CharField(max_length=5, blank=True, null=True, default=None)
    translator=models.CharField(max_length=30, blank=True, null=True, default=None)
    count=models.CharField(max_length=5, blank=True, null=True, default=None)
    binding=models.CharField(max_length=20, blank=True, null=True, default=None)
    paper=models.CharField(max_length=20, blank=True, null=True, default=None)
    literature=models.CharField(max_length=30, blank=True, null=True, default=None)
    description=models.TextField(blank=True, null=True, default=None)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active=models.BooleanField(default=True)


    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name='Книга'
        verbose_name_plural='Книги'


