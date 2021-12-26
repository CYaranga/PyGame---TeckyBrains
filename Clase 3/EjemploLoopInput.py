prompt = "\nDime algo y lo repetire por ti:"
prompt += "\nIntroduce 'salir' pata finalizar el programa. "
mensaje = ""
while mensaje != 'salir':
    mensaje = input(prompt)

    if mensaje != 'salir':
        print(mensaje)