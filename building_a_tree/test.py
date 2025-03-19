from hexlet import fs
tree = fs.mkdir('/', [fs.mkfile('hexlet.log')], {'hidden': True})
print(fs.get_name(tree))
print(fs.get_meta(tree).get('hidden'))

# [file] = fs.get_children(tree)
# print(fs.get_name(file))
# 'hexlet.log'

# Так делать не нужно, выведет None. Такого файла нет.
# print(fs.get_meta(file).get('unknown'))

# # А вот так делать не надо
# # У файлов нет потомков
# fs.get_children(file)

# Дополнительно есть такая функция 
# Проверяется, является ли tree директорией (результат - True).
print(fs.is_directory(tree))
# True

# Проверяется, является ли tree файлом (результат - False).
print(fs.is_file(tree))
# False

# Получаем дочерние элементы директории tree и присваиваем первый элемент списку file.
[file] = fs.get_children(tree)


# Проверяем, является ли file файлом (результат - True).
print(fs.is_file(file))
# True

# Проверяем, является ли file директорией (результат - False).
print(fs.is_directory(file))
# False
