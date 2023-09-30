
-- 조인(JOIN)

-- 다양한 조인 문 표기 방법(1)
-- WHERE 조건 사용
SELECT client.clientNo, clientName, bsQty
FROM client, bookSale
WHERE client.clientNo = bookSale.clientNo;
-- ambiguous : 모호한 (명백하지 않음)
-- 양쪽 테이블에 공통되는 열 이름 앞에 모호성을 없애기 위해
-- 테이블명 표기 (테이블명이 없으면 오류)

-- client 테이블과 bookSale 테이블을 공통되는 열 clientNo를 기준으로 inner join
-- 의미 : 어떤 고객?
-- 한 번이라도 주문한 적이 있는 고객 
-- 여기에 없는 고객은 한 번도 주문한 적이 없는 고객

-- 다양한 조인 문 표기 방법(2)
-- 양쪽 테이블에 공통되지는 않지만 모든 열 이름에 테이블명 붙임
SELECT client.clientNo, client.clientName, bookSale.bsQty
FROM client, bookSale
WHERE client.clientNo = bookSale.clientNo;

-- 다양한 조인 문 표기 방법(3)
-- 테이블명 대신 별칭(Alias) 사용
SELECT C.clientNo, C.clientName, BS.bsQty
FROM client C, bookSale BS
WHERE C.clientNo = BS.clientNo;


-- 다양한 조인 문 표기 방법(4)
-- JOIN ON 명시
SELECT C.clientNo, C.clientName, BS.bsQty
FROM bookSale BS
	JOIN client C
	ON C.clientNo = BS.clientNo;


-- 다양한 조인 문 표기 방법(5)
-- INNER JOIN ON 명시
SELECT C.clientNo, C.clientName, BS.bsQty
FROM bookSale BS
	INNER JOIN client C
	ON C.clientNo = BS.clientNo;
-- 가장 많이 사용되는 방법으로 권장
-- 우리는 이 방법 사용

-- client 테이블과 bookSale 테이블 위치 바꿔도 됨
SELECT C.clientNo, C.clientName, BS.bsQty
FROM client C
	INNER JOIN bookSale BS
	ON C.clientNo = BS.clientNo;

-- ----------------------------------------------------
-- 모든 열 (*) 출력 
SELECT *
FROM client C
	INNER JOIN bookSale BS
	ON C.clientNo = BS.clientNo;

-- 필요한 열만 추출
-- 한 번이라도 도서를 주문한 적이 있는 고객의 고객번호와 고객명 출력 
SELECT C.clientNo, C.clientName
FROM client C
	INNER JOIN bookSale BS
	ON C.clientNo = BS.clientNo;


-- 필요한 열만 추출
-- 한 번이라도 도서를 주문한 적이 있는 고객의 고객번호와 고객명 출력 
-- 중복되는 행은 한 번만 출력 
SELECT DISTINCT C.clientNo, C.clientName
FROM client C
	INNER JOIN bookSale BS
	ON C.clientNo = BS.clientNo;

-- -------------------------------------------------------
-- 3개 테이블 결합 : 조인 조건 2개

-- 주문된 도서에 대하여 고객명과 도서명 출력
-- bookSale, client, book
SELECT BS.bsNo, C.clientName, B.bookName
FROM booksale BS
	INNER JOIN client C ON C.clientNo = BS.clientNo
    INNER JOIN book B ON B.bookNo = BS.bookNo;

SELECT BS.bsNo, C.clientName, B.bookName
FROM client C
	INNER JOIN booksale BS ON C.clientNo = BS.clientNo
    INNER JOIN book B ON B.bookNo = BS.bookNo;


-- 도서를 주문한 고객의 고객 정보, 주문 정보, 도서 정보 출력
-- 주문번호, 주문일, 고객번호, 고객명, 도서명, 주문수량
SELECT BS.bsNo, BS.bsDate, C.clientNo, C.clientName, B.bookName, BS.bsQty
FROM booksale BS
     INNER JOIN client C ON C.clientNo = BS.clientNo
     INNER JOIN book B ON B.bookNo = BS.bookNo;

-- 고객별로 총주문수량 계산하여
-- 고객명과 총주문수량 출력
-- 총주문수량 기준 내림차순 정렬
-- 고객번호, 고객명, 총주문수량 출력 (client, bookSale)
SELECT C.clientNo 고객번호, C.clientName 고객명, SUM(BS.bsQty) 총주문수량
FROM bookSale BS
  INNER JOIN client C ON C.clientNo = BS.clientNo
GROUP BY C.clientNo
ORDER BY 총주문수량 DESC;

-- 주문된 도서의 주문일, 고객명, 도서가격, 주문수량, 주문액 계산하여 출력
-- 주문일 기준 오름차순 정렬

-- select BS.bsDate 주문일 ,C.clientName 고객명 , B.bookName 도서명, B.bookPrice 도서가격, BS.bsQty 주문수량, B.bookPrice*BS.bsQty 주문액
-- from bookSale BS
-- 	inner join client C on C.clientNo = BS.clientNo
--     inner join book B on B.bookNo = BS.bookNo
-- order by 주문일자;

-- where 절 추가
-- 2021년 ~ 현재까지 판매된 도서의 주문일, 고객명, 도서가격, 주문수량, 주문액 계산하여 출력

select BS.bsDate ,C.clientName , B.bookName, B.bookPrice, BS.bsQty , B.bookPrice*BS.bsQty 주문액
from bookSale BS
	inner join client C on C.clientNo = BS.clientNo
    inner join book B on B.bookNo = BS.bookNo
    where BS.bsdate >= '2021-01-01'
order by BS.bsDate;

-- ------------------------------------------
-- 조인 연습문제

-- 1. 모든 도서에 대하여 도서의 도서번호, 도서명, 출판사명 출력
SELECT B.bookNo 도서번호, B.bookName 도서명, P.pubName 출판사명
FROM book B 
	INNER JOIN publisher P ON P.pubNo = B.pubNo;

-- 2. '서울 출판사'에서 출간한 도서의 도서명, 저자명, 출판사명 출력 (조건에 출판사명 사용)
SELECT B.bookName 도서명, B.bookAuthor 저자명, P.pubName 출판사명
FROM book B 
	INNER JOIN publisher P ON P.pubNo = B.pubNo
WHERE P.pubName= '서울 출판사';

-- 3. '정보출판사'에서 출간한 도서 중 판매된 도서의 도서명 출력 (중복된 경우 한 번만 출력) (조건에 출판사명 사용)
SELECT DISTINCT B.bookName 도서명
FROM book B
	INNER JOIN publisher P ON P.pubNo = B.pubNo
    INNER JOIN bookSale BS ON BS.bookNo = B.bookNo
WHERE P.pubName= '정보출판사';

-- 4. 도서가격이 30,000원 이상인 도서를 주문한 고객의 고객명, 도서명, 도서가격, 주문수량 출력
SELECT C.clientName 고객명, B.bookName 도서명, B.bookPrice 도서가격, BS.bsQty 주문수량
FROM bookSale BS
	INNER JOIN client C ON C.clientNo = BS.clientNo
    INNER JOIN book B ON B.bookNo = BS.bookNo
WHERE B.bookPrice >= 30000;

-- 5. '안드로이드 프로그래밍' 도서를 구매한 고객에 대하여 도서명, 고객명, 성별, 주소 출력 (고객명으로 오름차순 정렬)
SELECT B.bookName 도서명, C.clientName 고객명, C.clientGender 성별, C.clientAddress 주소
FROM bookSale BS
	INNER JOIN client C ON C.clientNo = BS.clientNo
    INNER JOIN book B ON B.bookNo = BS.bookNo
WHERE B.bookName = '안드로이드 프로그래밍'
ORDER BY 고객명;

-- 6. ‘도서출판 강남'에서 출간된 도서 중 판매된 도서에 대하여 ‘총 매출액’ 출력
SELECT SUM(BS.bsQty*B.bookPrice) 총매출액
FROM bookSale BS
	INNER JOIN book B ON B.bookNo = BS.bookNo
    INNER JOIN publisher P ON P.pubNo = B.pubNo
WHERE P.pubName = '도서출판 강남';

-- 7. ‘서울 출판사'에서 출간된 도서에 대하여 판매일, 출판사명, 도서명, 도서가격, 주문수량, 주문액 출력
SELECT BS.bsDate 판매일, P.pubName 출판사명, B.bookName 도서명, B.bookPrice 도서가격, 
       BS.bsQty 주문수량, B.bookPrice*BS.bsQty 주문액
FROM bookSale BS
    INNER JOIN book B ON B.bookNo = BS.bookNo
    INNER JOIN publisher P ON P.pubNo = B.pubNo
WHERE P.pubName = '서울 출판사';

-- 8. 판매된 도서에 대하여 도서별로 도서번호, 도서명, 총 주문 수량 출력
SELECT B.bookNo 도서번호, B.bookName 도서명, SUM(BS.bsQty) 총주문수량
FROM bookSale BS
    INNER JOIN book B ON B.bookNo = BS.bookNo
GROUP BY B.bookNo;

-- 9. 판매된 도서에 대하여 고객별로 고객명, 총구매액 출력 ( 총구매액이 100,000원 이상인 경우만 해당)
SELECT C.clientName 고객명, SUM(B.bookPrice*BS.bsQty) 총구매액
FROM bookSale BS
	INNER JOIN book B On B.bookNo = BS.bookNo
    INNER JOIN client C ON C.clientNo = BS.clientNo
GROUP BY C.clientNo
HAVING SUM(B.bookPrice*BS.bsQty) >= 100000;

-- 10. 판매된 도서 중 ＇도서출판 강남'에서 출간한 도서에 대하여 고객명, 주문일, 도서명, 주문수량, 출판사명 출력 
--     (고객명으로 오름차순 정렬)
-- 4개 테이블 조인 : 조인조건 3개
SELECT C.clientName 고객명, BS.bsDate 주문일, B.bookName 도서명, 
       BS.bsQty 주문수량, P.pubName 출판사명
FROM bookSale BS
	INNER JOIN client C ON C.clientNo = BS.clientNo
	INNER JOIN book B ON B.bookNo = BS.bookNo
    INNER JOIN publisher P ON P.pubNo = B.pubNo
WHERE P.pubName = '도서출판 강남'
ORDER BY 고객명;

-- --------------------------------------------------------------------
-- 외부 조인 (Outer JOIN) 
-- 공통된 속성을 매개로 하는 정보가 없더라도 
-- 데이터를 버리지 않고 연산의 결과를 테이블에 표시
-- 좌측외부조인 / 우측외부조인 / 완전외부조인

-- 왼쪽(client) 테이블 기준
-- client 테이블의 데이터 모두 출력
-- 오른쪽 bookSale 테이블 : 
	-- client 테이블에는 존재하지만 bookSale 테이블에는 존재하지 않는 고객에 대해서는 null로 출력
    -- null 의미 : 고객 중 한 번도 구매한 적이 없는 고객에 해당 
SELECT * 
FROM client C
	 LEFT OUTER JOIN bookSale BS
     ON C.clientNo = BS.clientNo
ORDER BY C.clientNo;

-- 고객 중 한 번도 구매한 적이 없는 고객
SELECT C.clientNo, C.clientName 
FROM client C
	 LEFT OUTER JOIN bookSale BS
     ON C.clientNo = BS.clientNo
WHERE BS.clientNo IS NULL
ORDER BY C.clientNo;

-- 도서 중에서 한 번도 판매된 적이 없는 도서 출력 
SELECT *
FROM book B
	LEFT OUTER JOIN booksale BS
    ON B.bookNo = BS.bookNo
    WHERE BS.bsNo IS NULL
ORDER BY B.bookNo;

SELECT B.bookNo, B.bookName
FROM book B
	LEFT OUTER JOIN booksale BS
    ON B.bookNo = BS.bookNo
    WHERE BS.bsNo IS NULL
ORDER BY B.bookNo;

-- 오른쪽 테이블(bookSale) 기준
-- bookSale 테이블의 데이터 모두 출력
-- 이때 client 테이블에는 한 번이라도 주문한 적이 있는 고객 정보만 출력
SELECT * 
FROM client C
	 RIGHT OUTER JOIN bookSale BS
     ON C.clientNo = BS.clientNo
ORDER BY C.clientNo;

-- 완전 외부 조인 (FULLL OUTER JOIN)
-- MySQL에서는 FULL OUTER JOIN 지원하지 않음
-- LEFT JOIN과 RIGHT JOIN을 UNION 해서 사용
SELECT * 
FROM client C
	 LEFT JOIN bookSale BS
     ON C.clientNo = BS.clientNo
     
UNION

SELECT * 
FROM client C
	 RIGHT JOIN bookSale BS
     ON C.clientNo = BS.clientNo;
