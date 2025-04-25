import customtkinter as ctk 
import random

"""
features to add:
- restricting the user to input 2 char long number ❌
- displaying the placeholder text even after deletion ❌
- decrement the number of trials left after each unsuccessfull trial ❌
- increment the score for successfull guesses ❌
- display the score ✅
- force the user to only enter integers ❌
- give hints to the user on how close they are to the true number ❌
"""

#---- Frame displaying numbers ----
class NumberGuessingFrame(ctk.CTkFrame):
    def __init__(self, root, **kwargs): 
        super().__init__( root, **kwargs) 
        self.font= ctk.CTkFont(family= "Poppins", size= 20) # setting the font of the text
        self.mainText= ctk.CTkLabel(self,
                                text_color= "#fff", 
                                font= self.font, 
                                height= 150, 
                                anchor="center", 
                                justify= "center"
                                ) # Stringvar used to set the text later in the main app
        
        self.scoreText = ctk.CTkLabel(self, 
                                      text_color= "#fff",
                                      font= self.font,

        )
        # sticky attribue allow to expand to the cell size
        self.mainText.grid(row= 1, column= 0, padx=20, pady= 15, sticky= 'ew') 
        self.scoreText.grid(row =0, column= 0, padx= 10, sticky ="w")

#---- display alerts
class AlertFrame(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(master= root, **kwargs)
        self.alertText = ctk.CTkLabel(self) # textvariable set in the main app
        self.alertText.pack()

#---- validation button ----
class ButtonFrame(ctk.CTkFrame):
    def __init__(self, root, fg_color= "transparent",corner_radius= 0, **kwargs):
        super().__init__(root, **kwargs)

        self.font = ctk.CTkFont(family= "Poppins", size= 20) # setting the font of the text

        # button itself
        self.button = ctk.CTkButton(self,
                                    text= "Click me", 
                                    fg_color= "blue", 
                                    font= self.font, 
                                    height= 75)
        self.button.grid(row = 0, column= 0)

#----- Number of trials left ------
class TrialFrame(ctk.CTkFrame):
    def __init__(self, root,**kwargs):
        super().__init__(master= root, **kwargs)
        self.font = ctk.CTkFont(family= "Poppins", size= 15) # setting the font of the text
        
        # Label containing the number of trials left
        self.text = ctk.CTkLabel(self, font= self.font)
        self.text.grid(row= 0, column= 0)


#------ main app -------
class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Numgy")
        self.geometry("400x550+700+200") # window size and position

        
        # ---- Logic of the number guessing -----
        MAX = 10
        MIN = 0
        self.toGuess = random.randint(MIN, MAX) # generation of the number to guess
        self.score = 0
        self.trials = 3
        self.guess = None

        # ---- Variable text ----
        display = ctk.StringVar(value= f"Guess a number between \n {MIN} and {MAX}") 
        score = ctk.StringVar(value= f" Score: {self.score}")
        trials = ctk.StringVar(value= f"Number of trials left: {self.trials}")
        self.alertText = ctk.StringVar()
        

        # Fame containing the text
        self.textFrame = NumberGuessingFrame(self, fg_color= "#5f5f5f", corner_radius= 7)
        self.textFrame.mainText.configure(textvariable = display) # displays the range within which the number lies
        self.textFrame.scoreText.configure(textvariable = score)
        self.textFrame.grid_columnconfigure(0, weight= 1)
        self.textFrame.pack(fill= "both")

        # User entry frame
        self.UserText = ctk.CTkEntry(
            self,
            width= 175, 
            height= 75, 
            placeholder_text="00",
            justify= "center",
            font= ctk.CTkFont(family= "Poppins", size=100),
            fg_color= "transparent",
            border_width= 0, # completely gets rid of the border
            )
        self.UserText.pack(fill= "both", pady= (5, 0))

        #  Frame with Alert text
        self.alert = AlertFrame(self)
        self.alert.alertText.configure(textvariable= self.alertText)
        self.alert.pack(pady = (5, 0))

        # Frame containing the button
        self.buttonFrame = ButtonFrame(self)
        self.buttonFrame.pack(pady= (10, 0))
        self.buttonFrame.grid_columnconfigure(0, weight = 1)
        self.buttonFrame.grid_rowconfigure(0, weight= 1)
        self.buttonFrame.button.configure(command= self.getText)

        # Frame containing the number of trials left
        self.trial = TrialFrame(self, fg_color= "transparent", width= 40, height=20)
        self.trial.text.configure(textvariable = trials)
        self.trial.pack( pady= (5,0))

    # just to test what happens in the terminal
    def getText(self):
        self.guess = self.UserText.get()
        print(self.toGuess)  
        print(self.guess)
        self.alertText.set("alert")
        self.UserText.delete(0, "end") 
    
    # logic to implement later
    # def checkIntInput(self, func):
    #     pass

    
    # def incrementScore(self):
    #     if int(self.guess) == self.toGuess:
    #         self.score += 1
    #     print(self.score)

    

window = MainApp()

window.mainloop()