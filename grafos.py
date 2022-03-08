from entities.surface_type import SurfaceType


class Point(object):

  def __init__(self, matrix, linha, coluna):
    if len(matrix) == 0 or len(matrix[0]) == 0:
      raise ValueError("Matrix inválida")

    self.matrix = matrix
    self.linha = linha
    self.coluna = coluna
    self.isFirstLine = linha == 0
    self.isLastLine = linha == len(matrix) - 1
    self.isFirstColumn = coluna == 0
    self.isLastColumn = coluna == len(matrix[0]) - 1
    self.indice = None

  def __repr__(self):
    return f'({self.indice}:{self.linha},{self.coluna})'

  def get_value(self):
    return self.matrix[self.linha][self.coluna]

  def get_index(self):
    return self.indice


  def set_value(self, value):
    self.matrix[self.linha][self.coluna] = value


  def scan_by_value(self, surface_type, matched):
    if self.get_value() == surface_type.code:
      self.indice = len(matched)
      matched.append(self)
      self.set_value(surface_type.legend)
      matched = self.get_adjacents(surface_type, matched)
    return matched

  def get_grafo(self, surface_type, points_list):
      grafo = []
      if self.move_right() != None and self.move_right().get_value() == surface_type.legend:
        indice = self.find_point_index(self.move_right(), points_list)
        grafo.insert(self.get_index(), indice)

      if self.move_down() != None and self.move_down().get_value() == surface_type.legend:
        indice = self.find_point_index(self.move_down(), points_list)
        grafo.insert(self.get_index(), indice)

      return grafo

  def find_point_index(self, point, point_list):
    for p in point_list:
      if p.equals(point):
        return p.get_index()

  def get_adjacents (self, surface_type, matched):
    if self.move_up() != None:
      matched = self.move_up().scan_by_value(surface_type, matched)
    if self.move_down() != None:
      matched = self.move_down().scan_by_value(surface_type, matched)
    if self.move_left() != None:
      matched = self.move_left().scan_by_value(surface_type, matched)
    if self.move_right() != None:
      matched = self.move_right().scan_by_value(surface_type, matched)
    return matched

  def equals(self, point):
    return self.matrix == point.matrix and self.linha == point.linha and self.coluna == point.coluna

  def move_up(self):
    if not self.isFirstLine:
      return Point(matrix, self.linha - 1, self.coluna)

  def move_down(self,):
    if not self.isLastLine:
      return Point(matrix, self.linha + 1, self.coluna)

  def move_left(self):
    if not self.isFirstColumn:
      return Point(matrix, self.linha, self.coluna - 1)

  def move_right(self):
    if not self.isLastColumn:
      return Point(matrix, self.linha, self.coluna + 1)




  # def adjacents(self):
  #   points = []
  #   if not self.topAdjacent() == None:
  #     points.append(self.topAdjacent())

  #   if not self.bottomAdjacent() == None:
  #     points.append(self.bottomAdjacent())

  #   if not self.leftAdjacent() == None:
  #     points.append(self.leftAdjacent())

  #   if not self.rightAdjacent() == None:
  #     points.append(self.rightAdjacent())

  #   return points




# matrix = [
#   [0,1,0],
#   [1,1,0],
#   [0,0,1],
# ]

matrix = [
  [1,0,1,1,1],
  [0,0,1,3,3],
  [2,2,1,0,3],
  [2,2,1,0,0],
  [0,3,1,2,2],
  [1,3,1,2,2],
  [1,3,1,0,0],
  [1,0,1,0,0],
  [0,0,1,0,0],
  [0,0,1,0,0],
  [0,0,1,0,0],
]
def scan_surface_by_surface_type(matrix, surface_type:SurfaceType):
  points_of_surfaces = []
  grafos_of_surfaces = []
  for linha in range(len(matrix)):
    for coluna in range(len(matrix[linha])):
      surface_points = []
      point = Point(matrix, linha, coluna)
      surface_points = point.scan_by_value(surface_type,surface_points)
      if len(surface_points) > 0:
        grafos = []
        for point in surface_points:
          grafos.append(point.get_grafo(surface_type,surface_points))

        points_of_surfaces.append(surface_points)
        grafos_of_surfaces.append(grafos)
  return points_of_surfaces, grafos_of_surfaces


rio = SurfaceType("Rio", 1, "R")
terra = SurfaceType("Terra", 0, "A")
vegatacao = SurfaceType("Vegetação", 2, "V")
rocha = SurfaceType("Rochas", 3, "H")
surfaces_types = [rio, terra, vegatacao, rocha]


for s in surfaces_types:
  points_of_surfaces, grafos_of_surfaces = scan_surface_by_surface_type(matrix, s)
  print (f"\nQuantidade de áreas de {s.name}: {len(points_of_surfaces)} áreas")
  lenght_of_surface = []
  cont = 1

  for st in points_of_surfaces:
    print(f"\n{cont}o área de {s.name} ")
    lenght_of_surface.append(len(st))
    print(f" - Extensão: {len(st)} unidade(s)")
    print(f" - Pontos: {st}")
    print(f" - Grafo: {grafos_of_surfaces[cont-1]}")
    cont += 1



  #print (f"Grafos {s.name}(s) : {grafos_of_surfaces}")



#[[1],[2],[3]]

# def get_extension(point:Point, points_of_river, visitados):
#   if (achaPonto(visitados, point)):
#     visitados.append(point)
#     vizinhos = point.adjacents()
#     if len(vizinhos) > 0:
#       for p in vizinhos:
#           if p.get_value() == 1:
#             points_of_river.append(point)
#             points_of_river, visitados = get_extension(p, points_of_river, visitados)
#   return points_of_river, visitados

# def achaPonto(lista, ponto):
#   for pontoVisitado in lista:
#     if pontoVisitado.linha == ponto.linha and pontoVisitado.coluna == ponto.coluna:
#       return False
#   return True

# rivers = []
# points_of_river = []
# visitados = []
# for linha in range(len(matrix)):
#   for coluna in range(len(matrix[linha])):
#     point = Point(matrix, linha, coluna)
#     if (achaPonto(visitados, point)):
#       if point.get_value() == 1:
#         points_of_river.append(point)
#         points_of_river, visitados = get_extension(point, points_of_river, visitados)
#       else:
#         visitados.append(point)

#     rivers.append(len(points_of_river))

# print (rivers)



# for point in points:
#   print(point.adjacents())



