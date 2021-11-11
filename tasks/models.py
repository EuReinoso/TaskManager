from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Block(models.Model):
    
    title = models.CharField(max_length=255, default='')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Task(models.Model):

    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    description = models.TextField(default='')
    done = models.CharField(
        max_length=5,
        choices = STATUS
    )
    block = models.ForeignKey(Block, on_delete= models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description