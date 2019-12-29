class Node:
  
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.east=None
    self.se=None
    self.south=None
    self.weight = -1

  def set_weights(self,east, se, south):
    self.east = east
    self.se = se
    self.south = south
  def node_print():
    print("node_print:",self.x, self.y, self.east, self.se, self.south. self.weight)

class Graph:
  
  def __init__(self,first,second):
    self.first_string=first
    self.second_string = second
    self.len_first = len(first_string)
    self.len_second = len(second_string)
    self.first_alphabet = "ACTG"
    self.second_alphabet="AUTG"
    self.num_cols = len_first
    self.num_rows = len_second
    self.matrix=[]
     for i in range(0, num_rows):
      row = []
      for j in range(0,num_cols):
        row.append(Node(i,j))
      self.matrix.append(row)
    #set match for entries
    def make_match(self):
      