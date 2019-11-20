from django.db import models

# Create your models here.
class Visior(models.Model):
    name=models.CharField(max_length =100, default='')
    email_adress=models.EmailField(max_length = 254) 
    phone=models.BigIntegerField(default=0)
    check_in_time=models.DateTimeField(auto_now_add=True)
    check_out_time=models.DateTimeField()

    def __str__(self):
        return self.name

class Host(models.Model):
    name=models.CharField(max_length =100, default='')
    email_adress=models.EmailField(max_length = 254) 
    phone=models.BigIntegerField(default=0)

    def __str__(self):
        return self.name

