from django.contrib.auth.mixins import UserPassesTestMixin
from kavenegar import *

def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('416E464557734A644D4444684C6D655A475333433545577A366F676D52637865436850733476332B4878343D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message' : f'{code} کد شما'
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
        
class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin
