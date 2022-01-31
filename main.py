twenty_five = 25
about_pi = 3
total = twenty_five + about_pi
print(total)
twenty_five = "25"
about_pi = "3"
total = twenty_five + about_pi
print(total)
print("Символы " + "в кавычках — " + "это " + "строки.")
word1 = "Символы "
word2 = "в кавычках — "
word3 = "это "
word4 = "строки."
text = word1 + word2 + word3 + word4
print(text)

step_today = 8452
step_ysterday = 6783
step_sum = step_today + step_ysterday
print('Сколько шагов сделал Геннадий за два дня?')
print(step_sum)

six = 6
print(six * 7)

lol = 'хо'
print(lol * 10)

number = 100
rubles = " рублей"
print(str(number) + rubles)

one_hundred = '100'
five_hundred = '500'
print(int(one_hundred) + int(five_hundred))

count = 8
print("У вас" + str(count) + "новых сообщений")

count = 8
str1 = "У вас "
str2 = " новых сообщений"
message = str1 + str(count) + str2
print(message)

one_hundred = 100
print(one_hundred)

print(3 + 5)

print(3 + 5)
print('Всё в порядке!')

one_hundred = 100
five_hundred = '500'
print('В ответе можно получить 600, а можно и 100500!')
print(str(one_hundred) + str(five_hundred))
print('Вот мы и получили 100500')

one_hundred = 100
five_hundred = '500'
print('В ответе можно получить 600, а можно и 100500!')
print(int(one_hundred) + int(five_hundred))
print('Вот мы и получили 600')

one_hundred = "100"
five_hundred = "500"
print("В ответе можно получить 600, а можно и 100500!")
print(one_hundred + five_hundred)
print("Вот мы и получили 100500")


temperature = -25
weather = 'солнечно'
print("Сегодня", weather)
print("Температура воздуха", temperature, "градусов")

first = 87.2
second = 50.2
third = 50.242
print(first + second + third)

# Будет напечатано: 187.642

first = 87.2
second = 50.2
third = 50.242
print(str(first) + str(second) + str(third))

# Будет напечатано: 87.250.250.242

first = '87.2'   # Строка
second = '50.2'  # Тоже строка
third = '50.242' # И это строка
print(float(first) + float(second) + float(third)) # А в итоге получится число!

# Будет напечатано: 187.642

# Функция int() просто убирает всё, что после запятой. Вместе с запятой:
a = int(3.14)
print(a)

# Будет напечатано: 3

fraction = 1.5  # Дробь
print("Целая часть = " + str(int(fraction)))
# Вернётся строка, представляющая собой целочисленную часть дроби.
# Выполните этот код в окне тренажёра и посмотрите, что получится.

a = 16 * 2.2 + 7 - 0.2
print(a)

# Будет напечатано: 42.0

speed_kmh = 1079252848.8
speed_kms = int(speed_kmh / 3600)
print('Скорость света равна', speed_kms, 'км/с')

snake = "38.2"
length = 6.5
result = int(length * float(snake))
print('В вагоне можно поставить в ряд', result, 'попугаев')

snake = "38.2"
length = 6.5
result_0 = length * float(snake)
result = int(result_0)
print('В вагоне можно поставить в ряд', result, 'попугаев')

russian_alphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
print(russian_alphabet[1])
print(russian_alphabet[0])
print(russian_alphabet)


# сохраним в списках вторую и третью строки таблицы Пифагора
pithagoras_2 = [
    2*1, 2*2, 2*3, 2*4, 2*5, 2*6, 2*7, 2*8, 2*9
]
pithagoras_3 = [
    3*1, 3*2, 3*3, 3*4, 3*5, 3*6, 3*7, 3*8, 3*9
]
print(pithagoras_2)
print(pithagoras_3)


# Список может быть и из одного элемента; в списке trubadur лишь один Трубадур:
trubadur = ['Трубадур']

# А в другом списке - несколько музыкантов
animals = ['Кот', 'Пёс', 'Осёл', 'Петух']

# Но им нужен фронтмен-солист. И немаловажно, что это человек
# При сложении списков получится новый список
bremen_musicians = trubadur + animals

# Теперь в группе полно участников:
print(bremen_musicians)

# Будет напечатано: ['Трубадур', 'Кот', 'Пёс', 'Осёл', 'Петух']

count = len(bremen_musicians)
print(count)

# Будет напечатано: 5






print('Привет, я Анфиса!')

friends = [
    "Сергей", "Соня", "Дима", "Алина", "Егор"
]
print(friends)




friends = ['Сергей', 'Соня', 'Дима', 'Алина', 'Егор']
# присвойте переменной index такое значение,
# чтобы из списка friends была выбрана Алина
index = len(friends)
print('Привет, ' + friends[index] + ', я Анфиса!')







