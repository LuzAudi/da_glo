class Matrix:

    #Init an empty matrix
    rows = 0
    columns = 0
    matrix = []

    def __init__(self):
        self.matrix = []
        self.rows = 0
        self.columns = 0

    def create_matrix(self,matrix):
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        self.matrix =  [[matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]

    def input_matrix(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[float(input("Row {},Column {}: ".format(row, col))) for col in range(columns)] for row in range(rows)]
        self.show_matrix()        
        return self.matrix

    #method to show the matrix on screen as a matrix
    def show_matrix(self):
        for row in self.matrix:
            print(row)
    

    def clear(self):
        self.matrix = []


    def get_value_of_position(self, i, j):
        return self.matrix[i][j]


    #Matrices addition
    def __add__(self,other):
        if self.rows != other.rows and self.columns != other.columns :
            raise ValueError("Addition requires matrices of the same order")
        else: 
            result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns)]
                for i in range(self.rows)]
        
            for r in result: 
                print(r) 


    #Scalar multiplication
    def scalar_product(self,x):
        result = [[self.matrix[i][j] * x for j in range(self.columns)] for i in range(self.rows)]
        return result


    #Matrix multiplication
    def product(self,m):
        if self.columns is not m.rows: 
            raise Exception('Number of rows and number of columns do not match')
        for i in range(self.rows):
            row = []
            for j in range(m.columns):
                add = 0
                for c in range(self.columns):
                    add += self.get_value_of_position(i,c) * m.get_value_of_position(c,j)
                row.append(add)
            yield row
    

    # Matrix transpose
    def transpose(self,m):
        result = [[m[j][i] for j in range(self.columns)] for i in range(self.rows)]
        return result

    
    def get_matrix_minor(self,m,i,j):
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
    
    #Matrix Determinant 
    def determinant_matrix(self,m):
        if len(m) == 1: 
            return m[0][0]
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        
        det = 0
        for c in range(len(m)):
            det += ((-1)**c)*m[0][c]*self.determinant_matrix(self.get_matrix_minor(m,0,c))
        return det
    

    # Adjugate matrix
    def adjugate_matrix(self,m):
        cofactors = []
        for i in  range(self.rows):
            cofactorRow = []
            for j in range(self.rows):
                minor = self.get_matrix_minor(m,i,j)
                cofactorRow.append(((-1)**(i+j)) * self.determinant_matrix(minor))
            cofactors.append(cofactorRow)
        print([[cofactors[r][c] for r in range(len(cofactors))] for c in range(len(cofactors))])

    # Inverted matrix
    def inverted_matrix(self,m):
        det = self.determinant_matrix(m)
        
        cofactors = []
        for i in  range(self.rows):
            cofactorRow = []
            for j in range(self.rows):
                minor = self.get_matrix_minor(m,i,j)
                cofactorRow.append(((-1)**(i+j)) * self.determinant_matrix(minor))
            cofactors.append(cofactorRow)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c]/det
        cofactors = self.transpose(cofactors)
        return cofactors

  
    # A method to obtain a matrix row
    def get_row(self, n):
        print(self.matrix[n])
        return self.matrix[n]

    # A method to obtain a matrix row
    def get_col(self, n):
        column_items = []
        i = 0
        while i < self.rows:
            column_items.append(self.matrix[i][n])
            i += 1
        
        for item in column_items:
            print(item)
        return column_items    


# a = [[5,7,5],[9,4,4],[7,8,1]]
# b = [[4,7],[1,8]]

# m1 = Matrix()
# m2 = Matrix()
# m1.create_matrix(a)
# m2.create_matrix(b)
#m1.adjugate_matrix(m1.matrix)        
# m2.adjugate_matrix(m2.matrix)


# for e in m2.transpose(m2.matrix):
#     print(e)

# for e in m1.inverted_matrix(m1.matrix):
#     print(e)
