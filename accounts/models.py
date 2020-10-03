from django.db import models
from django.contrib.auth.models import User

STATE_CHOICES = (
    ('andamanandnicobar Islands','Andaman and Nicobar Islands'),
    ('arunachalpradesh','Arunachal Pradesh'),
    ('assam','Assam'),
    ('bihar','Bihar'),
    ('chandigarh','Chandigarh'),
    ('chhattisgarh','Chhattisgarh'),
    ('dadra','Dadra and Nagar Haveli and Daman and Diu'),
    ('delhi','Delhi'),
    ('goa','Goa'),
    ('gujarat','Gujarat'),
    ('haryana','Haryana'),
    ('himachal','Himachal Pradesh'),
    ('jammu','Jammu and Kashmir'),
    ('jhar','Jharkhand'),
    ('kar','Karnataka'),
    ('ker','Kerala'),
    ('ladakh','Ladakh'),
    ('lak','Lakshadweep'),
    ('madh','Madhya Pradesh'),
    ('maha','Maharashtra'),
    ('mani','Manipur'),
    ('mizo','Mizoram'),
    ('naga','Nagaland'),
    ('odi','Odisha'),
    ('puducherry','Puducherry'),
    ('punjab','Punjab'),
    ('rajas','Rajasthan'),
    ('sikkim','Sikkim'),
    ('tamilnadu','Tamil Nadu'),
    ('tel','Telangana'),
    ('tri','Tripura'),
    ('uttar','Uttar Pradesh'),
    ('uttarkhand','Uttarakhand'),
    ('westbengal','West Bengal'),
)
#
# class Profile(models.Model):
#     user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
#     organisation=models.CharField(max_length=200, choices=COLOR_CHOICES,default='Company1')
#
#     def __str__(self):
#         return self.user.username


class Organisation(models.Model):
    organisation_logo=models.ImageField(upload_to ='uploads/')
    organisation_name=models.CharField(max_length=200,default="")
    industry = models.CharField(max_length=200, default="")
    business_location = models.CharField(max_length=200, default="")
    company_address1 = models.CharField(max_length=200, default="")
    company_address2 = models.CharField(max_length=200, default="",null=True)
    city = models.CharField(max_length=200, default="")
    state = models.CharField(max_length=200,choices=STATE_CHOICES,default="tamilnadu")
    zipcode=models.CharField(max_length=200,default="")
    fax=models.CharField(max_length=200,default="")
    ph_no=models.CharField(max_length=200,default="")
    Company_ID=models.CharField(max_length=200,default="")
    Tax_ID = models.CharField(max_length=200, default="")
    website=models.CharField(max_length=200, default="")
    email=models.EmailField(default="")

    def __str__(self):
        return self.organisation_name

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    organisation=models.ForeignKey(Organisation ,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

