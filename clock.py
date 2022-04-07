import time
import datetime as dt
import turtle
  
     
# saati gösterecek çerçeve
cerceve = turtle.Turtle()
 
# ekranı oluşturalım
ekran = turtle.Screen()
 
# ekran arka alan rengi
ekran.bgcolor("yellow")
  
# sistemden mevcut zamanı alalım
sn = dt.datetime.now().second
dk = dt.datetime.now().minute
sa = dt.datetime.now().hour

while True:
    cerceve.hideturtle()
    cerceve.clear()
    # display the time
    cerceve.write(str(sa).zfill(2)
            +":"+str(dk).zfill(2)+":"
            +str(sn).zfill(2),
            font =("Times New Roman", 50, "bold"))
    time.sleep(1)
    sn+= 1
     
    if sn == 60:
        sn = 0
        dk+= 1
     
    if dk == 60:
        dk = 0
        sa+= 1
     
    if sa == 13:
        sa = 1