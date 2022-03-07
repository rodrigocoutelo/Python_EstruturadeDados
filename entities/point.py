class Point(object):
  def __init__(self, matrix, line, column):
    self.line = line
    self.column = column
    self.matrix = matrix
    self.is_in_first_line = line == 0
    self.is_in_last_line = line == (len(matrix) - 1)
    self.is_in_first_column = column == 0
    self.is_in_last_column = column == (len(matrix[0]) - 1)


  def get_point(self):
    return self.matrix[self.line][self.column]

  def set_point(self, value):
    self.matrix[self.line][self.column] = value

  def move_up(self):
    return Point(self.matrix, self.line - 1, self.column)
  def move_down(self):
    return Point(self.matrix, self.line + 1, self.column)
  def move_left(self):
    return Point(self.matrix, self.line, self.column - 1)
  def move_right(self):
    return Point(self.matrix, self.line, self.column + 1)
