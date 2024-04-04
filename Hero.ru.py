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