import property

class Housing(property.Property):
    def __init__(self, title=None, price=None, area=None, bedrooms=None, bathrooms=None):
        
        self.__bedrooms = bedrooms # private
        self.__bathrooms = bathrooms # private
        self._property_type = 'house' # protected
        self.price = price

    def get_bedrooms(self):
        return self.__bedrooms

    def get_bathrooms(self):
        return self.__bathrooms

    def get_price(self, format=False):
        return self.price if not format else 'UGX '+str(self.price)
    