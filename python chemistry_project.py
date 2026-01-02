
print("\nWelcome to Vedika's Chemistry Project")

def mass_converter():
    print("\n--- Mass Converter ---")
    print("1. Gram to Kilogram")
    print("2. Kilogram to Gram")

    choice = int(input("Enter choice: "))

    if choice == 1:
        gram = float(input("Enter grams: "))
        kg = gram / 1000
        print("Kilograms =", kg)
    elif choice == 2:
        kg = float(input("Enter kilograms: "))
        gram = kg * 1000
        print("Grams =", gram)
    else:
        print("Invalid choice")


def volume_converter():
    print("\n--- Volume Converter ---")
    print("1. Milliliter to Liter")
    print("2. Liter to Milliliter")

    choice = int(input("Enter choice: "))

    if choice == 1:
        ml = float(input("Enter milliliters: "))
        l = ml / 1000
        print("Liters =", l)
    elif choice == 2:
        l = float(input("Enter liters: "))
        ml = l * 1000
        print("Milliliters =", ml)
    else:
        print("Invalid choice")


def temperature_converter():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Enter choice: "))

    if choice == 1:
        c = float(input("Enter Celsius: "))
        f = (c * 9/5) + 32
        print("Fahrenheit =", f)
    elif choice == 2:
        f = float(input("Enter Fahrenheit: "))
        c = (f - 32) * 5/9
        print("Celsius =", c)
    else:
        print("Invalid choice")


def chemistry_quiz():
    print("\n--- Chemistry Quiz ---")
    score = 0

    print("\nQ1. What is the chemical formula of water?")
    print("a) H2O")
    print("b) CO2")
    print("c) O2")
    ans = input("Enter answer: ")

    if ans.lower() == 'a':
        score += 1

    print("\nQ2. pH value of acid is?")
    print("a) Greater than 7")
    print("b) Less than 7")
    print("c) Equal to 7")
    ans = input("Enter answer: ")

    if ans.lower() == 'b':
        score += 1

    print("\nQ3. Which gas is used in photosynthesis?")
    print("a) Oxygen")
    print("b) Nitrogen")
    print("c) Carbon Dioxide")
    ans = input("Enter answer: ")

    if ans.lower() == 'c':
        score += 1

    print("\nYour Score:", score, "/ 3")



while True:
    print("\n====== CHEMISTRY APP ======")
    print("1. Mass Converter")
    print("2. Volume Converter")
    print("3. Temperature Converter")
    print("4. Chemistry Quiz")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        mass_converter()
    elif choice == 2:
        volume_converter()
    elif choice == 3:
        temperature_converter()
    elif choice == 4:
        chemistry_quiz()
    elif choice == 5:
        print("Thank you for using Chemistry App!")
        break
    else:
        print("Invalid choice, try again")
