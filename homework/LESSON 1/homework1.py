# -*- coding: utf-8 -*-
"""Homework1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c_awD2Ud_jqgzT7_kWsTJ5UTkqdqL8DS

**Вспомнить всё: if**

Напишите программу, которая считывает температуру в градусах Цельсия и выводит "ХОЛОДНО", если температура меньше 15.5,
"ЖАРКО", если температура больше 28, и "НОРМАЛЬНО" в остальных случаях.
"""

#Вспомнить всё: if
n = float(input())
if n < 15.5:
  print('ХОЛОДНО')
elif n > 28:
  print('ЖАРКО')
else:
  print('НОРМАЛЬНО')

"""**Найди кота**

Напишите программу, которая находит кота. Пользователь вводит сначала количество строк, потом сами строки.
Если хотя бы в одной введённой строке нашлось сочетание букв «Кот» или «кот», программа выводит «МЯУ», иначе программа выводит «НЕТ».
"""

#Найди кота
n = int(input('Введите необходимое количество строк '))
res = ''
for i in range(n):
  p = str(input())
  if 'кот' in p.lower():
    res = 'мяу'
print(res)

"""**Слова и буквы**

Напишите программу, которая считывает слова, слово «стоп» — сигнал остановки (оно не должно принимать участие в анализе). Из введённых слов нужно выбрать самое длинное и самое короткое (гарантируется, что все они имеют разную длину) и проверить, есть ли все буквы короткого слова в длинном. Вывести «ДА» или «НЕТ» в зависимости от этого.

"""

#Слова и буквы
import numpy as np
world = []
l = []
fn = ''
res = 'ДА'
while not('стоп' in fn):
  fn = str(input()).lower()
  world.append(fn)
  l.append(int(len(fn)))
d = ''.join(world[np.argmax(l[:-1])])
b = ''.join(world[np.argmin(l[:-1])])
# print(set(b) & set(d))
for i in range(len(b)):
  if b[i] in d:
    d = d.replace(b[i],'',1)
  else:
    res = 'НЕТ'
print(res)

"""**Список покупок**

Вы собираетесь в магазин и записываете, что нужно купить.
Напишите программу, которая считывает сначала количество покупок, потом по очереди сами эти покупки, затем выводит их же в том же порядке.

"""

#Список покупок
print(*[input() for i in range(int(input()))], sep='\n')

"""**Ххооллоодд**

Очень холодно, вы дрожите, зуб на зуб не попадает, разговариваете соответственно.
Формат ввода
Вводится одна строка.
Формат вывода
Выводится та же строка, но каждый символ повторяется дважды.

"""

#Ххооллоодд
print(*[i*2 for i in input()], sep='')

"""**Формальное приветствие**

Напишите функцию greet(), чтобы она спрашивала у пользователя имя и фамилию (каждое на отдельной строке), а затем выводила официальное приветствие в форме “Здравствуйте, {имя} {фамилия}.”.

"""

#Формальное приветствие
def greet(name, surname):
  print(f'Здравствуйте, {name} {surname}')

n = input('Введите имя ')
s = input('Введите фамилию ')
greet(n,s)

"""**Маленький колокольчик**

Написать класс LittleBell, который при вызове метода sound печатает слово ding.

Формат ввода

Каждый тест представляет собой код, в котором будет использоваться ваш класс. Файл c решением не обязательно называть solution.py, он будет переименован автоматически. Тест запускается с вашим классом, а его вывод сравнивается с правильным решением.

"""

from solution2 import LittleBell
bell = LittleBell()
bell.sound()
bell.sound()
bell.sound()

class LittleBell():
  def sound(self):
    print('ding')

bell = LittleBell()
bell.sound()
bell.sound()
bell.sound()

"""**Остаточные знания**

Программированием начала заниматься только в ВУЗе, в основном программа была нацелена на решение прикладных задач, поэтому в коде разбиралась постольку поскольку, в основном всегда давалась рыба, по которой делала задания, к тому же основным языком программирования был MATLAB.
Сама начала что-то изучать в прошлом году, когда попала на производственную практику на скучную работу, проходила курс на степике, основную сложность представляли циклы, собственно на них я и остановилась, иногда тяжело понять логику работы кода и что я должна сделать, до сих пор с ними путаюсь, особенно с вложенными, благо что в интернете полно информации. Иногда тяжело исправлять свои ошибки, особенно, когда код ошибку не выдает, а делает не то, что мне нужно. Но я думаю все это приходит с практикой
"""