ask_dict = {
  'как дела?': 'хорошо',
  'чем занимаешься?': 'отвечаю на твои вопросы',
  'кто ты?': 'программа'
}


def ask_user():
  while True:
    ask = input('Задай мне вопрос: ')
    if ask_dict.get(ask) != None:
      return ask_dict.get(ask)
      break
    else:
      print('Задай другой ворос!')
      
a = ask_user()
print(a)