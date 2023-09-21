# 리스트 연습문제

# 01
# 영화 예매 순위 기준 top3는 다음과 같다.
# 영화 제목을 movie_rank 이름의 리스트에 저장하라. (순위 정보는 저장하지 않는다.)

# 순위   영화
# 1      닥터 스트레인지
# 2      스플릿
# 3      럭키

movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)
# 결과 : ["닥터 스트레인지", "스플릿", "럭키"]


# 02
# movie_rank 리스트에 "배트맨"을 추가하라.
# 결과 : ['닥터 스트레인지', '스플릿', '럭키', '배트맨']

movie_rank.append("배트맨")
print(movie_rank)


# 03
# "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
# 결과 : ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']

movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 04
# movie_rank 리스트에서 '럭키'를 삭제하라.
# 결과 : ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']

movie_rank.remove("럭키")
print(movie_rank)


# 05
# movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
# 결과 : ['닥터 스트레인지', '슈퍼맨']

movie_rank.remove("스플릿")
movie_rank.remove("배트맨")
print(movie_rank)

# 06
# lang1과 lang2 리스트가 다음과 같을 때
# lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
# 결과 :['Python', 'C', 'C++', 'JAVA', 'HTML', 'CSS', 'JavaScript']
lang1 = ["Python", "C", "C++", "JAVA"]
lang2 = ["HTML", "CSS", "JavaScript"]

langs = lang1 + lang2
print(langs)

# 07
# 다음 리스트에서 최대값과 최소값을 출력하라. 
# 결과 :
# max:  7
# min:  1

nums = [5, 2, 6, 7, 3, 4, 1]

print("max : ", max(nums))
print("min : ", min(nums))

# 08
# 다음 리스트의 합을 출력하라.
# 결과 :  15

nums = [1, 2, 3, 4, 5]

print(sum(nums))

# 09
# 다음 리스트에 저장된 데이터의 개수를 출력하라.
# 결과 : 12
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자",
        "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]

print(len(cook))

# 10
# 다음 리스트의 평균을 출력하라.#
# 결과  : 3.0

nums = [1, 2, 3, 4, 5]

print(sum(nums) / len(nums))

# 11
# price 변수에는 날짜와 종가 정보가 저장돼 있다.
# 날짜 정보를 제외하고 가격 정보만을 출력하라.
# 결과 : [100, 130, 140, 150, 160, 170]
price = ['202300906', 100, 130, 140, 150, 160, 170]

print(price[1:])

# 12
# 슬라이싱을 사용해서 홀수만 출력하라.
# 결과 : [1, 3, 5, 7, 9]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 13
# 슬라이싱을 사용해서 짝수만 출력하라.
# 결과 : [2, 4, 6, 8, 10]
print(nums[1::2])


# 14
# 리스트의 숫자를 역 방향으로 출력하라.
# 결과 : [5, 4, 3, 2, 1]
nums = [1, 2, 3, 4, 5]
print(nums[::-1])


# 15
# 리스트에서 다음 원소 출력하라.
# 결과  : 삼성전자 Naver

companies = ['삼성전자', 'LG전자', 'Naver']
print(" ".join(companies[::2]))


# 16
# 리스트를 문자열로 변환
# 결과 : 삼성전자 LG전자 Naver SK하이닉스 현대차

companies = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '현대차']
print(" ".join(companies))


# 17
# 리스트를 문자열로 변환
# 결과 : 삼성전자/LG전자/Naver/SK하이닉스/현대차

companies = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '현대차']
print("/".join(companies))

# 18
# 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
# 문자열을 리스트로 분리 저장하라.
# 예 : ['삼성전자', 'LG전자', 'Naver']

string = "삼성전자/LG전자/Naver"
companies = string.split("/")
print(companies)