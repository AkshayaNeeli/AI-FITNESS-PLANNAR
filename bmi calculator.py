# AI Health Diet & Fitness Planner

age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# BMI calculation
bmi = weight / (height * height)

print("\nYour BMI is:", round(bmi, 2))

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal Weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print("Category:", category)

# Calorie calculation
calories = 24 * weight

print("\nEstimated daily calories needed:", int(calories))
print("For weight loss:", int(calories - 300), "calories/day")
print("To maintain weight:", int(calories), "calories/day")
print("For weight gain:", int(calories + 300), "calories/day")

# Diet recommendation
print("\nRecommended Diet Plan:")

if category == "Underweight":
    print("Breakfast: Milk + Banana + Peanut butter sandwich")
    print("Lunch: Rice + Dal + Chicken/Fish + Vegetables")
    print("Dinner: Chapati + Paneer/Chicken + Salad")

elif category == "Normal Weight":
    print("Breakfast: Idli/Dosa + Sambar")
    print("Lunch: Rice + Dal + Vegetables + Curd")
    print("Dinner: Chapati + Vegetable curry + Salad")

elif category == "Overweight":
    print("Breakfast: Oats + Fruits")
    print("Lunch: Brown rice + Dal + Vegetables")
    print("Dinner: Grilled chicken/fish + Salad")

else:
    print("Breakfast: Oats + Green tea")
    print("Lunch: Vegetable salad + Dal soup")
    print("Dinner: Light vegetable soup")

# Workout recommendation
print("\nRecommended Workout Plan:")

if category == "Underweight":
    print("Light strength training")
    print("Push-ups and squats")
    print("30 minutes walking")

elif category == "Normal Weight":
    print("45 minutes walking or jogging")
    print("Yoga or stretching")
    print("Light strength exercises")

elif category == "Overweight":
    print("8000–10000 steps walking")
    print("Skipping or cycling")
    print("30 minutes cardio workout")

else:
    print("Daily walking 10000 steps")
    print("Low-impact exercises")
    print("Light yoga and stretching")