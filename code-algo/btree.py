from random import *

class Node:
    def __init__(self, val): # constructor
        self.val = val
        self.left = None #initially no value 
        self.right = None
    
    def get(self): # get value
        return self.val 
    
    def set(self, val): #change value
        self.val = val
        
class Btree:  # define class
    def __init__(self): 
        self.root = None # no root reference 

    def setRoot(self, val):
        self.root = Node(val) # set root reference

    def insert(self, val): # insert a note
        if(self.root is None):
		    # if root not set , set value
            self.setRoot(val)
		 
        else:
            self.insertNode(self.root, val)

    def insertNode(self, curNode, val): 
        if(val <= curNode.val): #going left
            if(curNode.left): #securely find empty left 
                self.insertNode(curNode.left, val)
            else:
                curNode.left = Node(val) #found empty left
        elif(val > curNode.val): # going right
            if(curNode.right):
			    #securely find right or left
                self.insertNode(curNode.right, val) 
            else:
                curNode.right = Node(val)
    
	#keep looking left and then right
    def find(self, val):
        return self.findNode(self.root, val)

    def findNode(self, curNode, val):
        if(curNode is None):
            return None
        elif(val == curNode.val):
            return curNode
        elif(val < curNode.val):
            return self.findNode(curNode.left, val)
        else:
            return self.findNode(curNode.right, val)
    
    def display(self):
        self.displayInorder(self.root)
        
    def displayInorder(self,node):
        if (node.left):
            self.displayInorder(node.left)
        print(node.val)
        if (node.right):
            self.displayInorder(node.right)

myTree=Btree()
for i in range  (4):
  n=randint(1, 100)
  print(n)
  myTree.insert(n )
print("-------")
myTree.display()
print("-------")
myTree.insert(22 )
myNode=myTree.find(22)
if (myNode !=None):
  print(myNode.val)
