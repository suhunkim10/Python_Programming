# 조건문 : if문, match문

age = 17

if age >= 18:
    print("성년")
else:
    print("미성년")

score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")


# match 문
grade = "A"

match grade:
    case "A":
        print("우수")  # break 자동
    case "B":
        print("양호")
    case "C":
        print("보통")
    case _:  # default에 해당
        print("알 수 없음")


# 반복문 : for문, while문

# while문
# 1 ~ 10까지 반복 출력
i = 0
while i < 10:
    i += 1
    print(i)
    if i == 5:
        break  # 반복문 종료
else:
    print("End")  # 반복문이 정상적으로 종료되었을 때만 실행

nums = [1, 3, 5, 7, 9]
target = 2
i = 0

while i < len(nums):
    if nums[i] == target:
        print("여깅네????????????")
        break
    i += 1
else:
    print("없어 이런 씨")

# 1 ~ 10까지의 합
# sum = 55
i = 0
tot = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    tot += i

print(f"sum = {tot}")
