import tkinter as tk
from tkinter import messagebox

turno = 'X'
ganador_x = 0
ganador_o = 0

tablero = [
    ['','',''],
    ['','',''],
    ['','','']
]

def reiniciar_juego():
    global tablero
    tablero = [
        ['','',''],
        ['','',''],
        ['','','']
    ]
    boton1.config(text='', state="active")
    boton2.config(text='', state="active")
    boton3.config(text='', state="active")
    boton4.config(text='', state="active")
    boton5.config(text='', state="active")
    boton6.config(text='', state="active")
    boton7.config(text='', state="active")
    boton8.config(text='', state="active")
    boton9.config(text='', state="active")

def mostrar_tablero():
    for fila in tablero:
        for columna in fila:
            print(columna if columna != '' else '-', end=' | ')
        print()
    print()

def comprobar_ganador():
    #por cada fila en el tablero
    for fila in range(3):
        #for cada columna en la fila
        for columna in range(3):
            if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] != '':
                return turno
            if tablero[columna][0] == tablero[columna][1] == tablero[columna][2] != '':
                return turno

            if tablero[0][0] == tablero[1][1] == tablero [2][2] != '':
                return turno
            if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
                return turno

def dibujar(boton,x,y):
    global ganador_x, ganador_o
    tablero[x][y] = turno
    mostrar_tablero()

    if turno == 'X':
        color = '#FF0000'
    else:
        color = '#0000FF'

    boton.config(
        state = "disable",
        text=turno,
        disabledforeground = color
    )
    ganador = comprobar_ganador()
    if ganador:
        messagebox.showinfo("GANADOR", f"GANÓ {turno}")
        if ganador == 'X':
            ganador_x += 1
        else:
            ganador_o += 1
        return
    cambiar_turno()

def cambiar_turno():
    global turno
    if turno == 'X':
        turno = 'O'
    else:
        turno = 'X'

def main():
    ventana = tk.Tk()
    ventana.title("El gato")
    ventana.geometry("600x700")
    ventana.resizable("False","False")

    global boton1
    boton1 = tk.Button(
        ventana,
        width=20,
        height=10,
        command=lambda: dibujar(boton1,0,0)
    )
    boton1.grid(row=1, column=1, padx=(20,0), pady=(20,0))

    global boton2
    boton2 = tk.Button(
        ventana,
        width=20,
        height=10,
        command=lambda: dibujar(boton2,0,1)
    )
    boton2.grid(row=1, column=2, padx=(0,0), pady=(20,0))

    global boton3
    boton3 = tk.Button(
        ventana,
        width=20,
        height=10,
        command=lambda: dibujar(boton3,0,2)
    )
    boton3.grid(row=1, column=3, padx=(0,0), pady=(20,0))

    global boton4
    boton4 = tk.Button(
        ventana,
        width=20,
        height=10,
        command=lambda: dibujar(boton4,1,0)
    )
    boton4.grid(row=2, column=1, padx=(20,0), pady=(0,0))

    global boton5
    boton5 = tk.Button(
        ventana,
        width=20,
        height=10,
        command=lambda: dibujar(boton5,1,1)
    )
    boton5.grid(row=2, column=2, padx=(0,0), pady=(0,0))

    global boton6
    boton6 = tk.Button(
        ventana,
        width=20,
        height=10,
        command=lambda: dibujar(boton6,1,2)
    )
    boton6.grid(row=2, column=3, padx=(0,0), pady=(0,0))

    global boton7
    boton7 = tk.Button(
        ventana,
        width=20,
        height=10,
        command=lambda: dibujar(boton7,2,0)
    )
    boton7.grid(row=3, column=1, padx=(20,0), pady=(0,0))

    global boton8
    boton8 = tk.Button(
        ventana,
        width=20,
        height=10,
        command=lambda: dibujar(boton8,2,1)
    )
    boton8.grid(row=3, column=2, padx=(0,0), pady=(0,0))

    global boton9
    boton9 = tk.Button(
        ventana,
        width=20,
        height=10,
        command=lambda: dibujar(boton9,2,2)
    )
    boton9.grid(row=3, column=3, padx=(0,0), pady=(0,0))
    
    reinicio = tk.Button(
        ventana,
        text="Reiniciar",
        width=20,
        height=5,
        command=lambda:reiniciar_juego()
    )
    reinicio.grid(row=4,column=2,padx=(0,0),pady=(10,0))

    ventana.mainloop()

main()