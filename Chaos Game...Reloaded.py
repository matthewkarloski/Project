######################################################################################################################
# Name: Matthew Karloski
# Date: 11/2/18
# Description:  this programming assignment is to implement a coordinate system class using the
#               Tkinter Python library that will enable plotting points graphically
#               in different fractal patterns imported from the Fractals file. Me, Dawson, and
#               Asia worked on this together
######################################################################################################################
from Tkinter import *
from random import randint
import math
from Fractals import *
# the 2D point class
class Point(object):
    def __init__(self, x_value = 0.0, y_value = 0.0):
        self.x_value = x_value
        self.y_value = y_value
        
    @property
    def x_value(self):
        return self._x_value

    @x_value.setter
    def x_value(self, value):
        self._x_value = value

    @property
    def y_value(self):
        return self._y_value

    @y_value.setter
    def y_value(self, value):
        self._y_value = value

    def dist(self, other):
        #put the distance formula in for 2 points
        d = math.sqrt(((self.x_value - other.x_value)**2) + ((self.y_value - other.y_value)**2))
        return d

    def midpt(self, other):
        #put the midpoint formula in for 2 points and have it return a point
        midpoint = Point((self.x_value + other.x_value)/2, (self.y_value + other.y_value)/2)
        return midpoint

    def __str__(self):
        s = "({}, {})".format(self.x_value, self.y_value)
        return s

# the chaos game class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class ChaosGame(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill = BOTH, expand = 1)
        self.vertex_radius = 2
        self.vertex_color = "red"
        #set the radius of all the points to 0
        self.point_radius = 0
        #create the list of colors that we need to use for the points
        self.point_color = ["black", "green", "blue", "cyan", "yellow", "magenta"]
        self.dimensions = {"min_x" : 2, "min_y" : 2, "max_x" : 594, "max_y" : 514}
        self.dimensions["mid_x"] = ((self.dimensions["min_x"] + self.dimensions["max_x"]) / 2)
        self.dimensions["mid_y"] = ((self.dimensions["min_y"] + self.dimensions["max_y"]) / 2)
    def make(self, name):
        if (name == "SierpinskiTriangle"):
            s = SierpinskiTriangle(Canvas)

            #plot vertices
            v = 0
            for i in s.vertices:
                self.plot_point(s.vertices[v], self.vertex_color, self.vertex_radius)
                v += 1
            onePoint = s.vertices[0].interpt(s.vertices[1], s.r)

            #plot first point
            self.plot_point(onePoint, self.point_color[randint(0,5)], self.point_radius)

            #plot rest of the points
            for i in range(s.num_points-1):
                onePoint = onePoint.interpt(s.vertices[randint(0,2)], s.r)
                self.plot_point(onePoint, self.point_color[randint(0,5)], self.point_radius)

        elif (name == "SierpinskiCarpet"):
            s = SierpinskiCarpet(Canvas)

            #plot vertices
            v = 0
            for i in s.vertices:
                self.plot_point(s.vertices[v], self.vertex_color, self.vertex_radius)
                v += 1

            #plot first point
            onePoint = s.vertices[0].interpt(s.vertices[1], s.r)
            self.plot_point(onePoint, self.point_color[randint(0,5)], self.point_radius)

            #plot rest of the points
            for i in range(s.num_points-1):
                onePoint = onePoint.interpt(s.vertices[randint(0,7)], s.r)
                self.plot_point(onePoint, self.point_color[randint(0,5)], self.point_radius)

        elif (name == "Pentagon"):
            s = Pentagon(Canvas)

            #plot vertices
            v = 0
            for i in s.vertices:
                self.plot_point(s.vertices[v], self.vertex_color, self.vertex_radius)
                v += 1

            #plot first point
            onePoint = s.vertices[0].interpt(s.vertices[1], s.r)
            self.plot_point(onePoint, self.point_color[randint(0,5)], self.point_radius)

            #plot rest of the points
            for i in range(s.num_points-1):
                onePoint = onePoint.interpt(s.vertices[randint(0,4)], s.r)
                self.plot_point(onePoint, self.point_color[randint(0,5)], self.point_radius)

        elif (name == "Hexagon"):
            s = Hexagon(Canvas)

            #plot vertices
            v = 0
            for i in s.vertices:
                self.plot_point(s.vertices[v], self.vertex_color, self.vertex_radius)
                v += 1

            #plot first point
            onePoint = s.vertices[0].interpt(s.vertices[1], s.r)
            self.plot_point(onePoint, self.point_color[randint(0,5)], self.point_radius)

            #plot rest of the points
            for i in range(s.num_points-1):
                onePoint = onePoint.interpt(s.vertices[randint(0,5)], s.r)
                self.plot_point(onePoint, self.point_color[randint(0,5)], self.point_radius)

        elif (name == "Octagon"):
            s = Octagon(Canvas)

            #plot vertices
            v = 0
            for i in s.vertices:
                self.plot_point(s.vertices[v], self.vertex_color, self.vertex_radius)
                v += 1

            #plot first point
            onePoint = s.vertices[0].interpt(s.vertices[1], s.r)
            self.plot_point(onePoint, self.point_color[randint(0,5)], self.point_radius)

            #plot rest of the points
            for i in range(s.num_points-1):
                onePoint = onePoint.interpt(s.vertices[randint(0,7)], s.r)
                self.plot_point(onePoint, self.point_color[randint(0,5)], self.point_radius)



    def plot_point(self, point, ptcolor, ptradius):
        

        #make the vertices, plot them, and put them in a list
        self.create_oval(point.x, point.y, point.x + ptradius * 2, point.y + ptradius * 2, outline= ptcolor, fill= ptcolor)
        
##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 800x800
WIDTH = 600
HEIGHT = 520

#the implemented fractals
FRACTALS = ["SierpinskiTriangle", "SierpinskiCarpet", "Pentagon", "Hexagon", "Octagon"]

#create the fractals in individual (sequencial) windows
for f in FRACTALS:
    # create the window
    window = Tk()
    window.geometry("{}x{}".format(WIDTH, HEIGHT))
    window.title("The Chaos Game...Reloaded")
    # create the chaos game as a Tkinter canvas inside the window
    s = ChaosGame(window)
    # plot some random points
    s.make(f)
    # wait for the window to close
    window.mainloop()
