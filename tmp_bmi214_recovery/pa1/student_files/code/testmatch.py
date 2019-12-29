class Node:
  
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.first_AA=None
    self.second_AA=None
    self.weight = -1
  def printNode(self):
    print("x y:",self.x,self.y," first_AA, secondAA",self.first_AA, self.second_AA, "weight:",self.weight)

class Match:
  def __init__(self):
    self.matrix=[]
    with open('match1.txt') as fh:
      cnt=0
      for line in fh:
        if cnt==0:
          self.len_first_alphabet = int(line.strip())
          self.num_cols = self.len_first_alphabet
        elif(cnt==1):
          self.first_alphabet = [x for x in line.strip()]
        elif(cnt==2):
          self.len_second_alphabet = int(line.strip())
          self.num_rows = self.len_second_alphabet
        elif(cnt==3):
          self.second_alphabet = [x for x in line.strip()]
          self.init_matrix()
        else:
          print("adding to match:",cnt,line)
          #parse and add to self.matrix
          parse_line = line.strip().split()
          print("parse_line:",parse_line)
          col_coord = int(parse_line[0])
          row_coord = int(parse_line[1])
          #print("row_coord",row_coord, type(row_coord))
          firstAA = parse_line[2]
          secondAA = parse_line[3]
          similarity = float(parse_line[4])
          print("row_coord:",row_coord," col_coord:",col_coord," firstAA:",firstAA, " secondAA:",secondAA," similarity:",similarity)
          self.matrix[row_coord-1][col_coord-1].first_AA=firstAA
          self.matrix[row_coord-1][col_coord-1].second_AA=secondAA
          self.matrix[row_coord-1][col_coord-1].weight = similarity
        cnt +=1
    
  def init_matrix(self):
    for i in range(0, self.num_rows):
        row = []
        for j in range(0,self.num_cols):
          row.append(Node(i,j))
        self.matrix.append(row)
    print("+++++++++++++++")
    self.print_matrix()
    print("+++++++++++++++")
    
  def print_matrix(self):
    print("********************")
    print("print matrix:")
    print("self.num_cols:",self.num_cols," self.num_rows:",self.num_rows)
    print("self.first_alphabet:",self.first_alphabet," self.second_alphabet:", self.second_alphabet)
    for i in range(0,self.num_rows):
      for j in range(0, self.num_cols):
        self.matrix[i][j].printNode()
    print("********************")

  def lookup(self,a,b):
    '''
      return match given a=first string AA, b=second string AA
    '''
    col = self.first_alphabet.index(a)
    row = self.second_alphabet.index(b)
    return self.matrix[row][col].weight
    
m = Match()  
m.print_matrix()
print("A A similarity:",m.lookup('A','A'))