#Runs the model

from autoumpire import models, targeting
import networkx as nx
import matplotlib.pyplot as plt


players_list = list(range(0,4))
new_game = models.Game(players_list)

print(new_game.players)

current_targeting = targeting.TargetingGraph()
current_targeting.generate_graph(new_game.players)
print(list(current_targeting.find_all_neighbors(0)))
print(list(current_targeting.find_successors(0)))
print(list(current_targeting.find_predecessors(0)))