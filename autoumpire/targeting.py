from autoumpire import models
import random
import networkx as nx
import matplotlib.pyplot as plt
import sys

seed = 6985696973381347607
# seed = random.randrange(sys.maxsize)
random.seed(seed)

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

        non_saturated_nodes = player_list.copy()

        #round 1
        self.target_graph.add_edges_from(list(self.build_edge(non_saturated_nodes).edges))
        #round 2
        self.target_graph.add_edges_from(list(self.build_edge(non_saturated_nodes).edges))
        #round 3
        self.target_graph.add_edges_from(list(self.build_edge(non_saturated_nodes).edges))

        nx.draw(self.target_graph, with_labels = True)
        plt.savefig("target_graph.png")

    def build_edge(self, player_list):
        working_graph = self.target_graph.copy()
        #print(len(list(working_graph.edges())))
  
        for player in player_list:
            working_node_list = player_list.copy()
            working_node_list.remove(player) #so cannot form an edge to itself
            for node in player_list:
                if node in working_node_list:
                    if len(list(working_graph.predecessors(node))) >= self.targets: #removes all nodes already got 3 players targeting it
                        working_node_list.remove(node)
                    elif player in list(working_graph.successors(node)):
                        working_node_list.remove(node)
                
            if len(working_node_list) != 0:
                target = random.choice(working_node_list)
                working_graph.add_edge(player, target)
            else:
                print(f"No available valid targets for node {player}")

        return(working_graph)

    def find_all_neighbors(self, node):
        return nx.all_neighbors(self.target_graph, node)
    
    def find_successors(self, node):
        return self.target_graph.successors(node)
    
    def find_predecessors(self, node):
        return self.target_graph.predecessors(node)
    
    def find_all_edges(self):
        return self.target_graph.edges()
    
    def check_num_targets_all(self):
        """
        Checks if all nodes have the right number of predecessors and successors
        """
        print("Seed was:", seed)
        count = 0
        for node in self.target_graph.nodes():
            if len(list(self.find_successors(node))) == 3 and len(list(self.find_predecessors(node))) == 3:
                print(f"node {node} - correct")
            else:
                print(f"node {node} - incorrect: successors = {len(list(self.find_successors(node)))}, predecessors = {len(list(self.find_predecessors(node)))}")
                count += 1
        
        if count == 0:
            return True 
        else:
            print(count)
            return False



