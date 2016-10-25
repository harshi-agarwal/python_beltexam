from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
import datetime
# Create your models here.
class UserManager(models.Manager):
    def validate(self,user):
        errors=[]
        user1=User.objects.filter(username=user['username'])
        name_regex = re.compile(r'^[a-zA-Z]+$')
        username_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+$')
        if len(user['fname'])<3 and not name_regex.match(user['fname']):
            print "false name"
            errors.append("Invalid name or too short")
        if len(user['username'])<1:
            errors.append("username cannot be blank!")
        if not username_REGEX.match(user['username']) and len(user['username'])<3:
            print "false username"
            errors.append("Invalid username or too short !")
        if len(user['password']) <8:
            print "false password"
            errors.append("too short password")
        if not user['cpassword'] == user['password']:
            # print user['password']
            # print user['cpassword']
            print "false confirm password"
            errors.append("password and confirm password do not match")
        if user['datehired'] < str(datetime.date.today()) and len(user['datehired']) <1:
            print "wrong date"
            errors.append("date hired cannot be back dated or empty")
        if user1:
            errors.append("username already taken !")
        if len(errors)>0:
            return (False,errors)
        else:
            print "true"
            # print user
            pass2=user['password']
            pass3=pass2.encode()
            hashed= bcrypt.hashpw(pass3,bcrypt.gensalt())
            # print hashed
            # pass1= bcrypt.hashpw(pass3,hashed)
            # print pass1
            User.objects.create( name=user['fname'],username=user['username'],Password=hashed)
            return (True,user)
    def login(self,user):
        print user
        user_log=self.filter(username=user['username'])
        if user_log:
            print user_log
            pass2=user['Password']
            pass3=pass2.encode()
            if bcrypt.hashpw(pass3,user_log[0].Password.encode())== user_log[0].Password:
                print user_log[0].id
                return {'user':user_log[0]}
            # else:
        return{'error':"username or password failed"}


class User(models.Model):
    name= models.CharField(max_length=50)
    username= models.CharField(max_length=50)
    Password= models.CharField(max_length=255)
    datehired =models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)




    objects=UserManager()
