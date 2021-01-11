class Car():
    '''
    Car class
    Author : Kim
    Date : 2020. 12. 12
    Description : Class, Static, Instance Method
    '''

    # 클래스 변수 선언 (모든 인스턴스가 공유 _ 모든 인스턴스가 공통적으로 참조하는 변수는 클래스 변수로 선언)
    price_per_rate = 1.0   ## 예컨데, 자동차에 적용되는 관세율

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):  ## 이게 없으면 객체 조회시 Wrapping된 보기 어려운 정보로 표시
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):  ## 상기 Str와 유사하나, 개발자 관점에서 결과 출력시 사용
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method
    ## self : 객체의 고유한 속성 값을 사용한다는 약속
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Info : {} - {}'.format(self._company, self._details.get('price')))

    # Instance Method
    def get_price(self):
        return 'Original Car Price => Company: {}, price: {}'.format(self._company, self._details['price'])

    # Instance Method
    def raising_price(self):
        return 'Changed Car Price => Company: {}, price: {}'.format(self._company, self._details['price']* Car.price_per_rate)

    # Class Method
    @classmethod
    def raise_price(cls, per):   # 여기서 cls는 모체인 Car Class를 의미함, per만 실제로 받는 변수
        # 인스턴스 매소드는 변수로 self를 받고, 클래스 매소드는 변수로 클래스를 받는다.
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_rate = per
        print('Succeed! price increased')

    # Static Method  (스태틱 변수는 따로 없다.)
    @staticmethod
    def is_hyundai(inst):
        if inst._company == 'Hyundai':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry. This car is not Hyundai'


# self의 의미 : 각 인스턴스는 고유의 아이디 아래 여러 속성값을 갖는다는 약속
car1 = Car("Hyundai", {'color':'White', 'horsepower':400, 'price':500})
car2 = Car("GM", {'color':'Red', 'horsepower':300, 'price':450})
car3 = Car("Ford", {'color':'Silver', 'horsepower':350, 'price':480})

# 전체 정보 출력
car1.detail_info()

# 가격 정보만 출력  (아래처럼 직접 접근하는 방법은 좋지 않다. 따로 메소드를 만들어서 접근하는게 정석)
print(car1._details.get('price'))
print(car1._details['price'])

# 추가한 인스턴스 매소드를 통해 가격 출력
print(car1.get_price())
print(car1.raising_price())

# 가격 인상율에 대한 클래스 변수를 조작하기 위한 클래스 매소드를 생성후 조작
Car.raise_price(1.5)

# 클래스 매소드를 통해 수정한 인상율이 잘 적용되었는지 확인
print(car1.get_price())
print(car1.raising_price())

# 스태틱 매소드를 활용한 차량의 제조사 확인
print(Car.is_hyundai(car1))
print(Car.is_hyundai(car2))