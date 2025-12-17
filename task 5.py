import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.color = "#A9DFBF"
        self.id = str(uuid.uuid4())


def build_graph(node, graph, position, x_start=0, y_start=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=str(node.value))
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_x = x_start - 1 / 2 ** layer
            position[node.left.id] = (left_x, y_start - 1)
            build_graph(node.left, graph, position, left_x, y_start - 1, layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right_x = x_start + 1 / 2 ** layer
            position[node.right.id] = (right_x, y_start - 1)
            build_graph(node.right, graph, position, right_x, y_start - 1, layer + 1)


def custom_palette(steps):
    palette = [
        "#006400",
        "#228B22",
        "#32CD32",
        "#ADFF2F",
        "#D0FFB0",
        "#F0FFF0",
    ]
    if steps <= len(palette):
        return palette[:steps]
    extra = ["#F5FFF5"] * (steps - len(palette))
    return palette + extra


def dfs(root):
    stack = [root]
    order = []
    visited = set()
    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            order.append(node)
            visited.add(node.id)
            stack.append(node.right)
            stack.append(node.left)
    return order


def bfs(root):
    queue = deque([root])
    order = []
    visited = set()
    while queue:
        node = queue.popleft()
        if node and node.id not in visited:
            order.append(node)
            visited.add(node.id)
            queue.append(node.left)
            queue.append(node.right)
    return order


def show_traversal(traversal_func):
    order = traversal_func(root)
    colors = custom_palette(len(order))
    for idx, node in enumerate(order):
        node.color = colors[idx]
    graph = nx.DiGraph()
    position = {root.id: (0, 0)}
    build_graph(root, graph, position)
    node_colors = [graph.nodes[n]['color'] for n in graph.nodes]
    labels = {n: graph.nodes[n]['label'] for n in graph.nodes}
    plt.figure(figsize=(8, 5))
    nx.draw(
        graph,
        pos=position,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=node_colors
    )
    plt.show()
    for node in order:
        node.color = "#A9DFBF"


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

print("DFS (стек):")
show_traversal(dfs)

print("BFS (черга):")
show_traversal(bfs)
