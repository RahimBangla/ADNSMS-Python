#ADN SMS Api for Python / Django / Flask
A lightweight python API for adnsms message sending. Supports Python Project. While this pacakge can be used with Django/Flask, there is also a package specific to Django with more features, queue support that can be found here - [ADN SMS Python](https://github.com/rahimbangla/ADNSMS-Python)

## Requirements

- requests

## Usage

- Clone the repository
- Install the dependencies with `pip install -r requirements.txt`
- Import the class and create instance to access its functions.
  Or

---

- Install the package with `pip install ADNSMS`

## Example

A simple single sms send example.

```python
from ADNSMS import ADNSMS

    # api_key, api_secret provided by ADNSMS
    ADNSMS = ADNSMS('api_key', 'api_secret')
    # You can change the api url if needed. i.e.
    # ADNSMS.url = 'new_url'
    result = ADNSMS.send('123456789','This is a test message.')

    print(result)
```

## Output

Success output for above example.

```javascript
{
  "request_type": "single_sms",
  "campaign_uid": "CXXXXXXXXXXXXXXXX",
  "sms_uid": "SXXXXXXXXXXXXXXXX",
  "invalid_numbers": [],
  "api_response_code": 200,
  "api_response_message": "SUCCESS"
}
```

## More Info

You can find a full documentation with more details in `docs` folder.
