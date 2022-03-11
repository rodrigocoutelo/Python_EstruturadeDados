class Point(object):

  def __init__(self, matrix, line, column):
    if len(matrix) == 0 or len(matrix[0]) == 0:
      raise ValueError("Matrix inválida")

    self.matrix = matrix
    self.line = line
    self.column = column
    self.is_first_line = line == 0
    self.is_last_line = line == len(matrix) - 1
    self.is_first_column = column == 0
    self.is_last_column = column == len(matrix[0]) - 1
    self.index = None

  def __repr__(self):
    return f'Node[{self.index}]:({self.line},{self.column})'

  def get_value(self):
    return self.matrix[self.line][self.column]

  def set_value(self, value):
    self.matrix[self.line][self.column] = value

  def get_index(self):
    return self.index

  def move_up(self):
    if not self.is_first_line:
      return Point(self.matrix, self.line - 1, self.column)

  def move_down(self,):
    if not self.is_last_line:
      return Point(self.matrix, self.line + 1, self.column)

  def move_left(self):
    if not self.is_first_column:
      return Point(self.matrix, self.line, self.column - 1)

  def move_right(self):
    if not self.is_last_column:
      return Point(self.matrix, self.line, self.column + 1)

  def equals(self, point):
    return self.matrix == point.matrix and self.line == point.line and self.column == point.column

  def scan_by_value(self, surface_type, matched):
    if self.get_value() == surface_type.code:
      self.index = len(matched)
      matched.append(self)
      self.set_value(surface_type.legend)
      matched = self.get_adjacents(surface_type, matched)
    return matched

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

  def get_grafo(self, surface_type, points_list):
      grafo = []
      if self.move_left() != None and self.move_left().get_value() == surface_type.legend:
        index = self.find_point_index(self.move_left(), points_list)
        grafo.insert(self.get_index(), index)

      if self.move_right() != None and self.move_right().get_value() == surface_type.legend:
        index = self.find_point_index(self.move_right(), points_list)
        grafo.insert(self.get_index(), index)

      if self.move_down() != None and self.move_down().get_value() == surface_type.legend:
        index = self.find_point_index(self.move_down(), points_list)
        grafo.insert(self.get_index(), index)

      if self.move_up() != None and self.move_up().get_value() == surface_type.legend:
        index = self.find_point_index(self.move_up(), points_list)
        grafo.insert(self.get_index(), index)

      return grafo

  def find_point_index(self, point, point_list):
    for p in point_list:
      if p.equals(point):
        return p.get_index()




