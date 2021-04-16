def divisors(a):
	divs = []
	i = 1
	while i <=a :
		if (a % i==0):
			divs.append(i)
		i = i+1
	print(divs)
	return divs

print("Divisors of number 12:")
divisors(12)
