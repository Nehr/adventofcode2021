import re

def part_one():
  raw_data = {
    '0': '',
    '1': '',
    '2': '',
    '3': '',
    '4': '',
    '5': '',
    '6': '',
    '7': '',
    '8': '',
    '9': '',
    '10': '',
    '11': ''
  }
  
  with open('input.txt') as f:
    for line in f:
      x = int(0)

      new_line = re.match('[0-1]+', line)
      for char in new_line[0]:
        raw_data[str(x)] += str(char)
        x += 1
  
  gamma = ''
  epsilon = ''
  
  for key, value in raw_data.items():
    ones = value.count('1')
    zeroes = value.count('0')
    if ones > zeroes:
      gamma += '1'
      epsilon += '0'
    else:
      gamma += '0'
      epsilon += '1'
  
  gamma_decimal = int(gamma, 2)
  epsilon_decimal = int(epsilon, 2)
  print(f'gamma_decimal: {gamma_decimal}')
  print(f'epsilon_decimal: {epsilon_decimal}')
  
  return gamma_decimal * epsilon_decimal


print('\nPart 1:')
print(part_one())
#print('\nPart 2:')
#print(part_two())
