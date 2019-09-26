from copy import deepcopy as copy
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
    x1, y1, c = movimento()
    display(x1,y1)
    x2, y2 = movimento2(x1,y1,c)
    cad1_x, cad1_y, cad2_x, cad2_y, cad3_x, cad3_y, cad4_x, cad4_y = movimento3()
    #grude(x2, y2, cad1_x, cad1_y, cad2_x, cad2_y, cad3_x, cad3_y, cad4_x, cad4_y )
    if cad1_x -25 <= x2 <= cad1_x + 25 and cad1_y -25 <= y2 <= cad1_y + 25:
        fill(0,200,0)
        ellipse(x2, y2, 150, 150)
    if cad2_x -25 <= x2 <= cad2_x + 25 and cad2_y -25 <= y2 <= cad2_y + 25:
        fill(0,200,0)
        ellipse(x2, y2, 150, 150)
    if cad3_x -25 <= x2 <= cad3_x + 25 and cad3_y -25 <= y2 <= cad3_y + 25:
        fill(0,200,0)
        ellipse(x2, y2, 150, 150)
    if cad4_x -25 <= x2 <= cad4_x + 25 and cad4_y -25 <= y2 <= cad4_y + 25:
        fill(0,200,0)
        ellipse(x2, y2, 150, 150)
    
       
def display(x1, y1):
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
    global c_0
    c = map(copy(mouseX), 0, width, 0, c_0)
    x1 = copy(130 + c/sqrt(2))
    y1 = copy(720 - c/sqrt(2))
    c_0 = sqrt(sq(370-130)+sq(720-480))
    return x1, y1, c
   
   
def movimento2(x1,y1,c):
    #if keyPressed == True:
       
    t = (millis()-t0)/1000.0  
    delta_x = c_0 - c
    v = sqrt(k*sq(delta_x)-2*50*(y1))
    vx=v*sqrt(2)/2
    vy=-(vx-50*t)
    x2 = (x1 + vx*t)
    y2 = (y1 + vy*t+ 25*t*t)
    fill(250,0,0)
    ellipse(x2, y2, 50, 50)
    text("x2 e {}, y2 e {}, v e {},vx e {}, vy e {},t e {}".format(x2,y2,v,vx,vy,t), 200,200)
    delta_x = c_0 - c
    return x2, y2
   
def movimento3():
    t = (millis()-t0)/1000.0
    fill(200,10,200)
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
    
    return cad1_x, cad1_y, cad2_x, cad2_y, cad3_x, cad3_y, cad4_x, cad4_y

               
       

       
def mouseClicked():
  global oldt, t0
  t0 = millis()
  oldt = t0/1000.0
