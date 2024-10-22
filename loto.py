from utils import Card, Out_Bag


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
    