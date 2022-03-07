from entities import Surface, SurfaceType


rio = SurfaceType("Rio", 1, "R")
terra = SurfaceType("Terra", 0, "A")
vegatacao = SurfaceType("Vegetação", 2, "V")
surfaces_types = [rio, terra, vegatacao]

surface_matrix = [
  [1,0,1,1,1],
  [0,0,1,0,0],
  [2,2,1,0,0],
  [2,2,1,0,0],
  [0,0,1,2,2],
  [1,0,1,2,2],
  [1,0,1,0,0],
  [1,0,1,0,0],
  [0,0,1,0,0],
  [0,0,1,0,0],
  [0,0,1,0,0],
]

surface = Surface(surface_matrix)
for s in surfaces_types:
  print(f"{s.name}: {surface.find_surface_by_type(s)}")


