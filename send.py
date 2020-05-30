import requests, datetime, random

urlc = 'https://nairman.pythonanywhere.com'
urls = 'https://nairman.pythonanywhere.com/send'
client = requests.session()
client.get(urlc)
csrftoken = client.cookies['csrftoken']
dd = dict(tem=random.uniform(-100,100),dat=datetime.datetime.now(),sensfk=1,csrfmiddlewaretoken=csrftoken)
client.post(urls, data = dd)
