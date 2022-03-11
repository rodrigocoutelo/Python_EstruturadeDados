from util.arguments import getArgs
from entities.surface_type import SurfaceType
from entities.surface import Surface

matrix, area_to_search = getArgs()

if matrix is None:
 matrix = [
  [1,3,3,3,0], #0
  [1,0,0,2,2], #1
  [1,0,0,2,2], #2
  [3,1,1,1,0], #3
  [3,3,1,1,1], #4
  [1,1,1,1,1], #5
  [0,1,1,1,2], #6
  [0,2,1,2,2], #7
  [1,2,1,0,0], #8
  [1,0,0,0,0], #9
  [1,0,0,0,0], #9
  [1,3,3,3,1], #9
  [1,1,1,1,1], #9
  ]




  #[[1], [2,3], [1,4], [0], [1]]

#Usa dados defaults se os parâmetros não vierem da linha de comando.
if not area_to_search is None:
  surfaces_types = [area_to_search]
else:
  rivers = SurfaceType("Rio", 1, "R")
  lands = SurfaceType("Terra", 0, "A")
  trees = SurfaceType("Vegetação", 2, "V")
  rocks = SurfaceType("Rochas", 3, "H")
  surfaces_types = [rivers, lands, trees, rocks]

print("Análise da superfíce")
print(f"Tipos de superfícies analisada(s): {surfaces_types}")

for s in surfaces_types:
  surface = Surface(matrix, s)
  surface.scan_by_surface_type()

  print (f"\nQuantidade de áreas de {s.name}: {len(surface.points_of_surfaces)} área(s)")
  lenght_of_surface = []
  cont = 1

  for pofs in surface.points_of_surfaces:
    lenght_of_surface.append(len(pofs))
    print(f"\n{cont}o área de {s.name} ")
    print(f" - Extensão: {len(pofs)} unidade(s)")
    print(f" - Pontos: {pofs}")
    print(f" - Grafo: {surface.surface_grafos[cont-1]}")
    cont += 1

  print("\nSaída Simples")
  print(f"{s.name}: {lenght_of_surface}")












