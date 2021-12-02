def part_one():
  amount = int(0)
  x = int(0)

  with open('input.txt') as f:
    for line in f:
      if x == 0:
        x = int(line)
      else:
        if int(line) > x:
          amount += 1
        x = int(line)

  return str(amount)

def part_two():
  amount = int(0)
  x = int(0)
  last_sum = int(0)
  input_data = open('input.txt', 'r')
  lines = input_data.read().split('\n')

  for line in lines:
    if x < (len(lines) - 2):
      first_number = int(lines[x])
      second_number = int(lines[(x + 1)])
      third_number = int(lines[(x + 2)])

      the_sum = int(get_numbers(first_number, second_number, third_number))

      if x > 0:
        if the_sum > last_sum:
          amount += 1

      last_sum = the_sum
    x += 1

  input_data.close()
  return amount

def get_numbers(x, y, z):
  return int(x) + int(y) + int(z)

print('\nPart 1:')
print(part_one())
print('\nPart 2:')
print(part_two())
