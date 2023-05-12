import openai

openai.api_key = "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"

def generar_respuesta(pregunta):
    respuesta = "No se pudo obtener una respuesta en este momento."

    try:
        # Generar respuesta de la IA
        respuesta = openai.Completion.create(
            engine="ada",
            prompt=pregunta,
            max_tokens=5,
            n=1,
            stop=None,
            temperature=0.7
        )

        respuesta = respuesta.choices[0].text.strip()

    except Exception as e:
        respuesta = f"Error: {str(e)}"

    return respuesta

pregunta = "¿Qué es ChatGPT?"
respuesta = generar_respuesta(pregunta)
print(respuesta)
