#import module_manager
#module_manager.review()

#import Leap, sys, thread, time 
import random, math
import os, sys, inspect, thread, time
sys.path.insert(0, "C:\Users\ahanamukhopadhyay\Downloads\LeapDeveloperKit_2.3.1+31549_mac\LeapSDK\lib/x86")

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture


from Tkinter import *

class Pod(object):
    #Model
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.fill = "green"
    
    #View 
    def draw(self,canvas):
        x1 = self.cx - 30
        x2 = self.cx + 30
        y1 = self.cy - 10
        y2 = self.cy + 10
        r = 5
        points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
        canvas.create_polygon(points, smooth = True, fill = "green3", outline = "black", width = 2)
        
    # def __repr__(self):
    #     return "normal pod"
    
class WithSpring(Pod):
    def draw(self,canvas):
        x1 = self.cx - 30
        x2 = self.cx + 30
        y1 = self.cy - 10
        y2 = self.cy + 10
        r = 5
        points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
        canvas.create_polygon(points, smooth = True, fill = "green3", outline = "black", width = 2)
        x = (x1 + x2) // 2
        canvas.create_oval(x - 5, y1 - 8, x + 10, y1)
        canvas.create_oval(x - 5, y1 - 10, x + 10, y1 - 2)
        canvas.create_oval(x - 5, y1 - 12, x + 10, y1 - 4)
        canvas.create_oval(x - 5, y1 - 14, x + 10, y1 - 6)        
        
class BreakingPod(Pod):
    def __init__(self, cx, cy):
        super().__init__(cx,cy)
    
    def draw(self,canvas):
        x1 = self.cx - 30
        x2 = self.cx + 30
        y1 = self.cy - 10
        y2 = self.cy + 10
        r = 5
        points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
        canvas.create_polygon(points, smooth = True, fill = "brown", outline = "black", width = 2)
        
        crackP = (self.cx - 2, self.cy - 10, self.cx + 2, self.cy - 10, self.cx, self.cy, self.cx - 3, self.cy + 2, self.cx + 2, self.cy + 10, self.cx  - 2, self.cy + 10, self.cx - 7, self.cy + 2, self.cx - 5, self.cy)
        canvas.create_polygon(crackP, fill = "white")

class MovingPod(Pod):
    def __init__(self,cx,cy):
        super().__init__(cx,cy)
        self.speed = 5
        self.direction = 1
    
    def draw(self,canvas):
        x1 = self.cx - 30
        x2 = self.cx + 30
        y1 = self.cy - 10
        y2 = self.cy + 10
        r = 5
        points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
        canvas.create_polygon(points, smooth = True, fill = "blue", outline = "black", width = 2)
    
    def move(self):
        self.cx += self.speed * self.direction
    
    def isHittingSide(self, width, height):
        return (self.cx - 30 <= 0 or self.cx + 30 >= width)
               
    def change(self):
        self.direction *= -1
    
##

#THIS NEEDS TO GET CALLED AS PART OF THE LEAP MOTION 
class Ball(object):
    def __init__(self,cx,cy):
        self.cx = cx
        self.cy = cy
        self.speed = 30
        
    def draw(self,canvas):
        canvas.create_oval(self.cx - 5, self.cy - 5, self.cx + 5, self.cy + 5, fill = "IndianRed1", outline = "black")
    
    def shootBall(self):
        self.cy -= self.speed
        print(self.cy)
        
    def onScreen(self):
        return(self.cy >= 0)

##      
        
#Model
class Dude(object):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.speed = 50
        
    def draw(self, canvas):
        r = 50/2
        #yellow circle body
        canvas.create_oval(self.cx-r, self.cy-r, self.cx+r, self.cy+r, fill = "gold", outline = "gold")
        #yellow rectangle body
        canvas.create_rectangle(self.cx-r, self.cy,self.cx+r, self.cy+r, fill = "gold", outline = "gold")
        #green pantS
        canvas.create_rectangle(self.cx-r, self.cy+r,self.cx+r, self.cy+2*r, fill = "green", outline = "black")
        canvas.create_line(self.cx-r, self.cy+r+r/3,self.cx+r, self.cy+r+r/3)
        canvas.create_line(self.cx-r, self.cy+r+2*r/3,self.cx+r, self.cy+r+2*r/3)
        #legs
        margin = 5
        legDiff = (2*r-2*margin)//3
        for leg in range(4):
            x1 = self.cx-r+margin+legDiff*leg
            x2 = x1 + 4
            y1 = self.cy+2*r
            y2 = self.cy+2*r + 10
            canvas.create_line(x1, y1, x1, y2, width = 2)
            canvas.create_line(x1, y2, x2, y2, width = 2)
        #rectangle and circle nose
        nose = 10
        canvas.create_rectangle(self.cx+r, self.cy-nose/4,self.cx+r+8, self.cy+nose/4, fill = "gold", outline ="gold")
        centerX = self.cx+r+8
        centerY = self.cy
        noseR = nose/4
        canvas.create_oval(centerX-noseR, centerY-noseR, centerX+noseR, centerY+noseR, fill = "gold", outline = "gold")
        #two eyes
        canvas.create_oval(self.cx+6, self.cy-3, self.cx+8, self.cy, fill = "black")
        canvas.create_oval(self.cx+15, self.cy-3, self.cx+17, self.cy, fill = "black")
        


class LeftDude(Dude):
    def draw(self, canvas):
        r = 50/2
        #yellow circle body
        canvas.create_oval(self.cx-r, self.cy-r, self.cx+r, self.cy+r, \
        fill = "gold", outline = "gold")
        #yellow rectangle body
        canvas.create_rectangle(self.cx-r, self.cy,self.cx+r, self.cy+r, fill = "gold", outline = "gold")
        #green pants
        canvas.create_rectangle(self.cx-r, self.cy+r,self.cx+r, self.cy+2*r, fill = "green", outline = "black")
        canvas.create_line(self.cx-r, self.cy+r+r/3,self.cx+r, self.cy+r+r/3)
        canvas.create_line(self.cx-r, self.cy+r+2*r/3,self.cx+r, self.cy+r+2*r/3)
        #legs
        margin = 5
        legDiff = (2*r-2*margin)//3
        for leg in range(4):
            x1 = self.cx-r+margin+legDiff*leg
            x2 = x1 - 4
            y1 = self.cy+2*r
            y2 = self.cy+2*r + 10
            canvas.create_line(x1, y1, x1, y2, width = 2)
            canvas.create_line(x1, y2, x2, y2, width = 2)
        #rectangle and circle nose
        nose = 10
        canvas.create_rectangle(self.cx-r, self.cy-nose/4,self.cx-r-8, self.cy+nose/4, fill = "gold", outline ="gold")
        centerX = self.cx-r-8
        centerY = self.cy
        noseR = nose/4
        canvas.create_oval(centerX-noseR, centerY-noseR, centerX+noseR, \
        centerY+noseR, fill = "gold", outline = "gold")
        #two eyes
        canvas.create_oval(self.cx-6, self.cy-3, self.cx-8, self.cy, fill = "black")
        canvas.create_oval(self.cx-15, self.cy-3, self.cx-17, self.cy, fill = "black")

class UpDude(Dude):
    def draw(self, canvas):
        r = 50/2
        #yellow circle body
        canvas.create_oval(self.cx-r, self.cy-r, self.cx+r, self.cy+r, \
        fill = "gold", outline = "gold")
        #yellow rectangle body
        canvas.create_rectangle(self.cx-r, self.cy,self.cx+r, self.cy+r, \
        fill = "gold", outline = "gold")
        #green pants
        canvas.create_rectangle(self.cx-r, self.cy+r,self.cx+r, self.cy+2*r, \
        fill = "green", outline = "black")
        canvas.create_line(self.cx-r, self.cy+r+r/3,self.cx+r, self.cy+r+r/3)
        canvas.create_line(self.cx-r, self.cy+r+2*r/3,self.cx+r, self.cy+r+2*r/3)
        #legs
        margin = 5
        legDiff = (2*r-2*margin)//3
        for leg in range(4):
            x1 = self.cx-r+margin+legDiff*leg
            y1 = self.cy+2*r
            y2 = self.cy+2*r + 10
            canvas.create_line(x1, y1, x1, y2, width = 2)
        #rectangle and circle nose
        nose = 10
        canvas.create_rectangle(self.cx-nose/4, self.cy-r, self.cx+nose/4, self.cy-r-8, fill = "gold", outline = "gold")
        centerX = self.cx
        centerY = self.cy-r-8
        noseR = nose/4
        canvas.create_oval(centerX-noseR, centerY-noseR, centerX+noseR, \
        centerY+noseR, fill = "gold", outline = "gold")
        #two eyes
        canvas.create_oval(self.cx-6, self.cy-10, self.cx-4, self.cy-7, fill = "black")
        canvas.create_oval(self.cx+4, self.cy-10, self.cx+6, self.cy-7, fill = "black")
    
    # def podParameter(self):
    #     pass
    #     
    # def hitPod(self,other):
    #     if(not isinstance(other, Pod)): # Other must be an Pod
    #         return False
    #     else:
    #         #check if dude is hitting Pod
    #         pass
    # 
    # def landPod(self,other):
    #     # if '''coordinate of legs''' >= other.cy + 10:
    #     #     '''coordinate of legs''' = other.cy + 10
    #     pass
    #         
    # 
    # def jumping(self,other):
    #     if hitPod(self,other):
    #         #jump!
    #         pass


##
class Monster(object):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        
    def draw(self, canvas):
        #main shape
        r = 35
        coord = self.cx - r/2,self.cy+100, self.cx+r/2, self.cy+40
        canvas.create_arc(coord, start=0, extent=180, fill="dodger blue", outline = "black", width = 4)
        #teeth with lines
        canvas.create_rectangle(self.cx, self.cy+61, self.cx+3, self.cy+55, fill = "violet")
        canvas.create_line(self.cx+3, self.cy+61, self.cx+3, self.cy+55, fill = "black")
        canvas.create_rectangle(self.cx+3, self.cy+61, self.cx+6, self.cy+55, fill = "violet")
        canvas.create_line(self.cx+6, self.cy+61, self.cx+6, self.cy+55, fill = "black")
        canvas.create_rectangle(self.cx+6, self.cy+61, self.cx+9, self.cy+55, fill = "violet")
        canvas.create_line(self.cx+9, self.cy+61, self.cx+9, self.cy+55, fill = "black")
        canvas.create_rectangle(self.cx+9, self.cy+61, self.cx+12, self.cy+55, fill = "violet")
        canvas.create_line(self.cx+12, self.cy+61, self.cx+12, self.cy+55, fill = "black")
        eyeX = self.cx + 4
        eyeY = self.cy +50
        #draws eye
        canvas.create_oval(eyeX-2, eyeY-2, eyeX+3, eyeY+3, fill = "yellow")
        #draws hair spikes
        canvas.create_line(self.cx, self.cy+40, self.cx, self.cy+30)
        canvas.create_line(self.cx-3, self.cy+41, self.cx-4, self.cy+30)
        canvas.create_line(self.cx+3, self.cy+41, self.cx+4, self.cy+30)
        canvas.create_line(self.cx-6, self.cy+42, self.cx-8, self.cy+32)
        canvas.create_line(self.cx+6, self.cy+42, self.cx+8, self.cy+32)
        #draw two legs
        margin = 5
        legX = self.cx - r/2 + margin
        y1 = self.cy+100
        y2 = self.cy+110
        canvas.create_line(legX + r/2, self.cy+70, legX+r/2, self.cy+80, fill = "dodger blue", width = 3)
        canvas.create_line(legX, self.cy+70, legX, self.cy+80, fill = "dodger blue", width = 3)
        canvas.create_line(legX + r/2, self.cy+80, legX+r/2+7, self.cy+80, fill = "dodger blue", width = 3)
        canvas.create_line(legX, self.cy+80, legX+7, self.cy+80, fill = "dodger blue", width = 3)
    
    def move(self):
        x = random.randint(0,2)
        directionX = random.choice([-1,1])
        self.cx += x * directionX
        y = random.randint(0,2)
        directionY = random.choice([-1,1])
        self.cy += y * directionY

        
    
class RedMonster(Monster):
    def draw(self, canvas):
        xr = 40
        yr = 35
        #spikes
        angle = 0
        r = xr * 2/3
        for i in range(16):
            canvas.create_line(self.cx, self.cy, self.cx + r*math.cos(angle), self.cy + r*math.sin(angle))
            angle += math.radians(360/16)
        #main oval
        canvas.create_oval(self.cx - xr/2, self.cy - yr/2, self.cx + xr/2, self.cy + yr/2, fill = "tomato", width = 3)
        xrDif = xr/5
        #three yellow dots
        canvas.create_oval(self.cx - xr/2 + 5, self.cy - 3, self.cx - xr/2 + 5 + xrDif, self.cy + 5, fill = "gold", width = 2)
        canvas.create_oval(self.cx - xr/2 + 2*xrDif+1, self.cy - 10, self.cx - xr/2 + 3*xrDif+1, self.cy-2, fill = "gold", width = 2)
        canvas.create_oval(self.cx + xr/2 - 5 - xrDif, self.cy - 3, self.cx + xr/2 - 5, self.cy + 5, fill = "gold", width = 2)
        #eyes inside yellow dots
        canvas.create_oval(self.cx - xr/2 + 5+xrDif/2-1, self.cy - 1, self.cx - xr/2 + 5 + xrDif/2+1, self.cy + 1, fill = "black")
        canvas.create_oval(self.cx - xr/2 + 2*xrDif+1+xrDif/2-1, self.cy - 7, self.cx - xr/2 + 2*xrDif+1+xrDif/2+1, self.cy-6, fill = "black", width = 2)
        canvas.create_oval(self.cx + xr/2 - 5 - xrDif/2-1, self.cy, self.cx + xr/2 - 5 - xrDif/2-1, self.cy+1, fill = "black", width = 2)
        #two eyes
        canvas.create_oval(self.cx-3, self.cy+1, self.cx-1, self.cy + 4, fill = "gold", width = 2)
        canvas.create_oval(self.cx+2, self.cy+1, self.cx+4, self.cy + 4, fill = "gold", width = 2)
        #line
        canvas.create_line(self.cx-xr/2+3, self.cy+8, self.cx+xr/2-3, self.cy+8, width = 2)



####################################
# customize these functions
####################################


def init(data):
    #graphics data
    data.pods = []
    data.monsters = []
    data.timerCalls = 0
    data.rows = 26
    data.cols = 20
    data.ball = None
    data.location = []
    data.shootingBall = False
    data.x = 0
    data.y = 0 #ball coordinates when starts shooting
    data.dudeMode = "normal"
    data.dudeX = data.width//2
    data.dudeY = data.height - 210
    data.dude = Dude(data.dudeX,data.dudeY)
    data.speed = 50

    #leap motion data
    data.secs = 0
    data.blockCoords = []
    data.tipPos = 0
    data.controller = Leap.Controller()
    data.frame = data.controller.frame()
    data.fingerNames = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    data.boneNames = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    data.currDir = "Right"

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    #leap motion code
    if data.timerDelay % 10 == 0:
        data.secs += 1
    updateLeapMotionData(data)
    printLeapMotionData(data)
    
    #animation code
    data.timerCalls += 1
    if data.timerCalls % 10 == 0:
        cx = random.randint(30,470)
        cy = random.randint(10,640)
        newPod = Pod(cx,cy)
        data.pods.append(newPod)
    if data.timerCalls % 20 == 0:
        cx = random.randint(30,470)
        cy = random.randint(10,640)
        newBPod = BreakingPod(cx,cy)
        data.pods.append(newBPod)
    if data.timerCalls % 30 == 0:
        cx = random.randint(30,470)
        cy = random.randint(10,640)
        newSPod = WithSpring(cx,cy) 
        data.pods.append(newSPod)
    if data.timerCalls % 50 == 0:
        cx = random.randint(30,470)
        cy = random.randint(10,640)
        newMPod = MovingPod(cx,cy)
        data.pods.append(newMPod)
    if data.timerCalls % 50 == 0:
        cx = random.randint(30,470)
        cy = random.randint(10,640)
        newMonster = Monster(cx,cy)
        data.monsters.append(newMonster)
    if data.timerCalls % 50 == 0:
        cx = random.randint(30,470)
        cy = random.randint(10,640)
        newMonster = RedMonster(cx,cy)
        data.monsters.append(newMonster)
    for pods in data.pods:
        if isinstance(pods,MovingPod):
            pods.move()
            if pods.isHittingSide(data.width,data.height):
                pods.change()
    for monster in data.monsters:
        monster.move()
    
    # if data.shootingBall == False:
    #     data.location.append((data.dudeX, data.dudeY))
    # elif data.shootingBall == True:
    #     i = len(data.location) - 1
    #     (data.x,data.y) = data.location[i]
    #     data.ball = Ball(data.x,data.y)
    # if data.y != 0:
    #     data.y -= 30
    #     if not data.ball.onScreen():
    #         data.shootingBall == False
    #         data.ball = None
    #         data.y = 0
    
    # ##################SHOOTING BALL
    
    # if data.shootingBall == True:
    #     for ball in data.ball:
    #         if ball.onScreen() == True:
    #             ball.shootBall()
    #         else: 
    #             data.ball.remove(ball)
    #             data.shootingBall = False
    #             data.ball.append(Ball(data.dudeX, data.dudeY))
    
    # if data.shootingBall == True:
    #     data.dudeMode = "shoot"    

    
    data.dudeY += data.speed
    g = 10 #gravity acceleration 
    data.speed -= g
    if data.speed < -50:
        data.speed = 50


def updateLeapMotionData(data):
    data.frame = data.controller.frame()

def printLeapMotionData(data):
    frame = data.frame
    data.controller.config.set("Gesture.Circle.MinRadius", 2)
    data.controller.config.set("Gesture.Circle.MinArc", .1)
    data.controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
    data.controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
    data.controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
    data.controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)
    data.controller.config.set("Gesture.Swipe.MinLength", 100)
    data.controller.config.set("Gesture.Swipe.MinVelocity", 500)
    
    mostForwardOnHand = frame.hands[0].fingers.frontmost
    #position of hand
    data.tipPos = (mostForwardOnHand.tip_position[0], \
    mostForwardOnHand.tip_position[1])
    #position of block
    blockPos = (data.tipPos[0]+300, data.height-data.tipPos[1]*1.1,\
    data.tipPos[0]+5, data.height-data.tipPos[1]*1.1, data.secs)
    

    # Get hands
    prevPos = 0.5
    for hand in frame.hands:
        if hand.grab_strength != prevPos and hand.grab_strength == 1.0:
            print hand.grab_strength
            data.blockCoords.append(blockPos)
            break
        prevPos = hand.grab_strength

        handType = "Left hand" if hand.is_left else "Right hand"

        
        #print "here", hand.palm_position[0]
        if hand.palm_position[0] > 0: 
            data.dir = "right"
            #print "right"
        else:
            data.dir = "left"
            #print "left"
    
            
        # Get the hand's normal vector and direction
        normal = hand.palm_normal
        direction = hand.direction


def getCellBounds(row,col,data):
    columnWidth = data.width / data.cols
    rowHeight = data.height / data.rows
    x0 = col * columnWidth
    x1 = (col+1) * columnWidth
    y0 = row * rowHeight
    y1 = (row+1) * rowHeight
    return (x0, y0, x1, y1)    

def redrawAll(canvas, data):
    '''#floating block
    canvas.create_line(data.tipPos[0]+300, data.height \
    data.tipPos[1],data.tipPos[0]+320, data.height-data.tipPos[1])
    prevSecs = 0
    for i in data.blockCoords:
        if i[4] - prevSecs > 1:
            canvas.create_line(i[0], i[1], i[2], i[3])
        prevSecs = i[4]'''
        
    #background
    canvas.create_rectangle(0,0,data.width,data.height, fill = "old lace")
    #grid
    for row in range(data.rows):
        for col in range(data.cols):
            (x0, y0, x1, y1) = getCellBounds(row, col, data)
            canvas.create_rectangle(x0, y0, x1, y1, outline = "gold")
    
    for pods in data.pods:
        pods.draw(canvas)
        
    for monster in data.monsters:
        monster.draw(canvas)
    
    if data.shootingBall == True and data.ball != None:
        data.ball.draw(canvas)
            
    if data.dudeMode == "normal":
        data.dude = Dude(data.dudeX,data.dudeY)
        data.dude.draw(canvas)
    
    elif data.dudeMode == "left":
        data.dude = LeftDude(data.dudeX, data.dudeY)
        data.dude.draw(canvas)
    
    elif data.dudeMode == "shoot":
        data.dude = UpDude(data.dudeX, data.dudeY)
        data.dude.draw(canvas)

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    if event.keysym == "Left":
        data.dudeX -= 5
        data.dudeMode = "left"
    elif event.keysym == "Right":
        data.dudeX += 5
        data.dudeMode = "normal"
    elif event.keysym == "space":
        data.shootingBall = True

        
        
####################################
# use the run function as-is
####################################


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(500, 650)
