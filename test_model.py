import unittest, housing, land
from property import Property

class PropertyTest(unittest.TestCase):
    def test_initializes_child(self):
        my_house = housing.Housing(2, 4)
        my_land = land.Land()
        self.assertTrue(isinstance(my_house, housing.Housing))
        self.assertTrue(isinstance(my_land, land.Land))
        
    def test_inheritance(self):
        my_house = housing.Housing(2, 4)
        my_land = land.Land()
        self.assertTrue(isinstance(my_house, Property))
        self.assertTrue(isinstance(my_land, Property))
    
    def test_polymorphism(self):
        my_property = Property()
        my_house = housing.Housing('House in Kampala', 200000, 5000, 3, 2)
        my_land = land.Land('Land in Mukono', 7000000, 10000)
        
        self.assertEqual('property', my_property.get_type())
        self.assertEqual('land', my_land.get_type())
        self.assertEqual('house', my_house.get_type())
        self.assertEqual('UGX 200000', my_house.get_price(format=True))
        self.assertEqual(200000, my_house.get_price())
    
    def test_encapsulation(self):
        my_house = housing.Housing('House in Kampala', 200000, 5000, 3, 2)
        my_land = land.Land('Land in Mukono', 7000000, 10000)

        with self.assertRaises(AttributeError):
            my_house.__bedrooms
            my_house.__bathrooms
        self.assertEqual('land', my_land.get_type())
        self.assertEqual(3, my_house.get_bedrooms())
        self.assertEqual(2, my_house.get_bathrooms())
    