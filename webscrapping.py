# import modules 
from tkinter import *
import sports 
from tkinter import messagebox  
  
def cricket_info(): 
      
    try: 
        match = sports.get_match(sports.CRICKET, e1.get() , e2.get()) 
        date.set(match.match_date) 
        time.set(match.match_time) 
        league.set(match.league) 
        team1.set(match.home_team) 
        team2.set(match.away_team) 
        team1_score.set(match.away_score) 
        team2_score.set(match.home_score) 
        link.set(match.match_link) 
    except: 
        messagebox.showerror("showerror", "No match found")  
  
  
  
  
# object of tkinter 
# and background set for light grey 
master = Tk() 
master.configure(bg='light grey') 
  
# Variable Classes in tkinter 
date = StringVar(); 
time = StringVar(); 
league = StringVar(); 
team1 = StringVar(); 
team2 = StringVar(); 
team1_score = StringVar(); 
team2_score = StringVar(); 
link = StringVar(); 
  
# Creating label for each information 
# name using widget Label  
Label(master, text="Team 1 :" , bg = "light grey").grid(row=0, sticky=W) 
Label(master, text="Team 2 :" , bg = "light grey").grid(row=1, sticky=W) 
Label(master, text="Date :" , bg = "light grey").grid(row=2, sticky=W) 
Label(master, text="Time :", bg = "light grey").grid(row=3, sticky=W) 
Label(master, text="League :", bg = "light grey").grid(row=4, sticky=W) 
Label(master, text="Team 1 :", bg = "light grey").grid(row=5, sticky=W) 
Label(master, text="Team 2 :", bg = "light grey").grid(row=6, sticky=W) 
Label(master, text="Team 1 score :", bg = "light grey").grid(row=7, sticky=W) 
Label(master, text="Team 2 score :", bg = "light grey").grid(row=8, sticky=W) 
Label(master, text="Link :", bg = "light grey").grid(row=9, sticky=W) 
  
  
# Creating lebel for class variable 
# name using widget Entry 
Label(master, text="", textvariable= date ,bg = "light grey").grid(row=2,column=1, sticky=W) 
Label(master, text="", textvariable= time ,bg = "light grey").grid(row=3,column=1, sticky=W) 
Label(master, text="", textvariable= league ,bg = "light grey").grid(row=4,column=1, sticky=W) 
Label(master, text="", textvariable= team1 ,bg = "light grey").grid(row=5,column=1, sticky=W) 
Label(master, text="", textvariable= team2 ,bg = "light grey").grid(row=6,column=1, sticky=W) 
Label(master, text="", textvariable= team1_score ,bg = "light grey").grid(row=7,column=1, sticky=W) 
Label(master, text="", textvariable= team2_score ,bg = "light grey").grid(row=8,column=1, sticky=W) 
Label(master, text="", textvariable= link ,bg = "light grey").grid(row=9,column=1, sticky=W) 
  
  
e1 = Entry(master) 
e1.grid(row=0, column=1) 
  
e2 = Entry(master) 
e2.grid(row=1, column=1) 
  
# creating a button using the widget   
# Button that will call the submit function  
b = Button(master, text="Show", command=cricket_info ) 
b.grid(row=0, column=2,columnspan=2, rowspan=2,padx=5, pady=5) 
  
mainloop()
