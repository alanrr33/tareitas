from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Pendiente(models.Model):
    title=models.CharField(max_length=150)
    memo=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    datecompleted=models.DateTimeField(null=True,blank=True)
    important=models.BooleanField(default=False)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
