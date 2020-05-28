class User:
    def __init__(self, info):
        self.info = info
        self.id = info.get('id', None)
        self.login = info.get('login', None)
        self.password = info.get('pass', None)
        self.role = info.get('role', None)
        self.status = info.get('status', None)
        self.registration_date = info.get('registration_date', None)
        self.id_passport = info.get('id_passport', None)
        self.name1 = info.get('name1', None)
        self.name2 = info.get('name2', None)
        self.name3 = info.get('name3', None)
        self.block_begin = info.get('block_begin', None)
        self.block_end = info.get('block_end', None)
        self.model = info.get('model', None)
        self.car_number = info.get('car_number', None)
        self.rating = info.get('driver_rating', 0) if info.get('rating', 0) is not None else 0
        self.series = info.get('series', None)
        self.number = info.get('number', None)
        self.gender = info.get('gender', None)
        self.date_experation = info.get('date_experation', None)
        self.date_receiving = info.get('date_receiving', None)
        self.identification_number = info.get('identification_number', None)

