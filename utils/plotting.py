from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import networkx as nx

def plot_graph():
    G=nx.DiGraph()
    G.add_edge(5,6)
    G.add_edge(5,4)
    pos={5:(2,0),6:(3,-1),4:(1,-1)}
    fig=Figure(figsize=(5,5))
    nx.draw(G,with_labels=True,pos=pos,node_color="skyblue")