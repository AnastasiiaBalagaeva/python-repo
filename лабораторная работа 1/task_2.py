# TODO Найдите количество книг, которое можно разместить на дискете

book_pages = 100
lines = 50
symbols = 25
one_char = 4
disk = 1.44 * 1024 * 1024
number_of_books = int(disk // (book_pages * lines * symbols * one_char))

print("Количество книг, помещающихся на дискету:", number_of_books)
