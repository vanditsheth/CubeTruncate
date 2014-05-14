#Cube using primitives and truncation
#Made by:- Vandit Sheth

import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

#Flag for mode switching
flag=0

#Here the value of sets how deep th cut will be
a = 1
b = 0.3
c = a - b

#Setting defaults for rotation and truncation
press = 0
press1 = 0
xrot = 0.0
yrot = 0.0
zrot = 0.0

#Setting all the vertices(including the ones introduced on truncation)
v0 = [0,0,0]
v1 = [a,0,0]
v2 = [0,a,0]
v3 = [a,a,0]
v4 = [0,0,a]
v5 = [a,0,a]
v6 = [0,a,a]
v7 = [a,a,a]

v01 = [b,0,0]
v02 = [0,b,0]
v04 = [0,0,b]

v10 = [c,0,0]
v13 = [a,b,0]
v15 = [a,0,b]

v20 = [0,c,0]
v23 = [b,a,0]
v26 = [0,a,b]

v31 = [a,c,0]
v32 = [c,a,0]
v37 = [a,a,b]

v40 = [0,0,c]
v45 = [b,0,a]
v46 = [0,b,a]

v51 = [a,0,c]
v54 = [c,0,a]
v57 = [a,b,a]

v62 = [0,a,c]
v64 = [0,c,a]
v67 = [b,a,a]

v73 = [a,a,c]
v75 = [a,c,a]
v76 = [c,a,a]

#Front Face (which vertexes to include is decided based on press number)
def face0():
   glBegin(GL_LINE_LOOP)
   if press>=8:
           glVertex3fv(v02)
   else:
           glVertex3fv(v0)
   if press>=7:
           glVertex3fv(v13)
   else:
           glVertex3fv(v1)
   if press>=5:
           glVertex3fv(v31)
   else:
           glVertex3fv(v3)
   if press>=6:
           glVertex3fv(v20)
   else:
           glVertex3fv(v2)
   glEnd()

#Left side Face (which vertexes to include is decided based on press number)
def face1():
   glBegin(GL_LINE_LOOP)
   if press>=8:
           glVertex3fv(v04)
           glVertex3fv(v02)
   else:
           glVertex3fv(v0)
   if press>=6:
           glVertex3fv(v20)
           glVertex3fv(v26)
   else:
           glVertex3fv(v2)
   if press>=2:
           glVertex3fv(v62)
           glVertex3fv(v64)
   else:
           glVertex3fv(v6)
   if press>=4:
           glVertex3fv(v46)
           glVertex3fv(v40)
   else:
           glVertex3fv(v4)
   glEnd()

#Bottom face (which vertexes to include is decided based on press number)
def face2():
   glBegin(GL_LINE_LOOP)
   if press>=8:
           glVertex3fv(v04)
   else:
           glVertex3fv(v0)
   if press>=7:
           glVertex3fv(v15)
   else:
           glVertex3fv(v1)
   if press>=3:
           glVertex3fv(v51)
   else:
           glVertex3fv(v5)
   if press>=4:
           glVertex3fv(v40)
   else:
           glVertex3fv(v4)
   glEnd()

#Back Face (which vertexes to include is decided based on press number)
def face3():
   glBegin(GL_LINE_LOOP)
   if press>=1:
           glVertex3fv(v75)
   else:
           glVertex3fv(v7)
   if press>=2:
           glVertex3fv(v64)
   else:
           glVertex3fv(v6)
   if press>=4:
           glVertex3fv(v46)
   else:
           glVertex3fv(v4)
   if press>=3:
           glVertex3fv(v57)
   else:
           glVertex3fv(v5)
   glEnd()

#Right Side Face (which vertexes to include is decided based on press number)
def face4():
   glBegin(GL_LINE_LOOP)
   if press>=1:
           glVertex3fv(v73)
           glVertex3fv(v75)
   else:
           glVertex3fv(v7)
   if press>=3:
           glVertex3fv(v57)
           glVertex3fv(v51)
   else:
           glVertex3fv(v5)
   if press>=7:
           glVertex3fv(v15)
           glVertex3fv(v13)
   else:
           glVertex3fv(v1)
   if press>=5:
           glVertex3fv(v31)
           glVertex3fv(v37)
   else:
           glVertex3fv(v3)
   glEnd()

#Top Face (which vertexes to include is decided based on press number)
def face5():
   glBegin(GL_LINE_LOOP)
   if press>=1:
           glVertex3fv(v73)
   else:
           glVertex3fv(v7)
   if press>=2:
           glVertex3fv(v62)
   else:
           glVertex3fv(v6)
   if press>=6:
           glVertex3fv(v26)
   else:
           glVertex3fv(v2)
   if press>=5:
           glVertex3fv(v37)
   else:
           glVertex3fv(v3)
   glEnd()

#Front Face (which vertexes to include is decided based on press number)
def face01():
   glBegin(GL_LINE_LOOP)
   if press1>=8:
           glVertex3fv(v02)
           glVertex3fv(v01)
   else:
           glVertex3fv(v0)
   if press1>=7:
           glVertex3fv(v10)
           glVertex3fv(v13)
   else:
           glVertex3fv(v1)
   if press1>=5:
           glVertex3fv(v31)
           glVertex3fv(v32)
   else:
           glVertex3fv(v3)
   if press1>=6:
           glVertex3fv(v23)
           glVertex3fv(v20)
   else:
           glVertex3fv(v2)
   glEnd()
   
#Left Side Face (which vertexes to include is decided based on press number)
def face11():
   glBegin(GL_LINE_LOOP)
   if press1>=8:
           glVertex3fv(v04)
           glVertex3fv(v02)
   else:
           glVertex3fv(v0)
   if press1>=6:
           glVertex3fv(v20)
           glVertex3fv(v26)
   else:
           glVertex3fv(v2)
   if press1>=2:
           glVertex3fv(v62)
           glVertex3fv(v64)
   else:
           glVertex3fv(v6)
   if press1>=4:
           glVertex3fv(v46)
           glVertex3fv(v40)
   else:
           glVertex3fv(v4)
   glEnd()
   
#Bottom Face (which vertexes to include is decided based on press number)
def face21():
   glBegin(GL_LINE_LOOP)
   if press1>=8:
           glVertex3fv(v04)
           glVertex3fv(v01)
   else:
           glVertex3fv(v0)
   if press1>=7:
           glVertex3fv(v10)
           glVertex3fv(v15)
   else:
           glVertex3fv(v1)
   if press1>=3:
           glVertex3fv(v51)
           glVertex3fv(v54)
   else:
           glVertex3fv(v5)
   if press1>=4:
           glVertex3fv(v45)
           glVertex3fv(v40)
   else:
           glVertex3fv(v4)
   glEnd()

#Back Face (which vertexes to include is decided based on press number)
def face31():
   glBegin(GL_LINE_LOOP)
   if press1>=1:
           glVertex3fv(v75)
           glVertex3fv(v76)
   else:
           glVertex3fv(v7)
   if press1>=2:
           glVertex3fv(v67)
           glVertex3fv(v64)
   else:
           glVertex3fv(v6)
   if press1>=4:
           glVertex3fv(v46)
           glVertex3fv(v45)
   else:
           glVertex3fv(v4)
   if press1>=3:
           glVertex3fv(v54)
           glVertex3fv(v57)
   else:
           glVertex3fv(v5)
   glEnd()

#Right Side Face (which vertexes to include is decided based on press number)
def face41():
   glBegin(GL_LINE_LOOP)
   if press1>=1:
           glVertex3fv(v73)
           glVertex3fv(v75)
   else:
           glVertex3fv(v7)
   if press1>=3:
           glVertex3fv(v57)
           glVertex3fv(v51)
   else:
           glVertex3fv(v5)
   if press1>=7:
           glVertex3fv(v15)
           glVertex3fv(v13)
   else:
           glVertex3fv(v1)
   if press1>=5:
           glVertex3fv(v31)
           glVertex3fv(v37)
   else:
           glVertex3fv(v3)
   glEnd()

#Top Face (which vertexes to include is decided based on press number)
def face51():
   glBegin(GL_LINE_LOOP)
   if press1>=1:
           glVertex3fv(v73)
           glVertex3fv(v76)
   else:
           glVertex3fv(v7)
   if press1>=2:
           glVertex3fv(v67)
           glVertex3fv(v62)
   else:
           glVertex3fv(v6)
   if press1>=6:
           glVertex3fv(v26)
           glVertex3fv(v23)
   else:
           glVertex3fv(v2)
   if press1>=5:
           glVertex3fv(v32)
           glVertex3fv(v37)
   else:
           glVertex3fv(v3)
   glEnd()

#cube and cube1 act as data structure abstractions as faces are defined inside them
#Cube for rectangle truncate mode
def cube():
   face0()
   face1()
   face2()
   face3()
   face4()
   face5()

#Cube for triangle truncate mode
def cube1():
   face01()
   face11()
   face21()
   face31()
   face41()
   face51()

def display():
   global flag
   glClear (GL_COLOR_BUFFER_BIT)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   glFrustum(-1.0, 1.0, -1.0, 1.0, 1, 5.0)
   glMatrixMode(GL_MODELVIEW)

   glLoadIdentity()              
   gluLookAt (0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

   glColor3f (1.0, 1.0, 1.0)

   #Rotating the cube in all 3 directions
   glRotatef(xrot, 1.0, 0.0, 0.0)
   glRotatef(yrot, 0.0, 1.0, 0.0)
   glRotatef(zrot, 0.0, 0.0, 1.0)
   glTranslatef(-0.5, -0.5, -0.5)

   #Making cube based on the mode
   if(flag==0):
       cube()
   else:
       cube1()
       
   glFlush ()

def keyboard(key, x, y):
   global press, press1, flag, xrot, yrot, zrot

   #Quit on Esc
   if key == chr(27):
      import sys
      sys.exit(0)

   #Cube rotation in x-direction
   elif key == 'z':
      xrot = xrot - 10.0
   elif key == 'Z':
      xrot = xrot + 10.0

   #Cube rotation in y-direction
   elif key == 'x':
      yrot = yrot - 10.0
   elif key == 'X':
      yrot = yrot + 10.0

   #Cube rotation in z-direction
   elif key == 'c':
      zrot = zrot - 10.0
   elif key == 'C':
      zrot = zrot + 10.0

   #Incrementing key press to cut the edge/vertex of the cube(decided based on mode)
   elif key == 'a':
      if press1 < 8 and flag==1:
              press1 = press1 + 1.0
      if press < 8 and flag==0:
              press = press + 2.0
   elif key == 'A':
      if press1 > 0 and flag==1:
              press1 = press1 - 1.0
      if press > 0 and flag==0:
              press = press - 2.0

   #Mode swithcing
   elif key == 's':
       press = 0
       press1 = 0
       if(flag==0):
           flag=1
       else:
           flag=0
        
   glutPostRedisplay()   

glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (500, 500)
glutInitWindowPosition (0, 0)
glutCreateWindow ('Cube Edge/Corner Truncate')
glClearColor(0.0,0.0,0.0,0.0)
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMainLoop()
