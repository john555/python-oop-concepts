import property

class Housing(property.Property):
    def __init__(self, bedrooms=None, bathrooms=None):
        """constructor"""
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
