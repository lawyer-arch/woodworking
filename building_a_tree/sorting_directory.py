from hexlet import fs
import copy

# Создаем директорию с вложенными узлами с именем "/"

tree = fs.mkdir('/', [
    fs.mkfile('one'),
    fs.mkfile('two'),
    fs.mkdir('three'),
])

# Получаем список дочерних элементов корневой директории
children = fs.get_children(tree)
# print(children)

# Создаем глубокую копию метаданных корневой директории
new_meta = copy.deepcopy(fs.get_meta(tree))


# Клонируем список дочерних элементов
new_children = children[:]

# Разворачиваем список дочерних элементов в обратном порядке
new_children.reverse()

# Создаем новое дерево файловой системы с тем же именем, отсортированными дочерними элементами и новыми метаданными
tree2 = fs.mkdir(fs.get_name(tree), new_children, new_meta)

# Получаем имена дочерних элементов нового дерева и возвращаем их в виде списка
print(list(map(fs.get_name, fs.get_children(tree2))))
# ['three', 'two', 'one']