name = "monty python"
print(name.title())
print(name.lower())
print(name.upper())

# Let's write an algorithm that accomplishes
space_flag = True
for letter in name:
    if space_flag == True:
        print(letter.upper())
    else:
        print(letter)
    if letter == "\n":
        space_flag = True
    else:
        space_flag = False
