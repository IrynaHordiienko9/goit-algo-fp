import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="deepskyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_heap_tree(heap, color="deepskyblue"):
    if not heap:
        return None
    nodes = [Node(val, color=color) for val in heap]
    for i, node in enumerate(nodes):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]
    return nodes[0]


def add_edges(graph, node, position, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_x = x - 1 / 2 ** layer
            position[node.left.id] = (left_x, y - 1)
            add_edges(graph, node.left, position, x=left_x, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right = x + 1 / 2 ** layer
            position[node.right.id] = (right, y - 1)
            add_edges(graph, node.right, position, x=right, y=y - 1, layer=layer + 1)


def draw_heap(heap, color="deepskyblue"):
    root = build_heap_tree(heap, color=color)
    if not root:
        print("Купа порожня")
        return
    tree = nx.DiGraph()
    position = {root.id: (0, 0)}
    add_edges(tree, root, position)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=position, labels=labels, arrows=False, node_size=2500, node_color=colors, font_size=14)
    plt.title("Візуалізація бінарної купи", fontsize=16)
    plt.show()


heap = [15, 10, 8, 7, 9, 5, 6]
draw_heap(heap)
