"""
ÁRBOL DE BÚSQUEDA BINARIO (BST) EN PYTHON
========================================

Este archivo implementa un Árbol de Búsqueda Binario (Binary Search Tree, BST)
usando Programación Orientada a Objetos (POO).

Incluye:
- Inserción
- Búsqueda
- Eliminación
- Recorridos (inorden, preorden, postorden)
- Altura
- Encontrar mínimo y máximo

Cada línea está explicada con comentarios detallados.
"""

# =========================
# CLASE NODO
# =========================
class Nodo:
    """
    Representa un nodo dentro del árbol.
    Cada nodo contiene:
    - valor: el dato almacenado
    - izquierda: referencia al hijo izquierdo
    - derecha: referencia al hijo derecho
    """

    def __init__(self, valor):
        # Guardamos el valor que tendrá el nodo
        self.valor = valor

        # Inicialmente no tiene hijos
        self.izquierda = None
        self.derecha = None


# =========================
# CLASE ÁRBOL BST
# =========================
class ArbolBST:
    """
    Implementación de un Árbol de Búsqueda Binario.

    PROPIEDAD CLAVE:
    - Todo valor menor va a la izquierda
    - Todo valor mayor va a la derecha
    """

    def __init__(self):
        # La raíz empieza vacía
        self.raiz = None

    # =========================
    # INSERTAR
    # =========================
    def insertar(self, valor):
        """
        Inserta un valor en el árbol.
        """
        if self.raiz is None:
            # Si el árbol está vacío, el nuevo nodo será la raíz
            self.raiz = Nodo(valor)
        else:
            # Si no está vacío, usamos función recursiva
            self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        """
        Función auxiliar recursiva para insertar.
        """
        if valor < nodo.valor:
            # Si el valor es menor, vamos a la izquierda
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_rec(nodo.izquierda, valor)

        elif valor > nodo.valor:
            # Si el valor es mayor, vamos a la derecha
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_rec(nodo.derecha, valor)

        # Si es igual, no insertamos (evitamos duplicados)

    # =========================
    # BUSCAR
    # =========================
    def buscar(self, valor):
        """
        Busca un valor en el árbol.
        Devuelve True si existe, False si no.
        """
        return self._buscar_rec(self.raiz, valor)

    def _buscar_rec(self, nodo, valor):
        """
        Búsqueda recursiva.
        """
        if nodo is None:
            return False

        if valor == nodo.valor:
            return True

        elif valor < nodo.valor:
            return self._buscar_rec(nodo.izquierda, valor)

        else:
            return self._buscar_rec(nodo.derecha, valor)

    # =========================
    # RECORRIDOS
    # =========================
    def inorden(self):
        """
        Recorre el árbol en orden (izquierda, raíz, derecha).
        Devuelve lista ordenada.
        """
        resultado = []
        self._inorden_rec(self.raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo, resultado):
        if nodo:
            self._inorden_rec(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden_rec(nodo.derecha, resultado)

    def preorden(self):
        resultado = []
        self._preorden_rec(self.raiz, resultado)
        return resultado

    def _preorden_rec(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self._preorden_rec(nodo.izquierda, resultado)
            self._preorden_rec(nodo.derecha, resultado)

    def postorden(self):
        resultado = []
        self._postorden_rec(self.raiz, resultado)
        return resultado

    def _postorden_rec(self, nodo, resultado):
        if nodo:
            self._postorden_rec(nodo.izquierda, resultado)
            self._postorden_rec(nodo.derecha, resultado)
            resultado.append(nodo.valor)

    # =========================
    # ENCONTRAR MÍNIMO
    # =========================
    def minimo(self):
        """
        Devuelve el valor mínimo del árbol.
        """
        actual = self.raiz

        # Vamos todo a la izquierda
        while actual.izquierda:
            actual = actual.izquierda

        return actual.valor

    # =========================
    # ENCONTRAR MÁXIMO
    # =========================
    def maximo(self):
        """
        Devuelve el valor máximo del árbol.
        """
        actual = self.raiz

        # Vamos todo a la derecha
        while actual.derecha:
            actual = actual.derecha

        return actual.valor

    # =========================
    # ALTURA
    # =========================
    def altura(self):
        """
        Calcula la altura del árbol.
        """
        return self._altura_rec(self.raiz)

    def _altura_rec(self, nodo):
        if nodo is None:
            return 0

        izquierda = self._altura_rec(nodo.izquierda)
        derecha = self._altura_rec(nodo.derecha)

        return max(izquierda, derecha) + 1

    # =========================
    # ELIMINAR
    # =========================
    def eliminar(self, valor):
        """
        Elimina un valor del árbol.
        """
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
            elif nodo.izquierda is None:
                return nodo.derecha

            elif nodo.derecha is None:
                return nodo.izquierda

            # Caso 3: dos hijos
            # Buscamos el sucesor (mínimo del subárbol derecho)
            sucesor = self._min_nodo(nodo.derecha)

            nodo.valor = sucesor.valor

            nodo.derecha = self._eliminar_rec(nodo.derecha, sucesor.valor)

        return nodo

    def _min_nodo(self, nodo):
        """
        Devuelve el nodo con el valor mínimo.
        """
        actual = nodo
        while actual.izquierda:
            actual = actual.izquierda
        return actual


# =========================
# EJEMPLO DE USO
# =========================
if __name__ == "__main__":
    arbol = ArbolBST()

    valores = [50, 30, 70, 20, 40, 60, 80]

    for v in valores:
        arbol.insertar(v)

    print("Inorden:", arbol.inorden())
    print("Preorden:", arbol.preorden())
    print("Postorden:", arbol.postorden())

    print("Buscar 40:", arbol.buscar(40))

    print("Minimo:", arbol.minimo())
    print("Maximo:", arbol.maximo())

    print("Altura:", arbol.altura())

    arbol.eliminar(70)
    print("Inorden después de eliminar 70:", arbol.inorden())
