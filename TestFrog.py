import unittest

import new_frog

"""
 4 4
 1 2 0.1
 2 4 0.2
 1 3 0.5
 3 4 0.1
 0.720000
 0.648000
 """

class TestFrog(unittest.TestCase):


 def test_weigth(self):
     nodes_all = new_frog.create_dictionary_nodes(4)
     edge = new_frog.Nodes_Edge(1, float(1-0.1), 2 )
     nodes_all[1].append(edge)
     edge = new_frog.Nodes_Edge(2, float(1-0.2), 4)
     nodes_all[2].append(edge)
     edge = new_frog.Nodes_Edge(1, float(1 -0.5),  3)
     nodes_all[1].append(edge)
     edge = new_frog.Nodes_Edge(3, float(1 -0.1), 4)
     nodes_all[3].append(edge)
     table = new_frog.create_table_track(4)

     new_frog.dijkstra_priority_creation(nodes_all,table )



 def test_another_test_weigth_hello(self):
     nodes_all = new_frog.create_dictionary_nodes(4)
     edge = new_frog.Nodes_Edge(1, float(1- 0.5),  2 )
     nodes_all[1].append(edge)
     edge = new_frog.Nodes_Edge(2, float(1 -0.3), 3)
     nodes_all[2].append(edge)
     edge = new_frog.Nodes_Edge(3, float(1-0.2), 4)
     nodes_all[3].append(edge)
     table = new_frog.create_table_track(4)

     new_frog.dijkstra_priority_creation(nodes_all,table )



 def test_another_test_weigth(self):
     nodes_all = new_frog.create_dictionary_nodes(2)

     edge = new_frog.Nodes_Edge(1, float(1-0.5),  2 )
     nodes_all[1].append(edge)
     table = new_frog.create_table_track(1)

     new_frog.dijkstra_priority_creation(nodes_all,table )













