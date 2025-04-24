import customtkinter as ctk 
import random

#---- Frame displaying numbers ----
class MyFrame(ctk.CTkFrame):
    def __init__(self, root, fg_color= "transparent",corner_radius= 0, **kwargs): 
        super().__init__( root, **kwargs) # allows me to recreate a frame with custom attributes
        self.font= ctk.CTkFont(family= "Poppins ", size= 20)
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

        self.font = ctk.CTkFont(family= "Poppins ", size= 20)
        self.button = ctk.CTkButton(self, text= "Click me", fg_color= "blue", font= self.font, height= 75)
        self.button.grid(row = 0, column= 0)

#----- Number of trials left ------
class TrialFrame(ctk.CTkFrame):
    def __init__(self, root,**kwargs):
        super().__init__(master= root, **kwargs)
        self.font = ctk.CTkFont(family= "Poppins ", size= 15)
        
        # Label containing the number of trials left
        self.text = ctk.CTkLabel(self, text=" Number of trials left: ", font= self.font)
        self.text.grid(row= 0, column= 0)


#------ main app -------
class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Numgy")
        self.geometry("500x550+700+200")

        
        # ---- Logic of the number guessing -----

        MAX = 10
        MIN = 0
        self.toGuess = random.randint(MIN, MAX)
        display = ctk.StringVar(value= f"Guess a number between \n {MIN} and {MAX}") 
        self.score = 0
        self.trials = 3
        self.guess = None

        # Fame containing the text
        self.textFrame = MyFrame(self, fg_color= "#5f5f5f", corner_radius= 7)
        self.textFrame.text.configure(textvariable = display)
        self.textFrame.grid_columnconfigure(0, weight= 1)
        self.textFrame.grid(row= 0, column= 0, padx= 45, pady=10, sticky= "ew")

        # User entry
        self.UserText = ctk.CTkEntry(
            self,
            width= 200, 
            height= 155, 
            placeholder_text="00",
            justify= "center",
            font= ctk.CTkFont(family= "Poppins ", size=140),
            fg_color= "transparent",
            border_width= 0, # completely gets rid of the border
            )
        self.UserText.grid(row= 1, column = 0, padx= 45, pady= 10)

        # Frame containing the button
        self.buttonFrame = ButtonFrame(self)
        self.buttonFrame.grid(row= 2, column= 0, padx= 45, pady= 10, sticky="ew")
        self.buttonFrame.grid_columnconfigure(0, weight = 1)
        self.buttonFrame.grid_rowconfigure(0, weight= 1)
        self.buttonFrame.button.configure(command= self.getText)

        #Frame containing the number of trials left
        self.trial = TrialFrame(self, fg_color= "transparent")
        self.trial.grid(row= 3, column= 0)

        # if int(self.guess) == self.toGuess:
        #     self.score += 1
        # print(self.toGuess)
        # print(self.guess)
        # print(self.score)
    def getText(self):
        self.guess = self.UserText.get()
        print(self.toGuess)
        print(self.guess)
        

    






window = MainApp()

window.grid_columnconfigure(0, weight= 1)
window.grid_rowconfigure(1, weight= 1)
window.mainloop()