import random
import customtkinter as ctk 
import appUI
"""
features to add:
- restricting the user to input 2 char long number ✅
- displaying the placeholder text even after deletion ❌
- decrement the number of self.trials left after each unsuccessfull trial ✅
- increment the score for successfull guesses ✅
- display the score ✅
- force the user to only enter integers ✅
- give hints to the user on how close they are to the true number ✅
- prevent the trial number from going below 0 ✅
- end the game when the number of tials reaches 0 ❌
- increasing the difficulty and number of trials when the use passes a level ❌
- notify the user that the new value to guess is different when their get a correct answer ✅
- make a more appealing UI ❌
"""


#------ main app -------
class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Numgy")
        self.geometry("400x550+700+200") # window size and position
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill= "both")
        # -- validatecommand callback checking if the user enter at most a 2 digit number
        validation = self.register(self.input_validation) 

        # ----  initialisation of the game
        self.MIN, self.MAX = 0, 10 # range of values to guess
        self.toGuess = random.randint(self.MIN, self.MAX) # generating the number to guess
        self.score = 0 # score initialized to 0
        self.trials = 3 # 3 trials per game


        # ---- Variable text ----
        instruction = ctk.StringVar(value=f"Guess a number between \n {self.MIN} and {self.MAX}") 
        self.score_text = ctk.StringVar(value= f" Score: {self.score}")
        self.trials_text = ctk.StringVar(value= f"Number of trials left: {self.trials}")
        self.alertText = ctk.StringVar() # will only be set if the user must be notified of something
        
        # ---- Frame containing the text----
        self.textFrame = appUI.NumberGuessingFrame(self.container, fg_color= "#5f5f5f", corner_radius= 0)
        self.textFrame.scoreText.configure(textvariable = self.score_text)
        self.textFrame.mainText.configure(textvariable = instruction) 
        self.textFrame.grid_columnconfigure(0, weight= 1)
        self.textFrame.pack(fill= "both")

        # ---- User entry frame ----
        # The input is checked after value is entered and the full input is passed to our callback for validation
        self.UserText = appUI.UserEntry(self.container, validate = "key", validatecommand = (validation, "%P"))
        self.UserText.pack(pady= (5, 0))

        #-----  Frame with Alert text ----
        self.alert = appUI.AlertFrame(self.container, fg_color= "transparent")
        self.alert.alertText.configure(textvariable= self.alertText)
        self.alert.pack(pady = (5, 0))

        # ---- Frame containing the button
        self.buttonFrame = appUI.ButtonFrame(self.container)
        self.buttonFrame.set_command(self.getText)
        self.buttonFrame.pack(pady= (10, 0))
       
        # Frame containing the number of trials left
        self.trial = appUI.TrialFrame(self.container, fg_color= "transparent", width= 40, height=20)
        self.trial.text.configure(textvariable = self.trials_text)
        self.trial.pack( pady= (5,0))


    
    def erase_txt(self):
        self.UserText.delete(0, "end") # erasing the entry 
        # self.UserText.configure(placeholder_text= "00")

    def getText(self):
        """
        function that gets the user entry text, checks if it is a digit
        and call the incrementScore() function
        -> None
        """

        self.guess = self.UserText.get()
        if self.guess.isdigit():
            self.guess = int(self.guess)
            self.incrementScore()
            # --- just to see what happens in he terminal
            print(self.toGuess)  
            print(self.guess)
        else: 
            self.alertText.set("You must enter an integer")
        self.erase_txt() # erase the text and reset the placeholder 

    def incrementScore(self):
        """
        function that increment the score and
        updates the alert text and number to guess
        -> None
        """
        if self.guess == self.toGuess:
            self.score += 1 
            self.toGuess = random.randint(self.MIN, self.MAX) # generate a new value if the user got the answer
            self.alertText.set("Correct!, guess a new number")

            # future feature: increase the range of value each time the user gets a correct answer
            self.score_text.set(f"Score: {self.score}") # displays new score
        else:
            self.hint() # notifies the user that their anser is incorrect
            self.decrement_trials() # decrements the nubmer of trials left
            
    def hint(self):
        """
        function that indicates how close the user is to the true value
        -> None
        """
        difference = self.toGuess - self.guess
        if difference < 0:
            self.alertText.set(f"Incorrect: the number is  smaller ")    
        else: 
            self.alertText.set(f"Incorrect: the number is  larger ")
            
    def decrement_trials(self):
        """
        function that decrements the number of trials left 
        and updates the trial text
        -> None
        """
        self.trials -= 1 if self.trials > 0 else 0
        self.trials_text.set(f"Number of trials left: {self.trials}")
        # ending the game
        if self.trials == 0:
            self.game_over()
    
    def input_validation(self, userInput):
        """
        function checking if the user input is less that or equal to 2 
        -> bool
        """
        return True if len(userInput) <= 2 else False
    
    def game_over(self):
        self.Game_over = appUI.GameOver(self)
        self.Game_over.pack()
        self.Game_over.tkraise()
        # self.buttonFrame[state] = "disabled" # make the button unclickable after losing


    
if __name__ == "__main__":
    window = MainApp()
    window.mainloop()