stack = []
print(type(stack))

print(f" Stack: {stack}")

stack.append(10)
stack.append(20)
stack.append(30)
print(f" Stack after pushing: {stack}")


popped = stack.pop()
print(f" Popped item: {popped}")
print(f" Stack after pop: {stack}")


if stack:
    print(f" Top of stack: {stack[-1]}")
else:
    print(" Stack is empty, nothing to peek.")


print(f" Is stack empty? {len(stack) == 0}")