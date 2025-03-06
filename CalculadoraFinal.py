from tkinter import *
import tkinter as tk
import re

root = tk.Tk()
root.title("Calculadora")
root.geometry("334x518")
root.config(bg="black")
root.resizable(False, False)
despuesResultado = False

def borrar():
    pantalla.delete("1.0", "end")
    pantalla.insert("1.0", "0")

def borrarCaracter():
    pantalla.delete("end-2c", "end-1c")
    if pantalla.get("1.0", "end-1c") == "" or pantalla.get("1.0", "end-1c") == "0":
        pantalla.delete("1.0", "end")
        pantalla.insert("1.0", "0")

def insertar(valor):
    global despuesResultado
    if despuesResultado:
        if valor in ["+", "-", "x", "÷"]:
            despuesResultado = False
        else:
            pantalla.delete("1.0", "end")
            despuesResultado = False

    if pantalla.get("1.0", "end-1c") == "Error":
        pantalla.delete("1.0", "end")
        pantalla.insert("1.0", "0")

    validar = pantalla.get("end-2c", "end-1c")
    longitud = len(pantalla.get("1.0", "end-1c"))
    operaciones = ["+", "-", "x", "÷"]
    especial = ["\u00B2", "\u221A", "1/"]

    if validar in operaciones and valor in operaciones:
        pantalla.delete("end-2c", "end-1c")
    elif validar not in operaciones and valor in operaciones:
        operacion()
        despuesResultado = False
        pantalla.insert("end", valor)
        return

    if pantalla.get("1.0", "end-1c") == "0" and valor not in operaciones:
        pantalla.delete("1.0", "end")
    if validar in especial and valor not in operaciones:
        operacion()
        despuesResultado = False

    if longitud > 15:
        return
    pantalla.insert("end", valor)
    if longitud <= 12:
        pantalla.config(font=("Segoe UI Semibold", 36))
    else:
        pantalla.config(font=("Segoe UI Semibold", 24))

def operacion():
    global despuesResultado
    try:
        aux = pantalla.get("1.0", "end-1c")
        aux = aux.replace("x", "*")
        aux = aux.replace("÷", "/")
        aux = aux.replace("\u00B2", "**2")
        aux = aux.replace("\u221A", "**0.5")
        aux = aux.replace("1/", "-1")
        aux = aux.replace("%", "/100")

        resultado = eval(aux)
        resultado = round(resultado, 15)
        pantalla.delete("1.0", "end")
        pantalla.insert("1.0", str(resultado))
        despuesResultado = True

        longitud = len(pantalla.get("1.0", "end-1c"))
        if longitud <= 12:
            pantalla.config(font=("Segoe UI Semibold", 36))
        else:
            pantalla.config(font=("Segoe UI Semibold", 24))
    except Exception:
        pantalla.delete("1.0", "end")
        pantalla.insert("1.0", "Error")
        despuesResultado = True

def positivoNegativo():
    if pantalla.get("1.0", "end-1c") != "0":
        aux = pantalla.get("1.0", "end-1c")
        resultado = float(aux) * -1
        pantalla.delete("1.0", END)
        pantalla.insert("1.0", resultado)

def unoSobreX():
    if pantalla.get("1.0", "end-1c") != "0":
        aux = pantalla.get("1.0", "end-1c")
        resultado = 1 / float(aux)
        pantalla.delete("1.0", END)
        pantalla.insert("1.0", resultado)

def porcentaje():
    aux = pantalla.get("1.0", "end-1c")
    dividir = re.split(r'([÷x+-])', aux)

    global despuesResultado

    if len(dividir) >= 3 and dividir[0] and dividir[2]:
        num1, operador, num2 = float(dividir[0]), dividir[1], float(dividir[2])

        if operador == '+':
            resultado = num1 + (num1 * num2 / 100)
        elif operador == '-':
            resultado = num1 - (num1 * num2 / 100)
        elif operador == 'x':
            resultado = (num1 * num2) / 100
        elif operador == '÷':
            resultado = (num1 / num2) * 100
        else:
            resultado = 0

        pantalla.delete("1.0", "end")
        pantalla.insert("end", str(resultado))
        despuesResultado = True
    else:
        pantalla.delete("1.0", "end")
        pantalla.insert("end", "0")

texto = tk.Label(root, text="Estándar ", font=("Segoe UI Semibold", 18), fg="white", bg="black", anchor="w")
texto.place(x=2, y=10, width=100, height=36)

pantalla = tk.Text(root, width=12, font=("Segoe UI Semibold", 36), fg="white", bg="black", relief="flat")
pantalla.insert("1.0", "0")
pantalla.place(x=2, y=48, width=329, height=80)

boton5 = tk.Button(root, text="%", font=("Segoe UI Semibold", 18), fg="white", bg="dimgray", relief="flat", height=1, width=5, command=porcentaje)
boton5.place(x=2, y=168)

boton6 = tk.Button(root, text="CE", font=("Segoe UI Semibold", 18), fg="white", bg="dimgray", relief="flat", height=1, width=5, command=borrar)
boton6.place(x=85, y=168)

boton7 = tk.Button(root, text="C", font=("Segoe UI Semibold", 18), fg="white", bg="dimgray", relief="flat", height=1, width=5, command=borrar)
boton7.place(x=168, y=168)

boton8 = tk.Button(root, text="<--", font=("Segoe UI Semibold", 18), fg="white", bg="dimgray", relief="flat", height=1, width=5, command=borrarCaracter)
boton8.place(x=251, y=168)

boton9 = tk.Button(root, text="1/x", font=("Segoe UI Semibold", 18), fg="white", bg="dimgray", relief="flat", height=1, width=5, command=lambda: unoSobreX())
boton9.place(x=2, y=226)

boton10 = tk.Button(root, text="x\u00B2", font=("Segoe UI Semibold", 18), fg="white", bg="dimgray", relief="flat", height=1, width=5, command=lambda: insertar("\u00B2"))
boton10.place(x=85, y=226)

boton11 = tk.Button(root, text="\u221Ax", font=("Segoe UI Semibold", 18), fg="white", bg="dimgray", relief="flat", height=1, width=5, command=lambda: insertar("\u221A"))
boton11.place(x=168, y=226)

boton12 = tk.Button(root, text="÷", font=("Segoe UI Semibold", 18), fg="white", bg="dimgray", relief="flat", height=1, width=5, command=lambda: insertar("÷"))
boton12.place(x=251, y=226)

boton13 = tk.Button(root, text="7", font=("Segoe UI Semibold", 18), fg="white", bg="gray", relief="flat", height=1, width=5, command=lambda: insertar("7"))
boton13.place(x=2, y=284)

boton14 = tk.Button(root, text="8", font=("Segoe UI Semibold", 18), fg="white", bg="gray", relief="flat", height=1, width=5, command=lambda: insertar("8"))
boton14.place(x=85, y=284)

boton15 = tk.Button(root, text="9", font=("Segoe UI Semibold", 18), fg="white", bg="gray", relief="flat", height=1, width=5, command=lambda: insertar("9"))
boton15.place(x=168, y=284)

boton16 = tk.Button(root, text="x", font=("Segoe UI Semibold", 18), fg="white", bg="dimgray", relief="flat", height=1, width=5, command=lambda: insertar("x"))
boton16.place(x=251, y=284)

boton17 = tk.Button(root, text="4", font=("Segoe UI Semibold", 18), fg="white", bg="gray", relief="flat", height=1, width=5, command=lambda: insertar("4"))
boton17.place(x=2, y=342)

boton18 = tk.Button(root, text="5", font=("Segoe UI Semibold", 18), fg="white", bg="gray", relief="flat", height=1, width=5, command=lambda: insertar("5"))
boton18.place(x=85, y=342)

boton19 = tk.Button(root, text="6", font=("Segoe UI Semibold", 18), fg="white", bg="gray", relief="flat", height=1, width=5, command=lambda: insertar("6"))
boton19.place(x=168, y=342)

boton20 = tk.Button(root, text="-", font=("Segoe UI Semibold", 18), fg="white", bg="dimgray", relief="flat", height=1, width=5, command=lambda: insertar("-"))
boton20.place(x=251, y=342)

boton21 = tk.Button(root, text="1", font=("Segoe UI Semibold", 18), fg="white", bg="gray", relief="flat", height=1, width=5, command=lambda: insertar("1"))
boton21.place(x=2, y=400)

boton22 = tk.Button(root, text="2", font=("Segoe UI Semibold", 18), fg="white", bg="gray", relief="flat", height=1, width=5, command=lambda: insertar("2"))
boton22.place(x=85, y=400)

boton23 = tk.Button(root, text="3", font=("Segoe UI Semibold", 18), fg="white", bg="gray", relief="flat", height=1, width=5, command=lambda: insertar("3"))
boton23.place(x=168, y=400)

boton24 = tk.Button(root, text="+", font=("Segoe UI Semibold", 18), fg="white", bg="dimgray", relief="flat", height=1, width=5, command=lambda: insertar("+"))
boton24.place(x=251, y=400)

boton1 = tk.Button(root, text="+/-", font=("Segoe UI Semibold", 18), fg="white", bg="gray", relief="flat", height=1, width=5, command=positivoNegativo)
boton1.place(x=2, y=458)

boton2 = tk.Button(root, text="0", font=("Segoe UI Semibold", 18), fg="white", bg="gray", relief="flat", height=1, width=5, command=lambda: insertar("0"))
boton2.place(x=85, y=458)

boton3 = tk.Button(root, text=".", font=("Segoe UI Semibold", 18), fg="white", bg="gray", relief="flat", height=1, width=5, command=lambda: insertar("."))
boton3.place(x=168, y=458)

boton4 = tk.Button(root, text="=", font=("Segoe UI Semibold", 18), fg="midnightblue", bg="lightskyblue", relief="flat", height=1, width=5, command=operacion)
boton4.place(x=251, y=458)

root.mainloop()
#sin comentarios