class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @property
    def memory(self):
        return self.__memory

    def __make_computations(self):
        addition = self.__cpu + self.__memory
        subtraction = self.__cpu - self.__memory
        multiplication = self.__cpu * self.__memory
        division = self.__cpu / self.__memory 
        return addition, subtraction, multiplication, division

    def display_results(self):
        addition, subtraction, multiplication, division = self.__make_computations()
        print(f'Сложение (cpu + memory): {addition:.2f}')
        print(f'Вычитание (cpu - memory): {subtraction:.2f}')
        print(f'Умножение (cpu * memory): {multiplication:.2f}')
        print(f'Деление (cpu / memory): {division if isinstance(division, str) else f"{division:.2f}"}')

    def info(self):
        print(f'Компьютер: CPU={self.__cpu}, Memory={self.__memory}')

class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card

    @property
    def memory_card(self):
        return self.__memory_card

    def info(self):
        super().info()  
        print(f'Карта памяти: {self.__memory_card}')

computer = Computer(3.5, 16)  
laptop = Laptop(2.6, 8, 512) 

computer.display_results()
laptop.display_results()

computer.info()
laptop.info()

print(f'CPU компьютера: {computer.cpu}')
print(f'Memory ноутбука: {laptop.memory}')
print(f'Карта памяти ноутбука: {laptop.memory_card}')

