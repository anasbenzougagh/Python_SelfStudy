import numbers


def concat(a: str, b, c='', d='', e=''):
    print(f'{a} {b} {c} {d} {e}'.strip())

def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:
    return n1 + n2 + n3 + n4

def calculate(num1: numbers, operator: str, num2: numbers) -> numbers:
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print("Invalid Operator")
        return 0