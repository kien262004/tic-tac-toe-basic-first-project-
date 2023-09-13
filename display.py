import customtkinter as ctk
from machinePlay import *

class display(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        self.size_board = 3
        self.game = board()
        self.geometry("400x600")
        self.title("games")
        self.main_display()
        self.mainloop()
        
    #----------------------------------------------------------------
    # display functions   
    def main_display(self):
        self.states = "other"
        self.main_screen = ctk.CTkFrame(self)
        self.main_widget = ctk.CTkFrame(self.main_screen)
        ctk.CTkLabel(self.main_screen,text="Tic Toa Toe",font=("Terminal",32),text_color="white").pack(pady=100)
        ctk.CTkButton(self.main_widget,text="New Game",font=("Terminal",18),fg_color="white",hover_color="#C8C8C8",text_color="black",command=lambda: self.set_newgame(self.main_widget,self.main_screen)).pack(pady=20)
        ctk.CTkButton(self.main_widget,text="Option",font=("Terminal",18),fg_color="white",hover_color="#C8C8C8",text_color="black",command=self.set_option).pack(pady=20)
        ctk.CTkButton(self.main_widget,text="Quit",font=("Terminal",18),fg_color="white",hover_color="#C8C8C8",text_color="black",command=self.set_quit).pack(pady=20)
        self.main_screen.pack(expand=True,fill="both")
        self.main_widget.pack()

    def option_display(self):
        self.option_screen = ctk.CTkFrame(self)
        self.option_widget = ctk.CTkFrame(self.option_screen)
        if self.states == "ingame mode":
            ctk.CTkButton(self.option_widget,text="Resume",font=("Terminal",18),fg_color="white",hover_color="#C8C8C8",text_color="black",command=self.resume_func).pack(pady=10)
            ctk.CTkButton(self.option_widget,text="Start new game",font=("Terminal",18),fg_color="white",hover_color="#C8C8C8",text_color="black",command=lambda: self.set_newgame(self.option_widget,self.option_screen)).pack(pady=10)
        ctk.CTkButton(self.option_widget,text="Resize game",font=("Terminal",18),fg_color="white",hover_color="#C8C8C8",text_color="black",command=self.resize_func).pack(pady=10)
        ctk.CTkButton(self.option_widget,text="Return",font=("Terminal",18),fg_color="white",hover_color="#C8C8C8",text_color="black",command=self.return_func).pack(pady=10)
        self.option_screen.pack(expand=True,fill="both")
        self.option_widget.pack(pady=20)
    
    def ingame_display(self):
        self.button_arr = dict()
        self.ingame_screen = ctk.CTkFrame(self)
        self.play_area = ctk.CTkFrame(self.ingame_screen)
        ctk.CTkLabel(self.play_area,fg_color="white").place(relx=0,rely=0,relwidth=1,relheight=1)
        self.play_area.grid_rowconfigure(list(range(self.size_board)),weight=1,uniform="a")
        self.play_area.grid_columnconfigure(list(range(self.size_board)),weight=1,uniform="a")
        for i in range(self.size_board):
            for j in range(self.size_board):
                self.create_button([i,j]).grid(row=i,column=j,sticky="news",padx=5,pady=5)
        self.play_area.place(relx=0,rely=0.02,relwidth=1,relheight=2/3)
        self.button_area = ctk.CTkFrame(self.ingame_screen)
        ctk.CTkButton(self.button_area,text="Option",font=("Terminal",18),fg_color="white",hover_color="#C8C8C8",text_color="black",command=self.set_option).pack(pady=20)
        ctk.CTkButton(self.button_area,text="Quit",font=("Terminal",18),fg_color="white",hover_color="#C8C8C8",text_color="black",command=self.set_quit).pack()
        self.button_area.place(relx=0,relwidth=1,rely=2/3+0.02,relheight=1/3-0.02)
        self.ingame_screen.pack(expand=True,fill="both")
        
    
    def endgame_display(self,case):
        self.endgame_screen = ctk.CTkFrame(self)
        self.endgame_widget = ctk.CTkFrame(self.endgame_screen)
        ctk.CTkLabel(self.endgame_widget,text=case,font=("Terminal",28),text_color="white").pack(pady=100)
        ctk.CTkButton(self.endgame_widget,text="Start new game",font=("Terminal",18),fg_color="white",hover_color="#C8C8C8",text_color="black",command=lambda: self.set_newgame(self.endgame_widget,self.endgame_screen)).pack(pady=10)
        ctk.CTkButton(self.endgame_widget,text="Quit",font=("Terminal",18),fg_color="white",hover_color="#C8C8C8",text_color="black",command=self.set_quit).pack(pady=10)
        self.endgame_widget.pack(expand=True,fill="both")
        self.endgame_screen.pack(expand=True,fill="both")
    #----------------------------------------------------------------
    # command functions
    # main functions
    def set_newgame(self,frame,father_frame):
        frame.destroy()
        frame = ctk.CTkFrame(father_frame)
        ctk.CTkButton(frame,text="1 Player",font=("Terminal",18),fg_color="white",hover_color="#C8C8C8",text_color="black",command=lambda: self.start_game(1)).pack(pady=20)
        ctk.CTkButton(frame,text="2 Player",font=("Terminal",18),fg_color="white",hover_color="#C8C8C8",text_color="black",command=lambda: self.start_game(2)).pack(pady=20)
        frame.pack()

    def set_option(self):
        if self.states == "ingame mode":
            self.ingame_screen.pack_forget()
        else:
            self.main_screen.pack_forget()
        self.option_display()
    
    def set_quit(self):
        self.quit()
        
    # subfunctions
    # option functions
    
    def resume_func(self):
        self.option_screen.destroy()
        self.ingame_screen.pack(expand=True,fill="both")
    def resize_func(self):
        self.option_widget.pack_forget()
        self.option_select = ctk.CTkFrame(self.option_screen)
        screens = ["300x450","400x600"]
        val_select = ctk.StringVar(value = f'{round(self.winfo_width()/1.25)}x{round(self.winfo_height()/1.25)}')
        ctk.CTkComboBox(self.option_select,values=screens,variable=val_select,font=("Terminal",18),fg_color="white",text_color="black",command=lambda x:self.geometry(val_select.get())).pack(pady=10)
        ctk.CTkButton(self.option_select,text="Confirm",font=("Terminal",18),fg_color="white",hover_color="#C8C8C8",text_color="black",command=self.confirm_func).pack(pady=10)
        self.option_select.pack()
        
    def return_func(self):
        self.option_screen.destroy()
        if self.states == "ingame mode":
            self.ingame_screen.pack(expand=True,fill="both")
        else:
            self.main_screen.pack(expand=True,fill="both")
            
    def confirm_func(self):
        self.option_select.destroy()
        self.option_widget.pack()
        
    # ingame functions
    def start_game(self,type):
        self.type = type # loại game cần thay
        self.turn = 9
        self.game.clear()
        if self.states == "ingame mode":
            self.ingame_screen.destroy()
            self.option_screen.destroy()
        elif self.states == "endgame mode":
            self.endgame_screen.destroy()
        else:
            self.main_screen.destroy()
        self.states = "ingame mode"
        self.ingame_display()
        
    def create_button(self,location):
        button = ctk.CTkButton(self.play_area,text=" ",fg_color="#333333",corner_radius=0,font=("Arial",50),text_color_disabled="white",hover=False,command=lambda: self.played_button(button,location))
        self.button_arr[f"{location[0]} {location[1]}"] = button
        return button
    
    def played_button(self,unit,location):
        self.game.play(move(location[0],location[1]))
        if self.turn%2 == 1:
            unit.configure(text="O",state="disabled")
        else:
            unit.configure(text="X",state="disabled")
        self.turn -= 1
        if self.game.done():
            self.prep_end()
        if self.type == 1 and self.turn%2 == 0 and self.turn !=0:
            look_ahead(self.game,self.turn,recommend)
            new_location = [recommend.row,recommend.col]
            self.played_button(self.button_arr[f"{new_location[0]} {new_location[1]}"],new_location)
            
    def prep_end(self):
        self.states = "endgame mode"
        self.ingame_screen.destroy()
        if self.game._the_winner() == 1:
            self.endgame_display("First player wins")
        elif self.game._the_winner() == 2:
            self.endgame_display("Second player wins")
        else:
            self.endgame_display("Draw")
