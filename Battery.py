import math
from math import ceil
#Battery Estimation Program
#if this is python version 2.. write raw_input
batteryCap = input("What is your Battery's Capacity? ")
    if batteryCap == "N/A":
    batteryType = input("What battery type do you use? ") 
minVol = input("What is the minimum voltage level? ") #2.5V is minimum
numBat = input("How many batteries in a series? ")
sleepPower = input("How much power does Logger use when in sleep mode? ")
logBasePower = input("What is the logger's base power? ") #why we need this
awakePower = input("What is the power consumption when logging? ")
senPowerDraw = input("What is the sensor's power draw? ")
logInterval = input("What is the logging interval? ") #Units: Seconds?
logDuration = input("What is logging duration? ") 
if logDuration = "N/A":
    logDuration =.25
if logInterval == "N/A":
    logInterval = 1 #if we don not know the logging duration or interval we assume it will be 1 second
minTemp = input("What is the minimum temperature that the battery is opearting in?")
TSleep = logInterval - logDuration
TAwake = logDuration

V = ceil((minVol/numBat)*10)/10.0
#same as above code V = ceil(V*10)/10.0
volt = .9
mini = 20

for x in range(0,4):
    dif = abs(volt - V)
    if dif <= mini:
            mini = dif
            Vt = volt
    volt = volt + .1        

oneTwoV = (10, 192, 102, 116, 1000, .201) #(x,y) = (I,R)
oneOneV = (10, 220, 102, 189, 1000, .287)
oneV = (10, 240, 102, 219, 1000, .654) 
PNineV = (10, 275, 102, 264, 1000, .922)

if Vt == 1.2:
    ROne = oneTwoV[1]
    RTwo = oneTwoV[5]
    IOne = oneTwoV[0]
    ITwo = oneTwoV[4]
    COne = oneTwoV[0]*oneTwoV[1]
    CTwo = oneTwoV[5]*oneTwoV[4]
if Vt == 1.1:
    ROne = oneOneV[1]
    RTwo = oneOneV[5]
    IOne = oneOneV[0]
    ITwo = oneOneV[4]
    COne = oneOneV[0]*oneOneV[1]
    CTwo = oneOneV[5]*oneOneV[4]
    
if Vt == 1:
    ROne = oneV[1]
    RTwo = oneV[5]
    IOne = oneV[0]
    ITwo = oneV[4]
    COne = oneV[0]*oneV[1]
    CTwo = oneV[5]*oneV[4]
    
if Vt == 0.9:
    ROne = PNineV[1]
    RTwo = PNineV[5]
    IOne = PNineV[0]
    ITwo = PNineV[4]
    COne = PNineV[0]*PNineV[1]
    CTwo = PNineV[5]*PNineV[4]

Peukert = Peukert(ROne, RTwo, COne, CTwo)
PeukertB = PeukertB(ROne, RTwo, IOne, ITwo)

time = Time(logDuration, batteryCap, awakePower, Peukert)
#C is I3*T3, awakePower*Time logger Awake
def Peukert(ROne, RTwo, COne, CTwo): #BatteryStuff Formula
                    k = math.log(RTwo/ROne)/(math.log(COne/ROne) - math.log(CTwo/RTwo))
                    return k
#This uses the graph     

def Time(H, C, I, K): #H = rated discharge time, C = rated capacity, I = discharge current (amp), k = peukerts number
        t = H*((C/(I*H))**K) #what is our C, do they give to us? I = load from sensor, H is the interval of power
        return t #What is I0
def EffCapacity(C, I, H, K):
        EfCap = C*(C/I*H)**(k-1)
        return EfCap
          
def PeukertB(ROne, RTwo, IOne, ITwo):
    k = math.log(multi, ITwo) #base is ITwo
    return k



