//This script is to download pics from funnie.st site

import requests
from bs4 import BeautifulSoup
from progressbar import *

link=raw_input('Paste the link here: ')
res=requests.get(link)
data=BeautifulSoup(res.content)
Total_image=int(data.findChild('h3').string[-2:])

for pic in range(Total_image):
	res=requests.get(link)
	data=BeautifulSoup(res.content)
	next_image=data.findChildren('link')
	image_name=link[24:-3]+link[-2:-1]
	for img in next_image:
		if 'next' in img['rel']:
			link=img['href']
	image=data.findChildren('img')

	for i in image:
		if 'jpg' in i['src']:
			r=requests.get(i['src'])
			size=float(r.headers['content-length'])
			mbSize = 1024*1024	#used for conversion to Mb
			TotalSize = (size)/mbSize
			widgets = ['Test: ', Percentage(), ' ', Bar(">"), ' ', ETA(), ' ', FileTransferSpeed()]
			progress = ProgressBar(widgets=widgets,maxval=TotalSize)
			progress.start()

			count=0
			if r.status_code == 200:
			    try:
				    f=open(image_name+'.jpg', 'wb')
				    print "%s downloaded" % image_name
			    except Exception, e:
			        print "Error occured:", e
			        sys.exit(1)
		        for chunk in r.iter_content(256):
		            f.write(chunk)	
		            count=256
		            progress.update(count/mbSize)
          		f.close()
          		progress.finish()