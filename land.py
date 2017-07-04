import property

class Land(property.Property):
    def __init__(self, title=None, price=None, area=None):
        
        self._property_type = 'land'
        self.price = price
    
    def get_type(self):
        return self._property_type

    def get_price(self, format=False):
        return self.price if not format else 'UGX '+str(self.price)
    