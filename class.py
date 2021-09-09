  
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



class Node1:
    def __init__(self):
        self.data = None
        self.next_data = None

l = Node1()  #empty list
l.data = 10   
l.next_data = 15    
print(l.data, l.next_data)   
