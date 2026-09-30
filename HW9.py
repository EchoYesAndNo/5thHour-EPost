#Name:Echo Post
#Class: 5th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
favorite_holiday_dictionary = {
    "holiday" : "Halloween",
    "day" : [14, 25, 31],
    "color" : "Orange"
}
#3. Print the keys of the dictionary from #2.
print(favorite_holiday_dictionary)
#4. Print the values of the dictionary from #2
print(favorite_holiday_dictionary.values())
#5. Print one of the three numbers from the list by itself
print(favorite_holiday_dictionary["day"][2])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
favorite_holiday_dictionary.update({"mascot" : "Ghost"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(favorite_holiday_dictionary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
five_hour_class_dict = {
    "student_1" : {
        "Name" : "Neely",
        "Grade" : 12,
        "Sport" : True,
    },
    "student_2" : {
        "Name" : "Lila",
        "Grade" : 9,
        "Sport" : False,
    },
    "student_3" : {
        "Name" : "Adrian",
        "Grade" : 9,
        "Sport" : False,
    },
}

#9. Print the names of all three classmates on the same line.
print(five_hour_class_dict["student_1"]["Name"],five_hour_class_dict["student_2"]["Name"],five_hour_class_dict["student_3"]["Name"])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
five_hour_class_dict.pop("student_3")
print(five_hour_class_dict)