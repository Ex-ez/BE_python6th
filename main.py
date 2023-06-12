class Engine:
    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine stopped"


class Wheels:
    def rotate(self):
        return "Wheels are rotating"


# 다중 상속
class Car(Engine, Wheels):
    pass


# 인스턴스 생성
my_car = Car()

# 부모 클래스의 메소드 사용
print(my_car.start())
print(my_car.rotate())
