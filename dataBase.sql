-- this is a table for publisher
create table publisher(
    publisherName varchar(30),
    address varchar(30),
    website varchar(30),
    primary key (publisherName));
-- table for book cuz the relation of book and publisher is many to one I brought publisher in table of book
create table book(
    bookId varchar(10),
    bookNumber int,
    title varchar(20),
    field varchar(20),
    pages int,
    price float,
    publisherName varchar(30),
    primary key (bookId,bookNumber),
    foreign key (publisherName) references publisher(publisherName));
-- creating table for ordinary people
create table ordinary(
    nationalCode char(10),
    name varchar(20),
    family varchar(20),
    job varchar(20),
    userName varchar(20) unique,
    password varchar(20),
    primary key (nationalCode));
-- table for students
create table student(
    nationalCode char(10),
    name varchar(20),
    family varchar(20),
    studentId varchar(20),
    university varchar(20),
    userName varchar(20) unique,
    password varchar(20),
    primary key (nationalCode));
-- table for instructor
create table instructor(
    nationalCode char(10),
    name varchar(20),
    family varchar(20),
    instructorId varchar(20),
    university varchar(20),
    userName varchar(20) unique,
    password varchar(20),
    primary key (nationalCode));
-- table for customers and phone numbers
-- student
create table student_phoneNum(
    nationalCode char(10),
    phoneNum char(11),
    primary key (nationalCode,phoneNum),
    foreign key (nationalCode) references student(nationalCode));
-- teachers
create table instructor_phoneNum(
    nationalCode char(10),
    phoneNum char(11),
    primary key (nationalCode,phoneNum),
    foreign key (nationalCode) references instructor(nationalCode));
create table ordinary_phoneNum(
    nationalCode char(10),
    phoneNum char(11),
    primary key (nationalCode,phoneNum),
    foreign key (nationalCode) references ordinary(nationalCode));
-- table for customers and address
-- student
create table student_address(
    nationalCode char(10),
    address varchar(30),
    primary key (nationalCode,address),
    foreign key (nationalCode) references student(nationalCode));
-- teachers
create table instructor_address(
    nationalCode char(10),
    address varchar(30),
    primary key (nationalCode,address),
    foreign key (nationalCode) references instructor(nationalCode));
-- ordinay
create table ordinary_address(
    nationalCode char(10),
    address varchar(30),
    primary key (nationalCode,address),
    foreign key (nationalCode) references ordinary(nationalCode));
-- creating table for history
create table history(
    historyId varchar(20),
    receivedDate time,
    remainingDays int,
    returnedDate time,
    cost float,
    bookId varchar(10),
    bookNumber int,
    primary key (historyId),
    foreign key (bookId,bookNumber) references book(bookId,bookNumber));
-- creating account table
-- every customer has one account and an account belongs to just one person so its one to one relation
-- student
create table student_account(
    nationalCode char(10),
    balance float,
    createDate date,
    primary key (nationalCode),
    foreign key (nationalCode) references student(nationalCode));
-- instructor
create table instructor_account(
    nationalCode char(10),
    balance float,
    createDate date,
    primary key (nationalCode),
    foreign key (nationalCode) references instructor(nationalCode));
-- ordinary
create table ordinary_account(
    nationalCode char(10),
    balance float,
    createDate date,
    primary key (nationalCode),
    foreign key (nationalCode) references ordinary(nationalCode));
-- history is kind of multi value every account can have zero,one,two,.... and more histories and in history field we can put null if customer has no history
-- for students
create table student_account_history(
    nationalCode char(10),
    historyId varchar(20),
    primary key (nationalCode,historyId),
    foreign key (nationalCode) references student_account(nationalCode),
    foreign key (historyId) references history(historyId));
-- for teachers
create table instructor_account_history(
    nationalCode char(10),
    historyId varchar(20),
    primary key (nationalCode,historyId),
    foreign key (nationalCode) references instructor_account(nationalCode),
    foreign key (historyId) references history(historyId));
-- for ordinary
create table ordinary_account_history(
    nationalCode char(10),
    historyId varchar(20),
    primary key (nationalCode,historyId),
    foreign key (nationalCode) references  ordinary_account(nationalCode),
    foreign key (historyId) references history(historyId));
-- these are just to test how it workd
-- for publisher
insert into publisher values ('phoniex','address1','www.phoniex.com');
insert into publisher values ('balck swan','address2','www.blackswan.com');
insert into publisher values ('white swan','address3','www.whiteswan.com');
insert into publisher values ('razaz','address4','www.razazhub.com');
insert into publisher values ('diamond dogs','address5','www.diamonddogs.com');
insert into publisher values ('dark','address6','www.dark99.com');
insert into publisher values ('shining','address7','www.shining.com');
-- for student
insert into student values('0023251026','mohammad','meymani','9731113','amirkabir','mcaptain79','mohammad1234');
insert into student_account values ('0023251026',100000,'2021-01-01');
insert into student values('1023241026','aghay','ahadi','9731106','amirkabir','iamalivahed78','ali1234');
insert into student_account values ('1023241026',8000,'2021-03-07');
-- for instructor
insert into instructor values ('2023351226','hmreza','zarandi','i885634','amirkabir','hzarandi56','hmreza1234');
insert into instructor_account values ('2023351226',72.33,'2000-4-8');
insert into instructor values ('2123451236','arman','reybod','ins856344','amirkabir','reybod_a','arman1234');
insert into instructor_account values ('2123451236',5.34,'2010-5-11');
-- for ordinary
insert into ordinary values ('0120454236','esi','pashang','infuencer','esipashang','esi1234');
insert into ordinary_account values ('0120454236',30000,'2021-5-11');
insert into ordinary values ('0120454260','kami','hosseini','infuencer','kamy_hi','kami1234');
insert into ordinary_account values ('0120454260',35000,'2021-6-11');
update ordinary set password = 'esipashang1234' where name = 'esi';
update ordinary set job = 'influencer ' where job = 'infuencer';
-- inserting some books to our data base
-- science fiction books
insert into book values ('b1',1,'harry potter1','science fiction',150,10,'phoniex');
insert into book values ('b2',1,'harry potter2','science fiction',200,15,'phoniex');
insert into book values ('b3',1,'harry potter3','science fiction',100,8,'phoniex');
insert into book values ('b4',1,'harry potter4','science fiction',250,15,'phoniex');
insert into book values ('b4',2,'harry potter4','science fiction',100,10,'phoniex');
insert into book values ('b4',3,'harry potter4','science fiction',310,20,'phoniex');
-- educational university
insert into book values ('b5',1,'707 amar','educational',200,20,'white swan');
insert into book values ('b6',1,'707 riazi2','educational',300,30,'white swan');
insert into book values ('b6',2,'707 riazi2','educational',130,15,'white swan');
insert into book values ('b7',1,'707 riazi1','educational',230,17,'white swan');
insert into book values ('b8',1,'707 fizik1','educational',100,10,'white swan');
insert into book values ('b9',1,'707 fizik2','educational',50,20,'white swan');
insert into book values ('b9',2,'707 fizik2','educational',250,20,'white swan');
-- refrence
insert into book values ('b10',1,'clrs','refrence',500,50,'dark');
insert into book values ('b11',1,'adams riazi','refrence',300,40,'dark');
insert into book values ('b11',2,'adams riazi','refrence',300,40,'dark');
insert into book values ('b11',3,'adams riazi','refrence',400,60,'balck swan');
insert into book values ('b12',1,'paterson','refrence',400,50,'dark');
insert into book values ('b12',2,'paterson','refrence',400,70,'dark');
insert into book values ('b13',1,'silver shot','refrence',700,90,'dark');

