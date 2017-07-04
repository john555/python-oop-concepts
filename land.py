import property

class Land(property.Property):
    def __init__(self, title=None, price=None, area=None):
        
        #super()
        self.property_type = 'land'

