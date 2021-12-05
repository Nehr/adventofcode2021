import re

def convert_vertical(x, y):
  if (x == 'up'):
    return -y
  else:
    return y

def part_one():
  x = int(0)
  y = int(0)

  with open('input.txt') as f:
    for line in f:
      search = re.search(r'([\w]+)\s([\d]+)', line)
      direction = search.group(1)
      amount = int(search.group(2))
      if search:
        if direction == 'forward':
          x += amount
        else:
          y += convert_vertical(direction, amount)
      else:
        print('search failed')

  return f'x: {str(x)}, y: {str(y)} | total: {str(x*y)}'

def part_two():
  forward = int(0)
  aim = int(0)
  depth = int(0)

  with open('input.txt') as f:
    for line in f:
      search = re.search(r'([\w]+)\s([\d]+)', line)
      direction = search.group(1)
      amount = int(search.group(2))
      if search:
        if direction == 'forward':
          forward += amount
          if aim != 0:
            depth += aim*amount
        else:
          aim += convert_vertical(direction, amount)
      else:
        print('search failed')

  return f'forward: {str(forward)}, aim: {str(aim)}, depth: {depth} | total: {str(forward*depth)}'

print('\nPart 1:')
print(part_one())
print('\nPart 2:')
print(part_two())
