class Point(object):

  def __init__(self, line, column, value=None):
    self.line = line
    self.column = column
    self.value = value
    # print("linha: ",line,"coluna:", column)

  def is_River(self, area):
    if area[self.line][self.column] == 1:
      return True

    return False




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
  line = 0
  column = 0

  while True:
    point = Point(line, column)
    if point not in already_checked:
      if point.is_River(matrix):
        already_checked.append(point)
        rivers_point.append(point)
        river_size += 1
        next_column = column + 1
        while point.is_River(matrix) and next_column <= number_of_columns -1:
          point = Point(line, next_column)
          already_checked.append(point)
          if point.is_River(matrix):
            rivers_point.append(point)
            river_size += 1
            next_column += 1
          else:
            lands_point.append(point)
            next_line = line + 1
      while point.is_River(matrix) and next_line <= number_of_lines - 1:
        point = Point(next_line, column)
        already_checked.append(point)
        if point.is_River(matrix):
          rivers_point.append(point)
          river_size += 1
          next_line += 1
        else:
          lands_point.append(point)
      else:
        already_checked.append(point)
        lands_point.append(point)
    if line == number_of_lines-1 and column == number_of_columns-1:
      break
    elif line < number_of_lines-1 and column == number_of_columns-1:
      line += 1
      column = 0
    else:
      column += 1

print(result)
print("Rios")
for r in rivers_point:
  print(r.line, r.column)

print("Terras")
for l in lands_point:
  print(l.line, l.column)

print("Resultado:", result)

