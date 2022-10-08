import os
import tkinter as tk
from poop import Poop
from PIL import ImageTk, Image
import tkinter.font as font
color={"purple":"#461E52",
        "pink":"#DD517F",
        "yellow":"#E68E36",
        "darkblue":"#556DC8",
        "lightblue":"#7998EE"}

class Interface():
    
    def __init__(self,bot):
        self.bot=bot
        self.win = tk.Tk()
        
    #poop.talk()
        self.win.wm_attributes('-transparentcolor','white')
        mainF = font.Font(family='Helvetica', size=20, weight='bold')    
        bot.greet()
        iconpath=path=os.path.join("images\\iconfaster.ico")
        self.win.iconbitmap(iconpath)
        screen_width =  self.win.winfo_screenwidth()
        screen_height = self.win.winfo_screenheight()
        self.win.geometry(str(screen_width)+"x"+str(screen_height))
        self.win.state('zoomed')
        path=os.path.join("images\\background.jpg")
        img = ImageTk.PhotoImage(Image.open(path))  # PIL solution
        bgHolder=tk.Label(image=img)
        bgHolder.place(x=0,y=0,relwidth=1, relheight=1)
        
        self.talkBtn=tk.Button(self.win,command=self.botTalks, text="Talk",bg=color["lightblue"],fg=color["darkblue"],font=mainF,activebackground=color["lightblue"],activeforeground=color["purple"],borderwidth=0)
        self.talkBtn.pack(side="top",anchor="n",pady=20)
        self.win.title('Personalized Optimized Organizational Program')
        self.userText=tk.Label(self.win,font=mainF,fg=color["darkblue"],bg=color["lightblue"])
        self.botText=tk.Label(self.win,font=mainF,fg=color["darkblue"],bg=color["lightblue"], wraplength=500)
        
        self.win.mainloop()
        
        
        
        
    def botTalks(self):
        ctr=0
        self.win.grab_set()
        for el in self.bot.talk():
            
            val=el
            if ctr%2==0:
                val=el
                self.userText["text"]=val
                self.userText.pack(side="left",anchor="n",pady=20)
            else:
                self.botText["text"]=val
                self.botText.pack(side="right",anchor="n",pady=20)
            ctr+=1
            self.win.update()
            
        self.win.grab_release()
        
def main():
    bot=Poop()
    int=Interface(bot)

    
    
if __name__=="__main__":
    main()