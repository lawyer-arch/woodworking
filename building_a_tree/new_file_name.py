from hexlet import fs
import copy

file = fs.mkfile('one', {'size': 35})

# При переименовании важно сохранить метаданные
new_meta = copy.deepcopy(fs.get_meta(file))
new_file = fs.mkfile('new name', new_meta)

print(new_file)