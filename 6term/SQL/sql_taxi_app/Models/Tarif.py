class Tarif:
    def __init__(self, info):
        self.info = info
        self.id = info.get('id', None)
        self.name = info.get('tarif', None)
        self.city = info.get('city', None)
        self.no_city = info.get('no_city', None)