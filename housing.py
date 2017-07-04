import property

class Housing(property.Property):
    def __init__(self, title=None, price=None, area=None, bedrooms=None, bathrooms=None):
        
        super()
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.property_type = 'housing'
        