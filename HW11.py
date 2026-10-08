#Name: Echo Post
#Class: 5th Hour
#Assignment: HW11
import random

#1. Print "Hello World!"
print("Hello World")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
list_one = [random.randint(1,100),random.randint(1,100),random.randint(1,100)]
#3. Print the list.
print(list_one)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if list_one[0] > list_one[1] and list_one[0] > list_one[2]:
    print(f"{list_one[0]} is the highest")
    num = list_one[0]
elif list_one[1] > list_one[0] and list_one[1] > list_one[2]:
    print(f"{list_one[1]} is the highest")
    num = list_one[1]
else:
    print(f"{list_one[2]} is the highest")
    num = list_one[2]
#5. Tie the result (the largest number) from #4 to a variable called "num".

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    if num % 3 == 0:
        print("is divisible by 2 and 3")
    else:
        print("is divisible by 2")
else:
    if num % 3 == 0:
        print("is divisible by 3")
    else:
        print("is not divisible by 2 nor 3")