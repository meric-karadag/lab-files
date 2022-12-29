class BinaryTreeNode:
	def __init__(self,data):
		self.data = data
		self.leftChild = None
		self.rightChild = None

node1 = BinaryTreeNode(50)
node2 = BinaryTreeNode(20)
node3 = BinaryTreeNode(45)
node4 = BinaryTreeNode(11)
node5 = BinaryTreeNode(15)
node6 = BinaryTreeNode(30)
node7 = BinaryTreeNode(78)

node1.leftChild = node2
node1.rightChild = node3
node2.leftChild = node4
node2.rightChild = node5
node3.leftChild = node6
node3.rightChild = node7


print("left child of the node is:")
print(node3.leftChild.data)


def datum(tree):
    return tree[0]
def left(tree):
    return tree[1]
def right(tree):
    return tree[2]
def isempty(tree):
    return tree == []
def isleaf(tree):
    return left(tree) == [] and right(tree) == []
def makenode(datum, left=[], right=[]):
    return [datum, left, right]

"""      1
       /   \
     10     20
    /   \     \
  11     12    21 
 /  \   /     /  \
4    5 6     7    8
            /    /
           56   65"""

my_tree = [1,[10,[11, [4],[5]],[12,[6],[]]],[20, [],[21,[7, [56],[]],[8, [65],[]]]]]
tree2 = [1, [2, [3, [], []], []], [5, [], [6, [], []]]]
def count_leaves(tree):
    if isempty(tree):
        return 0
    if isleaf(tree):
        return 1
    else:
        return count_leaves(left(tree)) + count_leaves(right(tree2))

#print(count_leaves(tree2))

def sum_tree(tree):
    if isempty(tree):
        return 0
    else:
    	return datum(tree) + sum_tree(left(tree)) + sum_tree(right(tree))

print(sum_tree(tree2))

def inorder(tree):
	if isempty(tree): return
	inorder(left(tree))
	print(datum(tree))
	inorder(right(tree))

print(inorder(tree2))