import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.animation import FuncAnimation
import time

mpl.rcParams['font.family'] = 'AppleGothic'
mpl.rcParams['axes.unicode_minus'] = False

class Exchange:
    def __init__(self, name):
        self.name = name
        self.opens = []
        self.highs = []
        self.lows = []
        self.closes = []
        self.holding = 0
        self.buy_price_total = 0

        start = random.randint(900, 1100)
        self.opens.append(start)
        self.highs.append(start)
        self.lows.append(start)
        self.closes.append(start)

    def prepare_price_change(self):
        reasons = [
            ("외국인 투자자 대규모 매수", lambda ch: "호재 뉴스로 인해 급등", random.uniform(0.06, 0.1)),
            ("정부 규제 완화 발표", lambda ch: "긍정적 시장 반응", random.uniform(0.03, 0.06)),
            ("시장 관망세", lambda ch: "부정적 시장 반응" if ch < 0 else "긍정적 시장 반응", random.uniform(-0.03, 0.03)),
            ("금리 인상 우려", lambda ch: "부정적 시장 반응", random.uniform(-0.06, -0.03)),
            ("악재 뉴스 유포", lambda ch: "악재 뉴스로 인해 급락", random.uniform(-0.1, -0.06))
        ]
        return random.choice(reasons)

    def apply_price_change(self, reason_func, change):
        last_close = self.closes[-1]
        open_price = last_close
        close_price = round(open_price * (1 + change), 2)
        high_price = round(max(open_price, close_price) * (1 + random.uniform(0, 0.03)), 2)
        low_price = round(min(open_price, close_price) * (1 - random.uniform(0, 0.03)), 2)

        reason = reason_func(change)
        print(f"[{self.name}] 변동 사유: {reason} ({'+' if change >= 0 else ''}{round(change * 100, 2)}%) → 종가 {close_price}원")

        self.opens.append(open_price)
        self.highs.append(high_price)
        self.lows.append(low_price)
        self.closes.append(close_price)

    def simulate_price_quick(self):
        last_close = self.closes[-1]
        open_price = last_close
        change = random.uniform(-0.1, 0.1)
        close_price = round(open_price * (1 + change), 2)
        high_price = round(max(open_price, close_price) * (1 + random.uniform(0, 0.03)), 2)
        low_price = round(min(open_price, close_price) * (1 - random.uniform(0, 0.03)), 2)

        self.opens.append(open_price)
        self.highs.append(high_price)
        self.lows.append(low_price)
        self.closes.append(close_price)

    def get_price(self):
        return self.closes[-1]

    def buy(self, amount, user_money):
        price = self.get_price()
        total = price * amount
        if user_money >= total:
            self.holding += amount
            self.buy_price_total += total
            return total, price
        return 0, price

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

def simulate_all_prices(exchanges, skip_idx=None):
    for i, ex in enumerate(exchanges):
        if i != skip_idx:
            ex.simulate_price_quick()

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

def show_chart(exchange, exchanges):
    fig, ax = plt.subplots()

    def animate(i):
        evidence, reason_func, change = exchange.prepare_price_change()
        exchange.apply_price_change(reason_func, change)

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

        for idx in range(len(opens)):
            color = 'red' if closes[idx] > opens[idx] else 'blue'
            ax.plot([idx, idx], [lows[idx], highs[idx]], color=color)
            ax.plot([idx, idx], [opens[idx], closes[idx]], color=color, linewidth=6)

    ani = FuncAnimation(fig, animate, interval=3000, cache_frame_data=False)
    plt.tight_layout()
    plt.show()

def main():
    exchanges = [Exchange(name) for name in ["A소", "B소", "C소", "D소", "E소"]]
    user_money = 10000

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

if __name__ == "__main__":
    main()