from CounterModule import *
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as font
import time
from PIL import Image, ImageTk
from game import*
from threading import Thread
import tkinter as tk 
# from data_collection import data_collection
# from training import training
from inference import inference
from data_collection_yoga import data_collection_yoga
from data_training_yoga import data_training_yoga
from inference_yoga import inference_yoga
import tkinter.font as font
from playsound import playsound

root = tk.Tk(className='Main MENU')
root.geometry("434x700")
root.minsize(434,700)
root.maxsize(434,700)

introFrame = tk.Frame(root, bg= "#F5F7FD" )
introFrame.place(height=1000, width=630, x=0, y=0)

homeFrame = tk.Frame(root, bg= "#F5F7FD" )
homeFrame.place(height=1000, width=630, x=1000, y=0)

workoutFrame = tk.Frame(root, bg= "#F5F7FD" )
workoutFrame.place(height=1000, width=630, x=1000, y=0)

difficultyFrame = tk.Frame(root, bg= "#F5F7FD" )
difficultyFrame.place(height=1000, width=630, x=1000, y=0)

yogaFrame = tk.Frame(root, bg= "#F5F7FD" )
yogaFrame.place(height=1000, width=630, x=1000, y=0)

def introFrameOpen():
    introFrame.place(x=0,y=0) 
    homeFrame.place(x=-630,y=0)
    workoutFrame.place(x=-630,y=0)
    difficultyFrame.place(x=-630,y=0)
    yogaFrame.place(x=-630,y=0)

def homeFrameOpen():
    homeFrame.place(x=0,y=0)
    introFrame.place(x=-630,y=0)
    workoutFrame.place(x=-630,y=0)
    difficultyFrame.place(x=-630,y=0)
    yogaFrame.place(x=-630,y=0)

def workoutFrameOpen():
    workoutFrame.place(x=0,y=0)
    homeFrame.place(x=-630,y=0)
    introFrame.place(x=-630,y=0)
    difficultyFrame.place(x=-630,y=0)
    yogaFrame.place(x=-630,y=0)

def difficultyFrameOpen():
    difficultyFrame.place(x=0,y=0)
    workoutFrame.place(x=-630,y=0)
    homeFrame.place(x=-630,y=0)
    introFrame.place(x=-630,y=0)
    yogaFrame.place(x=-630,y=0)

def yogaFrameOpen():
    difficultyFrame.place(x=-630,y=0)
    workoutFrame.place(x=-630,y=0)
    homeFrame.place(x=-630,y=0)
    introFrame.place(x=-630,y=0)
    yogaFrame.place(x=0,y=0)



def easy():
    entry1 = 3
    difficulty = entry1
    playsound('Audio Files\\bicepcurls.mp3')
    curl_counter(difficulty)
    take_rest()
    playsound('Audio Files\\highknees.mp3')
    running_counter(difficulty)
    take_rest()
    playsound('Audio Files\\toetouch.mp3')
    toeTouch_counter(difficulty)
    take_rest()
    playsound('Audio Files\\jumps.mp3')
    jump_counter(5)
    take_rest()
    homeFrameOpen()

def moderate():
    entry1 = 3
    difficulty = entry1  
    curl_counter(difficulty)
    take_rest()
    squat_counter(difficulty)
    take_rest()
    tricep_counter(difficulty)
    take_rest()
    homeFrameOpen()
    
def hard():
    kick_counter(5)
    take_rest()
    punch_counter(5)
    homeFrameOpen()

def posture_detector_callback():
    posture_detector_advanced_u()
    homeFrameOpen()

def yoga_run():
    inference_yoga()
    homeFrameOpen()
    cap.release()

def inference_call():
    inference()
    cap.release()

def counter_time_callback():
    # if __name__ == '__main__':
    #     Thread(target = Zenitsu_Run).start()
    #     Thread(target = game_detection).start()
    # inference()
    pass
#######################################
# Sign in frame

landingImage = (Image.open("Assets/image 1.png"))
landingImage = landingImage.resize((434,563), Image.ANTIALIAS)
landingImage = ImageTk.PhotoImage(landingImage)
label = Label(introFrame, image = landingImage)
label.place(x=int(0), y=(0))

signupImage = Image.open("Assets/image 3.png")
signupImage = signupImage.resize((230,60), Image.ANTIALIAS)
signupImage = ImageTk.PhotoImage(signupImage)
startButton = Button(introFrame,image = signupImage ,bg='#F5F7FD',command = homeFrameOpen ,borderwidth = 0)
startButton.place(x=int(102.2), y=int(503.55))

startimage = Image.open("Assets/image 4.png")
startimage = startimage.resize((230,60), Image.ANTIALIAS)
startimage = ImageTk.PhotoImage(startimage)
startButton = Button(introFrame,image = startimage ,bg='#F5F7FD',command = homeFrameOpen ,borderwidth = 0)
startButton.place(x=int(102.2) ,y=int(580.43))


################################################################################
#home Frame

topimage = (Image.open("Assets/page1_1.png"))
topimage = topimage.resize((434,156), Image.ANTIALIAS)
topimage = ImageTk.PhotoImage(topimage)
label = Label(homeFrame, image = topimage,borderwidth = 0)
label.place(x=0, y=0)

buttonHome1 = Image.open("Assets/page1_2.png")
buttonHome1 = buttonHome1.resize((367,133), Image.ANTIALIAS)
buttonHome1 = ImageTk.PhotoImage(buttonHome1)
startButton = Button(homeFrame,image = buttonHome1 ,command = workoutFrameOpen ,borderwidth = 0)
startButton.place(x=33 ,y=182)

buttonHome2 = Image.open("Assets/page1_3.png")
buttonHome2 = buttonHome2.resize((367,133), Image.ANTIALIAS)
buttonHome2 = ImageTk.PhotoImage(buttonHome2)
startButton = Button(homeFrame,image = buttonHome2 ,command = posture_detector_callback ,borderwidth = 0)
startButton.place(x=33 ,y=341)

# buttonHome3 = Image.open("Assets\page1_5.png")
# buttonHome3 = buttonHome3.resize((367,133), Image.ANTIALIAS)
# buttonHome3 = ImageTk.PhotoImage(buttonHome3)
# startButton = Button(homeFrame,image = buttonHome3 , command = inference_call ,borderwidth = 0)
# startButton.place(x=33 ,y=501)

################################################################################
#workout Frame

topimagework = (Image.open("Assets/page1_1.png"))
topimagework = topimagework.resize((434,156), Image.ANTIALIAS)
topimagework = ImageTk.PhotoImage(topimagework)
label = Label(workoutFrame, image = topimagework,borderwidth = 0)
label.place(x=0, y=0)

buttonHomework1 = Image.open("Assets/page2_2.png")
buttonHomework1 = buttonHomework1.resize((367,133), Image.ANTIALIAS)
buttonHomework1 = ImageTk.PhotoImage(buttonHomework1)
startButton1 = Button(workoutFrame,image = buttonHomework1 ,command = difficultyFrameOpen ,borderwidth = 0)
startButton1.place(x=33 ,y=182)

buttonHomework2 = Image.open("Assets/page2_3.png")
buttonHomework2 = buttonHomework2.resize((367,133), Image.ANTIALIAS)
buttonHomework2 = ImageTk.PhotoImage(buttonHomework2)
startButton2 = Button(workoutFrame,image = buttonHomework2 ,command = yogaFrameOpen ,borderwidth = 0)
startButton2.place(x=33 ,y=341)

buttonHomework3 = Image.open("Assets/page2_4.png")
buttonHomework3 = buttonHomework3.resize((367,133), Image.ANTIALIAS)
buttonHomework3 = ImageTk.PhotoImage(buttonHomework3)
startButton3 = Button(workoutFrame,image = buttonHomework3 ,command = hard ,borderwidth = 0)
startButton3.place(x=33 ,y=501)


################################################################################
#difficulty Frame

topimagediff = (Image.open("Assets/page1_1.png"))
topimagediff = topimagediff.resize((434,156), Image.ANTIALIAS)
topimagediff = ImageTk.PhotoImage(topimagediff)
label = Label(difficultyFrame, image = topimagediff,borderwidth = 0)
label.place(x=0, y=0)

buttonHomediff1 = Image.open("Assets/page3_2.png")
buttonHomediff1 = buttonHomediff1.resize((367,133), Image.ANTIALIAS)
buttonHomediff1 = ImageTk.PhotoImage(buttonHomediff1)
startButton4 = Button(difficultyFrame,image = buttonHomediff1 ,command = easy ,borderwidth = 0)
startButton4.place(x=33 ,y=182)

buttonHomediff2 = Image.open("Assets/page3_3.png")
buttonHomediff2 = buttonHomediff2.resize((367,133), Image.ANTIALIAS)
buttonHomediff2 = ImageTk.PhotoImage(buttonHomediff2)
startButton5 = Button(difficultyFrame,image = buttonHomediff2 ,command = moderate ,borderwidth = 0)
startButton5.place(x=33 ,y=341)

buttonHomediff3 = Image.open("Assets/page3_4.png")
buttonHomediff3 = buttonHomediff3.resize((367,133), Image.ANTIALIAS)
buttonHomediff3 = ImageTk.PhotoImage(buttonHomediff3)
startButton6 = Button(difficultyFrame,image = buttonHomediff3, command = hard ,borderwidth = 0)
startButton6.place(x=33 ,y=501)

###############################
#yoga frame

topimageyoga = (Image.open("Assets/page4_1.png"))
topimageyoga = topimageyoga.resize((434,156), Image.ANTIALIAS)
topimageyoga = ImageTk.PhotoImage(topimageyoga)
label = Label(yogaFrame, image = topimageyoga,borderwidth = 0)
label.place(x=0, y=0)

buttonHomeyoga1 = Image.open("Assets/page4_2.png")
buttonHomeyoga1 = buttonHomeyoga1.resize((367,133), Image.ANTIALIAS)
buttonHomeyoga1 = ImageTk.PhotoImage(buttonHomeyoga1)
startButton7 = Button(yogaFrame,image = buttonHomeyoga1 ,command = data_collection_yoga ,borderwidth = 0)
startButton7.place(x=33 ,y=182)

buttonHomeyoga2 = Image.open("Assets/page4_3.png")
buttonHomeyoga2 = buttonHomeyoga2.resize((367,133), Image.ANTIALIAS)
buttonHomeyoga2 = ImageTk.PhotoImage(buttonHomeyoga2)
startButton8 = Button(yogaFrame,image = buttonHomeyoga2 ,command = data_training_yoga ,borderwidth = 0)
startButton8.place(x=33 ,y=341)

buttonHomeyoga3 = Image.open("Assets/page4_4.png")
buttonHomeyoga3 = buttonHomeyoga3.resize((367,133), Image.ANTIALIAS)
buttonHomeyoga3 = ImageTk.PhotoImage(buttonHomeyoga3)
startButton9 = Button(yogaFrame,image = buttonHomeyoga3,command = yoga_run ,borderwidth = 0)
startButton9.place(x=33 ,y=501)

root.mainloop()