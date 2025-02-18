def count_pattern_occurrences(text):
    count = 0  # Counter for matches
    words = text.split()  # Split the text into words

    for word in words:
        if word.startswith("C") and word.endswith("jeb"):
            count += 1  # Increment count if the word matches the pattern

    return count  # Return the total number of matches

# Example usage
sample_text = "ChelloJeb Csomethingjeb Canotherjeb Ctestjeb Cnotjeb C123jeb"
result = count_pattern_occurrences(sample_text)
print("Number of matches:", result)