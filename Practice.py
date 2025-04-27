cook_book = {}

with open('Recipes.txt', encoding='utf-8') as file:
    while True:
        dish_name = file.readline().strip()
        if not dish_name:
            break  # если блюдо не считалось — конец файла

        ingredients_count = int(file.readline().strip())
        ingredients = []

        for _ in range(ingredients_count):
            ingredient_line = file.readline().strip()
            name, quantity, measure = ingredient_line.split(' | ')
            ingredients.append({
                'ingredient_name': name,
                'quantity': int(quantity),
                'measure': measure
            })

        cook_book[dish_name] = ingredients
        file.readline()  # пропускаем пустую строку между блюдами

print(cook_book)

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
