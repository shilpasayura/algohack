#doubleTree
class Node :
	"""Node of a Tree"""
	def __init__(self) :
		self.data = None
		self.left = None
		self.right= None

def Build(head) :
	head.data = 2
	x = [1,3]
	new_left = Node()
	new_left.data = 1
	head.left = new_left
	new_right = Node()
	new_right.data = 3
	head.right = new_right
	return head

def printTree(head) :
	if head == None:
		return
	else :
		print ("Data : %d" % (head.data))
		printTree(head.left)
		printTree(head.right)

def NewNode(obj) :
	new = Node()	
	new.data = obj
	new.left = None
	new.right= None
	return new

def doubleTree(head) :	
	if head == None:
		return 
	else :
		temp = Node()
		doubleTree(head.left)
		doubleTree(head.right)
		temp = head.left
		head.left = NewNode(head.data)
		head.left.left = temp

head = Node()
head = Build(head)
print ("Present Tree ")
printTree(head)
doubleTree(head)
print ("After doubling ")
printTree(head)
