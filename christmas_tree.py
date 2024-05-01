# Script to understand the functionality of lists of lists

picture = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
]

for item in picture:
        for sub_item in item:
                if sub_item:    # equal to sub_item == 1
                        print("*", end="")      # to not go to the head
                else:
                        print(" ", end="")

        print()