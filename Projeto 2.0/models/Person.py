import re


class ExexeptionName(Exception):
    pass


class Person:
    def __init__(this):
        this.__name = None
        this.__cpf = None

    @property
    def setName(self):
        return self.__name

    @setName.setter
    def setName(self, name):
        try:
            if re.findall(r"[^a-zA-Z ]", name):
                raise ExexeptionName("Only letters are allowed in the name")
            self.__name = name
        except ExexeptionName as e:
            print("(Error setName)", e)

    @property
    def setCPF(self):
        return self.__cpf

    @setCPF.setter
    def setCPF(self, cpf):
        try:
            if re.findall(r"[^0-9]", cpf):
                raise ExexeptionName("The CPF can only contain numbers!")

            if len(cpf) == 11:
                raise ExexeptionName("The CPF has to contain 11 numbers!")

            if not self._checkCPF():
                raise ExexeptionName("The CPF is invalid!")


        except ExexeptionName as e:
            print("(Error setName)", e)

    def _checkCPF(self):

        soma = sum(int(self.__cpf[i]) * (10 - i) for i in range(9))
        resto = (soma * 10) % 11
        if resto == 10:
            resto = 0
        if resto != int(self.__cpf[9]):
            return False

        # Verificar o segundo dígito verificador
        soma = sum(int(self.__cpf[i]) * (11 - i) for i in range(10))
        resto = (soma * 10) % 11
        if resto == 10:
            resto = 0
        if resto != int(self.__cpf[10]):
            return False
        return True
