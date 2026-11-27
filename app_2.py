import json

def sum_values(*args):
    return sum(args)

def quote(price, quantity, shipping = 3000):
    subtotal = price * quantity
    if subtotal >= 30000:
        shipping = 0
        print("무료 배송")
    else:
        print("배송비 3000원")
    return subtotal + shipping

def profile(**kwargs):
    return kwargs

itemsPrice = [("pen", 1500), ("book", 12000), ("tv", 3000000), ("computer", 4000000),("apple", 3000)]
name = ""
test1 = []
while True:
    print("1. 상품 목록 보기 (가격 정렬)")
    print("2. 주문 담기 및 견적 계산")
    print("3. 수량 일괄 정산 리포트 (컴프리헨션)")
    print("4. 보유 vs 관심 상품 비교 (집합 연산)")
    print("5. 주문 내역 JSON 저장 및 불러오기")
    print("6. 회원 프로필 / 추가 메모 등록 (**kwargs)")
    print("0. 종료")

    selectStr = input("원하는 버튼을 눌러주세요 >>")
    select = int(selectStr)
    if select == 1:
        print()
        items = sorted(itemsPrice, key = lambda item: item[1], reverse=True)
        print(itemsPrice)
        print("최고가 상품: ", items[0])
        print("추천 TOP3: ", items[:3])
        print()
    elif select == 2:
        print("주문 담기")
        if name == "":
            name = input("사용자 이름 : ").strip()
        else:
            print(name,"님 환영합니다.")
        while True:
            member = input("회원 여부 : (ex: y / n) ").strip()
            if member == "y":
                memberYn = True
                break
            elif member == 'n':
                memberYn = False
                break
            else:
                print("입력 값이 틀렸습니다. 다시 입력해주세요")
        try:
            total_price2 = 0
            total_price = 0
            shopping = input("구매하실 물건 입력해주세요: (ex : pen,book) ")
            shopping_list = shopping.split(",")

            raw_quantity = input("구매하실 물건의 수량을 입력하세요: (ex: 5,4) ")
            raw_quantity_list = raw_quantity.split(",")
            raw_quantity_list_list = []
            for x in raw_quantity_list:
                raw_quantity_list_list.append(int(x))
            for i in range(len(shopping_list)):
                item_name = shopping_list[i]
                quantity = raw_quantity_list_list[i]

                for item in itemsPrice:
                    if item[0] == item_name:
                        price = item[1]
                        subtotal = price * quantity
                        total = quote(price,quantity)
                        print(f"{item_name} : {price}원 x {quantity}개 + = {total}원")
                        total_price2 += total
                        test1.append(item_name)
                        test1.append(quantity)
            print(f"총 주문 금액 : {total_price2}원")
        except ValueError:
            print("정수를 입력하세요") 
    elif select == 3:
            quantities = [2, 3, 0, -1, 1]
            amounts = [n * 12000  for n in quantities if n > 0]
            report = {str(i + 1): v for i, v in enumerate(amounts)}
            print(amounts)
            print(report)
    elif select == 4:
        owned_items = {"book", "computer", "apple"}
        wish_items = {"computer", "tv", "pen"}   
        print("교집합: ", sorted(owned_items & wish_items))
        print("차집합: ", sorted(owned_items - wish_items))
        print("합집합: ", sorted(owned_items | wish_items))
    
    elif select == 5:
        try:
            dict = {"name": name, "member 여부":memberYn, "total_price": total_price2}
            text = json.dumps(dict, ensure_ascii=False)
            print(text)
            print(test1) #출력
            for i in range(len(test1)):
                if i % 2 == 0:
                    print(f"물품 명 : {test1[i]} , 갯수 : {test1[i+1]}")
                    if i <= len(test1):
                        break
                else:
                    print(f"물품 명 : {test1[i+1]} , 갯수 : {test1[i+2]}")
                    if i <= len(test1):
                        break
            print(sorted(items, key= lambda item: item[1], reverse=True))
            print(json.loads(text)["name"], json.loads(text)["member 여부"],json.loads(text)["total_price"])
        except NameError:
            print("2번 이름 먼저 입력하세요")
    elif select == 6:
        if name == "":
            name = input("이름:")
            level = input("레벨 :")
            grade = input("등급 :")
            profile1 = profile(name=name, leber = level, grade = grade)
            print(profile1)
        else:
            level = input("레벨 :")
            grade = input("등급 :")
            profile1 = profile(name=name, leber = level, grade = grade)
            print(profile1)
        point = (10, 20)
        x, y = point
        print("매장 좌표", x, y)
    elif select == 0:
        print("종료 합니다.")
        break
