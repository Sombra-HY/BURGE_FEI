import re
from Order import Order

class ExexeptionName(Exception):
    pass


class Person():
    def __init__(this):
        this.__name = None
        this.__cpf = None
        this.orders = Order()

    @property
    def setCPF(self):
        return self.__cpf
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

    @setCPF.setter
    def setCPF(self, cpf):
        try:
            if re.findall(r"[^0-9]", cpf):
                raise ExexeptionName("The CPF can only contain numbers!")
            if len(cpf) == 11:
                raise ExexeptionName("The CPF has to contain 11 numbers!")
            if not self.__checkCPF__():
                raise ExexeptionName("The CPF is invalid!")

            self.orders.setCPF(cpf)

        except ExexeptionName as e:
            print("(Error setName)", e)

    def __checkCPF__(self):

        soma = sum(int(self.__cpf[i]) * (10 - i) for i in range(9))
        resto = (soma * 10) % 11
        if resto == 10:
            resto = 0
        if resto != int(self.__cpf[9]):
            return False

        # Check second check digit
        soma = sum(int(self.__cpf[i]) * (11 - i) for i in range(10))
        resto = (soma * 10) % 11
        if resto == 10:
            resto = 0
        if resto != int(self.__cpf[10]):
            return False
        return True






