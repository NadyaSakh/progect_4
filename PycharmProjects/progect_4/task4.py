"""

Вариант 7

Задача 7
Дан файл с текстом. Написать скрипт, который форматирует текст к следующему стилю:

1) Название файла выводится в самом начале текста, центрируется и выводится заглавными буквами.
2) Весь текст выравнивается по центру
3) Каждый абзац разделен пустой строкой
4) Начало каждого абзаца содержит отступ от левого края в 4 пробела и начинается с большой буквы.
5) В конце документа имя и фамилия автора.

"""


def read_function(lines):
    try:
        with open('derevensky_mag.txt', 'r', encoding="windows-1251") as my_file:
             lines = my_file.readlines()
    except FileNotFoundError:
        print("Ошибка: Файл не найден")
        quit()

    return lines, my_file


def write_function(out_lines):
    with open("output.txt", "w+") as new_file:
        for line in out_lines:
            new_file.write(line)


def find_max_string(lines):
    try:
        max_length = len(max(lines, key= lambda string: len(string)))
        return max_length
    except ValueError:
        print("Ошибка: Файл пустой")
        quit()


def write_title(out_lines, my_file, length):
    title_upper = "{}\n".format(my_file.name.upper().center(length))
    out_lines.append(title_upper)
    return out_lines


def write_author(out_lines, length):
    author = "\n{}".format("Автор текста: Евгений Исаев.".center(length))
    out_lines.append(author)
    return out_lines


def write_main_text(lines, out_lines, length):
    for line in lines:
        line = line.strip("\n")
        if line.find('\t'):  # если абзац начинается с табуляции
            line = line.replace('\t', '    ')
        if line.startswith('    '):  # если строки нвчинаются с 4 пробелов
            iterator = 1
            space_index = line.find('    ')
            while not line[space_index + iterator].isalpha():  # находим первую функцию в строке
                iterator += 1
            upper_char = line[space_index + iterator].upper()
            line = line[:space_index + iterator] + upper_char + line[space_index + iterator + 1:]
            line = "\n    {}\n".format(line.center(length))
            out_lines.append(line)
        else:  # отдельные строки не с нового абзаца
            line = "{}\n".format(line.center(length))
            out_lines.append(line)
    return out_lines


def main():
    lines = []
    out_lines = []

    lines, my_file = read_function(lines)
    length = find_max_string(lines)
    write_title(out_lines, my_file, length)
    write_main_text(lines, out_lines, length)
    write_author(out_lines, length)
    write_function(out_lines)

if __name__ == "__main__":
    main()
