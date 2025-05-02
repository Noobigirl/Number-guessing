import random
import customtkinter as ctk 
import appUI
"""
features to add:
- restricting the user to input 2 char long number ❌
- displaying the placeholder text even after deletion ❌
- decrement the number of trials left after each unsuccessfull trial ❌
- increment the score for successfull guesses ❌
- display the score ✅
- force the user to only enter integers ✅
- give hints to the user on how close they are to the true number ❌
"""


#------ main app -------
class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Numgy")
        self.geometry("400x550+700+200") # window size and position

        # initialisation of the game
        self.MIN, self.MAX = 0, 10 # range of values to guess
        self.toGuess = random.randint(self.MIN, self.MAX) # generate value to guess
        self.score = 0 # score initialized to 0
        trials = 3 # 3 trials per game

        # ---- Variable text ----
        instruction = ctk.StringVar(value= f"Guess a number between \n {self.MIN} and {self.MAX}") 
        self.score_text = ctk.StringVar(value= f" Score: {self.score}")
        trials_text = ctk.StringVar(value= f"Number of trials left: {trials}")
        self.alertText = ctk.StringVar()
        
        # ---- Frame containing the text----
        self.textFrame = appUI.NumberGuessingFrame(self, fg_color= "#5f5f5f", corner_radius= 7)
        # instructions giving the range within which the number lies and the score
        self.textFrame.scoreText.configure(textvariable = self.score_text)
        self.textFrame.mainText.configure(textvariable = instruction) 
        self.textFrame.grid_columnconfigure(0, weight= 1)
        self.textFrame.pack(fill= "both")

        # User entry frame
        self.UserText = ctk.CTkEntry(
            self,
            width= 175, 
            height= 75, 
            placeholder_text="00", # default text
            justify= "center",
            font= ctk.CTkFont(family= "Poppins", size=100),
            fg_color= "transparent",
            border_width= 0, # completely gets rid of the border
            )
        self.UserText.pack(fill= "both", pady= (5, 0))

        #  Frame with Alert text
        self.alert = appUI.AlertFrame(self)
        self.alert.alertText.configure(textvariable= self.alertText)
        self.alert.pack(pady = (5, 0))

        # Frame containing the button
        self.buttonFrame = appUI.ButtonFrame(self)
        self.buttonFrame.pack(pady= (10, 0))
        self.buttonFrame.grid_columnconfigure(0, weight = 1)
        self.buttonFrame.grid_rowconfigure(0, weight= 1)
        self.buttonFrame.button.configure(command= self.incrementScore)

        # Frame containing the number of trials left
        self.trial = appUI.TrialFrame(self, fg_color= "transparent", width= 40, height=20)
        self.trial.text.configure(textvariable = trials_text)
        self.trial.pack( pady= (5,0))

    # just to test what happens in the terself.MINal
    def getText(self):
        self.guess = self.UserText.get()
        try: 
            int(self.guess)
            print(self.toGuess)  
            print(self.guess)
            self.alertText.set("valid")
            self.UserText.delete(0, "end") 
        except ValueError:
            self.alertText.set("You must enter an integer")
            self.UserText.delete(0, "end") 
    
    # logic to implement later
    # def checkIntInput(self, func):
    #     pass

    
    def incrementScore(self):
        self.guess = self.UserText.get() # gets the value entered
        try:
            if int(self.guess) == self.toGuess:
             self.score += 1 
             self.toGuess = random.randint(self.MIN, self.MAX) # generate a new value if the user got the anser
            else:
                pass
            self.alertText.set("") # nothing went wrong, so alert text should stay empty
            self.UserText.delete(0, "end") # erases the texte entry
            self.score_text.set(f"Score: {self.score}")
            # ---- just to check what happens in the terself.MINal
            print(self.guess)
            print(self.toGuess)  
        except ValueError:
                self.alertText.set("You must enter an integer")
                self.UserText.delete(0, "end") 

    

window = MainApp()

window.mainloop()