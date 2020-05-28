class PaymentCard:
    def __init__(self, info):
        self.info = info
        self.id = info.get('id_credit_card', None)
        self.name = info.get('name', None)
        self.card_number = info.get('card_number', None)
        self.expiration_date = info.get('expiration_date', None)
        self.security_code = info.get('security_code', None)
