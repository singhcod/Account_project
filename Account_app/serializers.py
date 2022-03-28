from rest_framework import serializers

from Account_app.models import Account
from django.contrib.auth.hashers import make_password

class AccountRegisterSerializer(serializers.ModelSerializer):
   password = serializers.CharField(write_only=True)
   class Meta:
       model = Account
       fields = ('firstname','lastname','username','email','password','role_type','mobile','image')


   def create(self,validated_data):
       account = Account.objects.create(
           firstname=validated_data['firstname'],
           lastname=validated_data['lastname'],
           username=validated_data['username'],
           email = validated_data['email'],
           mobile=validated_data['mobile'],
           password=make_password(validated_data['password'],salt='hello'),
           role_type= validated_data['role_type'],
           image= validated_data['image']
       )
       account.save()
       return account