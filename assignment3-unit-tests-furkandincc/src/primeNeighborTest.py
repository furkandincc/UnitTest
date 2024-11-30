import unittest
import primeNeighbor as pn

class PrimeNeighborTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    """
    def test_lower_bound(self):
        actualResult = pn.primeNeighbor(upperBound=2)
        expectedResult = None 
        self.assertEqual(expectedResult, actualResult)

    def test_prime_number(self):
        actualResult = pn.primeNeighbor(upperBound=37)
        expectedResult = 35  
        self.assertEqual(expectedResult, actualResult)

    def test_non_prime_number(self):
        actualResult = pn.primeNeighbor(upperBound=14)
        expectedResult = 11  
        self.assertEqual(expectedResult, actualResult)

    def test_large_number(self):
        actualResult = pn.primeNeighbor(upperBound=250)
        expectedResult = 247  
        self.assertEqual(expectedResult, actualResult)
    """
    def test_non_number(self):
        actualResult = pn.primeNeighbor(upperBound= "Furkan")
        expectedResult = 2  
        self.assertEqual(expectedResult, actualResult)

if __name__ == '__main__':
    unittest.main()
