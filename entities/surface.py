from copy import deepcopy
from entities.surface_type import SurfaceType
from entities.point import Point


class Surface(object):

  def __init__(self, matrix):
    if len(matrix) <= 0:
      raise Exception("Matrix inválida")
    self.matrix = matrix


  def find_surface_by_type(self, surface_type:SurfaceType):
    matrix = deepcopy(self.matrix)
    return self.search_on_surface(matrix, surface_type)

  def find_surface_grafos(self, surface_type:SurfaceType):
    matrix = deepcopy(self.matrix)
    return self.search_for_grafos(matrix, surface_type)

  def search_for_grafos(self, matrix, surface_type):
    for line in range(0, len(matrix)):
      if surface_type.code in (matrix[line]): #sá busca se a linha tiver alguma superfície do tipo procurado
        for column in range(0, len(matrix[line])):
          point = Point(matrix, line, column) # transforma toda a matriz em um objeto da classe Point
          if point.get_point() == surface_type.code:
            start_point = point
            grafos, points = self.createGrafo(surface_type, start_point, -1)
    return grafos, points

  def createGrafo(self,surface_type:SurfaceType, current_point:Point, cont , grafos = list(), points = {}, anterior_point:Point = None):

    if current_point.get_point() == surface_type.code:
      current_point.set_point(surface_type.legend)
      cont = cont + 1
      points[(current_point.line, current_point.column)] = cont

      if not anterior_point == None and  anterior_point.get_point() == surface_type.legend:
        try:
          grafo = grafos[points[(anterior_point.line, anterior_point.column)]]
        except:
          grafo = [cont]

        grafo.append(cont)
        grafos.insert(points[(current_point.line, current_point.column)],grafo)

      self.deep_search(surface_type,current_point,cont,grafos,points)
    return grafos, points

  def deep_search(self, surface_type:SurfaceType, current_point:Point, cont, grafos, points):
    #up
    if not current_point.is_in_first_line:
      self.createGrafo(surface_type, current_point.move_up(),cont,grafos,points,current_point )

    #down
    if not current_point.is_in_last_line:
      self.createGrafo(surface_type, current_point.move_down(),cont,grafos,points,current_point)

    #left
    if not current_point.is_in_first_column:
      self.createGrafo(surface_type, current_point.move_left(),cont,grafos,points,current_point)

    #right
    if not current_point.is_in_last_column:
      self.createGrafo(surface_type, current_point.move_right(),cont,grafos,points,current_point)

    return


  def search_on_surface(self, matrix, surface_type):
    result = []
    extension_of_area = 0
    for line in range(0, len(matrix)):
      if surface_type.code in (matrix[line]): #sá busca se a linha tiver alguma superfície do tipo procurado
        for column in range(0, len(matrix[line])):
          point = Point(matrix, line, column) # transforma toda a matriz em um objeto da classe Point
          if point.get_point() == surface_type.code:
            start_point = point
            extension_of_area = self.is_surface_of_type(start_point,surface_type)
            result.append(extension_of_area)
            result.sort()
    return result

  def is_surface_of_type(self, point:Point, surface_type:SurfaceType, extension_of_area=0):
    if point.get_point() == surface_type.code:
      point.set_point(surface_type.legend)
      extension_of_area += 1
      extension_of_area = self.check_extension(point,surface_type,extension_of_area)
    return extension_of_area

  def check_extension(self, point:Point,surface_type,current_extension_of_area):
    #up
    if not point.is_in_first_line:
      current_extension_of_area =  self.is_surface_of_type(point.move_up(),surface_type, current_extension_of_area)

    #down
    if not point.is_in_last_line:
      current_extension_of_area = self.is_surface_of_type(point.move_down(),surface_type, current_extension_of_area)

    #left
    if not point.is_in_first_column:
      current_extension_of_area = self.is_surface_of_type(point.move_left(),surface_type, current_extension_of_area)

    #right
    if not point.is_in_last_column:
      current_extension_of_area = self.is_surface_of_type(point.move_right(),surface_type, current_extension_of_area)

    return current_extension_of_area


