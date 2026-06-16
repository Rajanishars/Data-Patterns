class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(t1, t2):
    if not t1: return t2
    if not t2: return t1
    root = TreeNode(t1.val + t2.val)
    root.left = mergeTrees(t1.left, t2.left)
    root.right = mergeTrees(t1.right, t2.right)
    return root

def build_tree_from_input():
    val = input().strip()
    if val.lower() == 'none' or val == '':
        return None
    root = TreeNode(int(val))
    def add_children(node):
        left_val = input().strip()
        if left_val.lower() != 'none' and left_val != '':
            node.left = TreeNode(int(left_val))
            add_children(node.left)
        right_val = input().strip()
        if right_val.lower() != 'none' and right_val != '':
            node.right = TreeNode(int(right_val))
            add_children(node.right)
    add_children(root)
    return root

def print_inorder(node):
    if not node: return
    print_inorder(node.left)
    print(node.val, end=" ")
    print_inorder(node.right)

tree1 = build_tree_from_input()
tree2 = build_tree_from_input()
merged = mergeTrees(tree1, tree2)
print_inorder(merged)
print()
