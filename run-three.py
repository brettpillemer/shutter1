#!/usr/bin/env python

import RPi.GPIO as GPIO
import time


from Tkinter import *

root = Tk()
root.title("Shade Systems")
root.geometry("1020x600")

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT)# MOVEMENT - FORWARD
GPIO.setup(16, GPIO.OUT)# DIRECTIION - REVERSE

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # BREAK HOME POSITION SWITCH
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # SAFETY STOP SWITCH
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # BREAK END POSITION SWITCH

GPIO.output(18,GPIO.LOW)
GPIO.output(16,GPIO.LOW)




# VARIABLES #


 # YELLOW #
y_ENTRY800 = IntVar()
y_ENTRY900 = IntVar()
y_ENTRY1000 = IntVar()
y_ENTRY1100 = IntVar()
y_ENTRY1200 = IntVar()
y_ENTRY1300 = IntVar()
y_ENTRY1400 = IntVar()
y_ENTRY1500 = IntVar()
y_ENTRY1600 = IntVar()
y_ENTRY1700 = IntVar()
y_ENTRY830 = IntVar()
y_ENTRY930 = IntVar()
y_ENTRY1030 = IntVar()
y_ENTRY1130 = IntVar()
y_ENTRY1230 = IntVar()
y_ENTRY1330 = IntVar()
y_ENTRY1430 = IntVar()
y_ENTRY1530 = IntVar()
y_ENTRY1630 = IntVar()
y_ENTRY1730 = IntVar()
# BLUE #
b_ENTRY800 = IntVar()
b_ENTRY900 = IntVar()
b_ENTRY1000 = IntVar()
b_ENTRY1100 = IntVar()
b_ENTRY1200 = IntVar()
b_ENTRY1300 = IntVar()
b_ENTRY1400 = IntVar()
b_ENTRY1500 = IntVar()
b_ENTRY1600 = IntVar()
b_ENTRY1700 = IntVar()
b_ENTRY830 = IntVar()
b_ENTRY930 = IntVar()
b_ENTRY1030 = IntVar()
b_ENTRY1130 = IntVar()
b_ENTRY1230 = IntVar()
b_ENTRY1330 = IntVar()
b_ENTRY1430 = IntVar()
b_ENTRY1530 = IntVar()
b_ENTRY1630 = IntVar()
b_ENTRY1730 = IntVar()
# RED #
r_ENTRY800 = IntVar()
r_ENTRY900 = IntVar()
r_ENTRY1000 = IntVar()
r_ENTRY1100 = IntVar()
r_ENTRY1200 = IntVar()
r_ENTRY1300 = IntVar()
r_ENTRY1400 = IntVar()
r_ENTRY1500 = IntVar()
r_ENTRY1600 = IntVar()
r_ENTRY1700 = IntVar()
r_ENTRY830 = IntVar()
r_ENTRY930 = IntVar()
r_ENTRY1030 = IntVar()
r_ENTRY1130 = IntVar()
r_ENTRY1230 = IntVar()
r_ENTRY1330 = IntVar()
r_ENTRY1430 = IntVar()
r_ENTRY1530 = IntVar()
r_ENTRY1630 = IntVar()
r_ENTRY1730 = IntVar()
# Coordinates
b_X=IntVar()
b_Y=IntVar()
r_X=IntVar()
r_Y=IntVar()
l_X=IntVar()
l_Y=IntVar()
c_X=IntVar()
gap = IntVar()

time1 = ''
getStartTime = IntVar()
entryStartTime = IntVar()
varStartPosition = IntVar()
resetEntry = IntVar()
ENTRYInterval = IntVar()
ENTRYStartTime = IntVar()


Tcount = IntVar()
Ccount = IntVar()

# Radio
var = IntVar()

# TIME BOOLEANS
time800 = False
time900 = False
time1000 = False

move800 = IntVar()
move900 = IntVar()
move1000 = IntVar()
move1100 = IntVar()
move1200 = IntVar()
move1300 = IntVar()
move1400 = IntVar()
move1500 = IntVar()
move1600 = IntVar()
move1700 = IntVar()
move830 = IntVar()
move930 = IntVar()
move1030 = IntVar()
move1130 = IntVar()
move1230 = IntVar()
move1330 = IntVar()
move1430 = IntVar()
move1530 = IntVar()
move1630 = IntVar()
move1730 = IntVar()
move1800 = IntVar()
moveInterval = IntVar()
i = IntVar()

moveStartTime = IntVar()
# CHECK #
chk800 = IntVar()
chk830 = IntVar()
chk900 = IntVar()
chk930 = IntVar()
chk1000 = IntVar()
chk1030 = IntVar()
chk1100 = IntVar()
chk1130 = IntVar()
chk1200 = IntVar()
chk1230 = IntVar()
chk1300 = IntVar()
chk1330 = IntVar()
chk1400 = IntVar()
chk1430 = IntVar()
chk1500 = IntVar()
chk1530 = IntVar()
chk1600 = IntVar()
chk1630 = IntVar()
chk1700 = IntVar()
chk1730 = IntVar()
chk1800 = IntVar()






def saveFile():
    file = open('/home/pi/Desktop/summer.txt','w')
    file.write('this is a summer file')
    file.close()

def openFile():
    file = open('/Desktop/summer.txt','w')
    file.write('this is a summer file')
    file.close()






### FUNCTIONS ###


# MOVE MOTORS #

def y_season()
    y_ENTRY

def timeloop():
    Tcount = int(ENTRY800.get())
    Ccount = chk800.get()
    FuncMove(Tcount, Ccount)

    FuncStop()

    Tcount = int(ENTRY830.get())
    Ccount = chk830.get()
    FuncMove(Tcount, Ccount)

    FuncStop()
    
    Tcount = int(ENTRY900.get())
    Ccount = chk900.get()
    FuncMove(Tcount, Ccount)

    FuncStop()

    Tcount = int(ENTRY930.get())
    Ccount = chk930.get()
    FuncMove(Tcount, Ccount)

    FuncStop()
    
    Tcount = int(ENTRY1000.get())
    Ccount = chk1000.get()
    FuncMove(Tcount, Ccount)

    FuncStop()

    Tcount = int(ENTRY1030.get())
    Ccount = chk1030.get()
    FuncMove(Tcount, Ccount)
    
    FuncStop()
    
    Tcount = int(ENTRY1100.get())
    Ccount = chk1100.get()
    FuncMove(Tcount, Ccount)

    FuncStop()

    Tcount = int(ENTRY1130.get())
    Ccount = chk1130.get()
    FuncMove(Tcount, Ccount)

    FuncStop()
    
    Tcount = int(ENTRY1200.get())
    Ccount = chk1200.get()
    FuncMove(Tcount, Ccount)

    FuncStop()

    Tcount = int(ENTRY1230.get())
    Ccount = chk1230.get()
    FuncMove(Tcount, Ccount)

    FuncStop()
    
    Tcount = int(ENTRY1300.get())
    Ccount = chk1300.get()
    FuncMove(Tcount, Ccount)

    FuncStop()

    Tcount = int(ENTRY1330.get())
    Ccount = chk1330.get()
    FuncMove(Tcount, Ccount)

    FuncStop()
    
    Tcount = int(ENTRY1400.get())
    Ccount = chk1400.get()
    FuncMove(Tcount, Ccount)

    FuncStop()

    Tcount = int(ENTRY1430.get())
    Ccount = chk1430.get()
    FuncMove(Tcount, Ccount)

    FuncStop()
    
    Tcount = int(ENTRY1500.get())
    Ccount = chk1500.get()
    FuncMove(Tcount, Ccount)

    FuncStop()

    Tcount = int(ENTRY1530.get())
    Ccount = chk1530.get()
    FuncMove(Tcount, Ccount)

    FuncStop()
    
    Tcount = int(ENTRY1600.get())
    Ccount = chk1600.get()
    FuncMove(Tcount, Ccount)

    FuncStop()

    Tcount = int(ENTRY1630.get())
    Ccount = chk1630.get()
    FuncMove(Tcount, Ccount)

    FuncStop()
    
    Tcount = int(ENTRY1700.get())
    Ccount = chk1700.get()
    FuncMove(Tcount, Ccount)

    FuncStop()

    Tcount = int(ENTRY1730.get())
    Ccount = chk1730.get()
    FuncMove(Tcount, Ccount)

    gpioClear()
    
    FunClose()

    

def FunClose():
    GPIO.output(18,GPIO.LOW)
    GPIO.output(16,GPIO.LOW)
    GPIO.cleanup()
    

def FuncMove(Tcount, Ccount): 
    count = 0
    GPIO.output(18,GPIO.LOW)    
    GPIO.output(16,GPIO.LOW)
    while (count < Tcount):
            GPIO.output(18,GPIO.HIGH)    
            if Ccount is 1:
                GPIO.output(16,GPIO.HIGH)              
            if GPIO.input(11) == 1: #HOME
                GPIO.output(18,GPIO.LOW)  
                GPIO.output(16,GPIO.LOW)  
                return
            if GPIO.input(13) == 1: #SAFETY
                GPIO.output(18,GPIO.LOW)  
                GPIO.output(16,GPIO.LOW)  
                return
            if GPIO.input(15) == 1: #END
                GPIO.output(18,GPIO.LOW)  
                GPIO.output(16,GPIO.LOW)  
                return
            time.sleep(1)
            count = count + 1

# INTERVAL STOP #
def FuncStop():
    count = 0
    Tcount = int(ENTRYInterval.get())
    GPIO.output(18,GPIO.LOW)    
    GPIO.output(16,GPIO.LOW)
    while (count < Tcount):
            GPIO.output(18,GPIO.LOW)    
            if chk1800.get():
                GPIO.output(16,GPIO.LOW)              
            if GPIO.input(11) == 1: #HOME
                GPIO.output(18,GPIO.LOW)  
                GPIO.output(16,GPIO.LOW)  
                return
            if GPIO.input(13) == 1: #SAFETY
                GPIO.output(18,GPIO.LOW)  
                GPIO.output(16,GPIO.LOW)  
                return
            if GPIO.input(15) == 1: #END
                GPIO.output(18,GPIO.LOW)  
                GPIO.output(16,GPIO.LOW)  
                return
            time.sleep(1)
            count = count + 1    

            

    

# WORKING SMALL FUNCTIONS #
#########################################################################################################


# CLOCK #
def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)

# CLEAR GPIO #
def gpioClear():
    GPIO.output(18,GPIO.LOW)
    GPIO.output(16,GPIO.LOW)
    GPIO.cleanup()

# CALIBRATE #
def programReset():
    varStartPosition = int(resetEntry.get())
    while True:
        while GPIO.input(11) == 0:
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(16,GPIO.HIGH)
        else:
             GPIO.output(18,GPIO.HIGH)
             GPIO.output(16,GPIO.LOW)
             time.sleep(varStartPosition)
             GPIO.output(18,GPIO.LOW)
             GPIO.output(16,GPIO.LOW)
             return

# SET START TIME #

def programBeginStartTime():
    enteredStartTime = int(entryStartTime.get())
    getStartTime = time.strftime('%H%M')
#    label1 = Label(root,text="Time Now " + getStartTime)
#    label1.place(x=140, y=120)
#    label2 = Label(root,text="Time Entered " + str(enteredStartTime))
#    label2.place(x=140, y=150)    
    result = (str(getStartTime) == str(enteredStartTime))
#    print result
    if result:
        programBegin()
#        label5 = Label(root,text='True')
#        label5.place(x=140, y=180)
    if result is False:
#        label5 = Label(root,text='False')
#        label5.place(x=140, y=180)
        time.sleep(1)
        tick()
        programBeginStartTime()

        
#########################################################################################################
GPIO.output(18,GPIO.LOW)
GPIO.output(16,GPIO.LOW)

# GUI    #
# 8 9 10 #

# CANVAS #
canvasTop = Canvas(root, width = 190, height = 470, bg = "yellow")
canvasTop.place(x=220, y=30)
canvasTop = Canvas(root, width = 190-20, height = 470-20)
canvasTop.place(x=220+10, y=30+10)
canvasTop = Canvas(root, width = 190, height = 470, bg = "blue")
canvasTop.place(x=440, y=30)
canvasTop = Canvas(root, width = 190-20, height = 470-20)
canvasTop.place(x=440+10, y=30+10)
canvasTop = Canvas(root, width = 190, height = 470, bg = "red")
canvasTop.place(x=660, y=30)
canvasTop = Canvas(root, width = 190-20, height = 470-20)
canvasTop.place(x=660+10, y=30+10)

# CLOCK #
clock = Label(root, bg='green')
clock.place(x=100, y=30)
tick()
# DATE #
#clock = Label(root, font=('times', 15), bg='green')
#clock.place(x=40, y=10)
#tick()

# BUTTONS #
# Calibrate #
# labelReset = Label(root,text='Calibrate Start')
# labelReset.place(x=40, y=40)
entryReset = Entry(root, width  =5, textvariable = resetEntry)
entryReset.place(x=40, y=60)
buttonReset = Button(root, text="Calibrate", width  =10, command = programReset)
buttonReset.place(x=90, y=60)
# TEST RUN #
# labelRunTest = Label(root,text='Test Run')
# labelRunTest.place(x=40, y=140)
runTest = Button(root, text="Test Run", width  =10, command = timeloop)
runTest.place(x=90, y=90)
# START TIME #
# label1 = Label(root,text='Start Time HM')
# label1.place(x=40, y=220)
entry1 = Entry(root, width =5, textvariable = entryStartTime)
entry1.place(x=40, y=120)
buttonBegin = Button(root, text="Start Time", width  =10, command = programBeginStartTime)
buttonBegin.place(x=90, y=120)
# GPIO CLEAR #
buttonClear = Button(root, text="Clear Pins", width  =10, command = gpioClear)
buttonClear.place(x=90, y=150)




############## TIME INPUTS ###############
# Radio Buttin #
radiiobuttonBlue = Radiobutton(root, text="Yellow Season", variable=var, value = "1")
radiiobuttonBlue.place(x=90, y=180)
radiiobuttonBlue = Radiobutton(root, text="Blue Season", variable=var, value = "2")
radiiobuttonBlue.place(x=90, y=200)
radiiobuttonBlue = Radiobutton(root, text="Red Season", variable=var, value = "3")
radiiobuttonBlue.place(x=90, y=220)


# TIME YELLOW #
l_X= -26
l_Y= 2
c_X= 5
gap = 30

label800 = Label(root,text='8:00',width =9)
label800.place(x=260+l_X, y=40+l_Y)
entry800 = Entry(root, width =5, textvariable = y_ENTRY800)
entry800.place(x=260, y=60)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk800).place(x=230+c_X, y=60)

label830 = Label(root,text='8:30',width =9)
label830.place(x=380+l_X-gap, y=40+l_Y)
entry830 = Entry(root, width =5, textvariable = y_ENTRY830)
entry830.place(x=380-gap, y=60)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk830).place(x=350+c_X-gap, y=60)

label900 = Label(root,text='9:00',width =9)
label900.place(x=260+l_X, y=80+l_Y)
entry900 = Entry(root, width =5, textvariable = y_ENTRY900)
entry900.place(x=260, y=100)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk900).place(x=230+c_X, y=100)

label930 = Label(root,text='9:30',width =9)
label930.place(x=380+l_X-gap, y=80+l_Y)
entry930 = Entry(root, width =5, textvariable = y_ENTRY930)
entry930.place(x=380-gap, y=100)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk930).place(x=350+c_X-gap, y=100)

label1000 = Label(root,text='10:00',width =9)
label1000.place(x=260+l_X, y=120+l_Y)
entry1000 = Entry(root, width =5, textvariable = y_ENTRY1000)
entry1000.place(x=260, y=140)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1000).place(x=230+c_X, y=140)

label1030 = Label(root,text='10:30',width =9)
label1030.place(x=380+l_X-gap, y=120+l_Y)
entry1030 = Entry(root, width =5, textvariable = y_ENTRY1030)
entry1030.place(x=380-gap, y=140)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1030).place(x=350+c_X-gap, y=140)

label1100 = Label(root,text='11:00',width =9)
label1100.place(x=260+l_X, y=160+l_Y)
entry1100 = Entry(root, width =5, textvariable = y_ENTRY1100)
entry1100.place(x=260, y=180)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1100).place(x=230+c_X, y=180)

label1130 = Label(root,text='11:30',width =9)
label1130.place(x=380+l_X-gap, y=160+l_Y)
entry1130 = Entry(root, width =5, textvariable = y_ENTRY1130)
entry1130.place(x=380-gap, y=180)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1130).place(x=350+c_X-gap, y=180)

label1200 = Label(root,text='12:00',width =9)
label1200.place(x=260+l_X, y=200+l_Y)
entry1200 = Entry(root, width =5, textvariable = y_ENTRY1200)
entry1200.place(x=260, y=220)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1200).place(x=230+c_X, y=220)

label1230 = Label(root,text='12:30',width =9)
label1230.place(x=380+l_X-gap, y=200+l_Y)
entry1230 = Entry(root, width =5, textvariable = y_ENTRY1230)
entry1230.place(x=380-gap, y=220)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1230).place(x=350+c_X-gap, y=220)

label1300 = Label(root,text='13:00',width =9)
label1300.place(x=260+l_X, y=240+l_Y)
entry1300 = Entry(root, width =5, textvariable = y_ENTRY1300)
entry1300.place(x=260, y=260)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1300).place(x=230+c_X, y=260)

label1330 = Label(root,text='13:30',width =9)
label1330.place(x=380+l_X-gap, y=240+l_Y)
entry1330 = Entry(root, width =5, textvariable = y_ENTRY1330)
entry1330.place(x=380-gap, y=260)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1330).place(x=350+c_X-gap, y=260)

label400 = Label(root,text='14:00',width =9)
label400.place(x=260+l_X, y=280+l_Y)
entry1400 = Entry(root, width =5, textvariable = y_ENTRY1400)
entry1400.place(x=260, y=300)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1400).place(x=230+c_X, y=300)

label430 = Label(root,text='14:30',width =9)
label430.place(x=380+l_X-gap, y=280+l_Y)
entry1430 = Entry(root, width =5, textvariable = y_ENTRY1430)
entry1430.place(x=380-gap, y=300)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1430).place(x=350+c_X-gap, y=300)

label1500 = Label(root,text='15:00',width =9)
label1500.place(x=260+l_X, y=320+l_Y)
entry1500 = Entry(root, width =5, textvariable = y_ENTRY1500)
entry1500.place(x=260, y=340)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1500).place(x=230+c_X, y=340)

label1530 = Label(root,text='15:30',width =9)
label1530.place(x=380+l_X-gap, y=320+l_Y)
entry1530 = Entry(root, width =5, textvariable = y_ENTRY1530)
entry1530.place(x=380-gap, y=340)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1530).place(x=350+c_X-gap, y=340)

label1600 = Label(root,text='16:00',width =9)
label1600.place(x=260+l_X, y=360+l_Y)
entry1600 = Entry(root, width =5, textvariable = y_ENTRY1600)
entry1600.place(x=260, y=380)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1600).place(x=230+c_X, y=380)

label1630 = Label(root,text='16:30',width =9)
label1630.place(x=380+l_X-gap, y=360+l_Y)
entry1630 = Entry(root, width =5, textvariable = y_ENTRY1630)
entry1630.place(x=380-gap, y=380)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1630).place(x=350+c_X-gap, y=380)

label1700 = Label(root,text='17:00',width =9)
label1700.place(x=260+l_X, y=400+l_Y)
entry1700 = Entry(root, width =5, textvariable = y_ENTRY1700)
entry1700.place(x=260, y=420)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1700).place(x=230+c_X, y=420)

label1730 = Label(root,text='17:30',width =9)
label1730.place(x=380+l_X-gap, y=400+l_Y)
entry1730 = Entry(root, width =5, textvariable = y_ENTRY1730)
entry1730.place(x=380-gap, y=420)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1730).place(x=350+c_X-gap, y=420)

labelInterval = Label(root,text='Interval (1800)')
labelInterval.place(x=300+l_X, y=450+l_Y)
entryInterval = Entry(root, width =5, textvariable = ENTRYInterval)
entryInterval.place(x=300, y=470)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1800).place(x=270+c_X, y=470)


# TIME BLUE #
b_X = 220
label800 = Label(root,text='8:00',width =9)
label800.place(x= b_X+l_X +260, y=40+l_Y)
entry800 = Entry(root, width =5, textvariable = b_ENTRY800)
entry800.place(x= b_X +260, y=60)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk800).place(x= b_X +230+c_X, y=60)

label830 = Label(root,text='8:30',width =9)
label830.place(x= b_X+l_X +380-gap, y=40+l_Y)
entry830 = Entry(root, width =5, textvariable = b_ENTRY830)
entry830.place(x= b_X +380-gap, y=60)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk830).place(x= b_X +350+c_X-gap, y=60)

label900 = Label(root,text='9:00',width =9)
label900.place(x= b_X+l_X +260, y=80+l_Y)
entry900 = Entry(root, width =5, textvariable = b_ENTRY900)
entry900.place(x= b_X +260, y=100)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk900).place(x= b_X +230+c_X, y=100)

label930 = Label(root,text='9:30',width =9)
label930.place(x= b_X+l_X +380-gap, y=80+l_Y)
entry930 = Entry(root, width =5, textvariable = b_ENTRY930)
entry930.place(x= b_X +380-gap, y=100)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk930).place(x= b_X +350+c_X-gap, y=100)

label1000 = Label(root,text='10:00',width =9)
label1000.place(x= b_X+l_X +260, y=120+l_Y)
entry1000 = Entry(root, width =5, textvariable = b_ENTRY1000)
entry1000.place(x= b_X +260, y=140)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1000).place(x= b_X +230+c_X, y=140)

label1030 = Label(root,text='10:30',width =9)
label1030.place(x= b_X+l_X +380-gap, y=120+l_Y)
entry1030 = Entry(root, width =5, textvariable = b_ENTRY1030)
entry1030.place(x= b_X +380-gap, y=140)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1030).place(x= b_X +350+c_X-gap, y=140)

label1100 = Label(root,text='11:00',width =9)
label1100.place(x= b_X+l_X +260, y=160+l_Y)
entry1100 = Entry(root, width =5, textvariable = b_ENTRY1100)
entry1100.place(x= b_X +260, y=180)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1100).place(x= b_X +230+c_X, y=180)

label1130 = Label(root,text='11:30',width =9)
label1130.place(x= b_X+l_X +380-gap, y=160+l_Y)
entry1130 = Entry(root, width =5, textvariable = b_ENTRY1130)
entry1130.place(x= b_X +380-gap, y=180)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1130).place(x= b_X +350+c_X-gap, y=180)

label1200 = Label(root,text='12:00',width =9)
label1200.place(x= b_X+l_X +260, y=200+l_Y)
entry1200 = Entry(root, width =5, textvariable = b_ENTRY1200)
entry1200.place(x= b_X +260, y=220)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1200).place(x= b_X +230+c_X, y=220)

label1230 = Label(root,text='12:30',width =9)
label1230.place(x= b_X+l_X +380-gap, y=200+l_Y)
entry1230 = Entry(root, width =5, textvariable = b_ENTRY1230)
entry1230.place(x= b_X +380-gap, y=220)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1230).place(x= b_X +350+c_X-gap, y=220)

label1300 = Label(root,text='13:00',width =9)
label1300.place(x= b_X+l_X +260, y=240+l_Y)
entry1300 = Entry(root, width =5, textvariable = b_ENTRY1300)
entry1300.place(x= b_X +260, y=260)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1300).place(x= b_X +230+c_X, y=260)

label1330 = Label(root,text='13:30',width =9)
label1330.place(x= b_X+l_X +380-gap, y=240+l_Y)
entry1330 = Entry(root, width =5, textvariable = b_ENTRY1330)
entry1330.place(x= b_X +380-gap, y=260)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1330).place(x= b_X +350+c_X-gap, y=260)

label400 = Label(root,text='14:00',width =9)
label400.place(x= b_X+l_X +260, y=280+l_Y)
entry1400 = Entry(root, width =5, textvariable = b_ENTRY1400)
entry1400.place(x= b_X +260, y=300)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1400).place(x= b_X +230+c_X, y=300)

label430 = Label(root,text='14:30',width =9)
label430.place(x= b_X+l_X +380-gap, y=280+l_Y)
entry1430 = Entry(root, width =5, textvariable = b_ENTRY1430)
entry1430.place(x= b_X +380-gap, y=300)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1430).place(x= b_X +350+c_X-gap, y=300)

label1500 = Label(root,text='15:00',width =9)
label1500.place(x= b_X+l_X +260, y=320+l_Y)
entry1500 = Entry(root, width =5, textvariable = b_ENTRY1500)
entry1500.place(x= b_X +260, y=340)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1500).place(x= b_X +230+c_X, y=340)

label1530 = Label(root,text='15:30',width =9)
label1530.place(x= b_X+l_X +380-gap, y=320+l_Y)
entry1530 = Entry(root, width =5, textvariable = b_ENTRY1530)
entry1530.place(x= b_X +380-gap, y=340)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1530).place(x= b_X +350+c_X-gap, y=340)

label1600 = Label(root,text='16:00',width =9)
label1600.place(x= b_X+l_X +260, y=360+l_Y)
entry1600 = Entry(root, width =5, textvariable = b_ENTRY1600)
entry1600.place(x= b_X +260, y=380)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1600).place(x= b_X +230+c_X, y=380)

label1630 = Label(root,text='16:30',width =9)
label1630.place(x= b_X+l_X +380-gap, y=360+l_Y)
entry1630 = Entry(root, width =5, textvariable = b_ENTRY1630)
entry1630.place(x= b_X +380-gap, y=380)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1630).place(x= b_X +350+c_X-gap, y=380)

label1700 = Label(root,text='17:00',width =9)
label1700.place(x= b_X+l_X +260, y=400+l_Y)
entry1700 = Entry(root, width =5, textvariable = b_ENTRY1700)
entry1700.place(x= b_X +260, y=420)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1700).place(x= b_X +230+c_X, y=420)

label1730 = Label(root,text='17:30',width =9)
label1730.place(x= b_X+l_X +380-gap, y=400+l_Y)
entry1730 = Entry(root, width =5, textvariable = b_ENTRY1730)
entry1730.place(x= b_X +380-gap, y=420)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1730).place(x= b_X +350+c_X-gap, y=420)

labelInterval = Label(root,text='Interval (1800)')
labelInterval.place(x= b_X+l_X +300, y=450+l_Y)
entryInterval = Entry(root, width =5, textvariable = ENTRYInterval)
entryInterval.place(x= b_X +300, y=470)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1800).place(x= b_X +270+c_X, y=470)

# TIME RED #
r_X = 440
label800 = Label(root,text='8:00',width =9)
label800.place(x= r_X+l_X +260, y=40+l_Y)
entry800 = Entry(root, width =5, textvariable = r_ENTRY800)
entry800.place(x= r_X +260, y=60)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk800).place(x= r_X +230+c_X, y=60)

label830 = Label(root,text='8:30',width =9)
label830.place(x= r_X+l_X +380-gap, y=40+l_Y)
entry830 = Entry(root, width =5, textvariable = r_ENTRY830)
entry830.place(x= r_X +380-gap, y=60)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk830).place(x= r_X +350+c_X-gap, y=60)

label900 = Label(root,text='9:00',width =9)
label900.place(x= r_X+l_X +260, y=80+l_Y)
entry900 = Entry(root, width =5, textvariable = r_ENTRY900)
entry900.place(x= r_X +260, y=100)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk900).place(x= r_X +230+c_X, y=100)

label930 = Label(root,text='9:30',width =9)
label930.place(x= r_X+l_X +380-gap, y=80+l_Y)
entry930 = Entry(root, width =5, textvariable = r_ENTRY930)
entry930.place(x= r_X +380-gap, y=100)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk930).place(x= r_X +350+c_X-gap, y=100)

label1000 = Label(root,text='10:00',width =9)
label1000.place(x= r_X+l_X +260, y=120+l_Y)
entry1000 = Entry(root, width =5, textvariable = r_ENTRY1000)
entry1000.place(x= r_X +260, y=140)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1000).place(x= r_X +230+c_X, y=140)

label1030 = Label(root,text='10:30',width =9)
label1030.place(x= r_X+l_X +380-gap, y=120+l_Y)
entry1030 = Entry(root, width =5, textvariable = r_ENTRY1030)
entry1030.place(x= r_X +380-gap, y=140)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1030).place(x= r_X +350+c_X-gap, y=140)

label1100 = Label(root,text='11:00',width =9)
label1100.place(x= r_X+l_X +260, y=160+l_Y)
entry1100 = Entry(root, width =5, textvariable = r_ENTRY1100)
entry1100.place(x= r_X +260, y=180)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1100).place(x= r_X +230+c_X, y=180)

label1130 = Label(root,text='11:30',width =9)
label1130.place(x= r_X+l_X +380-gap, y=160+l_Y)
entry1130 = Entry(root, width =5, textvariable = r_ENTRY1130)
entry1130.place(x= r_X +380-gap, y=180)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1130).place(x= r_X +350+c_X-gap, y=180)

label1200 = Label(root,text='12:00',width =9)
label1200.place(x= r_X+l_X +260, y=200+l_Y)
entry1200 = Entry(root, width =5, textvariable = r_ENTRY1200)
entry1200.place(x= r_X +260, y=220)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1200).place(x= r_X +230+c_X, y=220)

label1230 = Label(root,text='12:30',width =9)
label1230.place(x= r_X+l_X +380-gap, y=200+l_Y)
entry1230 = Entry(root, width =5, textvariable = r_ENTRY1230)
entry1230.place(x= r_X +380-gap, y=220)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1230).place(x= r_X +350+c_X-gap, y=220)

label1300 = Label(root,text='13:00',width =9)
label1300.place(x= r_X+l_X +260, y=240+l_Y)
entry1300 = Entry(root, width =5, textvariable = r_ENTRY1300)
entry1300.place(x= r_X +260, y=260)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1300).place(x= r_X +230+c_X, y=260)

label1330 = Label(root,text='13:30',width =9)
label1330.place(x= r_X+l_X +380-gap, y=240+l_Y)
entry1330 = Entry(root, width =5, textvariable = r_ENTRY1330)
entry1330.place(x= r_X +380-gap, y=260)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1330).place(x= r_X +350+c_X-gap, y=260)

label400 = Label(root,text='14:00',width =9)
label400.place(x= r_X+l_X +260, y=280+l_Y)
entry1400 = Entry(root, width =5, textvariable = r_ENTRY1400)
entry1400.place(x= r_X +260, y=300)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1400).place(x= r_X +230+c_X, y=300)

label430 = Label(root,text='14:30',width =9)
label430.place(x= r_X+l_X +380-gap, y=280+l_Y)
entry1430 = Entry(root, width =5, textvariable = r_ENTRY1430)
entry1430.place(x= r_X +380-gap, y=300)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1430).place(x= r_X +350+c_X-gap, y=300)

label1500 = Label(root,text='15:00',width =9)
label1500.place(x= r_X+l_X +260, y=320+l_Y)
entry1500 = Entry(root, width =5, textvariable = r_ENTRY1500)
entry1500.place(x= r_X +260, y=340)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1500).place(x= r_X +230+c_X, y=340)

label1530 = Label(root,text='15:30',width =9)
label1530.place(x= r_X+l_X +380-gap, y=320+l_Y)
entry1530 = Entry(root, width =5, textvariable = r_ENTRY1530)
entry1530.place(x= r_X +380-gap, y=340)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1530).place(x= r_X +350+c_X-gap, y=340)

label1600 = Label(root,text='16:00',width =9)
label1600.place(x= r_X+l_X +260, y=360+l_Y)
entry1600 = Entry(root, width =5, textvariable = r_ENTRY1600)
entry1600.place(x= r_X +260, y=380)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1600).place(x= r_X +230+c_X, y=380)

label1630 = Label(root,text='16:30',width =9)
label1630.place(x= r_X+l_X +380-gap, y=360+l_Y)
entry1630 = Entry(root, width =5, textvariable = r_ENTRY1630)
entry1630.place(x= r_X +380-gap, y=380)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1630).place(x= r_X +350+c_X-gap, y=380)

label1700 = Label(root,text='17:00',width =9)
label1700.place(x= r_X+l_X +260, y=400+l_Y)
entry1700 = Entry(root, width =5, textvariable = r_ENTRY1700)
entry1700.place(x= r_X +260, y=420)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1700).place(x= r_X +230+c_X, y=420)

label1730 = Label(root,text='17:30',width =9)
label1730.place(x= r_X+l_X +380-gap, y=400+l_Y)
entry1730 = Entry(root, width =5, textvariable = r_ENTRY1730)
entry1730.place(x= r_X +380-gap, y=420)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1730).place(x= r_X +350+c_X-gap, y=420)

labelInterval = Label(root,text='Interval (1800)')
labelInterval.place(x= r_X+l_X +300, y=450+l_Y)
entryInterval = Entry(root, width =5, textvariable = ENTRYInterval)
entryInterval.place(x= r_X +300, y=470)
Checkbutton(root, text="", onvalue=1, offvalue=0, variable=chk1800).place(x= r_X +270+c_X, y=470)



root.mainloop()





