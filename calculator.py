from operations import add, subtract, multiply


def main():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")
    if operation == '+':
        print("Result:", add(a, b))
    elif operation == '-':
        print("Result:", subtract(a, b))
    elif operation == '*':
        print("Result:", multiply(a, b))
    else:
        print("Operation not supported.")

if __name__ == "__main__":
    main()
