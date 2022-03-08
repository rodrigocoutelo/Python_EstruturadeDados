class SurfaceType(object):

  def __init__(self, name, code, legend):
    self.name = name
    self.code = code
    self.legend = legend

  def __repr__(self):
    return f"[{self.name} | Código: {self.code} | Label:{self.legend}]"
