-- DROP DATABASE  IF EXISTS `202`

CREATE DATABASE IF NOT EXISTS `202`;

USE `202`;

SET CHARSET utf8mb4;

CREATE TABLE IF NOT EXISTS locklist(
id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
memberId VARCHAR(255) NOT NULL,
name VARCHAR(255) NOT NULL,
type ENUM("fingerprint", "password", "card") DEFAULT "password" NOT NULL,
admin ENUM("Y","N") DEFAULT "N"
);

INSERT INTO locklist(memberId, name, type, admin) VALUES
("001", "姜月鹏", "fingerprint", "Y"),
("002", "保留卡-李忠科", "card", "Y"),
("006", "forAll", "password", "N"),
("007", "孟靖轶", "fingerprint", "N"),
("008", "李解", "fingerprint", "N"),
("009", "朱梓宁", "fingerprint", "N");


CREATE TABLE IF NOT EXISTS device(
id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
Etype VARCHAR(255) NOT NULL,
Ctype VARCHAR(255) NOT NULL,
brand VARCHAR(255),
modelNo VARCHAR(255),
serialNo VARCHAR(255),
imei VARCHAR(255),
time DATE NOT NULL DEFAULT 19700101,
price FLOAT,
amount INT NOT NULL DEFAULT 1
);

INSERT INTO device(Etype, Ctype, brand, modelNo, serialNo, imei, time, amount) VALUES
("screen", "屏幕", "ViewSonic", "VS18391", "WAA203403701", NULL, 20210930, 1),
("screen", "屏幕", "ViewSonic", "VS18391", "WAA203403685", NULL, 20210930, 1),
("screen", "屏幕", "ViewSonic", "VS18391", "WAA203403676", NULL, 20210930, 1),
("screen", "屏幕", "ViewSonic", "VS18391", "WAA203403625", NULL, 20210930, 1),
("screen", "屏幕", "LG", "29UM58", "905NTRLBD054", NULL, 20210930, 1),
("screen", "屏幕", "LG", "29UM58", "905NTHMBD057", NULL, 20210930, 1),
("screen", "屏幕", "LG", "29WL500", "007NTKF1D413", NULL, 20210930, 1),
("screen", "屏幕", "LG", "29WL500", "007NTQD1D476", NULL, 20210930, 1),
("screen", "屏幕", "LG", "29WL500", "007NTBK1D469", NULL, 20210930, 1),
("screen", "屏幕", "LG", "29WL500", "007NTJJ1D468", NULL, 20210930, 1),
("screen", "屏幕", "LG", "29WL500", "007NTRL1D470", NULL, 20210930, 1),
("screen", "屏幕", "SAMSUNG", "C32F391FW", "BZYBH4ZM501129Z", NULL, 20210930, 1),
("screen", "屏幕", "SAMSUNG", "C32F391FW", "BZYBH4ZM501444H", NULL, 20210930, 1),
("printer", "打印机", "HP", "LassrJet pro P1108", "VNFPP31649", NULL, 20210930, 1),
("printer", "打印机", "HP", "LassrJet pro P1108", "VNF4620580", NULL, 20210930, 1),
("printer", "打印机", "HP", "LassrJet pro P1108", "VNFPP31661", NULL, 20210930, 1),
("cable", "线材", NULL, "HDMI", NULL, NULL, 20210930, 13),
("cable", "线材", NULL, "VGA", NULL, NULL, 20210930, 15),
("cable", "线材", NULL, "电源线", NULL, NULL, 20210930, 1),
("power strip", "插线板", NULL, "插线板", NULL, NULL, 20210930, 1);

