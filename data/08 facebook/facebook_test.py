import webhose;
import time;
from datetime import datetime, timedelta


webhose.config(token='c6052904-f312-436b-a6d8-d915084ac866')    # backup token

days_back = 30
date_days_ago = datetime.now() - timedelta(days=days_back)
day = datetime.today().day

topic = 'facebook'
lang = 'english'
country = 'US'

# positive stories
rp = webhose.search("organization.positive:\"" + topic + 
	"\" language:\"" + lang + 
	"\" thread.country:\"" + country + 
	"\" format:\"" + "json" + 
	"\" domain_rank:<100000", since=int(time.mktime(date_days_ago.timetuple())) )

# calculate total number of articles by day
for post in ra:
	p = post.published
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	aa[d-day] += 1
out0 = open('all.txt', 'w')
out0.truncate()
for i in aa:
	out0.write(str(i))
	out0.write("\n")
out0.close()


out2 = open('test.txt', 'w')
out2.truncate()
out2.write(str(rp))
out2.write("\n")
out2.close()


#eof