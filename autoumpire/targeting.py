from autoumpire import models
import random
import networkx as nx
import matplotlib.pyplot as plt



class TargetingGraph:
    """
    Graph of which players are targeting who
    """
    def __init__(self) -> None:
        self.players = []
        self.target_graph = nx.DiGraph()
        self.targets = 3

    def generate_graph(self, player_list):
        self.target_graph.add_nodes_from(player_list)
        self.target_graph.add_edges_from([(0,1),(2,3),(3,1)])

        nx.draw(self.target_graph, with_labels = True)
        plt.savefig("target_graph.png")

    def find_all_neighbors(self, node):
        return nx.all_neighbors(self.target_graph, node)
    
    def find_successors(self, node):
        return self.target_graph.successors(node)
    
    def find_predecessors(self, node):
        return self.target_graph.predecessors(node)
