from random import randint


class ChuteONumero:
    def __int__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        self.GeradorNumero()
        self.PedirValor()
        while self.tentar_novamente:
            if int(self.valor_chute) > self.valor_aleatorio:
                print('Chute um valor mais baixo!')
                self.PedirValor()
            elif int(self.valor_chute) < self.valor_aleatorio:
                print('Chute um valor mais alto!')
                self.PedirValor()
            self.tentar_novamente = False
            print("PARABÉNS VOCÊ ACERTOU!!")


    def PedirValor(self):
        self.valor_chute = int(input('Chute um número: '))

    def GeradorNumero(self):
        self.valor_aleatorio = randint(self.valor_minimo, self.valor_maximo)


chute = ChuteONumero()
chute.Iniciar()
