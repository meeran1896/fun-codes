#Getting wifi password
import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))
input("")

#Creating strong password
import random
print("".join([chr(i) for i in random.choices(range(33,126),k=15)]))

#Getting qr code decode
from qrtools import QR
my_QR = QR(filename = "home/user/Desktop/qr.png")
# decodes the QR code and returns True if successful
my_QR.decode()
# prints the data
print (my_QR.data)

#Stopwatch
#importing the required libraries
import tkinter as Tkinter
from datetime import datetime
counter = 66600
running = False
def counter_label(label):
    def count():
        if running:
            global counter
   
            # To manage the initial delay.
            if counter==66600:            
                display="Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display=string
   
            label['text']=display   # Or label.config(text=display)
   
            # label.after(arg1, arg2) delays by 
            # first argument given in milliseconds
            # and then calls the function given as second argument.
            # Generally like here we need to call the 
            # function in which it is present repeatedly.
            # Delays by 1000ms=1 seconds and call count again.
            label.after(1000, count) 
            counter += 1
   
    # Triggering the start of the counter.
    count()     
   
# start function of the stopwatch
def Start(label):
    global running
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
   
# Stop function of the stopwatch
def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
   
# Reset function of the stopwatch
def Reset(label):
    global counter
    counter=66600
   
    # If rest is pressed after pressing stop.
    if running==False:      
        reset['state']='disabled'
        label['text']='Welcome!'
   
    # If reset is pressed while the stopwatch is running.
    else:               
        label['text']='Starting...'
   
root = Tkinter.Tk()
root.title("Stopwatch")
   
# Fixing the window size.
root.minsize(width=250, height=70)
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6, command=lambda:Start(label))
stop = Tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label))
f.pack(anchor = 'center',pady=5)
start.pack(side="left")
stop.pack(side ="left")
reset.pack(side="left")
root.mainloop()

#Website blocker
# Run this script as root
  
import time
from datetime import datetime as dt
  
# change hosts path according to your OS
hosts_path = "/etc/hosts"
# localhost's IP
redirect = "127.0.0.1"
  
# websites That you want to block
website_list = 
["www.facebook.com","facebook.com",
      "dub119.mail.live.com","www.dub119.mail.live.com",
      "www.gmail.com","gmail.com"]
  
while True:
  
    # time of your work
    if dt(dt.now().year, dt.now().month, dt.now().day,8) 
    < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    # mapping hostnames to your localhost IP address
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
  
            # removing hostnmes from host file
            file.truncate()
  
        print("Fun hours...")
    time.sleep(5)
 
#Desktop notifier
import requests
import xml.etree.ElementTree as ET
  
# url of news rss feed
RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"    
  
def loadRSS():
    '''
    utility function to load RSS feed
    '''
    # create HTTP request response object
    resp = requests.get(RSS_FEED_URL)
  
    # return response content
    return resp.content
  
def parseXML(rss):
    '''
    utility function to parse XML format rss feed
    '''
    # create element tree root object
    root = ET.fromstring(rss)
  
    # create empty list for news items
    newsitems = []
  
    # iterate news items
    for item in root.findall('./channel/item'):
        news = {}
  
        # iterate child elements of item
        for child in item:
  
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
        newsitems.append(news)
  
    # return news items list
    return newsitems
  
def topStories():
    '''
    main function to generate and return news items
    '''
    # load rss feed
    rss = loadRSS()
  
    # parse XML
    newsitems = parseXML(rss)
    return newsitems

#Web scraping
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

