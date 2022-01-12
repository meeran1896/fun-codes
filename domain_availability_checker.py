# import modules 
from tkinter import *
import whois 
import sys 
  
  
# user define funtion 
# for get domain information 
def Domain_info(): 
    try: 
        domain = whois.whois(str(e1.get())) 
          
        if domain.domain_name == None: 
            sys.exit(1) 
  
    except: 
        result = "This domain is available"
      
    else: 
        result = "Oops! this domain already purchased"
    res.set(result) 
  
  
# object of tkinter 
# and background set for red 
master = Tk() 
master.configure(bg='white') 
  
# Variable Classes in tkinter 
res = StringVar() 
  
# Creating label for each information 
# name using widget Label 
Label(master, text="Website URL : ", bg="white").grid(row=0, sticky=W) 
Label(master, text="Result :", bg="white").grid(row=3, sticky=W) 
  
# Creating lebel for class variable 
# name using widget Entry 
Label(master, text="", textvariable=res, bg="white").grid( 
    row=3, column=1, sticky=W) 
  
e1 = Entry(master) 
e1.grid(row=0, column=1) 
  
# creating a button using the widget 
# Button that will call the submit function 
b = Button(master, text="Show", command=Domain_info, bg="red") 
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5,) 
  
mainloop()
