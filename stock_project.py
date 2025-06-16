import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.animation import FuncAnimation
import time

# 그래프에서 한글이 깨지지 않도록 폰트를 설정하고, 마이너스 기호도 제대로 보이도록 설정합니다.
mpl.rcParams['font.family'] = 'AppleGothic'
mpl.rcParams['axes.unicode_minus'] = False

# 각 거래소(투자소)의 시세 데이터 및 보유 상태를 관리하는 클래스입니다.
class Exchange:
    def __init__(self, name):
        self.name = name  # 거래소 이름
        self.opens = []   # 시가 리스트 (시간 흐름에 따른 시가 기록)
        self.highs = []   # 고가 리스트
        self.lows = []    # 저가 리스트
        self.closes = []  # 종가 리스트
        self.holding = 0  # 사용자가 보유한 수량
        self.buy_price_total = 0  # 총 매수한 금액의 합 (평균 단가 계산용)

        # 시작 가격을 무작위로 설정하여 초기값을 생성합니다.
        start = random.randint(900, 1100)
        self.opens.append(start)
        self.highs.append(start)
        self.lows.append(start)
        self.closes.append(start)

    # 시세 변동에 영향을 주는 사건과 그에 따른 변화율을 준비합니다.
    def prepare_price_change(self):
        reasons = [
            ("외국인 투자자 대규모 매수", lambda ch: "호재 뉴스로 인해 급등", random.uniform(0.06, 0.1)),
            ("정부 규제 완화 발표", lambda ch: "긍정적 시장 반응", random.uniform(0.03, 0.06)),
            ("시장 관망세", lambda ch: "부정적 시장 반응" if ch < 0 else "긍정적 시장 반응", random.uniform(-0.03, 0.03)),
            ("금리 인상 우려", lambda ch: "부정적 시장 반응", random.uniform(-0.06, -0.03)),
            ("악재 뉴스 유포", lambda ch: "악재 뉴스로 인해 급락", random.uniform(-0.1, -0.06))
        ]
        return random.choice(reasons)

    # 위에서 정해진 변동률을 실제 가격 데이터에 반영하여 새로운 가격 데이터를 생성합니다.
    def apply_price_change(self, reason_func, change):
        last_close = self.closes[-1]  # 가장 최근 종가
        open_price = last_close
        close_price = round(open_price * (1 + change), 2)
        high_price = round(max(open_price, close_price) * (1 + random.uniform(0, 0.03)), 2)
        low_price = round(min(open_price, close_price) * (1 - random.uniform(0, 0.03)), 2)

        reason = reason_func(change)  # 사유 메시지 생성
        print(f"[{self.name}] 변동 사유: {reason} ({'+' if change >= 0 else ''}{round(change * 100, 2)}%) → 종가 {close_price}원")

        # 생성한 가격 데이터를 시계열에 추가
        self.opens.append(open_price)
        self.highs.append(high_price)
        self.lows.append(low_price)
        self.closes.append(close_price)

    # 빠르게 변동하는 시세를 시뮬레이션하기 위한 간이 함수입니다.
    def simulate_price_quick(self):
        last_close = self.closes[-1]
        open_price = last_close
        change = random.uniform(-0.1, 0.1)  # -10% ~ +10% 사이 랜덤 변화
        close_price = round(open_price * (1 + change), 2)
        high_price = round(max(open_price, close_price) * (1 + random.uniform(0, 0.03)), 2)
        low_price = round(min(open_price, close_price) * (1 - random.uniform(0, 0.03)), 2)

        self.opens.append(open_price)
        self.highs.append(high_price)
        self.lows.append(low_price)
        self.closes.append(close_price)

    # 현재 가격을 반환합니다.
    def get_price(self):
        return self.closes[-1]

    # amount 만큼 매수하고, user_money가 충분한지 확인한 후 거래를 수행합니다.
    def buy(self, amount, user_money):
        price = self.get_price()
        total = price * amount
        if user_money >= total:
            self.holding += amount
            self.buy_price_total += total
            return total, price
        return 0, price

    # amount 만큼 매도하고, 평균 매입단가 대비 손익을 계산합니다.
    def sell(self, amount):
        price = self.get_price()
        if self.holding >= amount:
            self.holding -= amount
            total_income = price * amount
            total_quantity = self.holding + amount
            avg_buy_price = self.buy_price_total / total_quantity if total_quantity > 0 else 0
            profit = total_income - (avg_buy_price * amount)
            self.buy_price_total -= avg_buy_price * amount
            return total_income, price, profit
        return 0, price, 0

# 전체 거래소의 가격을 시뮬레이션하며, 특정 인덱스는 제외 가능
def simulate_all_prices(exchanges, skip_idx=None):
    for i, ex in enumerate(exchanges):
        if i != skip_idx:
            ex.simulate_price_quick()

# 현재 각 거래소의 가격, 보유량, 평가 금액을 표 형태로 출력합니다.
def show_all_status(exchanges):
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

# 실시간 캔들 차트를 애니메이션 형태로 보여줍니다.
def show_chart(exchange, exchanges):
    fig, ax = plt.subplots()

    def animate(i):
        # 선택된 거래소의 시세는 실제 이벤트 기반으로 반영
        evidence, reason_func, change = exchange.prepare_price_change()
        exchange.apply_price_change(reason_func, change)

        # 나머지는 빠르게 랜덤 변동만 반영
        for ex in exchanges:
            if ex != exchange:
                ex.simulate_price_quick()

        ax.clear()
        ax.set_title(f"{exchange.name} 실시간 캔들차트")
        ax.set_xlabel("시간")
        ax.set_ylabel("가격")

        opens = exchange.opens
        highs = exchange.highs
        lows = exchange.lows
        closes = exchange.closes

        # 각 시간별로 캔들(봉)을 그려줍니다.
        for idx in range(len(opens)):
            color = 'red' if closes[idx] > opens[idx] else 'blue'
            ax.plot([idx, idx], [lows[idx], highs[idx]], color=color)  # 고가~저가 라인
            ax.plot([idx, idx], [opens[idx], closes[idx]], color=color, linewidth=6)  # 시가~종가 바디

    ani = FuncAnimation(fig, animate, interval=3000, cache_frame_data=False)
    plt.tight_layout()
    plt.show()

# 메인 실행 함수
# 사용자 인터페이스를 CLI 형태로 구현해 반복 실행하며 거래를 시뮬레이션합니다.
def main():
    exchanges = [Exchange(name) for name in ["A소", "B소", "C소", "D소", "E소"]]  # 거래소 초기화
    user_money = 10000  # 시작 자금

    for _ in range(20):
        simulate_all_prices(exchanges)  # 시작 시 가격 초기화 시뮬레이션

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
            show_all_status(exchanges)

        elif choice == "2":
            for i, ex in enumerate(exchanges):
                print(f"{i}. {ex.name}")
            idx = int(input("차트 볼 투자소 번호 입력: "))
            if 0 <= idx < len(exchanges):
                show_chart(exchanges[idx], exchanges)

        elif choice == "3":
            for i, ex in enumerate(exchanges):
                print(f"{i}. {ex.name} (현재가: {ex.get_price()}원)")
            idx = int(input("매수할 투자소 번호 입력: "))
            evidence, reason_func, change = exchanges[idx].prepare_price_change()
            print(f"[{exchanges[idx].name}] 근거: {evidence} → 3초 후 가격 반영됨...")
            amount = int(input("몇 개 살래? "))
            time.sleep(3)
            simulate_all_prices(exchanges, skip_idx=idx)
            exchanges[idx].apply_price_change(reason_func, change)
            cost, price = exchanges[idx].buy(amount, user_money)
            if cost > 0:
                user_money -= cost
                print(f"{round(cost, 2)}원 지불하고 {amount}개 매수함.")
                print(f"지출: -{round(cost, 2)}원 / 잔액: {round(user_money, 2)}원")
                print(f"매수 당시 가격: {round(price, 2)}원")
            else:
                print("잔액 부족!")

        elif choice == "4":
            for i, ex in enumerate(exchanges):
                print(f"{i}. {ex.name} (보유량: {ex.holding})")
            idx = int(input("매도할 투자소 번호 입력: "))
            evidence, reason_func, change = exchanges[idx].prepare_price_change()
            print(f"[{exchanges[idx].name}] 근거: {evidence} → 3초 후 가격 반영됨...")
            amount = int(input("몇 개 팔래? "))
            time.sleep(3)
            simulate_all_prices(exchanges, skip_idx=idx)
            exchanges[idx].apply_price_change(reason_func, change)
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
            show_all_status(exchanges)
            print(f"보유 현금은 {round(user_money, 2)}원입니다.")

        elif choice == "0":
            print("시뮬레이터를 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

# 메인 실행
if __name__ == "__main__":
    main()