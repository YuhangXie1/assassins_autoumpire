from autoumpire import models
import random
import networkx as nx
import matplotlib.pyplot as plt
import sys
import pydot

#seed = 2470123492846919139


class TargetingGraph:
    """
    Object containing a regular 3-degree directed graph (3 in-degrees, 3 out-degrees per node)
    """
    def __init__(self, initial_graph_size, seed = None) -> None:
        self.target_graph = nx.DiGraph()
        self.initial_graph_size = initial_graph_size
        self.set_seed = False
        self.seed = None
        if seed != None:
            self.seed = seed
            self.set_seed = True
            

    def generate_solved_initial_graph(self, tries:int):
        print("Generating new solved initial graph")
        for x in range(int(tries)):
            if self.generate_initial_graph():
                print(f"Number of tries: {x+1}. Successful seed: {self.seed}")
                return self.seed

        raise RuntimeError(f"No valid graph found after {x+1} tries")

    def generate_initial_graph(self):
        """
        Initial building of 3-regular directed graph based on size

        Parameters:
            graph_size (int): number of nodes on graph

        Returns:
        """
        #randomises seed
        if not self.set_seed:
            self.seed = random.randrange(sys.maxsize)
        random.seed(self.seed)

        #add nodes to graph
        self.target_graph = nx.DiGraph()
        self.target_graph.add_nodes_from(list(range(0,self.initial_graph_size)))

        #list of all possible edges, and randomised
        possible_edges = [(u,v) for u in self.target_graph for v in self.target_graph if u != v]

        return self.build_edges(possible_edges)

    def build_edges(self, possible_edges):
        """
        Iteratively builds the edges between nodes

        Parameters:
            possible_edges (list): list of 2D tuples of (u,v) where u is the starting node and v the ending node

        """
        if len(possible_edges) == 0:
            raise RuntimeError("Possible edges list is empty")
        
        random.shuffle(possible_edges)

        #tracking number of in and out degrees for each node
        out_degrees = {node: len(list(self.find_successors(node))) for node in self.target_graph.nodes}
        in_degrees = {node: len(list(self.find_predecessors(node))) for node in self.target_graph.nodes}

        #checking edges are valid before adding them
        for u, v in possible_edges:
            if (v,u) not in self.target_graph.edges and out_degrees[u] < 3 and in_degrees[v] < 3 and self.check_if_cycle_3(u,v) is None:
                self.target_graph.add_edge(u,v)
                out_degrees[u] += 1
                in_degrees[v] += 1
            
            #exits loop if all nodes have the correct degrees
            if all(deg == 3 for deg in out_degrees.values()) and all(deg == 3 for deg in in_degrees.values()):
                return self.check_graph("build_edges - success")
        
        return self.check_graph("build_edges - failure")

    def find_all_neighbors(self, node):
        return nx.all_neighbors(self.target_graph, node)
    
    def find_successors(self, node):
        return self.target_graph.successors(node)
    
    def find_predecessors(self, node):
        return self.target_graph.predecessors(node)
    
    def find_all_edges(self):
        return self.target_graph.edges()
    
    def check_graph(self, caller = None):
        """
        Checks if all nodes satisfy the following conditions:
        1) Does not target itself
        2) Does not target another node targeting it (bidirectional)
        3) Has exactly 3 in-degrees (predecessors) and 3 out-degrees (successors)
        """
        print(f"Checking graph after {caller}")
        err_count = 0

        for (u,v) in self.target_graph.edges:
            if u == v: #No self targeting
                print(f"Connection error: edge ({u},{v}) targets itself")
                err_count += 1
            elif (v,u) in self.target_graph.edges: #no bidirectional edge
                print(f"Connection error: edge ({u},{v}) is bidirectional")
                err_count += 1

        for node in self.target_graph.nodes():
            successors = len(list(self.find_successors(node)))
            predecessors = len(list(self.find_predecessors(node)))
            if successors != 3 or predecessors != 3:
                print(f"node {node} - incorrect: successors = {successors}, predecessors = {predecessors}")
                err_count += 1

        if err_count == 0:
            print(f"Successful seed was: {self.seed}")
            return True
        else:
            print(f"Error count: {err_count}")
            return False

    def remove_one_node(self, node):
        print(f"removing node {node}")
        successors = list(self.find_successors(node))
        predecessors = list(self.find_predecessors(node))
        self.target_graph.remove_node(node)

        possible_edges = [(u,v) for u in predecessors for v in successors if u != v]
        
        return self.build_edges(possible_edges)
        #nx.draw(self.target_graph, with_labels = True)
        #plt.savefig(f"target_graph_remove_{node}.png")


    def cycle_analysis(self):
        cycles = nx.simple_cycles(self.target_graph, 3)
        return cycles

    def check_if_cycle_3(self, u, v):
        #check cycles of 3
        for w in self.target_graph:
            if (v, w) in self.target_graph.edges and (w, u) in self.target_graph.edges:
                return [(u,v),(v,w),(w,u)]
        #check cycles of 4
        #elif any((v, w) in self.target_graph.edges and (w, y) in self.target_graph.edges and (y, u) in self.target_graph.edges for w,y in self.target_graph):
        #    return True
        else:
            return None
        
    def visualise_graph(self):
        visual_target_graph = nx.nx_pydot.to_pydot(self.target_graph)

        #sets parameters
        visual_target_graph.set_layout("neato")
        visual_target_graph.set_overlap("false")

        #sets node attributes
        for node in visual_target_graph.get_nodes():
            node.set("shape","circle")
            node.set("style","filled")
            node.set("fontsize",8)
            node.set("fillcolor","blue")

        #generates png
        visual_target_graph.write_png("target_graph.png")