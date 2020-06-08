from rest_framework import views
import requests
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from Rcutting.api.serializers import ConsumSerializer


class Collectpay(views.APIView):
    def post(self, request):
        authtoken = request.data.get('authtoken', "")
        billId = request.data.get('billId', "")
        totalAmountPaid = request.data.get('totalAmountPaid', "")
        mobileNumber = request.data.get('mobileNumber', "")
        payerName = request.data.get('payerName', "")
        payload = {
            "RequestInfo": {
                "apiId": "Rainmaker",
                "ver": ".01",
                "action": "_create",
                "did": "1",
                "key": "",
                "msgId": "20170310130900|en_IN",
                "requesterId": "",
                "authToken": authtoken
            },
            "Payment": {
                "paymentDetails": [
                    {
                        "businessService": "RC",
                        "billId": billId,
                        "totalDue": totalAmountPaid,
                        "totalAmountPaid": totalAmountPaid
                    }
                ],
                "tenantId": "uk.dehradun",
                "totalDue": totalAmountPaid,
                "paymentMode": "Cash",
                "paidBy": "COMMON_OWNER",
                "mobileNumber": mobileNumber,
                "payerName": payerName,
                "totalAmountPaid": totalAmountPaid
            }
        }
        payload = json.dumps(payload)
        url = "https://uttarakhand-uat.egovernments.org/collection-services/payments/_create?"
        headers = {
            'authority': 'uttarakhand-uategovernments.org',
            'accept': 'application/json, text/plain, */*',
            'sec-fetch-dest': 'empty',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://uttarakhand-uat.egovernments.org',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'referer': 'https://uttarakhand-uat.egovernments.org/employee/egov-common/pay?consumerCode=UC/27-02-2020/000126&tenantId=uk.dehradun',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': '_ga=GA1.2.1111212684.1580208445',
            'accept-encoding': 'utf8'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        resp = response.json()
        print(type(resp))
        key = 'Errors'
        # print(resp)
        respon = dict()
        if(key in resp.keys()):
            respon['message'] = resp[key][0]['code']
            respon['recieptNo'] = 'NULL'
            respon['transactionNumber'] = "NULL"
            respon['totalAmountPaid'] = 'NULL'
        else:
            respon['message'] = "succesfull"
            respon['recieptNo'] = resp['Payments'][0]['paymentDetails'][0]['receiptNumber']
            respon['transactionNumber'] = resp['Payments'][0]['transactionNumber']
            respon['totalAmountPaid'] = resp['Payments'][0]['paymentDetails'][0]['totalAmountPaid']
        return Response(respon)
