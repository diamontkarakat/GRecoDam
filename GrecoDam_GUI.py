import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from random import   seed
from random import randrange
from random import randint
from _datetime import datetime
from tkinter import *

def objective_function(Vin,x1,L,A,B,n) :
    Vcur = Vin-x1
    dh = np.array((3 * Vcur) / (L * (A + B)))
    E = (1000 * 9.81 * n * (x1 / 86400) * dh) / 1000000
    return sum(E)
def on_click1():
    root.filename = filedialog.askopenfilename()
    return root.filename




def on_click():
    # _____________________________________________________
    print(root.filename)
    Qin = np.loadtxt(root.filename, dtype=float)
    qirr = np.array([random.uniform(86400, 259200) for i in range(364)])
    vmax = float(entry1.get())
    v_initial = float(entry3.get())
    A = float(entry4.get())
    B = float(entry5.get())
    L = float(entry6.get())
    dh_initial = 3 * v_initial / (L * (A + B))
    Vin = np.cumsum(Qin) + v_initial - qirr
    n = 0.75
    vmin = float(entry2.get())
    # -----------------------------------------------------------------------------------------------------
    time = [x for x in range(364 + 1) if x > 0]
    seed(datetime.now())
    print(v_initial)
    # Harmony Search Algorith
    # Harmony Memory
    hms = int(entry7.get())
    hm = np.array([])
    for i in range(hms):
        hm = np.append(hm, np.array([random.uniform(10000.00, 600000.00) for i in range(364)]))
    hm = np.reshape(hm, (364, hms))
    row = []
    for i in range(hms):
        row.append(objective_function(Vin, hm[:, i], L, A, B, n))
    hm = np.vstack([hm, row])
    # sorting harmony memory
    hmsort = hm[:, hm[-1, :].argsort()]
    # New Harmony
    hmcr = float(entry8.get())
    par = float(entry9.get())
    # ----------------------------------------------------------------------------------
    for k in range(10):
        NewHarmony = np.array([])
        if random.random() < hmcr:

            for i in range(0, 364):
                a = randint(0, hms - 1)
                NewHarmony = np.append(NewHarmony, hm[i, a])

            if random.random() < par:
                NewHarmony = NewHarmony + random.uniform(-100000.00, 100000.000)

        else:
            NewHarmony = np.array([randrange(1, 500000, 1) for i in range(364)])
        NewHarmony2 = np.append(NewHarmony, (objective_function(Vin, NewHarmony, L, A, B, n)))
        if objective_function(Vin, NewHarmony, L, A, B, n) > hmsort[364, 0]:
            hmsort[:, 0] = NewHarmony2
        # sort again
        hmsort = hmsort[:, hmsort[-1, :].argsort()]
        print(k)
    # print(hmsort)
    vfinal = Vin - hmsort[0:364, -1]
    print(vfinal.size)
    print(vfinal.shape)
    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.subplots_adjust(hspace=0.5)
    ax1.plot(time, Qin, linewidth=1.0, label="Input")
    ax2.plot(time, hmsort[0:364, -1], linewidth=1.0, label="Hydropower")
    ax2.plot(time, qirr, linewidth=1.0, label="Irrigation")
    ax1.set(title=r'Reservoir incoming flow per day',
            xlabel='time in days', ylabel=r'Flow $(\frac{m^3}{day})$')
    ax2.set(title=r'Reservoir outcoming flow per day',
            xlabel='time in days', ylabel=r'Flow $(\frac{m^3}{day})$')
    ax2.set_xlabel('time in days')
    ax2.plot(time, vfinal, linewidth=1.0, label="current reservoir volume")
    ax2.axhline(y=vmin, linewidth=1, color='r', label="Minimum water level")
    leg = plt.legend(loc='upper center')
    ax1.set_xlim(0, 365)
    ax2.set_xlim(0, 365)
    ax1.grid(True)
    ax2.grid(True)

    plt.show()


root = Tk()
root.title("GREcoDAM")
root.iconbitmap("./logo.ico")
root.geometry('800x600')
frame1 =  LabelFrame(root, text="Insert Dam Parameters")
frame1.grid(row=0,column=0,padx=10,pady=10)
label1 = Label(frame1,text="Maximum Volume (m^3)")
entry1 =  Entry(frame1)
entry1.insert(0, "1500000")
label2 = Label(frame1,text="Minimum Volume (m^3)")
entry2 =  Entry(frame1)
entry2.insert(0, "200000")
label3 = Label(frame1,text="Initial Volume (m^3)")
entry3 =  Entry(frame1)
entry3.insert(0, "1125000")
label1.pack()
entry1 .pack()
label2.pack()
entry2 .pack()
label3.pack()
entry3 .pack()
frame2 =  LabelFrame(root, text="Dam Geometry")
frame2.grid(row=20,column=0,padx=10,pady=10)
label4 = Label(frame2,text="A(m)")
entry4 =  Entry(frame2)
entry4.insert(0, "50")
label4.pack()
entry4.pack()
label5 = Label(frame2,text="B(m)")
entry5 =  Entry(frame2)
entry5.insert(0, "100")
label5.pack()
entry5.pack()
label6 = Label(frame2,text="L(m)")
entry6 =  Entry(frame2)
entry6.insert(0, "1000")
label6.pack()
entry6.pack()
frame3 =  LabelFrame(root, text="Harmony Search Algorith")
frame3.grid(row=40,column=0,padx=10,pady=10)
label7 = Label(frame3,text="HMS")
entry7 = Entry(frame3)
entry7.insert(0, "10")
label8 = Label(frame3,text="HMCR")
entry8 = Entry(frame3)
entry8.insert(0, "0.7")
label9 = Label(frame3,text="PAR")
entry9 = Entry(frame3)
entry9.insert(0, "0.5")
label7.pack()
entry7.pack()
label8.pack()
entry8.pack()
label9.pack()
entry9.pack()
btn1=Button(root,text="Solve",command=on_click)
btn1.grid(row=80,column=0)
btn2=Button(root,text="CSV Data",command=on_click1)
btn2.grid(row=60,column=0)


root.mainloop()
