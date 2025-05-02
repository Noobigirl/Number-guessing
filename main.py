import random
import customtkinter as ctk 
import appUI
"""
features to add:
- restricting the user to input 2 char long number ❌
- displaying the placeholder text even after deletion ❌
- decrement the number of self.trials left after each unsuccessfull trial ✅
- increment the score for successfull guesses ✅
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
        self.trials = 3 # 3 trials per game

        # ---- Variable text ----
        instruction = ctk.StringVar(value= f"Guess a number between \n {self.MIN} and {self.MAX}") 
        self.score_text = ctk.StringVar(value= f" Score: {self.score}")
        self.trials_text = ctk.StringVar(value= f"Number of trials left: {self.trials}")
        self.alertText = ctk.StringVar()
        
        # ---- Frame containing the text----
        self.textFrame = appUI.NumberGuessingFrame(self, fg_color= "#5f5f5f", corner_radius= 7)
        # instructions giving the range within which the number lies and the score
        self.textFrame.scoreText.configure(textvariable = self.score_text)
        self.textFrame.mainText.configure(textvariable = instruction) 
        self.textFrame.grid_columnconfigure(0, weight= 1)
        self.textFrame.pack(fill= "both")

        # ---- User entry frame ----
        self.UserText = appUI.UserEntry(self)
        self.UserText.pack(pady= (5, 0))

        #-----  Frame with Alert text ----
        self.alert = appUI.AlertFrame(self, fg_color= "transparent")
        self.alert.alertText.configure(textvariable= self.alertText)
        self.alert.pack(pady = (5, 0))

        # ---- Frame containing the button
        self.buttonFrame = appUI.ButtonFrame(self)
        self.buttonFrame.set_command(self.getText)
        self.buttonFrame.pack(pady= (10, 0))
       
        # Frame containing the number of trials left
        self.trial = appUI.TrialFrame(self, fg_color= "transparent", width= 40, height=20)
        self.trial.text.configure(textvariable = self.trials_text)
        self.trial.pack( pady= (5,0))

    def getText(self):
        """
        function that gets the user entry text, validates it
        and call the incrementScore() function
        """
        self.guess = self.UserText.get()
        try: 
            int(self.guess)
            self.incrementScore()
            # --- just to see what happens in he terminal
            print(self.toGuess)  
            print(self.guess)
            self.UserText.delete(0, "end") # eraing the entry 
        except ValueError:
            self.alertText.set("You must enter an integer")
            self.UserText.delete(0, "end") 
    
    def incrementScore(self):
        """
        function that increment the score and
        updates the alert text and number to guess
        -> None
        """
        if int(self.guess) == self.toGuess:
            self.score += 1 
            self.toGuess = random.randint(self.MIN, self.MAX) # generate a new value if the user got the anser
            # future feature: increase the range of value each time the user gets a correct answer
            self.score_text.set(f"Score: {self.score}") # displays new score
        else:
            self.alertText.set("incorrect") # notifies the user that their anser is incorrect
            self.decrement_trials() # decrements the nubmer of trials left
            
    def decrement_trials(self):
        """
        function that decrements the number of trials left 
        and updates the trial text
        -> None
        """
        self.trials -=1
        self.trials_text.set(f"Number of trials left: {self.trials}")
        # futur feature : end the game when the number of trials is 0

    
if __name__ == "__main__":
    window = MainApp()

    window.mainloop()