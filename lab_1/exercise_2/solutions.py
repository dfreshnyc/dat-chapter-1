from math import sqrt

even_total = 0

def fib(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

#<4,000,000 is the 32nd fib number
for n in range(0,31):	
	for x in range(0,n):
		if fib(x) % 2 == 0:
			even_total += fib(n)

print even_total

#x,y = 1, 1
#even_total = 0
#while x<= 4000000:
#	if x % 2 === 0;
#		even_sum += x
#	x, y = y, x + y
#print even_total
