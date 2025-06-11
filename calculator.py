def calculate(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == 'add':
            return num1 + num2
        elif operation == 'subtract':
            return num1 - num2
        elif operation == 'multiply':
            return num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return "Cannot divide by zero!"
            return num1 / num2
        else:
            return "Invalid operation"
    except ValueError:
        return "Invalid input"
