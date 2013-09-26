# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


import math

# This is a very naive and brute-force method.
# First, I brute-force all factors of the square root of the number
# Then, I use the Sieve of Eratosthenes to generate primes up to the largest factor.
# Finally, I test to see if the factor is within the Sieved prime numbers, and take the max.
# TODO: Use Miller-Rabin Test and Pollard's Rho to increase performance.

def esieve(max_number):
	witness = {}
	q = 2
	while q <= max_number:
		if q not in witness:
			yield q
			witness[q*q] = [q]
		else:
			for prime in witness[q]:
				witness.setdefault(prime+q, []).append(prime)
			del witness[q]
		q += 1

if __name__ == '__main__':
	test_number = 600851475143
	sqrt_number = math.sqrt(test_number)
	factor_list = []

	x = 2
	while x < sqrt_number:
		if test_number%x == 0: factor_list.append(x)
		x += 1

	factor_list = [x for x in factor_list if x in esieve(max(factor_list))]
	print max(factor_list)