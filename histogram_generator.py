# Script that it creates a histogram, made of asterisks, from the numbers in a list

listItem = []
condition = True
number = None

while condition == True:
    try:
        number = int(input("\nType an integer number to insert into a list (0 to stop the program): "))
    except Exception as e:
        print(f"\nWarning!! You have done something wrong (error: {e})!")

    if number == 0:
        condition = False
        break
    else:
        if number is not None:
            listItem.append(number)

print("\nThe list is: " + str(listItem) + "\n")

for i in listItem:
    print("*" * i)