/* 
 * 创建用户表
 */
create table user(
    uid INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL UNIQUE,
    passhash VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100),
    major VARCHAR(100),
    joinTime datetime,
    allTrainningTime VARCHAR(1000) DEFAULT "0",
    isTrainning ENUM("Y", "N") DEFAULT "N",
    currRecordId INT,
    admin ENUM("Y", "N") DEFAULT "N",
    email VARCHAR(100)
);

/*
 * 默认用户插入
 */
insert into user(uid, username, passhash, name, admin, email) values 
(1, "admin", "21232f297a57a5a743894a0e4a801fc3", "admin", "Y", "admin@mail.orangej.xyz"),
(2, "user", "ee11cbb19052e40b07aac0ca060c23ee", "user", "N", "user@mail.orangej.xyz");

/* 
 * 创建训练记录表
 */
create table trainningrecord(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL,
    startTime datetime NOT NULL,
    endTime datetime,
    valid ENUM("Y", "N") DEFAULT "N",
    isRecord ENUM("Y", "N") DEFAULT "N",
    timeLength VARCHAR(1000) DEFAULT "0"
);

/*
 * 插入默认训练记录
 */
-- insert into trainningrecord(id, username, )