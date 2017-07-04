
class Property(object):
    def __init__(self, id=None, property_type=None, title=None, description=None, price=0.0, area=None):
        """"""
        self.id = id
        self.title = title
        self.property_type = property_type
        self.description = description
        self.price = price
        self.coordinates = []
        self.area = area

    def set_gps_coordinates(self, coordinates):
        self.coordinates = coordinates
    