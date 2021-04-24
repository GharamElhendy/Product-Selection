import sys
import keyboard
n = 7  # seven lists
l1 = []  # list -> List of lists
for i in range(1, n+1):
    list1 = input(f"Enter multiple values separated by commas{i}: ").lower().title().split(",")
    l1.append(list1)  # append list in list
print(f"list {l1}")
# get common between lists
common = []  # list of sets
for i in range(len(l1)):
    for j in range(i+1, len(l1)):
        commonelements = set(l1[i]) & set(l1[j])  # sets are used to avoid duplicates
        if len(commonelements) > 0:  # to avoid appending of empty sets
            print(f"common elements between list {i+1} and list {j+1}: ", commonelements)
            common.append(commonelements)
print(f"Common elements between all lists {common}")
while True:
    keyboard.wait("esc")
    sys.exit()