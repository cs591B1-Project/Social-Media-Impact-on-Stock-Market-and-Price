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
ap_trump = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ap_election = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#  array to track number of positive articles by day
an = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
an_social = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
an_trump = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
an_election = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


#  array to track number of positive articles by day
aa = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
aa_social = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
aa_trump = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
aa_election = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

negativeFileName = 'facebook_neg_'
postiveFileName = 'facebook_pos_'
neutralFileName = 'facebook_neu_'
numNegativ = 21
numPositive = 1
numNeutral = 3

# Negative News Articles from 1 to 9 JSON files
with open('facebook_neg_1.json') as json_data:
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



with open('facebook_neg_2.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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

with open('facebook_neg_3.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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


with open('facebook_neg_4.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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


with open('facebook_neg_5.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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


with open('facebook_neg_6.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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


with open('facebook_neg_7.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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


with open('facebook_neg_8.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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


with open('facebook_neg_9.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
with open('facebook_neutral_1.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact


with open('facebook_neutral_2.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact


with open('facebook_neutral_3.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact


with open('facebook_neutral_4.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact



with open('facebook_neutral_5.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact


with open('facebook_neutral_6.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact


with open('facebook_neutral_7.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact


with open('facebook_neutral_8.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact


with open('facebook_neutral_9.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact


with open('facebook_neutral_10.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact


with open('facebook_neutral_11.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact



with open('facebook_neutral_12.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact


with open('facebook_neutral_13.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact


with open('facebook_neutral_14.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact


with open('facebook_neutral_15.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact


with open('facebook_neutral_16.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact


with open('facebook_neutral_17.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact


with open('facebook_neutral_18.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	aa_social[d-day] += social_impact


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
with open('facebook_p_1.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	ap_social[d-day] += social_impact


# calculates number of positive articles per day, from the last 30 days
with open('facebook_p_2.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	ap_social[d-day] += social_impact


# calculates number of positive articles per day, from the last 30 days
with open('facebook_p_3.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	ap_social[d-day] += social_impact


# calculates number of positive articles per day, from the last 30 days
with open('facebook_p_4.json') as json_data:
    d = json.load(json_data)
    print d["posts"][0]["thread"]["social"]["facebook"]

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
	ap_social[d-day] += social_impact


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