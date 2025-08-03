from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


raindrops = []
W_Width, W_Height = 750,750
shift = 0
drop=0



def generate_raindrops():
    global raindrops, shift
    glutPostRedisplay()
    
    if random.random() < 0.5:  
        raindrops.append([random.randint(-1500, 2000), 1000])
    # if random.random() < 0.4:
        # raindrops.append([random.randint(0,-750), random.randint(500,750)])

    for i in raindrops:
        i[0]+=shift

    new_raindrops = []
    for i in raindrops:
        i[1] -= 3  # Adjust the speed of the raindrops 
        if i[1] > -250:
            new_raindrops.append(i)
    raindrops = new_raindrops
    return raindrops



background_color = False

def keyboardListener(key, x, y):
    global background_color, raindrops
    if key == b'd':
        background_color = True
        print("Background Color: DAY")

    elif key == b'n':
        background_color = False
        print("Background Color: NIGHT")

    glutPostRedisplay()



def specialKeyListener(key, x, y):
    global raindrops,shift,drop

    if key == GLUT_KEY_RIGHT:

        shift+=.1
        drop+=1

        print("rain right")

    if key == GLUT_KEY_LEFT:

        shift-=.1
        drop-=1

        print("rain left")

    glutPostRedisplay()





def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    if background_color:
        glClearColor(1, 1, 1, 1)  # background White 
    else:
        glClearColor(0, 0, 0, 0)  # background Black 
        

    


    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)

    # drawAxes()
    # global ballx, bally, ball_size
    # draw_points(ballx, bally, ball_size)
    # drawShapes()

    

    glLineWidth(10)
    glBegin(GL_LINES)   
    glColor3f(0, 1, 0)     #color of the hous
    glVertex2d(150,40)
    glVertex2d(-150,40)
    
    glVertex2d(-150,40)
    glVertex2d(-150,-80)

    glVertex2d(150,40)
    glVertex2d(150,-80)

    glVertex2d(150,-80)
    glVertex2d(-150,-80)
    glEnd()

    
    glBegin(GL_LINES)
    glVertex2d(-30,-10) 
    glVertex2d(-30,-80) # floor point left

    glVertex2d(30,-10) 
    glVertex2d(30,-80) # floor point right

    # color of the door
    glColor3f(1, 1, 0)

    # top door 
    glVertex2d(-30,-10) 
    glVertex2d(30,-10) 

    glColor3f(1, 1, 0)
    # door floor 
    glVertex2d(-30,-80) 
    glVertex2d(30,-80)  

    glEnd()



    
# left window
    glBegin(GL_LINES)    
    glVertex2d(-70,10)
    glVertex2d(-70,-30)
      
    glVertex2d(-110,10)
    glVertex2d(-110,-30)

    glVertex2d(-70,10)
    glVertex2d(-110,10)


    glVertex2d(-70,-30)
    glVertex2d(-110,-30)
    glEnd()

# right window
    glBegin(GL_LINES)    
    glVertex2d(70,10)
    glVertex2d(70,-30)

    glVertex2d(110,10)
    glVertex2d(110,-30)

    glVertex2d(70,10)
    glVertex2d(110,10)

    glVertex2d(70,-30)
    glVertex2d(110,-30)
    glEnd()


    # roof of house triangle
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(-150, 40)
    glVertex2d(150, 40)
    glVertex2d(0, 90)
    glEnd()


    glLineWidth(1) 
    
# for increase line wide i use glLineWidth(3) 

    # ===================================================
# Generate and render raindrops
    raindrops = generate_raindrops()  # adjust the number of raindrops
    global shift,drop
    raindrops = generate_raindrops()  # adjust the number of raindrops
    glBegin(GL_LINES)
    glColor3f(0, 0, 1)  # raindrops color 
    # print(raindrops)


    for x in raindrops:
        glVertex2f(x[0]+shift, x[1]+shift)
        glVertex2f(x[0]+drop+shift, x[1]-10+shift)
        # glVertex2f(x, y - length)
    glEnd()

    glutSwapBuffers()



# def animate():
#     #//codes for any changes in Models, Camera
#     glutPostRedisplay()
#     global ballx, bally,speed
#     ballx=(ballx+speed)%180
#     bally=(bally+speed)%180

def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"Home")
init()

glutDisplayFunc(display)	#display callback function
# glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)

glutMainLoop()		#The main loop of OpenGL
