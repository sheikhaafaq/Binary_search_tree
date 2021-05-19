class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
        
    def insertnode(self,value):
        if self.data == None:
            self.data = value
        
        elif  value <= self.data:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insertnode(value)
            
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insertnode(value)
    
    def preOrder(self):
        if self.data != None:
            print(self.data)
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()
            
    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        if self.data != None:
            print(self.data)
            
    def inOrder(self):
        if self.left:
            self.left.inOrder()
        if self.data != None:
            print(self.data)
        if self.right:
            self.right.inOrder()
            
root = Node()
for x in [100 , 20 , 10 , 30 , 200 , 150 , 300]:
    root.insertnode(x)

print("PreOrder")
root.preOrder()
print("PostOrder")
root.postOrder()
print("InOrder")
root.inOrder()