from tkinter import *
from tkinter import filedialog as fd
import os
from tkinter import messagebox as mb
import webbrowser



root = Tk()
root.title("install appx for win10")
root.geometry("290x270")
root.resizable(width=False, height=False)



def open_and_install():
    op = fd.askopenfilename(title='Choose a file')
    print(op)
    ps = os.system("PowerShell add-appxpackage" + ' ' + op)
    mb.showerror("All done", op + "\n All done, program was installed in PC")



def callback(url):
    webbrowser.open_new(url)

b1 = Button(root, text= 'Install Appx', command=open_and_install)
b1.config(width=20, height=2, fg='blue')
b1.pack()

lab = Label(text ='Open Microsoft Windows Store,  \nCopy the link and paste it on the site: \n store.rg-adguard.net, \nselect the desired configuration'
                  '\n(x86 or x64, with the extension ".Appx"), '
                  '\nsave to PC \nfurther click in the program: "Install Appx",'
                  '\nselect the downloaded file '
                  '\nand wait for notification of successful installation. '
                  '\nLinks to sites:')
lab.place(x=2, y=60)

link2 = Label(root, text="Online Link Generator for Microsoft Store.", fg="blue", cursor="hand2")
link2.place(x=2, y= 220)
link2.bind("<Button-1>", lambda e: callback("https://store.rg-adguard.net/"))


link1 = Label(root, text="Microsoft Windows store", fg="blue", cursor="hand2")
link1.place(x=2, y= 240)
link1.bind("<Button-1>", lambda e: callback("https://www.microsoft.com/ru-ru/store/b/home"))



mainloop()
