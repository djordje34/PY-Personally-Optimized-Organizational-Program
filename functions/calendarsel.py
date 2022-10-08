import os
import tkinter as tk
from tkcalendar import *
from functions.offlinefuncs import open_notepad
import tkinter.font as font


color={"purple":"#461E52",
        "pink":"#DD517F",
        "yellow":"#E68E36",
        "darkblue":"#556DC8",
        "lightblue":"#7998EE"}
def getWindow(msg,username):                             #NOVA FNKCIJA U GUI DA POZOVE TALK BLOKIRA PROZOR I PRIKAZI LISTENING KAD SE UPALI TALK!!!
    
    name = os.path.join(f'C:\\Users\\{username}\\Desktop')
    root = tk.Tk()
    mainF = font.Font(family='Helvetica', size=16, weight='bold')   
    root.geometry("600x480")
                
                # Add Calendar
    cal = Calendar(root, selectmode = 'day',         
                            year = 2022, month = 1,
                            day = 1,date_pattern="dd-mm-y",selectbackground=color["pink"],headersbackground="black",headersforeground="white",
                            normalbackground=color["lightblue"],weekendbackground=color["lightblue"],borderbackground=color["purple"],othermonthbackground="lightgrey",othermonthforegorund="black"
                            ,font=mainF)
                
    cal.pack(pady = 20)
                
    def grad_date():
                    dt=cal.get_date().split('/')
                    dt='_'.join([x for x in dt])
                    ne=str(cal.get_date())+'.txt'
                    with open(name+"\\"+ne, 'w+') as f:
                        f.write(cal.get_date().replace("-",".")+".\n\n")
                        f.write(msg)
                        open_notepad(name+"\\"+ne)
                # Add Button and Label
    tk.Button(root, text = "Write a note",
                    command = grad_date,font=mainF,
                    bg=color["lightblue"],fg=color["darkblue"],activebackground=color["lightblue"],activeforeground=color["purple"]
                    ).pack(pady = 20)
                
    date = tk.Label(root, text = "",font=mainF,fg=color["yellow"])
    date.pack(pady = 20)
                
                
    root.mainloop()
    
    


def main():
    getWindow("OPEN","Djordje")

if __name__=='__main__':
    main()
    
    