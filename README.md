CubeTruncate
============

Information file for Cube Generation and Truncation

This code creates a cube using primitives and then truncates it to form polyhedra.

The cube has been made using lines; making the entire cube face-by-face. Each face in turn is made line-by-line. While making each face, the truncation is taken into account and necessary vertices are added on each face to show truncation based on the value of press (or press1 in case of triangle truncation). The code truncates the cube in 2 ways:- edge truncation i.e. rectangle truncation and vertex truncation i.e triangle truncation.

Whenever the key is pressed for truncation, it is logged and new vertices are introduced during re-display. Then lines are drawn joining these vertices. Hence, triangle or rectangle truncation is obtained. Initially the cube is in edge truncation mode. This can be switched to vertex truncation mode anytime by mode switch key(controls listed below)

The modules in the function are:
face0, face1, face2, face3, face4, face5 which are the modules making the faces of edge truncated cube. These modules contain the points that will be added on truncation. Similarly, there are face01, face11, face21, face31, face41, face51 modules for corner truncation. Then there are cube and cube1 modules which basically call the face modules. They are used to create a cube function. Other module is the keyboard key handling module which decides actions based on key presses.

CONTROLS:-
KEY			ACTION
a				Increments press wrt mode which in turn truncates the cube.
A				Undos the truncation done by 'a' (decrements press)

s				Switch mode between triangle and rectangle truncation

z				Rotates the cube wrt x-axis
Z				Same action as Z but in opposite direction
x				Rotates the cube wrt y-axis
X				Same action as X but in opposite direction
c				Rotates the cube wrt z-axis
C				Same action as C but in opposite direction

Esc				Quits the program and closes the display window
