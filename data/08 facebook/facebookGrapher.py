from ast import literal_eval
import matplotlib.pyplot as plt


p = [line.rstrip('\n') for line in open("positive.txt")]
n = [line.rstrip('\n') for line in open("negative.txt")]
a = [line.rstrip('\n') for line in open("all.txt")]

# stock closing prices from Nov 3 to Dec 3 (weedends/holidays given same price as previous closing)
s = [ 51.77, 52.75, 52.75, 52.75, 
	54.490002, 54.619999, 54.580002, 53.57, 53.93, 53.93, 53.93, 
	54.220001, 54.59, 55.439999, 55.849998, 55.77, 55.77, 55.77, 
	56.099998, 57.119999, 57.59, 57.59, 57.43, 57.43, 57.43, 
	57.59, 58.169998, 57.970001, 58.509998, 57.21, 57.21 ]

s = [ 120.75, 120.75, 122.150002, 124.220001, 123.18, 
	120.800003, 119.019997, 119.019997, 119.019997, 115.080002,
	117.199997, 116.339996, 117.790001, 117.019997, 117.019997, 
	117.019997, 121.769997, 121.470001, 120.839996, 120.839996, 
	120.379997, 120.379997, 120.379997, 120.410004, 120.870003, 
	118.419998, 115.099998, 115.400002, 115.400002, 115.400002]

# create numeric list from p
plist = []
for line in p:
	plist.append(literal_eval(line))

# create numeric list from p
nlist = []
for line in n:
	nlist.append(literal_eval(line))

# create numeric list from p
alist = []
for line in a:
	alist.append(literal_eval(line))

# create plot
plt.plot(s, label='Closing stock prices', color='blue')
plt.plot(p, label='# positive articles', color='orange')
plt.plot(n, label='# negative articles', color='green')
plt.plot(a, label='Total articles', color='red')
plt.legend()
plt.show()

# close-up plot
plt.plot(s, label='Closing stock prices', color='blue')
plt.plot(p, label='# positive articles', color='orange')
plt.legend()
plt.show()

#eof