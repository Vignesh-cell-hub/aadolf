from django.db import models
from django.contrib.auth.models import User

COLOR_CHOICES = (
    ('Company1','Company1'),
    ('Company2','Company2'),
)

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    organisation=models.CharField(max_length=200, choices=COLOR_CHOICES,default='Company1')

    def __str__(self):
        return self.user.username


# class Organisation(models.Model):
#     organisation_name=models.CharField(max_length=200,default="")
#     Gst_number=models.CharField(max_length=200,default="")
#     email=models.EmailField(default="")
#
#     def __str__(self):
#         return self.organisation_name
#
# class Profile(models.Model):
#     user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
#     organisation=models.ForeignKey(Organisation ,on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user.usernamez

