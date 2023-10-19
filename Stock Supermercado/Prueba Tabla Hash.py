from random import choice, randrange

def generar_clave_random() -> Clave:
  """
  Genera una clave alfanumerica de 10 digitos al azar
  """
  chars = "1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
  string = "".join(choice(chars) for _ in range(10))
  return Clave(string)

def generar_valor_random() -> int:
  """
  Devuelve un valor al azar entre 0 y 100 millones
  """
  return randrange(0, 100_000_000)

def prueba_de_funcionamiento(diccionario: Diccionario):
  # assert rompe el programa si la condición es falsa
  # esto es útil para verificar cosas que deberían ser ciertas

  clave = generar_clave_random()
  valor = generar_valor_random()

  diccionario.insert(clave, valor)

  assert len(diccionario) == 1

  assert diccionario.search(clave) == valor

  diccionario.delete(clave)

  assert len(diccionario) == 0

# Para probar esto, primero implemente to_int en Celda y la clase HashTable
prueba_de_funcionamiento(HashTable(100))