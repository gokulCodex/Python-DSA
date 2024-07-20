#In a binary tree, all nodes to the left of a node are smaller
#All nodes to the right of a node are larger

#Binary Tree implementation:
class BinaryTree:

    #Constructor
    def __init__(self,val=None):
        self.value=val
        if self.value:
            self.left=BinaryTree()
            self.right=BinaryTree()
        else:
            self.left=None
            self.right=None
        return
    
    #Only empty node has value None
    def isempty(self):
        return self.value==None
    
    #Leaf node have both children empty
    def isleaf(self):
        return self.value!=None and self.left.isempty() and self.right.isempty()
    
    #Inorder traversal
    def inorder(self):
        if self.isempty():
            return []
        else:
            return self.left.inorder()+[self.vlue]+self.right.inorder()

    #Dispay Tree as a string
    def __str__(self):
        return str(self.inorder())   
    
    #Check if value v occurs in tree
    def find(self,val):
        if self.isempty():
            return False
        if self.value==val:
            return True
        if val<self.value:
            return self.left.find(val)
        if val>self.value:
            return self.right.find(val)
    
    #Find minimum value of the tree (Logic is to keep traveling to left till no left node exist)
    def minval(self):
        if self.left.isempty():
            return self.value
        else:
            return self.left.minval()
    
    #Find maximum value of the tree (Logic is to keep traveling to right till no right node exist)
    def maxval(self):
        if self.right.isempty():
            return self.value
        else:
            return self.right.maxval()
    
    #Insert a value to the tree
    def insert(self,val):
        if self.isempty():
            self.value=val
            self.left=BinaryTree()
            self.right=BinaryTree()
        if self.value==val:
            return
        if val<self.value:
            self.left.insert(val)
            return
        if val>self.value:
            self.right.insert(val)
            return
    
    #Convert leaf node to empty node
    def makeempty(self):
        self.value,self.left,self.right=None,None,None
        return
    
    #Promote left child
    def copyleft(self):
        self.value=self.left.value
        self.right=self.left.right
        self.left=self.left.left
        return
    
    #Promote rigt child
    def copyright(self):
        self.value=self.right.value
        self.left=self.right.left
        self.right=self.right.right
        return
    
    #Delete a value
    def delete(self,val):
        if self.isempty():
            return
        if val<self.value:
            self.left.delete(val)
            return
        if val>self.value:
            self.right.delete(val)
            return
        if val==self.value:
            if self.isleaf():
                self.makeempty()
            elif self.left.isempty():
                self.copyright()
            elif self.right.isempty():
                self.copyleft()
            else:
                self.value=self.left.maxval()
                self.left.delete(self.left.maxval())
            return