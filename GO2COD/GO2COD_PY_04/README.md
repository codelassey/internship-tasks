# Body Mass Index Calculator

This is a simple Python project created as part of an internship program. The BMI (Body Mass Index) Calculator takes the user's height and weight as input, calculates their BMI, and categorizes the result based on standard health ranges.

## Features
- Accepts user input for height (in meters) and weight (in kilograms).
- Calculates BMI using the formula:
  \[
  BMI = (weight(kg)) / (height(m)^2)

- Categorizes the BMI result into four groups:
  - Underweight
  - Normal weight
  - Overweight
  - Obese
- Displays the BMI value and its corresponding category.

## Technologies Used
- Python 3.x

## How to Use
1. Ensure Python 3.x is installed on your computer.
2. Download or copy the bmi_calculator.py file.
3. Run the program in your terminal or preferred Python IDE.
4. Follow the prompts to enter your height and weight.
5. View your BMI and its category.

## BMI Categories
| Category        | BMI Range       |
|------------------|-----------------|
| Underweight     | Less than 18.5  |
| Normal weight   | 18.5 to 24.9    |
| Overweight      | 25 to 29.9      |
| Obese           | 30 or greater   |

## Example Output
When the program is run, it looks like this:

```plaintext
Enter your height in meters: 1.70
Enter your weight in kilograms: 65
Your BMI is: 22.49
Based on your BMI, you are categorized as: Normal weight
