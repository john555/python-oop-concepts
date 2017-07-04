
class Property(object):
    def __init__(self, property_type=None, title=None, price=None, area=None):

        self.title = title
        self.property_type = property_type
        self.price = price
        self.area = area
        self._property_type = 'property'
    
    def get_type(self):
        return self._property_type