from p1 import *
import unittest
from random import randint
import time

class Tests(unittest.TestCase):

    '''
    def test_subtract(self):
        print("Running subtraction tests.")
        for i in range(0, 501):
            for j in range(0, 501):
                self.assertEqual(i - j, subtract(i, j))
            print("    Finished i = ", i, " subtraction set")
        print("Finished subtraction tests.")
    '''
    '''
    def test_Divide(self):
        print("Running division tests.")
        for i in range(1, 501):
            for j in range(1, 501):
                self.assertEqual((i // j, i % j), Divide(i, j))
            print("    Finished i = ", i, " division set")
        print("Finished division tests.")
    '''
    '''
    def test_exp(self):
        print("Running exponent tests.")
        for i in range(1, 50):
            for j in range(1, 50):
                self.assertEqual(i**j, bin2dec(exp(dec2bin(i), dec2bin(j))))
            print("    Finished i = ", i, " exponent set")
        print("Finished division tests.")
    '''
    '''
    def test_problem1Calc(self):
        print("Running problem1Calc tests.")
        for i in range(0, 10):
            a = randint(0, 100)
            b = randint(0, 100)
            c = randint(0, 100)
            d = randint(0, 100)
            print("    Testing ", a, "^", b, " - ", c, "^", d) 
            start = time.time()
            ourResult = problem1Calc(a, b, c, d)
            end = time.time()
            print("Got an answer of ", ourResult)
            self.assertEqual((a**b) - (c**d), ourResult)
            
            print("    Finished test. Time taken: ", end - start)
        print("Finished problem1Calc tests.")
    '''
    '''
    def test_problem2Calc(self):
        print("Running problem2Calc tests.")
        for i in range(0, 10):
            a = randint(0, 1000)
            b = randint(0, 1000)
            c = randint(0, 1000)
            d = randint(0, 1000)
            print("    Testing ", a, "^", b, " / ", c, "^", d) 
            start = time.time()
            (ourQuotient, ourRemainder) = problem2Calc(a, b, c, d)
            end = time.time()
            print("Got a quotient of ", ourQuotient, " and a remainder of ", ourRemainder)
            actualQuotient = (a**b)//(c**d)
            actualRemainder = (a**b)%(c**d)
            self.assertEqual((actualQuotient, actualRemainder), (ourQuotient, ourRemainder))
            
            print("    Finished test. Time taken: ", end - start)
        print("Finished problem1Calc tests.")
    '''
    '''
    def test_problem3Calc(self):
        #If you run this code, you have to manually verify the results yourself.
        print("Running problem3Calc tests.")
        for a in range(1, 10):
            start = time.time()
            (numerator, denominator) = problem3Calc(a)
            result = numerator / denominator
            end = time.time()
            print("Got a numerator of ", numerator, " and a denominator of ", denominator)
            actualResult = 0
            for i in range(1, a + 1):
                actualResult = actualResult + (1.0/i)
                
            self.assertTrue(True)
            
            print("    Finished test i = ", i, ". Time taken: ", end - start)
        print("Finished problem1Calc tests.")
    '''

            

if __name__ == '__main__':
    unittest.main()
    



    
