from rest_framework import authentication
from rest_framework import exceptions
import json
import requests

class GooGleAuthMiddleware(authentication.BaseAuthentication):
    def authenticate(self, request):
        print("yess")
        response = GooGleAuthMiddleware.token_verification(request.headers['Authorization'].split(' ')[1])
        if response.status_code == 200:
            if 'true' != response.text:
                raise exceptions.AuthenticationFailed('Token Failed')
            else:
                raise exceptions.APIException('Server is not reachable')
        return super().authenticate(request)

    @staticmethod
    def token_verification(token):
        print("hI rAHUL i AM aUTHOMATIC cALL")
        payload = json.dumps({
            'access_token' : token 
        })
        headers = {
            'Content-Type' : 'application/json'
        }
        d = ''
        urls = f'{d}/api'
        try:
            response = requests.request("POST",urls,headers=headers,data=payload,verify=False)
            return response
        except Exception as e:
            raise Exception(e)