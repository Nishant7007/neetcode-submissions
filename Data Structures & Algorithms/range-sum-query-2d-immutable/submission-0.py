class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.n_rows = len(self.matrix)
        self.n_cols = len(self.matrix[0])

        
        self.sum_matrix = [[0]*self.n_cols for i in range(self.n_rows)]
        self.sum_matrix[0][0] = self.matrix[0][0]

        for i in range(self.n_rows):
            self.sum_matrix[i][0] = self.matrix[i][0]

        for i in range(0, self.n_rows):
            for j in range(1, self.n_cols):
                self.sum_matrix[i][j] = self.sum_matrix[i][j-1] + self.matrix[i][j]

        for i in range(1, self.n_rows):
            for j in range(0, self.n_cols):
                self.sum_matrix[i][j] = self.sum_matrix[i-1][j] + self.sum_matrix[i][j]


        # for i in range(self.n_rows):
        #     print(self.matrix[i])
       
        # print('*'*100)
        # for i in range(self.n_rows):
        #     print(self.sum_matrix[i])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        large_sum = self.sum_matrix[row2][col2]
        
        left = 0
        upper = 0
        diag = 0

        if(col1>0):
            left = self.sum_matrix[row2][col1-1]
        
        if(row1>0):
            upper = self.sum_matrix[row1-1][col2]
        
        if(row1>0 and col1>0):
            diag = self.sum_matrix[row1-1][col1-1]

        return large_sum - (left+upper-diag)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)