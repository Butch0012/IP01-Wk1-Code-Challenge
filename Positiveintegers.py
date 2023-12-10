def two_positive_numbers(a, b, c):
    # Count the number of positive numbers using a list comprehension
    positive_count = sum(x > 0 for x in [a, b, c])
 # Return True if exactly two numbers are positive, False otherwise
    return positive_count == 2
# Expected output:
print("Result 1:", two_positive_numbers(4, 8, -3)) #True