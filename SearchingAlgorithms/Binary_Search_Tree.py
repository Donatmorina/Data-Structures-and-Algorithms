class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        if self.value is not None:
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        else:
            self.left_child = None
            self.right_child = None
        
    def is_empty(self):
        return self.value is None
        
    def insert(self, value):
        if self.is_empty():
            self.value = value
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        elif value < self.value:
            self.left_child.insert(value)
        elif value > self.value:
            self.right_child.insert(value)
    
    def compute_sum(self):
        if self.is_empty():
            return 0
        else:
            return self.value + self.left_child.compute_sum() + self.right_child.compute_sum()

    
    def compute_count(self):
        if self.is_empty():
            return 0
        else:
            return 1 + self.left_child.compute_count() + self.right_child.compute_count()


my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(8)
my_tree.insert(10)
my_tree.insert(12)
print('Sum:', my_tree.compute_sum())
print('Number of nodes:', my_tree.compute_count())
