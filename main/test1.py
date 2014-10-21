__author__ = 'aliuzun'

import unittest



class MyTest(unittest.TestCase):

    def firstCheck(self):
        self.assertEqual(2,2)

    def new_func(self,data):
        num=0
        buffer = []
        data = [2,3,45,67,123,123,45,6,7,9,10,8]
        for i in range(sum(data)):
            for j in range(i):
                print j
                buffer.append(j)
        return num

    def deneme(self,data,look):
        lo,hi=0,len(data)
        mid=(lo+hi)/2
        return data[mid],look

    """Elhamdulillah Muslumaniz"""



# if __name__= '__main__':
#     unittest.main()

