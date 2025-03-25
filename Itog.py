files = ["Esenin.txt", "Recipes.txt"]  # Просто имена файлов

file_contents = []
for file in files:
    with open(file, encoding="utf-8") as f:
        lines = f.readlines()
        file_contents.append((file, len(lines), lines))

file_contents.sort(key=lambda x: x[1])  # Сортируем по количеству строк

for file_name, line_count, lines in file_contents:
    print(f"{file_name}\n{line_count}")  # Выводим имя файла и количество строк
    print("".join(lines))  # Выводим содержимое файла
    print()  # Добавляем пустую строку между файлами
