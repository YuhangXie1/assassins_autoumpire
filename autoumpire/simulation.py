#simulates a game
from autoumpire import targeting
import random

class SimGame:
    """
    Class representing simulation of a game where nodes of a generated graph are removed at random

    Attributes:
        initial_graph_size : int
        target_graph_array : [TargetingGraph object]
        lifetime : int

    """
    def __init__(self, initial_graph_size:int, seed = None) -> None:
        self.initial_graph_size = initial_graph_size
        self.seed = seed
        self.target_graph_array = [targeting.TargetingGraph(self.initial_graph_size, self.seed)]
        self.num_nodes_removed = 0
        

    def run(self, tries):
        initial_graph = self.target_graph_array[0]
        initial_seed = initial_graph.generate_solved_initial_graph(10)

        num_nodes_removed_dict = {}

        for x in range(tries):
            self.num_nodes_removed = 0
            working_graph = targeting.TargetingGraph(self.initial_graph_size)
            working_graph.target_graph = initial_graph.target_graph.copy()
            self.remove_random_node(working_graph)
            try:
                num_nodes_removed_dict[self.num_nodes_removed] += 1
            except KeyError:
                num_nodes_removed_dict[self.num_nodes_removed] = 1

        return num_nodes_removed_dict, initial_seed
            
    def remove_random_node(self, graph):
        node_to_remove = random.choice(list(graph.target_graph.nodes))
        if graph.remove_one_node(node_to_remove):
            self.num_nodes_removed += 1
            print(f"successfully removed node {node_to_remove}")
            self.remove_random_node(graph)
        else:
            print(f"Simulation end, nodes removed = {self.num_nodes_removed}")
            return self.num_nodes_removed

    def plot_lifetime(self, num_nodes_removed_dict):
        pass




