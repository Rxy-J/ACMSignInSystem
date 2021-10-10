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
    email VARCHAR(100)
);

/*
 * 默认用户插入
 */
INSERT INTO user(uid, username, passhash, name, allTrainningTime, admin, email) VALUES 
(1, "admin", "21232f297a57a5a743894a0e4a801fc3", "admin", 0, "Y", "admin@mail.orangej.xyz"),
(2, "user", "ee11cbb19052e40b07aac0ca060c23ee", "user", 40, "N", "user@mail.orangej.xyz"),
(3, "android", "a5ee8cae22abf57d3c4c29f52f32ce9a", "user", 40, "N", "user@mail.orangej.xyz");

/* 
 * 创建训练记录表
 */
CREATE TABLE IF NOT EXISTS trainningrecord(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL,
    startTime DATETIME NOT NULL,
    endTime DATETIME,
    valid ENUM("Y", "N") DEFAULT "N",
    isRecord ENUM("Y", "N") DEFAULT "N",
    isFinish ENUM("Y", "N") DEFAULT "N",
    timeLength INT DEFAULT 0
);

/*
 * 插入默认训练记录
 */
INSERT INTO trainningrecord(id, username, startTime, endTime, valid, isRecord, isFinish, timeLength) VALUES
(1, "user", "2021-09-22 11:10:00", "2021-09-22 11:10:20", "Y", "Y", "Y", 20),
(2, "user", "2021-09-22 11:10:30", "2021-09-22 11:10:50", "Y", "Y", "Y", 20),
(3, "android", "2021-10-01 11:10:30", "2021-10-01 12:10:30", "Y", "Y", "Y", 3600),
(4, "user", "2021-09-22 11:10:30", "2021-09-22 11:10:50", "Y", "Y", "Y", 20),
(5, "android", "2021-09-22 11:10:30", "2021-09-22 11:10:50", "Y", "Y", "Y", 20),
(6, "android", "2021-09-22 11:10:30", "2021-09-22 11:10:50", "Y", "Y", "Y", 20),
(7, "android", "2021-09-22 11:10:30", "2021-09-22 11:10:50", "Y", "Y", "Y", 20),
(8, "user", "2021-09-22 11:10:30", "2021-09-22 11:10:50", "Y", "Y", "Y", 20),
(9, "android", "2021-09-22 11:10:30", "2021-09-22 11:10:50", "Y", "Y", "Y", 20);
