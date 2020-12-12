## 예제 객체 만들기

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):  ## 이게 없으면 객체 조회시 Wrapping된 보기 어려운 정보로 표시
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):  ## 상기 Str와 유사하나, 개발자 관점에서 결과 출력시 사용
        return 'repr : {} - {}'.format(self._company, self._details)

car1 = Car("Hyundai", {'color':'White', 'horsepower':400, 'price':500})
car2 = Car("GM", {'color':'Red', 'horsepower':300, 'price':450})
car3 = Car("Ford", {'color':'Silver', 'horsepower':350, 'price':480})

print(car1)
print(car1.__dict__)


