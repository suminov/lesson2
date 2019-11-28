def age():
  years_old = abs(int(input('Введите Ваш возраст: ')))
  if 0 <= years_old < 2:
    return 'Ты еще слишком маленький чтобы быть тут.'
  elif 2 <= years_old < 6:
    return 'Вы ходите в детский сад.'
  elif 6 <= years_old < 18:
    return 'Вы учитесь в школе'
  elif 18 <= years_old < 24:
    return 'Вы студент.'
  elif 24 <= years_old < 65:
    return 'Вы работаете'
  else:
    return 'Вы на пенсии.'


a = age()

print(a)


def line(variable1, variable2):
  if type(variable1) != str or type(variable2) != str:
    return 0
  elif variable1 == variable2:
    return 1
  elif variable1 != variable2 and len(variable1) > len(variable2):
    return 2
  elif variable1 != variable2 and variable2 == 'learn':
    return 3
  else:
    return 4

b = line('hi', 'привет')
print(b)