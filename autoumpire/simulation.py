#simulates a game
from autoumpire import targeting
import random

class SimGame:

    def __init__(self, initial_graph_size:int) -> None:
        self.initial_graph_size = initial_graph_size
        self.target_graph_array = [targeting.TargetingGraph(self.initial_graph_size)]
        self.lifetime = 0

    def run(self):
        initial_graph = self.target_graph_array[0]
        initial_graph.generate_graph()

        working_graph = initial_graph.target_graph.copy()
        self.remove_random_node(working_graph)
             
    def remove_random_node(self, graph):
        if graph.target_graph.remove_node(random.choice(list(graph.target_graph.nodes()))):
            self.lifetime += 1
            self.remove_random_node(self,graph)
        else:
            print(f"Simulation end, lifetime = {self.lifetime}")
            return self.lifetime






