#  https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem?isFullScreen=true

class MyQueue(object):
    def __init__(self):
            self.items=[]
    
    def peek(self):
        i = self.items.pop()
        self.items.append(i)
        return i
        
    def pop(self):
        return self.items.pop()
        
    def put(self, value):
        self.items.insert(0, value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
