dictionary = dict()

while True:
    word = input("\n영어 단어 등록 (종료는 quit) : ")
    
    if word == 'quit':
        break
    
    if word in dictionary:
        print(word + "는 이미 등록된 단어 입니다.")
    else:
        meaning = input(word + "의 뜻 입력 (종료는 quit) : ")
        if meaning == 'quit':
            break
        dictionary[word] = meaning

print()

while True:
    search = input("\n검색할 단어 입력 (종료는 quit) : ")
    if search == 'quit':
        break
    
    if search in dictionary:
        print(search + "의 뜻은 " + dictionary[search] + "입니다.")
    else:
        print(search + "는 사전에 없는 단어 입니다.")

print("\n종료합니다")