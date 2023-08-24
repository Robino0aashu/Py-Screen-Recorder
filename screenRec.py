from tkinter import *
import pyscreenrec

scr=Tk()

scr.geometry("400x600")
scr.title("Screen Recorder")

scr.config(bg="#fff")
scr.resizable(False, False)

status=""

def startRec():
    status='Recording started'
    file=Filename.get()
    rec.start_recording(str(file+".mp4"),5)

def pauseRec():
    status='Paused!'
    rec.pause_recording()

def resumeRec():
    status='Recording'
    rec.resume_recording()

def stopRec():
    status="Recording saved"
    rec.stop_recording()

rec=pyscreenrec.ScreenRecorder()

#icon
image_icon=PhotoImage(file="icon.png")
scr.iconphoto(False, image_icon)

#bg image
image1=PhotoImage(file="yelllow.png")
Label(scr, image=image1, bg="#fff").place(x=-2, y=35)

image2=PhotoImage(file="blue.png")
Label(scr, image=image2, bg="#fff").place(x=223, y=200)

#Headline
lbl=Label(scr, text="Py Screen recorder", bg="#fff", font="arial 15 bold")
lbl.pack(pady=10)

image3=PhotoImage(file="recording.png")
Label(scr, image=image3, bd=5).pack(pady=30)

#Entry-Name
Filename=StringVar()
entry=Entry(scr, textvariable=Filename, width=18, font="arial 15")
entry.place(x=72, y=350)
Filename.set("Enter a name")


#buttons
start=Button(scr, text="Start", font="arial 20", bd=0, command=startRec)
start.place(x=135, y=235)

image4=PhotoImage(file="pause.png")
pause=Button(scr, image=image4, bd=0, bg="#fff", command=pauseRec)
pause.place(x=50, y=450)

image5=PhotoImage(file="resume.png")
resume=Button(scr, image=image5, bd=0, bg="#fff", command=resumeRec)
resume.place(x=150, y=450)

image6=PhotoImage(file="stop.png")
stop=Button(scr, image=image6, bd=0, bg="#fff", command=stopRec)
stop.place(x=250, y=450)


scr.mainloop()