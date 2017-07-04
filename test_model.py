import unittest, property, housing, land

class PropertyTest(unittest.TestCase):
    def test_initializes_child(self):
        my_housing = housing.Housing(2, 4)
        my_land = land.Land()
        self.assertTrue(isinstance(my_housing, housing.Housing))
        self.assertTrue(isinstance(my_land, land.Land))
        
    def test_inheritance(self):
        my_housing = housing.Housing(2, 4)
        my_land = land.Land()
        self.assertTrue(isinstance(my_housing, property.Property))
        self.assertTrue(isinstance(my_land, property.Property))
    
    def test_polymorphism(self):
        my_housing = housing.Housing('House in Kampala', 200000, 5000, 3, 2)
        my_land = land.Land('Land in Mukono', 7000000, 10000)
        #self.assertEqual()
        
    
    def test_encapsulation(self):
        my_house = housing.Housing('House in Kampala', 200000, 5000, 3, 2)
        my_land = land.Land('Land in Mukono', 7000000, 10000)

        with self.assertRaises(AttributeError):
            my_land.__property_type
            my_house.__bedrooms
            my_house.__bathrooms
        self.assertEqual('land', my_land.get_type())
        self.assertEqual(3, my_house.get_bedrooms())
        self.assertEqual(2, my_house.get_bathrooms())
    