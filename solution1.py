# Problem 1 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 
# 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

if __name__ == "__main__":
	# This is a functional programming style solution. I use a left fold without an initial value, using an anonymous function that adds each element in a lazily generated list of integers from 1 to 1000.
	three_or_five = lambda: reduce(lambda x, y: x+y, [x if x%3==0 or x%5==0 else 0 for x in xrange(1, 1000)])
	
	print three_or_five() # Prints 233168
