import property

class Land(property.Property):
    def __init__(self, title=None, price=None, area=None):
        
        #private property
        self.__property_type = 'land'
    
    def get_type(self):
        return self.__property_type
    