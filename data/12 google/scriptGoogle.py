import json;
import time;
from datetime import datetime, timedelta
from parseJSON import getSocialData

days_back = 30
date_days_ago = datetime.now() - timedelta(days=days_back)
day = datetime.today().day
day = 5

#  array to track number of positive articles by day
ap = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ap_social = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#  array to track number of positive articles by day
an = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
an_social = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


#  array to track number of positive articles by day
aa = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
aa_social = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


# Negative News Articles from 1 to 9 JSON files
with open('google_neg_1.json') as json_data:
    d = json.load(json_data)

rn = d["posts"]

# go through all posts
for post in rn:
	p = post["published"]
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	an[d-day] += 1
	social_impact = getSocialData(post)
	an_social[d-day] += social_impact
	#text = post["text"]
	#text = text.encode('ascii','ignore')
	#foundindx = text.findall("Election") 
	#print "Relevant Words: " + str(foundindx)
	#print text

with open('google_neg_2.json') as json_data:
    d = json.load(json_data)

rn = d["posts"]

# go through all posts
for post in rn:
	p = post["published"]
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	an[d-day] += 1
	social_impact = getSocialData(post)
	an_social[d-day] += social_impact


with open('google_neg_3.json') as json_data:
    d = json.load(json_data)

rn = d["posts"]

# go through all posts
for post in rn:
	p = post["published"]
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	an[d-day] += 1
	social_impact = getSocialData(post)
	an_social[d-day] += social_impact


with open('google_neg_4.json') as json_data:
    d = json.load(json_data)

rn = d["posts"]

# go through all posts
for post in rn:
	p = post["published"]
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	an[d-day] += 1
	social_impact = getSocialData(post)
	an_social[d-day] += social_impact


with open('google_neg_5.json') as json_data:
    d = json.load(json_data)

rn = d["posts"]

# go through all posts
for post in rn:
	p = post["published"]
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	an[d-day] += 1
	social_impact = getSocialData(post)
	an_social[d-day] += social_impact


with open('google_neg_6.json') as json_data:
    d = json.load(json_data)

rn = d["posts"]

# go through all posts
for post in rn:
	p = post["published"]
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	an[d-day] += 1
	social_impact = getSocialData(post)
	an_social[d-day] += social_impact


with open('google_neg_7.json') as json_data:
    d = json.load(json_data)

rn = d["posts"]

# go through all posts
for post in rn:
	p = post["published"]
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	an[d-day] += 1
	social_impact = getSocialData(post)
	an_social[d-day] += social_impact


with open('google_neg_8.json') as json_data:
    d = json.load(json_data)

rn = d["posts"]

# go through all posts
for post in rn:
	p = post["published"]
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	an[d-day] += 1
	social_impact = getSocialData(post)
	an_social[d-day] += social_impact


with open('google_neg_9.json') as json_data:
    d = json.load(json_data)

rn = d["posts"]

# go through all posts
for post in rn:
	p = post["published"]
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	an[d-day] += 1
	social_impact = getSocialData(post)
	an_social[d-day] += social_impact


with open('google_neg_10.json') as json_data:
    d = json.load(json_data)

rn = d["posts"]

# go through all posts
for post in rn:
	p = post["published"]
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	an[d-day] += 1

with open('google_neg_11.json') as json_data:
    d = json.load(json_data)

rn = d["posts"]

# go through all posts
for post in rn:
	p = post["published"]
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	an[d-day] += 1
	social_impact = getSocialData(post)
	an_social[d-day] += social_impact


with open('google_neg_12.json') as json_data:
    d = json.load(json_data)

rn = d["posts"]

# go through all posts
for post in rn:
	p = post["published"]
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	an[d-day] += 1
	social_impact = getSocialData(post)
	an_social[d-day] += social_impact


out0 = open('negative.txt', 'w')
out0.truncate()

for i in an:
	out0.write(str(i))
	out0.write("\n")
out0.close()

out0 = open('negative_social.txt', 'w')
out0.truncate()

for i in an_social:
	out0.write(str(i))
	out0.write("\n")
out0.close()

# calculate total number of neutral articles by day
with open('google_neu_1.json') as json_data:
    d = json.load(json_data)

ra = d["posts"]

for post in ra:
	p = post["published"]
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	aa[d-day] += 1
	social_impact = getSocialData(post)
	an_social[d-day] += social_impact


with open('google_neu_2.json') as json_data:
    d = json.load(json_data)

ra = d["posts"]

for post in ra:
	p = post["published"]
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	aa[d-day] += 1
	social_impact = getSocialData(post)
	an_social[d-day] += social_impact



out0 = open('all.txt', 'w')
out0.truncate()
for i in aa:
	out0.write(str(i))
	out0.write("\n")
out0.close()

out0 = open('all_social.txt', 'w')
out0.truncate()
for i in aa_social:
	out0.write(str(i))
	out0.write("\n")
out0.close()

# calculates number of positive articles per day, from the last 30 days
with open('google_pos_1.json') as json_data:
    d = json.load(json_data)

rp = d["posts"]

for post in rp:
	p = post["published"]
	m = int(p[5:7])
	if m == 11:
		d = int(p[8:10])
	else:
		d = int(p[8:10])+30
	ap[d-day] += 1
	social_impact = getSocialData(post)
	an_social[d-day] += social_impact



out1 = open('positive.txt', 'w')
out1.truncate()
for i in ap:
	out1.write(str(i))
	out1.write("\n")
out1.close()


out1 = open('positive_social.txt', 'w')
out1.truncate()
for i in ap_social:
	out1.write(str(i))
	out1.write("\n")
out1.close()