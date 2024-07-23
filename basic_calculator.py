def calculate(num1, operation, num2):
    if operation == "/" and num2 == 0:
        return None
    
    
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return None
    
    
#def calculate(num1, operation, num2):
#    try:
#        return eval(f'{num1}{operation}{num2}')
#    except Exception:
#        return