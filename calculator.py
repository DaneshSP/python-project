while True:
    try:
        choice = int(input("1: Add\n2: Subtract\n3: Multiply\n4: Division\n5: Exit\nEnter your choice: "))
        if choice == 1:
            A = int(input("Enter the first number: "))
            B = int(input("Enter the second number: "))
            print(f"{A} + {B} = {A + B}")
        elif choice == 2:
            A = int(input("Enter the first number: "))
            B = int(input("Enter the second number: "))
            print(f"{A} - {B} = {A - B}")
        elif choice == 3:
            A = int(input("Enter the first number: "))
            B = int(input("Enter the second number: "))
            print(f"{A} * {B} = {A * B}")
        elif choice == 4:
            try:
                A = int(input("Enter the first number: "))
                B = int(input("Enter the second number: "))
                print(f"{A} / {B} = {A / B}")
            except ZeroDivisionError:
                print("Division by zero is not allowed")
        elif choice == 5:
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Please enter a valid choice (1-5)")
    except ValueError:
        print("Please enter a valid number (1-5) for choice")