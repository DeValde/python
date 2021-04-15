import unittest
from ipynb.fs.full.Tasks1 import speed,helpCauchy,leapYear



class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(speed(50,25),2)
        self.assertEqual(speed(30,10),3)
    def test2(self):
        self.assertEqual(helpCauchy(3,10),30)
        self.assertEqual(helpCauchy(2,12),24)
    def test3(self):
        self.assertEqual(leapYear(366),True)
        self.assertEqual(leapYear(365),False)
        self.assertEqual((leapYear(0)),False)



if __name__ == '__main__':
    unittest.main()
