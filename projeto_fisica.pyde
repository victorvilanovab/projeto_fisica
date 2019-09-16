c_0 = sqrt(sq(370-130)+sq(720-480))
k=8
t0 = millis()
oldt = t0/1000.0

def setup():
    size(1400,800)


def draw():
    global c_0, k, c
    background(225)
    t0 = millis()
    movimento()
    display()
    movimento2()
    

        
def display():
    fill(1,1,1)
    rect(0, 740, 1400, 60)
    fill(255,0,0)
    triangle(150, 740 , 390, 740, 390,500)
    line(150, 740 , 110,700)
    line(130, 720 , x1, y1)
    fill(250,0,230)
    ellipse(x1, y1, 50, 50)

def movimento():
    global x1, y1, c_0, c
    c = map(mouseX, 0, width, 0, c_0)
    x1 = 130 + c/sqrt(2)
    y1 = 720 - c/sqrt(2)
    c_0 = sqrt(sq(370-130)+sq(720-480))
    
def movimento2():
    if keyPressed == True:
        
        t = (millis()-t0)/1000.0  
        delta_x = c_0 - c
        v = sqrt(k*sq(delta_x)-2*10*(y1))
        vx=v*sqrt(2)/2
        vy=-(vx-10*t)
        x2 = (x1 + vx*t)
        y2 = (y1 + vy*t+ 5*t*t)
        fill(250,0,230)
        ellipse(x2, y2, 50, 50)
        text("x2 e {}, y2 e {}, v e {},vx e {}, vy e {},t e {}".format(x2,y2,v,vx,vy,t), 200,200)
        delta_x = c_0 - c
        oldt = t
        
def mouseClicked():
  global oldt, t0
  t0 = millis()
  oldt = t0/1000.0
    
