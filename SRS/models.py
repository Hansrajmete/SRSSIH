from __future__ import unicode_literals
from django.db import models


class user(models.Model):
    user_name = models.CharField(primary_key=True, max_length=25)
    password = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=20, null=True)

class user_details(models.Model):
    user_name=models.ForeignKey(user, on_delete=models.CASCADE)
    aadhaar = models.CharField(max_length=100,null=True)
    pancard = models.CharField(max_length=100,null=True)
    hsc = models.CharField(max_length=100,null=True)
    ssc = models.CharField(max_length=100,null=True)
    cast_certificate = models.CharField(max_length=100,null=True)
    first_name = models.CharField(max_length=20,null=True)
    middle_name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=20,null=True)
    gender = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=20,null=True)
    city = models.CharField(max_length=20,null=True)
    state = models.CharField(max_length=20,null=True)
    pincode = models.CharField(max_length=20,null=True)
    country=models.CharField(max_length=20,null=True)

class jobs(models.Model):
    job_id = models.AutoField(primary_key=True, max_length=10)
    job_name = models.CharField(max_length=20,null=True)
    job_description = models.CharField(max_length=20,null=True)
    date_of_joining = models.DateField(max_length=20,null=True)
    location = models.CharField(max_length=20,null=True)

class applied_jobs(models.Model):
    job_id=models.ForeignKey(jobs,on_delete=models.CASCADE,related_name='app_job')
    user_name = models.ForeignKey(user, on_delete=models.CASCADE, related_name='app_user')
    dof_app=models.DateField(max_length=20,null=True)
    status=models.IntegerField(default='1')
