word = input().lower()
word_len = len(word)

result = 0

for char in word:
    letter = char
    if letter == 'a':
        result += 1
    elif letter == 'e':
        result += 2
    elif letter == 'i':
        result += 3
    elif letter == 'o':
        result += 4
    elif letter == 'u':
        result += 5
print(result)
