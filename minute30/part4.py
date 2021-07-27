# ==============================
# class
#   이름 첫글자 대문자
# ==============================

# class Car(object):
class Car:
    maxSpeed = 300
    maxPeople = 5

    def start(self):
        print("Run")

    def stop(self):
        print("Stop")

    # 매직메서드
    def __str__(self):
        return "Hello World"

    def __init__(self):
        print("{} 생성자".format(type(self)))


k9 = Car()
print(k9.maxSpeed)
# print(type(k9))
# print(dir(k9))


class Hybrid(Car):
    battery = 1000
    batteryKM = 300


k9h = Hybrid()
print(k9h)
print(k9h.maxSpeed)

# ==============================
# 빌트인 펑션
#   ref https://docs.python.org/3/library/functions.html
#   print
#   sum
#   max: 가장 큰 값
#   min: 가장 작은 값
#   abs: 절대값
#   bin: 형변환
# ==============================
