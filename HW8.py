#Name: Echo Post
#Class: 5th Hour
#Assignment: HW8


#1. Import the "random" library
import random
#2. print "Hello World!"
print("Hello World")
#3. Create three different variables that each randomly generate an integer between 1 and 10
first_var = random.randint(1,10)
second_var = random.randint(1,10)
third_var = random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(first_var, second_var, third_var)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
first_sum = first_var + 2
second_sum = second_var - 4
third_sum = third_var * 1.5
#6. Print each result from #5 on the same line.
print(first_sum, second_sum, third_sum)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
one_through_four_list = [random.randint( 1, 6), random.randint( 1, 6), random.randint( 1, 6), random.randint( 1, 6)]
#8. Sort the list in #7 and print it.
one_through_four_list.sort()
print(one_through_four_list)
#9. Add together the highest three numbers in the list from #7 and print the result.
one_through_four_sum_of_high_three = one_through_four_list[1] + one_through_four_list[2] + one_through_four_list[3]
print(one_through_four_sum_of_high_three)
#10. Create a list with 5 names of other students in this class and print the list.
name_list = ["Neely", "Cruise", "Santi", "Anthony", "Adrian"]
print(name_list)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(name_list)
print(name_list)
#12. Print a random choice from the list of names from #10.
name_choice = random.choice(name_list)
print(name_choice)