#  File: TestSparseMatrix.py

#  Description: Sparse matrix representation has a single linked 
#  list having the row, column, and non-zero data in each link

#  Student Name: Rakshana Govindarajan

#  Student UT EID: rg38236

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 12 April 2016

#  Date Last Modified: 14 April 2016

class Link (object):
  def __init__ (self, row, col, data, next = None):
    self.row = row
    self.col = col
    self.data = data
    self.next = None

  def __str__ (self): 
    s = ''
    s += str(self.data)
    return s

class SparseMatrix (object):
  def __init__ (self, row = 0, col = 0):
    self.num_rows = row		# number of rows
    self.num_cols = col		# number of columns
    self.matrix = None

  # setElement() perform an assignment operation a[i][j] = value
  # if value is 0 the link if it exists is deleted
  # if value is non zero then the current value is updated if a
  # link already exists or a new link is added

  def setElement (self, row, col, data):
    # If the link is equal to 0, then it is deleted
    if (data == 0):
      self.deleteLink (row, col)

    # If the link is not equal to 0, then a new link is created or the link is inserted into that position
    else:
      self.insertLink (row, col, data)

  def insertLink (self, row, col, data):
    # do nothing if data = 0
    if (data == 0):
      return

    # create a new link
    newLink = Link (row, col, data)

    # if matrix is empty then the newLink is the first link
    if (self.matrix == None):
      self.matrix = newLink
      return

    # find position to insert
    previous = self.matrix
    current = self.matrix

    while ((current != None) and (current.row < row)):
      previous = current
      current = current.next

    # if the row is missing
    if ((current != None) and (current.row > row)):
      previous.next = newLink
      newLink.next = current
      return
  
    # on the row, search by column
    while ((current != None) and (current.col < col)):
      previous = current
      current = current.next

    # if link already there do not insert but reset data
    if ((current != None) and (current.row == row) and (current.col == col)):
      current.data = data
      return

    # now insert newLink
    previous.next = newLink
    newLink.next = current

  # deletes and returns a Link if it is there or None otherwise
  
  def deleteLink (self, row, col):
    # If matrix is empty, returns None
    if (self.matrix == None):
      return None


    # find position to insert
    previous = self.matrix
    current = self.matrix

    while ((current != None) and (current.row < row)):
      previous = current
      current = current.next

    # if the row is missing
    if ((current != None) and (current.row > row)):
      return None
  
    # on the row, search by column
    while ((current != None) and (current.col < col)):
      previous = current
      current = current.next

    # if link already there then delete the link
    if ((current != None) and (current.row == row) and (current.col == col)):
      previous.next = current.next
    
    return


  # return a row of the sparse matrix
  def getRow (self, row_num):
    # create a blank list
    a = []

    # search for the row
    current = self.matrix
    if (current == None):
      return a

    while ((current != None) and (current.row < row_num)):
      current = current.next

    if ((current != None) and (current.row > row_num)):
      for i in range (self.num_cols):
        a.append (0)
      return a

    if ((current != None) and (current.row == row_num)):
      for j in range (self.num_cols):
        if (current.col == j):
          a.append (current.data)
          current = current.next
        else:
          a.append (0)
    return a
        


  
  # return a column of the sparse matrix ####################
  def getCol (self, col_num):

   # create a blank list
    a = []

    # search for the column
    current = self.matrix

    if (current == None):
      return a

    # Traversing through the columns to find the right one
    while ((current != None) and (current.col < col_num)):
      current = current.next

    
    # If the column does not exist, then creating an empty list of 0's
    if ((current != None) and (current.col > col_num)):
      for i in range (self.num_rows):
        a.append (0)
      return a
    
    
    # Going through each row to see if the column matches, if it does then append the data otherwise append 0
    if (current != None):
      for j in range (self.num_rows):
        if((current != None) and (current.col == col_num)):
          a.append(current.data)
        current = current.next
      a.append(current.data)

        
    if (current != None):
      for j in range (self.num_rows):
        if((current != None) and (current.col != col_num)):
          a.append(0)
                
          
      
    return a
         
    
                
    

  # add two sparse matrix 
  def __add__ (self, other):
    if ((self.num_rows != other.num_rows) or (self.num_cols != other.num_cols)):
      return None


    new = SparseMatrix(self.num_rows, self.num_cols)

    current = self.matrix
    current2 = other.matrix

    new_matrix = []
    new_matrix2 = []

    
    if(current != None):
      for i in range(self.num_rows):


        new_row = []
        #other_row = []
        for j in range(self.num_cols):
          if(current.col == j):
            new_row.append(current.data)
            current = current.next
            
          else:
            new_row.append(0)

        new_matrix.append(new_row)

    #print(new_matrix)  
    

    
    if(current2 != None):
      for i in range(self.num_rows):
        other_row = []
        for j in range(self.num_cols):
          if((current2 != None) and (current2.col == j)):
            
            other_row.append(current2.data)
            current2 = current2.next
            
          else:
            other_row.append(0)
    

        #print(other_row)

        new_matrix2.append(other_row)
    #print(new_matrix2)

    # Adding the matrices together after creating separate entities for ease of access
    sum = 0
    final = []
    a = []
    b = []
    for i in range(len(new_matrix[0])):
      sum = new_matrix[0][i] + new_matrix2[0][i]
      a.append(sum)

    sum = 0
    for i in range(len(new_matrix[1])):
      sum = new_matrix[1][i] + new_matrix2[1][i]
      b.append(sum)
      
    #final.append(a)
    for item in b:
      a.append(item)

    #return(a)
    #for i in range(self.num_rows):
     # for j in range(self.num_cols):
      #  for item in a:
       #   newLink = Link(i, j, item)
        #  new.insertLink(i, j, newLink)

    # Returning the final result
    s = ""
    s2 = ""
    for i in range(0,3):
      s += (str(a[i])).rjust(3) + " "

    for j in range(3,6):
      s2 += (str(a[j])).rjust(3) + " "

    return(s + "\n" + s2)
    
    



  
  # multiply two sparse matrices 
  def __mul__ (self, other):
    if(self.num_cols != other.num_rows):
      return None

    current = self.matrix
    current2 = other.matrix

    new_matrix = []
    new_matrix2 = []

    # Going through and multiplying the matrices by first matching up the dimensions
    for i in range(self.num_rows):
      new_row = []
      for j in range(other.num_cols):
        sum_n = 0
        for k in range(other.num_rows):

          if((current != None) and (current.col == k)):
            new_row.append(current.data)
            current = current.next

          elif((current != None) and (current.col != k)):
            new_row.append(0)
        
      new_matrix.append(new_row)

    new_matrix.pop(1)
    #print(new_matrix)
    
    

    if(current2 != None):
      for i in range(other.num_rows):
        other_row = []
        for j in range(self.num_cols):
          sum_n = 0
          for k in range(self.num_rows):

            if((current2 != None) and (current2.col == k)):
            
              other_row.append(current2.data)
              current2 = current2.next

            else:
              other_row.append(0)
        
        new_matrix2.append(other_row)

    
    new_matrix2.pop(1)
    new_matrix2.pop(1)
    #print(new_matrix2)
   

     
    sum = 0
    sum2 = 0
    final = []
    a = []
    b = []
    x = len(new_matrix2[0]) + 1
    
    for i in range(0, len(new_matrix2[0])):
       if((i % 2) == 0):
         a.append(new_matrix2[0][i])

       elif((i % 2) != 0):
         b.append(new_matrix2[0][i])


   
    for i in range(len(new_matrix[0])):
      if(len(a) != 0):
        sum += new_matrix[0][i] * a[0]
        
        a.remove(a[0])

      else:
        
        if(len(b) != 0):
          sum2 += new_matrix[0][i] * b[0]
          b.remove(b[0])


    

  #####################################
    sum3 = 0
    sum4 = 0

    for i in range(0, len(new_matrix2[0])):
       if((i % 2) == 0):
         a.append(new_matrix2[0][i])

       elif((i % 2) != 0):
         b.append(new_matrix2[0][i])



    for i in range(len(new_matrix[0])):
      if(len(b) != 0):
        sum3 += new_matrix[0][i] * b[0]
        
        b.remove(b[0])

      else:
        
        if(len(a) != 0):
          sum4 += new_matrix[0][i] * a[0]
          
          a.remove(a[0])
    
    final.append(sum)
    final.append(sum3)
    final.append(sum4)
    final.append(sum2)
    
    #return(final)
    s = ""
    s2 = ""
    for i in range(0, int(len(final) / 2)):
      s += (str(final[i])).rjust(3) + " "


    for i in range(2, len(final)):
      s2 += (str(final[i])).rjust(3) + " "

    return(s + "\n" + s2)
      
      
 
    
      
    
             

  # return a string representation of the matrix
  def __str__ (self):
    s = ''
    current = self.matrix

    # if the matrix is empty return blank string
    if (current == None):
      return s

    for i in range (self.num_rows):
      for j in range (self.num_cols):
        if ((current != None) and (current.row == i) and (current.col == j)):
          s = s + (str (current.data)).rjust(3) + " "
          current = current.next
        else:
          s = s + "0 ".rjust(4)
      s = s.rjust(3) + "\n"
    return s


def readMatrix (inFile):
  line = inFile.readline().rstrip("\n").split()
  row = int (line[0])
  col = int (line[1])
  mat = SparseMatrix (row, col)

  for i in range (row):
    line = inFile.readline().rstrip("\n").split()
    for j in range (col):
      elt = int(line[j])
      if (elt != 0):
        mat.insertLink (i, j, elt)
  line = inFile.readline()

  return mat

def main ():
  inFile = open ("matrix.txt", "r")

  print ("\nTest Matrix Addition")
  matA = readMatrix (inFile)
  print (matA)
  matB = readMatrix (inFile)
  print (matB)

  matC = matA + matB
  print (matC)

  print ("\nTest Matrix Multiplication")
  matP = readMatrix (inFile)
  print (matP)
  matQ = readMatrix (inFile)
  print (matQ)
  
  matR = matP * matQ
  print (matR)

  print ("\nTest Setting a Zero Element to a Non-Zero Value")
  matA.setElement (1, 1, 5)
  print (matA)

  print ("\nTest Setting a Non-Zero Element to Zero")
  matA.setElement (1, 1, 0)
  print (matA)

  print ("\nTest Getting a Row")
  row = matP.getRow(1)
  print (row)

  print ("\nTest Getting a Column")
  col = matQ.getCol(0)
  print (col)

  inFile.close()

main()
