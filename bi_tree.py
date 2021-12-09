from queue import Queue

class Node():
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None
# 建立一颗树, 层序方式表示
def build_tree_level(number):
    if len(number) == 0:
        return None
    assert number[0] is not None
    root = Node(number[0])
    q = Queue()
    q.put(root)
    i = 1
    while q.qsize() > 0:
        p = q.get()
        if i < len(number) and number[i] is not None:
            left = Node(number[i])
            p.left = left
            q.put(left)
        if i + 1 < len(number) and number[i + 1] is not None:
            right = Node(number[i + 1])
            p.right = right
            q.put(right)
        i += 2
    return root

# 先序遍历递归
def pre_visit_simple(root):
    if root is not None:
        print(root.v)
        pre_visit_simple(root.left)
        pre_visit_simple(root.right)
# 先序遍历非递归
def pre_visit_nocurve(root):
    if root is None:
        return
    s = [root]
    p = root
    while len(s) > 0 or p:
        if p:
            print(p.v)
            s.append(p)
            p = p.left
        else:
            s.pop()
            p = p.right
# 中序遍历递归
def mid_visit_simple(root):
    if root:
        mid_visit_simple(root.left)
        print(root.v)
        mid_visit_simple(root.right)
# 中序遍历非递归
def mid_visit_nocurve(root):
    if root:
        return
    s = []
    p = root
    while len(s) > 0 or p:
        if p:
            s.append(p)
            p = p.left
        else:
            p = s.pop()
            print(p.v)
            if p.right:
                p = p.right
            else:
                p = None

# 后序遍历递归
def post_visit_simple(root):
    if root is not None:
        post_visit_simple(root.left)
        post_visit_simple(root.right)
        print(root.v)

# 后序遍历非递归
def post_visit_nocurve(root):
    if root is None:
        return
    s = []
    p = root
    pre = None
    while len(s) > 0 or p:
        if p:
            s.append(p)
            p = p.left
        else:
            p = s.top()
            if p.right and p.right != pre:
                p = p.right
            else:
                pre = s.pop()
                print(pre.v)
                p = None
root = build_tree_level([0, 1, None, 2, 4])
pre_visit_simple(root)
pre_visit_nocurve(root)
mid_visit_simple(root)
post_visit_simple(root)
        


