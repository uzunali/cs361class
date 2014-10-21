__author__ = 'aliuzun'

import unittest



class MyTest(unittest.TestCase):

    def firstCheck(self):
        self.assertEqual(2,2)

    def new_func(self,data):
        num=10
        for i in data:
            if num>i:
                num==i
        return num

    def deneme(self,data,look):
        lo,hi=0,len(data)
        mid=(lo+hi)/2
        return data[mid],look

    """Elhamdulillah Muslumaniz"""



# if __name__= '__main__':
#     unittest.main()

