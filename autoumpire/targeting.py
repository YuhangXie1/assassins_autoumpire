from autoumpire import models
import random
import networkx as nx
import matplotlib.pyplot as plt
import sys

#seed = 6985696973381347607
seed = random.randrange(sys.maxsize)
random.seed(seed)

class TargetingGraph:
    """
    Object containing a regular 3-degree directed graph (3 in-degrees, 3 out-degrees per node)
    """
    def __init__(self) -> None:
        self.target_graph = nx.DiGraph()

    def generate_graph(self, player_list):

        #add nodes to graph
        self.target_graph.add_nodes_from(player_list)

        #list of all possible edges, and randomised
        possible_edges = [(u,v) for u in self.target_graph for v in self.target_graph if u != v]
        random.shuffle(possible_edges)

        #tracking number of in and out degrees for each node
        out_degrees = {node: 0 for node in self.target_graph.nodes}
        in_degrees = {node: 0 for node in self.target_graph.nodes}

        #checks each edge and see if they are valid additions
        for u, v in possible_edges:
            if (v,u) not in self.target_graph.edges and out_degrees[u] < 3 and in_degrees[v] <3:
                self.target_graph.add_edge(u,v)
                #print(f"added edge ({u},{v})")
                out_degrees[u] += 1
                in_degrees[v] += 1
                
            if all(deg == 3 for deg in out_degrees.values()) and all(deg == 3 for deg in in_degrees.values()):
                break

        self.check_graph()
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
    
    def check_graph(self):
        """
        Checks if all nodes satisfy the following conditions:
        1) Does not target itself
        2) Does not target another node targeting it (bidirectional)
        3) Has exactly 3 in-degrees (predecessors) and 3 out-degrees (successors)
        """

        print("Seed was:", seed)
        err_count = 0

        
        for (u,v) in self.target_graph.edges:
            if u == v: #No self targeting
                print(f"Connection error: edge ({u},{v}) targets itself")
                err_count += 1
            elif (v,u) in self.target_graph.edges: #no bidirectional edge
                print(f"Connection error: edge ({u},{v}) is bidirectional")
                err_count += 1

        for node in self.target_graph.nodes():
            if len(list(self.find_successors(node))) == 3 and len(list(self.find_predecessors(node))) == 3:
                print(f"node {node} - correct")
            else:
                print(f"node {node} - incorrect: successors = {len(list(self.find_successors(node)))}, predecessors = {len(list(self.find_predecessors(node)))}")
                err_count += 1
        
        if err_count == 0:
            return True
        else:
            print(f"Error count: {err_count}")
            return False



