"""
Fibonacci Sequence - Enter a number and have the program
generate the Fibonacci sequence to that number or to the
Nth number.
"""

def fibo(n):
	"""
	Given a number n, return a fibonacci sequence with that many numbers
	:param n: enter a number and have a Fibonacci sequence of that many numbers
	:type n: int
	:return: Fibonacci sequence with n numbers
	:rtype: generator
	"""
	a = 0
	b = 1

	for i in range(n):
		yield a
		a,b = b,a+b

if __name__ == '__main__':
	while True:
		try:
			n = int(input("How many numbers do you want in your Fibonacci sequence? "))
		except:
			print("That's not a valid number! Please try again")
		else:
			break
	print(list(fibo(n)))
