
 # ABSOLUTE ERROR 10-6
def recover_input (self):

      number_lilies, possible_jumps  = input("Enter a values\n").split()
      convert_jump = int(possible_jumps)
      key_nodes_probability = dict()
      # CREATE A DICTIONARY CONTAINS A LIST OF THE NODE WITH AN PERCENTAGE
      # ASSIGN THE PERCENTAGE STANDARD
      for s in range(1, int(number_lilies)+1):
         if s == 1:
             key_nodes_probability[s] = float(0)
         else:
             key_nodes_probability[s] = float(1)
         sorted(key_nodes_probability.items())
      # BEGIN TO EVALUATE
      # IF THE EVENT OCCURS THE SAME TIME + OTHERWISE MULTIPLICATION
      # https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm Dijkstra
      while convert_jump > 0:
        nodes, edge, prob_fall_down =  input("Enter a values\n").split()
        convert_float = float(prob_fall_down)
        for i in range(int(nodes)+1, int(edge)+1):
            if convert_float < key_nodes_probability [i]:
                key_nodes_probability [i] = convert_float
        convert_jump -= 1
      success = 1
      # CONVERT PERCENTAGE
      for k,v in key_nodes_probability.items():
        if v == float(0):
          continue
        else:
         variation = float(1) - v
         success *= float(variation)
         # ABSOLUTE ERROR 10 -6
      print(f"{success:.6f}")

if __name__ == "__main__":

    recover_input("")





