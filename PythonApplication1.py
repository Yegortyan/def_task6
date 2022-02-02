#Функция, вычисляющая среднее арифметическое элементов массива. 
#Массив должен состоять из случайных чисел, длинной 10 элементов. 
import random
array = [random.randint(1, 10) for _ in range(1, 11) ]
def sred():
    print(sum(array) / len(array))
sred()