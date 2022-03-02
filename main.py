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

for line in range(len(matrix)):
  for column in range(len(matrix[line])):
      if matrix[line][column] == 1:
        rivers_point.append([line,column])
      else:
        lands_point.append([line,column])

print(rivers_point)
print(lands_point)



def isRiver(line, column, area):
  if area[line][column] == 1:
    return True

  return False
