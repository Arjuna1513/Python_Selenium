from ddt import ddt, data, unpack
import unittest
@ddt
class DataDriven(unittest.TestCase):

    @data((1,2),(3,4),(5,6))
    @unpack
    def test_add(self, arg1, arg2):
        print(arg1 + arg2)
