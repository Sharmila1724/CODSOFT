value1 = int(input("Enter your first number = "))
operator = input("Enter the operator you want = ")
value2 = int(input("Enter your second number = "))
def final_key():
    def repeat(val, val1):
        if operator == "+":
            def add_numbers(a, b):
                sum = a + b
                return sum

            result = add_numbers(val, val1)
            print(result)

        elif operator == "-":
            def add_numbers(a, b):
                sum = a - b
                return sum

            result = add_numbers(val, val1)
            print(result)

        elif operator == "*":
            def add_numbers(a, b):
                sum = a * b
                return sum

            result = add_numbers(val, val1)
            print(result)

        elif operator == "%":
            def add_numbers(a, b):
                sum = a - b
                return sum

            result = add_numbers(val, val1)
            print(result)

    repeat(value1, value2)
final_key()

true = True
false = False
while true:
    continue_asking = input("Type 'Yes' if you would like to continue calculating or Type 'No' to exit  = ").title()
    if continue_asking == "No":
        print("Thank you for calculating.")
        break
    elif continue_asking == "Yes":
        value1 = int(input("Enter your first number = "))
        operator = input("Enter your operator you want = ")
        value2 = int(input("Enter your second number = "))
        final_key()