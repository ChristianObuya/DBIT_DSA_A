from collections import deque

# Using deque as a stack
stack = deque([10, 20, 30])
print(f"  Initial deque: {list(stack)}")

stack.append(100)
stack.append(200)
stack.append(300)

item = stack.pop()
print(f"  Popped from deque: {item}")
print(f"  After pop: {list(stack)}")

# Append (Right Side) – Stack
stack.append(40)
print(f"  After append(40): {list(stack)}")

# Append Left – Queue
stack.appendleft(5)
print(f"  After appendleft(5): {list(stack)}")

# Pop (Right Side)
right = stack.pop()
print(f"  Popped from right: {right}")
print(f"  After pop(): {list(stack)}")

# Pop (Left Side)
left = stack.popleft()
print(f"  Popped from left: {left}")
print(f"  After popleft(): {list(stack)}")


print(f"  Front item: {stack[0]}")
print(f"  Rear item: {stack[-1]}")


stack.clear()
print(f"  After clear(): {list(stack)}")



