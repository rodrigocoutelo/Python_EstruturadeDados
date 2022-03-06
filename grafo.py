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

def is_river(line, column, size_course=0, vertices=list(), cont=-1):
  grafo = list()
  if matrix[line][column] == 1:
    cont += 1
    vertices.insert(cont, [line, column])
    matrix[line][column] = "R"
    size_course += 1
    size_course, vertices, cont = check_course(line,column,size_course, vertices, cont)

  return size_course, vertices, cont

def check_course(line,column,current_size_course,vertices, cont):

  #up
  if line > 0:
    current_size_course, vertices, cont =  is_river(line-1, column,current_size_course,vertices, cont)

  #down
  if line < number_of_lines-1:
    current_size_course, vertices, cont = is_river(line+1, column,current_size_course,vertices, cont)

  #left
  if column > 0:
    current_size_course, vertices, cont = is_river(line, column-1,current_size_course,vertices, cont)

  #right
  if column < number_of_columns-1:
    current_size_course, vertices, cont = is_river(line, column+1,current_size_course,vertices, cont)

  return current_size_course, vertices, cont


def ache_o_rio(matrix):
  cont = -1
  vertices = list()
  vert = []
  if len(matrix) > 0:
    for i in range(0, len(matrix)): #Numeros Linhas - 1
      if 1 in (matrix[i]):
        for j in range(0, len(matrix[i])): #Numeros Colunas - 1
          if matrix[i][j] == 1:
            retorno, vertices, cont = is_river(i,j, 0, list(), cont)
            result.append(retorno)
            vert.append(vertices)

          #elif matrix[i][j] == 0:
            #retorno = is_Island(i,j)

  print(vert)        # result_i.append(retorno)
  result.sort()
  print (result)
 # result_i.sort()

ache_o_rio(matrix)
 # print("Ilhas", result_i)




