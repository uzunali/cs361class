__author__ = 'aliuzun'

import unittest



class MyTest(unittest.TestCase):

    def firstCheck(self):
        self.assertEqual(2,2)

    def new_func(self,data):
        for i in data:
            print i



# if __name__= '__main__':
#     unittest.main()

