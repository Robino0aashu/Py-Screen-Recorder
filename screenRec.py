import tkinter as tk
import pyscreenrec

scr=tk.Tk()

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
image_icon=tk.PhotoImage(file="icon.png")
scr.iconphoto(False, image_icon)

#bg image
image1=tk.PhotoImage(file="yelllow.png")
tk.Label(scr, image=image1, bg="#fff").place(x=-2, y=35)

image2=tk.PhotoImage(file="blue.png")
tk.Label(scr, image=image2, bg="#fff").place(x=223, y=200)

#Headline
lbl=tk.Label(scr, text="Py Screen recorder", bg="#fff", font="arial 15 bold")
lbl.pack(pady=10)

image3=tk.PhotoImage(file="recording.png")
tk.Label(scr, image=image3, bd=5).pack(pady=30)

#Entry-Name
Filename=tk.StringVar()
entry=tk.Entry(scr, textvariable=Filename, width=18, font="arial 15")
entry.place(x=72, y=350)
Filename.set("Enter a name")


#buttons
start=tk.Button(scr, text="Start", font="arial 20", bd=0, command=startRec)
start.place(x=135, y=235)

image4=tk.PhotoImage(file="pause.png")
pause=tk.Button(scr, image=image4, bd=0, bg="#fff", command=pauseRec)
pause.place(x=50, y=450)

image5=tk.PhotoImage(file="resume.png")
resume=tk.Button(scr, image=image5, bd=0, bg="#fff", command=resumeRec)
resume.place(x=150, y=450)

image6=tk.PhotoImage(file="stop.png")
stop=tk.Button(scr, image=image6, bd=0, bg="#fff", command=stopRec)
stop.place(x=250, y=450)


scr.mainloop()