use sqldb4;

use mysql;

-- 사용자 계정 조회
SELECT * FROM user;

-- 사용자 계성 생성 
-- CREATE USER 계정명@호스트 identified by 비밀번호;
-- 호스트 
	-- localhost : 로컬에서 접근 가능
    -- 192.168.172.1 : 특정 IP에서 접근 가능 
    -- '%' : 어디에서나 접근 가능 
    
-- 비밀번호 변경 
	-- SET PASSWORD for '계정명@호스트' = '새 비밀번호';

-- 계정 삭제 : DROP USER 계정명@호스트; 



