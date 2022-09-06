import tkinter as tk
import datetime
import time
from tkinter import filedialog
import tkinter.messagebox as tm
import preprocess as pr
import DTALG as dt
import RFALG as rf
from tkinter import ttk
from_date = datetime.datetime.today()
currentDate = time.strftime("%d_%m_%y")
fontScale=1
fontColor=(0,0,0)
cond=0
bgcolor="#F08080"
fgcolor="black"
#setting the title
window = tk.Tk()
window.title("Visualization and Analysis of Crimes")
#setting window size
window.geometry('1280x720')
window.configure(background=bgcolor)
#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
crim=['BATTERY','OTHER OFFENSE','ROBBERY','NARCOTICS','CRIMINAL DAMAGE','WEAPONS VIOLATION','THEFT','BURGLARY','MOTOR VEHICLE THEFT','PUBLIC PEACE VIOLATION','ASSAULT','CRIMINAL TRESPASS','CRIM SEXUAL ASSAULT','INTERFERENCE WITH PUBLIC OFFICER','ARSON','DECEPTIVE PRACTICE','LIQUOR LAW VIOLATION','KIDNAPPING','SEX OFFENSE','OFFENSE INVOLVING CHILDREN','PROSTITUTION','GAMBLING','INTIMIDATION','STALKING','OBSCENITY','PUBLIC INDECENCY','HUMAN TRAFFICKING','CONCEALED CARRY LICENSE VIOLATION','OTHER NARCOTIC VIOLATION','HOMICIDE','NON-CRIMINAL']

message1 = tk.Label(window, text="Visualization and Analysis of Crimes" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline'))
message1.place(x=100, y=10)

lbl = tk.Label(window, text="SELECT DATASET",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl.place(x=10, y=200)
txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt.place(x=300, y=215)
lbl1 = tk.Label(window, text="LATITUDE",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl1.place(x=10, y=300)
lat = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
lat.place(x=300, y=315)
lbl1 = tk.Label(window, text="LONGITUDE",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl1.place(x=500, y=300)
lon = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
lon.place(x=750, y=315)
lbl1 = tk.Label(window, text="DATE",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl1.place(x=10, y=400)
txt2 = ttk.Combobox(window,width=10,font=('times', 15, ' bold '),values=["2015"])
txt2.place(x=300, y=415)
txt2.current(0)
txt3 = ttk.Combobox(window,width=10,font=('times', 15, ' bold '),values=["01","02","03","04","05","06","07","08","09","10","11","12"])
txt3.place(x=430, y=415)
txt3.current(0)
txt4 = ttk.Combobox(window,width=10,font=('times', 15, ' bold '),values=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"])
txt4.place(x=560, y=415)
txt4.current(0)
lbll1 = tk.Label(window, text="TIME",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbll1.place(x=700, y=400)
txt5 = ttk.Combobox(window,width=10,font=('times', 15, ' bold '),values=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"])
txt5.place(x=900, y=415)
txt5.current(0)

txt6 = ttk.Combobox(window,width=10,font=('times', 15, ' bold '),values=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"])
txt6.place(x=1030, y=415)
txt6.current(0)

lbl4 = tk.Label(window, text="NOTIFICATION  ",width=20  ,fg=fgcolor,bg=bgcolor  ,height=2 ,font=('times', 15, ' bold ')) 
lbl4.place(x=10, y=500)

message = tk.Label(window, text="" ,bg="white"  ,fg="black",width=30  ,height=2, activebackground = bgcolor ,font=('times', 15, ' bold ')) 
message.place(x=300, y=500)

#Clear Button
def clear():
	txt.delete(0, 'end') 
	res = ""
	message.configure(text= res)

#Browse Button
def browse():
	path=filedialog.askopenfilename()
	print(path)
	txt.insert('end',path)
	if path !="":
		print(path)
	else:
		tm.showinfo("Input error", "Select Dataset")

def preprocess():
	sym=txt.get()
	if sym != "" :
		#pr is reference to the preprocess module
		pr.process(sym)
		res = "Preprocess Finished Successfully"
		#writing text in notification box
		message.configure(text= res)
		#tm is the tkinter message box
		tm.showinfo("Input", "Preprocess Finished Successfully")
	else:
		tm.showinfo("Input error", "Select Dataset")

			
#Buttons		
		
clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor  ,width=20  ,height=2 ,activebackground = "#CD5C5C" ,font=('times', 15, ' bold '))
clearButton.place(x=760, y=600)

browse = tk.Button(window, text="Browse",command=browse ,fg=fgcolor  ,bg=bgcolor  ,width=15  ,height=1, activebackground = "#CD5C5C" ,font=('times', 15, ' bold '))
browse.place(x=530, y=205)

pre = tk.Button(window, text="Visualize",command=preprocess, fg=fgcolor  ,bg=bgcolor  ,width=18  ,height=2, activebackground = "#CD5C5C" ,font=('times', 15, ' bold '))
pre.place(x=10, y=600)


quitWindow = tk.Button(window, text="QUIT", command=window.destroy  ,fg=fgcolor ,bg=bgcolor  ,width=18  ,height=2, activebackground = "#CD5C5C" ,font=('times', 15, ' bold '))
quitWindow.place(x=1020, y=600)

 
window.mainloop()
