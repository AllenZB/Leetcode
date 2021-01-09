# # Python program to construct tree using inorder and preorder traversals

class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

pos_order=[1,2,3,4,5]
in_order=[1,2,5,3,4]
def constrct_tree(pos_order,in_order):
    if len(pos_order)==0:
        return None
    center=pos_order[-1]
    root=Node(center)
    index=0
    for i in range(len(in_order)):
        if in_order[i]==center:
            index=i
            break
    root.left=constrct_tree(pos_order[:index],in_order[:index])
    root.right=constrct_tree(pos_order[index:-1],in_order[index+1:])
    return root
root=constrct_tree(pos_order,in_order)

