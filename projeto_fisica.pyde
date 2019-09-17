c_0 = sqrt(sq(370-130)+sq(720-480))
k=8
t0 = millis()
oldt = t0/1000.0
pontos = 0
def setup():
    size(1400,800)


def draw():
    global c_0, k, c
    background(225)
    movimento()
    display()
    movimento2()
    movimento3()
  #  grude()
        
def display():
    fill(1,1,1)
    rect(0, 740, 200 , 60)
    fill(70,130,180)
    #rect(150, 740 , 390, 740)
    line(150, 740 , 110,700)
    line(130, 720 , x1, y1)
    fill(250)
    rect(960+120, 500 , 5, 790)
    line(960, 790 , 960+120,500)
    line(960+250, 790 , 960+120+5,500)
    rect(960, 790 , 250, 740)
    ellipse(x1, y1, 50, 50)
    noFill()
    circle(960+120, 500, 450)

def movimento():
    global x1, y1, c_0, c
    c = map(mouseX, 0, width, 0, c_0)
    x1 = 130 + c/sqrt(2)
    y1 = 720 - c/sqrt(2)
    c_0 = sqrt(sq(370-130)+sq(720-480))
    
def movimento2():
    global x2,y2
    #if keyPressed == True:
        
    t = (millis()-t0)/1000.0  
    delta_x = c_0 - c
    v = sqrt(k*sq(delta_x)-2*50*(y1))
    vx=v*sqrt(2)/2
    vy=-(vx-50*t)
    x2 = (x1 + vx*t)
    y2 = (y1 + vy*t+ 25*t*t)
    fill(0,255,127)
    ellipse(x2, y2, 50, 50)
    text("x2 e {}, y2 e {}, v e {},vx e {}, vy e {},t e {}".format(x2,y2,v,vx,vy,t), 200,200)
    delta_x = c_0 - c
    
def movimento3():
    global cad1_x, cad1_y, cad2_x, cad2_y, cad3_x, cad3_y, cad4_x, cad4_y
    t = (millis()-t0)/1000.0
    fill(139,0,139)
    cad1_x = 1080 + 225*cos(t) -25
    cad1_y = 500 + 225*sin(t) - 25
    rect(cad1_x, cad1_y ,50, 50)
    
    cad2_x = 1080 + 225*cos(PI/2+t) -25
    cad2_y = 500 + 225*sin(PI/2+t) - 25
    rect(cad2_x, cad2_y ,50, 50)
    
    cad3_x = 1080 + 225*cos(PI+t) -25
    cad3_y = 500 + 225*sin(PI+t) - 25
    rect(cad3_x, cad3_y ,50, 50)
    
    cad4_x = 1080 + 225*cos(3*PI/2+t) -25
    cad4_y = 500 + 225*sin(3*PI/2+t) - 25
    rect(cad4_x, cad4_y ,50, 50)

#def grude():
#    global x2,y2,cad1_x,cad1_y,cad2_x,cad2_y,cad3_x,cad3_y,cad4_x,cad4_y
#    text("SUA PONTUACAO E {}".format(pontos), 400,400)
#    if x2 == cad1_x and y2 == cad1_y:
#        pontos+=1
#    elif x2 == cad2_x and y2 == cad2_y:
#        pontos+=1
#    elif x2 == cad3_x and y2 == cad3_y:
#        pontos+=1
#    else x2 == cad4_x and y2 == cad4_y:
#        pontos+=1
                
        

        
def mouseClicked():
  global oldt, t0
  t0 = millis()
  oldt = t0/1000.0
