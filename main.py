import requests, time

# both 'x-test' and 'x-test2' are sent
headers = {'Content-Type': 'application/vnd.alertme.zoo-6.1+json', 'Accept': 'application/vnd.alertme.zoo-6.1+json',
           'X-Omnia-Client': 'Hive Web Dashboard'
           }
url = 'https://api-prod.bgchprod.info:443/omnia'


def login():
    data = '''{
    "sessions": [{
    "username": "@gmail.com",
    "password": "",
    "caller": "WEB"
    }]
    }'''
    response = requests.post(url + "/auth/sessions", data=data, headers=headers)
    sessionId = response.json()['sessions'][0]['sessionId']
    headers['X-Omnia-Access-Token'] = sessionId


def light_control(node_id='c5abfc1e-7fd3-4682-a118-25c6c8f99c25', state='ON', level='1.0'):
    data = '''{
    "nodes":[{
    "attributes":{
    "state":{"targetValue":"'''+state+'''"},
    "brightness":{"targetValue":'''+level+'''}
    }
    }]
    }'''
    command_url = url + '/nodes/' + node_id
    response = requests.put(command_url, data=data, headers=headers)
    print(level)


def get_devices():
    response = requests.get(url + "/nodes", headers=headers)
    print(response.json())


login()
get_devices()
for i in range(1,101):
    light_control(level=str(float(i)))
    time.sleep(1)
