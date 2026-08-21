# 변수

a = 2
b = 3
print(a, b)

# a = 2, b = 3
# a = (2, b) = 3

a = 2
b = 3
a, b = 2, 3  # 권장
print(a, b)

# 값 swap
temp = a
a = b
b = temp
print(a, b)

a, b = b, a
print(a, b)

# 변수명 규칙(C와 동일)
# 알파벳, 숫자, 특문(_)만 가능
# 숫자로 시작 X
# 예약어 금지
i_hate_kwakhyeonjin = 1

# name! = "뽀로로"
# 2name = "크롱"
_age = 17
# class = "클래수"

이름 = "뽀로로 카운터"
print(이름)

student_name = "크롱"  # snake
studentName = "크롱"  # camel

MAX_SCORE = 100
