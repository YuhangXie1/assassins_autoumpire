#Runs the model

from autoumpire import models, targeting
import networkx as nx
import matplotlib.pyplot as plt



current_targeting = targeting.TargetingGraph(100)
current_targeting.generate_solved_initial_graph(10)
#print(len(list(current_targeting.find_all_edges())))
#print(list(current_targeting.cycle_analysis()))

#current_targeting.remove_node(0)
#print(list(current_targeting.cycle_analysis()))

#current_targeting.remove_node(1)
#print(list(current_targeting.cycle_analysis()))



# def find_solution_graph(node_list):
#     found_solution = False
#     while found_solution == False:
#         current_targeting = targeting.TargetingGraph()
#         current_targeting.generate_graph(node_list)
#         if current_targeting.check_graph() == True:
#             found_solution = True

#find_solution_graph(players_list)
        
#seed: 6985696973381347607 