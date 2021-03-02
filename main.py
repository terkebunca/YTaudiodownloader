import tkinter
from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from tkinter import messagebox

Folder_Name = ""


def openlocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if len(Folder_Name) > 1:
        locationError.config(text=Folder_Name, fg="crimson")

    else:
        locationError.config(text="folder seç abim.", fg="red")


def getlink():
    url = linkgir.get()
    global yt
    if len(url) > 1:
        yt = YouTube(url)
        itagkutu.config(text=yt.streams.filter(only_audio=True))


def donmadanindir():
    getitag = itagEntry.get()
    ys = yt.streams.get_by_itag(getitag)
    ys.download(Folder_Name)

def clicked():
    messagebox.showinfo("yardımsal", "1)Üstte yer alan boşluğa YouTube linkini yazıver.\n2)save yöresi butonuyla "
                                     "indirmek istediğin yeri seç.\n3)"
                                     "Ekranda çıkan stream ID'lerinden(itag) istediğini seçip aşağıdaki boşluğa yaz"
                                     " ve indir butonuna tıkla!ihihi")


main = tkinter.Tk()
main.title("indie-bindie")
main.geometry("320x530")
main.configure(bg="gray10")
main.columnconfigure(0, weight=1)
main.resizable(False, False)

welcome = tkinter.Label(main, text="*isim*", bg="gray10", fg="white", font=("DOCALLISME ON STREET", 20))
welcome.place(anchor="center")
welcome.pack(pady=8)

linkgirVar = StringVar()
linkgir = Entry(main, textvariable="URL girizgahı", width=35, bg="black", fg="green2")
linkgir.place(anchor="center")
linkgir.pack(pady=15)

submitbutton = tkinter.Button(main, text="Submit", width=7, command=getlink)
submitbutton.pack(pady=5)

saveBaton = Button(main, width=11, text="save yöresi", command=openlocation)
saveBaton.pack(pady=5)

locationError = Label(main, text="", bg="gray10", fg="red", font=("jost", 10))
locationError.pack()

itagkutu = Label(main, bg="black", fg="red2", width=35, height=17, wraplengt=250)
itagkutu.pack(pady=5)

itagVar = IntVar()
itagEntry = tkinter.Entry(main, width=8, bg="black", fg="green2")
itagEntry.pack(padx=5)

buttondd = Button(main, text="Download", command=donmadanindir, bg="green3")
buttondd.pack(pady=10)

buttonhelp = Button(main, text="?", command=clicked, bg="red4", fg="white")
buttonhelp.place(x=300, y=500)

main.mainloop()
