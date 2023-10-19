from typing import Any

class Clave():
  """
  Almacena la clave real a ser hasheada,
  usando la representación que se desee,
  y encapsula el algoritmo de hash elegido.
  """

  def __init__(self, key: str):
    self.key = key


  def to_int(self) -> int:
    """
    Esta función debe convertir el valor de la key en un número.
    """
    total=0
    for char in self.key:
      total += ord(char)
    return total

  def __eq__(self, other) -> bool:
    """
    Decide si dos claves son iguales
    """
    return self.key == other.key

  def __str__(self):
    return str(self.key)



# No es necesario cambiar nada en esta celda! Esta celda solo define la interfaz
# del TAD Diccionario.
from typing import Any

class Diccionario():
  """
  Interfaz del TAD Diccionario
  - insert(key, value) - Inserta un elemento con clave key y valor value en el diccionario.
      Si la clave ya se encuentra en el diccionario, debe reemplazar el value anterior por el nuevo.
  - search(key) - Devuelve la el value asociado con la clave key, o muestra un mensaje de error si la clave no se encuentra.
  - delete(key) - Elimina el elemento con clave key del diccionario.
  """

  def insert(self, key: Clave, data: Any) -> None:
    pass

  def search(self, key: Clave) -> Any:
    pass

  def delete(self, key: Clave) -> None:
    pass



class HashTable(Diccionario):
  """
  Implementación de Diccionario con tabla hash
  de tamaño fijo y resolución de colisiones
  por encadenamiento
  """

  def __init__(self, size: int):
    self.size = size
    self.table = [[] for _ in range(size)]
    self.lenght=0


  def insert(self, key: Clave, data: Any) -> None:
    """
    Implementacion del metodo insert

    Crea un indice y agrega key y data en la posición i en la tabla hash.
    """
    index = key.to_int() % self.size
    self.table[index].append((key, data))
    self.lenght += 1


  def search(self, key: Clave) -> Any | None:
    """
    Implementacion del metodo search.

    Crea el indice de la clave e itera sobre la lista hasta encontrarlo, si lo encuentra, devuelve el dato y si no, no devuelve nada.
    """
    index = key.to_int() % self.size
    for k,data in self.table[index]:
      if k == key:
        return data
    return None


  def delete(self, key: Clave) -> None:
    """
    Implementacion del metodo delete
    """
    index = key.to_int() % self.size
    for tupla in self.table[index]:
        k, data = tupla
        if k == key:
            self.table[index].remove(tupla)
            self.lenght -= 1


  def __len__(self) -> int:
    """
    Este método sobrecarga la función `len`.
    Debe devolver la cantidad de elementos insertados en la tabla.
    Si la tabla está vacía, devuelve cero.
    """
    return self.lenght


  def _load_factor(self) -> float:
    """
    Este método debe devolver el factor de carga de la tabla.
    """
    factor_carga = self.lenght / self.size
    return factor_carga

  def _longest_list(self) -> int:
    """
    Este método debe devolver la longitud de la lista mas larga de la tabla
    """
    longitud = 0
    for tupla in self.table:
      if len(tupla) > longitud:
        longitud = len(tupla)

  def __str__(self) -> str:
    """
    Mostrar la cantidad de elementos de la tabla (__len__), el factor de carga (_load_factor)
    y la longitud de la lista mas larga (_longest_list)
    """
    return f"el largo de la lista es :{self.__len__()}, el factor de carga es {self._load_factor()}, la longitud de la lista mas larga es {self._longest_list()} "

  def ver_tabla(self):
    for tupla in self.table:
      print(tupla)
