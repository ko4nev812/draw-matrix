# Drawing on a matrix #

## What is this? ##
The module allows you to create a symbolic matrix and draw different lines on it, after which you can convert the drawn lines into a beautiful structure.

## Quick Guide ##

Drawing a simple, beautiful line:

    
    my_picture = Сanvas_matrix(10,10)
    my_picture.makeline(1, 1, 8, 9)
    my_picture.beautify()
    my_picture.pt()



----------


### Using ###


Using the library is as simple and convenient as possible:

Let's import it first:
First, import everything from the library (use the `from `...` import *` construct).

To start working with the module, you need to create an object with the class `Canvas_matrix`, in this case we are creating a 10 by 10 matrix filled with spaces:

	my_picture = Сanvas_matrix(10,10," ")

This class has several methods that will help you master this library:

`.pt()` - prints the entire matrix, if pt = True, the garden will be printed after printing for the next print:


	my_picture.pt(pt = False)

`.makeline(x1, y1, x2, y2)` - draws a line at two points, the coordinates start at 1, that is, the coordinate at the upper left point will be `[0,0]`

	my_picture.makeline(1, 1, 8, 9)

`.point(x, y, r)` - draws a point in x, y coordinates with the same width and height r:

	my_picture.point(5, 7, 2)

`.local_draw` - stores the coordinates of the local drawing, you no longer need to count the coordinates from the origin, but only from the beginning of the local coordinates:

	my_picture.local_draw = [x, y]

`.beautify()` - Transforms a boring picture from identical symbols into a beautiful picture with different symbols:

	my_picture.beautify()

an example of drawing a simple picture:

	t = Сanvas_matrix(10,25)
    t.local_draw = [7,0]
    t.makeline(0, 0, 4, 2)
    t.makeline(20, 2)
    t.makeline(25, -1)
    t.local_draw = [2,4]
    t.point(0,0)
    t.point(10,-1)
    t.beautify()
    t.pt(False)

