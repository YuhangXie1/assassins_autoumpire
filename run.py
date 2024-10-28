#Runs the model

from autoumpire import models, targeting
import networkx as nx
import matplotlib.pyplot as plt


players_list = list(range(0,30))
new_game = models.Game(players_list)

print(new_game.players)

current_targeting = targeting.TargetingGraph()
current_targeting.generate_graph(new_game.players)
print(len(list(current_targeting.find_all_edges())))