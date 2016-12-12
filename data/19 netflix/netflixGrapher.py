from ast import literal_eval
import matplotlib.pyplot as plt


p = [line.rstrip('\n') for line in open("positive.txt")]
n = [line.rstrip('\n') for line in open("negative.txt")]
a = [line.rstrip('\n') for line in open("all.txt")]

# stock closing prices from Nov 3 to Dec 3 (weedends/holidays given same price as previous closing)

s = [ 782.52002,
782.52002,
782.52002,
790.51001,
785.309998,
762.559998,
754.02002,
754.02002,
754.02002,
736.080017,
758.48999,
764.47998,
771.22998,
760.539978,
760.539978,
760.539978,
769.200012,
768.27002,
760.98999,
760.98999,
761.679993,
761.679993,
761.679993,
768.23999,
770.840027,
758.039978,
747.919983,
750.5,
750.5,
750.5]


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