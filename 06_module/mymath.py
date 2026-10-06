# 사용자 정의 모듈
print("start:", __name__)
PI = 3.14


def add(a, b):
    return a + b


print(PI)
print(add(10, 20))


if __name__ is "__main__":
    print(PI)
    print(add(10, 20))
