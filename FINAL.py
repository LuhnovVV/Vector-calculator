#from tkinter import *
from tkinter.ttk import Combobox  
import comp_func as cf
import numpy as np
from tkinter.ttk import Radiobutton 
import tkinter.font as font


def get2D(x1,y1,x2,y2):
    lst1 = []
    lst1.append(int(x1))
    lst1.append(int(y1))
    a = np.array(lst1)
    
    lst2 = []
    lst2.append(int(x2))
    lst2.append(int(y2))
    b = np.array(lst2)
    return a,b
    
def get3D(x1,y1,z1,x2,y2,z2):
    lst1 = []
    lst1.append(int(x1))
    lst1.append(int(y1))
    lst1.append(int(z1))
    a = np.array(lst1)
    
    lst2 = []
    lst2.append(int(x2))
    lst2.append(int(y2))
    lst2.append(int(z2))
    b = np.array(lst2)
    return a,b


def clicked():
    Z = combo.get() #номер задачи
    D = selected.get()
    x1 = clicks2.get()
    y1 = clicks3.get()
    x2 = clicks5.get()
    y2 = clicks6.get()


    if D == 2:
        a = get2D(x1,y1,x2,y2)[0]
        b = get2D(x1,y1,x2,y2)[1]  
    else:
        z1 = clicks4.get()
        z2 = clicks7.get()
        a = get3D(x1,y1,z1,x2,y2,z2)[0]
        b = get3D(x1,y1,z1,x2,y2,z2)[1]
        
        
    # выбор типа умножения    
    if combo['values'].index(Z) == 0:
        valks = cf.scal(a,b)
        print(valks)
        clickss = IntVar()
        clickss.set(valks) 
        lb = Label(window, textvariable=clickss, font = 100)   
        lb.place(x=120, y=280) 
        
       
    elif combo['values'].index(Z) == 1:
        if len(a) == 2:
            print("Для векторов размерности 2, векторное произведение дает только площадь параллелограмма построенного на этих векторах, векторное умножение в общем смысле не определенно") 
            valkc = cf.cross(a,b)
            print(valkc)
        else:
            valkc = cf.cross(a,b)[0],cf.cross(a,b)[1],cf.cross(a,b)[2]
            print(cf.cross(a,b)[0],cf.cross(a,b)[1],cf.cross(a,b)[2])
        clicksc = IntVar()
        clicksc.set(valkc) 
        lb = Label(window, textvariable=clicksc, font = 100)   
        lb.place(x=88, y=310) 
    
    elif combo['values'].index(Z) == 2:
        valk = cf.tensor(a,b)
        for k in range(0, len(valk)):
            for n in range(0, len(valk[k])):
                print(valk[k][n], end=' ')
            print()
        valk1 = cf.tensor(a,b)[0][0],cf.tensor(a,b)[0][1],cf.tensor(a,b)[0][2]
        valk2 = cf.tensor(a,b)[1][0],cf.tensor(a,b)[1][1],cf.tensor(a,b)[1][2]
        valk3 = cf.tensor(a,b)[2][0],cf.tensor(a,b)[2][1],cf.tensor(a,b)[2][2]
        clicksv1 = IntVar() 
        clicksv1.set(valk1) 
        clicksv2 = IntVar() 
        clicksv2.set(valk2) 
        clicksv3 = IntVar() 
        clicksv3.set(valk3) 
        lbv1 = Label(window, textvariable=clicksv1, font = 100)   
        lbv1.place(x=88, y=350) 
        lbv2 = Label(window, textvariable=clicksv2, font = 100)   
        lbv2.place(x=88, y=370) 
        lbv3 = Label(window, textvariable=clicksv3, font = 100)   
        lbv3.place(x=88, y=390) 
        
    elif combo['values'].index(Z) == 3:
        valkm1 = round(np.linalg.norm(a),3)
        valkm2 = round(np.linalg.norm(b),3)
        clicksm1 = IntVar()
        clicksm2 = IntVar()
        clicksm1.set(valkm1) 
        clicksm2.set(valkm2) 
        lbm1 = Label(window, textvariable=clicksm1, font = 100)   
        lbm2 = Label(window, textvariable=clicksm2, font = 100)  
        lbm1.place(x=70, y=430)
        lbm2.place(x=140, y=430)
        print(valkm1,valkm2)
    
    elif combo['values'].index(Z) == 4:
        valkp = a + b
        clicksp = IntVar()
        clicksp.set(valkp) 
        lbp = Label(window, textvariable=clicksp, font = 100)   
        lbp.place(x=88, y=470)
        print(valkp)
    
    else:
        valkh = a - b
        clicksh = IntVar()
        clicksh.set(valkh) 
        lbm = Label(window, textvariable=clicksh, font = 100)   
        lbm.place(x=88, y=510)
        print(valkh)
    
### создание окна
window = Tk() 
window.title("Калькулятор") 
#window.geometry('300x300') 
window.geometry('270x550') 


### выпадающее меню с выбором типа умножения
clicks1 = IntVar() 
combo = Combobox(window, textvariable=clicks1, width=25, font=(10))  
combo['values'] = ("Скалярное произведение",
                   "Векторное произведение", 
                   "Тензорное произведение",
                   "Модуль вектора",
                   "Сложение векторов",
                   "Вычитание векторов")  
combo.current(0) 
combo.place(x=10, y=140) 





### текстовое окно с заданием размерности
lblD = Label(window, text ="Размерность вектора:", font=(10))   
lblD.place(x=0, y=90)  
selected = IntVar()  
radD1 = Radiobutton(window, text='2D', value=2, variable=selected)  
radD2 = Radiobutton(window, text='3D', value=3, variable=selected)  
radD1.place(x=180, y=92) 
radD2.place(x=220, y=92) 


### кнопка триггера
btn = Button(window, text="Подсчет", command=clicked, height = 1, width = 10)
#btn['font'] = font.Font(size=10) # размер шрифта
btn['font']=font.Font(weight="bold")
btn.place(x=80, y=200) 
clicks = IntVar()




### задаем координаты векторов

# координаты первого вектора
lbl2 = Label(window, text ="i1 =", font=(100))   
lbl2.place(x=0, y=0)   
clicks2 = IntVar() 
txt2 = Entry(window,width=5, textvariable=clicks2, font=(100)) 
txt2.place(x=50, y=2) 

lbl3 = Label(window, text ="j1 =", font=(100))   
lbl3.place(x=0, y=20)    
clicks3 = IntVar() 
txt3 = Entry(window,width=5, textvariable=clicks3, font=(100)) 
txt3.place(x=50, y=22)  

lbl4 = Label(window, text ="k1 =", font=(100))   
lbl4.place(x=0, y=40)
clicks4 = IntVar() 
txt4 = Entry(window,width=5, textvariable=clicks4, font=(100)) 
txt4.place(x=50, y=42)  

# координаты второго вектора
lbl5 = Label(window, text ="i2 =", font=(100))   
lbl5.place(x=150, y=0)  
clicks5 = IntVar() 
txt5 = Entry(window,width=5, textvariable=clicks5, font=(100)) 
txt5.place(x=200, y=2) 

lbl6 = Label(window, text ="j2 =", font=(100))   
lbl6.place(x=150, y=20)
clicks6 = IntVar() 
txt6 = Entry(window,width=5, textvariable=clicks6, font=(100)) 
txt6.place(x=200, y=22) 

lbl7 = Label(window, text ="k2 =", font=(100))   
lbl7.place(x=150, y=40)
clicks7 = IntVar() 
txt7 = Entry(window,width=5, textvariable=clicks7, font=(100)) 
txt7.place(x=200, y=42) 

window.mainloop() 
