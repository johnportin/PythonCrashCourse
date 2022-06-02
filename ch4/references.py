letters = ['a', 'b', 'c']

for letter in letters:
    letter = 'z'
    print(letter)

other_letters = letters

del(other_letters[-1])


print(letters)