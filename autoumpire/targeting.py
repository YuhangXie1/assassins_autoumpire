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
        working_graph = nx.DiGraph()
        working_graph.add_nodes_from(player_list)

        #round 1, finding a random, non-self to connect to
        for player in player_list:
            working_node_list = player_list.copy()
            working_node_list.remove(player) #so cannot form an edge to itself
            for node in working_node_list:
                if len(list(working_graph.predecessors(node))) >= self.targets: #removes all nodes already got 3 players targeting it
                    working_node_list.remove(node)
            
            target = random.choice(working_node_list)
            print("adding edge between" + str((player,target)))
            working_graph.add_edge(player, target)


        
        # self.target_graph.add_nodes_from(player_list)
        # self.target_graph.add_edges_from([(0,1),(2,3),(3,1)])

        self.target_graph = working_graph
        nx.draw(self.target_graph, with_labels = True)
        plt.savefig("target_graph.png")

    def find_all_neighbors(self, node):
        return nx.all_neighbors(self.target_graph, node)
    
    def find_successors(self, node):
        return self.target_graph.successors(node)
    
    def find_predecessors(self, node):
        return self.target_graph.predecessors(node)
    
    def find_all_edges(self):
        return self.target_graph.edges()