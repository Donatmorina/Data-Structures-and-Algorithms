#Graph
class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
    
    def add_edge(self, node1, node2, directed=False):
        if node1 not in self.adjacency_list:
            self.add_node(node1)
        if node2 not in self.adjacency_list:
            self.add_node(node2)
        self.adjacency_list[node1].append(node2)
        if not directed:
            self.adjacency_list[node2].append(node1)
    
    def display(self):
        for node, edges in self.adjacency_list.items():
            print(f"{node} -> {', '.join(map(str, edges))}")
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbor in self.adjacency_list.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)
    
    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            node = queue.pop(0)
            print(node, end=" ")
            for neighbor in self.adjacency_list.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

print("Graph Operations:")
graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("D", "E", directed=True)  # Directed edge
graph.display()
print("\nDFS from node A:")
graph.dfs("A")
print("\nBFS from node A:")
graph.bfs("A")
print()
print("\n")



#Tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)
    
    def add_left(self, parent, child_data):
        parent.left = TreeNode(child_data)
    
    def add_right(self, parent, child_data):
        parent.right = TreeNode(child_data)
    
    def pre_order(self, node):
        if node:
            print(node.data, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)
    
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.data, end=" ")
            self.in_order(node.right)
    
    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end=" ")


print("Tree Operations:")
tree = BinaryTree("A")
tree.add_left(tree.root, "B")
tree.add_right(tree.root, "C")
tree.add_left(tree.root.left, "D")
tree.add_right(tree.root.left, "E")

print("Pre-order Traversal:")
tree.pre_order(tree.root)
print("\nIn-order Traversal:")
tree.in_order(tree.root)
print("\nPost-order Traversal:")
tree.post_order(tree.root)
print()


