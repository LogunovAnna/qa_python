from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_rating_add_value_three_rating_changed(self):
        # тест метода set_book_rating
        # устанавливаем новый рейтинг(3) в экземпляре и проверяем что значение изменилось
        collector = BooksCollector()

        collector.add_new_book('Когда бог был кроликом')
        collector.set_book_rating('Когда бог был кроликом', 3)

        assert collector.get_book_rating('Когда бог был кроликом') == 3

    def test_set_book_rating_add_value_zero_rating_not_changed(self):
        # негативный тест метода set_book_rating
        # устанавливаем новый рейтинг(0) в экземпляре и проверяем что значение не изменилось
        collector = BooksCollector()

        collector.add_new_book('Однорукий аплодисмент')
        collector.set_book_rating('Однорукий аплодисмент', 0)

        assert collector.get_book_rating('Однорукий аплодисмент') == 1

    def test_get_books_with_specific_rating_add_two_books_one_book_received(self):
        # тест метода get_books_with_specific_rating
        # создаем 2 экземпляра, один из них с рейтингом 3. Проверяем, что метод вернул только один элемент
        collector = BooksCollector()

        collector.add_new_book('Однорукий аплодисмент')
        collector.add_new_book('Шампиньон моей жизни')
        collector.set_book_rating('Однорукий аплодисмент', 3)
        collector.set_book_rating('Шампиньон моей жизни', 5)
        assert 'Однорукий аплодисмент' in collector.get_books_with_specific_rating(3)

    def test_get_books_rating_add_one_book_one_book_received(self):
        # тест метода get_books_rating
        # создаем один экземпляра проверяем что длина словаря один
        collector = BooksCollector()

        collector.add_new_book('Шампиньон моей жизни')

        assert len(collector.get_books_rating()) == 1

    def test_add_book_in_favorites_add_one_book_one_book_received(self):
        # тест метода add_book_in_favorites
        # создаем экземпляр проверяем что он добавился в список избранного
        collector = BooksCollector()

        collector.add_new_book('Мой дедушка был вишней')
        collector.add_book_in_favorites('Мой дедушка был вишней')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_add_delete_one_book_zero_book_received(self):
        # тест метода delete_book_from_favorites
        # создаем экземпляр проверяем, добавляем и удаляем из списка избранного. Проверяем что список пуст
        collector = BooksCollector()

        collector.add_new_book('Однорукий аплодисмент')
        collector.add_book_in_favorites('Однорукий аплодисмент')
        collector.delete_book_from_favorites('Однорукий аплодисмент')

        assert len(collector.get_list_of_favorites_books()) == 0

