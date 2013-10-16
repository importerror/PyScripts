from bs4 import BeautifulSoup
import re
import requests
import json

TOKEN="CAACEdEose0cBAICZBZBVSznbEXsZBtlTwOVLem0tCw24kZB4sXZCCwtCc98jB6sFZCUZBVq82PqSTWvymLhpjupVEfZB5npyWoGZBnIG5Md9gcd23WeH0YaPkOPQi3bYUA7wmnxaFxoZAe1zVqWowWibme35GQCVCpRdJ1w6CHAvJivOM1SY9SpLqQ7gRGSAuLugNbH93dnfq9MQZDZD"
movie_data=requests.get('https://graph.facebook.com/100000305682125?fields=id,name,movies&access_token='+TOKEN)
result = json.loads(movie_data.text)

count=0
raw=[]
for i in result['movies']['data']:
	count+=1
	print count,i['name']
	raw.append(i['id'])

choice=input("Enter your choice: ")
choice-=1
link='https://www.facebook.com/plugins/fan.php?connections=100&id='+str(raw[choice])

data=requests.get(link)
soup=BeautifulSoup(data.content)
for i in soup.find_all('a',href=re.compile('https://www\.facebook\.com/')):
	try:
		print unicode(i['title'])
	except KeyError:
		continue
	except UnicodeEncodeError:
		continue