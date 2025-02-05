from calculator.opertions import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a: float, b: float) -> float:
        return add(a,b)

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return subtract(a,b)

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return multiply(a,b)

    @staticmethod
    def divide(a: float, b: float) -> float:
        return divide(a,b)

