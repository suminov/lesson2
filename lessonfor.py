for x in range(10):
  print(x+1)

print(


)

word = input('Введите любое слово: ')
for letter in word:
  print(letter)

print(


)

rating  = [{'shool_class': '4a', 'scores': [2, 3, 3, 5, 4]},
{'shool_class': '4b', 'scores': [2, 4, 5, 5, 4]}, 
{'shool_class': '4v', 'scores': [2, 2, 3, 5, 3]}]

a = 0
for result in rating:
  print('Средний балл {} класса: {}'
  .format(result['shool_class'], sum(result['scores'])/len(result['scores'])))
  sum_scores += sum(result['scores'])/len(result['scores'])

print(sum_scores/len(rating))