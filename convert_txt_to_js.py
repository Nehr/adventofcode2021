import re

output_type = 'matrix'

file_in = '4/input_matrix_test.txt'
file_out = 'output.js'

f_in = open(file_in, 'r')

f_out = open(file_out, 'w')

# Array
if (output_type == 'array'):
  f_out.write('const array = [\n')
  f_out.close()
  f_out = open(file_out, 'a')

  for line in f_in:
    new_line = re.match(r'[\w]+', line)
    f_out.write(f'\t\'{new_line[0]}\',\n')

  f_out.write(']\n')

# Matrix
if (output_type == 'matrix'):
  f_out.write('const matrix = [\n')
  f_out.close()
  f_out = open(file_out, 'a')
  
  for line in f_in:
    new_line = re.findall(r'\d{1,2}', line)
    if new_line != None and len(new_line):
      f_out.write('\t[ ')
      for char in new_line[:-1]:
        f_out.write(f'{char}, ')
      f_out.write(f'{new_line[-1]}')
      f_out.write(' ],\n')

  f_out.write('];\n')


f_out.close()