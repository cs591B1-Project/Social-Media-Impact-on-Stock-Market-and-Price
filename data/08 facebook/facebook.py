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
	"\" domain_rank:<100000", since=int(time.mktime(date_days_ago.timetuple())) )

# negative stories
rn = webhose.search("organization.negative:\"" + topic +
	"\" language:\"" + lang +
	"\" thread.country:\"" + country +
	"\" domain_rank:<100000", since=int(time.mktime(date_days_ago.timetuple())) )

# all stories
ra = webhose.search("organization:\"" + topic +
	"\" language:\"" + lang +
	"\" thread.country:\"" + country +
	"\" domain_rank:<100000", since=int(time.mktime(date_days_ago.timetuple())) )

print "Gathering Data"
#  array to track number of positive articles by day
ap = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#  array to track number of positive articles by day
an = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#  array to track number of positive articles by day
aa = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

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

# calculates number of positive articles per day, from the last 30 days
for post in rp:
	p = post.published
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	ap[d-day] += 1
out1 = open('positive.txt', 'w')
out1.truncate()
for i in ap:
	out1.write(str(i))
	out1.write("\n")
out1.close()

# calculate number of negative articles
for post in rn:
	p = post.published
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	an[d-day] += 1
out2 = open('negative.txt', 'w')
out2.truncate()
for i in an:
	out2.write(str(i))
	out2.write("\n")
out2.close()


#eof