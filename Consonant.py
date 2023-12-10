def solve(word):
    # Initialize an empty list to store values
    consonant_values = []
    # Loop  the characters of the word
    for substring in word.split('aeiou'):
        # Initializing a list to store individual character values
        values = [ord(char) - ord('a') + 1 for char in substring]
        # Add the sum of values to the list
        consonant_values.append(sum(values))
        # Find the highest value in the list and return it
    return max(consonant_values)
#Expected output 26
result1 = solve("zodiacs")  
# Display the results
print("Result 1:", result1)