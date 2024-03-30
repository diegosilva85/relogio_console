import time

segundo = '00'
contador = 0


# -------------------------------------- Ajusta os valores que serão mostrados -----------------------------------------
def display(valor: int) -> str:
    if valor < 10:
        return f'0{valor}'
    if valor >= 10:
        return f'{valor}'


# ---------------------------------------------- Ajustar a hora --------------------------------------------------------
hora_int = None

while hora_int is None or hora_int > 23 or hora_int < 0:
    try:
        hora_int = int(input('Informe a hora: '))
        if hora_int > 23 or hora_int < 0:
            print("Valor não permitido, por favor insira um valor entre 0 e 23.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

hora = display(hora_int)

# ---------------------------------------------- Ajustar os minutos ----------------------------------------------------
minuto_int = None

while minuto_int is None or minuto_int > 59 or minuto_int < 0:
    try:
        minuto_int = int(input('Informe os minutos: '))
        if minuto_int > 59 or minuto_int < 0:
            print("Valor não permitido, por favor insira um valor entre 0 e 59.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

minuto = display(minuto_int)

# --------------------------------------------- Laço principal ---------------------------------------------------------
while True:
    print(f'{hora}:{minuto}:{segundo}')
    time.sleep(1)
    contador += 1
    if contador == 60:
        minuto_int += 1
        contador = 0
    if minuto_int == 60:
        hora_int += 1
        minuto_int = 0
    if hora_int == 24:
        hora_int = 0

    segundo = display(contador)
    minuto = display(minuto_int)
    hora = display(hora_int)
