import customtkinter as ctk 

class MyFrame(ctk.CTkFrame):
    # frames needs to be initialized with the master frame, which is the attribute "root"
    def __init__(self, root, fg_color= "transparent", corner_radius= 0): 
        super().__init__(root, fg_color= fg_color, corner_radius= corner_radius) # allows me to recreate a frame with custom attributes
        #the font is not correctly set. You shoul use a CTkFont object
        self.text= ctk.CTkLabel(self, text=" Guess the number", text_color= "#fff", font=("Perfect Delight 1992.otf", 20)) 
        #sticky attribue allow to expand to the cell size
        self.text.grid(row= 0, column= 0, padx=20, pady= 75, sticky= 'ew') 


class ButtonFrame(ctk.CTkFrame):
    def __init__(self, root, fg_color= "transparent", width= 100, height= 50,corner_radius= 0):
        # you need to explicitly pass the arguments to the constructor since you don't know the order in which the parameters are placed in the parent class
        super().__init__(master= root, fg_color= fg_color, width= width, height= height, corner_radius= corner_radius)
        self.button = ctk.CTkButton(self, text= "Click me", fg_color= "blue")
        self.button.grid(row = 0, column= 0)




class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Numgy")
        self.geometry("500x550+700+200")
        self._set_appearance_mode("dark")

        # Fame containing the text
        self.textFrame = MyFrame(self, "#5f5f5f", 7)
        self.textFrame.grid_columnconfigure(0, weight= 1)
        self.textFrame.grid(row= 0, column= 0, padx= 45, pady=10, sticky= "ew")

        # Frame containing the button
        self.buttonFrame = ButtonFrame(self)
        self.buttonFrame.grid(row= 4, column= 0, padx= 45, pady= 10, sticky="ew")
        self.buttonFrame.grid_columnconfigure(0, weight = 1)
  


window = MainApp()
window.grid_columnconfigure(0, weight= 1)
window.mainloop()