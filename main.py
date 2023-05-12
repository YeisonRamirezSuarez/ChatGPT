import tkinter as tk
from tkinter import messagebox
import openai

# Configurar OpenAI API
openai.api_key = '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'

def enviar_mensaje():
    mensaje = campo_texto.get()
    mostrar_mensaje("Tú", mensaje)

    # Obtener respuesta de la IA
    respuesta = generar_respuesta(mensaje)
    mostrar_mensaje("IA", respuesta)

    campo_texto.delete(0, tk.END)

def mostrar_mensaje(nombre, mensaje):
    etiqueta_mensaje = tk.Label(chat_frame, text=f"{nombre}: {mensaje}", bg="lightblue", relief=tk.RAISED, anchor="w", justify=tk.LEFT)
    etiqueta_mensaje.pack(padx=10, pady=5, anchor="w")

def generar_respuesta(pregunta):
    respuesta = "No se pudo obtener una respuesta en este momento."

    try:
        # Generar respuesta de la IA
        respuesta = openai.Completion.create(
            engine="text-davinci-003",
            prompt=pregunta,
            max_tokens=1200,
            n=1,
            stop=None,
            temperature=0.7
        )

        respuesta = respuesta.choices[0].text.strip()

    except Exception as e:
        messagebox.showerror("Error", str(e))

    return respuesta

ventana = tk.Tk()
ventana.title("Chat")

# Frame para el chat
chat_frame = tk.Frame(ventana)
chat_frame.pack(padx=10, pady=10)

# Campo de entrada de texto
campo_texto = tk.Entry(ventana, width=50)
campo_texto.pack(padx=10, pady=10)

# Botón de enviar
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack(padx=10, pady=5)

ventana.mainloop()
