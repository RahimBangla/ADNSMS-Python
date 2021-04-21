from ADNSMS import ADNSMS


# api_key, api_secret provided by ADNSMS
ADNSMS = ADNSMS('api_key', 'api_secret')
# You can change the api url if needed. i.e.
# ADNSMS.url = 'new_url'
result = ADNSMS.send('123456789', 'This is a test message.')

print(result)
