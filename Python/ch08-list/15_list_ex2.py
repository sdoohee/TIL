words = ['개과천선', '구사일생', '군계일학', '무용지물', '동고동락',
                '유비무환', '입신양명', '괄목상대', '막역지우', '고장난명']  

question = ["잘못을 고치고 옳은 길에 들어섬", 
                "죽일 고비를 여러 번 겪으며 살아나다", 
                "평범한 사람 가운데 뛰어난 사람",
                "아무짝에나 쓸모 없는 것", 
                "고통과 즐거움을 함께 한다", 
                "미리 준비해두면 근심 걱정이 없다", 
                "사회적으로 인정받고 출세하여 이름을 세상에 드날림",
                "다른 사람의 학식이나 업적이 크게 진보한 것을 말함",
                "생사를 같이 할 수 있는 친밀한 벗",
                "상대 없이 혼자서는 어떤 일을 이룰 수 없다"]

import random

print("사자성어 맞추기 게임을 시작합니다")
print("------------------------------------")

index = random.randint(0, len(words)-1) # 동일한 문제 반복

while True:   
    # index = random.randint(0, len(words)-1) # 문제 계속 변경됨

    print(question[index]) # 문제 출력
    answer = input("이말의 사자성어는? : ") # 답 입력

    if answer == words[index]:
        print("\n맞습니다.. 게임을 종료합니다.")
        break
    else:
        print("\n틀렸습니다...다시 도전 !\n")