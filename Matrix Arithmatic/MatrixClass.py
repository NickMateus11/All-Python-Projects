class matrix():
    def __init__(self,rawInput):
        self.raw_matrix = rawInput
        self.create()
        self.show()
    def create(self):
        self.aug_matrix = self.raw_matrix[self.raw_matrix.index('[')+1:self.raw_matrix.index(']')]
        self.aug_matrix = self.aug_matrix.split(';')
        for i in range(len(self.aug_matrix)):
            self.aug_matrix[i] = self.aug_matrix[i].split(',')
            for j in range(len(self.aug_matrix[i])):
                self.aug_matrix[i][j] = self.format(self.aug_matrix[i][j])
        self.name = self.raw_matrix[0:self.raw_matrix.index('=')].strip()
    def format(self,num):
        return (int(num) if float(num)%1==0 else float(format(num,'.2f')))
    def show(self):
        print('{} = \n'.format(self.name),end = '')        
        for row in self.aug_matrix:
            print(end='\t')
            for entry in row:
                print(entry, end=' '*(6-len(str(entry))))
            print(end='\n\n')
    def row_swap(self,R1,R2):
        self.aug_matrix[R1-1],self.aug_matrix[R2-1] = self.aug_matrix[R2-1],self.aug_matrix[R1-1]
    def row_mult(self,R,scalar):
        for j in range(len(self.aug_matrix[R-1])):
            self.aug_matrix[R-1][j] = self.format(self.aug_matrix[R-1][j] * scalar)
        return R  
    def row_add(self,R1,R2):
        for j in range(len(self.aug_matrix[R1-1])):
            self.aug_matrix[R1-1][j] = self.format(self.aug_matrix[R1-1][j] + self.aug_matrix[R2-1][j])
        return R1
            

A = matrix('A = [1,2,3,4;5,6,7,8;2,23,53,7]')

A.row_add(2,A.row_mult(1,-5))
A.row_mult(1,-1/5)
A.row_add(3,A.row_mult(1,-2))
A.row_mult(1,-1/2)
A.row_add(A.row_mult(3,4),A.row_mult(2,19))
A.row_mult(2,-1/76)
A.row_mult(3,1/36)
A.row_add(1,A.row_mult(2,-2))
A.row_mult(2,-.5)
A.row_add(1,3)
A.row_mult(1,-1)
A.row_add(1,3)
A.row_mult(1,-1)
A.row_add(1,3)
A.row_add(2,A.row_mult(3,-2))
A.row_mult(3,-.5)
A.show()
