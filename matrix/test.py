from matrix import Matrix
import unittest

class MatrixTests(unittest.TestCase):
    def test_add(self):
        a = [[5,7,8],[9,4,14],[3,1,2],[1,7,1]]
        b = [[4,3,0],[11,14,14],[32,13,2],[11,7,1]]

        m1 = Matrix()
        m2 = Matrix()

        m1.create_matrix(a)
        m2.create_matrix(b)

        m3 = m1 + m2
        self.assertTrue(m3 == [[9,10,8],[20,18,28],[35,14,4],[12,14,2]])
    
    def test_mul(self):
        m1 = Matrix()
        m1.create_matrix([[3,1],[4,5],[8,1]])
        m2 = Matrix()
        m2.create_matrix([[1,1],[4,8]]) 
        m3 = m1.product(m2)
        self.assertTrue(m3 == [[7,11],[24,44],[12,16]])
    
    def test_scalar(self):
        m1 = Matrix()
        m1.create_matrix([1,4,2],[2,4,1])
        m3 = m1.scalar_product(2)
        self.assertTrue(m3 == [[2,8,4],[4,8,2]])
    
    def test_det(self):
        m1 = Matrix()
        m1.create_matrix([1,4,2],[2,4,1])
        m2 = m1.determinant_matrix(m1.matrix)
        self.assertTrue(m2 == 2)

        
if __name__ == "__main__":
    unittest.main()