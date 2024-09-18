# """ Объектно ориентированное программирование """

# " Наследование и множественное наследование "

# class Game:
#     def __init__(self, game_name, graphics, game_year, company):
#         self.game_name = game_name
#         self.graphics = graphics
#         self.game_year = game_year
#         self.company = company
        
#     def info(self):
#         print(f"Название игры - {self.game_name}, максимальная графика - {self.graphics}, дата релиза - {self.game_year}, создатели - {self.company}")
        
# game = Game('CsGO', 'FULL HD 4K', 2013, 'Valve')
# # game.info()

# class Roblox(Game):
#     def __init__(self, game_name, graphics, game_year, company, multiplayer):
#         super().__init__(game_name, graphics, game_year, company)
#         # Game.__init__(game_name, graphics, game_year, company)
#         self.multiplayer = multiplayer
#         self.name = 'player'
#         self.gender = 'man'
#         self.skin = 'VIP'
#         self.hp = 100
        
#     # def info(self):
#     #     print(f"Название игры - {self.game_name}, максимальная графика - {self.graphics}, дата релиза - {self.game_year}, создатели - {self.company}, мультиплеер - {self.multiplayer}")
    
#     def info_player(self):
#         print(f"Игрок - {self.name}, Пол - {self.gender}, Облик - {self.skin}, Здоровье - {self.hp}")
#         print('=========================\nROBLOX - запустился и готов к игре!')

#     def edit_player(self):
#         name = input("vvedite imya igroka: ")
#         gender = input("vvedite pol igroka: ") 
#         skin = input("vvedite oblik personaja: ")
#         self.name = name 
#         self.gender = gender
#         self.skin = skin
    
    
# roblox = Roblox("Roblox", 'ULTRA', '2006', 'Roblax Corporation', "Да")
# # roblox.info()
# # roblox.edit_player()
# # roblox.info_player()

# class Snake(Roblox):
#     def __init__(self, name, gender, skin):
#         self.name = name 
#         self.gender = gender
#         self.skin = skin 
#         self.hp = 100

# snake = Snake('beka', 'men', 'platinium')
# snake.info_player()


class Animal:
    def __init__(self, name):
       self.name = name 

    def eat(self):
        print(f"{self.name}  est" )

    def sleep(self):
        print(f"{self.sleep}  spit ")

class Walker(Animal):
    def __init__(self, name):
        self.name = name 
        
animal = Animal('jivotnoye') 
animal.eat()
animal.sleep()