from django.db import models

# Create your models here.


class Host(models.Model):
    name=models.CharField(max_length =100, default='')
    email_address=models.EmailField(max_length = 254) 
    phone=models.BigIntegerField()
    address=models.CharField(max_length=100,default='', blank=True)

    def __str__(self):
        return self.name

class Visitor(models.Model):
    name=models.CharField(max_length =100, default='')
    email_address=models.EmailField(max_length = 254) 
    phone=models.BigIntegerField()
    check_in_time=models.DateTimeField(auto_now_add=True)
    check_out_time=models.DateTimeField(null=True,blank=True)
    host=models.ForeignKey(Host,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name