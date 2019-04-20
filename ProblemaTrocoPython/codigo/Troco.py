'''
Classe de cálculo de troco

Métodos: calculo_troco() - Faz o cálculo dos
'''


class CalculaTroco:
    # Faz o cálculo inicial e mostra a quantidade de moedas necessárias para solução.
    def calcula_troco(self, validas, valor_troco, cont, resp_inicial):
        for i in range(1, valor_troco + 1):
            contador = i
            moeda_encontrada = 1
            for j in validas:
                if j <= i:
                    if cont[i - j] + 1 < contador:
                        contador = cont[i - j] + 1
                        moeda_encontrada = j
                # Armazena na tabela os troco ótimos
                cont[i] = contador
                resp_inicial[i] = moeda_encontrada
        # Retorna a quantidade ótima para o troco
        self.mensagem_quantidade_moedas(cont[valor_troco])

    def caminho_dinamico(self, resp_inicial, valor_troco):
        moedas = []
        while valor_troco > 0:
            moeda_escolhida = resp_inicial[valor_troco]
            moedas.append(moeda_escolhida)
            valor_troco = valor_troco - moeda_escolhida
        # Mostra as moedas selecionadas para o método dinâmico
        self.mensagem_resultados(moedas)

    def mensagem_quantidade_moedas(self, quant):
        print("A quantidade necessária de moedas para o resultado são: {}.\n".format(quant))

    def mensagem_resultados(self, moedas):
        print("Resultado com programação dinâmica:{}.\n".format(moedas))

    # Método para mostrar a quantia do troco.
    def mensagem_quantia(self, quantia):
        print("O troco necessário para conlcuir essa trasação, em centavos, é de {} centavos.\n".format(quantia))