from src.conta.conta import Conta
from src.conta.conta_poupanca import ContaPoupanca


class CriarPoupanca:
    if __name__ == '__main__':

        conta = Conta("21.342-7")

        conta = ContaPoupanca(conta)
        #  print(type(conta))
        #  conta = ContaPoupanca("21.342-7")
        conta.creditar(500.87)
        conta.debitar(45.00)

        print(conta.get_saldo())

        ContaPoupanca(conta).render_juros(0.01)
        print(conta.get_saldo())
        #  print(type(conta))

        #  conta.render_juros(0.01)
        #  print(conta.get_saldo())
