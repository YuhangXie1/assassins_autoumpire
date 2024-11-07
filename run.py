#Runs the model

from autoumpire import models, targeting, simulation
import networkx as nx
import matplotlib.pyplot as plt



# current_targeting = targeting.TargetingGraph(100)
# print(current_targeting.generate_solved_initial_graph(10))
# current_targeting.remove_node(0)

#seed = 6273828566894813741

new_sim = simulation.SimGame(30)
new_dict, new_seed = new_sim.run(10)
print(new_dict)
print(new_seed)
plt.bar(new_dict.keys(), new_dict.values())
plt.savefig("output.png")
#new_sim.remove_random_node(new_sim.working_graph)
