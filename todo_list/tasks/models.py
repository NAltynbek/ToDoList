from django.db import models

class Task(models.Model):
    text = models.CharField(max_length=50)
    done = models.BooleanField(default=False)


    def __str__(self):
        return self.text
