
"""
DIJISTRKA ALGORITHM REQUIRED:
1. Create a list of nodes that have the cost to reach the node ( the starting point the cost should be 0), the cost , and the previous node
2. Create a queue where you store the edge with its cost
3. Extract with pop the lowest probability ( the beginning is 0). Pop remove
4  add the cost + the next cost edge
5. Store the previous node
6. When you reach the end you will find the shortest past and its cost
"""

import heapq

def create_table_object (limit)-> list:
    list_table_prior = list()
    for n in range(1, limit+1):
       if n == 1:
           ts = TableCostNodes(n, 0, None )
           list_table_prior.append(ts)
       else:
           ts = TableCostNodes(n, float('inf'), None)
           list_table_prior.append(ts)
            # IT SHOULD BE IN ORDER
    return list_table_prior




def dijkstra_priority_creation(nodes_all):
    list_priority = create_table_object(len(nodes_all))
    queue = list()
    priority_queue = heapq
    # COST NODES
    priority_queue.heappush(queue, (1, 1)) # THE FIRST IS THE PROBABILITY TO NOT FALL DOWN THE SECOND THE NODE
    list_nodes_success = list()
    while True:
        # VISITED THE EDGE WITH LOWEST PRIORITY
        if queue:
          priority = priority_queue.heappop(queue)
          for ts in nodes_all[priority[1]]:
                # VISITED THE EDGE AND PUSH
                # CALCULATE COST TAKE IN ACCOUNT THE START
                if priority[0] < 0:
                    # KEEP NEGATIVE
                    cost = priority[0]* (1 - ts.probability)  # EXTRACT THE PROBABILITY
                else:
                    cost = (priority[0] * -1) * (1 - ts.probability)  # EXTRACT THE PROBABILITY

                # ADD THE NEXT POINTER
                priority_queue.heappush(queue, (cost, ts.next_pointer_edge,))
                objects =  list_priority[ts.next_pointer_edge-1]
                if cost  < objects.cost :
                    objects.cost = cost
                    objects.previousNode = ts.before
        else:
            break


    success =  list_priority[len(list_priority)-1]
    print(f"{success.cost*-1:.6f}")

def create_dictionary(limit)-> dict:
    nodes = dict()
    for i in range(1, limit+1):
        nodes[i] = list()
    return nodes


def verify_constraint_number (n):
    verify  = True
    if n < 2 or n > 10000:
        verify = False
    return verify


def recover_input():

  number_lilies, possible_jumps = input().split()
  convert_number = int(number_lilies)
  convert_jump = int(possible_jumps)
  if verify_constraint_number(convert_number):
    nodes_all = create_dictionary(convert_number)

  # CREATE DICTIONARY
    while convert_jump > 0 :
        nodes, edge, prob_fall_down = input().split()
        convert_nodes = int(nodes)
        next_converts_edge = int(edge)
        # CREATE OBJECT NODES WITH IT OWN EDGE
        probability_fall_down_conversion = float(prob_fall_down)
        probability_safe = 1 - probability_fall_down_conversion
        edge_prob = EdgeProbability(convert_nodes, probability_fall_down_conversion, next_converts_edge, probability_safe)
        # EXTRACT THE OBJECT AND STORE THE CORRECT ORDER
        nodes_all[convert_nodes].append(edge_prob)
        convert_jump -=1
    dijkstra_priority_creation(nodes_all)


class EdgeProbability:

    def __init__(self, before, probability, next_pointer_edge, probability_safe):
                self.before = before
                self.probability = probability
                self.next_pointer_edge = next_pointer_edge
                self.probability_safe = probability_safe

class TableCostNodes:
    def __init__(self, node, cost, previous_node):
                self.node = node
                self.cost = cost
                self.previousNode = previous_node



if __name__ == '__main__':
        recover_input()
