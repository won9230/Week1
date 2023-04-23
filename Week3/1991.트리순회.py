import sys
n = int(sys.stdin.readline())
tree = {}
for i in range(n):
    root , left,right = sys.stdin.readline().split()
    tree[root] = [left,right]
    
print(tree)

def A(_root):
    if _root != '.':
        print(_root,end='')
        A(tree[_root][0])
        A(tree[_root][1])

def B(_root):
    if _root != '.':
        B(tree[_root][0])
        print(_root,end='')
        B(tree[_root][1])

def C(_root):
    if _root != '.':
        C(tree[_root][0])
        C(tree[_root][1])
        print(_root,end='')

A('A')
print()
B('A')
print()
C('A')














# import sys
# n = int(sys.stdin.readline())
# tree = {}

# for i in range(n):
#     root, left, right = sys.stdin.readline().rstrip().split()
#     tree[root] = [left,right]

# def A(root):
#     if root != '.':
#         print(root,end='')
#         A(tree[root][0])
#         A(tree[root][1])

# def B(root):
#     if root != '.':
#         B(tree[root][0])
#         print(root,end='')
#         B(tree[root][1])

# def C(root):
#     if root != '.':
#         C(tree[root][0])
#         C(tree[root][1])
#         print(root,end='')

# A('A')
# print()
# B('A')
# print()
# C('A')
