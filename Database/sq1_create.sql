
-- 스키마 (데이터베이스) 생성
create schema sqldb1 default character set utf8;
create schema sqldb2 default character set UTF8MB4;

-- 스키마 (데이터베이스) 삭제
drop schema sqldb1;
drop database sqldb2;

use sqldb1;

-- 테이블 생성
create table product(
	prdNo varchar(10) not null primary key,
    prdName varchar(30) not null,
    prdPrice int,
    prdCompany varchar(30)
);

create table product2(
	prdNo varchar(10) not null,
    prdName varchar(30) not null,
    prdPrice int,
    prdCompany varchar(30),
    primary key(prdNo)
);

create table product3(
	prdNo varchar(10) not null,
    prdName varchar(30) not null,
    prdPrice int,
    prdCompany varchar(30),
    constraint PK_product_prdNo primary key(prdNo)
);

-- 기본키 / 외래키 제약조건 설정
-- publisher : 출판사 테이블
-- book : 도서 테이블

/*
	출판사 테이블 생성(출판사번호, 춢판사명)
    - 기본키로 pubNo 지정, NOT NULL
    - pubName NOT NULL로 설정
*/

create table publisher (
	pubNo varchar(10) not null primary key,
    pubName varchar(30) not null
);

/*
	도서 테이블 생성(도서번호, 도서명, 가격, 발행일, 출판사번호(외래키))
    제약조건 설정
    - 기본키 : bookNo, not null
    - 외래키 : punNo(참조하는 테이블과 기본키 지정)
    - bookPrice : 기본값 10000, 1000보다 크게 설정
    
*/

create table book(
	bookNo varchar(10) not null primary key,
    bookName varchar(30) not null,
    bookPrice int default 10000 check(bookPrice > 1000),
    bookDate date,
    pubNo varchar(10) not null,	-- 외래키로 사용하는 열이름(필수)
    foreign key (pubNo) references publisher (pubNo)	-- 외래키 제약 조건 설정
    -- foreign key (pubNo) references publisher (pubNo)
);

create table book2(
	bookNo varchar(10) not null primary key,
    bookName varchar(30) not null,
    bookPrice int default 10000 check(bookPrice > 1000),
    bookDate date,
    pubNo varchar(10) not null,	-- 외래키로 사용하는 열이름(필수)
	constraint FK_book_publisher foreign key (pubNo) references publisher (pubNo)	-- 외래키 제약 조건 설정
    -- foreign key (pubNo) references publisher (pubNo)
);

describe book;

create table category(
	ctgID int not null primary key,
    ctgName varchar(30) not null
);

create table cproduct(
	ctgID int not null primary key,
    ctgName varchar(10) not null,
    ctgNo int not null,
    constraint FK_cproduct_category foreign key (ctgNo) references category (ctgID)
);

-- 기본키 삭제
alter table department drop primary key;

