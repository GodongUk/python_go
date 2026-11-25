
price = int(input("가격:"))
total = 30000
is_member = False
if price < 0:
    message = "금액 오류"
elif price >= 30000 or is_member:
    message = "무료배송"
else:
    message = "배송비 3000원"
print(message)