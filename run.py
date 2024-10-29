#Runs the model

from autoumpire import models, targeting
import networkx as nx
import matplotlib.pyplot as plt


players_list = list(range(0,30))
new_game = models.Game(players_list)

current_targeting = targeting.TargetingGraph()
current_targeting.generate_graph(new_game.players)
print(len(list(current_targeting.find_all_edges())))
current_targeting.check_num_targets_all()


def find_solution_graph(node_list):
    found_solution = False
    while found_solution == False:
        current_targeting = targeting.TargetingGraph()
        current_targeting.generate_graph(node_list)
        if current_targeting.check_num_targets_all() == True:
            found_solution == True

#find_solution_graph(players_list)
        
#seed: 6985696973381347607 