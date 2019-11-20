class Stack:
    def __init__(self):
        self.list=[]
    def push(self, val):
        self.list.append(val)
    def pop(self):
        return self.list.pop()
s1=Stack()
s1.push("apple")
s1.push("grapes")
a=s1.pop()
print(a)

