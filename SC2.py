#Name: Echo Post
#Class: 5th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification
Height = int(input("Enter height in centimeters: "))
Weight = int(input("Enter weight in kilograms: "))
print(Height)
print(Weight)
BMI = (Weight/Height/Height) * 10000
print(BMI)
if BMI < 18.5:
    print("BMI is underweight")
elif BMI > 18.5 and BMI < 24.9:
    print("BMI is normal weight")
elif BMI > 24.9 and BMI < 29.9:
    print("BMI is overweight")
else:
    print("BMI is obese")

