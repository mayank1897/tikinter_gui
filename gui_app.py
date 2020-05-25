import tkinter
import os
from csv import DictWriter
from tkinter import ttk
window=tkinter.Tk()
window.title("Excaliber")
ttk.Label(window,foreground="red",text="Enter your name :-").grid(row=0,column=0,sticky=tkinter.W)
ttk.Label(window,foreground="red",text="Enter your age :-").grid(row=1,column=0,sticky=tkinter.W)
ttk.Label(window,foreground="red",text="Enter your Email :-").grid(row=2,column=0,sticky=tkinter.W)
ttk.Label(window,foreground="green",background="white",text="Gender :-").grid(row=3,column=0,sticky=tkinter.W)

name=tkinter.StringVar()
name_entry=ttk.Entry(window,width=30,textvariable=name)
name_entry.grid(row=0,column=1)


age=tkinter.StringVar()
age_entry=ttk.Entry(window,width=30,textvariable=age)
age_entry.grid(row=1,column=1)

email=tkinter.StringVar()
email_entry=ttk.Entry(window,width=30,textvariable=email)
email_entry.grid(row=2,column=1)

gender=tkinter.StringVar()
new_combobox=ttk.Combobox(window,width=10,state="readonly",textvariable=gender)
new_combobox.grid(row=3,column=1)
new_combobox["values"]=("Male","Female","Both")
new_combobox.current(0)


user_type=tkinter.StringVar()
ttk.Radiobutton(window,text="Student",value="Student",variable=user_type).grid(row=4,column=0)
ttk.Radiobutton(window,text="Teacher",value="Teacher",variable=user_type).grid(row=4,column=1)


check_box=tkinter.IntVar()
ttk.Checkbutton(window,text="Check for latest updates",variable=check_box).grid(row=5,column=0)


def function_call():
    names=name.get()
    age_get=age.get()
    emails=email.get()
    gender_get=gender.get()
    usertype_get=user_type.get()
    check_box_get=check_box.get()
    if (check_box_get==0):
        ttk.Label(window,foreground="blue",text="Click the check box for latest updates").grid(row=7,column=0)
    else:
        ttk.Label(window,background="#AEB0A3",text=f"congrats!!You've successfully checked in\nYour name is := {names}\nYour age is := {age_get}\nYour email is := {emails}\nYou're {gender_get}\nYou're {usertype_get}").grid(row=7,column=0)
    with open("database_excaliber.csv","a",newline="") as new_file:
        d=DictWriter(new_file,fieldnames=["Name","Age","Email","Gender","User_Type"])
        if (os.stat("database_excaliber.csv").st_size==0):
            d.writeheader()
        d.writerow({"Name":names,"Age":age_get,"Email":emails,"Gender":gender_get,"User_Type":usertype_get})    

    name_entry.delete(0,tkinter.END)
    age_entry.delete(0,tkinter.END)
    email_entry.delete(0,tkinter.END)


ttk.Button(window,text="Submit",command=function_call).grid(row=6,column=1)













window.mainloop()
