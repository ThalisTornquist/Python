
'''
motor_esquerdo.run(velocidade)
motor_direito.run(velocidade)

motor_esquerdo.stop()
motor_direito.stop()

# Sensores
sensor_esquerdo.read()      # True se detectar linha
sensor_centro.read()
sensor_direito.read()

sensor_distancia.read()     # Distância em centímetros

# Botão
botao.start()

# Espera
sleep(segundos)
'''
import time

from sympy.physics.units import millisecond


def frente():
    motor_esquerdo.run(100)
    motor_direito.run(100)

def esquerda():
    motor_esquerdo.run(60)
    motor_direito.run(100)

def direita():
    motor_esquerdo.run(100)
    motor_direito.run(60)

def parar():
    motor_esquerdo.stop()
    motor_direito.stop()


def start():
    while True:
        if botao:
            frente()
            time.sleep(3)
            break

def q3():
    while True:
        if sensor_centro:
            frente()
        elif sensor_esquerda:
            esquerda()
        elif sensor_direita:
            direita()
        else:
            parar()

def q4():
    while True:
        if sensor_distancia < 15:
            parar()
        else:
            seguir_linha()

def girar_eixo():
    while linha = False or giro < 360:
        MD = 100
        ME = -100

def achar_linha():
    utimo_comando_me = 'me 60' #rebe o ulktimo comando que o robo executou
    utimo_comando_md = 'md 100'

    girar_eixo()
    while True:
        if linha = false:
            MD = utimo_comando_md * -1
            ME = utimo_comando_me * -1
            time.sleep(0.5)
            girar_eixo()

        else:
            estado = seguir_linha()
            break # em teoria ele vai girar no eixo e procura a linha se nao achar ele segue o ultimoi comando porem no reverso e depos faz o giro novamente

def estados():
    estado = parar()

    if botao:
        estado = seguir_linha()

    if perdeu_linha:
        estado = achar_linha()

# o pid serve para corrigir de forma automatica a tragetoria de um robo;
# pois ai o robo nao fica 'cego' durante o tempo parado
# aumentaria o d do pid