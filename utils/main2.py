import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
# Tree node class
class TreeNode:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None
# Tree traversal functions
def preorder_traversal(root, visited=[]):
    if root:
        visited.append(root.value)
        preorder_traversal(root.left, visited)
        preorder_traversal(root.right, visited)
    return visited
def inorder_traversal(root, visited=[]):
    if root:
        inorder_traversal(root.left, visited)
        visited.append(root.value)
        inorder_traversal(root.right, visited)
    return visited
def postorder_traversal(root, visited=[]):
    if root:
        postorder_traversal(root.left, visited)
        postorder_traversal(root.right, visited)
        visited.append(root.value)
    return visited
def level_order_traversal(root):
    if not root:
        return [] 
    visited = []
    queue = deque([root])  
    while queue:
        node = queue.popleft()
        visited.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)  
    return visited
# Function to visualize the tree using NetworkX and Matplotlib
def visualize_tree(root, traversal_path, traversal_type):
    G = nx.DiGraph()
    pos = {}
    def add_edges(node, x, y, dx):
        if node is not None:
            pos[node.value] = (x, y)
            if node.left:
                G.add_edge(node.value, node.left.value)
                add_edges(node.left, x - dx, y - 1, dx / 2)
            if node.right:
                G.add_edge(node.value, node.right.value)
                add_edges(node.right, x + dx, y - 1, dx / 2)
    # Construct the tree graph
    add_edges(root, 0, 0, 4)
    # Create the plot
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold", arrows=False)
    # Highlight the traversal path
    for i, node in enumerate(traversal_path):
        nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color="red", node_size=600)
        plt.title(f"{traversal_type} - Step {i+1}: Visited {node}")
        plt.pause(0.8)
    plt.show()
# Function to generate the spanning tree using BFS
def generate_spanning_tree(root):
    if not root:
        return []
    
    visited = []
    queue = deque([root])
    spanning_edges = []  
    while queue:
        node = queue.popleft()
        visited.append(node.value)
        if node.left:
            spanning_edges.append((node.value, node.left.value))
            queue.append(node.left)
        if node.right:
            spanning_edges.append((node.value, node.right.value))
            queue.append(node.right)
    # Visualize the spanning tree
    visualize_spanning_tree(visited, spanning_edges)
# Function to visualize spanning tree
def visualize_spanning_tree(nodes, edges):
    G = nx.Graph()
    # Add nodes and edges to the graph
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    # Draw the spanning tree
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=500, font_size=10, font_weight="bold")
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=2)
    plt.title("Spanning Tree")
    plt.show()
# Example tree creation
def create_sample_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root
# Example usage of the toolkit
if __name__ == "_main_":
    root = create_sample_tree()
    # Select traversal type
    traversal_type = 'postorder'  # Can be 'preorder', 'inorder', 'postorder', 'level_order'
    # Perform the traversal
    if traversal_type == 'preorder':
        traversal_path = preorder_traversal(root, [])
    elif traversal_type == 'inorder':
        traversal_path = inorder_traversal(root, [])
    elif traversal_type == 'postorder':
        traversal_path = postorder_traversal(root, [])
    elif traversal_type == 'level_order':
        traversal_path = level_order_traversal(root)
    # Visualize the traversal
    visualize_tree(root, traversal_path, traversal_type)
    # Generate and visualize the spanning tree
    generate_spanning_tree(root)