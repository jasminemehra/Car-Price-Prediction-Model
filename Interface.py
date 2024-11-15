#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ----------------------------------------------------------------
# -----------------------GUI OF CAR PREDICTION---------------------------------


# -------------------------Importing Required Moduels---------------------------------

import pandas as pd
import numpy as np
from tkinter import *
from tkinter import ttk
from joblib import load
from tkinter import messagebox

win = Tk()
# ------------------Creating Geometry,Title,Bg color---------------------------
win.geometry("1450x750")
win.title("WELCOME TO CAR SELLING PRICE PREDICTION!")
win.state('zoomed')
win.config(bg="black")

year = StringVar()
drivenkm = StringVar()
fue = StringVar()
fue.set("Petrol")
seller = StringVar()
seller.set("Individual")
trans = StringVar()
trans.set("Manual")
owner = StringVar()
owner.set("First Owner")
mileage = StringVar()
engine = StringVar()
power = StringVar()
seat = StringVar()
seat.set("5")


def func():
    # ------------Loading file /data------------------
    la = load("fuel.joblib")
    lb = load("seller_type.joblib")
    lt = load("transmission.joblib")
    lo = load("owner.joblib")
    sc = load("scaling.joblib")
    reg = load("regressor.joblib")

    # --------------------------------Making Dictonary-----------------------------
    try:
        dfn = pd.DataFrame({"Year": int(year.get()), "Driven_Kilometers": int(drivenkm.get()),
                            "Fuel_Type": [str(fue.get())],
                            "Seller_Type": [str(seller.get())],
                            "Transmission": [str(trans.get())], "Owners": [str(owner.get())],
                            "Mileage": [float(mileage.get())], "Engine": [int(engine.get())],
                            "Power": [float(power.get())], "Seat": [float(seat.get())]})

        dfn["Fuel_Type"] = la.transform(dfn["Fuel_Type"])
        dfn["Seller_Type"] = lb.transform(dfn["Seller_Type"])
        dfn["Transmission"] = lt.transform(dfn["Transmission"])
        dfn["Owners"] = lo.transform(dfn["Owners"])
        dfn = sc.transform(dfn)

        output_var = ("THE APPROXIMATED PRICE OF THIS CAR IS : ₹{} ".format(int(reg.predict(dfn))))
        output_screen_label.config(text=output_var, font=("Century", 20), fg="White", bg="black")

    except:
        messagebox.showerror('Empty Fields', 'All Fields Are Mandatory !', icon='warning')


output_screen_label = Label(win)
output_screen_label.place(x=280, y=580)


# -------------------------Creating Exit Button--------------------------------------
def ExitApplication():
    box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application ?', icon='warning')
    if box == 'yes':
        win.destroy()


exit_button = Button(win, text="EXIT", bd='7', bg="white", font=("Arial", 10), command=ExitApplication)
exit_button.place(x=1200, y=580)

# ------------------------Creating Heading---------------------------------------
Label(win, text="C A R    P R I C E    P R E D I C T I O N", fg="White", bg="black",
      font=("aesthetica", 40)).place(x=180, y=40)

# ----------------creating Entries and Lables for Data Input-------------------

Label(win, text="Model Year", font=("Disengaged", 25), fg="White", bg="black").place(x=100, y=170)
Entry(win, textvariable=year, width=40, bg="white").place(x=390, y=180, height=23)

Label(win, text="Driven KMs", font=("Disengaged", 25), fg="White", bg="black").place(x=100, y=250)
Entry(win, textvariable=drivenkm, width=40, bg="white").place(x=390, y=260, height=23)

Label(win, text="Engine (CC)", font=("Disengaged", 25), fg="White", bg="black").place(x=100, y=330)
Entry(win, textvariable=engine, width=40, bg="white").place(x=390, y=350, height=23)

Label(win, text="Max Power", font=("Disengaged", 25), fg="White", bg="black").place(x=100, y=410)
Label(win, text="(BHP)", font=("Disengaged", 13), fg="White", bg="black").place(x=270, y=425)
Entry(win, textvariable=power, width=40, bg="white").place(x=390, y=420, height=23)

Label(win, text="Mileage", font=("Disengaged", 20), fg="White", bg="black").place(x=100, y=490)
Label(win, text="(KmpL)(km/kg)", font=("arial", 13), fg="White", bg="black").place(x=210, y=500)
Entry(win, textvariable=mileage, width=40, bg="white").place(x=390, y=500, height=23)

Label(win, text="Fuel Type", font=("Disengaged", 25), fg="White", bg="black").place(x=770, y=170)
ttk.Combobox(win, textvariable=fue, values=["Diesel", "Petrol", "CNG", "LPG"]).place(x=1080, y=180,
                                                                                     height=23)

Label(win, text="Seller Type", font=("Disengaged", 25), fg="White", bg="black").place(x=770, y=250)
ttk.Combobox(win, textvariable=seller,
             values=["Individual", "Dealer", "Trustmark Dealer"]).place(x=1080, y=260, height="23")

Label(win, text="Owner", font=("Disengaged", 25), fg="White", bg="black").place(x=770, y=330)
ttk.Combobox(win, textvariable=owner,
             values=["First Owner", "Second Owner", "Third Owner",
                     "Fourth & Above Owner", "Test Drive Car"]).place(x=1080, y=340, height=23)

Label(win, text="Total Seats", font=("Disengaged", 20), fg="White", bg="black").place(x=770, y=410)
ttk.Combobox(win, textvariable=seat,
             values=["2", "4", "5", "6", "7", "8", '9', "10", "14"]).place(x=1080, y=420, height=23)

Label(win, text="Transmission type", font=("Disengaged", 20), bg="black", fg="white").place(x=770, y=490)
ttk.Combobox(win, textvariable=trans, values=["Manual", "Automatic"]).place(x=1080, y=500, height=23)

# ------------WATERMARK

Label(win, text="© CU", fg="White", bg="black").place(x=25, y=580)

# ---------------------------------Creating Submit Button-------------------------------------
submit = Button(win, text="SUBMIT", bd='7', fg="black", bg="white", command=func)
submit.place(x=1125, y=580)

win.mainloop()
