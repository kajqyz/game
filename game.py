import random

# Глобальные переменные
inventory = []  
opened_doors = set() 
completed_tasks = set() 

# Словарь, который хранит информацию о дверях
doors = {
    'Входная дверь': {'code': '1', 'opened': False},
    'Секретная дверь': {'code': '2', 'opened': False},
    'Дверь в подземелье': {'code': '4', 'opened': False}
}

# Кортежи для координат объектов
key_position = (1, 2)
monster_positions = [(3, 4), (5, 6), (7, 8)]  # Множество монстров

# Оружие и его характеристики
weapons = {
    'меч': {'attack': 10, 'effect': 'Побеждает слабых монстров.'},
    'лук': {'attack': 8, 'effect': 'Позволяет атаковать на расстоянии.'},
    'щит': {'attack': 0, 'effect': 'Блокирует атаки монстра.'},
}

# Функции игры

def show_inventory():
    print("Ваш инвентарь:", inventory)

def take_item(item):
    if item not in inventory:
        inventory.append(item)
        print(f"Вы взяли {item}.")
    else:
        print(f"{item} уже в вашем инвентаре.")

def solve_puzzle(level):
    global opened_doors
    if level == 1:
        print("Задача 1: Найдите ключ, чтобы открыть дверь.")
        item = input("Что вы хотите сделать? (подсказка: взять ключ) ")
        if 'ключ' in item:
            take_item('ключ от входной двери')
            print("Ключ найден! Откройте дверь.")
            answer = input("Введите код для открытия двери: ")
            if answer == doors['Входная дверь']['code']:
                doors['Входная дверь']['opened'] = True
                print("Дверь открыта! Переходите ко второму уровню.")
                completed_tasks.add('первый уровень')
            else:
                print("Неверный код. Попробуйте еще раз.")
        else:
            print("Необходимо найти ключ для открытия двери.")
    elif level == 2:
        print("Задача 2: Победите монстра с помощью оружия!")
        if 'ключ от входной двери' in inventory:
            print("Монстр атакует! Используйте оружие для победы.")
            show_inventory()
            weapon = input("Какое оружие вы хотите использовать? (меч, лук, щит) ")
            if weapon in weapons and weapon in inventory:
                print(f"Вы использовали {weapon}!")
                if weapon == 'меч' or weapon == 'лук':
                    print(f"Вы победили монстра с помощью {weapon}.")
                    completed_tasks.add('второй уровень')
                elif weapon == 'щит':
                    print("Щит блокирует атаку монстра, но не убивает его.")
                elif weapon == 'магия':
                    print("Монстр повержен с помощью магии!")
                    completed_tasks.add('второй уровень')
            else:
                print("У вас нет такого оружия.")
        else:
            print("У вас нет нужного предмета для победы.")
    elif level == 3:
        print("Задача 3: Найдите секретный ключ.")
        print("Вы находитесь в комнате с двумя дверями.")
        action = input("Что вы хотите сделать? (подсказка: взять ключ от секретной двери) ")
        if 'ключ' in action:
            take_item('ключ от секретной двери')
            print("Теперь используйте этот ключ, чтобы открыть секретную дверь.")
            answer = input("Введите код для открытия двери: ")
            if answer == doors['Секретная дверь']['code']:
                doors['Секретная дверь']['opened'] = True
                print("Дверь открыта! Переходите к следующему уровню.")
                completed_tasks.add('третий уровень')
            else:
                print("Неверный код. Попробуйте еще раз.")
        else:
            print("Подсказка: вы не взяли ключ от секретной двери.")
    elif level == 4:
        print("Задача 4: Победите сильного монстра.")
        print("Вы столкнулись с страшным монстром!")
        if 'ключ от секретной двери' in inventory:
            action = input("Использовать ключ, чтобы убежать из замка или бороться с монстром? (введите 'сразиться с монстром' или 'использовать ключ') ")
            if 'сразиться' in action:
                print("Монстр повержен!")
                completed_tasks.add('четвертый уровень')
            elif 'ключ' in action:
                print("Вы использовали ключ, чтобы уйти, но ключ не работает.")
            else:
                print("Неверный выбор!")
        else:
            print("Необходимо иметь ключ для доступа к этой двери.")
    elif level == 5:
        print("Задача 5: Загадка и подземелье.")
        print("Вы достигли подземелья. Перед вами два пути: один ведет к выходу, другой — к ловушке.")
        puzzle = random.choice([
            ("Какой день недели идет после воскресенья?", "понедельник"),
            ("Какая планета находится ближе всего к Солнцу?", "меркурий")
        ])
        print(f"Загадка: {puzzle[0]}")
        answer = input("Ваш ответ: ")
        if answer == puzzle[1]:
            print("Вы разгадали загадку! Открывается путь к выходу.")
            print("Поздравляем, вы выиграли игру!")
            completed_tasks.add('пятый уровень')
        else:
            print("Неверный ответ. Попробуйте снова.")

def play_game():
    print("Добро пожаловать в замок!")
    take_item('меч')
    take_item('лук')
    while len(completed_tasks) < 5:
        if 'первый уровень' not in completed_tasks:
            solve_puzzle(1)
        elif 'второй уровень' not in completed_tasks:
            solve_puzzle(2)
        elif 'третий уровень' not in completed_tasks:
            solve_puzzle(3)
        elif 'четвертый уровень' not in completed_tasks:
            solve_puzzle(4)
        elif 'пятый уровень' not in completed_tasks:
            solve_puzzle(5)

play_game()