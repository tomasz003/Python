import tkinter as tk

aktualny_gracz="O"

def klik(przycisk:tk.Button):
    global aktualny_gracz
    przycisk.config(text=aktualny_gracz)
    if aktualny_gracz == "O":
        aktualny_gracz = "X"
    else:
        aktualny_gracz = "O"

okno = tk.Tk()
okno.title("Kółko i krzyżyk")
okno.geometry("600x700")

fr_przyciski=tk.Frame(okno)
fr_przyciski.grid(column=0, row=0)

przyciski=[]
for i in range(9):
    przycisk = tk.Button(fr_przyciski, text=str(i))
    przycisk.grid(column=i%3, row= i//3)
    przycisk.config(width=10, height=5)
    przycisk.config(command=lambda x=przycisk:klik(x))
    przyciski.append(przycisk)

okno.mainloop()

