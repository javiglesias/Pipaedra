#comentarios
#La cosa es hacer un tijeras, papel piedra
#los comentarios seran aleatorios, de entro los 3 que hay en casa seccion
import random
def cpu() :
    posibilidades_cpu = ["Tijera","Piedra","Papel","Debil humano"]
    random.shuffle(posibilidades_cpu)
    return posibilidades_cpu[0]
def comprobar(maq, jug) :
    opciones = ["Tijera","Piedra","Papel","Debil humano"]
    logica = [0,1,2,3]
    contador = 0
    for i in opciones:
        if jug == i:
            jug = logica[contador]
        if maq == i:
            maq = logica[contador]
        contador += 1
    if maq > jug:
        return False
    else:
        return True
while True:
    jugador = 0
    sms_error = ["RECUERDA: solo puedes elegir de 1-3",
    "A mi no me la cuelas, solo de 1-3",
    "ëh eh eh eh de 1 a 3, no te pases de listo"]
    sms_victoria = ["Empatamos, a la proxima pereceras",
    "FUCK, no tendras tanta suerte la siguente",
    "Tienes una mente avanzada para empatarme, humano"]
    sms_derrota_cpu = ["Has usado hack, fijo",
    "esto no quedará asi, juguemos otra",
    "Humano, no tientes a la suerte"]
    sms_derrota_j = ["Ja, que esperabas?",
    "No lo veias venir?",
    "Vuestra especie perecerá"]
    posibilidades = ["Tijera","Piedra","Papel"]
    resultados = ["Ganaste","Perdiste"]
    print("\n","JUGUEMOS, humano:")
    print("\n","1-Tijera","\n","2-Piedra","\n","3-Papel","\n")
    try:
        jugador = int(input('Jugada: '))
    except ValueError:
        print ("NaN")
    if jugador == -1:
        break
    elif jugador >3:
        random.shuffle(sms_error)
        print(sms_error[0])
        continue
    maquina = cpu()
    jugador_1 = posibilidades[jugador-1]
    print("CPU: ",maquina)
    print("Jugador: ", jugador_1)
    if posibilidades[jugador-1] == maquina:
        random.shuffle(sms_victoria)
        print (sms_victoria[0])
    else:
        if comprobar(maquina, jugador_1):
            random.shuffle(sms_derrota_cpu)
            print(sms_derrota_cpu[0])
        else:
            random.shuffle(sms_derrota_j)
            print(sms_derrota_j[0])