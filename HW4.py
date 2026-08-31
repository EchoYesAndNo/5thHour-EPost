#Name: Echo Post
#Class: 5th Hour
#Assignment: HW4

#1. Print "Hello World!"
print("Hello World")
#2. import the 'math' library
import math

#3. Create two variables, x and y, that asks the user for a decimal (float) for x and an integer for y.
x = float(input("Give me a decimal:"))
y = int(input("Give me a number:"))

#4. Create a variable with the value that is x and y added together.
int_sum = x + y

#5. Print the variable from #4.
print(int_sum)

#6. Create a variable with the value that is x and y added together, then divide the sum by 3.
divide_by_3 = (x + y) / 3

#7. Print the variable from #6.
print(divide_by_3)

#8. Create a variable with the value of the square root of y, then print the result.
square = (math.sqrt(y))
print(square)

#9. Use the round function to round x to the nearest tenths place (EX: 1.17 rounds to 1.1). Print the result.
round_tenth = (round(x,1))
print(round_tenth)

#10. Use the ceiling function to round x up to the nearest whole number. Print the result.
round_up = (math.ceil(x))
print(round_up)

#11. Use the floor function to round x down to the nearest whole number. Print the result.
round_down = (math.floor(x))
print(round_down)
