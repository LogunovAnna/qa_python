# qa_python
Проект qa_python Sprint2 - тренировка применения pytest

Использованые библиотеки: дополнительные библиотеки не используются

Зависимостей нет

Описание добавленных тестов:

test_set_book_rating_add_value_three_rating_changed - тест метода set_book_rating присваеваем значение 3 ОР рейтинг изменится и будет равен 3

test_set_book_rating_add_value_zero_rating_not_changed - негативный тест метода set_book_rating присваеваем значение 0 ОР рейтинг не изменится

test_get_books_with_specific_rating_add_two_books_one_book_received - тест метода get_books_with_specific_rating создаем два элемента ОР получаем книгу рейтинг которой равен заданному

test_get_books_rating_add_one_book_one_book_received - тест метода get_books_rating создаем элемент ОР метод возвращает словарь длиной 1

test_add_book_in_favorites_add_one_book_one_book_received - тест метода add_book_in_favorites создаем один элемент и добавляем его в список избранного ОР в списке избранного один элемент

test_delete_book_from_favorites_add_delete_one_book_zero_book_received - тест метода delete_book_from_favorites создаем два элемента, оба добавляем в список избранного ОР после вызова метода в списке избранного остался только один элемент

