DROP DATABASE IF EXISTS ACM;

CREATE DATABASE IF NOT EXISTS ACM;

USE ACM;

SET CHARSET utf8mb4;

/* 
 * 创建用户表
 */
CREATE TABLE IF NOT EXISTS user(
    uid INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL UNIQUE,
    passhash VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100),
    major VARCHAR(100),
    joinTime DATETIME,
    allTrainningTime INT DEFAULT 0,
    isTrainning ENUM("Y", "N") DEFAULT "N",
    currRecordId INT,
    admin ENUM("Y", "N") DEFAULT "N",
    secret VARCHAR(10),
    email VARCHAR(100)
);

/*
 * 默认用户插入
 */
INSERT INTO user(uid, username, passhash, name, allTrainningTime, admin, secret, email) VALUES
(1, "admin", "60106b4e3678d2f32d6cc9feececb7dd", "admin", 0, "Y", "123456", "admin@mail.orangej.xyz"),
(2, "user", "d2d670eea087c985f63afb04e61e13cb", "user", 7240, "N", "123456", "user@mail.orangej.xyz"),
(3, "android", "38975efa521536a17f33641a7efa9d84", "user", 3620, "N", "123456", "user@mail.orangej.xyz");

/* 
 * 创建训练记录表
 */
CREATE TABLE IF NOT EXISTS trainningrecord(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL,
    startTime DATETIME NOT NULL,
    endTime DATETIME,
    status ENUM("0", "1", "2", "3") DEFAULT "0" NOT NULL,
    timeLength INT DEFAULT 0
);

/*
 * 插入默认训练记录
 */
INSERT INTO trainningrecord(id, username, startTime, endTime, status, timeLength) VALUES
(1, "user", "2021-09-22 11:10:00", "2021-09-22 11:10:20", "3", 20),
(2, "user", "2021-09-22 11:10:30", "2021-09-22 11:10:50", "3", 20),
(3, "android", "2021-10-01 11:10:30", "2021-10-01 12:10:30", "3", 3600),
(4, "user", "2021-10-02 11:10:30", "2021-10-02 13:10:30", "3", 7200),
(5, "android", "2021-09-22 11:10:30", "2021-09-22 11:10:50", "3", 20),
(6, "android", "2021-09-22 11:10:30", "2021-09-22 11:10:50", "2", 20),
(7, "android", "2021-10-02 11:10:30", "2021-10-03 11:10:50", "1", 86420),
(8, "user", "2021-09-22 11:10:30", NULL, "0", 0),
(9, "android", "2021-09-22 11:10:30", NULL, "0", 0);
