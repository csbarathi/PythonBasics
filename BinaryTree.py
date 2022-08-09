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
   def preOrderTraversal(self, root):
      res = []
      if root:
         print("Root:|"+str(root.data))
         res.append(root.data)
         print("1|"+str(res)+"|"+("No left node" if (root.left is None) else "Left node present" ))
         res = res + self.preOrderTraversal(root.left)
         print("2|"+str(res)+"|"+("No right node" if (root.right is None) else "Right node present" ))
         res = res + self.preOrderTraversal(root.right)
         print("3|"+str(res))
      else:
          print("None Root")
      return res
   def postOrderTraversal(self, root):
      res = []
      if root:
         res = self.postOrderTraversal(root.left)
         res = res + self.postOrderTraversal(root.right)
         res.append(root.data)
      return res
   def inOrderTraversal(self, root):
      res = []
      if root:
         res = self.inOrderTraversal(root.left)
         res.append(root.data)
         res = res + self.inOrderTraversal(root.right)
      return res
sampleNode = Node(100)
sampleNode.add(50)
sampleNode.add(800)
sampleNode.add(2)
sampleNode.add(30)
sampleNode.print()
print("Pre Order:"+str(sampleNode.preOrderTraversal(sampleNode)))
print("In Order:"+str(sampleNode.inOrderTraversal(sampleNode)))
print("Post Order:"+str(sampleNode.postOrderTraversal(sampleNode)))
