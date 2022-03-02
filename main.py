matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

result = []
already_checked = []
rivers_point = []
lands_point = []
river_size = 0


if len(matrix) > 0:
  number_of_lines = len(matrix)
  number_of_columns = len(matrix[0])
  read_line = 0
  read_column = 0

  while True:
    print(matrix[read_line][read_column])

    if read_line == number_of_lines-1 and read_column == number_of_columns-1:
      break
    elif read_line < number_of_lines-1 and read_column == number_of_columns-1:
      print("mudou de linha")
      read_line += 1
      read_column = 0
    else:
      print("mudou de coluna")
      read_column += 1

