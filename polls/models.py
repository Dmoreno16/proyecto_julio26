from django.db import models
from django.forms import DateTimeField

# Create your models here.

class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data=models.DateTimeField('data_published')



