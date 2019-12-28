ask_dict = {
  'как дела?': 'хорошо',
  'чем занимаешься?': 'отвечаю на твои вопросы',
  'кто ты?': 'программа'
}


def ask_user():
  try:
    while True:
      ask = input('Задай мне вопрос: ')
      if ask in ask_dict != None:
        return ask_dict.get(ask)
      else:
        print('Задай другой ворос!')
  except KeyboardInterrupt:
    return 'Пока!'
      
a = ask_user()
print(a)