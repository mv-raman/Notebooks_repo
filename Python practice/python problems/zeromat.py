
import unittest
import copy
def zeromat(matrix):
    norows=len(matrix)
    nocols=len(matrix[0])
    new_matrix=copy.deepcopy(matrix)

    def nullify(row,col):
        for each1 in range(nocols):
            new_matrix[row][each1]=0
        for each2 in range(norows):
            new_matrix[each2][col]=0


    for eachrow in range(norows):
        for eachcol in range(nocols):
            if(matrix[eachrow][eachcol]==0):
                nullify(eachrow,eachcol)


    return new_matrix





class Test(unittest.TestCase):
    data = [
        ([
             [1, 2, 3, 4, 0],
             [6, 0, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 0, 18, 19, 20],
             [21, 22, 23, 24, 25]
         ], [
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [11, 0, 13, 14, 0],
             [0, 0, 0, 0, 0],
             [21, 0, 23, 24, 0]
         ])
    ]

    def test_zero_matrix(self):
        for [testmatrix,expected] in self.data:
            actual=zeromat(testmatrix)
            self.assertEqual(actual,expected)


if __name__=="__main__":
    unittest.main()