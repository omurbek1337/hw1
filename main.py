class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def names(self):
        return self.name

    def double_health(self):
        return self.health_points * 2

    def __str__(self):
        return f" его  прозвище {self.nickname}  его супер  {self.superpower}  и  его здоровье { self.health_points}"

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero('Mirlan', 'LOrd', 'BLASTERs', 100, "im not died")

print(hero.names())
print(hero.double_health())
print(hero)
print(len(hero.catchphrase))
