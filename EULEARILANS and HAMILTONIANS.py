import matplotlib.pyplot as plt
import networkx as nx

# Create a figure for the Eulerian graph
plt.figure(figsize=(10, 5))

# Create an Eulerian Graph
G_eulerian = nx.Graph()
G_eulerian.add_edges_from([('Sandbox', 'Slide'), ('Sandbox', 'Swing Set'), ('Slide', 'Swing Set')])

# Draw the Eulerian Graph
plt.subplot(1, 2, 1)
pos_eulerian = nx.spring_layout(G_eulerian)
nx.draw(G_eulerian, pos_eulerian, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_color='black', font_weight='bold')
plt.title('Eulerian Graph (Visit Each Path Once)')
plt.axis('off')

# Create a figure for the Hamiltonian graph
plt.subplot(1, 2, 2)

# Create a Hamiltonian Graph
G_hamiltonian = nx.Graph()
G_hamiltonian.add_edges_from([('Tree', 'Swing 1'), ('Tree', 'Swing 2'), ('Swing 1', 'Swing 2'), ('Swing 1', 'Bench'), ('Swing 2', 'Bench')])

# Draw the Hamiltonian Graph
pos_hamiltonian = nx.spring_layout(G_hamiltonian)
nx.draw(G_hamiltonian, pos_hamiltonian, with_labels=True, node_color='lightgreen', node_size=2000, font_size=15, font_color='black', font_weight='bold')
plt.title('Hamiltonian Graph (Visit Each Spot Once)')
plt.axis('off')

# Show the graphs
plt.tight_layout()
plt.show()
