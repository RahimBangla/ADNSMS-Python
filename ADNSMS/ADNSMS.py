import requests
# import random
# import json
# import datetime


class ADNSMS:

    url = 'https://portal.adnsms.com'
    check_balance = '/api/v1/secure/check-balance'
    send_sms = '/api/v1/secure/send-sms'
    check_campaign_status = '/api/v1/secure/campaign-status'
    check_sms_status = '/api/v1/secure/sms-status'

    def __init__(self, API_KEY, API_SECRET):
        '''
        Set default authentication parameters
        :param API_KEY:
        :param API_SECRET:
        '''
        self.API_KEY = API_KEY
        self.API_SECRET = API_SECRET

    # This Check Balance

    def checkBalance(self):
        '''
        Send the message to desired number
        :return: json
        '''
        result = requests.post(
            self.url+self.check_balance,
            data={
                'api_key': self.API_KEY,
                'api_secret': self.API_SECRET
            }
        )

        return result

    # This single/All in one send sms

    def send(self, request_type, message_type, mobile, message):
        '''
        Send the message to desired number
        :param mobile:
        :param message:
        :return: json
        '''
        result = requests.post(
            self.url+self.send_sms,
            data={
                'api_key': self.API_KEY,
                'api_secret': self.API_SECRET,
                'request_type': request_type,
                'message_type': message_type,
                'mobile': mobile,
                'message_body': message,
            }
        )

        return result

    # This OTP send sms

    def otp(self, message_type, mobile, message):
        '''
        Send the message to desired number
        :param mobile:
        :param message:
        :return: json
        '''
        result = requests.post(
            self.url+self.send_sms,
            data={
                'api_key': self.API_KEY,
                'api_secret': self.API_SECRET,
                'request_type': 'OTP',
                'message_type': message_type,
                'mobile': mobile,
                'message_body': message,
            }
        )

        return result

    # This Bulk send sms

    def sendBulkSms(self, message_type, mobile, message, campaignTitle=None):
        '''
        Send the message to desired number
        :param message_type:
        :param mobile:
        :param message:
        :param campaignTitle:
        :return: json
        '''
        data = {
            'api_key': self.API_KEY,
            'api_secret': self.API_SECRET,
            'request_type': 'GENERAL_CAMPAIGN',
            'message_type': message_type,
            'mobile': mobile,
            'message_body': message,
        }
        if campaignTitle == None:
            return {'Campaign Title is required for bulk campaign'}
        data['campaign_title'] = campaignTitle
        result = requests.post(
            self.url+self.send_sms,
            data=data
        )

        return result

    # This multibodyCampaign send sms (Comming Soon)

    # def multibodyCampaign(self, smsArray, message_type, campaignTitle=None):
    #     '''
    #     Send the message to desired number
    #     :param smsArray:
    #     :param message_type:
    #     :param campaignTitle:
    #     :return: json
    #     '''

    #     data = {
    #         'api_key': self.API_KEY,
    #         'api_secret': self.API_SECRET,
    #         'request_type': 'MULTIBODY_CAMPAIGN',
    #         'message_type': message_type,
    #     }
    #     if campaignTitle != None:
    #         data['campaign_title'] = campaignTitle

    #     for key, value in enumerate(smsArray):
    #         if value['mobile'] and value['message_body']:
    #             return {'SMS Array format is not correct.'}
    #         data['']
    #     result = requests.post(
    #         self.url+self.send_sms,
    #         data=data

    #     )

    #     return result


# This Check Campaign Status

    def checkCampaign(self, campaignUid):
        '''
        Send the message to desired number
        :param campaignUid:
        :return: json
        '''
        result = requests.post(
            self.url+self.check_balance,
            data={
                'api_key': self.API_KEY,
                'api_secret': self.API_SECRET,
                'campaign_uid': campaignUid
            }
        )

        return result


# This Check SMS Status

    def checkSms(self, smsUid):
        '''
        Send the message to desired number
        :param smsUid:
        :return: json
        '''
        result = requests.post(
            self.url+self.check_balance,
            data={
                'api_key': self.API_KEY,
                'api_secret': self.API_SECRET,
                'sms_uid': smsUid
            }
        )

        return result
