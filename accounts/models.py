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


