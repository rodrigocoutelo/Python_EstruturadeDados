class Point(object):

  def __init__(self, matrix, linha, coluna):
    if len(matrix) == 0 or len(matrix[0]) == 0:
      raise ValueError("Matrix inválida")

    self.matrix = matrix
    self.linha = linha
    self.coluna = coluna
    self.isFirstLine = linha == 0
    self.isLastLine = linha == len(matrix) - 1
    self.isFirstColumn = coluna == 0
    self.isLastColumn = coluna == len(matrix[0]) - 1
    self.indice = None

  def __repr__(self):
    return f'({self.indice}:{self.linha},{self.coluna})'

  def get_value(self):
    return self.matrix[self.linha][self.coluna]

  def get_index(self):
    return self.indice


  def set_value(self, value):
    self.matrix[self.linha][self.coluna] = value


  def scan_by_value(self, surface_type, matched):
    if self.get_value() == surface_type.code:
      self.indice = len(matched)
      matched.append(self)
      self.set_value(surface_type.legend)
      matched = self.get_adjacents(surface_type, matched)
    return matched

  def get_grafo(self, surface_type, points_list):
      grafo = []
      if self.move_right() != None and self.move_right().get_value() == surface_type.legend:
        indice = self.find_point_index(self.move_right(), points_list)
        grafo.insert(self.get_index(), indice)

      if self.move_down() != None and self.move_down().get_value() == surface_type.legend:
        indice = self.find_point_index(self.move_down(), points_list)
        grafo.insert(self.get_index(), indice)

      return grafo

  def find_point_index(self, point, point_list):
    for p in point_list:
      if p.equals(point):
        return p.get_index()

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

  def equals(self, point):
    return self.matrix == point.matrix and self.linha == point.linha and self.coluna == point.coluna

  def move_up(self):
    if not self.isFirstLine:
      return Point(self.matrix, self.linha - 1, self.coluna)

  def move_down(self,):
    if not self.isLastLine:
      return Point(self.matrix, self.linha + 1, self.coluna)

  def move_left(self):
    if not self.isFirstColumn:
      return Point(self.matrix, self.linha, self.coluna - 1)

  def move_right(self):
    if not self.isLastColumn:
      return Point(self.matrix, self.linha, self.coluna + 1)
