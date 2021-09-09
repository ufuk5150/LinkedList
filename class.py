  
class Node:
    data = None
    
    def __init__(self, a1,a2):
        number1 = a1
        number2 = a2
        self.number3 = number1 + number2
    def printer(self):
        return self.number3
    
lengths = Node(10,20)

output = lengths.printer()
lengths.data = 50
print(lengths.data)
print(output)
