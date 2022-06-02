ordinal_endings = {1: 'st', 2: 'nd', 3: 'rd'}

ordinals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for ordinal in ordinals:
    if ordinal in  ordinal_endings:
        print(f"{ordinal}{ordinal_endings[ordinal]}")
    else:
        print(f"{ordinal}th")
