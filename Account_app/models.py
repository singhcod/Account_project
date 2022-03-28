from django.db import models
from multiselectfield import MultiSelectFormField

# Create your models here.
class Account(models.Model):
    roles = (
        ('per_owner','pet_owner'),
        ('pet_shelter','pet_selter'),
        ('general_user','general_user'),
        ('verterinarian','verternarin'),
    )

    email = models.EmailField(unique=True,max_length=250)
    password = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    role_type = MultiSelectFormField(choices=roles)
    image = models.ImageField(
        upload_to="users/",blank=True,null=True
    )
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.email