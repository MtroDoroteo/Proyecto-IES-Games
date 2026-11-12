
import tkinter as tk
from tkinter import messagebox

# Función para saludar
def saludar(entrada_nombre,mensaje,boton):
    nombre = entrada_nombre.get().strip()

    if nombre == "":
        messagebox.showwarning(
            "Campo vacío",
            "Por favor, escribe tu nombre."
        )
    else:
        mensaje.config(
            text=f"¡Hola, {nombre}!\nBienvenido a nuestra aplicación.",
            fg="#00E676"
        )

        boton.config(
            state="disabled",
            text="¡SALUDO ENVIADO!"
        )

def main():
    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Ventana de Bienvenida")
    ventana.geometry("500x400")
    ventana.resizable(False, False)
    ventana.configure(bg="#151A30")

    # Título
    titulo = tk.Label(
        ventana,
        text="¡BIENVENIDO!",
        font=("Impact", 28),
        fg="#00FF00",
        bg="#151A30"
    )
    titulo.pack(pady=(35, 0))

    # Instrucciones
    instruccion = tk.Label(
        ventana,
        text="¿Cómo te llamas?",
        font=("Arial", 14, "bold"),
        fg="#FFD740",
        bg="#151A30"
    )
    instruccion.pack(pady=(10, 10))

    # Entrada de nombre
    entrada_nombre = tk.Entry(
        ventana,
        font=("Arial", 16),
        width=25,
        justify="center",
        bg="#263253",
        fg="white",
        insertbackground="white",
        relief="flat"
    )
    entrada_nombre.pack(ipady=10)

    # Botón para saludar
    boton = tk.Button(
        ventana,
        text="SALUDAR",
        font=("Impact", 16),
        width=18,
        height=2,
        bg="#FF1744",
        fg="white",
        activebackground="#D50000",
        activeforeground="white",
        relief="raised",
        bd=4,
        cursor="hand2",
        command= lambda: saludar(entrada_nombre, mensaje, boton)
    )
    boton.pack(pady=25)

    # Mensaje de bienvenida
    mensaje = tk.Label(
        ventana,
        text="",
        font=("Arial", 14, "bold"),
        fg="#00E676",
        bg="#151A30",
        justify="center"
    )
    mensaje.pack(pady=5)

    ventana.bind("<Return>", lambda event: saludar(entrada_nombre, mensaje, boton))
    # Iniciar ventana
    ventana.mainloop()

main()