class NodoAVL:
    """
    Clase que representa un nodo dentro del árbol AVL.
    """

    def __init__(self, valor):
        """
        Constructor del nodo.

        :param valor: Valor que almacenará el nodo.
        """
        self.valor = valor          # Valor almacenado en el nodo
        self.izquierda = None       # Referencia al hijo izquierdo
        self.derecha = None         # Referencia al hijo derecho
        self.altura = 1             # Altura del nodo (importante para AVL)


class ArbolAVL:
    """
    Clase que implementa un árbol AVL.
    """

    def __init__(self):
        """
        Constructor del árbol AVL.
        """
        self.raiz = None  # Inicialmente el árbol está vacío

    # -------------------------
    # FUNCIONES AUXILIARES
    # -------------------------

    def obtener_altura(self, nodo):
        """
        Devuelve la altura de un nodo.

        :param nodo: Nodo del cual obtener la altura.
        :return: Altura del nodo.
        """
        if not nodo:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        """
        Calcula el factor de balance de un nodo.

        :param nodo: Nodo a evaluar.
        :return: Diferencia entre alturas izquierda y derecha.
        """
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def actualizar_altura(self, nodo):
        """
        Actualiza la altura de un nodo.

        :param nodo: Nodo cuya altura será actualizada.
        """
        nodo.altura = 1 + max(
            self.obtener_altura(nodo.izquierda),
            self.obtener_altura(nodo.derecha)
        )

    # -------------------------
    # ROTACIONES (CLAVE DEL AVL)
    # -------------------------

    def rotacion_derecha(self, y):
        """
        Realiza una rotación simple a la derecha.

              y                     x
             / \                   / \
            x   T3     --->      T1  y
           / \                       / \
          T1  T2                    T2  T3
        """

        x = y.izquierda
        T2 = x.derecha

        # Rotación
        x.derecha = y
        y.izquierda = T2

        # Actualizar alturas
        self.actualizar_altura(y)
        self.actualizar_altura(x)

        return x

    def rotacion_izquierda(self, x):
        """
        Rotación simple a la izquierda.

            x                        y
           / \                      / \
          T1  y       --->         x  T3
             / \                  / \
            T2 T3               T1 T2
        """

        y = x.derecha
        T2 = y.izquierda

        # Rotación
        y.izquierda = x
        x.derecha = T2

        # Actualizar alturas
        self.actualizar_altura(x)
        self.actualizar_altura(y)

        return y

    # -------------------------
    # INSERCIÓN
    # -------------------------

    def insertar(self, valor):
        """
        Método público para insertar un valor.
        """
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        """
        Inserción recursiva con balanceo.

        :param nodo: Nodo actual.
        :param valor: Valor a insertar.
        :return: Nodo actualizado.
        """

        # 1. Inserción normal BST
        if not nodo:
            return NodoAVL(valor)

        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar(nodo.derecha, valor)
        else:
            return nodo  # No duplicados

        # 2. Actualizar altura
        self.actualizar_altura(nodo)

        # 3. Obtener balance
        balance = self.obtener_balance(nodo)

        # 4. Casos de desbalance

        # Caso izquierda-izquierda
        if balance > 1 and valor < nodo.izquierda.valor:
            return self.rotacion_derecha(nodo)

        # Caso derecha-derecha
        if balance < -1 and valor > nodo.derecha.valor:
            return self.rotacion_izquierda(nodo)

        # Caso izquierda-derecha
        if balance > 1 and valor > nodo.izquierda.valor:
            nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
            return self.rotacion_derecha(nodo)

        # Caso derecha-izquierda
        if balance < -1 and valor < nodo.derecha.valor:
            nodo.derecha = self.rotacion_derecha(nodo.derecha)
            return self.rotacion_izquierda(nodo)

        return nodo

    # -------------------------
    # ELIMINACIÓN
    # -------------------------

    def eliminar(self, valor):
        """
        Método público para eliminar un valor.
        """
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        """
        Eliminación recursiva con rebalanceo.
        """

        # 1. Eliminación BST
        if not nodo:
            return nodo

        if valor < nodo.valor:
            nodo.izquierda = self._eliminar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(nodo.derecha, valor)
        else:
            # Nodo con 1 o 0 hijos
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda

            # Nodo con 2 hijos
            temp = self._min_valor(nodo.derecha)
            nodo.valor = temp.valor
            nodo.derecha = self._eliminar(nodo.derecha, temp.valor)

        # 2. Actualizar altura
        self.actualizar_altura(nodo)

        # 3. Balance
        balance = self.obtener_balance(nodo)

        # 4. Casos de rotación

        if balance > 1 and self.obtener_balance(nodo.izquierda) >= 0:
            return self.rotacion_derecha(nodo)

        if balance > 1 and self.obtener_balance(nodo.izquierda) < 0:
            nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
            return self.rotacion_derecha(nodo)

        if balance < -1 and self.obtener_balance(nodo.derecha) <= 0:
            return self.rotacion_izquierda(nodo)

        if balance < -1 and self.obtener_balance(nodo.derecha) > 0:
            nodo.derecha = self.rotacion_derecha(nodo.derecha)
            return self.rotacion_izquierda(nodo)

        return nodo

    def _min_valor(self, nodo):
        """
        Encuentra el nodo con el menor valor.
        """
        actual = nodo
        while actual.izquierda:
            actual = actual.izquierda
        return actual

    # -------------------------
    # RECORRIDOS
    # -------------------------

    def inorden(self):
        """
        Recorrido inorden (izquierda, raíz, derecha).
        """
        self._inorden(self.raiz)
        print()

    def _inorden(self, nodo):
        if nodo:
            self._inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self._inorden(nodo.derecha)

    def preorden(self):
        """
        Recorrido preorden.
        """
        self._preorden(self.raiz)
        print()

    def _preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self._preorden(nodo.izquierda)
            self._preorden(nodo.derecha)

    def postorden(self):
        """
        Recorrido postorden.
        """
        self._postorden(self.raiz)
        print()

    def _postorden(self, nodo):
        if nodo:
            self._postorden(nodo.izquierda)
            self._postorden(nodo.derecha)
            print(nodo.valor, end=" ")
