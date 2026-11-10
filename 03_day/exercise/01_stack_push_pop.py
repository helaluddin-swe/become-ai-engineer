class Stack:
  def __init__(self):
      self.values=[]
  def push(self,x):
      self.values=[x]+self.values

  def pop(self):
        return self.values.pop(0)
s=Stack()
s.push(40)
s.push(50)
s.push(60)
s.push(70)
s.push(80)

print(s.values)
print(s.pop())
s.push(90)
s.push(100)
print(s.values)