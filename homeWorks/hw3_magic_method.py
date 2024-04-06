class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        if other.value == 0:
            print('на ноль делить нельзя')
        else:
            return self.value / other.value

num1 = Calculator(20)
num2 = Calculator(30)
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)



