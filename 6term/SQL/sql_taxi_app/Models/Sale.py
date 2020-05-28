class Sale:
    def __init__(self, info):
        self.info = info
        self.id = info.get('id', None)
        self.id_address_from = info.get('id_address_from', None)
        self.id_address_to = info.get('id_address_to', None)
        self.date = info.get('date', None)
        self.date1 = info.get('date1', None)
        self.cost = info.get('cost', None)
        self.name1 = info.get('name1', None)
        self.name2 = info.get('name2', None)
        self.name3 = info.get('name3', None)


