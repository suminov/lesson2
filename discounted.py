def discounted(price, discount, max_discount=20, name=''):
  try:
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
      raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount or 'iphon' in name.lower() or not name:
      return price
    else:
      return price - (price * discount / 100)
  except ValueError:
    raise ValueError('price, discount, max_discount должны быть числом')

print(discounted(10, '', True))