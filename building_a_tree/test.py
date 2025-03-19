from hexlet import fs
tree = fs.mkdir('/', [fs.mkfile('hexlet.log')], {'hidden': True})
print(fs.get_name(tree))
print(fs.get_meta(tree).get('hidden'))

[file] = fs.get_children(tree)
print(fs.get_name(file))
# 'hexlet.log'
fs.get_meta(file).get('unknown')

# А вот так делать не надо
# У файлов нет потомков
fs.get_children(file)