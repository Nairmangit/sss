import requests
import datetime

urlc = 'http://127.0.0.1:8000'
urls = 'http://127.0.0.1:8000/send'
client = requests.session()
client.get(urlc)
csrftoken = client.cookies['csrftoken']
dd = dict(tem=123,dat=datetime.datetime.now(),sensfk=1,csrfmiddlewaretoken=csrftoken)
client.post(urls, data = dd)
