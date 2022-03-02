import re
from pyparsing import col


#matrix = [
#     #0  1  2  3  4
#     [1, 0, 1, 0, 0],#0
#     [1, 0, 1, 0, 0],#1
#     [0, 1, 1, 1, 1],#2
#     [0, 0, 1, 0, 0],#3
#     [0, 0, 1, 0, 0],#4
# ]

matrix = [
  [1,0,0,1,1],
  [1,1,0,0,0],
  [0,0,0,0,1],
  [1,1,0,0,0]
]

number_of_lines = len(matrix)
number_of_columns = len(matrix[0])
already_checked = []
already_checked_i = []
result = []
result_i = []

def is_River(line, column, size_course=0):

  if [line, column] not in already_checked:
   # print("Checando","Linha:", line, "Coluna:", column, "Valor", matrix[line][column])
    already_checked.append([line, column])
    if matrix[line][column] == 1:
      matrix[line][column] = "R"
      size_course += 1
      size_course = check_course(line,column,size_course)


  return size_course

def is_Island(line, column, size_land=0):

  if [line, column] not in already_checked_i:
   # print("Checando","Linha:", line, "Coluna:", column, "Valor", matrix[line][column])
    already_checked_i.append([line, column])
    if matrix[line][column] == 0:
      matrix[line][column] = "L"
      size_land += 1
      size_land = check_land(line,column,size_land)


  return size_land

def check_land(line,column,current_size_land):
  #up
  if line > 0:
    current_size_land =  is_Island(line-1, column,current_size_land)
  #down
  if line < number_of_lines-1:
    current_size_land = is_Island(line+1, column,current_size_land)

  #left
  if column > 0:
    current_size_land = is_Island(line, column-1,current_size_land)

  #right
  if column < number_of_columns-1:
    current_size_land = is_Island(line, column+1,current_size_land)

  return current_size_land

def check_course(line,column,current_size_course):
  #up
  if line > 0:
    current_size_course =  is_River(line-1, column,current_size_course)
  #down
  if line < number_of_lines-1:
    current_size_course = is_River(line+1, column,current_size_course)

  #left
  if column > 0:
    current_size_course = is_River(line, column-1,current_size_course)

  #right
  if column < number_of_columns-1:
    current_size_course = is_River(line, column+1,current_size_course)

  return current_size_course

if len(matrix) > 0:
  for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
      if matrix[i][j] == 1:
        retorno = is_River(i,j)
        result.append(retorno)
      elif matrix[i][j] == 0:
        retorno = is_Island(i,j)
        result_i.append(retorno)

  result.sort()
  result_i.sort()
  print("Rios", result)
  print("Ilhas", result_i)




