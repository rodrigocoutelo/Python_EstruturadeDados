matrix = [
  [1,1,1,1,1],
  [0,0,1,0,0],
  [0,0,1,0,0],
  [0,0,1,0,0],
  [0,0,1,0,0],
  [1,0,1,0,0],
  [1,0,1,0,0],
  [1,0,1,0,0],
  [0,0,1,0,0],
  [0,0,1,0,0],
  [0,0,1,0,0],
]

number_of_lines = len(matrix)
number_of_columns = len(matrix[0])
already_checked_i = []
result = []
result_i = []

def is_river(line, column, size_course=0):

  if matrix[line][column] == 1:
    matrix[line][column] = "R"
    size_course += 1
    size_course = check_course(line,column,size_course)

  return size_course

def check_course(line,column,current_size_course):

  #up
  if line > 0:
    current_size_course =  is_river(line-1, column,current_size_course)

  #down
  if line < number_of_lines-1:
    current_size_course = is_river(line+1, column,current_size_course)

  #left
  if column > 0:
    current_size_course = is_river(line, column-1,current_size_course)

  #right
  if column < number_of_columns-1:
    current_size_course = is_river(line, column+1,current_size_course)

  return current_size_course

def ache_o_rio(matrix):
  if len(matrix) > 0:
    for i in range(0, len(matrix)): #Numeros Linhas - 1
      if 1 in (matrix[i]):
        for j in range(0, len(matrix[i])): #Numeros Colunas - 1
          if matrix[i][j] == 1:
            retorno = is_river(i,j)
            result.append(retorno)
          #elif matrix[i][j] == 0:
            #retorno = is_Island(i,j)
          # result_i.append(retorno)
  result.sort()
  print (result)
 # result_i.sort()

ache_o_rio(matrix)
 # print("Ilhas", result_i)




