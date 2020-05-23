from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=1000)
    user_loc = models.CharField(max_length=1000)
    user_password = models.CharField(max_length=1000)

    def __str__(self):
        return self.user_name


class RCForm(models.Model):
    Road_name = models.CharField(max_length=1000)
    RC_reason = models.TextField()
    RC_Cost = models.PositiveIntegerField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="rcform")

    def __str__(self):
        return self.Road_name
