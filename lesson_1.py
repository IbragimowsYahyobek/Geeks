# # full_name = 'aslan' #змеиный регистр

# # FullName = 'жибек' #verblijiy registr

# class Car: #shablon ili je chertej
#     def __init__(self, marka, model,  color): #__init__(mogicheskiy metod) qonstruktor
#     # atribut obekta 
#       self.marka = marka
#       self.model = model # self (ssilka na tekushiy obekt 
#       self.color = color 
#     # atribut classa
#       self.bak = 10
#       self.is_start = False

#     def info(self):
#         print(f"marka mashini - {self.marka}, model - {self.model}, svet - {self.color}")

#     def start(self):
#         if self.bak > 0:
#               self.is_start = True
#               print(f"mashina {self.marka} - {self.model} zavedena ")
#         else: 
#          print(f"mashina {self.marka} - {self.model} net topliva ")


#     def stop(self):
#         self.is_start = False
#         print(f"mashina {self.marka} - {self.medel} zaglusheno ")
    
#     def drive(self, city):
#         if self.is_start == True:
#          print(f"mashina {self.marka} = {self.model} edet v {city}")
#         else:
#            print(F"mashina {self.marka} - {self,model } ne zavedena ")

           

# bmw = Car('BMW', 'M5 F90', 'black')
# bmw.info()
# bmw.start()
# bmw.stop()
# bmw.drive()


# class Book:
#     def __init__(self, avtor, book_name, year):
#         self.avtor = avtor
#         self.book_name = book_name
#         self.year = year

#     def info(self):
#         print(f'avtor knigi - {self.avtor}, nazvanie knigi - {self.book_name}, god - {self.year}')
         

    

#     result = Book('Пушкин', 'Капитанская дочь', '1836')
#     result.info()  