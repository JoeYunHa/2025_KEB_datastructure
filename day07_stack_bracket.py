def check_bracket(expr: str) -> bool:

    stack = list()
    table = {')': '(', ']':'[','}':'{','>':'<' }
    for char in expr:
        if char in table.values():
            print(char)
            stack.append(char)
        elif char in table.keys():
            if not stack or table[char] != stack.pop():
                return False
    return len(stack) == 0

if __name__ == "__main__":
    expression = input("Input expression : ")
    print(check_bracket(expression))