# ---------------- CONSTANTES ---------------- #

PULSOS_10CM = 250      # ajustar na prática
PULSOS_GIRO = 850      # ajustar na prática


# ---------------- MOVIMENTOS ---------------- #

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


# ---------------- FUNÇÕES AUXILIARES ---------------- #

def encontrou_linha():

    return (
        sensor_esquerdo.read()
        or sensor_centro.read()
        or sensor_direito.read()
    )


def deslocamento_medio(inicio_esq, inicio_dir):

    deslocamento_esq = abs(
        motor_esquerdo.encoder() - inicio_esq
    )

    deslocamento_dir = abs(
        motor_direito.encoder() - inicio_dir
    )

    return (deslocamento_esq + deslocamento_dir) / 2


# ---------------- GIRAR ---------------- #

def girar():

    inicio_esq = motor_esquerdo.encoder()
    inicio_dir = motor_direito.encoder()

    while deslocamento_medio(inicio_esq, inicio_dir) < PULSOS_GIRO:

        if encontrou_linha():
            parar()
            return True

        motor_esquerdo.run(-100)
        motor_direito.run(100)

    parar()
    return False


# ---------------- VOLTAR DISTÂNCIA FIXA ---------------- #

def mover_encoder(me, md, pulsos):

    inicio_esq = motor_esquerdo.encoder()
    inicio_dir = motor_direito.encoder()

    while (
        deslocamento_medio(inicio_esq, inicio_dir)
        < pulsos
    ):

        if encontrou_linha():
            parar()
            return True

        motor_esquerdo.run(me)
        motor_direito.run(md)

    parar()
    return False


# ---------------- ACHAR LINHA ---------------- #

def achar_linha(ultimo):

    if ultimo == 'f':

        if mover_encoder(-100, -100, PULSOS_10CM):
            return

    elif ultimo == 'e':

        if mover_encoder(-60, -100, PULSOS_10CM):
            return

    elif ultimo == 'd':

        if mover_encoder(-100, -60, PULSOS_10CM):
            return

    girar()


# ---------------- SEGUIR LINHA ---------------- #

def seguir_linha(ultimo):

    if sensor_centro.read():

        frente()
        ultimo = 'f'

    elif sensor_esquerdo.read():

        esquerda()
        ultimo = 'e'

    elif sensor_direito.read():

        direita()
        ultimo = 'd'

    else:

        parar()
        achar_linha(ultimo)

    return ultimo


# ---------------- PROGRAMA PRINCIPAL ---------------- #

ultimo = 'f'

while True:

    # Obstáculo
    if sensor_distancia.read() <= 20:

        parar()

    else:

        ultimo = seguir_linha(ultimo)