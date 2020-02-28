-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema sql_taxi
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sql_taxi` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
USE `sql_taxi` ;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Country`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Country` (
  `id` TINYINT(1) UNSIGNED NOT NULL AUTO_INCREMENT,
  `fullname` VARCHAR(40) NOT NULL,
  `shortname` CHAR(13) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Region`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Region` (
  `id` SMALLINT(2) UNSIGNED NOT NULL,
  `fullname` VARCHAR(40) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Area`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Area` (
  `id` MEDIUMINT(3) UNSIGNED NOT NULL,
  `fullname` VARCHAR(40) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`City`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`City` (
  `id` MEDIUMINT(3) UNSIGNED NOT NULL,
  `fullname` VARCHAR(40) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Street`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Street` (
  `id` MEDIUMINT(3) UNSIGNED NOT NULL,
  `fullname` VARCHAR(40) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Adress`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Adress` (
  `id` MEDIUMINT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_country` TINYINT(1) UNSIGNED NOT NULL,
  `id_region` SMALLINT(2) UNSIGNED NOT NULL,
  `Id_area` MEDIUMINT(3) UNSIGNED NOT NULL,
  `id_city` MEDIUMINT(3) UNSIGNED NOT NULL,
  `id_street` MEDIUMINT(3) UNSIGNED NOT NULL,
  `house` CHAR(5) NOT NULL,
  `flat` CHAR(6) NULL DEFAULT NULL,
  `post_index` MEDIUMINT(3) NOT NULL,
  `street_type` ENUM('проспект', 'переулок', 'набережная', 'площадь', 'тракт', 'тупик', 'бульвар', 'аллея') NULL DEFAULT NULL,
  `city_type` ENUM('поселок', 'город', 'село') NULL DEFAULT NULL,
  `building` CHAR(2) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Adress_1_idx` (`id_country` ASC) VISIBLE,
  INDEX `fk_Adress_2_idx` (`id_region` ASC) VISIBLE,
  INDEX `fk_Adress_3_idx` (`Id_area` ASC) VISIBLE,
  INDEX `fk_Adress_4_idx` (`id_city` ASC) VISIBLE,
  INDEX `fk_Adress_5_idx` (`id_street` ASC) VISIBLE,
  CONSTRAINT `fk_Adress_1`
    FOREIGN KEY (`id_country`)
    REFERENCES `sql_taxi`.`Country` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Adress_2`
    FOREIGN KEY (`id_region`)
    REFERENCES `sql_taxi`.`Region` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Adress_3`
    FOREIGN KEY (`Id_area`)
    REFERENCES `sql_taxi`.`Area` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Adress_4`
    FOREIGN KEY (`id_city`)
    REFERENCES `sql_taxi`.`City` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Adress_5`
    FOREIGN KEY (`id_street`)
    REFERENCES `sql_taxi`.`Street` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Bank`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Bank` (
  `id` TINYINT(1) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(70) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Bank_account`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Bank_account` (
  `id` TINYINT(1) UNSIGNED NOT NULL AUTO_INCREMENT,
  `number` VARCHAR(50) NOT NULL,
  `id_bank` TINYINT(1) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Bank_account_1_idx` (`id_bank` ASC) VISIBLE,
  CONSTRAINT `fk_Bank_account_1`
    FOREIGN KEY (`id_bank`)
    REFERENCES `sql_taxi`.`Bank` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Car_producer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Car_producer` (
  `id` TINYINT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Car`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Car` (
  `id` INT(8) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_car_producer` TINYINT(3) UNSIGNED NOT NULL,
  `number` VARCHAR(10) NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `type_of_car` ENUM('Седан', 'Хэтчбек', 'Универсал', 'Лифтбэк', 'Купе', 'Кабриолет', 'Родстер', 'Стретч', 'Тарга', 'Внедорожник', 'Кроссовер', ' Пикап', 'Фургон', 'Минивэн') NOT NULL,
  `color` VARCHAR(45) NOT NULL,
  `year_issue` DATE NOT NULL,
  `current_adress` MEDIUMINT(3) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Car_1_idx` (`id_car_producer` ASC) VISIBLE,
  INDEX `fk_Car_2_idx` (`current_adress` ASC) VISIBLE,
  CONSTRAINT `fk_Car_1`
    FOREIGN KEY (`id_car_producer`)
    REFERENCES `sql_taxi`.`Car_producer` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Car_2`
    FOREIGN KEY (`current_adress`)
    REFERENCES `sql_taxi`.`Adress` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Contacts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Contacts` (
  `id` MEDIUMINT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
  `number_phone` INT(4) UNSIGNED NOT NULL,
  `code_phone` SMALLINT(2) UNSIGNED NOT NULL,
  `email` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Name`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Name` (
  `id` MEDIUMINT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(40) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Middlename`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Middlename` (
  `id` MEDIUMINT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
  `middlename` VARCHAR(40) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Surname`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Surname` (
  `id` MEDIUMINT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
  `surname` VARCHAR(40) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Passport`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Passport` (
  `id` MEDIUMINT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
  `series` CHAR(2) NOT NULL,
  `number` CHAR(8) NOT NULL,
  `identify_number` CHAR(14) NOT NULL,
  `id_country` TINYINT(1) UNSIGNED NOT NULL,
  `sex` ENUM('мужской', 'женский') NOT NULL,
  `date_of_birth` DATE NOT NULL,
  `date_of_issue` DATE NOT NULL,
  `date_of_expiry` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Passport_1_idx` (`id_country` ASC) VISIBLE,
  CONSTRAINT `fk_Passport_1`
    FOREIGN KEY (`id_country`)
    REFERENCES `sql_taxi`.`Country` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Person` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_name` MEDIUMINT(3) UNSIGNED NOT NULL,
  `id_middlename` MEDIUMINT(3) UNSIGNED NOT NULL,
  `id_surname` MEDIUMINT(3) UNSIGNED NOT NULL,
  `id_passport` MEDIUMINT(3) UNSIGNED NOT NULL COMMENT '			',
  `login` VARCHAR(45) NOT NULL,
  `pwd_hash` VARCHAR(45) NOT NULL,
  `id_bank_account` TINYINT(1) UNSIGNED NOT NULL,
  `id_contacts` MEDIUMINT(3) UNSIGNED NOT NULL,
  `role` ENUM('водитель', 'клиент') NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Person_1_idx` (`id_name` ASC) VISIBLE,
  INDEX `fk_Person_2_idx` (`id_middlename` ASC) VISIBLE,
  INDEX `fk_Person_3_idx` (`id_surname` ASC) VISIBLE,
  INDEX `fk_Person_4_idx` (`id_passport` ASC) VISIBLE,
  INDEX `fk_Person_5_idx` (`id_bank_account` ASC) VISIBLE,
  INDEX `fk_Person_6_idx` (`id_contacts` ASC) VISIBLE,
  CONSTRAINT `fk_Person_1`
    FOREIGN KEY (`id_name`)
    REFERENCES `sql_taxi`.`Name` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Person_2`
    FOREIGN KEY (`id_middlename`)
    REFERENCES `sql_taxi`.`Middlename` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Person_3`
    FOREIGN KEY (`id_surname`)
    REFERENCES `sql_taxi`.`Surname` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Person_4`
    FOREIGN KEY (`id_passport`)
    REFERENCES `sql_taxi`.`Passport` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Person_5`
    FOREIGN KEY (`id_bank_account`)
    REFERENCES `sql_taxi`.`Bank_account` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Person_6`
    FOREIGN KEY (`id_contacts`)
    REFERENCES `sql_taxi`.`Contacts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Credit_card`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Credit_card` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `number` BIGINT(19) UNSIGNED NOT NULL,
  `valid_month` TINYINT(3) UNSIGNED NOT NULL,
  `valid_year` TINYINT(3) UNSIGNED NOT NULL,
  `cvv` TINYINT(3) UNSIGNED NOT NULL,
  `id_person` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Credit_card_1_idx` (`id_person` ASC) VISIBLE,
  CONSTRAINT `fk_Credit_card_1`
    FOREIGN KEY (`id_person`)
    REFERENCES `sql_taxi`.`Person` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Provider`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Provider` (
  `id` TINYINT(3) UNSIGNED NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `id_adress` MEDIUMINT(3) UNSIGNED NOT NULL,
  `id_contacts` MEDIUMINT(3) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Provider_1_idx` (`id_contacts` ASC) VISIBLE,
  INDEX `fk_Provider_2_idx` (`id_adress` ASC) VISIBLE,
  CONSTRAINT `fk_Provider_1`
    FOREIGN KEY (`id_contacts`)
    REFERENCES `sql_taxi`.`Contacts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Provider_2`
    FOREIGN KEY (`id_adress`)
    REFERENCES `sql_taxi`.`Adress` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Transaction`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Transaction` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `rubles` SMALLINT(5) UNSIGNED NOT NULL,
  `kopecks` TINYINT(2) UNSIGNED NOT NULL,
  `id_credit_card` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Transaction_1_idx` (`id_credit_card` ASC) VISIBLE,
  CONSTRAINT `fk_Transaction_1`
    FOREIGN KEY (`id_credit_card`)
    REFERENCES `sql_taxi`.`Credit_card` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Store`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Store` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_tariff` SMALLINT(5) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Sale`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Sale` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_client` INT(10) UNSIGNED NOT NULL,
  `id_provider` TINYINT(3) UNSIGNED NOT NULL,
  `id_car` INT(8) UNSIGNED NOT NULL,
  `id_transaction` INT(10) UNSIGNED NOT NULL,
  `id_driver` INT(10) UNSIGNED NOT NULL,
  `id_store` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Sale_1_idx` (`id_client` ASC) VISIBLE,
  INDEX `fk_Sale_2_idx` (`id_provider` ASC) VISIBLE,
  INDEX `fk_Sale_3_idx` (`id_car` ASC) VISIBLE,
  INDEX `fk_Sale_4_idx` (`id_transaction` ASC) VISIBLE,
  INDEX `fk_Sale_5_idx` (`id_driver` ASC) VISIBLE,
  INDEX `fk_Sale_6_idx` (`id_store` ASC) VISIBLE,
  CONSTRAINT `fk_Sale_1`
    FOREIGN KEY (`id_client`)
    REFERENCES `sql_taxi`.`Person` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Sale_2`
    FOREIGN KEY (`id_provider`)
    REFERENCES `sql_taxi`.`Provider` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Sale_3`
    FOREIGN KEY (`id_car`)
    REFERENCES `sql_taxi`.`Car` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Sale_4`
    FOREIGN KEY (`id_transaction`)
    REFERENCES `sql_taxi`.`Transaction` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Sale_5`
    FOREIGN KEY (`id_driver`)
    REFERENCES `sql_taxi`.`Person` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Sale_6`
    FOREIGN KEY (`id_store`)
    REFERENCES `sql_taxi`.`Store` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
-- -----------------------------------------------------
-- Table `sql_taxi`.`Tariff`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql_taxi`.`Tariff` (
  `id` SMALLINT(5) UNSIGNED NOT NULL AUTO_INCREMENT,
  `within_city` DECIMAL(10,0) NOT NULL,
  `outside_sity` DECIMAL(10,0) NOT NULL,
  `short_description` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;