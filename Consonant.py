def solve(word):
    # Initialize an empty list to store values
    consonant_values = []
    # Loop  the characters of the word
    for substring in word.split('aeiou'):
        # Initializing a list to store individual character values
        values = [ord(char) - ord('a') + 1 for char in substring]