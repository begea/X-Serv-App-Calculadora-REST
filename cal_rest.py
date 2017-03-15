#!/usr/bin/python3

import webapp

class calc (webapp.webApp):

    calculadora = []

    def parse(self, request):

        metodo = request.split()[0]
        oper1 = request.split()[1].split("/")[1]
        oper2 = request.split(',')[-2]
        operacion = request.split(',')[-1]
        return (metodo, oper1, oper2, operacion)

    def process(self, parsedRequest):

        (metodo, oper1, oper2, operacion) = parsedRequest

        if metodo == "PUT":
            self.calculadora = [oper1, oper2, operacion]
            return("200 OK", "<html><body>Operacion realizada</body></html>")

        elif metodo == "GET":

                op = self.calculadora[2]
                if op == "+":
                    op1 = self.calculadora[0]
                    op2 = self.calculadora[1]
                    res = int(op1) + int(op2)
                    return ("200 OK", op1 + "+" + op2 + "=" + str(res))

                elif op == "-":
                    op1 = self.calculadora[0]
                    op2 = self.calculadora[1]
                    res = int(op1) - int(op2)
                    return ("200 OK", op1 + "-" + op2 + "=" + str(res))

                elif op == "*":
                    op1 = self.calculadora[0]
                    op2 = self.calculadora[1]
                    res = int(op1) * int(op2)
                    return ("200 OK", op1 + "*" + op2 + "=" + str(res))

                elif op == "/":
                    op1 = self.calculadora[0]
                    op2 = self.calculadora[1]
                    res = int(op1) / int(op2)
                    return ("200 OK", op1 + "/" + op2 + "=" + str(res))

                else:
                    return("404 Error", "<html><body>Operador mal introducido</body></html>")
        else:
            return("404 Error", "<html><body>Operacion mal realizada</body></html>")

if __name__ == "__main__":
    testWebApp = calc("localhost", 1238)
