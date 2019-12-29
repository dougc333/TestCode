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

class Matrix:

  def __init__(self, num_rows, num_cols):
    self.matrix=[]
    self.num_rows = num_rows
    self.num_cols = num_cols
    for i in range(0, num_rows):
      row = []
      for j in range(0,num_cols):
        row.append(Node(i,j))
      self.matrix.append(row)
  
  def make_test_graph(self):
    self.matrix[0][0].set_weights(3,None,1)
    self.matrix[0][1].set_weights(2,None,0)
    self.matrix[0][2].set_weights(4,None,2)
    self.matrix[0][3].set_weights(0,None,4)
    self.matrix[0][4].set_weights(None,None,3)
    #
    self.matrix[1][0].set_weights(3,None,3)
    self.matrix[1][1].set_weights(2,None,6)
    self.matrix[1][2].set_weights(4,None,5)
    self.matrix[1][3].set_weights(2,None,2)
    self.matrix[1][4].set_weights(None,None,1)
    #
    self.matrix[2][0].set_weights(0,None,4)
    self.matrix[2][1].set_weights(7,None,4)
    self.matrix[2][2].set_weights(3,None,5)
    self.matrix[2][3].set_weights(4,None,2)
    self.matrix[2][4].set_weights(None,None,1)
    #
    self.matrix[3][0].set_weights(3,None,5)
    self.matrix[3][1].set_weights(3,None,6)
    self.matrix[3][2].set_weights(0,None,8)
    self.matrix[3][3].set_weights(2,None,5)
    self.matrix[3][4].set_weights(None,None,3)
    #
    self.matrix[4][0].set_weights(1,None,None)
    self.matrix[4][1].set_weights(3,None,None)
    self.matrix[4][2].set_weights(2,None,None)
    self.matrix[4][3].set_weights(2,None,None)
    self.matrix[4][4].set_weights(None,None,None)
    #
  def set_long(self):
    for i in range(0,self.num_rows):
      #row=self.matrix[i]
      for j in range(0,self.num_cols):
        find_max=[]
        max_value=None
        print("debug i:",i," j:",j)
        if (i!=0 and j!=0):
          #access the node on top, to the left and to right. if they exist
          left = self.matrix[i-1][j].south + self.matrix[i-1][j].weight
          #top_left = matrix[i-1][j-1].se + self.matrix[i-1][j-1].weight
          top = self.matrix[i][j-1].east + self.matrix[i][j-1].weight
          find_max.append(left)
          #find_max.append(top_left)
          find_max.append(top)
          max_value = max(find_max)
          self.matrix[i][j].weight = max_value
        elif(i==0 and j>0):
          left = self.matrix[i][j-1].east+self.matrix[i][j-1].weight
          find_max.append(left)
          max_value = max(find_max)
          self.matrix[i][j].weight = max_value
        elif(i>0 and j==0):
          top = self.matrix[i-1][j].south + self.matrix[i-1][j].weight
          find_max.append(top)
          max_value = max(find_max)
          self.matrix[i][j].weight = max_value
        else:
          print("origin set to 0 i,j:",i,j) #once for 0,0
          self.matrix[i][j].weight = 0
        #if len(find_max)>0:
        #  self.matrix[i][j].weight=max_value   
        print("i j:",i,j,"find_max:",find_max)
      
  def backtrack(self):
    i = self.num_rows-1
    j = self.num_cols-1
    node_path=[]
    node_path.append((i,j))
    while(i>0 and j>0):
      print("backtrack i j:",i,j)
      if(i>0 and j>0):
        top=self.matrix[i-1][j].weight
        #upper_left = self.matrix[i-1][j-1].weight
        left = self.matrix[i][j-1].weight
        max_list=[]
        max_list.append(top)
        max_list.append(left)
        max_weight = max(max_list)
        if (max_weight == top):
          i=i-1
        elif(max_weight==left):
          j=j-1
        node_path.append((i,j)) 
      elif(i==0 and j>0 ):
        #find max and update
        top = self.matrix[i][j-1]
        j=j-1
        node_path.append((i,j))
      elif(i>0 and j==0):
        #find max and update
        left = self.matrix[i-1][j]
        i=i-1
        node_path.append((i,j))
      else:
        print("backtrach origin i j",i,j)
    print("node_path:",node_path)
  def print_me(self):
    print('----------------------------')
    for i in range(0,self.num_rows):
      for j in range(0,self.num_cols):
        print("i j:",i,j, self.matrix[i][j].east,self.matrix[i][j].se,self.matrix[i][j].south,self.matrix[i][j].weight )

  def test(self):
    self.make_test_graph()
    self.print_me()

graph=Matrix(5,5)
graph.test()
print("*************************")
graph.set_long()
print("$$$$$$$$$$$$$$$$$$$$$$$$$")
graph.backtrack()

