def two_positive_numbers(a, b, c):
    # Count the number of positive numbers using a list comprehension
    positive_count = sum(x > 0 for x in [a, b, c])
