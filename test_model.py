import unittest, property, housing, land

class Property(unittest.TestCase):
    def test_initializes_child(self):
        my_housing = housing.Housing(2, 4)
        my_land = land.Land()
        self.assertTrue(isinstance(my_housing, housing.Housing))
        self.assertTrue(isinstance(my_land, land.Land))
        

