import sys
import json

def quote(price, quantity, is_member, shipping=3000):
    # if quantity < 0:
    #     quantity = 0
    total = price * quantity
    if is_member or total >= 30000:
        shipping = 0
        print("무료배송")
    else:
        print("배송비 3000원")

    total += shipping
    print(total, "원")
    return total

def sum_values(*args):
    return sum(args)

def profile(**kwargs):
    return kwargs


print("수업 시간:", 60)
print("실행기:", sys.executable)

products = [("book", 12000), ("note", 8000), ("pen", 1500), ("bag", 25000), ("cup", 6000)]


owned_items = {"book", "pen"}
wish_items = {"pen", "bag"}

while(True):
    print()
    print("=== 파이썬 스마트 스토어 & 학습 매니저 ===")
    print("1. 상품 목록 보기 (가격 정렬)")
    print("2. 주문 담기 및 견적 계산")
    print("3. 수량 일괄 정산 리포트 (컴프리헨션)")
    print("4. 보유 vs 관심 상품 비교 (집합 연산)")
    print("5. 주문 내역 JSON 저장 및 불러오기")
    print("6. 회원 프로필 / 추가 메모 등록 (**kwargs)")
    print("0. 종료")

    a = input("선택 >> ")
    print()

    if(a == "1"):
        desc_product = sorted(products, key=lambda product: product[1], reverse=True)
        expensive = max(products, key=lambda product: product[1])
        recommend = products[1:4]

        print("상품 목록(가격 내림차순):", desc_product)
        print()
        print("최고가 상품:", expensive)
        print()
        print("추천 상품", recommend)
        print()

    elif(a == "2"):

        name = input("이름:").strip()

        while(True):
            is_member_in = input("회원입니까?(y/n):")
            is_member = False

            if is_member_in == "y":
                is_member = True
                break
            elif is_member_in == "n":
                is_member = False
                break
            else:
                print("잘못된 입력입니다.")
                continue

        # buy = []
        # while(True):
        #     buy_is_correct = True
        #     wish_list = set(input("주문할 상품:").split(","))
        #     for iii in buy:
        #         if not (iii == "book" or  iii == "note" or  iii == "pen" or  iii == "bag" or  iii == "cup"):
        #             print("잘못된 입력입니다.")
        #             buy_is_correct = False
        #             break
        #     if buy_is_correct == True:
        #         print(wish_list)
        #         break

        wish_list = input("주문할 상품:").split(",")
        print("위시리스트:", wish_list)

        while(True):
            buy_quantity = []
            totals2 = []
            try:
                for i in products:
                    x = int(input(f"{i[0]} 개수:"))
                    buy_quantity.append(x)
                    totals2.append(quote(i[1], x, is_member))
            except ValueError:
                print("잘못된 입력입니다. 정수를 입력하세요.")
                continue

            print(buy_quantity)
            print(totals2)
            print(sum_values(*totals2))
            break

        print()

        customer = {"이름": name, "회원": is_member, "위시리스트": wish_list, "주문 개수": buy_quantity, "주문 당 총가격": totals2, "총합": sum_values(*totals2)}

    elif(a == "3"):
        count = 0
        totals3 = []
        for i in buy_quantity:
            if i < 0:
                i = 0
            totals3.append(i * products[count][1])
            count += 1
        print(totals3)

        final_totals3 = {str(i + 1): value for i, value in enumerate(totals3)}
        print(final_totals3)
        print("총가격:", sum_values(*totals3))

    elif(a == "4"):
        print("보유 상품:", owned_items)
        print("위시리스트:", wish_items)
        print()
        print("구매 가능 상품:", sorted(owned_items & wish_items))
        print("구매 불가 상품:", sorted(wish_items - owned_items))
        print("ALL:", sorted(owned_items | wish_items))

    elif(a == "5"):
        try:
            text = json.dumps(customer, ensure_ascii=False)
            print("이름:",json.loads(text)["이름"])
            print("회원:",json.loads(text)["회원"])
            print("위시리스트:",json.loads(text)["위시리스트"])
            print("주문 개수:",json.loads(text)["주문 개수"])
            print("주문 당 총 가격:",json.loads(text)["주문 당 총가격"])
            print("총합:",json.loads(text)["총합"])
        except:
            print("Error")
        print()

    elif(a == "6"):
        x, y = (10, 20)
        print("매장 위치(경도):", x)
        print("매장 위치(위도):", y)
        print()
        a = input("이름:")
        b = input("레벨:")
        c = input("등급:")

        print(profile(이름=a, 레벨=b, 등급=c))
        print()
        print()
    elif(a == "0"):
        break
    else:
        print("잘못된 입력입니다.")

    



# owned_items = {"book", "pen"}
# wish_items = {"pen", "bag"}