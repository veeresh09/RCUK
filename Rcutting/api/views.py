from rest_framework import generics
from rest_framework import mixins
from rest_framework import views
from Rcutting.models import User
from Rcutting.models import RCForm
from Rcutting.api.serializers import Userinfo, Rcformviewer
import requests
import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from Rcutting.api.serializers import ConsumSerializer


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
        # user_nm = 'CounterEmployee'
        # usr_pwd = 'eGov@123'
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
        applcnt_name = request.POST.get('applcnt_name', "")
        #RC_reason = request.POST.get('RC_reason', "")
        RC_Cost = request.POST.get('RC_Cost', "")
        #applicnt_fname = request.POST.get('applicnt_fname', "")
        applicnt_email = request.POST.get('applicnt_email', "")
        applicant_mobno = request.POST.get('applicant_mobno', "")
        authtokn = request.POST.get('authtokn', "")
        applcntaddres = request.POST.get('applcntaddres', "")
        applcntdist = request.POST.get('applcntdist', "")
        applcntpin = request.POST.get('applcntpin', "")
        usr_consmcode = request.POST.get('usr_consmcode', "")
        #RD_loc = request.POST.get('RD_loc', "")
        #RD_ulbn = request.POST.get('RD_ulbn', "")
        #RD_wn = request.POST.get('RD_wn', "")
        #RD_type = request.POST.get('RD_type', "")
        #RD_len = request.POST.get('RD_len', "")
        #RD_lclty = request.POST.get('RD_lclty', "")
        #RD_ctgry = request.POST.get('RD_ctgry', "")
        url = "https://uttarakhand-uat.egovernments.org/billing-service/demand/_create"
        payload = {
            "RequestInfo": {
                "apiId": "Rainmaker",
                "ver": ".01",
                "ts": "",
                "action": "_search",
                "did": "1",
                "key": "",
                "msgId": "20170310130900|en_IN",
                "authToken": authtokn,
                "userInfo": {
                    "id": 224,
                    "userName": "CounterEmployee",
                    "salutation": None,
                    "name": applcnt_name,
                    "gender": "FEMALE",
                    "mobileNumber": applicant_mobno,
                    "emailId": applicnt_email,
                    "altContactNumber": None,
                    "pan": None,
                    "aadhaarNumber": None,
                    "permanentAddress": applcntaddres,
                    "permanentCity": applcntdist,
                    "permanentPinCode": None,
                    "correspondenceAddress": "Bangalore",
                    "correspondenceCity": None,
                    "correspondencePinCode": None,
                    "addresses": [
                        {
                            "pinCode": applcntpin,
                            "city": None,
                            "address": "Bangalore",
                            "type": "CORRESPONDENCE",
                            "id": 447,
                            "tenantId": "uk.dehradun",
                            "userId": 224,
                            "addressType": "CORRESPONDENCE",
                            "lastModifiedDate": None,
                            "lastModifiedBy": None
                        }
                    ],
                    "active": True,
                    "locale": None,
                    "type": "EMPLOYEE",
                    "accountLocked": False,
                    "accountLockedDate": 0,
                    "fatherOrHusbandName": "Test",
                    "signature": None,
                    "bloodGroup": None,
                    "photo": None,
                    "identificationMark": None,
                    "createdBy": 4,
                    "lastModifiedBy": 1,
                    "tenantId": "uk.dehradun",
                    "roles": [
                        {
                            "code": "TL_CEMP",
                            "name": "TL Counter Employee",
                            "tenantId": "uk.dehradun"
                        },
                        {
                            "code": "PTCEMP",
                            "name": "PT Counter Employee",
                            "tenantId": "uk.dehradun"
                        }
                    ],
                    "uuid": "3fc7f632-ff90-4eea-92bc-641fb9a809f1",
                    "createdDate": "13-12-2019 16:32:08",
                    "lastModifiedDate": "16-12-2019 16:21:57",
                    "dob": "1/12/2019",
                    "pwdExpiryDate": "12-03-2020 16:32:08"
                }
            },
            "Demands": [
                {
                    "tenantId": "uk.dehradun",
                    "consumerCode": usr_consmcode,
                    "mobileNumber": "9700339989",
                    "consumerName": "Siva",
                    "serviceType": "RC.road_cutting",
                    "businessService": "RC.road_cutting",
                    "demandDetails": [
                        {
                            "taxHeadMasterCode": "RC_TAX",
                            "collectionAmount": 0,
                            "taxAmount": RC_Cost
                        }
                    ],
                    "taxPeriodFrom": 1580927399034,
                    "taxPeriodTo": 1580927399034,
                    "additionalDetails": {
                        "comment": "Road Cutting Charges"
                    },
                    "payer": {
                        "uuid": "f7219c20-2cbb-4dd3-9d82-041d6bad7cfa"
                    },
                    "consumerType": "RC"
                }
            ]
        }

        payload = json.dumps(payload)
        headers = {
            'authority': 'bihar-uat.egovernments.org',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'accept': 'application/json, text/plain, */*',
            'sec-fetch-dest': 'empty',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://bihar-uat.egovernments.org',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'referer': 'https://bihar-uat.egovernments.org/employee/uc/newCollection',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'accept-encoding': 'utf8',
            'cookie': '_ga=GA1.2.987832590.1579677766'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return Response(response.json())


class getConsumerCode(views.APIView):
    def post(self, request):
        authtoken = request.data.get('authtoken', "")
        payload = {
            "RequestInfo": {
                "apiId": "Mihy",
                "ver": ".01",
                "action": "",
                "did": "1",
                "key": "",
                "msgId": "20170310130900|en_IN",
                "requesterId": "",
                "authToken": authtoken
            },
            "idRequests": [
                {
                    "idName": "",
                    "format": "RC/[CY:dd-MM-yyyy]/[seq_uc_demand_consumer_code]",
                    "tenantId": "bh.biharsharif"
                }
            ]
        }
        payload = json.dumps(payload)
        url = "https://uttarakhand-uat.egovernments.org/egov-idgen/id/_generate"
        headers = {
            'authority': 'bihar-micro-dev.egovernments.org',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'accept': 'application/json, text/plain, */*',
            'sec-fetch-dest': 'empty',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://bihar-micro-dev.egovernments.org',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'referer': 'https://bihar-micro-dev.egovernments.org/employee/uc/newCollection',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'accept-encoding': 'utf8',
            'cookie': '_ga=GA1.2.987832590.1579677766'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return Response(response.json())


class paymentView(views.APIView):
    def post(self, request):
        authtoken = request.data.get('authtoken', "")
        consumcode = request.data.get('consumcode', "")
        print(consumcode)
        print(authtoken)
        # print(request.data)
        payload = {
            "RequestInfo": {
                "apiId": "Rainmaker",
                "ver": ".01",
                "action": "",
                "did": "1",
                "key": "",
                "msgId": "20170310130900|en_IN",
                "requesterId": "",
                "authToken": authtoken
            }
        }
        payload = json.dumps(payload)
        url = "https://uttarakhand-uat.egovernments.org/billing-service/bill/v2/_fetchbill?tenantId=uk.dehradun&consumerCode=" + consumcode
        headers = {
            'authority': 'uttarakhand-uat.egovernments.org',
            'accept': 'application/json, text/plain, */*',
            'sec-fetch-dest': 'empty',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://uttarakhand-dev.egovernments.org',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'referer': 'https://uttarakhand-dev.egovernments.org/employee/egov-common/pay?consumerCode=UK-TL-2019-12-17-000098&tenantId=uk.haridwar',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'accept-encoding': 'utf8',
            'cookie': '_ga=GA1.2.1111212684.1580208445'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return Response(response.json())
