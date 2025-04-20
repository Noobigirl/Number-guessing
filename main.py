import customtkinter as ctk 

class MyFrame(ctk.CTkFrame):
    # frames needs to be initialized with the master frame, which is the attribute "root"
    def __init__(self, root, fg_color= "transparent", corner_radius= 0): 
        super().__init__(root, fg_color= fg_color, corner_radius= corner_radius) # allows me to recreate a frame with custom attributes
        baseFont = ctk.CTkFont(family="Perfect Delight 1992", size= 35)
        #the font is not correctly set. You shoul use a CTkFont object
        self.text= ctk.CTkLabel(self, text="Guess the number", text_color= "#fff", font=baseFont) 
        #sticky attribue allow to expand to the cell size
        self.text.grid(row= 0, column= 0, padx=20, pady= 75, sticky= 'ew') 



class ButtonFrame(ctk.CTkFrame):
    def __init__(self, root, fg_color= "transparent",corner_radius= 0):
        # you need to explicitly pass the arguments to the constructor since you don't know the order in which the parameters are placed in the parent class
        super().__init__(master= root, fg_color= fg_color, corner_radius= corner_radius)
        baseFont = ctk.CTkFont(family="Perfect Delight 1992", size= 25)
        self.button = ctk.CTkButton(self, text= "Click me", fg_color= "blue", font= baseFont)
        self.button.grid(row = 0, column= 0, sticky="nsew")




class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Numgy")
        self.geometry("500x550+700+200")
        

        # Fame containing the text
        self.textFrame = MyFrame(self, "#5f5f5f", 7)
        self.textFrame.grid_columnconfigure(0, weight= 1)
        self.textFrame.grid(row= 0, column= 0, padx= 45, pady=10, sticky= "ew")

        # Frame containing the button
        self.buttonFrame = ButtonFrame(self)
        self.buttonFrame.grid(row= 1, column= 0, padx= 45, pady= 10, sticky="ew")
        self.buttonFrame.grid_columnconfigure(0, weight = 1)
        self.buttonFrame.grid_rowconfigure(0, weight= 1)
  


window = MainApp()

window.grid_columnconfigure(0, weight= 1)
window.grid_rowconfigure(1, weight= 1)
window.mainloop()