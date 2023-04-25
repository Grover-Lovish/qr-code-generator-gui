import os
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle
import qrcode
from tkinter import messagebox
from PIL import Image

def generate():
    global url
    url = url_input.get()
    if len(url) == 0:
        messagebox.showerror("Error","Please enter url, You cant leave the input empty")
        
    else:
        qr = qrcode.make(url)
        qr.save("testo.png")
        image = Image.open("testo.png")
        resize =  image.resize((round(image.size[0]*0.3), round(image.size[1]*0.3)))
        resize.save("testo.png")
        display.config(borderwidth=2,relief="solid")
        img.config(file = "testo.png" )

def save():
    name = str(file_name.get())
    if len(name) == 0:
        messagebox.showerror("Error","You cant save file before giving it any name.")
    elif (name+".png") == "testo.png":
        messagebox.showwarning("Warning","You cant save file with this name ,try another name")
        file_name.delete(0,END)
    else:
        list_cwd = os.listdir()
        if (name+".png") in list_cwd:
            ans = messagebox.askyesno("Existing File","the name of file you are entering is already existing. Do you want to replace it ?")
            if ans == True:
                qr = qrcode.make(url)
                qr.save(name+".png")
                file_name.delete(0,END)
                messagebox.showinfo("File Saved","Your file is saved successfully")
            else:
                file_name.delete(0,END)
                messagebox.showinfo("info","Please use another name your file is not saved for now")
        else:
            qr = qrcode.make(url)
            qr.save(name+".png")
            file_name.delete(0,END)
            messagebox.showinfo("File Saved","Your file is saved successfully")

root = Tk()
root.geometry("700x400")
root.maxsize("800","560")
root.minsize("700","400")
style = ThemedStyle(root)
style.set_theme("yaru")

main_frame = ttk.Frame(root)
main_frame.pack(fill="both",expand=True)

heading_frame = ttk.Frame(main_frame,padding=20)
heading_frame.pack()
heading_label = ttk.Label(heading_frame,text = "QR CODE GENERATOR",font=("verdana",33,"bold"))
heading_label.pack()

input_frame = ttk.Frame(main_frame,padding=30)
input_frame.pack(fill="both")
input_frame.columnconfigure([0,2],weight=1)
input_frame.columnconfigure(1,weight=3)

url_label = ttk.Label(input_frame,text="enter URL here = ")
url_label.grid(row = 0,column = 0)
url_input = Entry(input_frame)
url_input.grid(row = 0,column=1,ipadx=100)
generate_btn = ttk.Button(input_frame,text = "GENERATE",command= generate)
generate_btn.grid(row=0,column=2)

display_frame = ttk.Frame(main_frame)
display_frame.pack(expand = 0,fill = "both")
img = PhotoImage()
display = Label(display_frame,image=img)
display.pack(anchor="center")

saving_frame = ttk.Frame(main_frame)
saving_frame.pack(expand=0,side="bottom",anchor="se",padx=50,pady=20)
saving_label = ttk.Label(saving_frame,text="Save as : ")
saving_label.grid(row = 0,column=0)
file_name = ttk.Entry(saving_frame)
file_name.grid(row = 0,column=1,padx=10)
save_btn = ttk.Button(saving_frame,text = "SAVE",command=save)
save_btn.grid(row=0,column=2)

root.mainloop()