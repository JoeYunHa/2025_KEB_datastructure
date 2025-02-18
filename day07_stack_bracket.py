def check_bracket(expr: str) -> bool:

    stack = list()
    table = {'(': ')', '[':']','{':'}','<':'>' }
    for char in expr:
        if char in table:
            stack.append(char)
        elif not stack or table[stack.pop()] != char:
            return False
        else:
            pass
    return len(stack) == 0

if __name__ == "__main__":
    expression = input("Input expression : ")
    print(check_bracket(expression))