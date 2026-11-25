
# 짝수 더하기
print("--------------짝수 더하기--------------")
total = 0
for number in range(1, 11):
    if number % 2 != 0:
        continue
    total += number
    
print(total)

print("----------------홀수 더하기-------------------")
# 홀수 더하기
sum = 0
number = 0
while number < 10:
    if number % 2 == 0:
        number += 1
    sum += number
    number += 1
print(sum)

print("----------------짝수만 출력-------------------")

#짝수만 출력
for number in range(1, 11):
    if number % 2 != 0:
        continue    
    print(number)

#홀수만 출력
print("----------------홀수만 출력---------------")

num = 0
while num < 10:
    if num % 2 == 1:
        print(num)
        num += 1
    num +=1