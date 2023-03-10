from django.db import models

from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class CheckList(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ListItem(models.Model):
    text = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    checklist = models.ForeignKey(CheckList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text