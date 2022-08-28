from django.db import models

# Create your models here.
class BlogUser(models.Model):
    uid=models.AutoField
    uname=models.CharField(max_length=50)
    upassword=models.CharField(max_length=40)

    def __str__(self):
        return self.uname