"""
IMPLEMENTACIÓN DE UN ÁRBOL BINARIO EN PYTHON USANDO POO
======================================================

Este archivo implementa un árbol binario completo con:
- Inserción
- Búsqueda
- Eliminación
- Recorridos (inorden, preorden, postorden, por niveles)
- Altura
- Conteo de nodos

Todo está explicado línea por línea.
"""

# =========================
# CLASE NODO
# =========================
class Nodo:
    """
    Representa un nodo individual del árbol.
    Cada nodo tiene:
    - valor: el dato almacenado
    - izquierda: referencia al hijo izquierdo
    - derecha: referencia al hijo derecho
    """

    def __init__(self, valor):
        # Guardamos el valor del nodo
        self.valor = valor

        # Inicialmente no tiene hijos
        self.izquierda = None
        self.derecha = None


# =========================
# CLASE ÁRBOL BINARIO
# =========================
class ArbolBinario:
    """
    Implementa un árbol binario de búsqueda (BST).

    REGLA:
    - Valores menores van a la izquierda
    - Valores mayores van a la derecha
    """

    def __init__(self):
        # La raíz del árbol empieza vacía
        self.raiz = None

    # =========================
    # INSERCIÓN
    # =========================
    def insertar(self, valor):
        """
        Inserta un valor en el árbol.
        """
        if self.raiz is None:
            # Si el árbol está vacío, el nuevo nodo es la raíz
            self.raiz = Nodo(valor)
        else:
            # Si no, llamamos al método recursivo
            self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        """
        Inserción recursiva.
        """
        if valor < nodo.valor:
            # Debe ir a la izquierda
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_rec(nodo.izquierda, valor)
        else:
            # Debe ir a la derecha
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_rec(nodo.derecha, valor)

    # =========================
    # BÚSQUEDA
    # =========================
    def buscar(self, valor):
        """
        Retorna True si el valor existe en el árbol.
        """
        return self._buscar_rec(self.raiz, valor)

    def _buscar_rec(self, nodo, valor):
        if nodo is None:
            return False

        if nodo.valor == valor:
            return True

        if valor < nodo.valor:
            return self._buscar_rec(nodo.izquierda, valor)
        else:
            return self._buscar_rec(nodo.derecha, valor)

    # =========================
    # RECORRIDOS
    # =========================
    def inorden(self):
        """
        Izquierda -> Raíz -> Derecha
        """
        return self._inorden_rec(self.raiz)

    def _inorden_rec(self, nodo):
        if nodo is None:
            return []
        return (
            self._inorden_rec(nodo.izquierda) +
            [nodo.valor] +
            self._inorden_rec(nodo.derecha)
        )

    def preorden(self):
        """
        Raíz -> Izquierda -> Derecha
        """
        return self._preorden_rec(self.raiz)

    def _preorden_rec(self, nodo):
        if nodo is None:
            return []
        return (
            [nodo.valor] +
            self._preorden_rec(nodo.izquierda) +
            self._preorden_rec(nodo.derecha)
        )

    def postorden(self):
        """
        Izquierda -> Derecha -> Raíz
        """
        return self._postorden_rec(self.raiz)

    def _postorden_rec(self, nodo):
        if nodo is None:
            return []
        return (
            self._postorden_rec(nodo.izquierda) +
            self._postorden_rec(nodo.derecha) +
            [nodo.valor]
        )

    # =========================
    # ALTURA
    # =========================
    def altura(self):
        return self._altura_rec(self.raiz)

    def _altura_rec(self, nodo):
        if nodo is None:
            return 0

        altura_izq = self._altura_rec(nodo.izquierda)
        altura_der = self._altura_rec(nodo.derecha)

        return 1 + max(altura_izq, altura_der)

    # =========================
    # CONTAR NODOS
    # =========================
    def contar_nodos(self):
        return self._contar_nodos_rec(self.raiz)

    def _contar_nodos_rec(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos_rec(nodo.izquierda) + self._contar_nodos_rec(nodo.derecha)

    # =========================
    # ELIMINACIÓN
    # =========================
    def eliminar(self, valor):
        self.raiz = self._eliminar_rec(self.raiz, valor)

    def _eliminar_rec(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_rec(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_rec(nodo.derecha, valor)
        else:
            # Caso 1: sin hijos
            if nodo.izquierda is None and nodo.derecha is None:
                return None

            # Caso 2: un hijo
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda

            # Caso 3: dos hijos
            sucesor = self._min_valor(nodo.derecha)
            nodo.valor = sucesor.valor
            nodo.derecha = self._eliminar_rec(nodo.derecha, sucesor.valor)

        return nodo

    def _min_valor(self, nodo):
        """
        Encuentra el nodo con el valor mínimo.
        """
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual


# =========================
# EJEMPLO DE USO
# =========================
if __name__ == "__main__":
    arbol = ArbolBinario()

    valores = [50, 30, 70, 20, 40, 60, 80]

    for v in valores:
        arbol.insertar(v)

    print("Inorden:", arbol.inorden())
    print("Preorden:", arbol.preorden())
    print("Postorden:", arbol.postorden())

    print("Buscar 40:", arbol.buscar(40))

    print("Altura:", arbol.altura())
    print("Total nodos:", arbol.contar_nodos())

    arbol.eliminar(30)
    print("Inorden después de eliminar 30:", arbol.inorden())
