def factorial(n):
	"""
	Calculate factorial of a number using recursion.
	
	Args:
		n (int): Non-negative integer
	
	Returns:
		int: Factorial of n
	"""
	# Base case
	if n == 0 or n == 1:
		return 1
	
	# Recursive case
	return n * factorial(n - 1)


def fibonacci(n):
	"""
	Calculate nth Fibonacci number using recursion.
	
	Args:
		n (int): Position in Fibonacci sequence
	
	Returns:
		int: nth Fibonacci number
	"""
	# Base cases
	if n <= 1:
		return n
	
	# Recursive case
	return fibonacci(n - 1) + fibonacci(n - 2)


# Example usage
if __name__ == "__main__":
	# Test factorial
	print(f"Factorial of 5: {factorial(5)}")
	print(f"Factorial of 0: {factorial(0)}")
	
	# Test fibonacci
	print(f"Fibonacci of 6: {fibonacci(6)}")
	print(f"Fibonacci of 10: {fibonacci(10)}")