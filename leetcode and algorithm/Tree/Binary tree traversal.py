class ListNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
ans=[]
def pre_order_recursion(root):  #recurrsion
    if not root:
        return
    ans.append(root.val)
    pre_order_recursion(root.left)
    pre_order_recursion(root.right)
def pre_order_iterative(r):  #iterative
    if not r:
        return
    stack=[]
    stack.append(r)
    while len(stack)>0:
        top=stack.pop()
        ans.append(top)
        if top.right:
            stack.append(top.right)
        if top.left:
            stack.append(top.left)
    return ans
def in_order_recursion(root):
    if not root:
        return
    in_order_recursion(root.left)
    ans.append(root.val)
    in_order_recursion(root.right)
def in_order_iterative(root):
    if not root:
        return
    stack=[]
    current=root
    while True:
        if current:
            stack.append(current)
            current=current.left
        elif(stack):
            top=stack.pop()
            ans.append(top.val)
            current=current.right
        else:
            break
    return ans
def post_order_recursion(root):
    if not root:
        return
    post_order_recursion(root.left)
    post_order_recursion(root.right)
    ans.append(root.val)
    return ans
def post_order_iterative(root):
    if not root:
        return
    stack=[]
    stack.append(root)
    while stack:
        current=stack.pop()
        ans.append(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    a=[]
    for i in reversed(ans):
        a.append(i)
    return reversed(a)