from django.db import models

class ComputerModel (models.Model):
    brand = models.CharField(max_length=20, default='Dell')  #производитель
#    type = models.CharField(max_length=10, default='laptop')  #desktops, laptop, tablet
    screen_size = models.FloatField(default=11)
#    installed_OS = models.CharField(max_length=20, default='Windows8')
    processor_type = models.CharField(max_length=20, default='Inspiron 11')
#    RAM = models.FloatField(default=2)
    price = models.CharField(max_length=20, default='30000 руб')

class OrderModel (models.Model):
    order_num = models.IntegerField(unique=True)
    order_date = models.DateField()
    computer = models.ForeignKey('ComputerModel', null=True)

class UserModel (models.Model):
    order_num = models.ForeignKey('OrderModel', null=True)
    user_name = models.CharField(max_length=20)
    user_surname = models.CharField(max_length=20)
    user_thirdname = models.CharField(max_length=20)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=20)
    user_adress = models.CharField(max_length=50)

