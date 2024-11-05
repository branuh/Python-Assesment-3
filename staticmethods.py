class Calculator:
    count = 0

    @staticmethod
    def add(num1, num2):
        Calculator.count += 1
        return num1 + num2

# Using the static method and checking the count
result = Calculator.add(5, 3)
print("Result:", result)
print("Number of additions:", Calculator.count)

result = Calculator.add(10, 20)
print("Result:", result)
print("Number of additions:", Calculator.count)