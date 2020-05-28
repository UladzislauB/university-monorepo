class PromoCode:
    def __init__(self, info):
        self.info = info
        self.id = info.get('id', None)
        self.promo = info.get('promo', None)
        self.expiration_date = info.get('expiration_date', None)
        self.discount_percent = info.get('discount_percent', None)