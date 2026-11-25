scorestr = input("점수를 입력하세요:").strip()
score = int(scorestr)
if score < 0 or score > 100:
    message = "오류"
elif score >= 90:
    message = "A"
elif score >= 80:
    message = "B"
else:
    message = "C"
print(f"점수는 {score}점 / 등급은 {message}등급")