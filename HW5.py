#Name: Echo Post
#Class: 5th Hour
#Assignment: HW5

#1. Print Hello World!
print("Hello World!")
#1. Create a list with 5 strings containing 5 different names in it.
one_list = ["Storm", "Hope", "Ghost", "Franklin", "Luta"]
#2. Append a new name onto the Name List.
one_list.append(input("Insert your name: "))
print(one_list)
#3. Print out the 4th name on the list.
print(one_list[3])
#4. Create a list with 4 different integers in it.
int_list = [15, 18, 20, 23]
#5. Insert a new integer into the 2nd spot and print the new list.
int_list.insert(1, 16)
print(int_list)
#6. Sort the list from lowest to highest and print the sorted list.
int_list.sort()
print(int_list)
#7. Add the 1st three numbers on the sorted list together and print the sum.
int_list_subsum = int_list[0] + int_list[1] + int_list[2]
print(int_list_subsum)
#8. Create a list with two strings, two integers, and two boolean values.
two_str_int_bool_list = ["moon", "sun", 100, 200, True, True]
print(two_str_int_bool_list)
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(two_str_int_bool_list[int(input("Insert Index Value to list: "))])