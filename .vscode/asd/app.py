import sys
print("app.py")
print("수업시간: ",60)
print("실행기 정보: ", sys.executable)

pri = {}
raw = {}
def sum_values(name,*args):
    total = sum(args)
    if name in pri:
        pri[name] +=total
    else:
        pri[name] =total

def profile(**kwargs):
    return kwargs

# 가격, 수량, 배송비
def quote(price, quantity, shipping=3000):
    is_member = True
    total = price * quantity
    if total < 0:
        message = "금액 오류"
    elif total >= 30000 and is_member:
        message = "무료 배송"
        shipping = 0
    else:
        message =  "배송비 3000원"
        shipping = 3000
    print(message)

    return total + shipping

def printinfo():
    print()
    print("===========================================")
    print("=== 파이썬 스마트 스토어 & 학습 매니저 ===")
    print("1. 상품 목록 보기 (가격 정렬)")
    print("2. 주문 담기 및 견적 계산")
    print("3. 수량 일괄 정산 리포트 (컴프리헨션)")
    print("4. 보유 vs 관심 상품 비교 (집합 연산)")
    print("5. 주문 내역 JSON 저장 및 불러오기")
    print("6. 회원 프로필 / 추가 메모 등록 (**kwargs)")
    print("0. 종료")
    print()

def manu1():
    st = sorted(mes, key=lambda item: item[1], reverse=True)
    
    print(st)
    print("최고의상품: ",mes[-1])
    print("추천 top3: ",st[:3])

def manu2():
    while True:
        print("1. 사용자 이름,회원,주문,수량")
        print("2. 배송비관련")
        print("3. 누적 주문금액")
        print("4. 메뉴로 되돌아가기")
        num = input("입력: ")
        if num == "1":
            try:
                name = input("이름: ").strip()
                if name in user:
                    item = input("상품명: ")
                    raw_quantity = int(input("수량: "))
                    item[raw] = raw_quantity
                    print("사용자가 있음")
                else:
                    print("사용자가 없습니다.")
            except ValueError:
                print("정수를 입력하세요")

        elif num == "2":
            try:
                for i in mes:
                    if i[0] == item:
                        print("계산된 금액: ",quote(i[1],raw_quantity))
            except ValueError:
                print("값이 없습니다.")

        elif num == "3":
            try:
                for i in mes:
                    if i[0] == item:
                        sum_values(i[0],quote(i[1],raw_quantity))
                        print(pri)
            except ValueError:
                print("값이 없습니다.")
        elif num == "4":
            print("메뉴로 되돌아갑니다.")
            break
        else:
            print("잘못 입력하셧습니다.")
            break

def manu3():
    print(raw)

def manu4():
    nam1 = {"name":"교집합","mes":sorted(awned_items & wish_items)}
    nam2 = {"name":"차집합","mes":sorted(awned_items - wish_items)}
    nam3 = {"name":"합집합","mes":sorted(awned_items | wish_items)}
    print(nam1)
    print(nam2)
    print(nam3)

def manu5():
    print

def manu6():
    print

user = {"근원","민수"}
mes = [("book",12000),("note",8000),("pen",1500),("bag",25000),("cup",6000)]
awned_items = {"book","note","cup"}
wish_items = {"pen","note"}

while True:
    printinfo()
    num = input("숫자 입력: ")
    if num == "1":
        manu1()
    elif num == "2":
        manu2()
    elif num == "3":
        manu3()
    elif num == "4":
        manu4()
    elif num == "5":
        print()
    elif num == "6":
        print()
    elif num == "0":
        break
    else:
        print("잘못입력하셧습니다.")
    
    



