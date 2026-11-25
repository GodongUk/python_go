import sys
import json
# 내부 함수 정의
def quote(prices, quantitys, shipping = 3000, is_member = False):
    total = 0
    try:
        for n, price in enumerate(prices):
            total += price* quantitys[n]
    except:
        return None
    if total>=30000 or is_member:
        print("무료배송입니다.")
        shipping = 0
    print(f"배송비는 {shipping:,}원 입니다.")
    return total + shipping

def profile(**kwargs):
    # kwargs가 딕셔너리 형태로 매개변수를 받음
    # 딕셔너리로 반환
    return kwargs

# 1. 앱 시작 화면 및 초기 데이터 설정
# 기본 정보 출력
print("파이썬 콘솔 어플리케이션 프로그램 ---------------------")
print("수업시간: ", 60)
print("파이썬 실행기 정보", sys.executable)
# 초기 상품 카탈로그
items = [("book", 12000),
         ("note", 8000),
         ("pen", 1500),
         ("bag", 25000),
         ("cup", 6000)]
# 매장 정보
shop_location = (10, 20)
# 사용자 프로필 및 보유/관심 상품 집합 초기화
# admin
user_profiles = {}
order_lists = {}
# user
owned_items = {"book", "pen"} # set type
wish_items = {"pen", "bag"} # set type
total_order_number = 0
ordered_items = {}

# 2. 메인 메뉴 루프
print()
print("=== 파이썬 스마트 스토어 & 학습 매니저 ===")
print("1. 상품 목록 보기 (가격 정렬)\n\
2. 주문 담기 및 견적 계산\n\
3. 수량 일괄 정산 리포트 (컴프리헨션)\n\
4. 보유 vs 관심 상품 비교 (집합 연산)\n\
5. 주문 내역 JSON 저장 및 불러오기\n\
6. 회원 프로필 / 추가 메모 등록 (**kwargs)\n\
0. 종료")
while True:    
    try: 
        menu = int(input("메뉴를 선택하시오: ").strip())
    except:
        print("잘못선택하셨습니다.")
        continue
    if menu == 0:
        print("종료합니다.")
        break
    elif menu == 1:
        # 상품 목록 보기 (가격 정렬)
        items = sorted(items, key= lambda item: item[1], reverse=True)
        print(f"상품명\t 가격")
        for item in items:
            print(f"{item[0]}\t {item[1]}")
        print(f"최고가 상품: {items[0][0]}")
        print(f"최저가 상품: {items[-1][0]}")
        best = list()
        for item in items[:3]:
            best.append(item[0])
        print(f"추천 TOP 3: {", ".join(best)}")
        continue
    elif menu == 2:
        user_name = input("주문자 이름: ").strip()
        while True:
            check_user = input("회원 여부(y/n): ").strip()
            if check_user == "y" or check_user == "yes":
                is_member = True
                break
            elif check_user == "n" or check_user == "no":
                is_member = False
                break
            else:
                print("잘못입력하셨습니다.")
                continue
        while True:
            try:
                order_items = input("주문 상품(,로 구분): ")
                order_items = [item.strip() for item in order_items.split(",")]
                no_item = list()
                for order_item in order_items:
                    found = False
                    for item, price in items:
                        if item == order_item:
                            found = True
                    if not found:
                        no_item.append(order_item)
                if no_item:
                    print(f"{", ".join(no_item)}은/는 존재하지 않는 상품입니다.")
                    continue
                break
            except:
                print("잘못입력하셨습니다.")
                continue
        while True:
            try:
                print("주문 수량을 입력하세요.")
                order_quantitys = list()
                for order_item in order_items:
                    order_quantity = int(input(f"{order_item}의 주문 수량: ").strip())
                    order_quantitys.append(order_quantity)
                break
            except(ValueError, TypeError):
                print("정수를 입력하세요")
                continue
            except:
                print("잘못입력하셨습니다.")
                continue
        order_prices = list()
        for order_item in order_items:
            for name, price in items:
                if order_item == name:
                    order_prices.append(price)
                    break
        total_price = quote(order_prices, order_quantitys, is_member = is_member)
        print(f"주문 금액은 총 {total_price:,}원 입니다")
        while True:
            confirm = input("주문하시겠습니까? (y/n): ").strip()
            if confirm == "y" or confirm == "yes":
                confirm = True
                break
            elif confirm == "n" or confirm == "no":
                confirm = False
                break
            else:
                print("잘못입력하셨습니다.")
                continue
        if confirm:
            order_list = {"주문자 이름": user_name,
                            "회원 여부": is_member,
                            "주문 상품": order_items,
                            "주문 수량": order_quantitys,
                            "개별 금액": order_prices,
                            "총 금액": total_price}
            total_order_number += 1
            order_lists[f"order{total_order_number}"] = order_list

    elif menu == 3:
        print("주문자의 누적 주문 수량 정산 리포트")
        user_name = input("주문자 이름: ").strip()
        user_order_items = list()
        user_order_quantitys = list()
        user_order_items_prices = list()
        for order_list in order_lists.values():
            print(order_list)
            print(order_list["주문자 이름"] == user_name)
            if order_list["주문자 이름"] == user_name:
                user_order_items.extend(order_list["주문 상품"])
                user_order_quantitys.extend(order_list["주문 수량"])
                user_order_items_prices.extend(order_list["개별 금액"])
        if not user_order_items:
            print(f"{user_name}님의 주문 목록이 없습니다.")
            continue
        ## 메뉴 3 요구사항 ---------------------------------------------------
        user_order_prices = [price*quantity for price, quantity in zip(user_order_items_prices, user_order_quantitys)]
        ## -----------------------------------------------------------------
        user_order_items_set = set(user_order_items)
        print(f"{user_name}님의 누적 주문 목록은 다음과 같습니다.")
        for item in user_order_items_set:
            total = 0
            for oitem, price in zip(user_order_items, user_order_prices):
                if oitem == item:
                    total += price
            print(f"{item}: {total:,}원")
        continue
    elif menu == 4:
        print("보유 상품 목록 ", ", ".join(owned_items))
        print("관심 상품 목록 ", ", ".join(wish_items))
        print("교집합: ", ", ".join(sorted(owned_items & wish_items)))
        print("차집합: ", ", ".join(sorted(wish_items - owned_items)))
        print("교집합: ", ", ".join(sorted(owned_items | wish_items)))
        continue
    elif menu == 5:
        print("마지막 주문 내역")
        json_order_list = json.dumps(order_lists, ensure_ascii=False)
        print(json_order_list)
        order_lists = json.loads(json_order_list)
        print(order_lists)
        continue
    elif menu == 6:
        x, y = shop_location
        print(f"매장 위치는 x: {x}, y: {y} 입니다")
        user_profile = profile(name="heeeun", ismember=True, age= 34)
        user_profiles[user_profile["name"]] = user_profile
        user_profile = profile(name="minju", ismember=True, age= 21)
        user_profiles[user_profile["name"]] = user_profile
        user_profile = profile(name="yujin", ismember=True, age= 22)
        user_profiles[user_profile["name"]] = user_profile
        print("전체 회원 목록")
        for user_profile in user_profiles.items():
            print(user_profile[0], user_profile[1])
        continue
    else:
        print("잘못선택하셨습니다.")
        continue

