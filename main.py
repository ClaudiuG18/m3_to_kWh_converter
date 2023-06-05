from tkinter import * 

class MainWindow(Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title("m3 to kWh Converter")
        self.geometry("400x200")
        self.resizable(height=False, width=False)
        frame = Converter(self).grid(row=0, column=0, sticky="NSEW")
  

        
class Converter (Frame):
    def __init__(self,container):
        super().__init__(container)
        m3_label = Label(self, text="Metri cubi gaz:", font=("arial",15, "bold")).grid(padx=5, pady=5)
        m3_entry = Entry(self, width= 20, font=("arial", 15,"bold")).grid(row=1,column=0, padx=5, pady=5)
        info_label =Label(self, text="Pentru acest calcul au fost luate in considerare urmatoarele:").grid(row=3,column=0)
        info_label2 = Label(self, text="Brennwert 11.305, ZusatzZahl = 0,9")
        convert_button = Button(self, text="CONVERT", font=("arial",15,"bold")).grid(row=2, column=0, ipadx=2, ipady=2)






root = MainWindow()
root.mainloop()

