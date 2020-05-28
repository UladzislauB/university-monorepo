import pymysql
import pymysql.cursors
from pymysql import MySQLError

from Models.Address import Address
from Models.PaymentCard import PaymentCard
from Models.PromoCode import PromoCode
from Models.Sale import Sale
from Models.Tarif import Tarif
from Models.User import User


class DBHelper:
    def __init__(self):
        self.connect = pymysql.connect(
            host='34.107.9.48',
            user='student',
            password='student',
            db='sql_taxi',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connect.cursor()

    def login_user(self, login, password):
        self.cursor.execute(f"CALL login_credential('{login}', '{password}');")
        result = self.cursor.fetchone()
        return result['result']

    def get_user(self, login):
        self.cursor.execute(f"CALL get_credential('{login}');")
        user = User(self.cursor.fetchone())
        return user

    def insert_user(self, login, password, name1, name2, name3, role):
        error = None
        try:
            self.cursor.execute(
                f"CALL insert_credential('{name1}','{name2}','{name3}','{login}','{password}','{role}');")
            self.connect.commit()
        except MySQLError as e:
            if e.args[0] == 1062:
                error = "User with this username is already registered"
            else:
                error = e.args[1]
        finally:
            return error

    def insert_passport(self, id, series, number, identification_number, gender, date_experation, date_receiving):
        self.cursor.execute(
            f"CALL insert_passport({id} ,'{series}','{number}','{identification_number}','{gender}',"
            f" '{date_experation}', '{date_receiving}');")
        self.connect.commit()

    def insert_car(self, id, model, number):
        self.cursor.execute(f"CALL insert_car({id}, '{model}', '{number}')")
        self.connect.commit()

    def insert_address(self, country, city_type, city, region, district, street_type, street, house, building, flat):
        self.cursor.execute(
            f"CALL insert_address('{country}', '{region}', '{district}', '{street}', '{city}',"
            f" '{street_type}', '{city_type}', '{house}', '{building}', '{flat}')"
        )
        self.connect.commit()
        id = self.cursor.fetchone()['id']
        return id

    def get_address(self, id):
        self.cursor.execute(f"CALL get_address('{id}');")
        address = Address(self.cursor.fetchone())
        return address

    def insert_card(self, login, name, card_number, expiration_date, security_code):
        self.cursor.execute(f"CALL insert_credit_card({id}, '{name}', {card_number}, '{expiration_date}',"
                            f" {security_code});")
        self.connect.commit()

    def get_cards(self, login):
        self.connect.commit()
        self.cursor.execute(f"CALL get_credit_card('{login}');")
        result = self.cursor.fetchall()
        cards = []
        for c in result:
            cards.append(PaymentCard(c))
        return cards

    def get_tariffs(self):
        self.connect.commit()
        self.cursor.execute(f"CALL get_tariffs();")
        result = self.cursor.fetchall()
        tariffs = []
        for t in result:
            tariffs.append(Tarif(t))
        return tariffs

    def check_promo(self, promo):
        self.connect.commit()
        self.cursor.execute(f"CALL check_promo('{promo}');")
        result = self.cursor.fetchone()
        return result['discount_procent']

    def set_driver_status(self, login, type):
        self.cursor.execute(f"CALL set_driver_status('{login}', '{type}')")
        self.connect.commit()

    def get_free_driver(self):
        self.connect.commit()
        self.cursor.execute(f"CALL get_free_driver();")
        result = self.cursor.fetchone()
        if result is None:
            return 0
        else:
            return result['id']

    def order_taxi(self, login_client, login_driver, id_payment_card, if_tariff, cost, address_from, address_to):
        print(f"CALL order_taxi('{login_client}', {if_tariff}, {id_payment_card}, '{login_driver}', {cost}, {address_from}, {address_to})")
        self.cursor.execute(f"CALL order_taxi('{login_client}', {if_tariff}, {id_payment_card}, '{login_driver}', {cost}, {address_from}, {address_to})")
        self.connect.commit()
        result = self.cursor.fetchone()
        return result['id_s']

    def end_order_taxi(self, id, comment, raiting):
        self.cursor.execute(f"CALL end_order_taxi({id}, '{comment}', {raiting})")
        self.connect.commit()

    def get_all_user(self, name1, name2, name3, role, status):
        self.connect.commit()
        self.cursor.execute(
            f"CALL get_all_users('{name1}', '{name2}', '{name3}', '{role}', '{status}')")
        result = self.cursor.fetchall()
        users = []
        for u in result:
            users.append(User(u))
        return users

    def get_all_tariffs(self):
        self.connect.commit()
        self.cursor.execute(
            f"CALL get_all_tariff()")
        result = self.cursor.fetchall()
        tariffs = []
        for t in result:
            tariffs.append(Tarif(t))
        return tariffs

    def get_all_promo_codes(self):
        self.connect.commit()
        self.cursor.execute(
            f"CALL get_all_promo()")
        result = self.cursor.fetchall()
        promo_codes = []
        for p in result:
            promo_codes.append(PromoCode(p))
        return promo_codes

    def insert_tariff(self, tariff, city, no_city):
        self.cursor.execute(f"CALL insert_tariff('{tariff}', {city}, {no_city})")
        self.connect.commit()

    def insert_promo(self, promo, date, discount):
        self.cursor.execute(f"CALL insert_promo('{promo}', '{date}', {discount})")
        self.connect.commit()

    def get_history(self, login):
        self.connect.commit()
        print(login)
        print(f"CALL get_history('{login}')")
        self.cursor.execute(f"CALL get_history('{login}')")
        result = self.cursor.fetchall()
        sales = []
        for s in result:
            sales.append(Sale(s))
        return sales
