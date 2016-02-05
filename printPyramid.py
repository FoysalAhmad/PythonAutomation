#!usr/bin/env
n = 5
k = 15
#m = k-n+1
for i in range(n,0,-1):
	#m=1
	m = k-i+1
	for j in range(i):
	#	sum = k - n+ m
		print(m),
		k-=1
		m +=1	
	print('\n')

