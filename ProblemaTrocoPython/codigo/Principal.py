from codigo.Troco import CalculaTroco
'''
Classe principal

Classe onde os métodos da classe Troco são utilizados.
'''

class Principal:

    cal = CalculaTroco()
    # Valor do troco.
    valor_troco = 68
    # Lista de moedas disponíveis. Baseada no Real (R$)
    moedas_disponiveis = [100,50,25,10,5,1]
    resp_incial = [0] * (valor_troco + 1)
    contador=[0]*(valor_troco + 1)

    # Mostra a valor do troco em centavos.
    cal.mensagem_quantia(valor_troco)
    # Faz o cálculo inicial e mostra a quantidade de moedas.
    cal.calcula_troco(moedas_disponiveis, valor_troco, contador,resp_incial)
    # Mostra as moedas utilizando a programação dinâmica.
    cal.caminho_dinamico(resp_incial, valor_troco)