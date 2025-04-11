import customtkinter as ctk 

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Numgy")
        self.geometry("600x550+700+200")
        self._set_appearance_mode("light")


window = MainApp()
window.mainloop()