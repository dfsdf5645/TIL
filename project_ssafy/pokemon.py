#의로받음
#푸키먼이라는 게임 만들어
#가상세계의 동물들 있는데
#각각 고유의 lv, hp, skill, info를 가진 생명체들
#둘이만나게되면 싸우는데 한명 hp가 0될때까지 싸움

#공통속성 가진 객체 정의
#클래스명 정의시 ClassName -> Pascal Case -> 단어 기준으로 앞글자 대문자로
class Pokemon:
    #모든 푸키먼들이 공통으로 가지는 속성
    #클래스 변수
    info = '푸키먼...'
    population = 0

    #생성자
    #매직 메서드 -> __name__
    #인스턴트 메서드 -> 첫번째 인자는 자기 자신
    #함수정의하는것과 동일 -> 모든 규칙 똑같이 작동 기본/가변인자 다 가능
    def __init__(self, name, lv=1):
        #classmethod인 increase를 호출할건데
        Pokemon.increase()

        #인스턴스 변수에 생성될때 넘겨받은 이름을 할당
        self.name = name
        self.lv = lv
        #스킬명과 공격력
        self.skill = ('몸통박치기', 10)
        self.hp = 100

        #본인만의 독특한 소개법
        self.info = self.name[:2] * 2

    #행동정의
    #인스턴스 메서드 -> 첫번째 인자로 self넘겨받고
    def attack(self):
        print(f'{self.info}')
        return self.skill[1] #공격력

    @classmethod
    def increase(cls):
        cls.population += 1

    #첫번째 인자로 self, cls 둘 다 받지 않음
    @staticmethod
    def battle(pok1, pok2): #함수 정의와 동일
        #영원히
        while True:
            pok2.hp -= pok1.attack()
            if pok2.hp <= 0:
                print(f'{pok2.name}이 쓰러졌다!')
                return
            pok1.hp -= pok2.attack()
            if pok1.hp <= 0:
                print(f'{pok1.name}이 쓰러졌다!')
                return


print(Pokemon.population, '피카츄 태어나기 전')
pika = Pokemon('피카츄') #새로운 객체 생성, pika에 할당
print(Pokemon.population, '피카츄 태어난 후')
# pika == Pokemon의 인스턴스
#생성자에는 2개의 인자 넣어주기로 함
#lv은 기본값이 있어서 이름만 넣어도 됨
print(pika.name)
print(pika.population) #접근해서 출력은 가능한데
print(pika.lv, pika.skill, pika.hp)
print(pika.info) #info = class 속성 pika, meta info 같음
pika.attack()

#똑같이 Pokemon에 해당하는 새로운 객체 생성
meta = Pokemon('메타몽', 5)
print(meta.lv, meta.skill, meta.hp)

pika.population += 1
print(pika.population) #1
print(Pokemon.population) #0
meta.attack()

Pokemon.battle(pika, meta)