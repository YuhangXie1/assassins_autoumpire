#simulates a game
from autoumpire import targeting
import random

class SimGame:

    def __init__(self, initial_graph_size:int) -> None:
        self.initial_graph_size = initial_graph_size
        self.target_graph_array = [targeting.TargetingGraph(self.initial_graph_size)]
        self.lifetime = 0

    def run(self, tries):
        initial_graph = self.target_graph_array[0]
        initial_seed = initial_graph.generate_solved_initial_graph(10)

        lifetime_dict = {}

        for x in range(tries):
            self.lifetime = 0
            working_graph = targeting.TargetingGraph(self.initial_graph_size)
            working_graph.target_graph = initial_graph.target_graph.copy()
            self.remove_random_node(working_graph)
            try:
                lifetime_dict[self.lifetime] += 1
            except KeyError:
                lifetime_dict[self.lifetime] = 1

        return lifetime_dict
            
    def remove_random_node(self, graph):
        node_to_remove = random.choice(list(graph.target_graph.nodes))
        if graph.remove_one_node(node_to_remove):
            self.lifetime += 1
            print(f"successfully removed node {node_to_remove}")
            self.remove_random_node(graph)
        else:
            print(f"Simulation end, lifetime = {self.lifetime}")
            return self.lifetime

    def plot_lifetime(self, lifetime_dict):
        pass




