from entities.surface_type import SurfaceType
from point import Point


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




