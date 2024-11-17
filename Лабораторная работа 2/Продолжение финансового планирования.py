def find_item_index(items, target):

    for index, item in enumerate(items):
        if item == target:
            return index
    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

search_items = ['банан', 'груша', 'персик']

for find_item in search_items:
    index_item = find_item_index(items_list, find_item)  # Вызов функции для получения индекса товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")