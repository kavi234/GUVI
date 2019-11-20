stack=[]
def push(a):
    stack.append(a)
def pop():
    return stack.pop()
push("apple")
push("orange")
push("banana")
print(stack)
print(pop())
print(stack)
print(pop())
print(stack)
print(pop())
print(stack)


