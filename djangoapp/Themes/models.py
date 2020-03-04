from django.db import models

# Create your models here.
from bootstrap_themes import list_themes

class Themes(models.Model):
    theme = models.CharField(max_length=255, default='default', choices=list_themes())