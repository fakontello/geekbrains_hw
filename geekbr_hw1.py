print("Вас приветствует игра Путь питониста!\n")

gamer = {'name': input('Как вас зовут?\n'),
         'age': int(input('Сколько тебе лет?\n')),
         'sex': input('Укажите ваш пол\n'),
         'pet_name': input('Имя домашнего питомца\n'),
         'game_love': input('Вы любите играть?(Да/Нет)\n'),
         }

if int(gamer['age']) < 18:
    print('Вы ещё слишком молоды!')

if int(gamer['age']) >= 90:
    print(input('Играть может быть утомительно для Вас! Вы действительно хотите играть?(Да/Нет)\n'))
    if input == 'да':
        print(input('Вы уверены?'))
        if input == 'да':
            print("Хорошо тогда начнем игру")
    else:
        print("Всего доброго,", gamer['name'])
else:
    print('Добро пожаловать,', gamer['name'])

print('Я могу назвать буквы алфавита, которых нет в твоем имени и произнести их!')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in gamer['name']:
    if char in alphabet:
        alphabet = alphabet.replace(char, '')
print(alphabet)