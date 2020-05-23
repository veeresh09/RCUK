from rest_framework import generics
from rest_framework import mixins

from Rcutting.models import User
from Rcutting.models import RCForm
from Rcutting.api.serializers import Userinfo, Rcformviewer
import requests
import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class UserlistView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = Userinfo

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('user_name', "")
        user_pswd = request.POST.get('user_password', "")
        user_nm = 'CounterEmployee'
        usr_pwd = 'eGov@123'
        url = "https://uttarakhand-uat.egovernments.org/user/oauth/token"
        payload = {'username': username,
                   'password': user_pswd,
                   'grant_type': 'password',
                   'scope': 'read',
                   'tenantId': 'uk.dehradun',
                   'userType': 'EMPLOYEE'}
        headers = {
            'authority': 'uttarakhand-dev.egovernments.org',
            'accept': 'application/json, text/plain, */*',
            'authorization': 'Basic ZWdvdi11c2VyLWNsaWVudDplZ292LXVzZXItc2VjcmV0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://uttarakhand-uat.egovernments.org',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'referer': 'https://uttarakhand-uat.egovernments.org/employee/user/login',
            'accept-encoding': 'utf8',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': '_ga=GA1.2.1111212684.1580208445',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return Response(response.json())


class RCformlistview(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = RCForm.objects.all()
    serializer_class = Rcformviewer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
