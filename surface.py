from copy import deepcopy
from surface_type import SurfaceType
from point import Point


class Surface(object):

  def __init__(self, matrix):
    if len(matrix) <= 0:
      raise Exception("Matrix inválida")

    self.matrix = matrix
    self.number_of_lines = len(matrix)
    self.number_of_columns = len(matrix[0])

  def find_surface_by_type(self, surface_type:SurfaceType):
    matrix = deepcopy(self.matrix)
    return self.search_on_surface(matrix, surface_type)

  def search_on_surface(self, matrix, surface_type):
    result = []
    extension_of_area = 0
    for line in range(0, len(matrix)):
      if surface_type.code in (matrix[line]):
        for column in range(0, len(matrix[line])): #Numeros Colunas - 1
          point = Point(matrix, line, column)
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


