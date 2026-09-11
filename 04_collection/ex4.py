# 튜플 심화

# ===========================================================
#  튜플에서 제공하는 메소드
# ===========================================================

t = (1, 1, 2, 2, 2)

# 1이 몇개 있는지?
print(t.count(1))

# 2의 첫번째 인덱스는?
print(t.index(2))

# ===========================================================
#  그 외
# ===========================================================

# tuple -> list 변환
l = list(t)
print(l)

# list -> tuple 변환
t = tuple(l)
print(t)

# 튜플을 이용해서 swap하기
a, b = 10, 20

# 튜플 언패킹
t = (1, 2, 3, 4)
print(*t)

a, b, c, d = t
print(a, b, c, d)

a, *b, c = t
print(a, b, c)

t2 = (5, 6)
print((*t, *t2))

# zip 함수 사용
subjects = ("국어", "수학", "영어")
scores = (80, 90, 95)

# (('국어', 80), ('수학', 90), ('영어', 95)) 출력하기
print(tuple(zip(subjects, scores)))

# ===========================================================
#  Tuple Comprehension은 없음
# ===========================================================

# generator 표현식

gen = (x for x in range(1, 11))
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i, end=" ")
print()

for i in gen:
    print(i, end=" ")
print()

# List Comprehension vs Generator 표현식
a = [x for x in range(1, 11)]
b = (x for x in range(1, 11))

print(sum(a), sum(a))
print(sum(b), sum(b))

# 1 ~ 10의 제곱수 튜플 만들기
# ()는 튜플이 아니라 generator를 생성하는 generator 표현식임
result = tuple(x**2 for x in range(1, 11))
print(result)

# tuple의 생성자에 generator를 넘겨 값을 순회하면서 튜플을 만듦

# 두 점의 x, y, z축 좌표값끼리 더한 튜플을 만들기
p1 = (1, 2, 3)
p2 = (10, 20, 30)
print(tuple(a + b for a, b in zip(p1, p2)))

# =========================================================
#  🔥 실습 문제
# =========================================================

# 일주일 동안의 학습 시간을 저장한 튜플
days = ("일", "월", "화", "수", "목", "금", "토")
hours = (2, 3, 1, 4, 5, 2, 6)

# 1️⃣ 월 ~ 금까지 총 학습시간 출력하기
# ✅ 15시간
print(sum(hours))

# 2️⃣ 가장 많이 공부한 시간 출력하기
# ✅ 6시간
print(max(hours))


# 3️⃣ 가장 많이 공부한 요일 출력하기
# ✅ 토요일
print(days[hours.index(max(hours))])
hour, day = max(zip(hours, days))
print(day)

# 4️⃣ 가장 높은 점수와 가장 낮은 점수 출력하기
scores = (90, 85, 78, 92, 88, 76)
print(min(x for x in scores), max(x for x in scores))

result = sorted(scores)
print(result[-1], result[0])

# ✅ max 점수: 92점, min 점수: 76점


# 5️⃣ 과일가게 총 재고 금액 구하기
stocks = (
    ("사과", 1000, 5),
    ("바나나", 2000, 3),
    ("체리", 5000, 2),
)

# 품목, 가격, 수량 튜플 만들기

# ✅ ('사과', '바나나', '체리')
# ✅ (1000, 2000, 5000)
# ✅ (5, 3, 2)

# 총 재고 금액 출력
total = sum(price * num for name, price, num in stocks)

print(total)

# ✅ 총액: 21,000원


stocks = (
    ("사과", "바나나", "체리"),
    (1000, 2000, 5000),
    (5, 3, 2),
)

print(*stocks)
total = sum(price * num for _, price, num in zip(*stocks))
print(total)
