import re

file_in = '3/input_test.txt'
file_out = 'output.js'

f_in = open(file_in, 'r')

f_out = open(file_out, 'w')
f_out.write('[\n')
f_out.close()
f_out = open(file_out, 'a')

for line in f_in:
  new_line = re.match(r'[\w]+', line)
  f_out.write(f'\t\'{new_line[0]}\',\n')

f_out.write(']\n')
