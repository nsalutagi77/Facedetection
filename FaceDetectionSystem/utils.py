from twilio.rest import Client


# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = 'AC3c410f0c033d8bc43d3d112aa4c634b2'
auth_token = '3de1d39e56c5de2830a7748ef2a1f4b3'

client = Client(account_sid, auth_token)

def send_sms(user_code, phone_number):
    message = client.api.account.messages.create(
        body=f'Hi! Your login verification code  {user_code}',
        to=f'{phone_number}',
        from_="+13614705426",
        )
    print("mobile number",phone_number)