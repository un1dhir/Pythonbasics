#Get user input
weight = float(input("Enter your weight in Kgs: "))
height = float(input("Enter your height in metres:"))
#calculate BMI
bmi = calculate_bmi(weight, height)
#determine bmi category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= 24.9:
    category = "Normal weight"
elif 25 <= bmi <29.9:
    category = "Overweight"
else:
    category = "Obese"
print(f"your BMI is {bmi:.2f},which is {category}.")