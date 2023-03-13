#display button with list of ulr in tkinter?
from io import BytesIO
from tkinter import *
from tkinter import Tk, Button
from urllib.request import urlopen
import webbrowser
from functools import partial
from PIL import ImageTk, Image
from tkinter import *
from tkinter import Tk, Button
import webbrowser
from urllib.request import urlopen 
from io import BytesIO
from functools import partial
from io import BytesIO
from urllib.request import urlopen
from PIL import Image, ImageTk

#List Of Links for tools
link_list = ['https://10.98.35.86/maximo/ui/login',
             'https://10.98.36.144:16311/ibm/console/logon.jsp', 
             'https://10.98.35.70/Views/Login/Login.aspx?rd=eyJPcmlnaW5VcmwiOiIvZGVmYXVsdC5hc3B4P3BpZD01NDYyYTAwOC0xODY4LTQyN2EtOGQxNC0xYzA5MGRlZDc5ZTcifQ%3d%3d', 
             'https://10.235.1.147', 
             'https://213.158.183.87:16311/ibm/console/logon.jsp', 
             'https://10.98.126.60:9003/msanpowerloss', 
             'https://10.98.126.69:5601/']

root = Tk()

#Title Of UI
root.title("MCC Web Launcher")
root.geometry("300x400")
root.configure(background='grey')

i=0

#load image from internet
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/We_logo.svg/800px-We_logo.svg.png"
u = urlopen(url)
raw_data = u.read()
u.close()
im = Image.open(BytesIO(raw_data))
resized=im.resize((100, 100), Image.ANTIALIAS)
image = ImageTk.PhotoImage(resized)


#Icon WE with the header
headerButton=Button(root, text="MCC Web Launcher", 
                    image=image, compound=TOP, font=10, 
                    fg='black', bg='grey', cursor='heart', 
                    borderwidth=0).pack(side=TOP)


#Footer Signature 
FooterButton=Button(root, text="Developed By Eng Mahmoud & Belal", bg='grey', borderwidth=0, font=('Script MT Bold', '13')).pack(side=BOTTOM)

#list of tools names
names_list=["ICD", 
            "Netcool", 
            "VC4", 
            "AMS", 
            "Proviso", 
            "Weconfig", 
            "Elastic search"]

#Button for every tool
for index, link, in enumerate(link_list):
    Button(root, text=f'{names_list[i]}', 
    command=partial(webbrowser.open, link), 
    width=10, 
    activebackground='purple').pack(side=TOP, pady=4)
    i+=1

root.mainloop()
