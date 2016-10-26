'''
Created on Oct 25, 2016

@author: Ravi Sankar Karuturi
'''
from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect('demo')