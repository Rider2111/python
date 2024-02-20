def text_editor(operations):
    text_stack = []
    text = ""
    #
    for op in operations:
        command = op[0]
        
        if command == "1":  # Append
            text_stack.append(text)
            text += op[1]
        elif command == "2":  # Delete
            text_stack.append(text)
            k = int(op[1])
            text = text[:-k]
        elif command == "3":  # Print
            k = int(op[1])
            print(text[k - 1])
        elif command == "4":  # Undo
            text = text_stack.pop() if text_stack else ""

if __name__ == "__main__":
    n = int(input().strip())
    ops = []

    for _ in range(n):
        op = list(map(str, input().strip().split()))
        ops.append(op)

    text_editor(ops)