def main():
    files = ['Esenin.txt', 'Recipes.txt']
    result = []

    for file in files:
        with open(file, encoding='utf-8') as f:
            lines = f.readlines()
            result.append((file, len(lines), lines))

    result.sort(key=lambda x: x[1])

    for file_name, line_count, lines in result:
        print(file_name)
        print(line_count)
        for line in lines:
            print(line.strip())
        print()  # Пустая строка между файлами

if __name__ == '__main__':
    main()

