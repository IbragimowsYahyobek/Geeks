class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
  
    def introduce_myself(self):
        married_status = "женат" 
        married_status_2 ="не замужем" 
        if self.is_married:
             print(f"Меня зовут {self.fullname}. Мне {self.age} лет. Я {married_status}.")
        else:
          print(f"Меня зовут {self.fullname}. Мне {self.age} лет. Я {married_status_2}.")


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience



person = Person("Яхе Ибрагимов", 30, True)
person.introduce_myself()

teacher = Teacher("Анна Ивановна", 45, False, 20)
teacher.introduce_myself()
print(f"Опыт преподавания: {teacher.experience} лет.")



