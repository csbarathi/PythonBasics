from dataclasses import dataclass


class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def add(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.add(data)
         elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add(data)
      else:
         self.data = data
   def print(self):
      if self.left:
         self.left.print()
      print( self.data),
      if self.right:
         self.right.print()
   def printData(self):
       if(self.data!=None):
           return self.data
       else:
           return None
   def unorderedTraversal(self, root):
      res = []
      if root:
         print("Root:|"+str(root.data))
         res.append(root.data)
         print("1|"+str(res)+"|"+("Left node present" if (root.left is None) else "No left node" ))
         res = res + self.unorderedTraversal(root.left)
         print("2|"+str(res)+"|"+("Right node present" if (root.right is None) else "No right node" ))
         res = res + self.unorderedTraversal(root.right)
         print("3|"+str(res))
      else:
          print("None Root")
      return res
   def orderedTraversal(self, root):
      res = []
      if root:
         res.append(root.data)
         res = self.orderedTraversal(root.left)
         res = res + self.orderedTraversal(root.right)
      return res
sampleNode = Node(100)
sampleNode.add(50)
sampleNode.add(800)
sampleNode.add(2)
sampleNode.add(30)
sampleNode.print()
print("Unordered:"+str(sampleNode.unorderedTraversal(sampleNode)))
print("Ordered:"+str(sampleNode.orderedTraversal(sampleNode)))