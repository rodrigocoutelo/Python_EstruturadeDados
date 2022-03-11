from entities.surface_type import SurfaceType
from entities.point import Point


class Surface(object):

  def __init__(self, points:list, surface_type:SurfaceType, ): #points vai receber a matriz
    self.surface_type = surface_type
    self.points = points
    self.points_of_surfaces = []
    self.surface_grafos = []


  def scan_by_surface_type(self):
    for line in range(len(self.points)):
      for column in range(len(self.points[line])):
        surface_points = []
        point = Point(self.points, line, column)
        surface_points = point.scan_by_value(self.surface_type,surface_points)
        if len(surface_points) > 0:
          surface_grafo = []
          for p in surface_points:
            surface_grafo.append(p.get_grafo(self.surface_type, surface_points))

          self.points_of_surfaces.append(surface_points)
          self.surface_grafos.append(surface_grafo)



