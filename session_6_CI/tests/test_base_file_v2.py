from base_file import add, subtract, multiply, divide



#def test_first_test_of_this_lecture():
#	assert add(2, 3) == 5
#	assert add(-1, 1) == 0
#	assert add(0, 0) == 0

#	assert subtract(5, 3) == 2


#def test_second_test_of_this_lecture():
#	assert multiply(2, 3) == 6
#	assert multiply(-1, 1) == -1
#	assert multiply(0, 100) == 0

#	assert divide(6, 3) == 2
#	assert divide(5, 0) == "Error! Division by zero."


def test_add():
	assert add(2, 3) == 5, "Failed: 2 + 3 should equal 5"
	assert add(-1, 1) == 0, "Failed: -1 + 1 should equal 0"
	assert add(0, 0) == 0, "Failed: 0 + 0 should equal 0"
	assert add(-2, -3) == -5, "Failed: -2 + (-3) should equal -5"


def test_subtract():
	assert subtract(5, 3) == 2, "Failed: 5 - 3 should equal 2"
	assert subtract(0, 0) == 0, "Failed: 0 - 0 should equal 0"
	assert subtract(-1, -1) == 0, "Failed: -1 - (-1) should equal 0"

def test_multiply():
	assert multiply(2, 3) == 6, "Failed: 2 * 3 should equal 6"
	assert multiply(-1, 1) == -1, "Failed: -1 * 1 should equal -1"
	assert multiply(0, 100) == 0, "Failed: 0 * 100 should equal 0"
	assert multiply(-2, -3) == 6, "Failed: -2 * (-3) should equal 6"

def test_divide():
	assert divide(6, 3) == 2, "Failed: 6 / 3 should equal 2"
	assert divide(5, 0) == "Error! Division by zero.", "Failed: division by zero should return error message"
	assert divide(-6, -3) == 2, "Failed: -6 / (-3) should equal 2"
	assert divide(-6, 3) == -2, "Failed: -6 / 3 should equal -2"