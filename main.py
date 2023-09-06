import json
import email_template
from send_email import *
import http.client

dotenv.load_dotenv()
host = 'jooble.org'
key = os.getenv('API_KEY')

connection = http.client.HTTPConnection(host)
# request headers
headers = {"Content-type": "application/json"}
# json query
body = '{ "keywords": "it", "location": "Bern"}'
connection.request('POST', '/api/' + key, body, headers)
response = connection.getresponse()
data = json.loads(response.read().decode('utf-8'))
data['location'] = json.loads(body)['location']
filled_template = email_template.get_filled_template(
    './templates/jobs_summary.html',
    data=data
)

send_email(receiver=os.getenv('EMAIL_FROM'),
           subject="New job positions",
           details=filled_template)
