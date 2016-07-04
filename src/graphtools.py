# Author: Rafael Pagliuca
# Created at: 2016-07-03
# Modified at: 2016-07-03

from __future__ import division
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

# This class is used to generate the same plots available for
# each network of http://konect.uni-koblenz.de
class GraphTools:

    def __init__(self, G):
        self.G = G

    # Plot the degree distribuion, i.e., the total count of nodes (y axis) having x (x axis) connections
    def degree_distribution(self):
        degrees = nx.degree_histogram(self.G)
        plt.loglog(degrees,'o')
        plt.show()

    # Plot the cumulative degree distribution, i.e., the probability of a node having more than x (x axis) connections
    def cumulative_degree_distribution(self):
        degrees = nx.degree_histogram(self.G)
        cumulative = list()
        sum = 0.0
        total = float(nx.number_of_nodes(self.G))
        for freq in degrees:
            sum += float(freq)
            cumulative.append(1-(sum/total))
        plt.loglog(cumulative,'o')
        plt.show()

    # Plot assortativity, i.e., the likeness of nodes of high degree connecting with other nodes of high degree,
    # and nodes of low degree connecting with other nodes of low degree
    # It is a scatterplot with one data point for every pair (node degree, average neighbor degree)
    def assortativity(self):
        node_degrees = nx.degree(self.G).values()
        node_neighbors_degrees = nx.average_neighbor_degree(self.G).values()
        plt.loglog(node_degrees, node_neighbors_degrees, 'o')
        plt.show()

    # Plot Lorenz curve: the closer to ((0,0), (1,0)) the Lorenz curve is,
    # the more the edeges are equally distributed among nodes
    def lorenz_curve(self):
        node_degrees = sorted(nx.degree(self.G).values())
        sum = 0
        count = 0
        total = len(node_degrees)
        step = int(total/100.0)
        percentiles = list()
        total_degrees = list()
        for deg in node_degrees:
            sum += deg
            count += 1
            if count % step == 0:
                percentile = count // step # Integer division
                percentiles.append(percentile)
                total_degrees.append(sum)
        plt.plot(percentiles, np.array(total_degrees)*100.0/sum,'-')
        plt.plot([0, 100], [0, 100], '--', color='black')
        plt.plot([0, 100], [100, 0], '--', color='black')
        plt.axes().set_aspect('equal')
        plt.show()

    # Plot the Clustering Coefficient Distribution
    # Percentage of nodes having clustering coefficient less than or equal x axis
    def clustering_coefficient_distribution(self):
        clustering_coefficients = sorted(nx.clustering(self.G).values())
        indices = range(0, len(clustering_coefficients))
        plt.plot(clustering_coefficients, np.array(indices)/len(clustering_coefficients), 'o')
        plt.show()

    # Plot the Distance Distribution up to 20 edges
    def distance_distribution(self):
        nodes = self.G.nodes()
        random.shuffle(nodes)
        distances = [0] * 20
        plt.ion()
        plt.show()
        for node in nodes:
            print node
            lengths = nx.single_source_shortest_path_length(self.G, node)
            for id in lengths:
                try:
                    distances[lengths[id]] += 1
                except:
                    pass
            print distances
            print
            cumulative = list()
            sum = 0
            for distance in distances:
                sum += distance
                cumulative.append(sum)

            plt.clf()
            plt.plot(np.array(cumulative)/sum)
            plt.pause(0.001)
