import RPi.GPIO as GPIO		# import GPIO
import paho.mqtt.client as mqtt
from tkinter import *

coffrage=[IOoutlfu,IOoutlfd,IOoutrfu,IOoutrfd,IOoutlmu,IOoutlmd,IOoutrmu,IOoutrmd,IOoutltu,IOoutltd,IOoutrtu,IOoutrtd]
pieds=[IOoutup1,IOoutdo1,IOoutup2,IOoutdo2,IOoutup3,IOoutdo3,IOoutup4,IOoutdo4]

class pied():
    def __init__(self,pieds):
        self.IOoutup1=IOoutup1
        self.IOoutdo1=IOoutdo1
        self.IOoutup2=IOoutup2
        self.IOoutdo2=IOoutdo2
        self.IOoutup3=IOoutup3
        self.IOoutdo3=IOoutdo3
        self.IOoutup4=IOoutup4
        self.IOoutdo4=IOoutdo4

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.IOoutup1,GPIO.OUT)
        GPIO.output(self.IOoutup1, False)
        GPIO.setup(self.IOoutdo1,GPIO.OUT)
        GPIO.output(self.IOoutdo1, False)
        GPIO.setup(self.IOoutup2,GPIO.OUT)
        GPIO.output(self.IOoutup2, False)
        GPIO.setup(self.IOoutdo2,GPIO.OUT)
        GPIO.output(self.IOoutdo2, False)
        GPIO.setup(self.IOoutup3,GPIO.OUT)
        GPIO.output(self.IOoutup3, False)
        GPIO.setup(self.IOoutdo3,GPIO.OUT)
        GPIO.output(self.IOoutdo3, False)
        GPIO.setup(self.IOoutup4,GPIO.OUT)
        GPIO.output(self.IOoutup4, False)
        GPIO.setup(self.IOoutdo4,GPIO.OUT)
        GPIO.output(self.IOoutdo4, False)

    def up1():
        GPIO.output(self.IOoutup, True)
        print("Activation up1")
    def down1():
        GPIO.output(self.IOoutdo, True)
        print("Activation down1")
    
    def up2():
        GPIO.output(self.IOoutup, True)
        print("Activation up2")
    def down2():
        GPIO.output(self.IOoutdo, True)
        print("Activation down2")

    def up3():
        GPIO.output(self.IOoutup, True)
        print("Activation up3")
    def down3():
        GPIO.output(self.IOoutdo, True)
        print("Activation down3")

    def up4():
        GPIO.output(self.IOoutup, True)
        print("Activation up4")
    def down4():
        GPIO.output(self.IOoutdo, True)
        print("Activation down4")



class coffrage():
    def __init__(self,coffrage):
        for i in coffrage:
            self.i = i
            GPIO.setup(self.i,GPIO.OUT)
            GPIO.output(self.i,False)
    def activer(i):
        GPIO.output(self.i,True)
        print("Activation "+str(i))

fenetre = Tk()
for i in [coffrage,pieds]:
    buton[i]=Button(fenetre,text=str(i),command=bouton+str(i))
n=0
while n<100:
    for i in [pieds,coffrage]:
        if bouton+str(i) == True:
            activer+str(i)
    if bouton4up :
        activerup1,activerup2,activerup3,activerup4
    if bouton4down:
        activerdo1,activerdo2,activerdo3,activerdo4
    n=n+1



d.affNettoie()
GPIO.cleanup()
