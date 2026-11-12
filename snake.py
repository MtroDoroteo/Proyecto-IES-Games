#IMPORTACIÓN DE LIBRERIAS
import tkinter as tk

#VARIABLES GLOBALES
tablero=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

#FUNCIONES

#MAIN
def main():
    ventana = tk.Tk()
    ventana.geometry("1000x600")
    ventana.title("Snake")
    ventana.resizable(False,False)

    canva = tk.Canvas(
        ventana,
        width=800,
        height=400,
        bg= "#FF0000"
    )
    canva.pack()

    for fila in range(5):
        for columna in range(10):
            canva.create_rectangle(
            (columna * 75) + 2, (fila * 75) + 2,
            (columna * 75) + 77, (fila * 75) + 77,
            outline="#000000"
            )

            if tablero[fila][columna] == 1:
                canva.create_oval(
                    (columna * 75) + 7, (fila * 75) + 7,
                    (columna * 75) + 72, (fila * 75) + 72,
                    fill="#00FF00"
                )

    ventana.mainloop()

main()