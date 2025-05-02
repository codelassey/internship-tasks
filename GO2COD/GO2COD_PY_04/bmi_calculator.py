# First, I need to collect the user's height (in meters) and weight (in kilograms).
# I'll use the input() function to get the values from the user.

# Asking for height and converting it to a float (since height can have decimals).
height = float(input("Enter your height in meters: "))

# Asking for weight and converting it to a float (since weight can have decimals too).
weight = float(input("Enter your weight in kilograms: "))

# Now I calculate the BMI using the formula: BMI = weight / (height ** 2)
# I'm using '**' to square the height.
bmi = weight / (height ** 2)

# Printing the calculated BMI to show the user.
print(f"Your BMI is: {bmi:.2f}")  # I use :.2f to limit the result to 2 decimal places.

# Next, I'll categorize the BMI based on the standard ranges.
# I'm using conditional statements (if, elif, else) to do this.

if bmi < 18.5:
    # If BMI is less than 18.5, the person is underweight.
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    # If BMI is between 18.5 and 24.9, the person has a normal weight.
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    # If BMI is between 25 and 29.9, the person is overweight.
    category = "Overweight"
else:
    # If BMI is 30 or more, the person is obese.
    category = "Obese"

# Finally, I display the category to the user.
print(f"Based on your BMI, you are categorized as: {category}")
