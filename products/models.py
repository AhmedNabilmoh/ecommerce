from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    desc = models.TextField(max_length=5000)
    def __str__(self):
        return self.name
    
class product(models.Model):
    name = models.CharField(max_length=50,unique=True)
    price = models.FloatField()
    desc = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey(category,related_name='product',on_delete=models.CASCADE)
    image = models.ImageField()
    def __str__(self):
        return self.name
class cart(models.Model):
    prid =models.DecimalField(max_digits=7,decimal_places=0)
    num =models.DecimalField(max_digits=7,decimal_places=0)