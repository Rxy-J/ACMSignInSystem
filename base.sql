
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
    allTrainningTime INT DEFAULT 0,
    isTrainning ENUM("Y", "N") DEFAULT "N",
    currRecordId INT,
    admin ENUM("Y", "N") DEFAULT "N",
    email VARCHAR(100)
);

/*
 * 默认用户插入
 */
insert into user(uid, username, passhash, name, allTrainningTime, admin, email) values 
(1, "admin", "21232f297a57a5a743894a0e4a801fc3", "admin", 0, "Y", "admin@mail.orangej.xyz"),
(2, "user", "ee11cbb19052e40b07aac0ca060c23ee", "user", 40, "N", "user@mail.orangej.xyz");

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
    timeLength INT DEFAULT 0
);

/*
 * 插入默认训练记录
 */
insert into trainningrecord(id, username, startTime, endTime, valid, isRecord, timeLength) values
(1, "user", "2021-09-22 11:10:00", "2021-09-22 11:10:20", "Y", "Y", 20),
(2, "user", "2021-09-22 11:10:30", "2021-09-22 11:10:50", "Y", "Y", 20);









-- select Eno, Ename 
-- from EMP
-- where Eno in {
--     select Eno 
--     from WORKS 
--     where  Cno="C1" or Cno="C2"
--     group by Eno
-- };

-- select Eno, sum(Cno), sum(Salary)
-- from WORKS
-- group by Eno;

-- select Eno
-- from WORKS
-- where Cno in {
--     select Cno
--     from WORKS
--     where Eno="2016001"
-- }

-- select Eno, Ename
-- from EMP
-- where Eno in {
--     select Eno
--     from WORKS
--     where Salary <= {
--         select Cno
--         from COMP
--         where Cname="IBM"
--     }
-- }
-- 1
