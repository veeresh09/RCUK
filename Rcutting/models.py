from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=1000)
    user_loc = models.CharField(max_length=1000)
    user_password = models.CharField(max_length=1000)

    def __str__(self):
        return self.user_name


class RCForm(models.Model):
    applcnt_name = models.CharField(max_length=1000, default='NULL')
    RC_reason = models.TextField(default='NULL')
    RC_Cost = models.PositiveIntegerField(default=500)
    applicnt_fname = models.CharField(max_length=1000, default='NULL')
    applicnt_email = models.CharField(max_length=1000, default='NULL')
    applicant_mobno = models.IntegerField(default=0)
    authtokn = models.TextField(default='NULL')
    applcntaddres = models.TextField(default='NULL')
    applcntdist = models.CharField(max_length=1000, default='NULL')
    applcntpin = models.IntegerField(default=0)
    RD_loc = models.CharField(max_length=1000, default='NULL')
    RD_ulbn = models.CharField(max_length=1000, default='NULL')
    RD_wn = models.CharField(max_length=1000, default='NULL')
    RD_type = models.CharField(max_length=1000, default='NULL')
    RD_len = models.FloatField(default=0.0)
    RD_lclty = models.CharField(max_length=1000, default='NULL')
    RD_ctgry = models.CharField(max_length=1000, default='NULL')
    usr_consmcode = models.CharField(
        max_length=1000, default="RC/06-02-2020/000002")
    # user = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name="rcform")

    def __str__(self):
        return self.applcnt_name
