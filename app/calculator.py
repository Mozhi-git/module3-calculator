from app.operations import Operations

class Calculator:
    @staticmethod
    def calculate(a: float, b: float, operation: str) -> float:
        if operation == "add":
            return Operations.addition(a, b)
        elif operation == "subtract":
            return Operations.subtraction(a, b)
        elif operation == "multiply":
            return Operations.multiplication(a, b)
        elif operation == "divide":
            return Operations.division(a, b)
        else:
            raise ValueError("Invalid operation.")