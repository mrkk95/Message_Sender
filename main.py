import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo,showerror 

def send_sms(number,message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization' : '',//You can provide your own authorization key.
        'sender_id' : 'FSTSMS',
        'message' : message,
        'language' : 'english',
        'route' : 'p',
        'numbers' : number
    } 
    response = requests.get(url,params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')

def btn_click():
        num = textNumber.get()
        msg = textMsg.get("1.0",END)
        r = send_sms(num,msg)
        if(r==True):
            showinfo("Send Success" , "Successfully sent")
        else:
            showerror("Error" , "Something went wrong")


root = Tk()
root.title("Message Sender App(Mr.kk)")
root.geometry("400x550")
font = ("Helvetica",22,"bold")
textNumber = Entry(root,font = font,bg = "orange")
textNumber.pack(fill=X,pady=20)
textMsg = Text(root,bg = "green")
textMsg.pack(fill=X)
sendBtn = Button(root,text = "Send SMS",command = btn_click,bg = "yellow",activebackground ="black", activeforeground ="red")
sendBtn.pack()
root.mainloop()