A=int(input("Enter Time In Hours : "))
B=int(input("Enter Time In Minutes : "))

HourHand=(A+B/60)*30
MinuteHand=B*6
Angle=abs(MinuteHand-HourHand)
if Angle>180:
    Angle=360-Angle
print(Angle)