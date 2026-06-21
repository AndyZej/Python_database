import re
from exercise_2 import text_to_search
# 1. Find all occurrences of the word 'love'
# Using \b (word boundary) ensures we don't match 'lovely' or 'beloved'
love_occurrences = re.findall(r'\blove\b', text_to_search)
# 2. Find all occurrences that match the pattern <sure>%
# Assuming you mean the literal string '<sure>%'
sure_pattern = re.findall(r'<sure>%', text_to_search)
# 3. Find all occurrences of words that end with the character '?'
# This matches one or more word characters followed by a literal '?'
words_ending_question = re.findall(r'\w+\?', text_to_search)
# 4. Find all words containing 'fair' (case-insensitive)
# \w* ensures we capture the full word containing the string
fair_words = re.findall(r'\b\w*fair\w*\b', text_to_search, re.IGNORECASE)
# Example output for verification
print(f"Occurrences of 'love': {len(love_occurrences)}")
print(f"Words containing 'fair': {fair_words}")
