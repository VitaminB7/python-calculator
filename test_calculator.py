import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        # Add the following test methods to the TestCalculator class:
        # add()	2 test cases 
        self.assertEqual(self.calc.add(100, 0), 100)
        self.assertEqual(self.calc.add(-10, 20), 10)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        # subtract()	2 test cases
        self.assertEqual(self.calc.subtract(4,2),2)
        self.assertEqual(self.calc.subtract(-5,1),-6)
        self.assertEqual(self.calc.subtract(-5,-5),0)
        self.assertEqual(self.calc.subtract(0,-2),2)

    def test_multiply(self):
        # multiply()	2 test cases
        self.assertEqual(self.calc.multiply(5,5),25)
        self.assertEqual(self.calc.multiply(-5,4),-20)
        self.assertEqual(self.calc.multiply(5,-4),-20)
        self.assertEqual(self.calc.multiply(-5,-4),20)
        self.assertEqual(self.calc.multiply(5,0),0)
        self.assertEqual(self.calc.multiply(0,5),0)
        self.assertEqual(self.calc.multiply(0,-5),0)

    def test_divide(self):
        # divide()	2 test cases
        self.assertEqual(self.calc.divide(50,10),5)
        self.assertEqual(self.calc.divide(-50,10),-5)
        self.assertEqual(self.calc.divide(50,-10),-5)
        self.assertEqual(self.calc.divide(-50,-10),5)
        self.assertEqual(self.calc.divide(50,0),"undefined")
        self.assertEqual(self.calc.divide(0,50),0)
        self.assertEqual(self.calc.divide(0,-50),0)
        self.assertEqual(self.calc.divide(1,1),1)
        self.assertEqual(self.calc.divide(-1,1),-1)
        self.assertEqual(self.calc.divide(-1,-1),1)
        self.assertEqual(self.calc.divide(5,2),2)

    def test_modulo(self):
        # modulo()	2 test cases
        self.assertEqual(self.calc.modulo(23,23),0)
        self.assertEqual(self.calc.modulo(23,3),2)
        self.assertEqual(self.calc.modulo(-7,3),2)
        self.assertEqual(self.calc.modulo(7,-3),"undefined")
        self.assertEqual(self.calc.modulo(-7,0),"undefined")
    

if __name__ == '__main__':
    unittest.main()