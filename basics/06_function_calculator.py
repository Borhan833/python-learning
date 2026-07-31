# Calculator
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
while True:
    print("-"*6,"Calculator Menu","-"*6)
    print("1.Add")
    print("2. Subtract")
    print("3.multiply")
    print("4.divide")
    print("5.Exit")
    try:
        user_choice = int(input("Choose an option: "))
        first_number=int(input("First number: "))
        second_number=int(input("Second number: "))
    except ValueError:
        print("Invalid option!2")
        continue

    if user_choice == 1 :
        print(add(first_number, second_number))
    elif user_choice == 2 :
        print(subtract(first_number, second_number))
    elif user_choice == 3 :
        print(multiply(first_number, second_number))
    elif user_choice == 4 :
        try:
            print(divide(first_number, second_number))
        except ZeroDivisionError:
            print("Second number can not be 0!")
    elif user_choice == 5 :
        print("Good Bye.")
        break
    else:
        print("Invalid option!!")
