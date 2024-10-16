import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import re

class Deco:
    def __init__(self):
        self.window = tk.Tk()
        self.textArea = tk.Text(self.window, wrap=tk.WORD, height=25, width=80)
        self.createWindow()
        self.showGui()
        self.codigoMaquina

    def createWindow(self):
        self.window.title("Decoder")
        self.window.geometry("700x600")

        titleLabel = tk.Label(self.window, text="Text Analyzer", font=("Arial", 16))
        titleLabel.pack(pady=10)

        button1 = tk.Button(self.window, text="Import file", command=self.selectFile)
        button1.pack(pady=10)
        button2 = tk.Button(self.window, text="Save file", command=self.saveFile)
        button2.pack(pady=10)
        button3 = tk.Button(self.window, text="Decode", command=self.decode)
        button3.pack(pady=10)

        exitButton = tk.Button(self.window, text="Exit", command=self.exitApp)
        exitButton.pack(pady=5)
        self.textArea.pack(pady=10)
        

    def selectFile(self):
        file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")], title="Select file")
        if file:
            self.loadFile(file)

    def loadFile(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        self.textArea.delete('1.0', tk.END)
        self.textArea.insert(tk.END, content)

    
    def decode(self):
        def convertirOp(parte1):
            if (parte1 == "suma"):
                return "01010"
            elif (parte1 == "resta"):
                return  "01110"
            elif (parte1 == "and"):
                return  "01000"
            elif (parte1 == "menorq"):
                return  "01111"
            elif (parte1 == "leer"):
                return  "00000"
            else:
                return "opcion invalida"
        
        def convertirDir(dir):
            numero = dir[1:]

            try:
                ultimo_entero = int(numero)
            except ValueError:
                messagebox.showinfo(f"El último carácter '{numero}' no es un número entero.")
                return "00000"

            nBinario = bin(ultimo_entero)[2:].zfill(5)
            
            return nBinario

        contenido = ""
        contenidoOriginal = ""
        contenidoBinario = ""
        self.codigoMaquina = ""
        lines = self.textArea.get('1.0', tk.END).strip().splitlines()
        for linea in lines:
            linea = linea.strip()

            partes = linea.split(' ')
        
            contenidoOriginal += linea + "\n"

            if len(partes) >= 4:
                parte1 = partes[0].lower()
                parte2 = partes[1]
                parte3 = partes[2]
                parte4 = partes[3]

                op = convertirOp(parte1)
                dirMemoria2 = convertirDir(parte2)
                dirOperando1 = convertirDir(parte3)
                dirOperando2 = convertirDir(parte4)

                newLinea = f"{op[:2]}_{dirOperando1}_{op[2:]}_{dirOperando2}_{dirMemoria2}"
                contenido += newLinea + "\n"
                contenidoBinario += f"{op[:2]}{dirOperando1}{op[2:]}{dirOperando2}{dirMemoria2}\n"
                

            elif(partes[0].lower() == "leer" and len(partes) == 2):
                parte1 = partes[0].lower()
                parte2 = partes[1]

                op = convertirOp(parte1)
                dirMemoria = convertirDir(parte2)

                newLinea = f"{op[:2]}_00000_{op[2:]}_00000_{dirMemoria}"
                contenido += newLinea + "\n"
                contenidoBinario += f"{op[:2]}00000{op[2:]}00000{dirMemoria2}\n"
                
            else :
                print("La línea no contiene suficientes partes:", linea)

        self.textArea.delete('1.0', tk.END)
        self.textArea.insert(tk.END, "Contenido original:\n")
        self.textArea.insert(tk.END, contenidoOriginal + "\n")

        self.textArea.insert(tk.END, "Contenido decodificado:\n")
        self.textArea.insert(tk.END, contenido + "\n")

        self.codigoMaquina = contenidoBinario


    def saveFile(self):
        if not self.codigoMaquina:
            messagebox.showinfo("Error", "No hay contenido decodificado para guardar.")
            return


        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file:
            with open(file, 'w', encoding='utf-8') as file:
                file.write(self.codigoMaquina)

    def exitApp(self):
        self.window.quit()

    def showGui(self):
        self.window.mainloop()

if __name__ == "__main__":
    Deco()
