import datetime
from datetime import date


class Order:

    def setCPF(self, cpf):
        self.cpf = cpf
        self.order = {self.cpf: {"Pedidos": {}}}

    def addOrder(self, idOrder, quantity, price, operationID):
        order = self.order[self.cpf]

        order["Pedidos"].update({
            len(order["Pedidos"]): {
                "ID": idOrder,
                "quantity": quantity,
                "price": price,
                "date": {"yy/mm/dd": date.today(), "hour": datetime.datetime.now()},
                "operationID": operationID
            }})

#   Idorder define o tipo de produto
#   quantity quantidade do produto
#   price valor de produto
#   operationID define o que aconteceu nesse pedido removido adicioanado