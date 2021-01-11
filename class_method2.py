class Car():
    '''
    Car class
    Author : Kim
    Date : 2020. 12. 12
    '''

    # 클래스 변수 선언 (모든 인스턴스가 공유 _ 모든 인스턴스가 공통적으로 참조하는 변수는 클래스 변수로 선언)
    car_count = 0


    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):  ## 이게 없으면 객체 조회시 Wrapping된 보기 어려운 정보로 표시
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):  ## 상기 Str와 유사하나, 개발자 관점에서 결과 출력시 사용
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Info : {} - {}'.format(self._company, self._details.get('price')))

# self의 의미 : 각 인스턴스는 고유의 아이디 아래 여러 속성값을 갖는다는 약속
car1 = Car("Hyundai", {'color':'White', 'horsepower':400, 'price':500})
car2 = Car("GM", {'color':'Red', 'horsepower':300, 'price':450})
car3 = Car("Ford", {'color':'Silver', 'horsepower':350, 'price':480})

# id 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__ 확인
print(dir(car1))   ## 내장되어 있는 매직 메소드 확인
print(car1)
print(car1.__dict__)   ## 내가 만든 네임스페이스만 보고 싶다면...

# Doctring
print(Car.__doc__)    # 클래스 설명 주석 출력

# detail info 메소드 실행
car2.detail_info()

# 비교
print(car1.__class__, car2.__class__)    ## 인스턴스의 모체가 되는 클레스 확인.. 전부 동일 값 출력
print(id(car1.__class__), id(car2.__class__), id(car3.__class__))  # 모체 클래스의 아이디이므로 전부 동일 값 출력

# 클래스 이름으로 인스턴스 접근하기
Car.detail_info(car3)

# 클래스 변수 설정 및 출력
print("모체 클래스를 통한 car 인스턴수의 개수 확인 : {}". format(Car.car_count))
print("개별 인스턴스를 통한 car 인스턴수의 개수 확인 : {}". format(car1.car_count))
print("개별 인스턴스를 통한 car 인스턴수의 개수 확인 : {}". format(car2.car_count))
## 클래스 변수는 클래스 본체와 각 인스턴스가 모두 공유하기 때문에 위의 값들은 모두 동일하게 나온다.

# 인스턴스 1개 삭제후 결과 보기
del car2
print("삭제후 car 인스턴수의 개수 확인 : {}". format(Car.car_count))
print("삭제후 car 인스턴수의 개수 확인 : {}". format(car1.car_count))



