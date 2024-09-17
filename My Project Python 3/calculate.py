import numpy as np
print(" -- 1 = +, 2= -, 3 = *, 4 = /, -- ")
while True:
    Do = input("Do you want to do ?...")
    if Do == "1":
        number_plus = []
        n_plus = int(input("How many numbers do you want to add? "))
        for i in range(n_plus):
            plus = float(input("Enter number: "))
            number_plus.append(plus)
        total_plus = np.sum(number_plus)
        print("The total sum is:", total_plus)
    elif Do == "2":
        number_minus = []
        n_minus = int(input("How many numbers do you want to Minus? "))
        first_number = float(input("Enter first number: "))
        for i_minus in range(n_minus - 1):
            minus = float(input("Enter number: "))
            number_minus.append(minus)
        total_minus = first_number - np.sum(number_minus)
        print("The total Minus is:", total_minus)
    elif Do == "3":
        number_multiplication = []
        n_multiplication = int(input("How many numbers do you want to multiply? "))
        for i_multiplication in range(n_multiplication):
            multiplication = float(input("Enter number: "))
            number_multiplication.append(multiplication)
        total_multiplication = np.prod(number_multiplication)
        print("The total multiplication is:", total_multiplication)
    elif Do == "4":
        number_division = []
        n_division = int(input("How many numbers do you want to divide? "))
        first_number = float(input("Enter first number: "))
        for i_division in range(n_division - 1):
            division = float(input("Enter number: "))
            number_division.append(division)
        # Prevent division by zero and multiple divisions
        if len(number_division) > 0 and np.all(number_division):
            total_division = first_number
            for divisor in number_division:
                total_division /= divisor
            print("The total division is:", total_division)
        else:
            print("Error: Cannot divide by zero or perform multiple divisions.")
    elif Do == "5":
        break