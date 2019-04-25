from django.db import models

# Create your models here.
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_heading = models.CharField(max_length=250)
    comment_body = models.TextField()
