import tkinter as tk

counter=0

def klik():
    global counter
    if counter == 0:
        przycisk.config(bg="yellow")
        counter+=1
    elif counter==1:
        napis.config(text="Drugi napis")
        counter+=1
    else:
        zawartosc = pole_tekstowe.get("1.0", "end-1c")
        napis.config(text=zawartosc)
okno = tk.Tk()
okno.title("Tytul okna")
okno.geometry("500x400")

napis = tk.Label(okno, text="Napis nr 1")
napis.pack()
napis.config(font=("Arial", 14))
napis["bg"] = "blue"
napis["fg"]="white"

przycisk = tk.Button(okno)
przycisk.pack()
przycisk.config(height=2, width=20, text="Click")
przycisk.config(font=("Times New Roman", 15), fg="green")
przycisk.config(command=klik)

pole_tekstowe=tk.Text(okno, height=2, width=20)
pole_tekstowe.pack()

ramka=tk.Frame(okno)
ramka.pack()
ramka.columnconfigure(0, weight=1)
ramka.columnconfigure(1, weight=2)
ramka.rowconfigure(0, weight=1)
ramka.rowconfigure(1, weight=2)


pole1=tk.Text(ramka)
pole2=tk.Text(ramka)
pole3=tk.Text(ramka)
pole4=tk.Text(ramka)
pole1.grid(row=0, column=0)
pole2.grid(row=0, column=1)
pole3.grid(row=1, column=0)
pole4.grid(row=1, column=1)


okno.mainloop()