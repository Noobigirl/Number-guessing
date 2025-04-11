import customtkinter as ctk 

class MyFrame(ctk.CTkFrame):
    def __init__(self, root, fg_color, corner_radius= 0): # frames needs to be initialized with the master frame, which is the attribute root
        super().__init__(root, fg_color= fg_color, corner_radius= corner_radius) # allows me to recreate a frame with custom attributes
        self.text= ctk.CTkLabel(self, text=" Guess the number", text_color= "#fff", font=("Perfect Delight 1992.otf", 20)) 
        #the font is not correctly set. You shoul use a CTkFont object
        self.text.grid(row= 0, column= 0, padx=20, pady= 75, sticky= 'ew')

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Numgy")
        self.geometry("500x550+700+200")
        self._set_appearance_mode("light")
        self.textFrame = MyFrame(self, "#b3b6b7")
        self.textFrame.grid_columnconfigure(0, weight= 1)
        self.textFrame.grid(row= 0, column= 0, padx= 45, pady=10, sticky= "ew")
  


window = MainApp()
window.grid_columnconfigure(0, weight= 1)
window.mainloop()