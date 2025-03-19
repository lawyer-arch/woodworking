from hexlet import fs
tree = fs.mkdir('/', [fs.mkfile('hexlet.log')], {'hidden': True})
print(fs.get_name(tree))
print(fs.get_meta(tree).get('hidden'))