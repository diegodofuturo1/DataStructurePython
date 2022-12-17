
dictionary = { 'domingo': 1, 'segunda': 2 }
dictionary['terca'] = 3
dictionary.update({ 'quarta': 4, 'quinta': 5 })

for item in dictionary.items():
    print(item)
for item in dictionary.keys():
    print(item)
for item in dictionary.values():
    print(item)
for day, index in dictionary.items():
    print(day, index)
