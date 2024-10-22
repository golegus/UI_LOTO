from utils import *
import unittest
import random
from unittest.mock import patch

class TestCard(unittest.TestCase):

    def setUp(self):
        random.seed(42) #фиксируем seed, чтобы получить предсказуемые результаты
        self.card=Card("Игрок1")

    def test_card_creation(self):
        card = self.card.get()

        self.assertEqual(len(card),3)
        for group in card:
            self.assertEqual(len(group),5)

    def test_card_number_unigue(self):
        card = self.card.get()

        all_numbers = set()
        for group in card:
            all_numbers.update(group.keys())

        # Проверяем что все числа уникальны
        self.assertEqual(len(all_numbers), 15)

    def test_check_number(self):
        # Фиксируем набор чисел для тестов
        with patch('random.randint', side_effect=[5, 16, 27, 38, 49, 6, 17, 28, 39, 50, 7, 18, 29, 40, 51]):
            card = Card("Игрок2")

        self.assertTrue(card.check(5))
        self.assertTrue(card.check(16))
        self.assertFalse(card.check(100))
    
    def test_full_card(self):
        #Отметим все числа как True
        card = self.card
        for g in card.get():
            for num in g:
                card.check(num)
            
        #Проверяем что карточка полная
        self.assertTrue(card.full())


class TestOfBag(unittest.TestCase):

    def setUp(self):
        random.seed(42)
        self.bag=Out_Bag()

    def test_get_num(self):
        #проверяем первое случайное число
        num=self.bag.get_num()
        self.assertEqual(num, 82)

        #проверяем, что число добавлено в out_nums
        self.assertIn(num, self.bag.out_nums)

    def test_get_num_repeated_calls(self):

        num1 = self.bag.get_num()
        num2 = self.bag.get_num()
        self.assertNotEqual(num1, num2)
        self.assertEqual(len(self.bag.out_nums), 2)

    def test_get_num_raises_error_when_no_available_numbers(self):
        # мокаем список доступных чисел, чтобы имитировать, что все числа выбраны
        with patch.object(self.bag, 'out_nums', set(range(1, 91))):
            with self.assertRaises(ValueError):
                self.bag.get_num()

    def test_get_rest(self):
        self.bag.get_num()
        self.assertEqual(self.bag.get_rest(), 89)

if __name__=='__main__':

    unittest.main()


