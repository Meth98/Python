# Script to learn the splicing functionality ([start_intex:last_index:step])

# String splicing
string = "Hello World! My name is Pippo"

print("\n\033[91mThe string is\033[0m:", string, "\n")

print("\033[92mSTRING SPLICING\033[0m:\n")
print("\t\033[91m12th letter\033[0m:", string[11])
print("\t\033[91mLast letter\033[0m:", string[-1])
print("\t\033[91m5th-to-last letter\033[0m:", string[-5])
print("\t\033[91m1st to 7th letter\033[0m:", string[0:7])
print("\t\033[91mFrom the 5th letter onward\033[0m:", string[4:])
print("\t\033[91mEntire string (first way)\033[0m:", string[:])
print("\t\033[91mFrom the 5th-to-last letter to the beginning\033[0m:", string[:-5])
print("\t\033[91mFrom the beginning to the 8th letter\033[0m:", string[:8])
print("\t\033[91mFrom the 3th to 5th-to-last letter\033[0m:", string[2:-5])
print("\t\033[91mFrom the second-to-last to 5th-to-last letter\033[0m:", string[-5:-1])
print("\t\033[91mEntire string (second way)\033[0m:", string[::1])
print("\t\033[91mFrom the second to 9th letter with step 3\033[0m:", string[1:9:3])
print("\t\033[91mEntire string starting from the end (with step -1)\033[0m:", string[::-1])

print("\n-----------------------------------------------------")

# List splicing
my_list = [2, "Hello", 4, "World", 456, "My name is", [2, 3, 7, 2456], "Pippo"]

print("\n\033[91mThe list is\033[0m:", my_list, "\n")

print("\033[92mLIST SPLICING\033[0m:\n")
print("\t\033[91m7th item\033[0m:", my_list[6])
print("\t\033[91mLast item\033[0m:", my_list[-1])
print("\t\033[91m3th-to-last item\033[0m:", my_list[-3])
print("\t\033[91m1st to 3th item\033[0m:", my_list[0:3])
print("\t\033[91mFrom the 5th item onward\033[0m:", my_list[4:])
print("\t\033[91mEntire list (first way)\033[0m:", my_list[:])
print("\t\033[91mFrom the 2th-to-last item to the beginning\033[0m:", my_list[:-2])
print("\t\033[91mFrom the beginning to the 4th item\033[0m:", my_list[:4])
print("\t\033[91mFrom the 3th to 4th-to-last item\033[0m:", my_list[2:-4])
print("\t\033[91mFrom the second-to-last to 5th-to-last item\033[0m:", my_list[-5:-1])
print("\t\033[91mEntire list (second way)\033[0m:", my_list[::1])
print("\t\033[91mFrom the second to 8th item with step 2\033[0m:", my_list[1:8:2])
print("\t\033[91mEntire list starting from the end (with step -1)\033[0m:", my_list[::-1])
print()