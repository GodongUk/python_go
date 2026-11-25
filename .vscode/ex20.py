
scores = []
errorlist = []
succeslist = []

for number in [0, 1, 2, 3]:
    numberstr = input(f"{number+1}번째 점수 입력: ")
    scores.append(numberstr)

for score in scores:
    try:
        num = int(score)
        if 0 <= num <= 100:
            if num >= 60:
                succeslist.append(num)
        else:
            errorlist.append(score)
    except ValueError:
        errorlist.append(score)

print("합격 목록:", succeslist)
print("오류 목록:", errorlist)
