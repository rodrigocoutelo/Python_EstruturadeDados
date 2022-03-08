from entities import SurfaceType
from surface import Surface
from arguments import getArgs

matrix, area_to_search = getArgs()

if matrix is None:
  matrix = [
  [1,0,1,1,1],
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

if area_to_search is None:
  area_to_search = SurfaceType("Rios", 1, "R")

surface = Surface(matrix, area_to_search)
surface.scan_by_surface_type()
surfaces_area_sizes = []
for st in surface.points_of_surfaces:
  surfaces_area_sizes.append(len(st))
print(f"{area_to_search.name} {surfaces_area_sizes}")


