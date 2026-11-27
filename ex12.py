def area(width, length):
    sum = width * length
    return sum

print(area(5,6))

if area(5,6) == 30:
    print("맞음")
else:
    print("틀림")

numstr1 = input("가로 길이 입력:")
numstr2 = input("세로 길이 입력:")
num1 = int(numstr1)
num2 = int(numstr2)

print(f"가로 세로 곱: {area(num1,num2)}")