import sys
import ast
from entities.surface_type import SurfaceType

def getArgs():
  matrix = None
  area_to_search = None

  args = sys.argv
  if len(args) > 1:
    try:
      matrix = ast.literal_eval(args[1])
    except:
      raise Exception("1o Argumento deve ser uma string com uma matriz bidemensional")

    if len(args) == 3:
      try:
        area_to_search = SurfaceType("Área Procurada", int(args[2]), "A")
      except Exception as e:
        print("Paramentros Inválidos: %s.  usar simples.py matriz:list, codigo_da_superficie_procurada:int usando dados default" % e)

    if len(args) > 3:
      try:
        area_to_search = SurfaceType(args[3], int(args[2]), args[3][0:1])
      except Exception as e:
        print("Paramentros Inválidos: %s.  usar simples.py matriz:list  codigo_da_superficie_procurada:int  nome_da_superficie_procurada:str, usando dados default " % e)

  return matrix, area_to_search

  args = getArgs()
