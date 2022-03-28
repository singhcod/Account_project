from django.shortcuts import render

# Create your views here.
from Account_app.models import Account
from Account_app.serializers import AccountRegisterSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class AccountRegisterView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountRegisterSerializer