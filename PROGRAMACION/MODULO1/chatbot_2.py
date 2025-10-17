#chatbot "asistente"
respuestas = {
    "hola": "¡hola! ¿como estas?",
    "como estas" : "muy bien, gracias. ¿y tu?",
    "ayuda" : "¿En que puedo ayudarte?",
    "gracias" : "¡De nada!", 
    "adios" : "Que tengas un buen dia",
}
print ("chatbot iniciado. escribe 'salir' para terminar.")
while True: 
    mensaje = input("tu:").lower()

    if mensaje == "salir":
        print("asistente: ¡Adios!")
        break

    encontrado = False
    for clave in respuestas:
        if clave in mensaje:
            lista_respuestas = respuestas[clave]
            print("asistente", lista_respuestas)
            encontrado = True
            break
    if not encontrado:
        print("asistente: lo siento, no entendi eso")    