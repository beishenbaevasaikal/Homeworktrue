class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_point, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_point = health_point
        self.catchphrase = catchphrase

    def get_name(self):
        print('Имя героя: ', self.name)

    def double_health(self):
        print(self.health_point * 2)


    def __str__(self):
        return (f"Прозвище: {self.nickname}, Суперсила: {self.superpower}, Очки здоровья: {self.health_point}")

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero("Сайтама", 'Ванпанчмен', 'Невероятная сила',
                 100, 'Комары...Бесят!')

hero.get_name()
hero.double_health()
print(hero)
print(len(hero))

class Airhero(SuperHero):
    def __init__(self, name, nickname, superpower, health_point, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_point, catchphrase)
        self.damage = damage
        self.fly = fly
class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_point, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_point, catchphrase)
        self.damage = damage
        self.fly = fly

class AirHero(SuperHero):
    def double_health(self):
        print(self.health_point ** 2)

class EarthHero(SuperHero):
    def double_health(self):
        print(self.health_point ** 2)

    def true_in_true_phrase(self):
        print("True in the true phrase is")

air_hero = AirHero("Гароу", 'Человек монстр', 'Сверхчеловеческие физические характеристики',
                   80, 'Время творить зло!')

earth_hero = EarthHero("Бэт", 'Стальная бита', 'Крайняя выносливость', 70,
                       'Герои никогда не проигрывают')

air_hero.double_health()
earth_hero.double_health()

class Villain(SuperHero):
   people = 'monster'

   def gen_x(self):
       pass

   def crit(self, damage):
       return damage ** 2


villain = Villain("Хаяте", 'Штурмовой ветер', 'Суперскорость', 100, 'С помощью своих сил, мы хотим правит миром')

