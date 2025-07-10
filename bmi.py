def calculate_bmi(height , weight):
    bmi = weight / (height ** 2)
    return bmi 

def bmi_categories(bmi):
    if bmi < 18.5 :
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif bmi > 24.9 :
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculation")

    try:
        weight = float(input("Enter your weight in kilogram (kg) : "))
        height = float(input("Enter your height in meter (m) : "))

        bmi = calculate_bmi(height,weight)
        category = bmi_categories(bmi)

        print(f"\n Your BMI is : {bmi: .2f}")
        print(f" Category : {category}")

    except ValueError:
        print("Please Enter valid input.")

if __name__ == "__main__":
    main()
