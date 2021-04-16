import unittest
import math
import import_ipynb
from Task2 import  minifizzbuzz,helpVlad,exist,area,sqEqu


def Geron(a,b,c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
def circle(r):
    return 3*r^2
def Discr(a,b,c):
    D = b*b-4*a*c
    if D < 0:
        raise Exception("D<0")
    elif D == 0:
        return (-b + math.sqrt(D)) / 2 / a
    else:
        return (((-b + math.sqrt(D)) / 2 / a), ((-b - math.sqrt(D)) / 2 / a))



class MyTestCase(unittest.TestCase):
    def test_miniFizzBuzz(self):
        self.assertEqual(minifizzbuzz(5),"fizz")
        self.assertEqual(minifizzbuzz(7),"buzz")
        self.assertEqual(minifizzbuzz(35),"fizzbuzz")
        self.assertEqual(minifizzbuzz(3),3)
    def test_helpVlad(self):
        self.assertEqual(helpVlad(4),3.5)
        self.assertEqual(helpVlad(0),0)
        self.assertEqual(helpVlad(-6),6)
    def test_exist(self):
        self.assertEqual(exist(3,4,5),True)
        self.assertEqual(exist(1,5,10),False)
        self.assertEqual(exist(10,25,3),False)
        self.assertEqual(exist(2,5,3),True)
    def test_area(self):
        self.assertEqual(area('1'),Geron(int(input()),int(input()),int(input())))
        self.assertEqual(area('2'),int(input())*int(input()))
        self.assertEqual(area('3'),circle(int(input())))
        with self.assertRaises(Exception) as context:
            area('4')
    def test_sqEqu(self):
        self.assertAlmostEqual(sqEqu(),Discr(float(input()),float(input()),float(input())),places=6) # проверить для трех случаев

if __name__ == '__main__':
    unittest.main()
