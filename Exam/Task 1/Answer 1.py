
def check_character(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


print(check_character('Order of the Phoenix', 'o'))