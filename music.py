from tkinter import *
from PIL import Image , ImageTk
from tkinter import filedialog
from pygame import mixer
mixer.init()



class music_player :
       def __init__(self, Tk):
          self.root=Tk
          self.root.title("Music_Player")
          self.root.geometry("500x500")
          self.root.configure(background="purple")
          
          #Adding Label 
        
          self.label = Label(text="Enjoy Buddy!", bg="black",fg="orange", font=22).place(x=50, y=20)
          
          # Adding image

          self.photo = ImageTk.PhotoImage(file="hisoka.jpg")
          photo = Label(self.root, image= self.photo, bg="white").place(x=50, y=50)

          def Openfile():
              global filename
              filename= filedialog.askopenfilename()
               
          # Menu
  
          self.menubar=Menu(self.root)
          self.root.configure(menu=self.menubar)

          self.submenu= Menu(self.menubar, tearoff=0)
          self.menubar.add_cascade(label="File", menu=self.submenu)
          self.submenu.add_command(label="Open", command=Openfile)
        

          # label 
          self.label1 =Label(self.root,text="Let's play it.", bg="black", fg="white", font=20)
          self.label1.pack(side=BOTTOM, fill=X)

          #function for play button
          def playmusic ():
              try:
                   paused 
              except NameError:
                   
                  try:
                    
                    mixer.music.load(filename)
                    mixer.music.play()
                    self.label1['text']="Music_Playing..."
                  except:
                    pass
                  
              else:
                      mixer.music.unpause()
                      self.label1["text"]="Music_Unpaused"
                  

          # creating Button
          #Play-Button 
          self.photo_B1= ImageTk.PhotoImage(file="button.jpg")
          photo_B1=Button(self.root, image=self.photo_B1, bd=0, bg="white", command=playmusic).place(x=1100, y=30)

          # functiom for pause button

          def musicpause():
               global paused
               paused = TRUE
               mixer.music.pause()
               self.label1["text"]="Music_Pause"

         #Pause Button
          self.photo_B2= ImageTk.PhotoImage(file="button2.png")
          photo_B2=Button(self.root, image=self.photo_B2, bd=0, bg="white", command=musicpause).place(x=1100, y=250)
            
          # self.pause_B2 =Button(self.root, text="Pause", bg="pink", command=musicpause, width=25, height=5).place(x=1100,y=250)

         #functiom for stop button 
          def stopmusic():
                mixer.music.stop()
                self.label1["text"]="Music_Stopped"

         
         # stop Button
          self.photo_B3= ImageTk.PhotoImage(file="button3.png")
          photo_B3=Button(self.root, image=self.photo_B3, bd=0, bg="white", command=stopmusic).place(x=1100, y= 480)

        
    

      
root=Tk()

obj = music_player(root)
root.mainloop() #to close window

 
































































