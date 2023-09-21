-- Drop 문

-- 테이블 삭제
-- publisher 테이블 삭제
-- 외래키 제약조건 설정되어 있기 때문에 삭제 시 오류
drop table publisher;

-- 외래키 제약조건 확인할 필요 없도록 설정
-- 가능하면 하지 않습니다
set foreign_key_checks = 0;

-- 외래키 제약조건 검사하도록 재설정
set foreign_key_checks = 1;