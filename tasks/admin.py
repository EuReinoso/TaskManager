from django.contrib import admin
from .models import Task, Block

# Register your models here.
admin.site.register([Task, Block])