# TODO Найдите количество книг, которое можно разместить на дискете

inf_size = 1.44
size_book = 100
strings = 50
symbols = 25
size_symbols = 4

print("Количество книг, помещающихся на дискету:", round((inf_size * 1024 * 1024) // (size_book * strings * symbols * size_symbols)))