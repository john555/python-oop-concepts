import property

class Land(property.Property):
    def __init__(self, title=None, price=None, area=None):
        
        self._property_type = 'land'
    
    def get_type(self):
        return self._property_type
    