
class Property(object):
    def __init__(self, property_type=None, title=None, price=None, area=None):

        self.title = title
        self.property_type = property_type
        self.price = price
        self.area = area
        self._is_listed = False
    
    def get_area(self):
        return self.area

    def is_listed(self):
        return self._is_listed