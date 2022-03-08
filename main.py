from util.arguments import getArgs
from entities.surface_type import SurfaceType
from entities.surface import Surface

matrix, area_to_search = getArgs()

if matrix is None:
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

if not area_to_search is None:
  surfaces_types = [area_to_search]
else:
  rio = SurfaceType("Rio", 1, "R")
  terra = SurfaceType("Terra", 0, "A")
  vegatacao = SurfaceType("Vegetação", 2, "V")
  rocha = SurfaceType("Rochas", 3, "H")
  surfaces_types = [rio, terra, vegatacao, rocha]

print("Análise de superfíce")
print(f"Superfícies analisada(s): {surfaces_types}")

for s in surfaces_types:
  surface = Surface(matrix, s)
  surface.scan_by_surface_type()
  print()
  print (f"\nQuantidade de áreas de {s.name}: {len(surface.points_of_surfaces)} área(s)")
  lenght_of_surface = []
  cont = 1
  for st in surface.points_of_surfaces:
    lenght_of_surface.append(len(st))
    print(f"\n{cont}o área de {s.name} ")
    print(f" - Extensão: {len(st)} unidade(s)")
    print(f" - Pontos: {st}")
    print(f" - Grafo: {surface.surface_grafos[cont-1]}")
    cont += 1

  print("\nSaída Simples")
  print(f"{s.name}: {lenght_of_surface}")












