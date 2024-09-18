# class Fruits:
#     def __init__(self, name, color, weight):
#         self.name = name 
#         self.color = color
#         self.weight = weight

#     def info(self):
#         print(f'название фрукта - {self.name}, цвет - {self.color}, масса - {self.weight}')

# result = Fruits('яблоко', 'красный', 'масса 1,5 кг' )
# result.info() 


class Book:
    def __init__(self, title, author, pages,):
        self.title = title
        self.author = author
        self.pages = 359

    def info(self):
        print(f'название книги - {self.title}, автор книги - {self.author}, колтчество страниц - {self.pages}')
    def check_pages(self):
        if self.pages < 100:
            print(f'Книга "{self.title}" тонкая (менее 100 страниц).')
        elif 100 <= self.pages <= 300:
            print(f'Книга "{self.title}" средняя (100-300 страниц).')
        else:
            print(f'Книга "{self.title}" толстая (более 300 страниц).')

result = Book('Путь фуболиста', 'Yahyo', 250)
result.info()
result.check_pages()
