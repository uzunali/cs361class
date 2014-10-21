__author__ = 'aliuzun'

import unittest



class MyTest(unittest.TestCase):

    def firstCheck(self):
        self.assertEqual(2,2)

    def new_func(self,data):
        num=0
        for i in data:
            if num<i:
                num==i
        return num



    """Elhamdulillah Muslumaniz"""



# if __name__= '__main__':
#     unittest.main()

