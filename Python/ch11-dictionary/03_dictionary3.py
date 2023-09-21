# 딕셔너리 

dictionary = {
    "name": "버섯 불고기 덮밥",
    "type": "덮밥",
    "ingredient": ["소고기", "버섯", "양파", "간장", "설탕"],
    "origin": "한국"
}

# 딕셔너리 요소 출력
print("요리명 : ", dictionary['name'])
print("종류 : ", dictionary['type'])
print("재료 : ", dictionary['ingredient'])
print("원산지 : ", dictionary['origin'])

print()

# 요리명을 '한우 버섯 불고기 덮밥'으로 변경
dictionary['name'] = '한우 버섯 불고기 덮밥'
print("요리명 : ", dictionary['name'])

print()

# 재료가 리스트로 출력되는 것을 원소만 출력 (문자열로 출력)
# 재료 : ['소고기', '버섯', '양파', '간장', '설탕']
# -> 소고기 버섯 양파 간장 설탕
dictionary['name'] = '한우 버섯 불고기 덮밥'
ingredients_str = ' '.join(dictionary['ingredient'])
print("요리명 : ",dictionary['name'])
print("종류 : ", dictionary['type'])
print("재료 : ", ingredients_str)
print("원산지 : ", dictionary['origin'])