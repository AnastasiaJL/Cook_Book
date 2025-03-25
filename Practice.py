cook_book = {
    'Шарлотка': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Сахар', 'quantity': 100, 'measure': 'г'},
        {'ingredient_name': 'Мука', 'quantity': 100, 'measure': 'г'},
        {'ingredient_name': 'Яблоко', 'quantity': 1, 'measure': 'кг'}
    ],
    'Пюре': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Масло', 'quantity': 5, 'measure': 'г'},
        {'ingredient_name': 'Сливки', 'quantity': 5, 'measure': 'мл'}
    ],
    'Сендвич с тунцом': [
        {'ingredient_name': 'Тунец', 'quantity': 50, 'measure': 'г'},
        {'ingredient_name': 'Кукуруза', 'quantity': 25, 'measure': 'г'},
        {'ingredient_name': 'Хлеб', 'quantity': 2, 'measure': 'ломтик'},
        {'ingredient_name': 'Майонез', 'quantity': 1, 'measure': 'стол.л.'},
        {'ingredient_name': 'Яйцо', 'quantity': 1, 'measure': 'шт.'}
    ]
}

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish not in cook_book:
            print(f'Ошибка: блюда "{dish}" нет в книге рецептов.')
            continue

        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count

            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {'measure': measure, 'quantity': quantity}

    return shop_list


# Проверка работы
result = get_shop_list_by_dishes(['Сендвич с тунцом', 'Пюре'], 10)
print(result)
