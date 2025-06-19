# 필요한 외부 라이브러리 임포트
import random                       # 무작위 수 생성에 사용
import pandas as pd                # 투자소 상태를 테이블로 보기 좋게 출력할 때 사용
import matplotlib.pyplot as plt    # 가격 변동 그래프 그릴 때 사용
import matplotlib as mpl           # 그래프 한글 폰트 깨짐 방지용 설정
from matplotlib.animation import FuncAnimation  # 실시간 차트 애니메이션용
import time                        # 시간 지연 (예: 3초 대기) 등에 사용

# 한글 폰트 설정 (macOS용 설정)
mpl.rcParams['font.family'] = 'AppleGothic'
mpl.rcParams['axes.unicode_minus'] = False  # 음수 부호 깨짐 방지

# 투자소 클래스 정의
class Exchange:
    def __init__(self, name):
        self.name = name  # 투자소 이름
        # 캔들 차트용 시가/고가/저가/종가 리스트
        self.opens = []
        self.highs = []
        self.lows = []
        self.closes = []
        
        # 보유 상태 관련 변수
        self.holding = 0  # 보유한 개수
        self.buy_price_total = 0  # 누적 매수 금액 (평균 단가 계산용)

        # 시작 가격 랜덤 설정 (900~1100원 사이)
        start = random.randint(900, 1100)
        self.opens.append(start)
        self.highs.append(start)
        self.lows.append(start)
        self.closes.append(start)

    # 가격 변동 사유와 변동폭을 준비하는 함수
    def prepare_price_change(self):
        reasons = [
            ("외국인 투자자 대규모 매수", lambda ch: "호재 뉴스로 인해 급등", random.uniform(0.06, 0.1)),
            ("정부 규제 완화 발표", lambda ch: "긍정적 시장 반응", random.uniform(0.03, 0.06)),
            ("시장 관망세", lambda ch: "부정적 시장 반응" if ch < 0 else "긍정적 시장 반응", random.uniform(-0.03, 0.03)),
            ("금리 인상 우려", lambda ch: "부정적 시장 반응", random.uniform(-0.06, -0.03)),
            ("악재 뉴스 유포", lambda ch: "악재 뉴스로 인해 급락", random.uniform(-0.1, -0.06))
        ]
        return random.choice(reasons)

    # 선택된 변동폭과 해설로 시세 반영
    def apply_price_change(self, reason_func, change):
        last_close = self.closes[-1]
        open_price = last_close
        close_price = round(open_price * (1 + change), 2)
        high_price = round(max(open_price, close_price) * (1 + random.uniform(0, 0.03)), 2)
        low_price = round(min(open_price, close_price) * (1 - random.uniform(0, 0.03)), 2)

        reason = reason_func(change)
        print(f"[{self.name}] 변동 사유: {reason} ({'+' if change >= 0 else ''}{round(change * 100, 2)}%) → 종가 {close_price}원")

        # 캔들 데이터 저장
        self.opens.append(open_price)
        self.highs.append(high_price)
        self.lows.append(low_price)
        self.closes.append(close_price)

    # 단순한 랜덤 시세 변동 (빠르게 반영할 때 사용)
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

    # 현재 종가 반환
    def get_price(self):
        return self.closes[-1]

    # 매수 기능
    def buy(self, amount, user_money):
        price = self.get_price() # 현재 종가
        total = price * amount # 매수 총액
        if user_money >= total:
            self.holding += amount # 보유량 증가
            self.buy_price_total += total # 누적 매수 금액 증가
            return total, price  # 총 지출 금액과 단가 반환
        return 0, price

    # 매도 기능
    def sell(self, amount):
        price = self.get_price()
        if self.holding >= amount:
            self.holding -= amount
            total_income = price * amount # 총 매도 금액
            total_quantity = self.holding + amount  # 기존 총 개수
            avg_buy_price = self.buy_price_total / total_quantity if total_quantity > 0 else 0 # 평균 매수 단가
            profit = total_income - (avg_buy_price * amount) 
            self.buy_price_total -= avg_buy_price * amount
            return total_income, price, profit
        return 0, price, 0




# 전체 투자소 가격을 시뮬레이션하는 함수
def simulate_all_prices(exchanges, skip_idx=None, selected_change=None, selected_func=None):
    for i, ex in enumerate(exchanges):
        if i == skip_idx:
            ex.apply_price_change(selected_func, selected_change)
        else:
            ex.simulate_price_quick()

# 현재 전체 투자소 상태 출력
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

# 특정 투자소의 캔들 차트 시각화
def show_chart(exchange, exchanges):
    fig, ax = plt.subplots()

    def animate(i):
        # 1. 현재 차트 대상 투자소에서 시세 변동 이유와 변화율 준비
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

        # 각 시간별 캔들 차트 그리기
        for idx in range(len(opens)):
            color = 'red' if closes[idx] > opens[idx] else 'blue'
            ax.plot([idx, idx], [lows[idx], highs[idx]], color=color)  # 고가~저가
            ax.plot([idx, idx], [opens[idx], closes[idx]], color=color, linewidth=6)  # 시가~종가
    # cache_frame_data=False로 설정해서 프레임 항상 새로고침
    ani = FuncAnimation(fig, animate, interval=3000, cache_frame_data=False)
    plt.tight_layout() # 차트 레이아웃 조정
    plt.show()

# 메인 실행 함수
def main():
    exchanges = [Exchange(name) for name in ["A소", "B소", "C소", "D소", "E소"]]  # 투자소 5개 초기화
    user_money = 10000  # 초기 자금

    # 시세 초기화
    for _ in range(20):
        for ex in exchanges:
            ex.simulate_price_quick()

    # 사용자 인터랙션 루프
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

        # 각 메뉴에 따라 기능 분기
        if choice == "1":
            show_all_status(exchanges)

        elif choice == "2":
            for i, ex in enumerate(exchanges):
                print(f"{i}. {ex.name}")
            idx = int(input("차트 볼 투자소 번호 입력: "))
            if 0 <= idx < len(exchanges):
                show_chart(exchanges[idx], exchanges)

        elif choice == "3":
            # 모든 투자소의 이름과 현재 가격 출력
            for i, ex in enumerate(exchanges):
                print(f"{i}. {ex.name} (현재가: {ex.get_price()}원)")
            # 유저가 매수할 투자소 번호 선택
            idx = int(input("매수할 투자소 번호 입력: "))
            # 선택된 투자소의 시세 변동 이벤트 준비
            evidence, reason_func, change = exchanges[idx].prepare_price_change()
            print(f"[{exchanges[idx].name}] 근거: {evidence} → 3초 후 가격 반영됨...")
            amount = int(input("몇 개 살래? "))
            time.sleep(3)
            # 모든 투자소 시세 업데이트 (선택한 투자소는 준비된 이유/변동폭으로 반영)
            # 유저가 고른 투자소 인덱스, 해당 투자소에 적용할 변동폭, 해당 투자소에 적용할 사유 함수
            simulate_all_prices(exchanges, skip_idx=idx, selected_change=change, selected_func=reason_func)
            cost, price = exchanges[idx].buy(amount, user_money)
            if cost > 0:
                user_money -= cost
                print(f"{round(cost, 2)}원 지불하고 {amount}개 매수함.")
                print(f"지출: -{round(cost, 2)}원 / 잔액: {round(user_money, 2)}원")
                print(f"매수 당시 가격: {round(price, 2)}원")
            else:
                print("매수 실패")

        elif choice == "4":
            for i, ex in enumerate(exchanges):
                print(f"{i}. {ex.name} (보유량: {ex.holding})")
            idx = int(input("매도할 투자소 번호 입력: "))
            # 해당 투자소의 가격 변동 근거 및 변화율을 미리 준비
            evidence, reason_func, change = exchanges[idx].prepare_price_change()
            print(f"[{exchanges[idx].name}] 근거: {evidence} → 3초 후 가격 반영됨...")
            amount = int(input("몇 개 팔래? "))
            time.sleep(3)
            # 전체 투자소의 가격을 업데이트, 선택된 투자소(`skip_idx`)에는 위에서 준비한 변동폭과 이유를 적용, 나머지 투자소는 랜덤하게 빠르게 변화시킴 (simulate_price_quick)
            simulate_all_prices(exchanges, skip_idx=idx, selected_change=change, selected_func=reason_func)
            # 선택한 투자소에서 실제 매도 로직 실행 → 매도금액(income), 현재가(price), 손익(profit) 반환
            income, price, profit = exchanges[idx].sell(amount)
            if income > 0:
                user_money += income
                print(f"{round(income, 2)}원 받고 {amount}개 매도함.")
                print(f"수익: +{round(income, 2)}원 / 잔액: {round(user_money, 2)}원")
                print(f"매도 당시 가격: {round(price, 2)}원")
                print(f"손익: {'+' if profit >= 0 else ''}{round(profit, 2)}원")
            else:
                print("매도 실패")

        elif choice == "5":
            for ex in exchanges:
                ex.simulate_price_quick()
            show_all_status(exchanges)
            print(f"보유 현금은 {round(user_money, 2)}원입니다.")

        elif choice == "0":
            print("시뮬레이터를 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

# 프로그램 실행 시작점
if __name__ == "__main__":
    main()