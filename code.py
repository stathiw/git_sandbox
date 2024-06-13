# Description: This is a simple python code that performs basic arithmetic operations.

class Calculator:
    def __init__(self):
        value = 0

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def exponent(self, x, y):
        return x ** y

    def modulus(self, x, y):
        return x % y


if __name__ == '__main__':
    print("Hello World")

    calc = Calculator()
    
    print(calc.add(1, 2))       # Output: 3
    print(calc.subtract(1, 2))  # Output: -1
    print(calc.multiply(1, 2))  # Output: 2
    print(calc.divide(1, 2))    # Output: 0.5 (the current implementation is not correct)
    print(calc.exponent(2, 3))  # Output: 8
