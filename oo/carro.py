"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado de velocidade
2) Método acelerar = Que deverá incrementar a velocidade de uma unidade
3) Método frear = Que deverá decrementar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, sul, leste, oeste
2) Método girar_a_direita
3) Método girar_a_esquerda

  N
O   L
  S

Exemplo:
# Testando motor
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0
>>> # Testando direção
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.virar_a_direita()
>>> direcao.valor
'Leste'
>>> direcao.virar_a_direita()
>>> direcao.valor
'Sul'
>>> direcao.virar_a_direita()
>>> direcao.valor
'Oeste'
>>> direcao.virar_a_direita()
>>> direcao.valor
'Norte'
>>> direcao.virar_a_esquerda()
>>> direcao.valor
'Oeste'
>>> direcao.virar_a_esquerda()
>>> direcao.valor
'Sul'
>>> direcao.virar_a_esquerda()
>>> direcao.valor
'Leste'
>>> direcao.virar_a_esquerda()
>>> direcao.valor
'Norte'
>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.frear()
>>> carro.calcular_velocidade()
0
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
'Leste'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Oeste'
"""