#Name: Echo Post
#Class: 5th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
num_list = [111, 222, 333, 444, 555, 666, 777, 888, 999]
print(num_list)
#2. Sort the list from highest to lowest.
num_list.sort(reverse=True)
print(num_list)
#3. Create an empty list.
empty_list = []
#4. Remove the median number from the first list and add it to the second list.
med = num_list.pop(4)
empty_list.append(med)
#5. Remove the first number from the first list and add it to the second list.
first = num_list.pop(0)
empty_list.append(first)
print(empty_list)
#6. Print both lists.
print(num_list)
print(empty_list)
#7. Add the two numbers in the second list together and print the result.
empty_list_subsum = empty_list[0] + empty_list[1]
print(empty_list_subsum)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
num_list.append(empty_list_subsum)
#9. Sort the first list from lowest to highest and print it.
num_list.sort()
print(num_list)