import os

'''
def main() -> None:
    # ...
    pass
'''

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def insert_into_tree(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_tree(root.left, value)
    else:
        root.right = insert_into_tree(root.right, value)
    return root

def main():
    input_filename = 'unsorted_nums.txt'
    output_filename = 'sorted_nums.txt'

'''
if __name__ == '__main__':
    main()
'''

