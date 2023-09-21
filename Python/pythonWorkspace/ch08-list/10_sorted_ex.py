scores = []
high = total = 0
sum = 0

for i in range(5):
    score = int(input("학생%d 점수 입력 : " %(i+1)))
    scores.append(score)
    sum += score
    if score >= 80:
        high += 1

# avg = float(sum) / len(scores)
avg = sum / len(scores)

print("총점 : %d" % sum)
print("평균 : %.2f" % avg)
print("80점 이상 학생 : %d명" % high)
print("점수 내림차순 정렬 :", scores)