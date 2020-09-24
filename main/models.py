from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length = 20)
    userid = models.CharField(max_length = 20)
    userpassword = models.CharField(max_length = 20)