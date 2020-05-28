class Address:
    def __init__(self, info):
        self.info = info
        self.id = info.get('id', None)
        self.country = info.get('country', None)
        self.city_type = info.get('city_type', None)
        self.city = info.get('city', None)
        self.region = info.get('region', None)
        self.district = info.get('area', None)
        self.street_type = info.get('street_type', None)
        self.street = info.get('street', None)
        self.house = info.get('house', None)
        self.building = info.get('building', None)
        self.flat = info.get('flat', None)


