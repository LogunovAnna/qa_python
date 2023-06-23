# qa_python
test_set_book_rating_add_value_three_rating_changed -тест метода set_book_rating присваеваем значение 3 ОР рейтинг изменится и будет равен 3

test_set_book_rating_add_value_zero_rating_not_changed - негативный тест метода set_book_rating присваеваем значение 0 ОР рейтинг не изменится

test_get_book_rating_add_two_books_both_rating_received - тест метода get_boos_rating создаем два элемента ОР рейтинг обеих книг совпадает со значениями в справочнике

test_get_books_with_specific_rating_add_four_books_two_books_received - тест метода get_books_with_specific_rating создаем четыре элемента ОР получаем две книги рейтинг которых равен заданному

test_get_books_rating_add_three_books_three_books_received - тест метода get_books_rating создаем три элемента ОР метод возвращает все три книги для проверки количества элементов преобразуем словарь в список

test_add_book_in_favorites_add_one_book_one_book_received - тест метода add_book_in_favorites создаем один элемент и добавляем его в список избранного ОР в списке избранного один элемент

test_delete_book_from_favorites_add_two_books_one_book_received - тест метода delete_book_from_favorites создаем два элемента, оба добавляем в список избранного ОР после вызова метода в списке избранного остался только один элемент

test_get_list_of_favorites_books_add_four_books_four_books_received - тест метода get_list_of_favorites_books создаем четыре элемента ОР метод возвращает четыре элемента
