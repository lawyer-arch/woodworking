import copy
from hexlet import fs


def change_owner(node, owner):
    name = fs.get_name(node)
    new_meta = copy.deepcopy(fs.get_meta(node))
    new_meta['owner'] = owner
    if fs.is_file(node):
        # Возвращаем обновленный файл
        return fs.mkfile(name, new_meta)
    children = fs.get_children(node)
    # Ключевая строчка
    # Вызываем рекурсивное обновление каждого потомка
    new_children = list(map(lambda child: change_owner(child, owner), children))
    new_tree = fs.mkdir(name, new_children, new_meta)
    # Возвращаем обновленную директорию
    return new_tree


# Строку кода с №15 можно заменить на цикл for 
# new_children = [chnge_owner(child, owner) for child in children] 
# Это упростит код и даст возможность легко изменить при необходимости
