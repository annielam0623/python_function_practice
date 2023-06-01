# Write a Python function called max_num()to find the maximum of three numbers.
l = [10, 20, 30]
max(l)

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):
    result = 1
    for num in numbers:
        result += num
    return result

#Write a Python function called rev_string() to reverse a string.
def reverse_string(s):
    return s [::-1]

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(number, start_range, end_range):
    return start_range <= number <= end_range

num = num_within(3, 2, 4)
    print(num)

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
def pasccal(n):
    triangle = []
    for i in range(n):
        row = [1]
        # i range(0, n-1) 
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
        triangle.append(row)
    for row in triangle:
        print(row)
pasccal(5)
