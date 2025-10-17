###chatbot
#Diccionario con claves respuestas
respuestas = {
    "hola": "¡Hola! ¿Como estas?",
    "Adios": "¡Adios! Que tengas un buen dia.",
    "como estas" : "muy bien, gracias. ¿y tu?",
    "gracias" : "¡De nada!"
}
print ("chatbaot iniciado. escribe 'salir' para terminar.")
while True: 
    mensaje = input("tu:").lower()

    if mensaje == "salir":
        print("bot: ¡Adios!")
        break

    encontrado = False
    for clave in respuestas:
        if clave in mensaje:
            lista_respuestas = respuestas[clave]
            print("bot", lista_respuestas)
            encontrado = True
            break
    if not encontrado:
        print("bot: lo siento, no entendi eso")    