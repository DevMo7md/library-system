from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
class Books(models.Model):
    choices = [
        ('Available','Available'),
        ('Sold','Sold'),
        ('Rented','Rented'),
    ]
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    book_photo = models.ImageField(upload_to='photos', blank=True, null=True)
    author_photo = models.ImageField(upload_to='photos', blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    retal_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    retal_peiod = models.IntegerField(blank=True, null=True)
    total_retal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    status = models.CharField(max_length=50, choices=choices, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self) -> str:
        return self.title