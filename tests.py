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

    # тест метода set_book_rating
    def test_set_book_rating_add_value_three_rating_changed(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавление книги проверяется в отдельном тесте, поэтому здесь заполняю экземпляр класса самостоятельно
        collector.books_rating = {'Когда бог был кроликом': 1}
        # установление рейтинга 3 книге
        collector.set_book_rating('Когда бог был кроликом', 3)

        # проверяю что рейтинг изменился и равен 3
        assert collector.books_rating['Когда бог был кроликом'] == 3

    # негативный тест метода set_book_rating
    def test_set_book_rating_add_value_zero_rating_not_changed(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавление книги проверяется в отдельном тесте, поэтому здесь заполняю экземпляр класса самостоятельно
        collector.books_rating = {'Однорукий аплодисмент': 2}
        # установление рейтинга 2 книге
        collector.set_book_rating('Однорукий аплодисмент', 0)

        # проверяю что рейтинг изменился и равен 2
        assert collector.books_rating['Однорукий аплодисмент'] == 2

    # тест метода get_books_rating
    def test_get_books_rating_add_two_books_both_rating_received(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавление книги проверяется в отдельном тесте, поэтому здесь заполняю экземпляры класса самостоятельно
        collector.books_rating = {'Однорукий аплодисмент': 3, 'Шампиньон моей жизни': 5}

        # получаем рейтинг обеих книг
        assert collector.get_book_rating('Однорукий аплодисмент') == 3 and collector.get_book_rating(
            'Шампиньон моей жизни') == 5

    # тест метода get_books_with_specific_rating
    def test_get_books_with_specific_rating_add_four_books_two_books_received(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавление книги проверяется в отдельном тесте, поэтому здесь заполняю экземпляры класса самостоятельно
        collector.books_rating = {'Однорукий аплодисмент': 3, 'Шампиньон моей жизни': 5, 'Когда бог был кроликом': 1,
                                  'Мой дедушка был вишней': 3}

        # проверяем что в списке только две книги
        assert len(collector.get_books_with_specific_rating(3)) == 2

    # тест метода get_books_rating
    def test_get_books_rating_add_three_books_three_books_received(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавление книги проверяется в отдельном тесте, поэтому здесь заполняю экземпляры класса самостоятельно
        collector.books_rating = {'Шампиньон моей жизни': 5, 'Когда бог был кроликом': 1, 'Мой дедушка был вишней': 3}

        # преобразовываем словарь в список и проверяем что в нем три элемента
        assert len(list(collector.get_books_rating()))

    # тест метода add_book_in_favorites
    def test_add_book_in_favorites_add_one_book_one_book_received(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавление книги проверяется в отдельном тесте, поэтому здесь заполняю экземпляр класса самостоятельно
        collector.books_rating = {'Мой дедушка был вишней': 10}
        # вызываю метод
        collector.add_book_in_favorites('Мой дедушка был вишней')

        # проверяю что в список избранного добавилась книга
        assert len(collector.favorites) == 1

    #тест метода delete_book_from_favorites
    def test_delete_book_from_favorites_add_two_books_one_book_received(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавление книги проверяется в отдельном тесте, поэтому здесь заполняю экземпляр класса самостоятельно
        collector.books_rating = {'Мой дедушка был вишней': 10, 'Однорукий аплодисмент': 3}
        # добавление в список избранного проверяется отдельным тестом, поэтому здесь создаю список избранного
        collector.favorites = ['Мой дедушка был вишней', 'Однорукий аплодисмент']
        # вызываю метод
        collector.delete_book_from_favorites('Однорукий аплодисмент')

        # проверяю что в списоке избранного одна книга
        assert len(collector.favorites) == 1

    # тест метода get_list_of_favorites_books
    def test_get_list_of_favorites_books_add_four_books_four_books_received(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавление книги проверяется в отдельном тесте, поэтому здесь заполняю экземпляры класса самостоятельно
        collector.books_rating = {'Однорукий аплодисмент': 10, 'Шампиньон моей жизни': 10, 'Когда бог был кроликом': 10,'Мой дедушка был вишней': 10}
        # добавление в список избранного проверяется отдельным тестом, поэтому здесь создаю список избранного
        collector.favorites = ['Однорукий аплодисмент', 'Шампиньон моей жизни', 'Когда бог был кроликом','Мой дедушка был вишней']

        # получаю список избранного проверяю его длину
        assert len(collector.get_list_of_favorites_books()) == 4


