import random            # 시세 변동, 시작 가격 등에서 랜덤 값을 생성할 때
import pandas as pd      # 투자소별 상태(이름, 현재가, 보유량 등)를 표 형태로 출력할 때
import matplotlib.pyplot as plt   # 투자소의 시세 변동을 그래프로 시각화할 때
import matplotlib as mpl          # 한글 폰트 & 그래프 설정(폰트, 마이너스 표시 등)
from matplotlib.animation import FuncAnimation  # 실시간 캔들 차트(움직이는거) 구현


# 한글 폰트 및 마이너스 부호 깨짐 방지 설정
mpl.rcParams['font.family'] = 'AppleGothic'
mpl.rcParams['axes.unicode_minus'] = False


class Exchange:
    #각 투자소(거래소)의 시세와 거래 내역, 보유 상태를 관리하는 클래스입니다.
    def __init__(self, name):
        # 투자소 이름
        self.name = name
        # 시가, 고가, 저가, 종가(캔들차트용) 리스트
        self.opens = []
        self.highs = []
        self.lows = []
        self.closes = []
        # 보유량과 누적 매수 금액
        self.holding = 0
        self.buy_price_total = 0


        # 시작 시 랜덤한 가격으로 캔들 초기화
        start = random.randint(900, 1100)
        self.opens.append(start)
        self.highs.append(start)
        self.lows.append(start)
        self.closes.append(start)


    def simulate_price(self):
        # 시세를 변동시켜 새로운 캔들(시가, 고가, 저가, 종가)을 생성합니다. 변동 이유 터미널에 출력
        last_close = self.closes[-1]
        open_price = last_close
        change = random.uniform(-0.1, 0.1)  # -10% ~ +10%
        close_price = round(open_price * (1 + change), 2)
        high_price = round(max(open_price, close_price) * (1 + random.uniform(0, 0.03)), 2)
        low_price = round(min(open_price, close_price) * (1 - random.uniform(0, 0.03)), 2)


        # 변동 사유 설명 문자열
        reason = ""
        if change > 0.05:
            reason = "호재 뉴스로 인해 급등"
        elif change > 0:
            reason = "긍정적 시장 반응"
        elif change < -0.05:
            reason = "악재 뉴스로 인해 급락"
        else:
            reason = "부정적 시장 반응"


        print(f"[{self.name}] 변동 사유: {reason} ({'+' if change >= 0 else ''}{round(change * 100, 2)}%) → 종가 {close_price}원")


        # 시세 데이터 저장
        self.opens.append(open_price)
        self.highs.append(high_price)
        self.lows.append(low_price)
        self.closes.append(close_price)


    def get_price(self):
        #현재 투자소의 마지막(최신) 종가를 반환합니다.
        return self.closes[-1]


    def buy(self, amount, user_money): # 개수만큼 매수
        # user_money는 사용자가 가지고 있는 자금
        price = self.get_price()
        total = price * amount
        if user_money >= total: # 자금이 충분하면 보유량, 총매수금액 증가, 실제 매수 금액과 가격 반환
            self.holding += amount
            self.buy_price_total += total
            return total, price
        return 0, price # 자금 부족하면 (0, 현재가) 반환
    
    # 매도 기능
    def sell(self, amount):
        # 매도 수익, 매도 가격, 손익(수익-매입가)을 반환
        price = self.get_price()
        if self.holding >= amount:  # 보유량이 충분할 때만 매도 가능
            self.holding -= amount  # 내가 가진 개수에서 팔려고 한 개수만큼 빼기
            total_income = price * amount # (현재 가격 * 판 개수)해서 현재 매도를 통해 들어오는 총 금액 계산


            total_quantity = self.holding + amount # 매도하고 남은거 + 판거 개수 == 매도 직전 총 보유량
            if total_quantity > 0:
                avg_buy_price = self.buy_price_total / total_quantity
            else:
                avg_buy_price = 0
            profit = total_income - (avg_buy_price * amount)
            self.buy_price_total -= avg_buy_price * amount
            return total_income, price, profit
        return 0, price, 0 # - 보유량 부족 시 (0, 현재가, 0) 반환


def simulate_all_prices(exchanges):
    #모든 투자소의 시세를 1회씩 갱신 (시간 동기화)
    for ex in exchanges:
        ex.simulate_price()


def show_all_status(exchanges):
    #각 투자소별 현재가, 보유량, 평가금액을 표 형태로 콘솔에 출력합니다.
    data = []
    for ex in exchanges:
        current_price = ex.get_price()
        holding = ex.holding
        value = round(current_price * holding, 2)
        data.append({
            '이름': ex.name,
            '현재가': current_price,
            '보유량': holding,
            '평가금액': value
        })
    df = pd.DataFrame(data)
    print("\n[투자소 현황]")
    print(df)
    print()


def show_chart(exchange, exchanges):
    # 특정 투자소의 실시간 캔들차트를 matplotlib 애니메이션으로 보여줍니다.
    # 차트 갱신 시 모든 투자소 시세도 함께 갱신됨
    fig, ax = plt.subplots()


    def animate(i):
        simulate_all_prices(exchanges)
        ax.clear()
        ax.set_title(f"{exchange.name} 실시간 캔들차트")
        ax.set_xlabel("시간")
        ax.set_ylabel("가격")


        opens = exchange.opens
        highs = exchange.highs
        lows = exchange.lows
        closes = exchange.closes


        for idx in range(len(opens)):
            color = 'red' if closes[idx] > opens[idx] else 'blue'
            ax.plot([idx, idx], [lows[idx], highs[idx]], color=color)
            ax.plot([idx, idx], [opens[idx], closes[idx]], color=color, linewidth=6)


    ani = FuncAnimation(fig, animate, interval=500)
    plt.tight_layout()
    plt.show()


def main():
    # - 투자소 초기화, 사용자 입력 받아 각 기능 실행
    exchanges = [Exchange(name) for name in ["A소", "B소", "C소", "D소", "E소"]]
    user_money = 10000  # 시작 자금


    # 초반 20회 시세 미리 생성
    for _ in range(20):
        simulate_all_prices(exchanges)


    while True:
        print("\n===== 투자 시뮬레이터 메뉴 =====")
        print("1. 전체 시세 보기")
        print("2. 주가 차트 보기 (실시간)")
        print("3. 매수")
        print("4. 매도")
        print("5. 내 자산 현황")
        print("0. 종료")
        print("==========================")
        print(f"현재 보유 자금: {round(user_money, 2)}원")


        choice = input("선택: ")


        if choice == "1":
            # 전체 투자소 현황 출력
            show_all_status(exchanges)


        elif choice == "2":
            # 실시간 차트: 투자소 선택 후 차트 시각화
            for i, ex in enumerate(exchanges):
                print(f"{i}. {ex.name}")
            idx = int(input("차트 볼 투자소 번호 입력: "))
            if 0 <= idx < len(exchanges):
                show_chart(exchanges[idx], exchanges)


        elif choice == "3":
            # 매수: 투자소 선택, 수량 입력, 실제 매수 처리
            simulate_all_prices(exchanges)
            for i, ex in enumerate(exchanges):
                print(f"{i}. {ex.name} (현재가: {ex.get_price()}원)")
            idx = int(input("매수할 투자소 번호 입력: "))
            amount = int(input("몇 개 살래? "))
            if 0 <= idx < len(exchanges):
                cost, price = exchanges[idx].buy(amount, user_money)
                if cost > 0:
                    user_money -= cost
                    print(f"{round(cost, 2)}원 지불하고 {amount}개 매수함.")
                    print(f"지출: -{round(cost, 2)}원 / 잔액: {round(user_money, 2)}원")
                    print(f"매수 당시 가격: {round(price, 2)}원")
                else:
                    print("잔액 부족!")


        elif choice == "4":
            # 매도: 투자소 선택, 수량 입력, 실제 매도 처리
            simulate_all_prices(exchanges)
            for i, ex in enumerate(exchanges):
                print(f"{i}. {ex.name} (보유량: {ex.holding})")
            idx = int(input("매도할 투자소 번호 입력: "))
            amount = int(input("몇 개 팔래? "))
            if 0 <= idx < len(exchanges):
                income, price, profit = exchanges[idx].sell(amount)
                if income > 0:
                    user_money += income
                    print(f"{round(income, 2)}원 받고 {amount}개 매도함.")
                    print(f"수익: +{round(income, 2)}원 / 잔액: {round(user_money, 2)}원")
                    print(f"매도 당시 가격: {round(price, 2)}원")
                    print(f"손익: {'+' if profit >= 0 else ''}{round(profit, 2)}원")
                else:
                    print("보유량 부족!")


        elif choice == "5":
            # 내 자산 현황: 투자소별 평가금액, 현금 출력
            show_all_status(exchanges)
            print(f"보유 현금은 {round(user_money, 2)}원입니다.")


        elif choice == "0":
            print("시뮬레이터를 종료합니다.")
            break


        else:
            print("잘못된 입력입니다. 다시 시도하세요.")


# 프로그램 직접 실행 시 main() 호출
if __name__ == "__main__":
    main()