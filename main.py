import customtkinter as ctk 
import random





#------ main app -------
class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Numgy")
        self.geometry("500x550+700+200")

        
        # ---- Logic of the number guessing -----

        MAX = 10
        MIN = 0
        toGuess = random.randint(MIN, MAX)
        display = ctk.StringVar(value= f"Guess a number between \n {MIN} and {MAX}") # write notes on that

        # Fame containing the text
        self.textFrame = MyFrame(self, fg_color= "#5f5f5f", corner_radius= 7)
        self.textFrame.text.configure(textvariable = display)
        self.textFrame.grid_columnconfigure(0, weight= 1)
        self.textFrame.grid(row= 0, column= 0, padx= 45, pady=10, sticky= "ew")

        # User entry
        self.UserEntry = ctk.CTkEntry(
            self,
            width= 200, 
            height= 155, 
            placeholder_text="00"
            )
        self.UserEntry.grid(row= 1, column = 0, padx= 45, pady= 10)

        # Frame containing the button
        self.buttonFrame = ButtonFrame(self)
        self.buttonFrame.grid(row= 2, column= 0, padx= 45, pady= 10, sticky="ew")
        self.buttonFrame.grid_columnconfigure(0, weight = 1)
        self.buttonFrame.grid_rowconfigure(0, weight= 1)

        #Frame containing the number of trials left
        self.trial = TrialFrame(self)
        self.trial.grid(row= 3, column= 0)
  
#---- Frame displaying numbers ----
class MyFrame(ctk.CTkFrame):
    def __init__(self, root, fg_color= "transparent",corner_radius= 0, **kwargs): 
        super().__init__( root, **kwargs) # allows me to recreate a frame with custom attributes
        #the font is not correctly set. You shoul use a CTkFont object
        self.font= ctk.CTkFont(family= "Perfect Delight 1992", size= 45)
        self.text= ctk.CTkLabel(self,
                                text_color= "#fff", 
                                font= self.font, 
                                height= 150, 
                                anchor="center", # write notes on that
                                justify= "center" # write notes on that

                                ) 
        #sticky attribue allow to expand to the cell size
        self.text.grid(row= 0, column= 0, padx=20, pady= 15, sticky= 'ew') 

#---- validation button ----
class ButtonFrame(ctk.CTkFrame):
    def __init__(self, root, fg_color= "transparent",corner_radius= 0, **kwargs):
        super().__init__(root, **kwargs)
        # you need to explicitly pass the arguments to the constructor since you don't know the order in which the parameters are placed in the parent class
        self.font = ctk.CTkFont(family= "Perfect Delight 1992", size= 45)
        self.button = ctk.CTkButton(self, text= "Click me", fg_color= "blue", font= self.font, height= 75)
        self.button.grid(row = 0, column= 0)

#----- Number of trials left ------
class TrialFrame(ctk.CTkFrame):
    def __init__(self, root,**kwargs):
        super().__init__(master= root, **kwargs)
        self.font = ctk.CTkFont(family= "Perfect Delight 1992", size= 25, slant= "italic")
        
        # Label containing the number of trials left
        self.text = ctk.CTkLabel(self, text=" Number of trials left: ", font= self.font)
        self.text.grid(row= 0, column= 0)









window = MainApp()

window.grid_columnconfigure(0, weight= 1)
window.grid_rowconfigure(1, weight= 1)
window.mainloop()