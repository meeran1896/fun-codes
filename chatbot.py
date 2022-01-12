from tkinter import *
root=Tk()
def send():
    send="you:"+a.get()
    text.insert(END,"\n"+send)
    if(a.get()=='hi'):
        text.insert(END,"\n" + "Bot:hello")
    elif(a.get()=='hello'):
        text.insert(END,"\n"+ "Bot:hi")
    elif(a.get()=='How are you?'):
        text.insert(END,"\n"+ "Bot:I am fine. How are you?")
    elif(a.get()=='I am fine'):
        text.insert(END,"\n"+ "Bot:Nice to hear that")
    else:
        text.insert(END,"\n"+ "Bot:I didn't get it ")
text=Text(root,bg='white')
text.grid(row=0,column=0,columnspan=2)
a=Entry(root,width=80)
send=Button(root,text='Send',bg='white',width=20,command=send).grid(row=1,column=1)
a.grid(row=1,column=0)
root.title('simple chatbot')
root.mainloop()
        
