words = ['apple', 'bat', 'atom', 'book']
by_letters = {}

for word in words:
    letter = word[0]
    if letter not in by_letters:
        by_letters[letter] = [word]
    else:
        by_letters[letter].append(word)

print(by_letters)
print(by_letters['c']) # KeyError!
