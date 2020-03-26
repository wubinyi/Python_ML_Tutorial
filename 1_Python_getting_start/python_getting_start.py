import numpy as np
# ==============================================================================
#                               Data Type
# ==============================================================================
# declare an integer number
integer_number = 10
# use type() function to get data type
data_type = type(integer_number)
print("integer_number {} has data type: {}".format(integer_number, data_type))

# declare a floating number
float_number = 10.0
data_type = type(float_number)
print("float_number {} has data type: {}".format(float_number, data_type))

# use float() function convert integer to float
number = float(integer_number)
print("number {} has data type: {}".format(number, type(number)))

# use int() function convert float to integer
number = int(float_number)
print("number {} has data type: {}".format(number, type(number)))

string = "hello!!!"
print("string {} has data type: {}".format(string, type(string)))


# ==============================================================================
#                               Operation
# ==============================================================================
print("")
operand_a = 10
operand_b = 100
sum = operand_a + operand_b
sub = operand_a - operand_b
mul = operand_a * operand_b
div = operand_a / operand_b
rest = operand_a % operand_b
print("sum {}, sub {}, mul {}, div {}, rest {}".format(sum, sub, mul, div, rest))


# ==============================================================================
#                               Program control flow
# ==============================================================================
print("")
if sub > 0:
    print("operand_a is larger than operand_b")
else:
    print("operand_a is smaller than operand_b")

# sum over from "1" to "sum"
sum_sum = 0
for i in range(sum):
    sum_sum += (i + 1)
print("sum over from {} to {} to get {}".format(1, sum, sum_sum))


# ==============================================================================
#                               Function definition
# ==============================================================================
def add(operand_a, operand_b):
    return operand_a + operand_b

print("adding 1.0 to 2.0 equals {}".format(add(1.0, 2.0)))


# ==============================================================================
#                               Begin to code
# task: write a function to realize matrix multiplication C = A * B
# A reference result "matrix_C_ref" is generated for comparison.
# ==============================================================================
print("")
matrix_A_width = 10
matrix_A_height = 16
matrix_B_width = 12
matrix_B_height = matrix_A_width
matrix_A = np.random.randint(low=-100, high=100, size=[matrix_A_height, matrix_A_width])
matrix_B = np.random.randint(low=-100, high=100, size=[matrix_B_height, matrix_B_width])
matrix_C_ref = np.matmul(matrix_A, matrix_B)
# how to get the shape of the data
matrix_C_shape = matrix_C_ref.shape
print("matrix_C_ref shape: {}".format(matrix_C_shape))

def my_matmul(A, B):
    matrix_C = np.zeros([matrix_A_height, matrix_B_width])
    # begin your code here, realizing your own function
    return matrix_C

is_equal = np.array_equal(my_matmul(matrix_A, matrix_B), matrix_C_ref)
print("Does matrix_C equal to matrix_C_ref: {}".format(is_equal))
print("-" * 60)
if not is_equal:
    print("\tYour implementation is not correct!!! Try again!!!")
else:
    print("\tGreat!!! You pass this test.")
print("-" * 60)