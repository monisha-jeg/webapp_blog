from __future__ import unicode_literals

from django.db import models

import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    post_text = models.CharField(max_length=300)
    def __str__(self):
    	return self.post_text
