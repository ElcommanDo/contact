from django.db import models

# Create your models here.

class Message(models.Model):
    name  = models.CharField(max_length=120)
    phone = models.CharField(max_length=11)
    Email = models.EmailField()
    Msg   = models.TextField(max_length=600)
    def __str__(self):
        return 'message from {} '.format(self.name) 
