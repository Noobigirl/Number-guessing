import customtkinter as ctk

DEFAULT_FONT= "Poppins"
DEFAULT_COLOR= "#fff"

#---- helper functions
def create_button(parent, text: str, font, **attributes):
    """
    This function creates a button 
    """
    return ctk.CTkButton(master= parent, text= text, font= font, **attributes)

def create_label(parent, font,  textvariable= None ,**attributes):
    """
    this function creates a label
    """
    return ctk.CTkLabel(master= parent, font= font, textvariable= textvariable, **attributes)

def set_font(size, family= DEFAULT_FONT):
    """
    Function used to set the font family and size
    """
    return ctk.CTkFont(family= family, size= size)


# ---- frame classes
class NumberGuessingFrame(ctk.CTkFrame):
    """
    Class containing the score and the range of number to guess
    methods: 
        create_widget
        layout_widget
    """
    def __init__(self, root, **kwargs): 
        super().__init__( root, **kwargs) 
        self.font= set_font(20) # setting the font of the text
        
        # I created thes methods in case I later want to and and place
        # widgets in this frame from the main app
        self.create_widget()
        self.layout_widget()

    def create_widget(self):
        """
        Initializes the widget inside the NumberGuesingFrame
        """
        self.scoreText = create_label(self, self.font, text_color= DEFAULT_COLOR)

        self.mainText= create_label(self, self.font, text_color= DEFAULT_COLOR)
        # Stringvar will be used to dynamically set the text later in the main app
        self.mainText.configure(height= 150, anchor="center", justify= "center")

    def layout_widget(self):
        """
        Geometry manager : grid
        """
        self.scoreText.grid(row =0, column= 0, padx= 10, sticky ="w") # label displaying  the score
        self.mainText.grid(row= 1, column= 0, padx=20, pady= 15, sticky= 'ew') # label displaying the instruction


class UserEntry(ctk.CTkEntry):
    """
    Frame containing the entry widget
    methods: 
        create_widget
        layout_widget
    width = 175, height = 75, placeholder_text = "00"
    """
    def __init__(self, root,**kwargs):
        self.font= set_font(100)
        super().__init__(master= root, 
        width= 175,
        height= 75, 
        placeholder_text= "00",
        justify= "center", # default text
        font= self.font,
        fg_color= "transparent",
        border_width= 0,  # completely gets rid of the border
        **kwargs)



#---- display alerts
class AlertFrame(ctk.CTkFrame):
    """
    Class containing the  alert text
    methods: 
       create_widget
       layout_widget
    """
    def __init__(self, root, **kwargs):
        super().__init__(master= root, **kwargs)
        self.font = set_font(13)
        self.create_widget()
        self.layout_widget()

    def create_widget(self):
         """
         Initializes the widget inside the AlertFrame
         """
         self.alertText = create_label(self, self.font) # textvariable set in the main app
    
    def layout_widget(self):
         """
         Geometry manager : pack
         """
         self.alertText.pack()


#---- validation button ----
class ButtonFrame(ctk.CTkFrame):
    """
    Class containing the validation button
    methods: 
        create_widget
        layout_widget
        set_command
    """
    def __init__(self, root, fg_color= "transparent",corner_radius= 0, **kwargs):
        super().__init__(root, **kwargs)
        self.font = set_font(20) # setting the font of the text
        self.create_widget()
        self.layout_widget()

    def create_widget(self):
        # button itself
        self.button = create_button(self, "Submit", self.font, fg_color= "blue", height= 75)
       
    def layout_widget(self):
         self.button.pack()
    
    def set_command(self, callback):
        self.button.configure(command= callback)


#----- Number of trials left ------
class TrialFrame(ctk.CTkFrame):
    """
    Class containing the number of trial left text
    methods: 
        create_widget
        layout_widget
    """
    def __init__(self, root,**kwargs):
        super().__init__(master= root,**kwargs)
        self.font = set_font(15)# setting the font of the text
        self.create_widget()
        self.layout_widget()
        
    def create_widget(self):
        # Label containing the number of trials left
        self.text = ctk.CTkLabel(self, font= self.font)

    def layout_widget(self):
        self.text.pack()


class GameOver(ctk.CTkFrame):
    """
    Class displaying the game over screen (frame)
    methods:
        create_widget
        layout_widget
        set_command
    """
    def __init__(self, root,*args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.font = set_font(30)
        self.create_widget()
        self.layout_widget()

        
    
    def create_widget(self):
        self.text = create_label(self, self.font, text="GAME OVER") 
        # game over button, command will be set by restart in the main program
        self.button = create_button(self, "Try Again", self.font)
    
    def layout_widget(self):
        self.text.pack()
        self.button.pack()

    def set_command(self, callback):
        self.button.configure(command= callback)