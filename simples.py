from entities import SurfaceType
from entities.surface import Surface
from util.arguments import getArgs

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
  rivers = SurfaceType("Rios", 1, "R")
  lands = SurfaceType("Terra", 0, "T")
  surfaces_types_to_search = [rivers, lands]
else:
  surfaces_types_to_search = [area_to_search]

for surfaces_type in surfaces_types_to_search:
    surface = Surface(matrix, surfaces_type)
    surface.scan_by_surface_type()
    surfaces_area_sizes = []
    for st in surface.points_of_surfaces:
      surfaces_area_sizes.append(len(st))
    print(f"{surfaces_type.name} {surfaces_area_sizes}")


