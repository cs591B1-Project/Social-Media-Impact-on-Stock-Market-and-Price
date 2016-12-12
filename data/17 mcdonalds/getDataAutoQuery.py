import webhose;
import time;
from datetime import datetime, timedelta
from lxml import html
import requests
import unirest

webhose.config(token='c6052904-f312-436b-a6d8-d915084ac866')

days_back = 30
date_days_ago = datetime.now() - timedelta(days=days_back)

organization = 'mcdonald'
lang = 'english'
country = 'US'

#set API Token
apiToken = 'c6052904-f312-436b-a6d8-d915084ac866'

# Build URL
#queryURL = 'https://webhose.io/search?token=' + apiToken + '&format=json&q=' + sentiment + '%3A%22' + organization + '%22&ts=1478565932339'

### UPDATE YOUR END POINT HERE - Amazon Positive
response = unirest.get("https://webhose.io/search?token=c6052904-f312-436b-a6d8-d915084ac866&format=json&q=language%3A(english)%20thread.country%3AUS%20organization.positive%3A%22McDonald%22&ts=1478580441983",
    headers={
    "Accept": "text/plain"
    }
)

count = 1
results = response.body["totalResults"]
while results > 0:

	fileName = 'md_pos_' + str(count) + '.json'
	out0 = open(fileName, 'w')
	out0.truncate()
	out0.write(response.raw_body)
	out0.write("\n")
	out0.close()
	
	count = count + 1

	print response.body["next"]
	url = 'https://webhose.io' + response.body["next"]
	response = unirest.get(url,
	    headers={
	    "Accept": "text/plain"
	    }
	)
	results = response.body["totalResults"]


## UPDATE YOUR END POINT HERE - Amazon Neutral
response = unirest.get("https://webhose.io/search?token=c6052904-f312-436b-a6d8-d915084ac866&format=json&q=language%3A(english)%20thread.country%3AUS%20organization.neutral%3A%22McDonald%22&ts=1478580512041",
    headers={
    "Accept": "text/plain"
    }
)

count = 1
results = response.body["totalResults"]
while results > 0:

	fileName = 'md_neu_' + str(count) + '.json'
	out0 = open(fileName, 'w')
	out0.truncate()
	out0.write(response.raw_body)
	out0.write("\n")
	out0.close()
	
	count = count + 1

	print response.body["next"]
	url = 'https://webhose.io' + response.body["next"]
	response = unirest.get(url,
	    headers={
	    "Accept": "text/plain"
	    }
	)
	results = response.body["totalResults"]



## UPDATE YOUR END POINT HERE - Amazon Negative
response = unirest.get("https://webhose.io/search?token=c6052904-f312-436b-a6d8-d915084ac866&format=json&q=language%3A(english)%20thread.country%3AUS%20organization.negative%3A%22McDonald%22&ts=1478580524652",
    headers={
    "Accept": "text/plain"
    }
)

count = 1
results = response.body["totalResults"]
while results > 0:

	fileName = 'md_neg_' + str(count) + '.json'
	out0 = open(fileName, 'w')
	out0.truncate()
	out0.write(response.raw_body)
	out0.write("\n")
	out0.close()
	
	count = count + 1

	print response.body["next"]
	url = 'https://webhose.io' + response.body["next"]
	response = unirest.get(url,
	    headers={
	    "Accept": "text/plain"
	    }
	)
	results = response.body["totalResults"]



'''
postiveData = webhose.search("organization.positive:\"" + topic + 
	"\" language:\"" + lang + 
	"\" thread.country:\"" + country + 
	"\" domain_rank:<100000", since=int(time.mktime(date_days_ago.timetuple())) )


negativeData = webhose.search("organization.negative:\"" + topic + 
	"\" language:\"" + lang + 
	"\" thread.country:\"" + country + 
	"\" format:\"" + "json" + 
	"\" domain_rank:<100000", since=int(time.mktime(date_days_ago.timetuple())) )

neutralData = webhose.search("organization.negative:\"" + topic + 
	"\" language:\"" + lang + 
	"\" thread.country:\"" + country + 
	"\" domain_rank:<100000", since=int(time.mktime(date_days_ago.timetuple())) )

page = requests.get('https://webhose.io/search?token=c6052904-f312-436b-a6d8-d915084ac866&format=json&q=organization.positive%3A%22Microsoft%22&ts=1478565802902')
#print page
#print page.content
#print negativeData.next
#tree = html.fromstring(page.content)
'''
