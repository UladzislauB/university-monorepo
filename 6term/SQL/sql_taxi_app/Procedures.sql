DELIMITER $$;
CREATE PROCEDURE `login_credential`(IN _log VARCHAR(50), IN _pass VARCHAR(50))
BEGIN
   DECLARE credential_id smallint;
   DECLARE _status VARCHAR(20);
   SELECT id INTO credential_id FROM credentials WHERE login = _log AND pass = _pass;

   IF credential_id IS NOT NULL THEN
      SELECT status INTO _status FROM credentials WHERE id = credential_id;
      IF _status = "Active" THEN
         SELECT 0 as result;
      ELSE
         SELECT 2 as result;
         END IF;
   ELSE
      SELECT 1 as result;
   END IF;
END$$;

DELIMITER $$;
CREATE PROCEDURE `get_all_users`(IN _name1 VARCHAR(64), IN _name2 VARCHAR(64), IN _name3 VARCHAR(64), IN _role VARCHAR(20), IN _status VARCHAR(20))
BEGIN
	SELECT credentials.id, login, role, status, name1, name2, name3, block_end
    FROM credentials
    INNER JOIN names1 on names1.id = credentials.id_name1
    INNER JOIN names2 on names2.id = credentials.id_name2
    INNER JOIN names3 on names3.id = credentials.id_name3
    WHERE
	(name1 LIKE CONCAT('%', _name1, '%')) AND
	(name2 LIKE CONCAT('%', _name2, '%')) AND
	(name3 LIKE CONCAT('%', _name3, '%')) AND
	(role LIKE CONCAT('%', _role, '%')) AND
	(status LIKE CONCAT('%', _status, '%'));
END$$;

DELIMITER $$;
CREATE PROCEDURE `insert_car`(IN _id MEDIUMINT, IN _model VARCHAR(50), IN _number VARCHAR(10))
BEGIN
	IF  NOT EXISTS (SELECT id FROM car WHERE (model, car_number) = (_model, _number)) THEN
        INSERT INTO car
        (model, car_number)
        VALUES (_model, _number);
    END IF;

	UPDATE driver
    SET id_car = (SELECT id FROM car WHERE (model, car_number) = (_model, _number))
    WHERE id_credential = _id;
END$$;

DELIMITER $$;
CREATE PROCEDURE `insert_passport`(IN _id MEDIUMINT, IN _series CHAR(2), IN _number VARCHAR(10),
IN _identification_number VARCHAR(16), IN _gender VARCHAR(10),
IN _date_experation DATETIME, IN _date_receiving DATETIME)
BEGIN
	INSERT INTO pasport
	(series, number, identification_number, gender, date_experation, date_receiving)
	VALUES (_series, _number, _identification_number, _gender, _date_experation, _date_receiving);

    UPDATE driver
    SET id_passport = (SELECT id FROM pasport WHERE identification_number = _identification_number)
    WHERE id_credential = _id;
END$$;

DELIMITER $$;
CREATE PROCEDURE `set_driver_status`(IN _login VARCHAR(45), IN _status VARCHAR(10))
BEGIN
	DECLARE id_d MEDIUMINT;
	SELECT driver.id INTO id_d FROM driver
	INNER JOIN credentials ON credentials.id = driver.id_credential
	WHERE login = _login;

	UPDATE driver SET status = _status
    WHERE id = id_d;
END$$;

DELIMITER $$
CREATE PROCEDURE `insert_address`(IN _country VARCHAR(45), IN _region VARCHAR(45), IN _area VARCHAR(45), IN _street VARCHAR(45), IN _city VARCHAR(45),
IN _street_type VARCHAR(20), IN _city_type VARCHAR(20), IN _house VARCHAR(5),  IN _building VARCHAR(1),  IN _flat VARCHAR(5))
BEGIN
	INSERT IGNORE INTO country(country) VALUES (_country);
    INSERT IGNORE INTO region(region) VALUES (_region);
    INSERT IGNORE INTO arear(area) VALUES (_area);
    INSERT IGNORE INTO street(street) VALUES (_street);
    INSERT IGNORE INTO city(city) VALUES (_city);

    INSERT INTO address(id_country, id_region, id_area, is_street, id_city, street_type,city_type, house, building, flat)
	VALUES (
	(SELECT id FROM country WHERE country=_country),
	(SELECT id FROM region WHERE region=_region),
	(SELECT id FROM arear WHERE area=_area),
	(SELECT id FROM street WHERE street=_street),
	(SELECT id FROM city WHERE city=_city),
    _street_type, _city_type, _house, _building, _flat);
    SELECT LAST_INSERT_ID() as id;
END$$


DELIMITER $$
CREATE PROCEDURE `insert_credit_card`(IN _login VARCHAR(45), IN _name VARCHAR(60), IN _card_number BIGINT, IN _expiration_date DATE, IN _security_code SMALLINT)
BEGIN
	DECLARE card_id, id_c MEDIUMINT;
	INSERT INTO credit_cards(name, card_number, expiration_date, security_code)
    VALUES (_name, _card_number, _expiration_date, _security_code);
	SET card_id = LAST_INSERT_ID();

    SELECT customer.id INTO id_c FROM customer
	INNER JOIN credentials ON credentials.id = customer.id_credential
	WHERE login = _login;
    INSERT INTO customer_creditcard(id_customer, id_credit_card)
    VALUES (id_c, card_id);
END$$

DELIMITER $$
CREATE PROCEDURE `get_credit_card`(IN _login VARCHAR(45))
BEGIN
	SELECT * from customer_creditcard
    INNER JOIN credit_cards ON credit_cards.id = customer_creditcard.id_credit_card
    INNER JOIN customer ON customer.id = customer_creditcard.id_customer
    INNER JOIN credentials ON credentials.id = customer.id_credential
    WHERE login = _login;
END$$

DELIMITER $$
CREATE PROCEDURE `get_free_driver`()
BEGIN
	SELECT id from driver WHERE status = "Online" limit 1;
END$$

DELIMITER $$
CREATE DEFINER=`student`@`%` PROCEDURE `check_promo`(IN _promo VARCHAR(45))
BEGIN
	DECLARE promo_id MEDIUMINT;
	DECLARE e_date DATETIME;
    SELECT id, expiration_date INTO promo_id, e_date FROM promocodes WHERE promo = _promo;
    IF promo_id is not NULL THEN
		IF e_date - NOW() > 0 THEN
			SELECT discount_percent FROM promocodes WHERE id = promo_id;
		ELSE
			SELECT -2 as discount_procent;
		END IF;
	ELSE
		SELECT -1 as discount_procent;
    END IF;
END$$

USE `mydb`;
DROP procedure IF EXISTS `order_taxi`;

DELIMITER $$
CREATE DEFINER=`student`@`%` PROCEDURE `order_taxi`(IN _log_customer VARCHAR(45), IN _id_tarif MEDIUMINT, IN _id_payment MEDIUMINT, IN _id_driver MEDIUMINT, IN _cost MEDIUMINT, IN _from MEDIUMINT, IN _to MEDIUMINT)
BEGIN
	DECLARE id_c, id_p MEDIUMINT;
    SELECT customer.id INTO id_c FROM customer
	INNER JOIN credentials ON credentials.id = customer.id_credential
	WHERE login = _log_customer;

    INSERT INTO payment(id_payment_card, cost, date)
    VALUES(_id_payment,_cost, NOW());
    SET id_p = LAST_INSERT_ID();

	INSERT INTO sales(id_customer, id_driver, id_tarif, id_payment, ride_status, date, id_address_from, id_address_to)
    VALUES(id_c, _id_driver, _id_tarif, id_p, 'Active', NOW(), _from, _to);
    SELECT LAST_INSERT_ID() as id_s;
END$$

DELIMITER $$
CREATE DEFINER=`student`@`%` PROCEDURE `end_order_taxi`(IN _id MEDIUMINT, IN _comment VARCHAR(250), IN _raiting MEDIUMINT)
BEGIN
	UPDATE sales SET
    ride_status = 'Finished', comment = _comment, date1 = NOW()
    WHERE id = _id;

    INSERT INTO driver_rating(id_driver, id_cutomer, rating, description)
    VALUES(
    (SELECT id_driver FROM sales WHERE id = _id), (SELECT id_customer FROM sales WHERE id = _id),
    _raiting, _comment);
END$$

DELIMITER $$
CREATE DEFINER=`student`@`%` PROCEDURE `get_history`(IN _login VARCHAR(45))
BEGIN
	DECLARE _role VARCHAR(20);
	SELECT role INTO _role FROM credentials WHERE login = _login;

	SELECT sales.id, id_address_from, id_address_to, sales.date, date1, cost, name1, name2, name3 FROM sales
    INNER JOIN customer on customer.id = sales.id_customer
    INNER JOIN driver on driver.id = sales.id_driver
    INNER JOIN payment on  payment.id = sales.id_payment
    INNER JOIN credentials on  credentials.id =
    (CASE
		WHEN _role = 'Client' THEN customer.id_credential
        WHEN _role = 'Driver' THEN driver.id_credential
	END)
    INNER JOIN names1 on  names1.id = credentials.id_name1
    INNER JOIN names2 on  names2.id = credentials.id_name2
    INNER JOIN names3 on  names3.id = credentials.id_name3
    WHERE login = _login;
END$$

DELIMITER $$
CREATE DEFINER=`student`@`%` PROCEDURE `insert_tariff`(IN _tariff VARCHAR(45), IN _city DOUBLE, IN _no_city DOUBLE)
BEGIN
	INSERT INTO tarif(tarif, city, no_city)
    VALUES(
    _tariff, _city, _no_city);
END$$

DELIMITER $$
CREATE DEFINER=`student`@`%` PROCEDURE `get_all_tariff`()
BEGIN
	SELECT id, tarif, city, no_city
    FROM tarif;
END$$

DELIMITER $$
CREATE DEFINER=`student`@`%` PROCEDURE `get_all_promo`()
BEGIN
	SELECT id, promo, expiration_date, discount_percent
    FROM promocodes;
END$$

DELIMITER $$
CREATE DEFINER=`student`@`%` PROCEDURE `insert_promo`(IN _promo VARCHAR(16), IN _expiration_date DATETIME, IN _discount_percent SMALLINT)
BEGIN
	INSERT IGNORE INTO promocodes(promo, expiration_date, discount_percent)
    VALUES(
    _promo, _expiration_date, _discount_percent);
END$$

DELIMITER $$
CREATE PROCEDURE delete_user(IN _log VARCHAR(45))
BEGIN
	DELETE FROM credentials WHERE login=_log;
END$$

DELIMITER $$
CREATE PROCEDURE set_blocked(IN _s CHAR(10), IN _log CHAR(50), IN _start DATETIME, IN _end DATETIME)
BEGIN
	UPDATE credentials SET
	block_begin = _start, block_end = _end, status = _s
	WHERE login = _log;
 END$$

DELIMITER $$
CREATE PROCEDURE update_role(IN _log VARCHAR(50), IN _user_type VARCHAR(20))
BEGIN
   UPDATE credentials SET
   role = _user_type
   WHERE login = _log;
END$$

LOCK TABLES names1 WRITE;
INSERT IGNORE INTO names1(name1) VALUES ('name1') ;
UNLOCK TABLES;

LOCK TABLES names2 WRITE;
INSERT IGNORE INTO names1(name1) VALUES ('name2') ;
UNLOCK TABLES;

•	Создаём триггер
LOCK TABLE users WRITE, users_backup READ;
UPDATE users SET
password = '{*}', salt = '{*}', role = '{*}',
status = '{*}', block_begin = '{*}',
block_end = '{*}', id_name1 = {*},
id_name2 = {*}, id_name3 = {*},
id_personal_info = {*}
WHERE id = '{*}'
DELETE FROM credentials_backup
WHERE user_id = {*}
ORDER BY change_date DESC limit 1


DELIMITER $$
CREATE PROCEDURE undo_user_backup_procedure()
BEGIN
	DECLARE backup_id smallint;
	DECLARE backup_type VARCHAR(20);
    START TRANSACTION;
    SET @disable_backup_trigger = 1;
    SELECT id, operation_type INTO backup_id, backup_type FROM users_backup ORDER BY change_date DESC limit 1;
	IF backup_type = 'Update' THEN
		UPDATE users
		INNER JOIN users_backup
		ON users.id = users_backup.user_id
		SET users.password = users_backup.password, users.salt = users_backup.salt, users.role = users_backup.role,
		users.status = users_backup.status, users.block_begin = users_backup.block_begin, users.block_end = users_backup.block_end,
		users.id_name1 = users_backup.id_name1, users.id_name2 = users_backup.id_name2, users.id_name3 = users_backup.id_name3,
		users.id_personal_info = users_backup.id_personal_info
		WHERE users_backup.id = backup_id;
	ELSE
		INSERT INTO OnlineStoreDB.users
		(id, login, password, salt, role, status, block_begin, block_end,
		registration_date, id_name1, id_name2, id_name3, id_personal_info)
		SELECT user_id, login, password, salt, role, status, block_begin, block_end,
		registration_date, id_name1, id_name2, id_name3, id_personal_info FROM users_backup WHERE id = backup_id;
	END IF;
    DELETE FROM users_backup WHERE id = backup_id;
    SET @disable_backup_trigger = 0;
    COMMIT;
END$$
DELIMITER $$


LOCK TABLES users WRITE, users_backup READ;
INSERT INTO users(id, login, password, status, role_id, block_begin, block_end,
registration_date, id_name1, id_name2, id_name3, id_personal_info)
VALUES
(id_u, 'login', 'password', 'status', id_role, 'DATE', 'DATE',
 'DATE', id1, id2, id3, id4);

DELETE FROM users_backup WHERE id = id
UNLOCK TABLES;














