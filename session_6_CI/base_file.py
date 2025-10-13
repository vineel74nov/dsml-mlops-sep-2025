a = 5
b = 10


def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	if y == 0:
		return "Error! Division by zero."
	return x / y


print("This is the base file being executed, from base_file.py, outside the main block., __name__ =", __name__)


if __name__ == "__main__":
	print("This will only run when base_file.py is executed directly.")
	print(f"Addition of {a} and {b} is: {add(a, b)}")
	print(f"Subtraction of {a} and {b} is: {subtract(a, b)}")
	print(f"Multiplication of {a} and {b} is: {multiply(a, b)}")
	print(f"Division of {a} and {b} is: {divide(a, b)}")