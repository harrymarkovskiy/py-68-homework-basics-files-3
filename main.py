import os
current = os.getcwd()

file_name = "result.txt"
full_path = os.path.join(current, file_name)

isExist = os.path.exists(full_path)

count = {}

with open('1.txt', encoding='utf-8') as f:
  name = f.name
  counter = 0
  for line in f:
    counter += 1
  count.update({name : counter})


with open('2.txt', encoding='utf-8') as f:
  name = f.name
  counter = 0
  for line in f:
    counter += 1
  count.update({name : counter})


with open('3.txt', encoding='utf-8') as f:
  name = f.name
  counter = 0
  for line in f:
    counter += 1
  count.update({name : counter})

#print(count)
sorted_values = sorted(count.values())
#print(sorted_values)

sorted_count = {}

for i in sorted_values:
  for k in count.keys():
    if count[k] == i:
      sorted_count[k] = count[k]

#print(sorted_count)
#print(sorted_count.items())

if isExist is False:
  print('Файла результата нет. Создан новый файл')
  result = open('result.txt', 'w+', encoding='utf-8')
else:
  print('Файл результата существует и был перезаписан')
  result = open('result.txt', 'w+', encoding='utf-8')

for k, v in sorted_count.items():
    filename = k
    lines = v
    file = open(filename, 'r', encoding='utf-8')
    content = file.read()
    result.write(f'Файл с именем: {filename}\nВ нем содержится {lines} строк\n{content}\n\n')
    file.close()

result.close()