class TV:

    _numTV = 0

    

    def __init__(self, marca, estado):

        self._marca = marca

        self._estado = estado

        self._canal = 1

        self._volumen = 1

        self._precio = 500

        self._control = None

        TV._numTV += 1

        

        

    def setMarca (self, marca):

        self._marca = marca

    

    def getMarca (self):

        return self._marca




    def setControl (self, control):

        self._control = control

    

    def getControl(self):

        return self._control




    def setPrecio (self, precio):

        self._precio = precio

    

    def getPrecio (self):

        return self._precio




    def getVolumen (self):

        return self._volumen

    

    def getCanal (self):

        return self._canal

    

    def setCanal (self, canal):

        if ((canal >= 1 and canal <=120) and (self._estado)):

            self._canal = canal

        else:

            pass

        

    @classmethod    

    def getNumTV(cls):

        return cls._numTV

    

    @classmethod

    def setNumTV(cls, numTV):

        cls._numTV = numTV

    

    def getEstado(self):

        return self._estado




    def turnOn(self):

        self._estado = True




    def turnOff(self):

        self._estado = False




    def canalUp(self):

        if (self._estado == True and self._canal<120):

            self._canal += 1 

    

    def canalDown(self):

        if (self._estado == True and self._canal>1):

            self._canal -= 1 




    def volumenUp(self):

        if (self._estado == True and self._volumen<7):

            self._volumen += 1

    

    def volumenDown(self):

        if (self._estado == True and self._volumen>1):

            self._volumen -= 1  

    










    def setVolumen (self, newVolumen):

        if (newVolumen <= 7  and newVolumen >= 1):

            self._volumen = newVolumen

        else:

            pass