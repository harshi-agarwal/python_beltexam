from __future__ import unicode_literals

from django.db import models
from ..user_app.models import User
# Create your models here.
class ProductManager(models.Manager):
    def validate_product(self,param,user):
        errors=[]
        if len(param['prod_name'])<1:
            errors.append("product cannot be blank")
        if len(param['prod_name'])<3:
            errors.append("Too short product name")
        if len(errors)>0:
            return (False,errors)
        else:
            print "True"
            self.create(prod_name=param['prod_name'],user=user)
            return (True,True)

class Product(models.Model):
    prod_name=models.CharField(max_length=50)
    user = models.ForeignKey(User,related_name="mywishlist")
    join = models.ManyToManyField(User,related_name="joined_user")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects= ProductManager()
