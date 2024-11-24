# bmi_calc.py

def calculate_bmi(weight: float, height: float):
    bmi = weight / (height ** 2)

    if bmi <= 18.5:
        category = "Underweight"
    elif 18.6 <= bmi <= 24.9:
        category = "Normal"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    elif bmi >= 30:
        category = "Obese"
    else:
        category = "Unknown"

    return f"Your BMI is {bmi:.2f}, which is considered {category}."











# print("Welcome to the Nigster Calc!")
# print("(calc is short for calculator chat)")

# weight = float(input("whats your weight?: "))
# height = float(input("whats your height?: "))

# bmi = weight / (height ** 2)

# if bmi <= 18.5:
#     print("nigga you have no meat")
#     answer = str(input("translate from niggahood to normal language?: ").lower())
#     if answer == 'yes':
#         print("Underweight")
#     elif answer == 'no':
#         print("fuck u eat shit")
#     else:
#         print("nigga u stupid?")
# elif 18.6 <= bmi <= 24.9:
#     print("ahh nigga u got nice things on ya")
#     answer = str(input("translate from niggahood to normal language?: ").lower())
#     if answer == 'yes':
#         print("Normal")
#     elif answer == 'no':
#         print("fuck u eat shit")
#     else:
#         print("nigga u stupid?")
# elif 25 <= bmi <= 29.9:
#     print("dam u got sum meat on ya")
#     answer = str(input("translate from niggahood to normal language?: ").lower())
#     if answer == 'yes':
#         print("Overweight")
#     elif answer == 'no':
#         print("fuck u eat shit")
#     else:
#         print("nigga u stupid?")
# elif bmi >= 30:
#     print("DAYUM SHAWTY OBEASE")
#     answer = str(input("translate from niggahood to normal language?: ").lower())
#     if answer == 'yes':
#         print("Obease")
#     elif answer == 'no':
#         print("fuck u eat shit")
#     else:
#         print("nigga u stupid?")
# else:
#     print("Ah nigga don't hate me cause I'm beautiful nigga. Maybe if you got rid of that old yee yee ass haircut, you'd get some bitches on yo dick. Oh, better yet, maybe Tanisha'll call your dog ass if she stops fuckin' with that brain surgeon or lawyer she fucking with. Niiggaaa")
    