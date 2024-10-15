import random

class Card():
    '''
    класс Card - карточка игрока

    '''
    def __init__(self, name):
        self.name = name
        self.card = []
        all_keys = set()  # множество для хранения всех уникальных чисел
        for _ in range(3):
            group = set()
            tens_counter = [0] * 9  # список для учета количества чисел в каждом десятке (от 1 до 90)            
            while len(group) < 5:
                num = random.randint(1, 90)
                ten_group = (num - 1) // 10  # вычисляем к какому десятку принадлежит число
                if num not in all_keys and tens_counter[ten_group] == 0:
                    group.add(num)
                    all_keys.add(num)
                    tens_counter[ten_group] += 1  # отмечаем, что в этом десятке уже есть число
            # Сортируем группу и отмечаем числа как неотмеченные (False)
            sorted_group = {key: False for key in sorted(group)}
            self.card.append(sorted_group)

    def get(self):
        return self.card

    def check(self, num):
        for group in self.card:
            if num in group:
                group[num]=True
                return True
        return False
    
    def full(self):
        for group in self.card:
            if not all(group.values()):
                return False
        return True
    





class Out_Bag():
    '''
    Out_Bag - класс - бочонки, которые выбраны из мешка

    '''
    def __init__(self):
        self.out_nums = set()  # Множество для хранения выброшенных бочонков

    def get_num(self):
        # Множество чисел от 1 до 90
        full_set = set(range(1, 91))

        # Получаем доступные числа, исключая уже выбранные
        available_nums = full_set - self.out_nums

        # Проверяем, есть ли доступные числа для выбора
        if not available_nums:
            raise ValueError("Все числа уже выбраны из мешка")

        # Возвращаем случайное число из доступных
        num = random.choice(list(available_nums))

        # Добавляем выбранное число в out_nums
        self.out_nums.add(num)

        return num

    def get_rest(self):
        return 90-len(self.out_nums)
    


def print_card(card: Card):
    card_name=card.name
    len_name=len(card_name)  
    if len_name <26:
        count_prefix=int((26-len(card_name))/2)
        print('-'*count_prefix,f'{card_name}','-'*(26-(count_prefix+len_name)))

    for dictionary in card.get():
            formatted_keys = []
            cur_pos=8
            # print(f'key={key}; prev_key={prev_key}')
            for key in dictionary.keys():
                if key<10:
                    width=key
                    cur_pos=8-key
                else:
                    width  = cur_pos+key//10+2
                    cur_pos=-key//10

                if not dictionary[key]:
                    formatted_keys.append(f"{key:{width}}")
                else:
                    key='-'
                    formatted_keys.append(f"{key:{width}}")
            # Печатаем форматированные ключи с динамическим количеством пробелов

            print(" ".join(formatted_keys))
    print('-'*28)

def main():
    computer_card=Card('Карточка компьютера')
    my_card=Card('Ваша карточка')
    bag=Out_Bag()
    while bag.get_rest()>0:
        print_card(my_card)
        print_card(computer_card)
        cur_num=bag.get_num()
        print(f'Вытащили бочонок по номером {cur_num}. Осталось {bag.get_rest()} бочонков.')
        answer=input(f'Зачеркнуть цифру? y/n ')

        if answer=='y':
            if not my_card.check(cur_num):
                print(f'В Вашей карточке нет номера {cur_num}! Вы проиграли...')
                exit()

        if answer=='n':
            if my_card.check(cur_num):
                print(f'В Вашей карточке есть номер {cur_num}! Вы проиграли...')
                exit() 

        if my_card.full():
            print(f'Вы выиграли. Поздравляю!')
            exit()

        computer_card.check(cur_num)

        if computer_card.full():
            print(f'Компютер выиграл. Увы...')
            exit()



if __name__ == "__main__":
    
    main()
    